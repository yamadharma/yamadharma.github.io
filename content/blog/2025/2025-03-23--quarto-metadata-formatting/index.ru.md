---
title: "Quarto. Оформление метаданных"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-23T20:24:00+03:00
lastmod: 2025-03-26T20:15:00+03:00
tags: ["markdown", "science-writing"]
categories: ["computer-science"]
draft: false
slug: "quarto-metadata-formatting"
---

Quarto. Оформление метаданных

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Quarto предоставляет богатый набор ключей метаданных YAML для описания деталей научной работы.
-   Пример заголовка YAML:
    ```yaml
    ---
    title: "Toward a Unified Theory of High-Energy Metaphysics: Silly String Theory"
    date: 2008-02-29
    author:
    ​  - name: Josiah Carberry
        id: jc
        orcid: 0000-0002-1825-0097
        email: josiah@psychoceramics.org
        affiliation:
    ​      - name: Brown University
            city: Providence
            state: RI
            url: www.brown.edu
    abstract: >
      The characteristic theme of the works of Stone is
      the bridge between culture and society. ...
    keywords:
    ​  - Metaphysics
    ​  - String Theory
    license: "CC BY"
    copyright:
      holder: Josiah Carberry
      year: 2008
    citation:
      container-title: Journal of Psychoceramics
      volume: 1
      issue: 1
      doi: 10.5555/12345678
    funding: "The author received no specific funding for this work."
    ---
    ```


## <span class="section-num">2</span> Авторы и аффилиации {#авторы-и-аффилиации}

-   Простой способ описания автора:
    ```yaml
    ---
    author: Norah Jones
    ---
    ```

-   Ключ `author` имеет ряд подключей, например ключ `affiliation` для аффилиации:
    ```yaml
    ---
    author:
      name: Norah Jones
      affiliation: Carnegie Mellon University
    ---
    ```
-   Можно описывать несколько авторов:
    ```yaml
    ---
    author:
    ​  - name: Norah Jones
        affiliation:
    ​      - Carnegie Mellon University
    ​      - University of Chicago
    ​  - name: Josiah Carberry
        affiliation: Brown University
    ---
    ```

-   Оба эти ключа можно указать с помощью форм единственного (`author` и `affiliation`) или множественное число (`authors` и `affiliations`).


### <span class="section-num">2.1</span> Автор {#автор}

-   Доступные ключи для `author`:
    -   `email`, `phone`, `fax`, `url` (строка) : контактные данные автора;
    -   `degrees` (строка) : ученые звания или профессиональные сертификаты;
    -   `orcid` (строка) : Открытый идентификатор исследователя (ORCID в форме 0000-0000-0000-0000);
    -   `note` (строка) : примечания для автора, например, сведения о вкладе;
    -   `acknowledgements` (строка) : благодарности автора;
    -   `roles`  (строка) : роли автора;
    -   `corresponding` (true/false) : автор-корреспондент;
    -   `equal-contributor` (true/false) : равные вклыды;
    -   `deceased` (true/false) : усопший:
    -   `id`  (строка) : идентификатор, который будет использоваться для ссылки на этого автора в других полях.
-   Например, более полное описание автора может выглядеть так:
    ```yaml
    ---
    author:
    ​  - name: Josiah Carberry
        orcid: 0000-0002-1825-0097
        url: https://en.wikipedia.org/wiki/Josiah_S._Carberry
        email: josiah@psychoceramics.org
        corresponding: true
    ---
    ```


#### <span class="section-num">2.1.1</span> Компоненты имени {#компоненты-имени}

-   Quarto автоматически анализирует ключ `name` и его компоненты.
-   Если автоматический разбор неверен, вы можете указать компоненты, `given`, `family`, `dropping-particle`, и `non-dropping-particle` напрямую:
    ```yaml
    ---
    author:
    ​  - name:
          given: Charles
          family: Gaulle
          non-dropping-particle: de
    ​  - name:
          given: Ludwig
          family: Beethoven
          dropping-particle: van
    ---
    ```


