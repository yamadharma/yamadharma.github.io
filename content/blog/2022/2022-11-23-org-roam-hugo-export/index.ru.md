---
title: "Org-roam. Экспорт в Hugo"
author: ["Dmitry S. Kulyabov"]
date: 2022-11-23T19:40:00+03:00
lastmod: 2026-03-10T20:06:00+03:00
tags: ["hugo", "org-mode", "org-roam"]
categories: ["computer-science"]
draft: false
slug: "org-roam-hugo-export"
---

Экспорт в Hugo из org-roam.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Базируется на пакете ox-hugo (см. [Org-mode. Экспорт в Hugo]({{< relref "2020-12-17-org-mode-export-hugo" >}})).


## <span class="section-num">2</span> Ошибки при экспорте {#ошибки-при-экспорте}


### <span class="section-num">2.1</span> ox-hugo: broken links {#ox-hugo-broken-links}


#### <span class="section-num">2.1.1</span> Подкаталоги в каталоге org-roam {#подкаталоги-в-каталоге-org-roam}

-   Если каталог для org-roam содержит подкаталоги, то при экспорте теряются ссылки.
-   Для ликвидации этой ошибки следует добавить в настройки:
    ```emacs-lisp
    (require 'org-roam-export)
    ```


#### <span class="section-num">2.1.2</span> Экспорт из поддерева {#экспорт-из-поддерева}

-   ox-hugo предлагает два варианта экспорта:
    -   экспорт всего файла;
    -   экспорт из поддерева.
-   При экспорте из поддерева ссылки типа `id_link` не отображаются.
-   Происходит поиск таких ссылок только в текущем поддереве.
-   Для реализации поиска в других фалах нужно добавить их в переменную `org-id-extra-files`:
    ```emacs-lisp
    (setq org-id-extra-files (directory-files-recursively org-roam-directory ".*\.org$" t))
    ```

    -   Впрочем, у меня это не сработало.
-   Также можно сделать хак для игнорирования ошибок:
    ```emacs-lisp
    (with-eval-after-load 'ox-hugo
      (setq org-hugo--preprocess-buffer nil))
    ```

    -   Вот это у меня сработало.


## <span class="section-num">3</span> Миграция на hugo page bundle {#миграция-на-hugo-page-bundle}

-   [Hugo. Использование page bundle]({{< relref "2026-03-03--hugo-page-bundle" >}})


### <span class="section-num">3.1</span> Свойства для экспорта {#свойства-для-экспорта}

-   Пример задания свойств для экспорта:
    ```org
    :PROPERTIES:
    :export_hugo_section: blog/2026
    :export_hugo_bundle: 2026-03-03--hugo-multilingual-support
    :export_file_name: index.ru.md
    :export_language: ru
    :END:
    ```

-   При экспорте будет создана структура:
    ```shell
    content/
    └── blog/
        └── 2026/
            └── 2026-03-03--hugo-multilingual-support/    <-- папка бандла
                ├── index.ru.md
                ├── index.en.md (для английской версии)
                └── (ресурсы)
    ```

-   `export_hugo_section: blog/2026` : задаёт путь к разделу (секции) внутри `content/`. Это может быть вложенная структура, например `blog/2026` создаст папки `blog/2026`.
-   `export_hugo_bundle: 2026-03-03--hugo-multilingual-support` : определяет имя папки самого бандла. Она будет создана внутри указанной секции.
-   `export_file_name: index.ru.md` : имя файла внутри бандла. Для листового бандла обязательно должно быть `index`. Если не добавить расширение `.md`, ox-hugo обрежет до `index`.
-   `export_language: ru` : явно указывает язык.

-   Для английской версии этого же поста создаётся отдельная секция с такими же `export_hugo_section` и `export_hugo_bundle`, но с `export_file_name: index.en.md` и `export_language: en`.


### <span class="section-num">3.2</span> Скрипт для миграции {#скрипт-для-миграции}


#### <span class="section-num">3.2.1</span> Что делает {#что-делает}

-   Находит все блоки `:PROPERTIES:` в `.org` файлах.
-   Извлекает значения `EXPORT_HUGO_SECTION` и `EXPORT_FILE_NAME`.
-   Определяет язык по префиксу `ru/` или `en/` в секции.
-   Формирует новые свойства:
    -   `export_hugo_section` (без языкового префикса)
    -   `export_hugo_bundle` (старое значение `EXPORT_FILE_NAME`)
    -   `export_file_name: index.ru.md` (или `index.en.md`)
    -   `export_language: ru` (или `en`)
-   Все ключи приводит к **нижнему регистру** (как вы просили).
-   Сохраняет остальные свойства без изменений.
-   Перезаписывает блок свойств в файле, создавая резервную копию (`.bak`).


#### <span class="section-num">3.2.2</span> Использование {#использование}

