---
title: "Литературное программирование"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-05T19:47:00+03:00
lastmod: 2025-05-12T14:19:00+03:00
tags: ["article", "programming"]
categories: ["computer-science"]
draft: false
slug: "literate-programming"
---

Литературное программирование.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Автором метода является Дональд Кнут [<a href="#citeproc_bib_item_1">1</a>].
-   Распространённое название: _Грамотное программирование_.
-   Литературное программирование --- метод разработки, нацеленный на повышение познаваемости программ и основанный на встраивании исходного кода в документацию.
-   Познаваемость программы --- свойство исходного кода и сопроводительной документации, которое характеризует объём умственных усилий, затрачиваемых читателем на понимание программы в целом и её частей в частности.
-   Объектом воздействия в литературном программировании является мозг человека, а не компьютер.


### <span class="section-num">1.1</span> Идеология метода {#идеология-метода}

-   Программа оформляется как книга.
-   Исходный код разбивается на кусочки и рассредотачивается по документации.
-   Кусочки кода связываются посредством гиперссылок.
-   Первична документация.
-   За основу берётся описание программы, в которое вставляются кусочки исходного кода.
-   Для встраивания кода в документацию применяется специальная разметка текста.


## <span class="section-num">2</span> Принципы реализации методики литературного программирования {#принципы-реализации-методики-литературного-программирования}

-   Программа составляется из кусочков (фрагментов).
-   Каждый фрагмент содержит блок кода и описывающую его документацию.
-   Фрагменты связываются гиперссылками.
-   Все фрагменты хранятся вместе, в одном физическом источнике.


### <span class="section-num">2.1</span> Служебные программы {#служебные-программы}

-   Программа `weave` обрабатывает источник и формирует документ, предназначенный человеку.
    -   В этом документе программа представлена в виде книги для чтения, в которой код перемежается с описанием.
-   Программа `tangle` извлекает из того же самого источника исходные коды и формирует из них файлы, предназначенные компилятору.
    -   В этих файлах программа представлена в том виде, как того требует целевой язык программирования.


## <span class="section-num">3</span> Реализации для разных языков программирования {#реализации-для-разных-языков-программирования}

-   [Julia. Литературное программирование]({{< relref "2025-05-12--julia-literate-programming" >}})


## <span class="section-num">4</span> Утилиты для литературного программирования {#утилиты-для-литературного-программирования}


### <span class="section-num">4.1</span> Entangled {#entangled}

-   Сайт: <https://entangled.github.io/>
-   Репозиторий: <https://github.com/entangled/entangled.py/>


## <span class="section-num">5</span> Статьи {#статьи}

-   [Knuth, D. E. (1984): Literate Programming]({{< relref "2023-08-06-knuth_1984_literate-programming_en" >}}) [<a href="#citeproc_bib_item_1">1</a>]
-   [Schulte, E. et al. (2012): A multi-language computing environment for literate programming and reproducible research]({{< relref "2023-08-06-schulte_2012_multi-language-literat-programming_en" >}}) [<a href="#citeproc_bib_item_2">2</a>]
-   [Kery, M. B. et al. (2018): The story in the notebook]({{< relref "2023-08-07-kery_2018_story-notebook_en" >}}) [<a href="#citeproc_bib_item_3">3</a>]


## <span class="section-num">6</span> Библиография {#библиография}

## Литература

<div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>1.	Knuth, D.E. Literate Programming / D.E. Knuth // The Computer Journal. – 1984. – Т. 27. – № 2. – Сс. 97–111. DOI: <a href="https://doi.org/10.1093/comjnl/27.2.97">10.1093/comjnl/27.2.97</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>2.	Schulte, E. A Multi-Language Computing Environment for Literate Programming and Reproducible Research / E. Schulte, D. Davison, T. Dye, C. Dominik // Journal of Statistical Software. – 2012. – Т. 46. – № 3. DOI: <a href="https://doi.org/10.18637/jss.v046.i03">10.18637/jss.v046.i03</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>3.	Kery, M.B. <a href="https://doi.org/10.1145/3173574.3173748">The Story in the Notebook</a> / M.B. Kery, M. Radensky, M. Arya и др. // Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems. – ACM, 2018. – Сс. 1–11.</div>
</div>
