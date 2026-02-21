---
title: "Преобразование djvu в pdf"
author: ["Dmitry S. Kulyabov"]
date: 2024-07-26T18:54:00+03:00
lastmod: 2025-04-29T16:54:00+03:00
tags: ["pdf"]
categories: ["computer-science"]
draft: false
slug: "convert-djvu-pdf"
---

Преобразование djvu в pdf.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Формат DjVu оптимизирует сжатие отсканированных документов, таких как книги, журналы и тексты с большим количеством изображений.
-   Он уменьшает размер файла, сохраняя качество, особенно для высококонтрастных изображений и текста.
-   Это делает DjVu идеальным для хранения больших коллекций отсканированных материалов, где важна эффективность хранения.
-   PDF является одним из наиболее широко используемых форматов для обмена, просмотра и печати документов.
-   PDF также поддерживает такие функции, как аннотации, цифровые подписи и текстовый поиск, которые не всегда доступны в DjVu.


## <span class="section-num">2</span> Использование DjVuLibre {#использование-djvulibre}

-   DjVuLibre --- набор инструментов и библиотек для работы с файлами DjVu.
-   Он широко используется для просмотра, создания и конвертации документов DjVu.
-   Сайт: <https://djvu.sourceforge.net/>


### <span class="section-num">2.1</span> Преобразование одного файла DjVu в PDF {#преобразование-одного-файла-djvu-в-pdf}

-   Преобразовать один файл DjVu в PDF:
    ```shell
    ddjvu -format=pdf input.djvu output.pdf
    ```
-   По умолчанию DjVuLibre сохраняет преобразованный PDF в том же каталоге, что и входной файл DjVu.
-   Можно указать желаемый выходной путь:
    ```shell
    ddjvu -format=pdf input.djvu /path/to/output/folder/output.pdf
    ```


### <span class="section-num">2.2</span> Преобразование нескольких файлов DjVu в PDF {#преобразование-нескольких-файлов-djvu-в-pdf}

-   Пакетное преобразование нескольких файлов DjVu:
    ```bash
    for file in *.djvu; do ddjvu -format=pdf "$file" "${file%.djvu}.pdf"; done
    ```


### <span class="section-num">2.3</span> Настройка параметров преобразования {#настройка-параметров-преобразования}

-   Можно настроить качество PDF с помощью параметра `-quality`, который принимает значения от 25 до 150 точек на дюйм (DPI).
-   Установим значение `-quality` равным 150:
    ```shell
    ddjvu -format=pdf -quality=150 input.djvu output.pdf
    ```
-   Включим определённые страницы в преобразование, используя опцию `-page`:
    ```shell
    ddjvu -format=pdf -page=1-5 input.djvu output.pdf
    ```

    -   Эта команда преобразует только страницы с 1 по 5  файла DjVu в новый PDF-файл.


## <span class="section-num">3</span> Использование ImageMagick {#использование-imagemagick}

-   ImageMagick ---  универсальное программное обеспечение с открытым исходным кодом, подходящее для обработки изображений.
-   Оно поддерживает различные форматы файлов и предлагает надежные инструменты для преобразования и редактирования изображений и документов, включая файлы DjVu.
-   Сайт: <https://imagemagick.org>
-   Репозиторий: <https://github.com/ImageMagick/ImageMagick>


### <span class="section-num">3.1</span> Преобразование одного файла DjVu в PDF {#преобразование-одного-файла-djvu-в-pdf}

-   Будем использовать утилиту `convert`:
    ```shell
    convert input.djvu output.pdf
    ```
-   Для корректного выполнения этой команды нужно убедиться, что политика безопасности ImageMagick разрешает чтение и запись PDF-файлов.
-   Проверим файл `/etc/ImageMagick-7/policy.xml`:
    ```xml
    <policy domain="coder" rights="read|write" pattern="PDF" />
    ```


### <span class="section-num">3.2</span> Преобразование нескольких файлов DjVu в PDF {#преобразование-нескольких-файлов-djvu-в-pdf}

-   Одновременная обработки нескольких файлов DjVu:
    ```bash
    for file in *.djvu; do convert "$file" "${file%.djvu}.pdf"; done
    ```


### <span class="section-num">3.3</span> Настройка параметров преобразования {#настройка-параметров-преобразования}

-   Изменим разрешение вывода с помощью опции `-density`:
    ```shell
    convert -density 120 input.djvu output.pdf
    ```

    -   Это устанавливает разрешение 120 точек на дюйм (DPI).
-   Чтобы извлечь определённые страницы, укажем диапазон страниц:
    ```c
    convert input.djvu[0-3] output.pdf
    ```

    -   Здесь страницы с 1 по 4 (индекс начинается с 0) преобразуются в PDF.

-   Для управления размером PDF-файлов мы можем использовать комбинацию параметров `-density=и =-quality`:
    ```c
    convert -density 120 -quality 90 input.djvu output.pdf
    ```

    -   Параметр `-quality` управляет качеством сжатия.
    -   Его значение варьируется от 1 до 100.


## <span class="section-num">4</span> Утилиты {#утилиты}

-   [Конвертация djvu в pdf. dpsprep]({{< relref "2025-04-29--convert-djvu-pdf-dpsprep" >}})