-   Сохраните скрипт в файл, например `migrate_org_props.py`.
-   Отредактируйте переменную `root_dir` в начале скрипта, указав путь к корневой папке с вашими org-файлами.
-   Убедитесь, что `dry_run = True` (режим просмотра без изменений).
-   Запустите скрипт: `python3 migrate_org_props.py`.
-   Просмотрите вывод. Для каждого файла, где будут найдены подходящие свойства, появится сообщение `[DRY RUN] Будет изменён: ...`. Также для каждого изменяемого блока будет показан фрагмент старого блока.
-   Если всё выглядит правильно, установите `dry_run = False` и запустите скрипт снова.
-   После завершения проверьте несколько файлов вручную и запустите `hugo server` для проверки сайта.


#### <span class="section-num">3.2.3</span> Скрипт {#скрипт}

```python
#!/usr/bin/env python3
"""
Преобразование org-свойств для многоязычных page bundle.
Ищет блоки :PROPERTIES:, содержащие EXPORT_HUGO_SECTION и EXPORT_FILE_NAME,
и преобразует их в формат page bundle с языковыми суффиксами.
Все ключи свойств приводятся к нижнему регистру.
"""

import os
import re
import sys
from pathlib import Path

# ====== НАСТРОЙКИ ======
root_dir = "/путь/к/вашим/org-файлам"   # <--- ИЗМЕНИТЕ ЭТО
dry_run = True                          # При True только просмотр, без записи
# =======================

# Регулярка для поиска блоков свойств
prop_block_re = re.compile(
    r'^(\s*):PROPERTIES:\s*\n(.*?)^\s*:END:\s*$',
    re.MULTILINE | re.DOTALL | re.IGNORECASE
)

# Регулярка для строк свойств
prop_line_re = re.compile(r'^\s*:([^:]+?):\s*(.*?)\s*$', re.MULTILINE)

def transform_properties(prop_text):
    """
    Преобразует текст внутри блока свойств.
    Возвращает новый текст или исходный, если преобразование не требуется.
    """
    # Собираем все текущие свойства, ключи приводим к нижнему регистру
    props = {}
    for match in prop_line_re.finditer(prop_text):
        key = match.group(1).strip()
        value = match.group(2).strip()
        props[key.lower()] = value

    # Проверяем наличие необходимых свойств
    if 'export_hugo_section' not in props or 'export_file_name' not in props:
        return prop_text

    section = props['export_hugo_section']
    old_filename = props['export_file_name']

    # Определяем язык по префиксу ru/ или en/
    lang = None
    if section.lower().startswith('ru/'):
        lang = 'ru'
        new_section = section[3:]   # убираем 'ru/'
    elif section.lower().startswith('en/'):
        lang = 'en'
        new_section = section[3:]   # убираем 'en/'
    else:
        # Нет языкового префикса – пропускаем
        return prop_text

    # Обновляем свойства
    props['export_hugo_section'] = new_section
    props['export_hugo_bundle'] = old_filename
    props['export_file_name'] = f"index.{lang}.md"
    props['export_language'] = lang

    # Сортируем ключи для стабильности порядка
    sorted_keys = sorted(props.keys())

    # Формируем текст свойств
    lines = [f":{key}: {props[key]}" for key in sorted_keys]
    return "\n".join(lines)

def process_file(filepath):
    """Обрабатывает один .org файл."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    modified = False

    # Ищем все блоки свойств и обрабатываем каждый
    for match in prop_block_re.finditer(content):
        old_block = match.group(0)
        indent = match.group(1)      # отступ перед :PROPERTIES:
        prop_text = match.group(2)

        new_prop_text = transform_properties(prop_text)
        if new_prop_text != prop_text:
            # Восстанавливаем блок с тем же отступом
            new_block = f"{indent}:PROPERTIES:\n{new_prop_text}\n{indent}:END:"
            new_content = new_content.replace(old_block, new_block)
            modified = True
            # Показываем фрагмент старого блока для информации
            print(f"    Будет изменён блок: {old_block[:80]}...")

    if modified:
        if dry_run:
            print(f"[DRY RUN] Будет изменён: {filepath}")
        else:
            # Создаём резервную копию с расширением .bak
            backup = filepath.with_suffix(filepath.suffix + '.bak')
            if not backup.exists():
                os.rename(filepath, backup)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Изменён: {filepath}")
    else:
        if dry_run:
            print(f"[DRY RUN] Без изменений: {filepath}")

def main():
    if dry_run:
        print("*** РЕЖИМ ПРОСМОТРА – файлы не будут изменены ***\n")
    else:
        print("*** РЕЖИМ ЗАПИСИ – файлы будут изменены ***\n")

    base = Path(root_dir).expanduser().resolve()
    if not base.is_dir():
        print(f"Ошибка: директория {base} не существует.")
        sys.exit(1)

    org_files = list(base.rglob("*.org"))
    print(f"Найдено .org файлов: {len(org_files)}")
    for org_file in org_files:
        process_file(org_file)

    if dry_run:
        print("\n*** ПРОСМОТР ЗАВЕРШЁН. Для применения изменений установите dry_run=False. ***")

if __name__ == "__main__":
    main()
```
