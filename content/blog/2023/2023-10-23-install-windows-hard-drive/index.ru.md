---
title: "Установка Windows с жёсткого диска"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-23T15:51:00+03:00
lastmod: 2024-11-27T11:57:00+03:00
tags: ["windows", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "install-windows-hard-drive"
---

Установка Windows с жёсткого диска.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Варианты установки {#варианты-установки}

-   Можно рассмотреть 2 варианта установки:
    -   UEFI + GPT + файловая система FAT32.
    -   BIOS + MBR + NTFS.
        -   Максимальный размер раздела составляет 2 ТБ.


### <span class="section-num">1.1</span> Ограничения {#ограничения}

-   В зависимости от размера файла `sources\install.wim` может потребоваться один раздел FAT32 или один раздел FAT32 и раздел NTFS.
-   Если размер `sources\install.wim` превышает 4 ГБ, необходимо использовать раздел FAT32 + NTFS, поскольку файловая система FAT32 не поддерживает файлы размером более 4 ГБ.


### <span class="section-num">1.2</span> UEFI {#uefi}

-   Рассматриваем вариант с UEFI.


#### <span class="section-num">1.2.1</span> Стандартный UEFI {#стандартный-uefi}

-   Стандартный UEFI видит только партиции с файловой системой FAT32.
-   Поэтому содержимое образа необходимо скопировать на партицию с NTFS.
-   А на партицию с FAT32 поместить файлы для начальной загрузки установщика Windows.


#### <span class="section-num">1.2.2</span> Сторонние загрузчики UEFI {#сторонние-загрузчики-uefi}

-   Некоторые загрузчики UEFI поддерживают файловую систему NTFS (см. [Загрузчик rEFInd]({{< relref "2024-01-29-refind-boot-manager" >}})).
-   В этом случае можно ограничиться партицией с файловой системой NTFS.
-   Содержимое образа необходимо скопировать на партицию с NTFS.


## <span class="section-num">2</span> Разделы диска {#разделы-диска}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Рекомендуемая структура разделов для Windows
</div>

| Раздел                                   | Размер    | Файловая система |
|------------------------------------------|-----------|------------------|
| Системный раздел EFI (ESP)               | 512 МБ    | FAT32            |
| Зарезервированный раздел Microsoft (MSR) | 128 МБ    |                  |
| Windows (C:)                             | &gt;60 ГБ | NTFS             |
| Образ восстановления (необязательно)     | 10 ГБ     | NTFS             |

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 2:</span>
  Структура разделов для размещения файлов установщика Windows
</div>

| Раздел                   | Размер | Файловая система |
|--------------------------|--------|------------------|
| Установщик Windows FAT32 | 8 ГБ   | FAT32            |
| Установщик Windows NTFS  | 10 ГБ  | NTFS             |

-   Установочный раздел нужно разместить после раздела Windows и образа восстановления.
-   Установочный раздел также можно создать на другом жестком диске или внешнем USB-накопителе.


### <span class="section-num">2.1</span> Разбивка диска {#разбивка-диска}


#### <span class="section-num">2.1.1</span> Инструментарий {#инструментарий}

<!--list-separator-->

1.  sgdisk

    -   Сайт: <https://www.rodsbooks.com/gdisk/>


#### <span class="section-num">2.1.2</span> Консоль Linux {#консоль-linux}

-   Создадим на диске партиции:
    ```shell
    partprobe /dev/sda
    sgdisk --zap-all /dev/sda

    ## ef00 EFI system partition
    sgdisk -n 0:0:+512M -t 0:ef00 -c 0:EFI /dev/sda
    ## 0c01 Microsoft reserved
    sgdisk -n 0:0:+128M -t 0:0c01 /dev/sda
    ## 0700 Microsoft basic data
    sgdisk -n 0:0:+60G -t 0:0700 -c 0:windows /dev/sda
    ## 2700 Windows recovery partition
    sgdisk -n 0:0:+10G -t 0:2700 ${DISK0}
    ## 0700 Microsoft basic data
    sgdisk -n 0:0:+8G -t 0:0700 /dev/sda
    sgdisk -n 0:0:+10M -t 0:0700 /dev/sda

    partprobe /dev/sda
    ```
-   Отформатируем диски:
    ```shell
    mkfs.ntfs -f -L windows /dev/sda3
    mkfs.vfat -n fat -F32 /dev/sda5
    mkfs.ntfs -f -L windistro /dev/sda6
    ```


## <span class="section-num">3</span> Подготовка файлов {#подготовка-файлов}

-   Скопируйте файлы из ISO-образа установщика Windows на жёсткий диск.
-   Если вы используете один раздел FAT32, просто скопируйте все файлы ISO в этот раздел.


### <span class="section-num">3.1</span> Использовании одного раздела FAT32 и одного раздела NTFS {#использовании-одного-раздела-fat32-и-одного-раздела-ntfs}

-   Раздел FAT32 используется для загрузки программы установки, затем программа установки попытается найти `install.wim` и другие файлы в разделе NTFS.
-   Важно, чтобы в каталоге `sources` раздела FAT32 был только файл `boot.wim` и не было других файлов.


#### <span class="section-num">3.1.1</span> Использование Windows {#использование-windows}

-   Предположим, что
    -   диск ISO установщика Windows смонтирован в `X:`;
    -   раздел FAT32 монтируется в `E:`;
    -   раздел NTFS монтируется в `F:`.
-   Скопируйте файлы:
    ```shell
    robocopy /s /xd:Sources X: E:
    md E:\Sources
    copy X:\Sources\boot.wim E:\Sources\
    robocopy /s X: F:
    ```


#### <span class="section-num">3.1.2</span> Использование Linux {#использование-linux}

-   Предположим, что
    -   диск ISO установщика Win 10 смонтирован в `/media/cdrom/`;
    -   раздел FAT32 монтируется в `/mnt/fat/`;
    -   раздел NTFS монтируется в `/mnt/ntfs/`.
-   Смонтируйте диски:
    ```shell
    mkdir -p /mnt/{fat,ntfs}
    mount /dev/sr0 /media/cdrom/
    mount /dev/sda5 /mnt/fat
    mount /dev/sda6 /mnt/ntfs
    ```

-   Скопируйте файлы на раздел NTFS:
    ```shell
    rsync -ai /media/cdrom/ /mnt/ntfs/
    ```

-   Скопируйте необходимые файлы на раздел FAT32 (не нужно при наличии загрузчика типа refind):
    ```shell
    rsync -ai --exclude='sources/' /media/cdrom/ /mnt/fat/
    mkdir /mnt/fat/sources
    cp /media/cdrom/sources/boot.wim /mnt/fat/sources/
    ```
