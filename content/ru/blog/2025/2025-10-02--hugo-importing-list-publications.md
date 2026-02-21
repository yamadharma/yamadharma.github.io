---
title: "Hugo. Сайт научника. Импорт списка публикаций"
author: ["Dmitry S. Kulyabov"]
date: 2025-10-02T15:57:00+03:00
lastmod: 2026-01-22T20:25:00+03:00
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


### <span class="section-num">2.2</span> Скрипт для исправления {#скрипт-для-исправления}

-   Сделал скрипт для исправления (`bib-hugoblox-fix.py`):
    ```python
    #!/usr/bin/env python

    import os
    import re
    import yaml
    from pathlib import Path
    import argparse

    FIELDS_MAPPING = {
        'doi': 'hugoblox.ids.doi',
        'pubmed': 'hugoblox.ids.pubmed',
        'arxiv': 'hugoblox.ids.arxiv',
        'isbn': 'hugoblox.ids.isbn',
        'pmc': 'hugoblox.ids.pmc',
        'patent': 'hugoblox.ids.patent'
    }

    def migrate_fields(content):
        yaml_regex = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
        match = yaml_regex.search(content)
        if not match:
            return content

        frontmatter = match.group(1)
        data = yaml.safe_load(frontmatter)
        if not data:
            return content

        modified = False
        hugoblox = data.get('hugoblox', {})

        ## Processing regular fields
        for old_field, new_path in FIELDS_MAPPING.items():
            if old_field in data:
                value = data[old_field]
                hugoblox_parts, *path_parts, field_name = new_path.split('.')

                current = hugoblox
                for part in path_parts:
                    current = current.setdefault(part, {})

                current[field_name] = value
                del data[old_field]
                modified = True

        ## Processing url_pdf, url_video
        for url_field, link_type in [('url_pdf', 'pdf'), ('url_video', 'video')]:
            if url_field in data:
                url = data[url_field]
                links = hugoblox.get('links', [])

                ## Check if a link of this type exists
                if not any(link.get('type') == link_type for link in links):
                    links.append({'type': link_type, 'url': url})
                    hugoblox['links'] = links
                    modified = True

                del data[url_field]
                modified = True

        if modified:
            ## Merge changes with existing hugoblox
            if 'hugoblox' in data:
                data['hugoblox'].update(hugoblox)
            else:
                data['hugoblox'] = hugoblox

            new_frontmatter = yaml.dump(data, allow_unicode=True, sort_keys=False, width=float("inf"))
            return content.replace(frontmatter, new_frontmatter, 1)

        return content

    def process_file(file_path, backup=True):
        with open(file_path, 'r') as f:
            content = f.read()

        new_content = migrate_fields(content)

        if content != new_content:
            if backup:
                backup_path = f"{file_path}.bak"
                Path(file_path).rename(backup_path)

            with open(file_path, 'w') as f:
                f.write(new_content)
            return True
        return False

    def process_directory(directory='content/publications/', backup=True):
        modified_files = []

        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    full_path = os.path.join(root, file)
                    if process_file(full_path, backup):
                        modified_files.append(full_path)

        print(f"Обработано файлов: {len(modified_files)}")
        for path in modified_files:
            print(f" - {path}")

    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description="Migrating fields in files Hugo-Blox")
        parser.add_argument('--directory', '-d', default='content/publications/',
                           help='Path to the publication directory')
        parser.add_argument('--no-backup', action='store_false', dest='backup',
                           help='Disable backup')

        args = parser.parse_args()
        process_directory(args.directory, args.backup)
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

    academic import ~/work/bib/bib/mine.bib content/ru/publications --compact --overwrite --verbose

    cd ${DIR}/content/en/publications
    find . -xtype l -delete
    ln -s ../../ru/publications/* .
    grep -r russian * | cut -f1 -d":" | xargs -r dirname | xargs -r rm

    cd ${DIR}

    ./scripts/bib-hugoblox-fix.py --directory content/ru/publications/ --no-backup
    ```
