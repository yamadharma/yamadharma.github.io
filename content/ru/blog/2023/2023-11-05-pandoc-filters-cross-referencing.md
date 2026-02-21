---
title: "Pandoc. Фильтры. Перекрёстные ссылки"
author: ["Dmitry S. Kulyabov"]
date: 2023-11-05T19:04:00+03:00
lastmod: 2024-02-17T20:19:00+03:00
tags: ["pandoc", "markdown"]
categories: ["computer-science"]
draft: false
slug: "pandoc-filters-cross-referencing"
---

Pandoc. Фильтры. Перекрёстные ссылки.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> pandoc-crossref {#pandoc-crossref}

-   Репозиторий: <https://github.com/lierdakil/pandoc-crossref>
-   Документация: <https://lierdakil.github.io/pandoc-crossref/>
-   Язык реализации: Haskell


## <span class="section-num">2</span> pandoc-xnos {#pandoc-xnos}

-   Репозиторий: <https://github.com/tomduck/pandoc-xnos>
-   Исправления (сторонние): <https://github.com/nandokawka/pandoc-xnos>
-   Обновлялся в 2020 году.
-   Проблемы с pandoc-3.
-   Состоит из нескольких фильтров:
    -   `pandoc-fignos` : нумерация рисунков и ссылки на рисунки;
    -   `pandoc-eqnos` : нумерация уравнении и ссылки на уравнения;
    -   `pandoc-tablenos` : нумерация таблиц и ссылки на таблицы;
    -   `pandoc-secnos` : нумерация ссылок на разделы (разделы нумеруются самим pandoc).


### <span class="section-num">2.1</span> pandoc-fignos {#pandoc-fignos}

-   Репозиторий: <https://github.com/tomduck/pandoc-fignos>


### <span class="section-num">2.2</span> pandoc-eqnos {#pandoc-eqnos}

-   Репозиторий: <https://github.com/tomduck/pandoc-eqnos>


### <span class="section-num">2.3</span> pandoc-tablenos {#pandoc-tablenos}

-   Репозиторий: <https://github.com/tomduck/pandoc-tablenos>


### <span class="section-num">2.4</span> pandoc-secnos {#pandoc-secnos}

-   Репозиторий: <https://github.com/tomduck/pandoc-secnos>
