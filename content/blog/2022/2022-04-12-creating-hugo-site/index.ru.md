---
title: "Создание сайта на Hugo"
author: ["Dmitry S. Kulyabov"]
date: 2022-04-12T20:49:00+03:00
lastmod: 2026-02-21T19:36:00+03:00
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

-   [Hugo. Развёртывание на базе страниц GitHub]({{< relref "2026-02-21--hugo-deploy-github-pages" >}})


## <span class="section-num">6</span> Добавление контента {#добавление-контента}

-   [Org-roam. Экспорт в Hugo]({{< relref "2022-11-23-org-roam-hugo-export" >}})
