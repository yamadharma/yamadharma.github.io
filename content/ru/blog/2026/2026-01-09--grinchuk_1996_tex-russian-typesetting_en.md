---
title: "Grinchuk, M. I. (1996) TeX and Russian Traditions of Typesetting"
author: ["Dmitry S. Kulyabov"]
date: 2026-01-09T22:11:00+03:00
lastmod: 2026-01-09T22:45:00+03:00
draft: false
slug: "grinchuk_1996_tex-russian-typesetting_en"
---

Grinchuk, Mikhail Ivanovich (1996) TeX and Russian Traditions of Typesetting  [<a href="#citeproc_bib_item_1">1</a>].

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Notes {#grinchuk_1996_tex-russian-typesetting_en}


### <span class="section-num">1.1</span> Notes for page 2 {#notes-for-page-2}

> 1.  The proclaim of theorems in the E system nowadays are typeset by a slanted font (\sl), whereas in the R system the standard is italic (\it).

-   Не самое важное отличие.
-   В русской традиции вообще слабо применяется наклонный шрифт.


### <span class="section-num">1.2</span> Notes for page 2 {#notes-for-page-2}

> The E system has two kinds of quotation marks: "xxxx" and \`xxxx'. The R system has two kinds too, but these are di erent: &lt;xxxx&gt; and "xxxx".

-   В большинстве языков разные кавычки.
-   Следует использовать пакет csquotes.


### <span class="section-num">1.3</span> Notes for page 2 {#notes-for-page-2}

> The E system distinguishes between short (-) and long (—) dashes; the first one is used for cases (a) and (b). In case (c), the hyphen char (-) is usually used, though it leads to confusion between two surnames and one double surname. In all four cases, the dash is used without spaces at either end, and a possible line break may occur following the dash.
> In contrast with the E system, the R system has only the long dash, surrounded by spaces (half the width of a usual space).

-   В русской традиции действительно используется только длинное тире.
-   Но английский подход кажется более эстетичным.


### <span class="section-num">1.4</span> Notes for page 2 {#notes-for-page-2}

> There is a short list of non-equal mathematical words: tan/tg, cosec/csc, sinh/sh, etc.

-   Кто к чему привык.
-   Тут трудно решить, что лучше.


### <span class="section-num">1.5</span> Notes for page 2 {#notes-for-page-2}

> And now the most essential: the E system permits one to break a formula after a binary operation or binary relation, but the R system also requires repetition of the mark at the beginning of the second line. This is true also for &hellip;

-   А вот это раздражает в английских текстах.
-   Следует использовать пакет rmathbr.


## <span class="section-num">2</span> Резюме {#резюме}


### <span class="section-num">2.1</span> Общая информация {#общая-информация}

-   Статья систематизирует различия между английским и русским стилями вёрстки в TEX, фокусируясь на математических формулах, и предлагает технические решения для реализации русских типографских норм в системе TEX.
-   Ключевой вопрос --- различие между английским (стандартным для TEX) и русским стилями оформления математических формул, в частности правило повторения знаков операций и отношений при переносе формулы на следующую строку.
-   Стандартные стили TEX не поддерживают эту особенность русской типографики, поэтому автор разработал программу для автоматического повторения знаков.


### <span class="section-num">2.2</span> Различия типографики (английская и русская) {#различия-типографики--английская-и-русская}

1.  Оформление теорем: в английском стиле используются наклонный шрифт (sl), в русском --- курсив (it).
2.  Знаки препинания: в русском стиле требуется особое оформление знаков препинания даже в тексте, набранном курсивом.
3.  Межсловные пробелы и переносы: необходимость увеличения межсловного интервала и вставки дискретных переносов.
4.  Кавычки: разные кавычки для русского и английского языков.
5.  Перенос математических формул: в русском стиле при разрыве строки знак операции (например, `+`) должен повторяться на следующей строке --- это не реализовано в стандартном TEX.


### <span class="section-num">2.3</span> Предложенные решения {#предложенные-решения}

-   Модификация файлов стилей для изменения оформления теорем, знаков препинания и пробелов.
-   Использование специальных команд (например, `brokenrel`, `brokenbin`) для управления переносами в математических формулах.
-   Настройка параметров `relpenalty` и `binoppenalty`, чтобы запретить встроенные переносы и обеспечить корректное повторение знаков.
-   Применение шрифтов с не наклонными цифрами и знаками препинания для соблюдения русского стиля.
-   Решения для обработки индексов и специальных конструкций (например, замена `mathord rightarrow` на вариант в фигурных скобках).


### <span class="section-num">2.4</span> Практическая значимость {#практическая-значимость}

-   Статья полезна:
    -   разработчикам и пользователям TEX, работающим с русскоязычными текстами (особенно математического содержания);
    -   тем, кто стремится соблюдать российские типографские стандарты при вёрстке;
    -   авторам, которым требуется адаптировать TEX для специфических требований оформления.


## <span class="section-num">3</span> Библиография {#библиография}

## Литература

<div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>1.	Grinchuk, M.I. TeX and Russian Traditions of Typesetting / M.I. Grinchuk. – [Электронный ресурс] // TUGboat. – 1996. – Т. 17. – № 4. – Сс. 385–388. – Режим доступа: <a href="https://www.tug.org/TUGboat/tb17-4/tb53grin.pdf">https://www.tug.org/TUGboat/tb17-4/tb53grin.pdf</a> (дата обращения: 03.01.2026).</div>
</div>