#### <span class="section-num">2.1.2</span> Степени {#степени}

-   Вы можете указать степени или ученые звания, используя ключ `degrees`:
    ```yaml
    author:
    ​  - name: Josiah Carberry
        degrees:
    ​      - B.S.
    ​      - PhD
    ```


#### <span class="section-num">2.1.3</span> Author Roles {#author-roles}

-   Роль автора может указываться в свободной форме:
    ```yaml
    author:
    ​  - name: Josiah Carberry
        roles: "Conceived and designed the study, analysed the results and wrote the manuscript."
    ```

-   Можно использовать таксономию CRediT (см. [DCM. Авторская этика]({{< relref "2024-08-10-dcm-author-ethics" >}})):
    ```yaml
    author:
    ​  - name: Josiah Carberry
        roles: conceptualization
    ```
-   Можно добавить несколько ролей:
    ```yaml
    author:
    ​  - name: Josiah Carberry
        roles: [investigation, data curation]
    ```

-   Можно указать роль вместе со степенью вклада:
    ```yaml
    author:
    ​  - name: Josiah Carberry
        roles:
    ​      - investigation: lead
    ​      - data curation: supporting
    ```

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  14 ролей участников
</div>

| Наименование                   | Алиас    |
|--------------------------------|----------|
| conceptualization              |          |
| data curation                  |          |
| formal analysis                | analysis |
| funding acquisition            | funding  |
| investigation                  |          |
| methodology                    |          |
| project administration         |          |
| resources                      |          |
| software                       |          |
| supervision                    |          |
| validation                     |          |
| visualization                  |          |
| writing – review &amp; editing | editing  |
| writing – original draft       | writing  |


### <span class="section-num">2.2</span> Аффилиация {#аффилиация}

-   Аффилиацию можно добавить непосредственно к автору:
    ```yaml
    ---
    author:
      name: Norah Jones
      affiliation: Carnegie Mellon University
    ---
    ```

-   Можно указать ключ `name`:
    ```yaml
    ---
    author:
      name: Norah Jones
      affiliation:
        name: Carnegie Mellon University
    ---
    ```
-   Дополнительные поля:
    -   `department` (строка);
    -   `group` (строка) : команда или исследовательская группа;
    -   `address` (строка);
    -   `city` (строка);
    -   `region` или `state` (строка);
    -   `country` (строка);
    -   `postal-code` (строка);
    -   `url` (строка) : сайт организации;
    -   `isni` (число) : 16-значный международный стандартный идентификатор имени (ISNI);
    -   `ringgold` (число) : 4-6-значный идентификатор Ringgold;
    -   `ror` (строка) : Идентификатор реестра исследовательских организаций (ROR), начинающийся с `https://ror.org/`, за которым следует 9-значный буквенно-цифровой идентификатор.

-   Например:
    ```yaml
    ---
    author:
      name: Josiah Carberry
      orcid: 0000-0002-1825-0097
      url: https://en.wikipedia.org/wiki/Josiah_S._Carberry
      email: josiah@psychoceramics.org
      corresponding: true
      affiliation:
    ​    - name: Brown University
          department: Psychoceramics
          city: Providence
          state: RI
          country: US
          url: www.brown.edu
          ringgold: 6752
          isni: 0000000419369094
    ---
    ```


## <span class="section-num">3</span> Аннотация {#аннотация}

-   Можно добавить аннотацию с помощью ключа `abstract`.
-   Поскольку аннотации обычно длиннее одной строки и могут содержать разметку, вам нужно будет предоставить её с использованием блочного стиля YAML.
-   Поместите символ `|` на той же строке, что и `abstract:` и сделайте отступ в два пробела для текста аннотации:
    ```yaml
    ---
    abstract: |
      This article evaluates novel approaches to do
      some really important things.
    ---
    ```


