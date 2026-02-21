---
title: "Gentoo. Дополнительные репозитории"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-01T13:41:00+03:00
lastmod: 2024-12-20T17:35:00+03:00
tags: ["linux", "gentoo"]
categories: ["computer-science"]
draft: false
slug: "gentoo-additional-repositories"
---

Gentoo. Дополнительные репозитории.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Ранее использовалась утилита `layman`.
-   Сейчас рекомендуется использовать модуль _eselect_ `eselect-repository`.
-   Документация:
    -   <https://wiki.gentoo.org/wiki/Eselect/Repository/ru>
    -   <https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/CustomTree/ru>


## <span class="section-num">2</span> Установка {#установка}

-   Установка:
    ```shell
    emerge app-eselect/eselect-repository
    ```


## <span class="section-num">3</span> Конфигурация {#конфигурация}

-   Для работы модуля должен существовать каталог или файл `repos.conf`, путь к которому задаётся переменной `REPOS_CONF` в `/etc/eselect/repository.conf`.
-   Будем использовать каталог конфигурации:
    ```shell
    mkdir -p /etc/portage/repos.conf
    ```
-   Файл настройки `/etc/eselect/repository.conf` изначально имеет следующий вид:
    ```conf-unix
    # конфигурация для eselect-repo
    # (читается как bash сценарий, поэтому значения должны оставаться совместимыми
    # с bash)

    # Следующие переменные указывают на пути,
    # настроенные во время сборки:
    #   CACHEDIR -- системный каталог кэша (напр. /var/cache)
    #   SYSCONFDIR -- системный каталог конфигурации (напр. /etc)
    #   SHAREDSTATEDIR -- системный каталог с разделяемыми состояниями
    # (shared state) (напр. /var)

    # Расположение файла или каталога с конфигурацией репозиториев.
    # Если это каталог, используются правила Portage для дочерних файлов.
    REPOS_CONF=${SYSCONFDIR}/portage/repos.conf

    # Файл, в который будут добавляться конфигурации новых репозиториев,
    # если REPOS_CONF является каталогом.  Вы можете использовать
    # переменную "${repository}", которая указывает на
    # название вновь добавленного репозитория.
    REPOS_CONF_SUBFILE=${REPOS_CONF}/eselect-repo.conf

    # Родительский каталог, куда будут добавлены сами репозитории.
    # Новые репозитории добавляются как дочерние каталоги
    # с названием самого репозитория.
    REPOS_BASE=${SHAREDSTATEDIR}/db/repos

    # Расположение списка удалённых репозиториев (remote repositories list).
    # По умолчанию использует список gentoo-mirror, который содержит,
    # прегенерированный кэш метаданных
    # (pregenerated metadata cache).
    REMOTE_LIST_URI=https://qa-reports.gentoo.org/output/repos/repositories.xml

    # Альтернатива: изначальный список Gentoo без прегенерации.
    #REMOTE_LIST_URI=https://api.gentoo.org/overlays/repositories.xml

    # Каталог, где будет храниться кэш repositories.xml. Файл всегда называется
    # "repositories.xml" из-за технических ограничений wget.
    REMOTE_LIST_CACHEDIR=~/.cache/eselect-repo

    # Интервал (в секундах) проверки списка удалённых репозиториев на изменения.
    # По умолчанию равен 2 часам.
    REMOTE_LIST_REFRESH=$(( 2 * 3600 ))
    ```


## <span class="section-num">4</span> Использование {#использование}


### <span class="section-num">4.1</span> Синхронизация репозитория {#синхронизация-репозитория}

-   Репозитории могут быть синхронизированы утилитой `emaint`:
    ```shell
    emaint sync -r foo
    ```


### <span class="section-num">4.2</span> Просмотр репозиториев {#просмотр-репозиториев}

-   Gentoo позволяет пользователям и разработчикам регистрировать репозитории на <https://repos.gentoo.org/> для публичного использования.
-   Просмотр списка репозиториев:
    ```shell
    eselect repository list
    ```

    -   суффикс `*` указывает, что этот репозиторий установлен и подключён;
    -   суффикс `#` указывает, что для этого репозитория необходимо обновить их информацию о синхронизации (путём выключения и включения), или они были настроены пользователем;
    -   суффикс `@` указывает, что такой репозиторий не указан по имени в официальном, опубликованном списке.

-   Перечислить только сконфигурированные репозитории:
    ```shell
    eselect repository list -i
    ```


### <span class="section-num">4.3</span> Добавление репозиториев {#добавление-репозиториев}

-   Добавление репозиториев с <https://repos.gentoo.org/>:
    ```shell
    eselect repository enable foo
    ```
-   Добавление произвольных репозиториев
    ```shell
    eselect repository add test git https://github.com/test/test.git
    ```

    -   Синтаксис:
        ```shell
        eselect repository add <название> <метод-синхронизации> <адрес-синхронизации>
        ```


### <span class="section-num">4.4</span> Отключение репозиториев {#отключение-репозиториев}

-   Отключение репозиториев без удаления содержимого:
    ```shell
    eselect repository remove foo
    ```

    -   Синтаксис:
        ```shell
        remove [-f] (<название>|<индекс>)
        ```
    -   Опция `-f` требуется для репозиториев, не зарегистрированных на repos.gentoo.org, или без информации о синхронизации.

-   Отключение репозиториев с удалением содержимого:
    ```shell
    eselect repository remove foo
    ```

    -   Синтаксис:
        ```shell
        remove [-f] (<название>|<индекс>)
        ```
    -   Опция `-f` требуется для репозиториев, не зарегистрированных на repos.gentoo.org, или без информации о синхронизации.


### <span class="section-num">4.5</span> Создание нового репозитория {#создание-нового-репозитория}

-   Создание каркаса репозитория:
    ```shell
    eselect repository create foo
    ```

    -   Синтаксис:
        ```shell
        create <название> [<путь>]
        ```


## <span class="section-num">5</span> Настройки репозиториев {#настройки-репозиториев}


### <span class="section-num">5.1</span> Приоритет репозиториев {#приоритет-репозиториев}

-   По умолчанию пакеты в оверлейных репозиториях имеют преимущество перед пакетами в репозитории `gentoo`.
-   Кроме того, можно управлять приоритетами дополнительных репозиториев.
-   Добавьте параметр приоритета в файл описания репозиториев `/etc/portage/repos.conf/eselect-repo.conf`:
    ```toml
    [local]
    location = /var/db/repos/local
    priority = 100
    ```


## <span class="section-num">6</span> Списки полезных репозиториев {#списки-полезных-репозиториев}


### <span class="section-num">6.1</span> Karma {#karma}

-   [Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})


### <span class="section-num">6.2</span> guru {#guru}

-   Страница: <https://wiki.gentoo.org/wiki/Project:GURU>
-   Репозиторий: <https://github.com/gentoo-mirror/guru>
-   Добавление репозитория:
    ```shell
    eselect repository enable guru
    ```
-   Синхронизация репозитория:
    ```shell
    emaint sync -r guru
    ```


### <span class="section-num">6.3</span> haskell {#haskell}

-   Добавление репозитория:
    ```shell
    eselect repository enable haskell
    ```
-   Синхронизация репозитория:
    ```shell
    emaint sync -r haskell
    ```
