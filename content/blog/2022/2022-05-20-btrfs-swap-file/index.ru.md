---
title: "Файл подкачки на btrfs"
author: ["Dmitry S. Kulyabov"]
date: 2022-05-20T10:29:00+03:00
lastmod: 2023-12-05T13:46:00+03:00
tags: ["sysadmin", "btrfs"]
categories: ["computer-science"]
draft: false
slug: "btrfs-swap-file"
---

Размещение файла подкачки на разделе _btrfs_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   btrfs поддерживает файл подкачки (начиная с ядра версии 5.0).
-   Файл подкачки **не может** находиться на любом рейде btrfs.
-   btrfs не позволяет создавать снапшоты, если на подтоме есть рабочий файл подкачки.
-   Рекомендуется размещать файл подкачки на отдельном подтоме.
-   Файл подкачки должен иметь свойство NODATACOW.
-   Файл подкачки должен быть без сжатия.


## <span class="section-num">2</span> Создание файла подкачки {#создание-файла-подкачки}

-   Подмонтируем раздел с btrfs:
    ```shell
    mkdir /mnt/gentoo
    mount -tbtrfs -orelatime,space_cache,discard,autodefrag,compress=zstd:9 /dev/sda4 /mnt/gentoo/
    ```
-   Создадим подтом для файла подкачки на btrfs:
    ```shell
    cd /mnt/gentoo/
    btrfs subvol create @swap
    ```
-   Отмонтируем том btrfs:
    ```shell
    umount /mnt/gentoo
    ```
-   Создадим точку монтирования:
    ```shell
    mkdir /swap
    ```
-   Подмонтируем подтом `@swap`:
    ```shell
    mount -o subvol=@swap /dev/sda4 /swap
    ```
-   Отключим для этого подтома CoW:
    ```shell
    chattr +C /swap
    ```
-   Создадим файл подкачки:
    ```shell
    truncate -s 0 /swap/swapfile
    ```
-   Отключим сжатие:
    ```shell
    btrfs property set /swap/swapfile compression ""
    ```
-   Установим права доступа `600` к файлу подкачки:
    ```shell
    chmod 600 /swap/swapfile
    ```
-   Установим размер файла подкачки.
    -   Можно задать размер вручную (например, 4GiB):
        ```shell
        fallocate -l 4G /swap/swapfile
        ```
    -   Можно установить размер файла подкачки исходя из размера оперативной памяти:
        ```shell
        fallocate -l $(free -h --si | awk 'NR == 2 {print $2}') /swap/swapfile
        ```
-   Отформатируем файл подкачки:
    ```shell
    mkswap /swap/swapfile
    ```
-   Активируем файл подкачки:
    ```shell
    swapon /swap/swapfile
    ```
-   Добавим запись в `/etc/fstab`, чтобы подключать файл подкачки при загрузке (для устройства с `UUID="f8963df3-1320-4bc0-a125-62be185b029e"`):
    ```conf-unix
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"	/swap               btrfs   relatime,discard,autodefrag,compress=zstd:9,subvol=@swap    0 0
    /swap/swapfile					none		    swap    sw								0 0
    ```
-   Проверьте, что файл `/etc/fstab` не содержит ошибок:
    ```shell
    findmnt --verify --verbose
    ```
