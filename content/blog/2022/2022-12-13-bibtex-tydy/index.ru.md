---
title: "Bibtex. Пакет bibtex-tydy"
author: ["Dmitry S. Kulyabov"]
date: 2022-12-13T17:27:00+03:00
lastmod: 2024-08-05T18:47:00+03:00
tags: ["bib", "tex"]
categories: ["computer-science"]
draft: false
slug: "bibtex-tydy"
---

Пакет bibtex-tydy позволяет выполнить проверку и чистку bib-файлов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/FlamingTempura/bibtex-tidy>
-   Написано на Javascript.
-   Можно использовать без установки из броузера: <https://flamingtempura.github.io/bibtex-tidy/>.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> pnpm {#pnpm}

-   Установка:
    ```shell
    pnpm add -g bibtex-tidy
    ```


### <span class="section-num">2.2</span> yarn {#yarn}

-   Установка:
    ```shell
    yarn global add bibtex-tidy
    ```


### <span class="section-num">2.3</span> npm {#npm}

-   Установка:
    ```shell
    npm install -g bibtex-tidy
    ```


## <span class="section-num">3</span> Примеры использования {#примеры-использования}


### <span class="section-num">3.1</span> Общий формат использования {#общий-формат-использования}

-   Запустите из командной строки:
    ```shell
    bibtex-tidy references.bib
    ```


### <span class="section-num">3.2</span> Не преобразовывать символы {#не-преобразовывать-символы}

-   По умолчанию производится экранирование не-ASCII символов: умляуты, русские буквы.
-   Если используется UTF-8, то данное поведение можно отключить:
    ```shell
    bibtex-tidy --no-escape references.bib
    ```


### <span class="section-num">3.3</span> Удаление дубликатов записей {#удаление-дубликатов-записей}

-   По умолчанию сообщается о наличии дублирующих записей.
-   Их можно слить вместе (то есть дубликаты будут удалены):
    ```shell
    bibtex-tidy --no-escape --merge references.bib
    ```
-   Существуют различные способы слияния:
    -   `first` : сохраняется только исходная запись;
    -   `last` : сохраняется только последний найденный дубликат;
    -   `combine` : сохранить исходную запись и объединить поля дубликатов, если они не существуют;
    -   `overwrite` : сохранить оригинальную запись и объединить поля дубликатов, перезаписывая существующие поля, если они уже существуют.
-   Для идентификации дубликатов можно использовать опцию `--duplicates`:
    -   `--duplicates doi` : одинаковые DOI;
    -   `--duplicates key` : одинаковые идентификаторы (ключи) записи;
    -   `--duplicates abstract` : одинаковые рефераты;
    -   `--duplicates citation` : одинаковые автор и заглавие);
    -   `--duplicates doi,key` : одинаковые DOI или ключи;
    -   `--duplicates` : одинаковые DOI, ключ, реферат или цитирование.


### <span class="section-num">3.4</span> Двойные скобки в поле `title` {#двойные-скобки-в-поле-title}

-   Bibtex переводит в поле `title` все прописные буквы (кроме первой) в строчные.
-   Чтобы избежать такое поведение, рекомендуется заключить значение поля `title` в двойные фигурные скобки.
-   В связи с этим возникает две задачи: поставить двойные фигурные скобки и убрать двойные фигурные скобки для поля `title`.
-   Поставить двойные фигурные скобки для поля `title`:
    ```shell
    bibtex-tidy --no-escape --enclosing-braces references.bib
    ```

    -   Можно задать список полей, которые следует заключить в двойные фигурные скобки:
        ```shell
        --enclosing-braces=title,journal
        ```
    -   Команда `--enclosing-braces` без опций эквивалентна команде `--enclosing-braces=title`.
-   Убрать двойные фигурные скобки для поля `title`:
    ```shell
    bibtex-tidy --no-escape --remove-braces references.bib
    ```

    -   Можно задать список полей, которые следует заключить в двойные фигурные скобки:
        ```shell
        --remove-braces=title,journal
        ```
    -   Команда `--remove-braces` без опций эквивалентна команде `--remove-braces=title`.
-   Убрать двойные фигурные скобки для всех полей:
    ```shell
    bibtex-tidy --no-escape --strip-enclosing-braces references.bib
    ```


### <span class="section-num">3.5</span> Красивости {#красивости}


#### <span class="section-num">3.5.1</span> Сортировка полей {#сортировка-полей}

-   Сортировать поля внутри записей выполняется с помощью ключа `--sort-fields`.
-   В качестве параметра задаётся список сортировки полей.
-   Если поля не указаны, то поля будут отсортированы следующим образом: title, shorttitle, author, year, month, day, journal, booktitle, location, on, publisher, address, series, volume, number, pages, doi, isbn, issn, url, urldate, copyright, category, note, metadata.


#### <span class="section-num">3.5.2</span> Сортировка записей {#сортировка-записей}

-   Сортировать записей выполняется с помощью ключа `--sort`.
-   В качестве параметра задаётся список полей.
-   Для сортировки по убыванию, добавьте к полю префикс тире (`-`).
-   Например:
    -   `--sort` : сортировка по идентификатору (ключу);
    -   `--sort=-year,name` : сортировать год по убыванию, а имя по возрастанию.


#### <span class="section-num">3.5.3</span> Прописные буквы {#прописные-буквы}

-   Если есть значения полей, записанные полностью прописными буквами, то можно переведите их в регистр с первыми заглавными буквами:
    ```shell
    bibtex-tidy --no-escape --drop-all-caps references.bib
    ```
-   Например, `{JOURNAL OF TEA}` станет `{Journal of Tea}`.
