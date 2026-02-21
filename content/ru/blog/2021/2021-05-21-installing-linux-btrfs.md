---
title: "Перенос Linux на btrfs"
author: ["Dmitry S. Kulyabov"]
date: 2021-05-21T20:38:00+03:00
lastmod: 2024-03-12T14:09:00+03:00
tags: ["btrfs", "sysadmin", "gentoo"]
categories: ["computer-science"]
draft: false
slug: "installing-linux-btrfs"
---

Перенос Gentoo Linux с одного диска на другой. На новом диске делается система btrfs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Исходное состояние системы {#исходное-состояние-системы}

-   Переносил несколько вариантов исходных систем.


### <span class="section-num">1.1</span> Система на LVM {#система-на-lvm}

-   Исходно система установлена на LVM:
    -   `/dev/sda1`: `/boot/EFI`;
    -   `/dev/sda2`: `/boot`;
    -   `/dev/vgs/root`: `/`;
    -   `/dev/vgs/var`: `/var`;
    -   `/dev/vgs/var_tmp`: `/var/tmp`;
    -   `/dev/vgs/vm`: `/var/vm`;
    -   `/dev/vgs/portage`: `/usr/portage`;
    -   `/dev/vgs/portage_local`: `/usr/local/share/portage`;
    -   `/dev/vgs/portage_com`: `/com/lib/portage`;
    -   `/dev/vgs/home`: `/home`.


### <span class="section-num">1.2</span> Система на btrfs {#система-на-btrfs}

-   Система на btrfs:
    -   `/dev/sda1`: `/boot/EFI`;
    -   `/dev/sda2`: `/boot`;
    -   `/dev/sda3`: `swap`;
    -   `/dev/sda4`: партиция с файловой системой btrfs.


## <span class="section-num">2</span> Разбиение диска {#разбиение-диска}

-   Установим тип разбиения в GPT.


### <span class="section-num">2.1</span> Выделенная boot-партиция {#выделенная-boot-партиция}

-   Разобьём на партиции:
    -   p1 --- 512M, для `EFI`.
    -   p2 --- 500--1024M, для `/boot`.
    -   p3 --- двойная оперативная память, для `swap`.
        -   Также можно разместить файл подкачки на `btrfs` (см. [Файл подкачки на btrfs]({{< relref "2022-05-20-btrfs-swap-file" >}})).
    -   p4 --- всё остальное для `btrfs`.
-   Создадим файловые системы:
    -   p1 (`EFI`):
        ```shell
        mkfs.vfat -F32 -n EFI /dev/sdc1
        ```
    -   p2 (`/boot`):
        ```shell
        mkfs.ext4 -L boot /dev/sdc2
        ```
    -   p3 (`swap` в случае отдельной партиции):
        ```shell
        mkswap -L swap /dev/sdc3
        ```
    -   p4 (`btrfs`)
        ```shell
        mkfs.btrfs /dev/sdc4
        ```


### <span class="section-num">2.2</span> Все разделы на файловой системе btrfs {#все-разделы-на-файловой-системе-btrfs}

-   Разобьём на партиции:
    -   p1 --- 1024M, для `EFI`.
    -   Файл подкачки на `btrfs` (см. [Файл подкачки на btrfs]({{< relref "2022-05-20-btrfs-swap-file" >}})).
    -   p4 --- всё остальное для `btrfs`.
-   Разобьём диск:
    ```shell
    sgdisk -n 0:0:+1024M -t 0:ef00 -c 0:EFI /dev/sdc
    sgdisk -n 0:0:0 -t 0:8300 -c 0:gentoo /dev/sdc
    ```
-   Создадим файловые системы:
    -   p1 (`EFI`):
        ```shell
        mkfs.vfat -F32 -n EFI /dev/sdc1
        ```
    -   p2 (`btrfs`) (см. [btrfs. Контрольные суммы]({{< relref "2024-02-19-btrfs-checksumming" >}})):
        ```shell
        mkfs.btrfs --checksum blake2 -L gentoo /dev/sdc2
        ```


## <span class="section-num">3</span> Подготовка раздела с btrfs {#подготовка-раздела-с-btrfs}

-   Подмонтируем раздел с btrfs:
    ```shell
    mkdir /mnt/to
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9 /dev/sdc2 /mnt/to/
    ```
-   Создадим подтома на btrfs (см. [Подтома btrfs]({{< relref "2021-08-27-btrfs-subvolumes" >}})):
    ```shell
    cd /mnt/to/
    btrfs subvol create @
    btrfs subvol create @var
    btrfs subvol create @var@tmp
    btrfs subvol create @var@log
    btrfs subvol create @vm
    btrfs subvol create @home
    btrfs subvol create @root
    btrfs subvol create @boot
    btrfs subvol create @libvirt
    ```
-   Подтома для _Gentoo Linux_.
-   Используется, если _portage_ размещается локально:
    ```shell
    cd /mnt/to/
    btrfs subvol create @portage
    btrfs subvol create @portage@local
    btrfs subvol create @portage@com
    ```
-   Если используется файл подкачки на файловой системе, то создадим для него подтом:
    ```shell
    cd /mnt/to/
    btrfs subvol create @swap
    ```


## <span class="section-num">4</span> Копирование существующих файловых систем {#копирование-существующих-файловых-систем}


### <span class="section-num">4.1</span> Система на LVM {#система-на-lvm}

-   Создадим точку монтирования:
    ```shell
    mkdir /mnt/from
    ```
-   Подмонтируем и скопируем root-партицию:
    ```shell
    mount /dev/vgs/root /mnt/from/
    rsync -av -HS --delete /mnt/from/ /mnt/to/@
    umount /mnt/from/
    ```
-   Подмонтируем и скопируем `/var`:
    ```shell
    mount /dev/vgs/var /mnt/from/
    rsync -av -HS --delete /mnt/from/ /mnt/to/@var
    umount /mnt/from/
    ```
-   Подмонтируем и скопируем `/boot`:
    ```shell
    mkdir /mnt/to/
    mount /dev/sdc2 /mnt/to
    mount /dev/sdb2 /mnt/from/
    rsync -av -HS --delete /mnt/from/ /mnt/to/
    umount /mnt/to
    umount /mnt/from
    ```
-   Подмонтируем и скопируем `portage`:
    ```shell
    mount /dev/vgs/portage /mnt/from/
    rsync -av -HS --delete /mnt/from/ /mnt/to/@portage
    umount /mnt/from/
    ```
-   Подмонтируем и скопируем `portage_local`:
    ```shell
    mount /dev/vgs/portage_local /mnt/from/
    rsync -av -HS --delete /mnt/from/ /mnt/to/@portage_local
    umount /mnt/from/
    ```


### <span class="section-num">4.2</span> Система на btrfs {#система-на-btrfs}


#### <span class="section-num">4.2.1</span> Подготовка к копированию {#подготовка-к-копированию}

-   Создадим точки монтирования:
    ```shell
    mkdir -p /mnt/from
    ```
-   Подмонтируем исходную файловую систему btrfs:
    ```shell
    mount /dev/sda4 /mnt/from/
    ```


#### <span class="section-num">4.2.2</span> Копирование основных файловых систем {#копирование-основных-файловых-систем}

-   Скопируем root-партицию:
    ```shell
    rsync -av -HS -AX --delete /mnt/from/@/* /mnt/to/@
    ```
-   Скопируем `/var`:
    ```shell
    rsync -av -HS -AX --delete /mnt/from/@var/* /mnt/to/@var
    ```
-   Подмонтируем и скопируем `/boot`:
    ```shell
    mkdir /mnt/boot
    mount /dev/sda2 /mnt/boot
    rsync -av -HS --delete /mnt/boot/* /mnt/to/@boot
    umount /mnt/boot
    ```


#### <span class="section-num">4.2.3</span> Копируем portage {#копируем-portage}

-   Если `portage` размещён локально, то его тоже надо скопировать.
-   Скопируем `@portage`:

<!--listend-->

```shell
rsync -av -HS --delete /mnt/from/@portage/* /mnt/to/@portage
```

-   Скопируем `@portage@local`:

<!--listend-->

```shell
rsync -av -HS --delete /mnt/from/@portage@local/* /mnt/to/@portage@local
```


#### <span class="section-num">4.2.4</span> Копируем системы с отключением CoW {#копируем-системы-с-отключением-cow}

-   Для файловых систем с образами виртуальных машин следует отключить CoW (copy-on-write) (см. [Подтома btrfs]({{< relref "2021-08-27-btrfs-subvolumes" >}})).
-   Так же стоит отключить _CoW_ для часто изменяемых файлов (например, журналов).
-   Подмонтируем файловую систему `btrfs`:
    ```shell
    mkdir -p /mnt/gentoo
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@ /dev/sdc2 /mnt/gentoo/
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@var /dev/sdc2 /mnt/gentoo/var
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@var@tmp /dev/sdc2 /mnt/gentoo/var/tmp
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@vm /dev/sdc2 /mnt/gentoo/var/vm
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@libvirt /dev/sdc2 /mnt/gentoo/var/lib/libvirt/images
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@var@log /dev/sdc2 /mnt/gentoo/var/log
    ```

<!--list-separator-->

1.  Копирование `/var/vm`

    -   Отключим для этого подтома CoW:
        ```shell
        cd /mnt/gentoo/var/
        chattr +C vm
        ```
    -   Скопируем `/var/vm`:
        ```shell
        rsync -av -HS -AX --delete /mnt/from/@vm/* /mnt/to/@vm
        ```

<!--list-separator-->

2.  Копирование `/var/lib/libvirt/images`

    -   Отключим для подтома `/var/lib/libvirt/images` CoW:
        ```shell
        cd /mnt/gentoo/var/lib/libvirt/
        chattr +C images
        ```
    -   Скопируем `/var/lib/libvirt/images`:
        ```shell
        rsync -av -HS -AX --delete /mnt/from/@libvirt/* /mnt/to/@libvirt
        ```

<!--list-separator-->

3.  Копирование `/var/log`

    -   Для `/var/log`
    -   Отключим для подтома `/var/log` CoW:
        ```shell
        cd /mnt/gentoo/var/
        chattr +C log
        ```
    -   Скопируем `/var/log`:
        ```shell
        rsync -av -HS -AX --delete /mnt/from/@var@log/* /mnt/to/@var@log
        ```

<!--list-separator-->

4.  Настройки `/var/tmp`

    -   Для `/var/tmp`
        ```shell
        cd /mnt/gentoo/var/
        chattr +C tmp
        ```
    -   Посмотреть результат можно командой:
        ```shell
        lsattr -a /mnt/gentoo/var/
        lsattr -a /mnt/gentoo/var/lib/libvirt/
        ```


## <span class="section-num">5</span> Установка загрузчика {#установка-загрузчика}

-   Перемонтируем файловую систему `btrfs`:
    ```shell
    mkdir -p /mnt/gentoo
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@ /dev/sdc2 /mnt/gentoo/
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@var /dev/sdc2 /mnt/gentoo/var
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@var@tmp /dev/sdc2 /mnt/gentoo/var/tmp
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@boot /dev/sdc2 /mnt/gentoo/boot
    mount /dev/sdc1 /mnt/gentoo/boot/efi
    ```
-   Подмонтируем псевдо-файловые системы:
    ```shell
    mount -o bind /dev /mnt/gentoo/dev/
    mount -o bind /proc /mnt/gentoo/proc/
    mount -o bind /sys /mnt/gentoo/sys/
    mount -o bind /run /mnt/gentoo/run/
    mount -t efivarfs efivarfs /mnt/gentoo/sys/firmware/efi/efivars
    ```
-   Установим загрузчик:
    ```shell
    cd /mnt/gentoo/
    chroot /mnt/gentoo/ /bin/bash
    grub-install /boot
    grub-mkconfig -o /boot/grub/grub.cfg
    ```


## <span class="section-num">6</span> Файл монтирования fstab {#файл-монтирования-fstab}

-   Создадим файл монтирования fstab.
-   Узнаем идентификатор партиции с файловой системой btrfs:
    ```shell
    blkid /dev/sdc2
    ```
-   Получим строчку:
    ```shell
    UUID="<uuid_number>"
    ```
-   Создадим файл `/mnt/to/etc/fstab`:
    ```conf-unix
    LABEL="boot"					/boot		ext4	relatime,discard=async					1 1
    LABEL="EFI"						/boot/efi	vfat	defaults,discard=async,flush,tz=UTC				0 0
    LABEL="swap"					none		swap	sw							0 0
    UUID="<uuid_number>"	/		btrfs	relatime,discard=async,autodefrag,compress=zstd:9,subvol=@	0 0
    UUID="<uuid_number>"	/var		btrfs	relatime,discard=async,autodefrag,compress=zstd:9,subvol=@var	0 0
    UUID="<uuid_number>"	/var/tmp	btrfs	relatime,discard=async,autodefrag,compress=zstd:9,subvol=@var_tmp	0 0
    UUID="<uuid_number>"	/var/vm		btrfs	relatime,discard=async,autodefrag,compress=zstd:9,subvol=@vm		0 0
    UUID="<uuid_number>"	/home		btrfs	relatime,discard=async,autodefrag,compress=zstd:9,subvol=@home	0 0
    UUID="<uuid_number>"	/usr/portage	btrfs	relatime,discard=async,autodefrag,compress=zstd:9,subvol=@portage	0 0
    UUID="<uuid_number>"	/usr/local/share/portage	btrfs	relatime,discard=async,autodefrag,compress=zstd:9,subvol=@portage_local	0 0
    UUID="<uuid_number>"	/com/lib/portage	btrfs	relatime,discard=async,autodefrag,compress=zstd:9,subvol=@portage_com	0 0
    ```
-   Если используется файл подкачки, то вместо отдельной партиции следует подключить этот файл в `/mnt/to/etc/fstab`:
    ```conf-unix
    UUID="<uuid_number>"	/swap		btrfs	relatime,discard=async,autodefrag,compress=zstd:9,subvol=@swap	0 0
    /swap/swapfile		none		swap    sw								0 0
    ```


## <span class="section-num">7</span> Файл подкачки на файловой системе btrfs {#файл-подкачки-на-файловой-системе-btrfs}


### <span class="section-num">7.1</span> Подготовка к созданию файла подкачки {#подготовка-к-созданию-файла-подкачки}

-   Для раздела файла подкачки следует отключить CoW (copy-on-write).
-   Подмонтируем файловую систему `btrfs`:
    ```shell
    mkdir -p /mnt/gentoo/
    mount -tbtrfs -orelatime,discard,autodefrag,compress=zstd:9,subvol=@ /dev/sdc2 /mnt/gentoo/
    ```
-   Создадим точку монтирования:
    ```shell
    mkdir /mnt/gentoo/swap
    ```
-   Подмонтируем подтом `@swap`:
    ```shell
    mount -tbtrfs -orelatime,discard,autodefrag,compress=zstd:9,subvol=@swap /dev/sdc2 /mnt/gentoo/swap
    ```
-   Отключим для этого подтома CoW:
    ```shell
    chattr +C /mnt/gentoo/swap
    ```


### <span class="section-num">7.2</span> Создание файла подкачки {#создание-файла-подкачки}


#### <span class="section-num">7.2.1</span> Старый подход {#старый-подход}

-   Создадим файл подкачки:
    ```shell
    truncate -s 0 /mnt/gentoo/swap/swapfile
    ```
-   Установим права доступа `600` к файлу подкачки:
    ```shell
    chmod 600 /mnt/gentoo/swap/swapfile
    ```
-   Установим размер файла подкачки исходя из размера оперативной памяти:
    ```shell
    fallocate -l $(free -h --si | awk 'NR == 2 {print $2}') /mnt/gentoo/swap/swapfile
    ```
-   Отформатируем файл подкачки:
    ```shell
    mkswap /mnt/gentoo/swap/swapfile
    ```


#### <span class="section-num">7.2.2</span> Новый подход {#новый-подход}

-   Работает начиная с версии утилит 6.1.
-   Создадим файл подкачки размером 8ГБ:
    ```shell
    btrfs filesystem mkswapfile --size 4g --uuid clear /mnt/gentooswap/swapfile
    ```
-   Создадим файл подкачки исходя из размера оперативной памяти:
    ```shell
    btrfs filesystem mkswapfile --size $(free -h --si | awk 'NR == 2 {print $2}') --uuid clear /mnt/gentoo/swap/swapfile
    ```


### <span class="section-num">7.3</span> Активация файла подкачки {#активация-файла-подкачки}

-   Активируем файл подкачки:
    ```shell
    swapon /mnt/gentoo/swap/swapfile
    ```
