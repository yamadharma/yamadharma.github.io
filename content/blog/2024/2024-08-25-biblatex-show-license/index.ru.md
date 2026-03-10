---
title: "BibLaTeX. Ссылка на лицензию"
author: ["Dmitry S. Kulyabov"]
date: 2024-08-25T13:21:00+03:00
lastmod: 2024-08-25T20:31:00+03:00
tags: ["latex", "tex", "bib"]
categories: ["computer"]
draft: false
slug: "biblatex-show-license"
---

BibLaTeX. Ссылка на лицензию.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Пакет _biblatex-license_.
-   CTAN: <https://ctan.org/pkg/biblatex-license>
-   Пакет обеспечивает модификацию стандартных стилей biblatex для связи цитируемых работ с лицензией, под которой они были опубликованы.
-   Это делается с помощью встроенного в _biblatex_ механизма `related` (посредством `relatedtype=license`).


## <span class="section-num">2</span> Использование {#использование}

-   Загрузить пакет после `biblatex`:
    ```latex
    \usepackage[options]{biblatex-license}
    ```
-   Опции:
    -   `license`, значения `short` (по умолчанию), `full`, `off` : как следует печатать лицензию;
    -   `url`, значения `false` (по умолчанию), `true` : следует ли явно печатать URL лицензии;
    -   `link`: значения `true` (по умолчанию), `false` : следует ли делать гиперссылку на лицензию;
    -   `introtext`: Дает возможность заменить текст описания на специфичный для языка (например, «лицензировано»).
-   Следует задать в файле библиографии описание лицензии:
    ```bibtex
    @Misc{CreativeCommons4.0,
    author = {{Creative Commons}},
    title = {{Attribution-NonCommercial-ShareAlike 4.0 International}},
    date = {2013-11-25},
    url = {https://creativecommons.org/licenses/by-nc-sa/4.0/},
    urldate = {2019-10-01},
    shorttitle = {{CC BY-NC-SA 4.0}},
    }
    ```
-   И сослаться на эту запись в необходимом месте:
    ```bibtex
    @book{Payne2019,
    author = {Blakeley Hoffman Payne},
    editor = {{MIT Media Lab Personal Robots Group} and Cynthia Breazeal},
    title = {An Ethics of Artificial Intelligence Curriculum for Middle
    School Students},
    related = {CreativeCommons4.0},
    relatedtype = {license},
    url = {https://t1p.de/rwlp},
    urldate = {2020-01-27},
    date = {2019-08},
    }
    ```
