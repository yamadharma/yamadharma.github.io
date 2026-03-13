---
title: "Pdf. Поиск подстроки"
author: ["Dmitry S. Kulyabov"]
date: 2023-06-27T09:28:00+03:00
lastmod: 2023-06-27T12:13:00+03:00
draft: false
slug: "pdf-grep"
---

Поиск подстроки в pdf-файле.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> pdfgrep {#pdfgrep}

-   pdfgrep пытается быть совместимым с GNU grep.


### <span class="section-num">1.1</span> Установка {#установка}

-   Gentoo
    ```shell
    emerge app-text/pdfgrep
    ```


### <span class="section-num">1.2</span> Использование {#использование}

-   Синтаксис pdfgrep:
    ```shell
    pdfgrep [OPTION] PATTERN FILE.pdf
    ```
-   Опции:
    -   `-c`, `--count`: количество совпадений (сами совпадения не выводятся);
    -   `-p`, `--page-count`: номера страниц, на которых найдены совпадения, и количество совпадений на странице;
    -   `-n`, `--page-number`: показать номер страницы в pdf-файле;
    -   `-m NUM`, `--max-count NUM`: задаёт максимальное количество совпадений;
    -   `-i`, `--ignore-case`: поиск без учёта регистра;
    -   `-A NUM`, `--after-context NUM`: вывести число строк, следующих после совпадающих строк;
    -   `-B NUM`, `--before-context NUM`: вывести число строк перед совпадающими строками;
    -   `-C NUM`, `--context NUM`: вывести число строк до и после совпадающих строк;
    -   `--cache`: кэширование отображаемого текста для ускорения поиска;
    -   `--password PASSWORD`: пароль для файла.


## <span class="section-num">2</span> pdftotext {#pdftotext}

-   Можно преобразовать pdf в текст и искать уже в нём.


### <span class="section-num">2.1</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge app-text/poppler
    ```


### <span class="section-num">2.2</span> Использование {#использование}

-   Поиск в одном файле:
    ```shell
    pdftotext file.pdf - | grep 'pattern'
    ```

    -   `-` необходим для вывода `pdftotext` на стандартный вывод, а не в файл.
-   Поиск в нескольких файлах:
    ```shell
    find /path -name '*.pdf' -exec sh -c 'pdftotext "{}" - | grep --with-filename --label="{}" --color "pattern"' \;
    ```

    -   `-` необходим для вывода `pdftotext` на стандартный вывод, а не в файлы;
    -   параметры `--with-filename` и `--label` поместят имя файла в вывод `grep`;
    -   параметр `--color` указывает `grep` на вывод с использованием цветов на терминале.


## <span class="section-num">3</span> Локальные поисковики {#локальные-поисковики}

-   Можно использовать какой-либо из локальных поисковиков.
-   [Локальные поисковики]({{< relref "2023-06-27-desktop-search" >}})
