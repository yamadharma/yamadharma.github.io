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
