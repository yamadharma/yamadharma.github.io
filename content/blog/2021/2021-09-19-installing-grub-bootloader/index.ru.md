---
title: "Установка загрузчика grub"
author: ["Dmitry S. Kulyabov"]
date: 2021-09-19T13:58:00+03:00
lastmod: 2023-09-29T19:46:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "installing-grub-bootloader"
---

Установка загрузчика grub2.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.gnu.org/software/grub/grub.html>


## <span class="section-num">2</span> Установка с UEFI {#установка-с-uefi}


### <span class="section-num">2.1</span> Установка в режиме UEFI {#установка-в-режиме-uefi}

-   Обычно разделы монтируются следующим образом:
    -   `/boot`: загрузочный раздел (значение по умолчанию для опции `--boot-directory`);
    -   `/boot/efi`: раздел UEFI (значение по умолчанию для опции `--efi-directory`).
-   Установка осуществляется следующим образом:
    ```shell
    grub-install --boot-directory=/boot --efi-directory=/boot/efi --target=x86_64-efi
    ```
-   Если используются значения по умолчанию, можно просто выполнить:
    ```shell
    grub-install
    ```


### <span class="section-num">2.2</span> Установка без доступа к UEFI {#установка-без-доступа-к-uefi}

-   Используется, если нужно установить EFI-версию GRUB2
    -   из системы, загруженной в режиме BIOS;
    -   для другой архитектуры;
    -   на сменный носитель.
-   При отсутствии доступа к переменным UEFI (`efibootmgr` не работает):
    ```shell
    grub-install --boot-directory=/boot --efi-directory=/boot/efi --target=x86_64-efi --removable
    ```


## <span class="section-num">3</span> Установка в режиме chroot {#установка-в-режиме-chroot}


### <span class="section-num">3.1</span> Подмонтировать каталоги {#подмонтировать-каталоги}

-   Создадим точку монтирования
    ```shell
    mkdir /mnt/
    ```
-   Подмонтируем партиции.
    -   Например, для btrfs:
        ```shell
        mount -o subvol=@ /dev/sda4 /mnt
        mount /dev/sda2 /mnt/boot
        mount /dev/sda1 /mnt/boot/efi
        mount -o subvol=@var /dev/sda4 /mnt/var
        mount -o subvol=@var-tmp /dev/sda4 /mnt/var/tmp
        mount -o subvol=@home /dev/sda4 /mnt/home
        ```


### <span class="section-num">3.2</span> Подмонтировать виртуальные файловые системы {#подмонтировать-виртуальные-файловые-системы}

-   Для функционирования окружения _chroot_ необходимо подключить виртуальные файловые системы:
    ```shell
    mount -t proc proc /mnt/proc
    mount -t sysfs sys /mnt/sys
    mount -o bind /dev /mnt/dev
    mount -t devpts pts /mnt/dev/pts/
    mount -o bind /run /mnt/run
    ```


### <span class="section-num">3.3</span> Подмонтировать виртуальные файловые системы для случая UEFI {#подмонтировать-виртуальные-файловые-системы-для-случая-uefi}

-   Для доступа к переменным UEFI нужно подмонтировать соответствующую виртуальную файловую систему:
    ```shell
    mount -t efivarfs efivarfs /mnt/sys/firmware/efi/efivars
    ```


### <span class="section-num">3.4</span> Перейти в chroot {#перейти-в-chroot}

-   Перейдём в окружение chroot
    ```shell
    cd /mnt
    chroot /mnt
    ```


### <span class="section-num">3.5</span> Установим grub {#установим-grub}

-   Установка grub выполняется стандартным образом:
    ```shell
    grub-install
    grub-mkconfig -o /boot/grub/grub.cfg
    ```
