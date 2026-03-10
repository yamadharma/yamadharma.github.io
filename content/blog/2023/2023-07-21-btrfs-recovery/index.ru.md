---
title: "Восстановление btrfs"
author: ["Dmitry S. Kulyabov"]
date: 2023-07-21T16:56:00+03:00
lastmod: 2024-03-17T20:50:00+03:00
tags: ["sysadmin", "btrfs"]
categories: ["computer-science"]
draft: false
slug: "btrfs-recovery"
---

Восстановление btrfs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Предварительная подготовка {#предварительная-подготовка}

-   Подготовьте флеш-диск (см. [Загрузочная флешка]({{< relref "2021-04-10-bootable-usb-stick" >}}))
-   Поместите на него образ SystemRescueCD (<https://www.system-rescue.org/>).


## <span class="section-num">2</span> Восстановление {#восстановление}

-   Загружаемся с внешнего устройства.
    -   При загрузке с SystemRescueCD лучше выбрать пункт `copy system to RAM`.
-   Запускаем проверку блоков:
    ```shell
    mount /dev/sda1 /mnt
    btrfs scrub start -Bd /mnt
    ```
-   Если система на монтируется, проверяем блоки на устройстве:
    ```shell
    btrfs scrub start -Bd /dev/sda1
    ```
-   Если не монтируется, попробуйте смонтировать для чтения:
    ```shell
    mount -o rescue /dev/sda1 /mnt
    ```
-   Запустите проверку файловой системы:
    ```shell
    btrfs check /dev/sda1
    ```
-   Если не поможет, скопируйте файловую систему:
    ```shell
    btrfs restore /dev/sda1 /mnt/usbdrive
    ```
-   Попробуйте восстановить суперблок:
    ```shell
    btrfs rescue super-recover /dev/sda1
    ```

    -   Попробуйте смонтировать устройство. Если смонтируется нормально, завершайте.
-   Попробуйте удалить лог:
    ```shell
    btrfs rescue zero-log /dev/sda1
    ```

    -   Попробуйте смонтировать устройство. Если смонтируется нормально, завершайте.
-   Попробуйте восстановить чанки:
    ```shell
    btrfs rescue chunk-recover /dev/sda1
    ```

    -   Попробуйте смонтировать устройство. Если смонтируется нормально, завершайте.
-   Запускаем восстановление файловой системы на устройстве (это может быть опасно):
    ```shell
    btrfs check --repair /dev/sda1
    ```
-   Запускаем проверку блоков:
    ```shell
    mount /dev/sda1 /mnt
    btrfs scrub start -Bd /mnt
    ```
