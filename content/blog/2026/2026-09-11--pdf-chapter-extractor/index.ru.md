---
title: "Скрипт PDF Chapter Extractor"
author: ["Dmitry S. Kulyabov"]
date: 2026-09-11T20:40:00+03:00
lastmod: 2026-09-11T20:52:00+03:00
tags: ["pdf"]
categories: ["computer-science"]
draft: false
slug: "pdf-chapter-extractor"
---

Скрипт PDF Chapter Extractor.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/ahmedalmagraby/pdf_chapter_extractor>
-   Для разделения PDF-файлов на отдельные главы на основе их метаданных (закладок/оглавления).
-   Также позволяет извлекать произвольные диапазоны страниц и объединять несколько PDF-документов в один.
-   Использует библиотеку `pypdf`.


### <span class="section-num">1.1</span> Основные возможности {#основные-возможности}

-   Извлечение глав по закладкам
    -   Разделение PDF-файла на части в зависимости от уровня вложенности закладок (уровни `0`, `1`, `2` и т.д.).
-   Выборочное извлечение.
-   Извлечение диапазонов страниц.
-   Объединение нескольких pdf-файлов в один.


## <span class="section-num">2</span> Установка {#установка}

-   Нужно иметь установленную библиотеку `pypdf`:

<!--listend-->

```shell
uv tool install pypdf
```


## <span class="section-num">3</span> Основные команды {#основные-команды}


### <span class="section-num">3.1</span> Извлечение глав {#извлечение-глав}

-   Извлекает главы, используя верхний (корневой) уровень закладок:

<!--listend-->

```shell
python pdf_chapter_extractor.py input.pdf
```


### <span class="section-num">3.2</span> Расширенное извлечение глав {#расширенное-извлечение-глав}

-   Извлечение закладок 1-го уровня вложенности (разделы ##) с сохранением в отдельную папку `chapters`:

<!--listend-->

```shell
python pdf_chapter_extractor.py input.pdf -o chapters -l 1
```


### <span class="section-num">3.3</span> Анализ документа {#анализ-документа}

-   Просмотр метаданных и дерева закладок без создания файлов:

<!--listend-->

```shell
python pdf_chapter_extractor.py input.pdf --inspect-only
```


### <span class="section-num">3.4</span> Извлечение диапазона страниц {#извлечение-диапазона-страниц}

-   Сохраняет страницы с 10-й по 25-ю (включительно).
-   Нумерация начинается с 1:

<!--listend-->

```shell
python pdf_chapter_extractor.py input.pdf --page-range 10-25
```


### <span class="section-num">3.5</span> Объединение PDF-файлов {#объединение-pdf-файлов}

-   Склеивает несколько файлов в один с именем `combined.pdf`:

<!--listend-->

```shell
python pdf_chapter_extractor.py --merge file1.pdf file2.pdf file3.pdf -o combined.pdf
```


### <span class="section-num">3.6</span> Запуск графического интерфейса {#запуск-графического-интерфейса}

```shell
python pdf_chapter_extractor.py --gui
```
