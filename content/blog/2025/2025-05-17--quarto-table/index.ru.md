---
title: "Quarto. Таблицы"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-17T15:42:00+03:00
lastmod: 2025-05-17T19:36:00+03:00
tags: ["science-writing", "markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-table"
---

Quarto. Таблицы.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Таблицы без обрамления {#таблицы-без-обрамления}


### <span class="section-num">1.1</span> Для PDF-документов {#для-pdf-документов}

-   Переопределите LaTeX-правила в YAML-заголовке или перед таблицей:
    ```yaml
    format:
      pdf:
        header-includes: |
          \renewcommand{\toprule}[2]{}
          \renewcommand{\bottomrule}[2]{}
    ```
-   Это удалит верхние и нижние линии.


### <span class="section-num">1.2</span> Для HTML-вывода {#для-html-вывода}

-   Добавьте CSS-стили:
    ```css
    table, th, td {
      border: none !important;
      border-collapse: collapse;
    }
    ```

-   Можно вставить в отдельный блок `css` или в файл стилей.


### <span class="section-num">1.3</span> Описание таблицы {#описание-таблицы}

1.  Используйте параметр класса `borderless` в YAML-заголовке таблицы:
    ```markdown
    ::: {.borderlessттт}
    | Column1 | Column2 |
    |---------|---------|
    | Data    | Data    |
    :::
    ```

2.  Для таблиц из кода добавьте опции:
    ```yaml
    #| tbl-cap-location: top
    #| tbl-class: borderless
    ```
