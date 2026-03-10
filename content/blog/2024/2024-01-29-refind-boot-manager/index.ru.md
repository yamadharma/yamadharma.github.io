---
title: "Загрузчик rEFInd"
author: ["Dmitry S. Kulyabov"]
date: 2024-01-29T11:41:00+03:00
lastmod: 2024-02-12T16:20:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "refind-boot-manager"
---

Загрузчик rEFInd.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.rodsbooks.com/refind/>
-   UEFI-загрузчик, способный запускать ядра EFISTUB.
-   Форк более не поддерживаемого rEFIt (только для Mac).


## <span class="section-num">2</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge sys-boot/refind
    ```


## <span class="section-num">3</span> Установка загрузчика {#установка-загрузчика}

-   Обозначим через `esp` точку монтирования системного раздела EFI.


### <span class="section-num">3.1</span> Установка скриптом {#установка-скриптом}

-   Скрипт `refind-install` устанавливает rEFInd и делает его загрузочной записью EFI по умолчанию:
    ```shell
    refind-install
    ```
-   Скрипт пытается:
    -   найти и примонтировать ESP;
    -   скопировать файлы rEFInd в `esp/EFI/refind/`;
    -   применить `efibootmgr`, чтобы сделать rEFInd загрузчиком EFI по умолчанию.
-   Можно установить rEFInd в стандартный/запасной путь загрузки `esp/EFI/BOOT/bootx64.efi`.
    -   Это полезно для загрузочных USB-устройств или для систем с проблемами с изменениями в NVRAM:
        ```shell
        refind-install --usedefault /dev/sdXY
        ```
    -   где `/dev/sdXY` --- системный раздел EFI (устройство, а не точка его монтирования).
-   По умолчанию refind-install устанавливает лишь драйвер для той файловой системы, где находится ядро.
-   Драйверы дополнительных файловых систем нужно установить:
    -   вручную копированием из `/usr/lib64/refind/drivers_x64/` в `esp/EFI/refind/drivers_x64/`
    -   задать опцию при установке:
        ```shell
        refind-install --alldrivers
        ```
-   После установки rEFInd должен создать файл `refind_linux.conf`, содержащий параметры ядра в том же каталоге, где и ядро.
-   Этот конфигурационный файл не будет создан, если Вы использовали опцию `--usedefault`.
-   В этом случае запустите:
    ```shell
    mkrlconf
    ```
-   Когда `refind-install` запускается в chroot, `/boot/refind_linux.conf` заполняется параметрами ядра из изначальной системы, а не той, куда устанавливается rEFInd.
-   Отредактируйте `/boot/refind_linux.conf` и убедитесь, что параметры ядра в нём верны.


### <span class="section-num">3.2</span> Ручная установка {#ручная-установка}

-   Скопируйте бинарный файл в ESP:
    ```shell
    mkdir -p esp/EFI/refind
    cp /usr/lib64/refind/refind_x64.efi esp/EFI/refind/
    ```

    -   Затем используйте efibootmgr, чтобы создать загрузочную запись в NVRAM UEFI, где `/dev/sdX` и `Y` --- устройство и номер раздела для вашего системного раздела EFI:
        ```shell
        efibootmgr --create --disk /dev/sdX --part Y --loader /EFI/refind/refind_x64.efi --label "rEFInd Boot Manager" --unicode
        ```
-   Если Вы хотите установить rEFInd в стандартный/запасной путь загрузки: замените esp/EFI/refind/ на esp/EFI/BOOT/ и скопируйте бинарный файл EFI rEFInd в esp/EFI/BOOT/bootx64.efi:
    ```shell
    mkdir -p esp/EFI/BOOT
    cp /usr/lib64/refind/refind_x64.efi esp/EFI/BOOT/bootx64.efi
    ```

    -   В этом случает прописывать загрузчик в NVRAM UEFI не надо.
-   rEFInd автоматически загружает все драйвера из подкаталогов `drivers` и `drivers_arch` (например, `drivers_x64`) в своем установочном каталоге
    ```shell
    mkdir esp/EFI/refind/drivers_x64
    cp /usr/lib64/refind/drivers_x64/drivername_x64.efi esp/EFI/refind/drivers_x64/
    ```
-   Скопируйте конфигурационный файл и отредактируйте настройки rEFInd:
    ```shell
    cp /usr/lib64/refind/refind.conf-sample esp/EFI/refind/refind.conf
    ```
-   Скопируйте иконки rEFInd:
    ```shell
    cp -r /usr/lib64/refind/icons esp/EFI/refind/
    ```


## <span class="section-num">4</span> Установка параллельно уже существующему UEFI Windows {#установка-параллельно-уже-существующему-uefi-windows}

-   rEFInd совместим с системным разделом EFI, созданным установкой UEFI Windows.
-   Установите rEFInd, как обычно.
-   По умолчанию, функция автообнаружения rEFInd должна опознать любые существующие загрузчики Windows.
-   Начиная с Windows 8 по умолчанию включена функция быстрого завершения работы.
    -   Помогает ускорить операции завершения и запуска.
    -   Может привести к повреждению файловой системы на мультизагрузочном компьютере.
    -   Отключить эту функцию:
        ```shell
        powercfg /h off
        ```


### <span class="section-num">4.1</span> Восстановление загрузчика {#восстановление-загрузчика}

-   После установки Windows заменяет загрузчик по умолчанию на свой.
-   Чтобы восстановить загрузку refind, необходимо запустить:
    ```shell
    bcdedit /set "{bootmgr}" path \EFI\refind\refind_x64.efi
    ```
