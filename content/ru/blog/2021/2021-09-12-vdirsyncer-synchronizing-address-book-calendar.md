---
title: "Vdirsyncer. Синхронизация адресной книги и календаря"
author: ["Dmitry S. Kulyabov"]
date: 2021-09-12T16:01:00+03:00
lastmod: 2021-11-02T12:31:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "vdirsyncer-synchronizing-address-book-calendar"
---

Синхронизация локальной базы контактов и календаря.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <http://vdirsyncer.pimutils.org/>
-   Репозиторий: <https://github.com/pimutils/vdirsyncer>


## <span class="section-num">2</span> Установка {#установка}

-   Linux
    -   Gentoo

        ```shell
        emerge vdirsyncer
        ```


## <span class="section-num">3</span> Конфигурирование {#конфигурирование}


### <span class="section-num">3.1</span> Типовая конфигурация {#типовая-конфигурация}

-   В поставке идёт пример файла конфигурации:

    ```ini
    # An example configuration for vdirsyncer.
    #
    # Move it to ~/.vdirsyncer/config or ~/.config/vdirsyncer/config and edit it.
    # Run `vdirsyncer --help` for CLI usage.
    #
    # Optional parameters are commented out.
    # This file doesn't document all available parameters, see
    # http://vdirsyncer.pimutils.org/ for the rest of them.

    [general]
    # A folder where vdirsyncer can store some metadata about each pair.
    status_path = "~/.vdirsyncer/status/"

    # CARDDAV
    [pair bob_contacts]
    # A `[pair <name>]` block defines two storages `a` and `b` that should be
    # synchronized. The definition of these storages follows in `[storage <name>]`
    # blocks. This is similar to accounts in OfflineIMAP.
    a = "bob_contacts_local"
    b = "bob_contacts_remote"

    # Synchronize all collections that can be found.
    # You need to run `vdirsyncer discover` if new calendars/addressbooks are added
    # on the server.

    collections = ["from a", "from b"]

    # Synchronize the "display name" property into a local file (~/.contacts/displayname).
    metadata = ["displayname"]

    # To resolve a conflict the following values are possible:
    #   `null` - abort when collisions occur (default)
    #   `"a wins"` - assume a's items to be more up-to-date
    #   `"b wins"` - assume b's items to be more up-to-date
    #conflict_resolution = null

    [storage bob_contacts_local]
    # A storage references actual data on a remote server or on the local disk.
    # Similar to repositories in OfflineIMAP.
    type = "filesystem"
    path = "~/.contacts/"
    fileext = ".vcf"

    [storage bob_contacts_remote]
    type = "carddav"
    url = "https://owncloud.example.com/remote.php/carddav/"
    #username =
    # The password can also be fetched from the system password storage, netrc or a
    # custom command. See http://vdirsyncer.pimutils.org/en/stable/keyring.html
    #password =

    # CALDAV
    [pair bob_calendar]
    a = "bob_calendar_local"
    b = "bob_calendar_remote"
    collections = ["from a", "from b"]

    # Calendars also have a color property
    metadata = ["displayname", "color"]

    [storage bob_calendar_local]
    type = "filesystem"
    path = "~/.calendars/"
    fileext = ".ics"

    [storage bob_calendar_remote]
    type = "caldav"
    url = "https://owncloud.example.com/remote.php/caldav/"
    #username =
    #password =
    ```


### <span class="section-num">3.2</span> Синхронизация с Google {#синхронизация-с-google}


### <span class="section-num">3.3</span> Синхронизация с Office 365 {#синхронизация-с-office-365}


### <span class="section-num">3.4</span> Синхронизация с Yandex {#синхронизация-с-yandex}


### <span class="section-num">3.5</span> Синхронизация с Fuux {#синхронизация-с-fuux}


## <span class="section-num">4</span> Утилиты для работы с _vdir_ {#утилиты-для-работы-с-vdir}


## <span class="section-num">5</span> Работа из Emacs {#работа-из-emacs}


## <span class="section-num">6</span> Обслуживание {#обслуживание}


### <span class="section-num">6.1</span> Запуск через таймер systemd {#запуск-через-таймер-systemd}

-   Дистрибутив включает файлы модулей для запуска с определённым интервалом (по умолчанию каждые 15 ± 5 минут).
-   Файл `vdirsyncer.service`:

    ```ini
    [Unit]
    Description=Synchronize calendars and contacts
    Documentation=https://vdirsyncer.readthedocs.org/

    [Service]
    ExecStart=/usr/bin/vdirsyncer sync
    RuntimeMaxSec=3m
    Restart=on-failure
    ```
-   Файл `vdirsyncer.timer`:

    ```ini
    [Unit]
    Description=Synchronize vdirs

    [Timer]
    OnBootSec=5m
    OnUnitActiveSec=15m
    AccuracySec=5m

    [Install]
    WantedBy=timers.target
    ```
-   Для запуска на уровне пользователя скопируйте их в каталог `~/.config/systemd/user`.
-   Для активации и запуска выполните:

    ```shell
    systemctl --user enable vdirsyncer.timer
    systemctl --user start vdirsyncer.timer
    ```
