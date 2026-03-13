---
title: "Quarto. Библиография"
author: ["Dmitry S. Kulyabov"]
date: 2026-02-01T16:42:00+03:00
lastmod: 2026-02-01T17:22:00+03:00
tags: ["markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-bibliography"
---

Quarto. Библиография.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Quarto позволяет автоматически создавать цитаты и библиографию, используя библиографический файл (например, BibTeX) и стандартный синтаксис Pandoc для цитирования.


## <span class="section-num">2</span> Добавление библиографии {#добавление-библиографии}


### <span class="section-num">2.1</span> Подготовьте файл библиографии {#подготовьте-файл-библиографии}

-   Создайте файл (например, `references.bib`) в формате BibTeX (см. [BibTeX]({{< relref "2021-09-28-bibtex" >}})).


### <span class="section-num">2.2</span> Подключите файл в документе Quarto {#подключите-файл-в-документе-quarto}

-   В YAML-заголовке документа (вверху файла `.qmd`) укажите путь к файлу:
    ```markdown
    ---
    title: "Мой документ"
    author: "Автор"
    bibliography: references.bib
    ---
    ```


### <span class="section-num">2.3</span> Изменение стиля цитирования {#изменение-стиля-цитирования}

-   Чтобы изменить формат (например, на APA или ГОСТ), используйте файл `*.csl`.
-   Укажите его в YAML:
    ```markdown
    csl: american-political-science-association.csl
    ```

-   Базу готовых стилей можно найти в [репозитории Citation Style Language](https://github.com/citation-style-language/styles).


### <span class="section-num">2.4</span> Цитируйте источники в тексте {#цитируйте-источники-в-тексте}

-   Используйте синтаксис `[@ключ_из_bib]` в любом месте текста для вставки цитаты.
-   Пример:
    -   `Blah Blah [@knuth1984]`  → Blah Blah (Knuth 1984)
    -   `@wickham2015 говорит...`  → Wickham (2015) говорит...
    -   `[-@ggplot2]`  → (2016) — так можно сослаться без имени автора.

-   По умолчанию библиография будет автоматически создана и размещена в конце документа.


## <span class="section-num">3</span> Дополнительные настройки {#дополнительные-настройки}


### <span class="section-num">3.1</span> Размещение библиографии в нужном месте {#размещение-библиографии-в-нужном-месте}

-   Если требуется, чтобы список литературы появился не в самом конце, а перед приложением, добавьте в нужном месте разметки блок:
    ```markdown
    ::: {#refs}
    :::
    ```


### <span class="section-num">3.2</span> Включение нецитированных источников {#включение-нецитированных-источников}

-   Чтобы добавить в список литературы работу, на которую нет прямой ссылки в тексте, используйте в YAML поле `nocite`:
    ```markdown
    nocite: |
      @неупомянутая_статья_2010, @другая_книга
      @*
    ```

-   Знак `@*` добавит **все** источники из `.bib`-файла.


## <span class="section-num">4</span> Плагины {#плагины}


### <span class="section-num">4.1</span> pandoc-ext/multibib {#pandoc-ext-multibib}

-   Репозиторий: <https://github.com/pandoc-ext/multibib>
-   Позволяет добавлять несколько библиографий.


### <span class="section-num">4.2</span> pandoc-ext/section-bibliographies {#pandoc-ext-section-bibliographies}

-   Репозиторий: <https://github.com/pandoc-ext/section-bibliographies>
-   Позволяет размещать библиографию для каждого элемента верхнего уровня (раздел, глава).
