---
title: "Подтома btrfs"
author: ["Dmitry S. Kulyabov"]
date: 2021-08-27T11:41:00+03:00
lastmod: 2026-02-16T12:45:00+03:00
tags: ["btrfs", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "btrfs-subvolumes"
---

Подтома (subvolumes) btrfs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Именование подтомов {#именование-подтомов}

-   Для определённости я называю подтома по шаблону `@имя_подтома`.


### <span class="section-num">1.1</span> Список подтомов {#список-подтомов}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Возможные наименования подтомов btrfs
</div>

| Подтом                | Точка монтирования                           | Описание                                                                                                                                                |
|-----------------------|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`                   | `/`                                          | Корневой каталог (системные файлы)                                                                                                                      |
| `@home`               | `/home`                                      | Домашний каталог с пользовательскими данными                                                                                                            |
| `@root`               | `/root`                                      | Домашний каталог пользователя `root`                                                                                                                    |
| `@snapshots`          | ‒                                            | Корневой подтом для снапшотов                                                                                                                           |
| `@snapshots@root`     | `/.snapshots`                                | Содержит снапшоты корня, которые создает `snapper`                                                                                                      |
| `@snapshots@home`     | `/home/.snapshots`                           | Содержит снапшоты домашнего каталога, которые создает `snapper`                                                                                         |
| `@machines`           | `/var/lib/machines`                          | Если не существует, то создаст systemd                                                                                                                  |
| `@portables`          | `/var/lib/portables`                         | Если не существует, то создаст systemd                                                                                                                  |
| `@docker`             | `/var/lib/docker`                            | Докер создаёт подтома в `./btrfs/subvolumes` либо в `./XXX/btrfs/subvolumes`                                                                            |
| `@var`                | `/var`                                       | Аналогично выше описанному                                                                                                                              |
| `@var@lib`            | `/var/lib`                                   | Вместо создания `@machines`, `@portables`, `@docker` можно создать только этот, если в `/var/lib` не будет храниться чего-то важного                    |
| `@var@tmp`            | `/var/tmp`                                   | Содержит временные файлы. Должен монтироваться с `nodatacow`                                                                                            |
| `@var@log` или `@log` | `/var/log`                                   | Содержит большое количество файлов, которые пишутся маленькими частями. Должен монтироваться с `nodatacow`                                              |
| `@swap`               | `/swap` или `/var/swap`, или `/var/lib/swap` | Подтом для файла подкачки. Должен монтироваться с `nodatacow` (см. [Файл подкачки на btrfs]({{< relref "20220520102900-фаил_подкачки_на_btrfs.md" >}})) |
| `@libvirt`            | `/var/lib/libvirt/images`                    | Образы для _libvirt_. Должен монтироваться с `nodatacow`                                                                                                |


### <span class="section-num">1.2</span> Минимально рекомендуемый набор подтомов {#минимально-рекомендуемый-набор-подтомов}

-   Минимум нужны два подтома: `@` и `@home`.


## <span class="section-num">2</span> Создание подтомов {#создание-подтомов}

-   При установки системы я создаю подтома следующим образом:
    -   Подмонтируем раздел с btrfs:
        ```shell
        mkdir /mnt/gentoo
        mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9 /dev/sdc2 /mnt/gentoo/
        ```
    -   Создадим подтома на btrfs:
        ```shell
        cd /mnt/gentoo/
        btrfs subvol create @
        btrfs subvol create @var
        btrfs subvol create @var@tmp
        btrfs subvol create @var@log
        btrfs subvol create @vm
        btrfs subvol create @portage
        btrfs subvol create @portage@local
        btrfs subvol create @portage@com
        btrfs subvol create @libvirt
        btrfs subvol create @home
        ```


## <span class="section-num">3</span> Отключение CoW {#отключение-cow}

-   Для файловых систем с образами виртуальных машин следует отключить CoW (copy-on-write).
-   Так же стоит отключить _CoW_ для часто изменяемых файлов (например, журналов).
-   Подмонтируем файловую систему `btrfs`:
    ```shell
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@vm /dev/sdc2 /mnt/gentoo/var/vm
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@libvirt /dev/sdc2 /mnt/gentoo/var/lib/libvirt/images
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@var@log /dev/sdc2 /mnt/gentoo/var/log
    mount -tbtrfs -orelatime,discard=async,autodefrag,compress=zstd:9,subvol=@var@tmp /dev/sdc2 /mnt/gentoo/var/tmp
    ```
-   Отключим для этого подтома CoW:
    -   Для `/var/vm`
        ```shell
        cd /mnt/gentoo/var/
        chattr +C vm
        ```
    -   Для `/var/lib/libvirt/images`
        ```shell
        cd /mnt/gentoo/var/lib/libvirt/
        chattr +C images
        ```
    -   Для `/var/log`
        ```shell
        cd /mnt/gentoo/var/
        chattr +C log
        ```
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


## <span class="section-num">4</span> Монтирование подтомов в fstab {#монтирование-подтомов-в-fstab}

-   При монтировании я указываю универсальный идентификатор (UUID) файловой системы:
    ```conf-unix
    # /etc/fstab
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"     /               btrfs   relatime,discard=async,autodefrag,compress=zstd:9,subvol=@    0 0
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"     /var            btrfs   relatime,discard=async,autodefrag,compress=zstd:9,subvol=@var 0 0
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"     /var/tmp        btrfs   relatime,discard=async,autodefrag,compress=zstd:9,subvol=@var_tmp     0 0
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"     /var/vm         btrfs   relatime,discard=async,autodefrag,compress=zstd:9,subvol=@vm          0 0
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"     /home           btrfs   relatime,discard=async,autodefrag,compress=zstd:9,subvol=@home        0 0
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"     /usr/portage    btrfs   relatime,discard=async,autodefrag,compress=zstd:9,subvol=@portage     0 0
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"     /usr/local/share/portage        btrfs   relatime,discard=async,autodefrag,compress=zstd:9,subvol=@portage_local       0 0
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"     /com/lib/portage        btrfs   relatime,discard=async,autodefrag,compress=zstd:9,subvol=@portage_com 0 0
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"    /var/lib/libvirt/images       btrfs   relatime,discard=async,autodefrag,compress=zstd:9,subvol=@libvirt 0 0
    ```
-   Идентификатор файловой системы можно узнать следующим образом:
    ```shell
    blkid /dev/sdc2
    ```


## <span class="section-num">5</span> Создание нового подтома {#создание-нового-подтома}

-   После установки системы может возникнуть необходимость создания дополнительных подтомов на существующем томе.
    ```shell
    mkdir /mnt/btrfs
    mount UUID=f8963df3-1320-4bc0-a125-62be185b029e /mnt/btrfs
    btrfs subvolume create /mnt/btrfs/@data
    ```
-   Подключим в `/etc/fstab`:
    ```shell
    UUID="f8963df3-1320-4bc0-a125-62be185b029e"	/data		btrfs	relatime,discard=async,autodefrag,compress=zstd:9,subvol=@data        0 0
    ```
