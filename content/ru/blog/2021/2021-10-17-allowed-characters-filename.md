---
title: "Допустимые символы в имени файла"
author: ["Dmitry S. Kulyabov"]
date: 2021-10-17T20:40:00+03:00
lastmod: 2023-07-14T17:43:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "allowed-characters-filename"
---

Допустимые символы в имени файла.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Для Windows базируемся на документе <https://docs.microsoft.com/ru-ru/windows/win32/fileio/naming-a-file>.


## <span class="section-num">2</span> Запрещённые печатные символы ASCII {#запрещённые-печатные-символы-ascii}


### <span class="section-num">2.1</span> Linux/Unix {#linux-unix}

-   `/` (forward slash)


### <span class="section-num">2.2</span> Windows {#windows}

-   `<` (less than)
-   `>` (greater than)
-   `:` (colon), в NTFS имеет семантику альтернативных потоков данных (Alternate Data Streams)
-   `"` (double quote)
-   `/` (forward slash)
-   `\` (backslash)
-   `|` (vertical bar or pipe)
-   `?` (question mark)
-   `*` (asterisk)


## <span class="section-num">3</span> Непечатаемые символы {#непечатаемые-символы}


### <span class="section-num">3.1</span> Linux/Unix {#linux-unix}

-   `0` или `NUL` (NULL byte)


### <span class="section-num">3.2</span> Windows {#windows}

-   `0`--`31` (ASCII control characters)


## <span class="section-num">4</span> Зарезервированные имена файлов {#зарезервированные-имена-файлов}


### <span class="section-num">4.1</span> Windows {#windows}

-   `CON`
-   `PRN`
-   `AUX`
-   `NUL`
-   `COM1`
-   `COM2`
-   `COM3`
-   `COM4`
-   `COM5`
-   `COM6`
-   `COM7`
-   `COM8`
-   `COM9`
-   `LPT1`
-   `LPT2`
-   `LPT3`
-   `LPT4`
-   `LPT5`
-   `LPT6`
-   `LPT7`
-   `LPT8`
-   `LPT9`


## <span class="section-num">5</span> Другие ограничения {#другие-ограничения}


### <span class="section-num">5.1</span> Windows {#windows}

-   Имена файлов не могут заканчиваться пробелом или точкой.


### <span class="section-num">5.2</span> macOS {#macos}

-   Двоеточие `:` и косая черта `/` запрещены в зависимости от контекста.
-   Двоеточие `:` используется в качестве разделителя в путях HFS, а косая черта `/` используется в качестве разделителя в путях POSIX.
