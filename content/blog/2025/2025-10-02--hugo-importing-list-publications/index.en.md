---
title: "Hugo. Researcher's website. Importing a list of publications"
author: ["Dmitry S. Kulyabov"]
date: 2025-10-02T15:57:00+03:00
lastmod: 2025-10-05T20:29:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "hugo-importing-list-publications"
---

Hugo. Researcher's website. Importing a list of publications

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Importer {#importer}

-   Uses the `academic` package.
-   PyPi: <https://pypi.org/project/academic/>
-   Repository: <https://github.com/BuildLore/academic-file-converter>
-   This tool automatically generates publication pages for Hugo-based sites (e.g., Wowchemy), including books, articles, and preprints.
-   Supports media file integration (PDF, images) and metadata customization.


### <span class="section-num">1.1</span> Installation {#installation}

```shell
pipx install academic
```


### <span class="section-num">1.2</span> Usage {#usage}

```shell
academic import my_publications.bib content/publication/
```


## <span class="section-num">2</span> Fixes for Hugo-blox {#fixes-for-hugo-blox}

-   The file structure has changed in hugo-blox.


### <span class="section-num">2.1</span> Format update using the DOI field as an example {#format-update-using-the-doi-field-as-an-example}

-   Previously, the DOI was specified at the top level of the YAML file, but now it must be placed in the `hugoblox.ids` section.

-   Old format:

<!--listend-->

```yaml
doi: 10.1038/s41586-023-06900-0
```

-   New format:

<!--listend-->

```yaml
hugoblox:
ids:
doi: 10.1038/s41586-023-06900-0
```

-   Similar for other identifiers (PubMed, arXiv, etc.):

<!--listend-->

```yaml
hugoblox:
ids:
doi: 10.1038/s41586-023-06900-0
pubmed: 12345678
arxiv: 2301.12345v1
```


### <span class="section-num">2.2</span> Fix script {#fix-script}

-   Created a fix script (`bib-hugoblox-fix.py`):
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
-   Launch:

<!--listend-->

```shell
python hugoblox_migrator.py --directory content/my_publications/
```

-   Options:
-   `--directory` : directory path (default: content/publications/);
-   `--no-backup` : disable backups.

-   The script will automatically process all `.md` files in the specified directory and its subdirectories.


## <span class="section-num">3</span> General script {#general-script}

-   My script for transferring bibliography (`scripts/bib.sh`):

<!--listend-->

```shell
#!/usr/bin/env bash

# pipx install academic

DIR=$(pwd)

academic import ~/work/bib/bib/mine.bib content/ru/publication --compact --overwrite --verbose

cd ${DIR}/content/en/publication
find . -xtype l -delete
ln -s ../../ru/publication/* .
grep -r russian * | cut -f1 -d":" | xargs -r dirname | xargs -r rm

cd ${DIR}

./scripts/bib-hugoblox-fix.py --directory content/ru/publication/ --no-backup
```
