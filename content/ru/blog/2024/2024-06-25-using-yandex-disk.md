---
title: "Использование Яндекс-диска"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-25T15:32:00+03:00
lastmod: 2024-09-16T13:52:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "using-yandex-disk"
---

Использование Яндекс-диска.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Монтирование с помощью rclone {#монтирование-с-помощью-rclone}


### <span class="section-num">1.1</span> Настройка {#настройка}

-   Настройте доступ к yandex.ru с помощью:
    ```shell
    rclone config
    ```


### <span class="section-num">1.2</span> Ручное монтирование {#ручное-монтирование}

-   Пусть учётная запись называется `account.yandex.ru`.
-   Подключить диск можно следующим образом:
    ```shell
    mkdir -p ~/n/account@yandex.ru
    rclone mount account@yandex.ru:/ ~/n/account@yandex.ru &
    ```


### <span class="section-num">1.3</span> Монтирование с помощью systemd {#монтирование-с-помощью-systemd}

-   Создайте файл `~/.config/systemd/user/rclone@.service`:
    ```shell
    # User service for Rclone mounting
    #
    # Place in ~/.config/systemd/user/
    # File must include the '@' (ex rclone@.service)
    # As your normal user, run
    #   systemctl --user daemon-reload
    # You can now start/enable each remote by using rclone@<remote>
    #   systemctl --user enable --now rclone@dropbox

    [Unit]
    Description=rclone: Remote FUSE filesystem for cloud storage config %i
    Documentation=man:rclone(1)
    After=network-online.target
    Wants=network-online.target
    AssertPathIsDirectory=%h/n/

    [Service]
    Type=notify
    ExecStartPre=-/usr/bin/mkdir -p %h/n/%i
    ExecStart= \
      /usr/bin/rclone mount \
        --config=%h/.config/rclone/rclone.conf \
        --allow-non-empty \
        --vfs-cache-mode writes \
        --vfs-cache-max-size 100M \
        --dir-cache-time 72h \
        --vfs-read-chunk-size-limit 128M \
        --vfs-read-chunk-size-limit off \
        --log-level INFO \
        --log-file /tmp/rclone-%i.log \
        --umask 022 \
        --allow-other \
        %i: %h/n/%i
    ExecStop=/bin/fusermount -uz %h/n/%i

    [Install]
    WantedBy=default.target
    ```
-   Перегрузите список сервисов:
    ```shell
    systemctl --user daemon-reload
    ```
-   Добавьте сервис в автозапуск:
    ```shell
    systemctl --user enable --now rclone@account@yandex.ru
    ```
