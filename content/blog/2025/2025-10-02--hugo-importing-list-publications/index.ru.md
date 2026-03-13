---
title: "Hugo. Сайт научника. Импорт списка публикаций"
author: ["Dmitry S. Kulyabov"]
date: 2025-10-02T15:57:00+03:00
lastmod: 2026-03-10T14:26:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "hugo-importing-list-publications"
---

Hugo. Сайт научника. Импорт списка публикаций.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Программа для импорта {#программа-для-импорта}

-   [Hugo. Шаблон для научных работников. Библиография]({{< relref "2025-01-08--hugo-template-for-scientists-bibliography" >}})
-   Используется пакет `academic`.
-   PyPi: <https://pypi.org/project/academic/>
-   Репозиторий: <https://github.com/BuildLore/academic-file-converter>
-   Инструмент позволяет автоматически генерировать страницы публикаций для сайтов на базе Hugo (например, Wowchemy), включая книги, статьи и препринты.
-   Поддерживает интеграцию медиафайлов (PDF, изображения) и настройку метаданных.


### <span class="section-num">1.1</span> Установка {#установка}

```shell
pipx install academic
```


### <span class="section-num">1.2</span> Использование {#использование}

```shell
academic import my_publications.bib content/publication/
```


## <span class="section-num">2</span> Исправления для Hugo-blox {#исправления-для-hugo-blox}

-   В hugo-blox изменилась структура файлов.


### <span class="section-num">2.1</span> Обновление формата на примере поля DOI {#обновление-формата-на-примере-поля-doi}

-   Раньше DOI указывался на верхнем уровне YAML-файла, но теперь его нужно поместить в секцию `hugoblox.ids`.

-   Старый формат:

<!--listend-->

```yaml
doi: 10.1038/s41586-023-06900-0
```

-   Новый формат:

<!--listend-->

```yaml
hugoblox:
  ids:
    doi: 10.1038/s41586-023-06900-0
```

-   Аналогично для других идентификаторов (PubMed, arXiv и т.д.):

<!--listend-->

```yaml
hugoblox:
  ids:
    doi: 10.1038/s41586-023-06900-0
    pubmed: 12345678
    arxiv: 2301.12345v1
```


### <span class="section-num">2.2</span> Переименование по языку {#переименование-по-языку}

-   Чтение языка из `cite.bib`
    -   Добавлена функция `get_language_from_bib()`, которая ищет поле `language`  в bib-файле с помощью регулярного выражения.
    -   Извлечённое значение передаётся в `normalize_language()` для преобразования в двухбуквенный код (поддерживаются полные названия вроде `russian` → `ru` ).
-   Переименование только для `index.md`
    -   Функция `rename_by_language()` срабатывает только если имя файла --- `index.md`  (без суффикса).
    -   Если целевой файл `index.{lang}.md`  уже существует, он либо получает бэкап ( `.bak`), либо удаляется (в зависимости от флага `--no-backup` ).
-   Интеграция в основной процесс
    -   В `process_file()` сначала выполняется миграция полей (как в исходном скрипте), затем --- переименование, если включён флаг `--rename`  (по умолчанию включён).
    -   Добавлен аргумент `--no-rename` , чтобы отключить автоматическое переименование.
-   Скрипт ожидает, что в каждой папке с публикацией есть файл `cite.bib` с полем `language`.
-   Для корректного определения языка добавлен словарь `LANG_MAP`. Вы можете дополнить его своими вариантами.
-   Если в папке уже есть несколько языковых файлов (например, `index.ru.md` и `index.en.md`), скрипт обработает только `index.md` . Остальные останутся без изменений.


### <span class="section-num">2.3</span> Удаление keywords {#удаление-keywords}

-   По умолчанию `keywords` преобразуются в `tags`.
-   Но нам нужны только проекты (типа `project:projectname`).
-   Остальные `keywords` нам не нужны.
-   Скрипт ожидает, что в папке каждой публикации есть файл `cite.bib` . Если его нет, обработка keywords пропускается.
-   Keywords должны быть разделены запятыми (стандарт BibTeX). Поддерживаются многострочные значения (флаг `re.DOTALL`).
-   Префикс `project:` проверяется без учёта регистра. После двоеточия может быть произвольный текст (название проекта), который и попадёт в список `projects`.
-   Функция `extract_projects_from_bib` возвращает только список проектов (из keywords с префиксом `project:` ). Остальные `keywords` игнорируются.
-   В `process_file` после миграции:
    -   Удаляется поле `tags`  (если оно есть).
    -   Обновляется поле `projects` в соответствии с извлечённым списком (если список не пуст, добавляется; если пуст и поле существовало --- удаляется).
    -   При любом изменении данных (projects или удаление tags) пересобирается YAML-фронтматтер и сохраняется файл.


### <span class="section-num">2.4</span> Скрипт для исправления {#скрипт-для-исправления}

-   Сделал скрипт для исправления (`bib-hugoblox-fix.py`):
    ```python
    #!/usr/bin/env python

    import os
    import re
    import yaml
    from pathlib import Path
    import argparse

    FIELDS_MAPPING = {
        "doi": "hugoblox.ids.doi",
        "pubmed": "hugoblox.ids.pubmed",
        "arxiv": "hugoblox.ids.arxiv",
        "isbn": "hugoblox.ids.isbn",
        "pmc": "hugoblox.ids.pmc",
        "patent": "hugoblox.ids.patent",
    }

    # Карта для нормализации названий языков (полные -> двухбуквенные коды)
    LANG_MAP = {
        "russian": "ru",
        "english": "en",
        "german": "de",
        "french": "fr",
        "spanish": "es",
        "chinese": "zh",
        "japanese": "ja",
        # добавьте при необходимости
    }


    def normalize_language(lang):
        """Преобразует полное название языка в двухбуквенный код ISO 639-1."""
        if not lang:
            return None
        lang = lang.strip().lower()
        # Если уже двухбуквенный код (en, ru и т.п.)
        if re.match(r"^[a-z]{2}$", lang):
            return lang
        # Ищем в карте
        return LANG_MAP.get(lang)


    def get_language_from_bib(bib_path):
        """Извлекает язык из поля language в cite.bib."""
        if not os.path.exists(bib_path):
            return None
        with open(bib_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Ищем поле language = {value} или language = "value"
        match = re.search(r'language\s*=\s*[{"](\w+)[}"]', content, re.IGNORECASE)
        if match:
            return normalize_language(match.group(1))
        return None


    def extract_projects_from_bib(bib_path):
        """
        Извлекает из поля keywords cite.bib только те слова,
        которые начинаются с 'project:', и возвращает список названий проектов.
        Остальные keywords игнорируются.
        """
        projects = []
        if not os.path.exists(bib_path):
            return projects
        with open(bib_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Ищем поле keywords = { ... }
        match = re.search(r"keywords\s*=\s*[{](.+?)[}]", content, re.IGNORECASE | re.DOTALL)
        if not match:
            return projects
        keywords_str = match.group(1)
        # Разделяем по запятой (возможны пробелы после запятой)
        raw_keywords = [kw.strip() for kw in keywords_str.split(",")]
        for kw in raw_keywords:
            if not kw:
                continue
            if kw.lower().startswith("project:"):
                parts = kw.split(":", 1)
                if len(parts) > 1:
                    project_name = parts[1].strip()
                    if project_name:
                        projects.append(project_name)
        return projects


    def migrate_fields(content):
        """Миграция полей внутри одного файла (без изменений)"""
        yaml_regex = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
        match = yaml_regex.search(content)
        if not match:
            return content, None

        frontmatter = match.group(1)
        data = yaml.safe_load(frontmatter)
        if not data:
            return content, data

        modified = False
        hugoblox = data.get("hugoblox", {})

        # Обработка стандартных полей
        for old_field, new_path in FIELDS_MAPPING.items():
            if old_field in data:
                value = data[old_field]
                hugoblox_parts, *path_parts, field_name = new_path.split(".")
                current = hugoblox
                for part in path_parts:
                    current = current.setdefault(part, {})
                current[field_name] = value
                del data[old_field]
                modified = True

        # Обработка url_pdf, url_video
        for url_field, link_type in [("url_pdf", "pdf"), ("url_video", "video")]:
            if url_field in data:
                url = data[url_field]
                links = hugoblox.get("links", [])
                if not any(link.get("type") == link_type for link in links):
                    links.append({"type": link_type, "url": url})
                    hugoblox["links"] = links
                del data[url_field]
                modified = True

        if modified:
            if "hugoblox" in data:
                data["hugoblox"].update(hugoblox)
            else:
                data["hugoblox"] = hugoblox

            new_frontmatter = yaml.dump(
                data, allow_unicode=True, sort_keys=False, width=float("inf")
            )
            return content.replace(frontmatter, new_frontmatter, 1), data

        return content, data


    def process_file(file_path, backup=True, rename_lang=True):
        dir_name = os.path.dirname(file_path)
        bib_path = os.path.join(dir_name, "cite.bib")

        # Читаем текущее содержимое .md
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Миграция полей (из старого формата в новый)
        new_content, data = migrate_fields(content)
        modified = content != new_content

        # Обработка keywords из cite.bib: извлекаем только проекты
        projects = extract_projects_from_bib(bib_path)

        # Обновляем данные: projects и удаляем tags
        if projects:
            data["projects"] = projects
        elif "projects" in data:
            del data["projects"]  # удаляем, если был, но теперь пусто

        # Удаляем tags полностью (независимо от наличия keywords)
        if "tags" in data:
            del data["tags"]
            modified = True

        # Если projects изменились (добавились/удалились), тоже нужно отметить modified
        if projects or "projects" in data:  # если projects не пуст или был удалён
            modified = True

        # Если были изменения в данных, пересобираем фронтматтер
        if modified:
            yaml_regex = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
            match = yaml_regex.search(new_content)
            if match:
                new_frontmatter = yaml.dump(
                    data, allow_unicode=True, sort_keys=False, width=float("inf")
                )
                new_content = new_content.replace(match.group(1), new_frontmatter, 1)

            # Сохраняем файл
            if backup:
                backup_path = f"{file_path}.bak"
                Path(file_path).rename(backup_path)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
            else:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
            print(f"Обновлён: {file_path}")

        # Переименование по языку (если нужно)
        renamed = False
        if rename_lang:
            lang = get_language_from_bib(bib_path)
            if lang:
                base_name = os.path.basename(file_path)
                if base_name == "index.md":
                    new_name = f"index.{lang}.md"
                    new_path = os.path.join(dir_name, new_name)
                    if os.path.exists(new_path):
                        if backup:
                            backup_existing = f"{new_path}.bak"
                            os.rename(new_path, backup_existing)
                        else:
                            os.remove(new_path)
                    os.rename(file_path, new_path)
                    print(f"Переименован: {file_path} -> {new_path}")
                    renamed = True

        return modified or renamed


    def process_directory(directory="content/publications/", backup=True, rename_lang=True):
        modified_files = []

        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".md"):
                    full_path = os.path.join(root, file)
                    if process_file(full_path, backup, rename_lang):
                        modified_files.append(full_path)

        print(f"Обработка завершена. Файлы с изменениями: {len(modified_files)}")
        for path in modified_files:
            print(f" - {path}")


    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description="Миграция полей, извлечение проектов из keywords и переименование по языку для Hugo-Blox"
        )
        parser.add_argument(
            "--directory",
            "-d",
            default="content/publications/",
            help="Путь к директории с публикациями",
        )
        parser.add_argument(
            "--no-backup",
            action="store_false",
            dest="backup",
            help="Отключить создание резервных копий",
        )
        parser.add_argument(
            "--no-rename",
            action="store_false",
            dest="rename_lang",
            help="Отключить автоматическое переименование по языку",
        )

        args = parser.parse_args()
        process_directory(args.directory, args.backup, args.rename_lang)
    ```
-   Запуск:
    ```shell
    python hugoblox_migrator.py --directory content/my_publications/
    ```
-   Опции:
    -   `--directory` : путь к каталогу (по умолчанию: content/publications/);
    -   `--no-backup` : отключить создание резервных копий.

-   Скрипт автоматически обработает все `.md` файлы в указанной директории и её поддиректориях.


## <span class="section-num">3</span> Общий скрипт {#общий-скрипт}

-   Мой скрипт для переноса библиографии (`scripts/bib.sh`):
    ```shell
    #!/usr/bin/env bash

    # pipx install academic


    DIR=$(pwd)

    academic import ~/work/bib/bib/mine.bib content/publications --compact --overwrite --verbose

    # cd ${DIR}/content/en/publications
    # find . -xtype l -delete
    # ln -s ../../ru/publications/* .
    # grep -r russian * | cut -f1 -d":" | xargs -r dirname | xargs -r rm

    # cd ${DIR}

    ./scripts/bib-hugoblox-fix.py --directory content/publications/ --no-backup
    ```
