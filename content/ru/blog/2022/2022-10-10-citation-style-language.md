---
title: "Citation Style Language (CSL)"
author: ["Dmitry S. Kulyabov"]
date: 2022-10-10T10:22:00+03:00
lastmod: 2023-10-17T13:23:00+03:00
tags: ["bib"]
categories: ["computer-science"]
draft: false
slug: "citation-style-language"
---

Язык стилей цитирования.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Язык стилей цитирования представляет собой открытый язык на основе XML для описания форматирования цитат и библиографий.
-   Сайт: <https://citationstyles.org/>
-   Репозиторий стилей: <https://github.com/citation-style-language/styles>.
-   Поиск по стилям:
    -   <https://www.zotero.org/styles>;
    -   <https://csl.mendeley.com/>.
-   Спецификация: <https://docs.citationstyles.org/en/stable/specification.html>.
-   Введение: <https://docs.citationstyles.org/en/stable/primer.html>


### <span class="section-num">1.1</span> История {#история}

-   CSL был создан Брюсом Д'Аркусом для использования с OpenOffice.org.
-   CSL был доработан в сотрудничестве с разработчиком Zotero Саймоном Корнблитом.
-   С 2008 года основная команда разработчиков состоит из Д'Аркуса, Фрэнка Беннета и Ринтце Зелле.
-   Версии CSL:
    -   0.8 (21 марта 2009 г.);
    -   0.8.1 (1 февраля 2010 г.);
    -   1.0 (22 марта 2010 г.), обратно несовместимый с предыдущими версиями;
    -   1.0.1 (3 сентября 2012 г.);
    -   1.0.2.


## <span class="section-num">2</span> Поддерживающие программы {#поддерживающие-программы}

-   Zotero: <https://www.zotero.org/>.
-   Mendeley: <http://mendeley.com/>.
-   Pandoc (см. [Pandoc]({{< relref "2021-08-28-pandoc" >}})) поддерживает цитаты в форматах CSL, YAML и JSON и может отображать их с использованием стилей CSL.


## <span class="section-num">3</span> Использование CSL в LaTeX {#использование-csl-в-latex}


### <span class="section-num">3.1</span> citeproc-lua {#citeproc-lua}

-   Реализация процессора CSL v1.0.2 на Lua.
-   Репозиторий: <https://github.com/zepinglee/citeproc-lua>
-   CTAN: <https://ctan.org/pkg/citation-style-language>


## <span class="section-num">4</span> Редактирование файлов CSL {#редактирование-файлов-csl}

-   Для редактирования можно использовать онлайн-редактора CSL Editor.
-   Адрес: <https://editor.citationstyles.org/visualEditor/>


## <span class="section-num">5</span> Соответствие полей CSL и библиографических систем {#соответствие-полей-csl-и-библиографических-систем}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Соответствие полей CSL и Mendeley
</div>

| CSL                | Mendeley               |
|--------------------|------------------------|
| article            | Generic                |
| bill               | Bill                   |
| book               | Book                   |
| chapter            | Book Section           |
| article            | Case                   |
| article            | Computer Program       |
| paper-conference   | Conference Proceedings |
| entry-encyclopedia | Encyclopedia Article   |
| motion_picture     | Film                   |
| speech             | Hearing                |
| article-journal    | Journal Article        |
| article-magazine   | Magazine Article       |
| article-newspaper  | Newspaper Article      |
| patent             | Patent                 |
| report             | Report                 |
| legislation        | Statute                |
| thesis             | Thesis                 |
| broadcast          | Television Broadcast   |
| webpage            | Web Page               |
| article            | Working Paper          |


## <span class="section-num">6</span> Стили CSL {#стили-csl}


### <span class="section-num">6.1</span> Стили CSL для библиографии ГОСТ {#стили-csl-для-библиографии-гост}

-   [Библиография. CSL. ГОСТ]({{< relref "2022-12-15-csl-gost" >}})
