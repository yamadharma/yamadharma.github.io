---
title: "Использование sfdisk"
author: ["Dmitry S. Kulyabov"]
date: 2022-03-08T19:45:00+03:00
lastmod: 2023-09-19T09:08:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "using-sfdisk"
---

Использование _sfdisk_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Примеры использования {#примеры-использования}

-   Создать один большой раздел
    ```shell
    echo ';' | sfdisk /dev/sda
    ```

-   Создать один большой раздел с определённым типом раздела
    -   W95 FAT32 (LBA)
        ```shell
        echo ',,c;' | sfdisk /dev/sda
        ```
    -   lvm
        ```shell
        echo ',,8e;' | sfdisk /dev/sdd
        ```

-   Три основных раздела: два по 50 МиБ и третья на всё остальное пространство:
    ```shell
    sfdisk /dev/sda << EOF
    ,50MiB
    ,50MiB
    ;
    EOF
    ```

-   Раздел диспетчера загрузки OS2 размером 1 МБ, раздел DOS размером 50 МБ и три расширенных раздела (DOS D:, подкачка Linux, Linux):
    ```shell
    sfdisk /dev/sda << EOF
    ,1MiB,a
    ,50MiB,6
    ,,E
    ;
    ,20MiB,4
    ,16MiB,S
    ;
    EOF
    ```

-   Полезные команды
    -   список разделов
        ```shell
        sfdisk -l /dev/sda
        ```
    -   список расширенных разделов
        ```shell
        sfdisk -l -x /dev/sda
        ```
    -   список типов разделов
        ```shell
        sfdisk -T
        ```
