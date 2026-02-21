---
title: "Буфер обмена. wl-clipboard"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-11T09:28:00+03:00
lastmod: 2025-03-11T09:29:00+03:00
tags: ["wayland", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "clipboard-wl-clipboard"
---

Буфер обмена. wl-clipboard.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Простой инструмент копирования и вставки для композиторов Wayland.
-   Репозиторий: <https://github.com/bugaevc/wl-clipboard>
-   Содержит две утилиты буфера обмена Wayland: `wl-copy` и `wl-paste`.


## <span class="section-num">2</span> Использование {#использование}

-   Копирование простого текстового сообщения:
    ```shell
    wl-copy Hello world!
    ```
-   Копирование списка файлов в папке:
    ```shell
    ls ~/Downloads | wl-copy
    ```
-   Копирование изображения:
    ```shell
    wl-copy < ~/Pictures/photo.png
    ```
-   Копирование предыдущей команды:
    ```shell
    wl-copy "!!"
    ```
-   Вставка в файл:
    ```shell
    wl-paste > clipboard.txt
    ```
-   Сортировка содержимого буфера обмена:
    ```shell
    wl-paste | sort | wl-copy
    ```
-   Выгрузка содержимого буфера обмена в pastebin при каждом изменении:
    ```shell
    wl-paste --watch nc paste.example.org 5555
    ```
