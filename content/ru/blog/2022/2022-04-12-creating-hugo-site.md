---
title: "Создание сайта на Hugo"
author: ["Dmitry S. Kulyabov"]
date: 2022-04-12T20:49:00+03:00
lastmod: 2025-10-02T15:57:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "creating-hugo-site"
---

Быстрое развертывание сайта на GitHub Pages с помощью генератора статического html _Hugo_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Установка программного обеспечения для _Hugo_ {#установка-программного-обеспечения-для-hugo}


### <span class="section-num">1.1</span> Необходимое программное обеспечение {#необходимое-программное-обеспечение}

-   Необходим сам _hugo_.
-   Есть две сборки: _Hugo_ и _Hugo Extended_.
-   _Hugo Extended_ отличается от _Hugo_ поддержкой SASS/SCSS.
-   Часть тем (например, Wowchemy --- [Hugo. Шаблон для научных работников]({{< relref "2021-07-02-hugo-template-for-scientists" >}})) требует наличия _Hugo Extended_.
-   Поскольку hugo использует модули _golang_, то следует установить и его.
-   Также может понадобиться NodeJS.


### <span class="section-num">1.2</span> Установка в различных операционных системах {#установка-в-различных-операционных-системах}


#### <span class="section-num">1.2.1</span> Linux {#linux}

-   Ubuntu:
    ```shell
    sudo apt-get install go hugo
    ```
-   Fedora:
    ```shell
    sudo dnf install go hugo
    ```
-   Gentoo:
    ```shell
    emerge dev-lang/go net-libs/nodejs dev-vcs/git
    USE="sass" emerge www-apps/hugo
    ```


#### <span class="section-num">1.2.2</span> Windows {#windows}

-   Chocolatey:
    ```shell
    choco install hugo-extended git go nodejs
    ```
-   Scoop:
    ```shell
    scoop install hugo-extended git go nodejs
    ```


#### <span class="section-num">1.2.3</span> Ручная установка {#ручная-установка}

-   Если устанавливаемая в системе версия _hugo_ меньше необходимой, тогда следует установить программу вручную.
-   Версию _hugo_ можно посмотреть при помощи команды:
    ```shell
    hugo version
    ```
-   Следует скачать архив с репозитория: <https://github.com/gohugoio/hugo/releases>


### <span class="section-num">1.3</span> Видео: Программное обеспечение для Hugo {#видео-программное-обеспечение-для-hugo}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 2a5ee9132f0e65a635aa6f2c11150767 >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube OvfQBCEkJig >}}

{{< /rtab >}}
{{< /tabs >}}


## <span class="section-num">2</span> Структура сайта {#структура-сайта}

-   Будем считать, что сайт находится в локальном каталоге:
    ```shell
    ~/work/blog/blog
    ```
-   Структура сайта
    -   archetypes Каталог, содержащий шаблоны новых md-файлов, которые создаёт Hugo с помощью команды `hugo new`.
    -   config.toml Основной конфиг сайта
    -   content Каталог данных, из которых Hugo будет генерировать сайт
    -   data Каталог дополнительных данных, которые непосредственно не
        участвуют в генерации сайта
    -   docs Корень генерируемого сайта. Этот каталог не создается Hugo, мы
        его получили при заведении репозитория на GitHub и ниже мы его
        пропишем в файле config.toml
    -   layouts Содержит шаблоны сайта
    -   static Каталог для статических данных (изображения, CSS, JavaScript и
        т.д.)
    -   themes Каталог для тем оформления сайта


## <span class="section-num">3</span> Установка темы (внешнего вида) сайта {#установка-темы--внешнего-вида--сайта}


### <span class="section-num">3.1</span> Видео: Установка темы сайта Hugo {#видео-установка-темы-сайта-hugo}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 60bdda1e308267aa4289a1ad06c80d02 >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube 1l1HO0sa_qs >}}

{{< /rtab >}}
{{< /tabs >}}


## <span class="section-num">4</span> Настройка сайта {#настройка-сайта}


## <span class="section-num">5</span> Публикация сайта {#публикация-сайта}


### <span class="section-num">5.1</span> Развёртывание на базе страниц GitHub (github pages) {#развёртывание-на-базе-страниц-github--github-pages}


#### <span class="section-num">5.1.1</span> Типы страниц GitHub {#типы-страниц-github}

-   Существует два типа страниц GitHub:
    -   Страницы пользователей/организаций: `https://<USERNAME|ORGANIZATION>.github.io/`
        -   Необходимо создать отдельный репозиторий `<USERNAME|ORGANIZATION>.github.io`.
        -   У пользователя может быть только одна страница подобного типа.
        -   Используется для личной страницы пользователя.
    -   Страницы проекта: `https://<USERNAME|ORGANIZATION>.github.io/<PROJECT>`
        -   Создаётся как ветка `gh-pages` в рамках существующего репозитория.
        -   Ваши файлы _Hugo_ хранятся в одной ветке, а ваши сгенерированные файлы публикуются в отдельной ветке в рамках одного проекта.


#### <span class="section-num">5.1.2</span> Создание репозитория для страницы пользователя на Github {#создание-репозитория-для-страницы-пользователя-на-github}

-   Чтобы опубликовать свой сайт со ссылкой `https://username.github.io`, необходимо создать репозиторий с именем `username.github.io`.
-   Перейдите на свою веб-страницу Github и нажмите «Создать», чтобы создать новый репозиторий.
-   Можно создать с помощью утилиты `gh` (см. [github: утилиты командной строки]({{< relref "2021-08-04-github-command-line-utilities" >}})):
    ```shell
    gh repo create username.github.io --public
    ```


#### <span class="section-num">5.1.3</span> Подключение репозитория к вложенной папке {#подключение-репозитория-к-вложенной-папке}

-   Создайте подмодуль `public` в папке блога:
    ```shell
    cd ~/work/blog/blog
    git submodule add git@github.com:username/username.github.io.git public
    ```


#### <span class="section-num">5.1.4</span> Изменить `baseURL` в `config.yaml` {#изменить-baseurl-в-config-dot-yaml}

-   Не забудьте задать значение для `baseURL` в файле `config.yaml`:
    -   `baseURL: 'https://<USERNAME>.github.io'` : для страницы пользователя;
    -   `baseURL: 'https://<USERNAME>.github.io/<REPOSITORY_NAME>'` : для репозитория проекта.
-   Если это не сделать, то ваш сайт не будет работать.


#### <span class="section-num">5.1.5</span> Генерация и развёртывание сайта {#генерация-и-развёртывание-сайта}

-   Сгенерите проект
    ```shell
    cd ~/work/blog/blog
    hugo
    ```
-   Зафиксируйте изменения и отправьте контент на GitHub:
    ```shell
    # Go To Public folder
    cd public

    # Add changes to git.
    git add .

    # Commit changes.
    git commit -am "rebuilding site $(date)"

    # Push source and build repos.
    git push origin master
    ```


## <span class="section-num">6</span> Добавление контента {#добавление-контента}

-   [Org-roam. Экспорт в Hugo]({{< relref "2022-11-23-org-roam-hugo-export" >}})
