---
title: "LaTeX. Пакет pax"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-04T20:58:00+03:00
lastmod: 2025-05-05T14:19:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex-pax"
---

LaTeX. Пакет pax.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   CTAN: <https://ctan.org/pkg/pax>
-   Пакет pax решает проблему потери кликабельных ссылок и аннотаций при включении PDF-файлов через пакет `pdfpages`.
-   Он работает в связке с Java-программой, которая извлекает данные о ссылках и сохраняет их для восстановления в финальном документе.


## <span class="section-num">2</span> Основные функции {#основные-функции}

-   Восстановление ссылок
    -   Сохраняет гиперссылки, закладки и аннотации из исходного PDF при вставке через `pdfpages`.
-   Поддержка интерактивности
    -   Позволяет кликать на ссылки, добавленные из внешнего PDF.
-   Совместимость
    -   Работает с `pdfLaTeX` и `LuaLaTeX`, но не поддерживает `XeLaTeX`.


## <span class="section-num">3</span> Зависимости {#зависимости}

-   Зависимости
    -   Java
    -   Perl
    -   PDFBox
    -   LaTeX-пакеты: `pax.sty`, `pdfpages`.


## <span class="section-num">4</span> Использование {#использование}


### <span class="section-num">4.1</span> Генерация pax-файла. {#генерация-pax-файла-dot}

-   Запустите команду для исходного pdf:
    ```shell
    java -jar pax.jar input.pdf
    ```

-   Можно использовать  Perl-скрипт:
    ```shell
    pdfannotextractor.pl input.pdf
    ```
-   В результате получаем файл `input.pax`.


### <span class="section-num">4.2</span> Вставка pdf в LaTeX {#вставка-pdf-в-latex}

-   В преамбуле для pdfLaTeX подключите пакеты:
    ```tex
    \usepackage{pdfpages}
    \usepackage{pax}
    ```

-   Для LuaLaTeX добавьте:
    ```tex
    \usepackage{pdftexcmds}
    \makeatletter
    \let\pdfescapename=\pdf@escapename
    \let\pdfstrcmp=\pdf@strcmp
    \makeatother
    \usepackage{pax}
    ```

-   Вставьте pdf:
    ```tex
    \includepdf[pages=-]{input.pdf}
    ```
