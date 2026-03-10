---
title: "BibTeX. Утилита Bibtool"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-25T19:15:00+03:00
lastmod: 2025-04-25T19:34:00+03:00
tags: ["latex", "bib"]
categories: ["computer-science"]
draft: false
slug: "bibtex-bibtool"
---

BibTeX. Утилита Bibtool.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   BibTool --— консольная утилита для работы с файлами BibTeX, предназначенная для автоматизации управления библиографическими базами данных.
-   Сайт: <https://www.gerd-neugebauer.de/software/TeX/BibTool/en/>
-   Репозиторий: <https://github.com/ge-ne/bibtool>
-   CTAN: <https://www.ctan.org/tex-archive/biblio/bibtex/utils/bibtool/>


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   В основном репозитории:
    ```shell
    emerge bibtool
    ```


## <span class="section-num">3</span> Основные операции {#основные-операции}

-   Сортировка записей
    -   Автоматическая сортировка библиографических записей по ключам, авторам, годам и другим параметрам.
    -   Поддержка прямого (`-s`) и обратного (`-S`) порядка сортировки.
        ```shell
        bibtool -s input.bib -o sorted.bib
        ```

-   Удаление дубликатов
    -   Поиск и удаление повторяющихся записей по ключам или содержимому.
    -   Ресурс `check.double` для проверки дубликатов.
        ```shell
        bibtool -- 'check.double = on' input.bib
        ```
    -   Создание чистого файла без дубликатов:
        ```shell
        bibtool -- 'check.double = on' -s input.bib -o clean.bib
        ```

-   Извлечение записей
    -   Фильтрация записей по ключам, авторам, годам или регулярным выражениям.
    -   Интеграция с `.aux`-файлами LaTeX для извлечения только используемых ссылок:
        ```shell
        bibtool -x main.aux -o extracted.bib
        ```
-   Генерация ключей
    -   Автоматическое создание ключей BibTeX в коротком (`-k`) или длинном (`-K`) формате.
    -   Настройка шаблонов ключей через ресурс `key.format`.
        ```shell
        bibtool -k input.bib -o new_keys.bib
        ```
-   Проверка синтаксиса
    -   Обнаружение ошибок в структуре файлов (например, незакрытые скобки, некорректные поля).
    -   Валидация через ресурсы `validate` и `check.required.fields`.

-   Объединение файлов
    -   Слияние нескольких `.bib`-файлов в один с устранением конфликтов.
        ```shell
        bibtool -i file1.bib -i file2.bib -o merged.bib
        ```
-   Поиск записей по ключевому слову:
    ```shell
    bibtool -- 'select{title "network"}' input.bib -o filtered.bib
    ```

-   Объединение с сортировкой по годам:
    ```shell
    bibtool -s -- 'sort.format = {%D(year)}' *.bib -o sorted_by_year.bib
    ```


## <span class="section-num">4</span> Скрипты {#скрипты}

-   Для пакетной работы используются ресурсные файлы (`.rsc`):
    ```shell
    new.field.type author = AUTHOR
    key.format = {%-1n(author)}%Y%T
    ```
