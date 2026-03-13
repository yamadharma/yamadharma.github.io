#!/usr/bin/env bash

# Refactor a page named `X.md` to `content/<section>/X/index.md` to use the
# new page bundles and featured image system
#
# - E.g. a post `content/post/X.md` is converted to `content/post/X/index.md`

refactor_pages_to_page_bundles_ru()
{
  # Check that the command was run from the site root.
  if [ ! -d ./content/ru/ ]; then
    echo "Please run the script from the root folder of your site" >&2
    exit 1
  fi
  # Iterate over pages except index.md and _index.md.
  local files="$(find ./content/ru/ -iname '*.md' -not -iname '*index.md')"
  for file in ${files}; do
    local pagedir="${file%.md}"

    echo "${file} -> ${pagedir}/index.ru.md"
    if [ ! -d "${pagedir}" ]; then
      mkdir "${pagedir}"
    fi

    mv "${file}" "${pagedir}/index.ru.md"
  done
}

# Bash Strict Mode
set -eu

# To debug, uncomment line below:
set -x
refactor_pages_to_page_bundles_ru "$@"
