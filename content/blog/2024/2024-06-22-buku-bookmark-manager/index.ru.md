---
title: "Менеджер закладок buku"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-22T20:43:00+03:00
lastmod: 2024-07-15T16:55:00+03:00
categories: ["computer-science"]
draft: false
slug: "buku-bookmark-manager"
---

Менеджер закладок buku.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Утилита управления закладками.
-   Репозиторий: <https://github.com/jarun/buku>


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   В основном репозитории:
    ```shell
    emerge www-misc/buku
    ```


## <span class="section-num">3</span> Использование {#использование}

-   Автоматический импорт закладок из вашего броузера:
    ```shell
    buku --ai
    ```
-   Добавить закладку (опция `--add`):
    ```shell
    buku --add https://www.ya.ru
    ```
-   Собственный заголовок (опция `--title`):
    ```shell
    buku --add http://www.ya.ru --title Yandex Site
    ```
-   Распечатать список закладок (опция `--print`):
    ```shell
    buku --print
    ```
-   Удалить закладку. Получите идентификатор закладки (например, с опцией `--print`) и используйте опцию `--delete`:
    ```shell
    buku --delete 3
    ```
-   Удалить более одной закладки (опция `--delete`, а затем идентификаторы закладок через пробел):
    ```shell
    buku -d 10 11
    ```
-   Удалить диапазон или список закладок:
    ```shell
    buku -d 100-200
    buku -d 100 15 200
    ```
-   Обновить заголовок закладки (опция `--update`, чтобы получить и обновить заголовок закладки из Интернета):
    ```shell
    buku --update
    ```
-   Обновить заголовок конкретной закладки (опция `--update` с идентификатором закладки):
    ```shell
    buku --update 1
    ```
-   Импортировать закладки (опция `--import`):
    ```shell
    buku --import bookmarks.html
    ```
-   Экспортировать закладки (опция `--export`):
    ```shell
    buku --export bookmark-2024-07-07.html
    ```
-   Заблокировать или разблокировать базу данных закладок (опции `--lock` или `--unlook`):
    ```shell
    buku --lock

    buku --unlock
    ```
-   Добавить закладку с тегами  `search engine` и `privacy`, комментарий  `Search engine with perks`, получите заголовок страницы из Интернета:
    ```shell
    buku -a https://ddg.gg search engine, privacy -c Search engine with perks
    ```
-   Добавьте закладку без названия  (работает и для обновления):
    ```shell
    buku -a https://ddg.gg search engine, privacy --title
    ```
-   Обновить существующую закладку с индексом 15012014, добавив новый URL-адрес, теги и комментарии, получить заголовок из Интернета:
    ```shell
    buku -u 15012014 --url http://ddg.gg/ --tag web search, utilities -c Private search engine
    ```
-   Обновить только комментарий для закладки 15012014:
    ```shell
    buku -u 15012014 -c this is a new comment
    ```

    -   Применяется также к `--url`, `--title` и `--tag`.
-   Удалить все  закладки:
    ```shell
    buku -d
    ```
-   Поиск закладок по любым ключевым словам `kernel` и `debugging`  в URL, заголовке или тегах:
    ```shell
    buku kernel debugging
    buku -s kernel debugging
    ```
-   Поиск закладок по всем ключевым словам `kernel` и `debugging`  в URL, заголовке или тегах:
    ```shell
    buku -S kernel debugging
    ```
-   Поиск закладок с тегами  `general kernel concepts`:
    ```shell
    buku --stag general kernel concepts
    ```
-   Показать подробную информацию о последних 10 закладках:
    ```shell
    buku -p -10
    ```
-   Заменить старый тег на новый тег:
    ```shell
    buku --replace 'old tag' 'new tag'
    ```
-   Удалить старый тег из БД:
    ```shell
    $ buku --replace 'old tag'
    ```
-   Открыть URL-адрес по индексу 15012014 в броузере:
    ```shell
    $ buku -o 15012014
    ```


## <span class="section-num">4</span> Интерфейсы {#интерфейсы}


### <span class="section-num">4.1</span> Emacs {#emacs}

-   ebuku - Interface to the buku Web bookmark manager.
-   [Emacs. Пакет ebuku]({{< relref "2024-06-22-emacs-ebuku" >}})


### <span class="section-num">4.2</span> Броузеры {#броузеры}


#### <span class="section-num">4.2.1</span> Bukubrow {#bukubrow}

-   Состоит из двух частей:
    -   расширения для броузера;
    -   интерфейса native messaging для хоста.

<!--list-separator-->

1.  WebExtension for Buku

    -   Расширения для броузеров.
    -   Репозиторий: <https://github.com/samhh/bukubrow-webext>
    -   Плагины для броузеров:
        -   Chrome/Chromium: <https://chrome.google.com/webstore/detail/bukubrow/ghniladkapjacfajiooekgkfopkjblpn>
        -   Firefox: <https://addons.mozilla.org/en-US/firefox/addon/bukubrow/>

<!--list-separator-->

2.  Bukubrow Host

    -   Интерфейс для хоста.
    -   Репозиторий: <https://github.com/samhh/bukubrow-host>

    <!--list-separator-->

    1.  Установка

        -   Gentoo:
            -   оверлей karma ([Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
                ```shell
                emerge -v www-misc/bukubrow
                ```
        -   После установки активировать:
            ```shell
            bukubrow --install-chromium
            bukubrow --install-firefox
            bukubrow --install-chrome
            ```
