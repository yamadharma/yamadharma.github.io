---
title: "Quarto. Плагин minted-quarto"
author: ["Dmitry S. Kulyabov"]
date: 2025-09-22T15:29:00+03:00
lastmod: 2026-02-07T15:36:00+03:00
tags: ["programming", "markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-plugin-minted-quarto"
---

Quarto. Плагин minted-quarto.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Плагин служит для выделения кода посредством minted (см. [LaTeX. Пакет minted]({{< relref "2024-11-05-latex-minted" >}})).


## <span class="section-num">2</span> nikitoshina/minted-quarto {#nikitoshina-minted-quarto}

-   Репозиторий: <https://github.com/nikitoshina/minted-quarto>
-   Установка:
    ```shell
    quarto install --no-prompt extension nikitoshina/minted-quarto
    ```


## <span class="section-num">3</span> yamadharma/minted-quarto {#yamadharma-minted-quarto}

-   Репозиторий:
    -   <https://github.com/yamadharma/minted-quarto>
    -   <https://gitverse.ru/dharma/minted-quarto>


### <span class="section-num">3.1</span> Установка {#установка}

-   Quarto:
    ```shell
    quarto install --no-prompt extension yamadharma/minted-quarto
    ```


### <span class="section-num">3.2</span> Использование {#использование}

-   Добавить фильтр в заголовок:
    ```yaml
    pdf:
      filters:
    ​    - minted-quarto
    ```
-   Рекомендуется установить его после других фильтров, использующих блоки (например, рисующих диаграммы).
