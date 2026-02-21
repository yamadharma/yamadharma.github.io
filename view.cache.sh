#!/usr/bin/env bash

mkdir -p "$(pwd)/resources/hugo_cache"
export HUGO_CACHEDIR="$(pwd)/resources/hugo_cache"

hugo server --disableFastRender --i18n-warnings
