---
title: "Gentoo. Пакет installkernel"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-22T11:58:00+03:00
lastmod: 2025-05-22T14:05:00+03:00
tags: ["sysadmin", "gentoo", "linux"]
categories: ["computer-science"]
draft: false
slug: "gentoo-installkernel"
---

Gentoo. Пакет installkernel.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/projg2/installkernel-gentoo>
-   Wiki: <https://wiki.gentoo.org/wiki/Installkernel>
-   Installkernel --— это набор скриптов для автоматической установки новых ядер и обновления загрузчика конфигурации.


## <span class="section-num">2</span> Основные команды {#основные-команды}

-   Установка ядра:
    ```shell
    kernel-install add KERNEL-VERSION KERNEL-IMAGE [INITRD-FILE...]
    ```

-   Удаление ядра:
    ```shell
    kernel-install remove KERNEL-VERSION
    ```

-   Просмотр установленных ядер:
    ```shell
    kernel-install list
    ```

-   Установка всех ядер:
    ```shell
    kernel-install add-all
    ```
-   Дополнительно можно использовать `eclean-kernel`.


## <span class="section-num">3</span> Конфигурация {#конфигурация}

-   Файлы конфигурации:
    -   `/etc/kernel/install.conf`;
    -   `/usr/lib/kernel/install.conf`;
    -   первый имеет приоритет над вторым.
-   Параметра конфигурации:
    ```conf-unix
    layout=
    initrd_generator=
    uki_generator=
    ```


### <span class="section-num">3.1</span> layout {#layout}

-   Поддерживается спецификации загрузчика:
    -   тип 1 ( `layout=bls` );
        -   используется с `systemd-boot`;
        -   рекомендуется включить USE-флаг `systemd-boot`;
        -   создает файлы в формате, совместимом с `systemd-boot`;

    -   тип 2 ( `layout=uki` );
        -   предназначен для использования в унифицированных образах ядра и поддерживается grub, systemd-boot, refind;
    -   для использования с GRUB ( `layout=grub` );
        -   чтобы использовать GRUB в сочетании с _Unified Kernel Images_, используйте раскладку `uki`;
    -   если USE-флаги grub , systemd-boot , efistub и uki отключены, используется макет, который обратно совместим с installkernel Debian (`layout=compat`);
        -   используется по умолчанию при отсутствии других USE-флагов;
        -   совместим с традиционным installkernel;
        -   обеспечивает обратную совместимость;
        -   рекомендуется для систем с нестандартными загрузчиками.

-   Макет `uki` (включенный USE-флагом `uki`) имеет приоритет над макетом `bls` (включенным USE-флагом `systemd-boot`), который, в свою очередь, имеет приоритет над макетом `grub` (включенным USE-флагом `grub`).


#### <span class="section-num">3.1.1</span> compat {#compat}

-   Макет compat очень похож на макет в традиционном installkernel Debian:
    ```shell
    /boot/initramfs-xyz-gentoo-dist.img            # Если USE=dracut (или другой генератор initramfs)
    /boot/kernel-xyz-gentoo-dist
    ```


#### <span class="section-num">3.1.2</span> efistub {#efistub}

-   Макет `efistub` идентичен макету `compat`, но перемещен в системный раздел EFI для загрузки EFI stub.
-   Образ ядра имеет суффикс `.efi`:
    ```shell
    /${ESP}/EFI/Gentoo/initramfs-xyz-gentoo-dist.img        # Если USE=dracut (или другой генератор initramfs)
    /${ESP}/EFI/Gentoo/kernel-xyz-gentoo-dist.efi
    ```


#### <span class="section-num">3.1.3</span> grub {#grub}

-   Макет grub идентичен макету compat с добавлением grub.cfg:
    ```shell
    /boot/grub/grub.cfg
    /boot/initramfs-xyz-gentoo-dist.img             # Если USE=dracut (или другой генератор initramfs)
    /boot/kernel-xyz-gentoo-dist
    ```


#### <span class="section-num">3.1.4</span> bls {#bls}

-   The Bootloader Specification Type 1
-   Используется в `systemd-boot`:
    ```shell
    /${ESP}/gentoo/xyz-gentoo-dist/initrd            # Если USE=dracut (или другой генератор initramfs)
    /${ESP}/gentoo/xyz-gentoo-dist/linux
    /${ESP}/loader/entries/gentoo-xyz-gentoo-dist.conf
    ```


#### <span class="section-num">3.1.5</span> uki {#uki}

-   The Bootloader Specification Type 2:
    ```shell
    /boot/grub/grub.cfg                                 # Если USE=grub
    /${ESP}/EFI/Linux/gentoo-xyz-gentoo-dist.efi
    ```


### <span class="section-num">3.2</span> initrd_generator {#initrd-generator}

