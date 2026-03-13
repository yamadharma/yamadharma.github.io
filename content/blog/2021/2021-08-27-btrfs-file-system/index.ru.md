---
title: "Файловая система btrfs"
author: ["Dmitry S. Kulyabov"]
date: 2021-08-27T11:33:00+03:00
lastmod: 2024-02-19T15:46:00+03:00
tags: ["btrfs", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "btrfs-file-system"
---

Файловая система _Btrfs_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


### <span class="section-num">1.1</span> Свойства {#свойства}

-   Копирование при записи (copy on write --- CoW).
    -   Все копии файла суммарно занимают на диске столько же места сколько оригинал, а при изменениях файлов данные всегда пишутся в новые страницы.
-   Снапшоты.
    -   Можно делать снимки состояния подтома на лету, а потом вернуть это состояние, например, после неудачного обновления или удаления чего-то нужного, просто отредактировав `/etc/fstab` и выполнив `mount -o remount mountpoint`.
    -   Для автоматического создания снапшотов можно использовать утилиту `snapper`.
-   Поддержка сжатия.
-   Поддержка подтомов.
    -   Вместо разделов предпочтительно использовать подтома.
    -   Подтома имеют динамический размер.
    -   Снапшоты являются по сути подтомами.
-   Поддержка дисков SSD.


## <span class="section-num">2</span> Опции монтирования {#опции-монтирования}


### <span class="section-num">2.1</span> SSD TRIM {#ssd-trim}

-   Файловая система Btrfs может освобождать неиспользуемые блоки с SSD диска, поддерживающего команду TRIM.
-   Поддерживается асинхронный discard, который доступен в виде опции монтирования `discard=async`.
    -   Включено по умолчанию начиная с linux 6.2.
    -   Незанятые экстенты не освобождаются сразу, а группируются и освобождаются позже в отдельном потоке, что улучшает задержки при записи на диск.
    -   Асинхронный discard можно безопасно использовать вместе с периодическим TRIM.


## <span class="section-num">3</span> Разное {#разное}

-   [Перенос Linux на btrfs]({{< relref "2021-05-21-installing-linux-btrfs" >}})
-   [Подтома btrfs]({{< relref "2021-08-27-btrfs-subvolumes" >}})
-   [btrfs. Контрольные суммы]({{< relref "2024-02-19-btrfs-checksumming" >}})


## <span class="section-num">4</span> Обслуживание btrfs {#обслуживание-btrfs}

-   [Обслуживание btrfs]({{< relref "2021-09-23-btrfs-maintenence" >}})
-   [Дедупликация файловой системы btrfs]({{< relref "2022-05-26-deduplication-btrfs-filesystem" >}})
-   [Восстановление btrfs]({{< relref "2023-07-21-btrfs-recovery" >}})


## <span class="section-num">5</span> Необходимое программное обеспечение {#необходимое-программное-обеспечение}


### <span class="section-num">5.1</span> btrfs-progs {#btrfs-progs}

-   Утилиты для работы с _btrfs_.
-   Установка
    -   Gentoo
        ```shell
        emerge sys-fs/btrfs-progs
        ```


### <span class="section-num">5.2</span> btrfsmaintenance {#btrfsmaintenance}

-   Скрипт для регулярного обслуживания файловой системы _btrfs_
-   Установка
    -   Gentoo
        ```shell
        emerge sys-fs/btrfsmaintenance
        ```


### <span class="section-num">5.3</span> snapper {#snapper}

-   Управление снапшотами
-   Установка
    -   Gentoo
        ```shell
        emerge app-backup/snapper
        ```


## <span class="section-num">6</span> Ресурсы {#ресурсы}

-   Документация: <https://btrfs.readthedocs.io/>
