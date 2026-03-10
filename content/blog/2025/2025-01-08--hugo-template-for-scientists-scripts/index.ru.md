---
title: "Hugo. Шаблон для научных работников. Полезные скрипты"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-08T20:29:00+03:00
lastmod: 2026-01-22T20:24:00+03:00
tags: ["hugo", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "hugo-template-for-scientists-scripts"
---

Hugo. Шаблон для научных работников. Полезные скрипты.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Просмотр сайта {#просмотр-сайта}

-   Удаление ненужных файлов (формул из emacs):
    ```shell
    rm static/ltximg/*
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      ~/work/blog/blog/view.sh
    </div>
-   Запускаем сайт для просмотра:
    ```shell
    hugo server --disableFastRender
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 2:</span>
      ~/work/blog/blog/view.sh
    </div>


## <span class="section-num">2</span> Публикация сайта {#публикация-сайта}

-   Скрипт:
    ```shell
    # If a command fails then the deploy stops
    set -e
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 3:</span>
      ~/work/blog/blog/deploy.sh
    </div>
-   Удаляем ненужные каталоги (чтобы они не попали на сайт):
    ```shell
    rm -rvf static/ltximg
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 4:</span>
      ~/work/blog/blog/deploy.sh
    </div>
-   Информационное сообщение:
    ```shell
    printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 5:</span>
      ~/work/blog/blog/deploy.sh
    </div>
-   Генерация сайта:
    ```shell
    # Build the project.
    hugo --minify
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 6:</span>
      ~/work/blog/blog/deploy.sh
    </div>
-   Создание индекса поиска:
    ```shell
    npm_config_yes=true npx pagefind --site "public" --output-subdir ../static/pagefind
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 7:</span>
      ~/work/blog/blog/deploy.sh
    </div>
-   Выкладывание на сайт:
    ```shell
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
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 8:</span>
      ~/work/blog/blog/deploy.sh
    </div>


## <span class="section-num">3</span> Создание списка публикаций {#создание-списка-публикаций}

-   [Hugo. Сайт научника. Импорт списка публикаций]({{< relref "2025-10-02--hugo-importing-list-publications" >}})