-   Параметр определяет, какой плагин должен использоваться для генерации `initramfs`.
-   В настоящее время единственным пакетом, который устанавливает такой плагин, является Dracut из `sys-kernel/dracut`.
-   Если флаг `USE=dracut` включён, этот параметр автоматически устанавливается в значение `dracut`.
-   В противном случае для этого параметра автоматически устанавливается значение `none`.


### <span class="section-num">3.3</span> uki_generator {#uki-generator}

-   Параметр управляет тем, какой плагин следует использовать для генерации унифицированного образа ядра.
-   Пакеты предоставляют такой плагин:
    -   `sys-kernel/dracut`;
    -   `systemd` (через флаг `ukify` в `sys-apps/systemd` и `sys-apps/systemd-utils`).
    -   Когда включен флаг `USE=ukify`, этот параметр автоматически устанавливается в `ukify`.
    -   Когда флаг `USE=ukify` отключен, но включены флаги `USE` `dracut` и `uki`, этот параметр автоматически устанавливается в `dracut`.
    -   В противном случае этот параметр автоматически устанавливается в `none`.


## <span class="section-num">4</span> Особенности {#особенности}


### <span class="section-num">4.1</span> dracut {#dracut}


#### <span class="section-num">4.1.1</span> hostonly {#hostonly}

-   Начиная с версии `sys-kernel/dracut-106` значение по умолчанию для параметра `hostonly` изменилось с отключенного на включенное.
-   `hostonly` :настройка для Dracut, которая управляет тем, сколько данных будет включено в создаваемый образ initramfs.
-   Когда она отключена, Dracut стремится сгенерировать образ initramfs, загружаемый на любом оборудовании.
-   Когда этот параметр включен, Dracut стремится сгенерировать образ initramfs, содержащий только то, что необходимо для загрузки текущей системы.
-   Настройка `hostonly` может быть отключена с помощью в `/etc/dracut.conf.d/`:
    ```shell
    mkdir -p /etc/dracut.conf.d
    echo "hostonly=no" >> /etc/dracut.conf.d/95-no-hostonly.conf
    ```


## <span class="section-num">5</span> Сравнение ukify и dracut {#сравнение-ukify-и-dracut}


### <span class="section-num">5.1</span> Основные возможности {#основные-возможности}

-   Dracut
    -   Создает как UKI (Unified Kernel Image), так и initramfs самостоятельно
    -   Имеет встроенный механизм создания initramfs
    -   Автоматически генерирует UKI при включении соответствующих флагов
    -   Поддерживает автоматическую установку в EFI System Partition
-   Ukify
    -   Создает только UKI, требует отдельный initramfs генератор
    -   Работает с любым initramfs, созданным сторонними инструментами
    -   Требует отдельной настройки initramfs через UgRD или Dracut
    -   Более гибкая интеграция с существующими initramfs


### <span class="section-num">5.2</span> Настройка и конфигурация {#настройка-и-конфигурация}

-   Dracut
    -   Конфигурация в файле `/etc/dracut.conf`
    -   Параметры командной строки ядра задаются в `/etc/dracut.conf`
    -   Для Secure Boot требуются настройки в `/etc/dracut.conf`
    -   Автоматическая генерация UKI при установке ядра
-   Ukify
    -   Конфигурация в файле `/etc/kernel/uki.conf`
    -   Параметры командной строки ядра задаются в `/etc/kernel/cmdline`
    -   Для Secure Boot требуются настройки в `/etc/kernel/uki.conf`
    -   Необходимость отдельной настройки initramfs генератора


### <span class="section-num">5.3</span> Особенности использования {#особенности-использования}

-   Dracut
    -   Однофайловая система --- все в одном инструменте
    -   Автоматическая генерация и установка UKI
    -   Встроенная поддержка Secure Boot
    -   Простота настройки через единый конфигурационный файл
-   Ukify
    -   Модульная система - можно комбинировать с разными initramfs генераторами
    -   Более гибкая настройка параметров UKI
    -   Интеграция с systemd-specific функциями


### <span class="section-num">5.4</span> Совместимость и интеграция {#совместимость-и-интеграция}

-   Dracut
    -   Лучше интегрирован с традиционными системами
    -   Поддерживает большинство загрузчиков без дополнительной настройки
    -   Автоматически определяет и использует существующую конфигурацию
-   Ukify
    -   Лучше работает с systemd-based системами
    -   Оптимизирован для современных UEFI систем
    -   Требует дополнительной настройки при использовании нестандартных initramfs


### <span class="section-num">5.5</span> Рекомендации по выбору {#рекомендации-по-выбору}

-   Используйте Dracut, если:
    -   Нужна простая и единая система управления UKI и initramfs
    -   Важна автоматическая генерация и установка
    -   Используется традиционный подход к настройке системы

-   Используйте Ukify, если:
    -   Нужна максимальная гибкость в выборе initramfs генератора
    -   Важна поддержка Measured Boot
    -   Используется современная systemd-based система
    -   Требуется интеграция с дополнительными функциями systemd
