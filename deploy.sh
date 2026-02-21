#!/usr/bin/env bash
# If a command fails then the deploy stops
set -e

rm -rvf static/ltximg

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

# Build the project.
hugo --minify --gc

npm_config_yes=true npx pagefind --site "public" --output-subdir ../static/pagefind
# pnpm run pagefind --site "public" --output-subdir ../static/pagefind

# Go To Public folder
cd public

# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site $(date)"
if [[ -n "$*" ]]
then
    msg="$*"
fi

git commit -am "$msg"

# Push source and build repos.
git push origin master
