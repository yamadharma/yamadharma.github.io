---
title: "Quarto. Структура для книги"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-27T16:33:00+03:00
lastmod: 2025-11-19T21:10:00+03:00
tags: ["science-writing", "markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-book-structure"
---

Quarto. Структура для книги.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Создание книги {#создание-книги}


### <span class="section-num">1.1</span> Общая информация {#общая-информация}

-   Quarto Books — это комбинации нескольких документов (глав) в одну рукопись.
-   Книги могут быть созданы в различных форматах:
    -   HTML
    -   PDF
    -   MS Word
    -   EPUB
    -   AsciiDoc


### <span class="section-num">1.2</span> Создание структуры книги {#создание-структуры-книги}

-   Чтобы создать новый проект книги из терминала, используйте команду `quarto create project`:
    ```shell
    quarto create project book mybook
    ```
-   Это создаст основу для простой книги в каталоге `mybook`.
-   Используйте `quarto preview` команда для рендеринга и предварительного просмотра книги:
    ```shell
    quarto preview mybook
    ```
-   Предварительный просмотр книги откроется в веб-броузере.


### <span class="section-num">1.3</span> Рабочий процесс {#рабочий-процесс}

Выше мы продемонстрировали, как создать и отредактировать простую книгу с главами, содержащимися в файлах. `index.qmd`, `intro.qmd`, `summary.qmd` . Здесь мы более подробно рассмотрим дополнительные аспекты процесса работы с книгами.


### <span class="section-num">1.4</span> Файл конфигурации {#файл-конфигурации}

-   Файл проекта Quarto ( `_quarto.yml` ) содержится в каталоге проекта книги.
-   Этот файл содержит начальную конфигурацию книги:
    ```yaml
    project:
      type: book

    book:
      title: "mybook"
      author: "Jane Doe"
      date: "8/18/2021"
      chapters:
    ​    - index.qmd
    ​    - intro.qmd
    ​    - summary.qmd
    ​    - references.qmd

    bibliography: references.bib

    format:
      html:
        theme: cosmo
      pdf:
        documentclass: scrreprt
      epub:
        cover-image: cover.png
    ```


#### <span class="section-num">1.4.1</span> Компиляция {#компиляция}

-   Используйте команду `render` для рендеринга всех форматов вывода:
    ```shell
    quarto render
    ```
-   Если не передавать аргументы `quarto render`, будут созданы все форматы.
-   Можно отображать отдельные форматы через аргумент `--to`:
    ```shell
    quarto render           # render all formats
    quarto render --to pdf  # render PDF format only
    ```
-   Результат компиляции книги будет записан в подкаталог `_book`:
    ```shell
    mybook/
      _book/
        index.html # and other book files
        mybook.pdf
        mybook.epub
    ```


## <span class="section-num">2</span> Структура книги {#структура-книги}


### <span class="section-num">2.1</span> Общая информация {#общая-информация}

-   Главы и разделы книги Quarto автоматически нумеруются (для перекрестных ссылок).
-   Можно указать, что некоторые части книги должны оставаться ненумерованными.
-   Свойства книги, такие как название, автор и структура главы, перечислены под `book`:
    ```yaml
    book:
      title: "mybook"
      author: "Jane Doe"
      date: "5/9/2021"
      chapters:
    ​    - index.qmd
    ​    - intro.qmd
    ​    - summary.qmd
    ​    - references.qmd
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      _quarto.yml
    </div>

    -   Файл `index.qmd` обязателен (потому что Quarto books также создают веб-сайт в формате HTML).
        -   Эта страница должна включать предисловие, благодарности и т. д. HTML-версия книги будет использовать `index.qmd` как домашняя страница и, если предусмотрено, разместит `cover-image` на этой странице.
    -   Остаток `chapters` включает в себя одну или несколько глав книги.
    -   Файл `references.qmd` будет включать сгенерированную библиографию.

-   Параметры рендеринга, которые должны применяться ко всем главам и всем форматам, перечислены на верхнем уровне `_quarto.yml` (т.е. не вложенном в `book`):
    ```yaml
    bibliography: references.bib
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 2:</span>
      _quarto.yml
    </div>
-   Параметры рендеринга, которые должны применяться ко всем главам для определённых форматов, перечислены в секции `format`:
    ```yaml
    format:
      html:
        theme: cosmo
      pdf:
        documentclass: scrreprt
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 3:</span>
      _quarto.yml
    </div>


### <span class="section-num">2.2</span> Названия {#названия}

-   Название задаётся в `title`:
    ```yaml
    ---
    title: "Introduction"
    ---
    ```


### <span class="section-num">2.3</span> Номера глав {#номера-глав}

-   Все главы пронумерованы по умолчанию.
-   Если вы хотите, чтобы глава была ненумерованной, просто добавьте класс `.unnumbered` к его основному заголовку:
    ```markdown
    # Preface {.unnumbered}
    ```
-   Можно смешивать пронумерованные и ненумерованные главы.
-   Хотя вы можете ссылаться на ненумерованные главы, вы не можете ссылаться на рисунки, таблицы и т. д. внутри них.


### <span class="section-num">2.4</span> Номера разделов {#номера-разделов}

-   Вы можете задать глубину нумерации через `number-depth`.
-   Например, чтобы пронумеровать только разделы, расположенные непосредственно под уровнем главы:
    ```yaml
    number-depth: 1
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 4:</span>
      _quarto.yml
    </div>

-   Если необходимо, чтобы `number-depth` применялась только к определённому формату, вложите его в `format` :
    ```yaml
    format:
      pdf:
        number-depth: 1
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 5:</span>
      _quarto.yml
    </div>

-   Опция `toc-depth` не зависит от `number-depth`.


### <span class="section-num">2.5</span> Библиография {#библиография}

-   Следует включить `div` с идентификатором `#refs` в том месте книге, где должна быть создана библиография:
    ```markdown
    # References {.unnumbered}

    ::: {#refs}
    :::
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 6:</span>
      _quarto.yml
    </div>


### <span class="section-num">2.6</span> Создание индекса {#создание-индекса}

-   Для вывода PDF вы можете создать индекс, используя пакет LaTeX `makeidx` вместе с командой `\index`.
-   Команда `\index` для выходных данных в формате, отличном от pdf, игнорируются.
-   Чтобы добавить индекс в PDF-файл книги, добавьте эти записи `include-in-header` и `include-after-body` в конфигурацию формата `pdf` в `_quarto.yml`:
    ```yaml
    format:
      html:
        theme: cosmo
      pdf:
        documentclass: scrreprt
        include-in-header:
          text: |
            \usepackage{makeidx}
            \makeindex
        include-after-body:
          text: |
            \printindex
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 7:</span>
      _quarto.yml
    </div>
-   Затем добавьте команды `\index{entry}` везде, где вам нужна запись индекса:
    ```markdown
    Markdown\index{Markdown} allows you to write using an easy-to-read, easy-to-write plain text format.
    ```
-   Также можете использовать пакет `imakeidx`:
    ```yaml
    format:
      html:
        theme: cosmo
      pdf:
        documentclass: scrreprt
        include-in-header:
          text: |
            \usepackage{imakeidx}
            \makeindex[intoc=true, columns=3, columnseprule=true, options=-s latex/indexstyles.ist]
        include-after-body:
          text: |
            \printindex
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 8:</span>
      _quarto.yml
    </div>
-   Этот пакет предлагает дополнительные возможности для форматирования индекса.
-   В приведенном выше примере:
    -   `intoc=true` включит запись для индекса в оглавление;
    -   `columns=3` отформатирует индекс в три столбца;
    -   `columnseprule=true` отобразит линию между столбцами индекса;
    -   `options=-s latex/indexstyles.ist` будут использоваться дополнительные параметры форматирования из файла индексного стиля, расположенного по адресу `latex/indexstyles.ist`.


### <span class="section-num">2.7</span> Части {#части}

-   Форматы EPUB и Word (Docx) в настоящее время не поддерживают организацию книг в части.
-   При рендеринге книги с частями в эти форматы части будут проигнорированы.
-   Вы можете разделить свою книгу на части, используя `part` в иерархии `chapters`:
    ```yaml
    book:
      chapters:
    ​    - index.qmd
    ​    - preface.qmd
    ​    - part: dice.qmd
          chapters:
    ​        - basics.qmd
    ​        - packages.qmd
    ​    - part: cards.qmd
          chapters:
    ​        - objects.qmd
    ​        - notation.qmd
    ​        - modifying.qmd
    ​        - environments.qmd
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 9:</span>
      _quarto.yml
    </div>
-   Тут файлы разметки `dice.qmd` и `cards.qmd` содержат заголовок части (как заголовок первого уровня), а также некоторое вводное содержание для части.
-   Если нужен только заголовок части, то вы можете использовать этот синтаксис:
    ```yaml
    book:
      chapters:
    ​    - index.qmd
    ​    - preface.qmd
    ​    - part: "Dice"
          chapters:
    ​        - basics.qmd
    ​        - packages.qmd
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 10:</span>
      _quarto.yml
    </div>
-   В выводе LaTeX для частей используется команда `\part`.


### <span class="section-num">2.8</span> Приложения {#приложения}

-   Можно включить приложения, добавив ключ `appendices`:
    ```yaml
    book:
      chapters:
    ​    - index.qmd
    ​    - intro.qmd
    ​    - summary.qmd
    ​    - references.qmd
      appendices:
    ​    - tools.qmd
    ​    - resources.qmd
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 11:</span>
      _quarto.yml
    </div>
-   Приложения нумеруются с использованием заглавных букв и имеют префикс, вставленный в их заголовок, чтобы указать, что они являются приложением (например, «Приложение A — Дополнительные ресурсы»).
-   Можно настроить префикс и разделитель:
    ```yaml
    crossref:
      appendix-title: "App."
      appendix-delim: ":"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 12:</span>
      _quarto.yml
    </div>


### <span class="section-num">2.9</span> Навигация по странице {#навигация-по-странице}

-   Если у вас есть книга с несколькими страницами в разделе или подразделе, часто бывает удобно предложить пользователю возможность перейти на следующую страницу (или предыдущую страницу) в нижней части страницы, которую он только что закончил читать.
-   Это можно включить это с помощью:
    ```yaml
    book:
      page-navigation: true
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 13:</span>
      _quarto.yml
    </div>
-   При включении навигация по страницам будет отображаться внизу страницы, когда есть следующая или предыдущая страница (включая следующий или предыдущий раздел).
-   Эта опция включена по умолчанию для книг, но не для веб-сайтов.


### <span class="section-num">2.10</span> Нижний колонтитул страницы {#нижний-колонтитул-страницы}

-   Используйте `page-footer` чтобы предоставить общий нижний колонтитул для всех страниц книги.
-   Самый простой нижний колонтитул просто предоставляет текст, который будет отцентрирован и отображен более светлым шрифтом:
    ```yaml
    book:
      page-footer: "Copyright 2021, Norah Jones"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 14:</span>
      _quarto.yml
    </div>
-   Можно выделить области нижнего колонтитула по отдельности (`left`, `right`, и `center`):
    ```yaml
    book:
      page-footer:
        left: "Copyright 2021, Norah Jones"
        right:
    ​      - icon: github
            href: https://github.com/
    ​      - icon: twitter
            href: https://twitter.com/
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 15:</span>
      _quarto.yml
    </div>

-   Можно использовать параметры `background`, `foreground`, `border` для дальнейшего управления внешним видом нижнего колонтитула.
-   По умолчанию нижний колонтитул не имеет фонового цвета и верхней границы.
-   Чтобы убрать границу, сделайте следующее:
    ```yaml
    book:
      page-footer:
        border: false
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 16:</span>
      _quarto.yml
    </div>
-   Использовать светлый фон (например, чтобы он соответствовал панели навигации):
    ```yaml
    book:
      page-footer:
        background: light
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 17:</span>
      _quarto.yml
    </div>
