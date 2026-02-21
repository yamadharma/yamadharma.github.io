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
