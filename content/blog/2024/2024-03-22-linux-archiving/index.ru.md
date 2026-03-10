---
title: "Linux. Архивирование"
author: ["Dmitry S. Kulyabov"]
date: 2024-03-22T13:42:00+03:00
lastmod: 2024-03-23T17:10:00+03:00
tags: ["linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "linux-archiving"
---

Linux. Архивирование и сжатие.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Компрессор xz {#компрессор-xz}


### <span class="section-num">1.1</span> Уровни сжатия {#уровни-сжатия}

-   `-0` .. `-3` : `-0` иногда работает быстрее, чем `gzip`, но сжимает намного лучше;
-   `-4` .. `-6` :сжатие от хорошего до очень хорошего, сохраняя при этом разумное использование памяти декомпрессора;
-   `-7` .. `-9` : похоже на `-6`, но с более высокими требованиями к памяти компрессора и декомпрессора.


### <span class="section-num">1.2</span> Переменные окружения {#переменные-окружения}

-   `XZ_OPT` : опции для текущей команды.


### <span class="section-num">1.3</span> Примеры использования {#примеры-использования}

-   Сжать файл в формат xz:
    ```shell
    xz filename
    ```
-   Сжать файл, не удаляя оригинал (опция `-k`):
    ```shell
    xz -k filename
    ```
-   Распаковать файл xz (опция `-d`, `--decompress`, `--uncompress`):
    ```shell
    xz -d filename.xz
    ```
-   Больше информации (опция `-v`):
    ```shell
    xz -v -d filename.xz
    ```
-   Распаковать файл и записать на стандартный вывод (опция `-c`):
    ```shell
    xz -dc filename.xz
    ```
-   Сжать файл, используя самое быстрое сжатие (опция `-0`):
    ```shell
    xz -0 filename
    ```
-   Сжать файл, используя лучшее сжатие  (опция `-9`):
    ```shell
    xz -9 filename
    ```
-   Указать количество используемых рабочих потоков (при выборе `0` количество потоков рассчитывается автоматически)  (опция `-T0`):
    ```shell
    xz -v -T0 -9 filename
    ```
-   Сжать весь каталог:
    ```shell
    tar -cf - dir1 | xz -9ze -T0 >dir1.txz
    ```
-   Использование `tar` с `xz` для сжатия всего каталога:
    ```shell
    tar -cJvf archive.tar.xz dir1
    ```


## <span class="section-num">2</span> Компрессор zstd {#компрессор-zstd}


### <span class="section-num">2.1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/facebook/zstd>
-   Сайт: <https://facebook.github.io/zstd/>


### <span class="section-num">2.2</span> Примеры использования {#примеры-использования}


## <span class="section-num">3</span> Архиватор tar {#архиватор-tar}


### <span class="section-num">3.1</span> Примеры использования {#примеры-использования}

-   Указание параметров для сжатия (опция `-I`, `–use-compress-program`):
    ```shell
    tar --use-compress-program='xz -9 -T0' cvf archive.tar.xz directory
    ```
-   Указание параметров для сжатия с помощью переменных окружения:
    -   xz, `XZ_OPT` : опции для текущей команды:
        ```shell
        XZ_OPT="-9 -T0" tar cJvf archive.tar.xz directory
        ```
    -   xz, `XZ_DEFAULTS` : глобальные опции:
        ```shell
        export XZ_DEFAULTS="-9 -T0"
        tar cJvf archive.tar.xz directory
        ```
