---
title: "Дедупликация файлов. jdupes"
author: ["Dmitry S. Kulyabov"]
date: 2024-02-23T18:08:00+03:00
lastmod: 2024-02-23T20:02:00+03:00
tags: ["sysadmin", "btrfs"]
categories: ["computer-science"]
draft: false
slug: "file-deduplication-jdupes"
---

Дедупликация файлов. jdupes.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.jdupes.com/>
-   Репозиторий:
    -   <https://codeberg.org/jbruchon/jdupes>
    -   ~~<https://github.com/jbruchon/jdupes>~~
-   Форк `fdupes`.
-   Включает поддержку дедупликации BTRFS.


## <span class="section-num">2</span> Примеры {#примеры}

-   Команда применяется к списку каталогов.
-   Найти дубликаты файлов:
    ```shell
    jdupes --recurse --print-summarize dir1 dir2
    ```
-   Преобразовать дубликаты в жёсткие ссылки:
    ```shell
    jdupes --recurse --link-hard dir1 dir2
    ```