## <span class="section-num">4</span> Ключевые слова {#ключевые-слова}

-   Ключевые слова можно добавлять с помощью ключа `keywords`:
    ```yaml
    ---
    keywords:
    ​  - open-source
    ​  - scientific publishing
    ​  - reproducible research
    ---
    ```


## <span class="section-num">5</span> Авторские права {#авторские-права}

-   Можно указать авторские права несколькими способами.
-   Напрямую в виде строки `copyright`:
    ```yaml
    ---
    copyright: "Copyright Acme, Inc. 2021. All Rights Reserved"
    ---
    ```
-   Используя подключ `statement`:
    ```yaml
    ---
    copyright:
      statement: "Copyright Acme, Inc. 2021. All Rights Reserved"
    ---
    ```
-   Можно указать ключи `holder` и `year`:
    ```yaml
    ---
    copyright:
      holder: Acme, Inc
      year: 2021
    ---
    ```
-   При указании `year` можно использовать диапазон (`year: 2021 - 2023`) или массив (`year: [2021, 2022, 2023]`).


## <span class="section-num">6</span> Лицензия {#лицензия}

-   Чтобы указать лицензию, можно указать строку `license`:
    ```yaml
    ---
    license: "This work is dedicated to the Public Domain"
    ---
    ```
-   Можно указать подключ `text`:
    ```yaml
    ---
    license:
      text: "This work is dedicated to the Public Domain"
    ---
    ```
-   Можно добавить дополнительные сведения, указав подключи `type` и `url`:
    ```yaml
    ---
    license:
      text: >
        Permission is granted to copy, distribute and/or
        modify this document under the terms of the GNU Free
        Documentation License, Version 1.3 or any later version
        published by the Free Software Foundation; with no
        Invariant Sections, no Front-Cover Texts, and no
        Back-Cover Texts. A copy of the license is included in
        the section entitled "GNU Free Documentation License"
      type: open-access
      url: https://www.gnu.org/licenses/fdl-1.3-standalone.html
    ---
    ```

-   Если вы выбираете лицензию Creative Commons (см. [Лицензии Creative Commons]({{< relref "2021-02-22-creative-commons-licenses" >}})), вы можете просто указать аббревиатуру:
    ```yaml
    ---
    license: "CC BY"
    ---
    ```

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 2:</span>
  Аббревиатуры лицензий Creative Commons
</div>

| Аббревиатура  | Тип лицензии                         |
|---------------|--------------------------------------|
| `CC BY`       | Attribution                          |
| `CC BY-SA`    | Attribution-ShareAlike               |
| `CC BY-ND`    | Attribution-NoDerivs                 |
| `CC BY-NC`    | Attribution-NonCommercial            |
| `CC BY-NC-SA` | Attribution-NonCommercial-ShareAlike |
| `CC BY-NC-ND` | Attribution-NonCommercial-NoDerivs   |
| `CC0`         | CC Zero                              |


## <span class="section-num">7</span> Цитирование {#цитирование}

-   Ключ `citation` позволяет указать дополнительные метаданные, которые используются для создания ссылки на документ.


## <span class="section-num">8</span> Финансирование {#финансирование}

-   Ключ `funding` может напрямую задаваться строкой:
    ```yaml
    ---
    funding: "The author(s) received no specific funding for this work."
    ---
    ```

-   Можно задать подключ `statement`:
    ```yaml
    ---
    funding:
      statement: "The author(s) received no specific funding for this work."
    ---
    ```

-   Ключ `funding` также может принимать подключи `source`, `recipient` и `investigator`.
-   `recipient` и `investigator` могут принимать строку или ссылку на автора или аффилиацию, используя `ref`:
    ```yaml
    ---
    author:
    ​  - name: Norah Jones
        id: nj
    funding:
    ​  - source: "NIH (Grant #: 1-R01-MH99999-01A1)"
        investigator:
    ​      - ref: nj
    ---
    ```
