---
title: "Quarto. Плагин pandoc-ext/diagram"
author: ["Dmitry S. Kulyabov"]
date: 2025-10-12T18:40:00+03:00
lastmod: 2025-10-12T18:51:00+03:00
tags: ["markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-plugin-pandoc-diagram"
---

Quarto. Плагин pandoc-ext/diagram.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/pandoc-ext/diagram>


## <span class="section-num">2</span> Типы диаграмм {#типы-диаграмм}

| тип диаграмм                                   | имя блока   | исполняемый файл | переменная окружения |
|------------------------------------------------|-------------|------------------|----------------------|
| [Asymptote](https://asymptote.sourceforge.io/) | `asymptote` | `asy`            | `ASYMPTOTE_BIN`      |
| [GraphViz](https://www.graphviz.org/)          | `dot`       | `dot`            | `DOT_BIN`            |
| [Mermaid](https://mermaid.js.org/)             | `mermaid`   | `mmdc`           | `MERMAID_BIN`        |
| [PlantUML](https://plantuml.com/)              | `plantuml`  | `plantuml`       | `PLANTUML_BIN`       |
| [TikZ](https://github.com/pgf-tikz/pgf)        | `tikz`      | `pdflatex`       | `PDFLATEX_BIN`       |
| [cetz](https://github.com/cetz-package/cetz)   | `cetz`      | `typst`          | `TYPST_BIN`          |
| [D2](https://d2lang.com/)                      | `d2`        | `d2`             | `D2_BIN`             |

-   В столбце _переменная окружения_ даются переменных среды, который можно использовать для указания конкретного исполняемого файла.


## <span class="section-num">3</span> Установка {#установка}

-   Quarto:
    ```shell
    quarto install extension pandoc-ext/diagram
    ```


## <span class="section-num">4</span> Использование {#использование}

-   Quarto, добавить `diagram` к записи `filters` в заголовке yaml:
    ```yaml
    ---
    filters:
    ​  - diagram
    ---
    ```

-   Pandoc:
    ```shell
    pandoc --lua-filter diagram.lua
    ```
