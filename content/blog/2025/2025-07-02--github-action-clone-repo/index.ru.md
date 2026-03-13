---
title: "github action при клонировании репозитория"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-02T11:36:00+03:00
lastmod: 2025-07-02T11:53:00+03:00
tags: ["programming"]
categories: ["computer-science"]
draft: false
slug: "github-action-clone-repo"
---

github action при клонировании репозитория.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Задача {#задача}

-   Необходимо было править файл `package.json` при клонировании репозитория.


## <span class="section-num">2</span> Вариант решения {#вариант-решения}

-   Создал каталог для файлов Actions:
    ```shell
    mkdir -p .github/workflows
    ```
-   Файл для описания клонирования назвал `clone.yaml`:
    ```shell
    touch .github/workflows/clone.yaml
    ```


## <span class="section-num">3</span> Содержание файла {#содержание-файла}

```yaml
name: Replace data in package.json
# У меня получилось использовать только триггер push.
on: push

permissions:
  contents: write

jobs:
  run-script:
    name: replace data

    # Пропускаем, если у нас репозиторий-шаблон.
    # Проверяем, что у нас первый коммит (только склонировали репозиторий).
    # We will only run this action when this repository isn't the template repository
    if: >-
      ${{ !github.event.repository.is_template && github.run_number == 1 }}

    runs-on: ubuntu-latest
    steps:
      - name: Configure Git
        run: |
          git config --global user.name "${GITHUB_ACTOR}"
          git config --global user.email "${GITHUB_ACTOR_EMAIL}"
        shell: bash

      - name: Checkout repository
        uses: actions/checkout@v3

        # Редактируем файл package.json
        # Заменяем версию на 1.0.0
      - name: Replace version
        run: |
          sed -i "s/\"version\": \".*\"/\"version\": \"1.0.0\"/" package.json
      - name: Replace name and email
        run: |
          sed -i "s/\"author\": \".*\"/\"author\": \"${{ github.actor }}\"/" package.json
      - name: Replace repository
        run: |
          sed -i "s|\"repository\": \".*\"|\"repository\": \"${{ github.repositoryUrl }}\"|" package.json

      - name: Commit changes
        run: |
          git add package.json
          git commit -m "Replace data in package.json"

      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: master
```
