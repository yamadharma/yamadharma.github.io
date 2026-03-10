---
title: "bibtex vs biblatex"
author: ["Dmitry S. Kulyabov"]
date: 2022-09-11T20:22:00+03:00
lastmod: 2023-07-11T17:55:00+03:00
tags: ["tex"]
categories: ["computer-science"]
draft: false
slug: "bibtex-biblatex"
---

Сравнение формата баз данных _BibTeX_ и _biblatex_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Типы записей {#типы-записей}

-   [BibTeX. Типы записей]({{< relref "2023-07-11-bibtex-entry-type" >}})
-   Набор типов записей, определенный с помощью _biblatex_ отличается от набора, используемого _BibTeX_.
-   В основном _biblatex_ добавляются новые типы записей, но есть несколько типов записей BibTeX, которые были удалены.
-   _biblatex_ по-прежнему распознает эти типы записей, но рассматривает их как псевдонимы для собственных типов.

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Соответствие типов записей BibTeX и biblatex
</div>

| BibTeX           | Biblatex                             |
|------------------|--------------------------------------|
| `@Conference`    | `@InProceedings`                     |
| `@Electronic`    | `@Online`                            |
| `@MastersThesis` | `@Thesis`, `type={Master's thesis}`  |
| `@PhDThesis`     | `@Thesis`, `type={PhD thesis}`       |
| `@TechReport`    | `@Report`, `type={technical report}` |
| `@www`           | `@Online`                            |


## <span class="section-num">2</span> Типы полей {#типы-полей}

-   Ряд полей устарел, но все еще принимается в качестве псевдонимов в _biblatex_:

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 2:</span>
  Соответствие типов полей BibTeX и biblatex
</div>

| BibTeX          | Biblatex       |
|-----------------|----------------|
| `address`       | `location`     |
| `annote`        | `annotation`   |
| `archiveprefix` | `eprinttype`   |
| `journal`       | `journaltitle` |
| `key`           | `sortkey`      |
| `pdf`           | `file`         |
| `primaryclass`  | `eprintclass`  |
| `school`        | `institution`  |


## <span class="section-num">3</span> Новые поля {#новые-поля}


### <span class="section-num">3.1</span> Поле `date` {#поле-date}

-   Вместо поля `year` рекомендуется использовать поле `date`.
-   Дата в поле `date` задаётся в формате `YYYY-MM-DD`.
