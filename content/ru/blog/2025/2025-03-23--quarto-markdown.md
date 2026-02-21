---
title: "Quarto. Язык markdown"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-23T20:36:00+03:00
lastmod: 2025-03-29T20:45:00+03:00
tags: ["markdown", "science-writing"]
categories: ["computer-science"]
draft: false
slug: "quarto-markdown"
---

Quarto. Язык markdown.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Quarto основан на Pandoc и использует его вариацию markdown в качестве базового синтаксиса документа.
-   Pandoc markdown --- это расширенная и слегка переработанная версия синтаксиса Markdown Джона Грубера.


## <span class="section-num">2</span> Форматирование текста {#форматирование-текста}

-   Markdown:
    ```markdown
    *курсив*, **полужирный**, ***полужирный курсив***
    ```

    -   _курсив_ , **полужирный** , **_полужирный курсив_**

-   Markdown:
    ```markdown
    верхний индекс^2^ нижний индекс~2~
    ```

    -   верхний индекс<sup>2</sup> / нижний индекс<sub>2</sub>
-   Markdown:
    ```markdown
    ~~зачеркивание~~
    ```

    -   ~~зачеркивание~~
-   Markdown:
    ```markdown
    `verbatim code`
    ```

    -   `verbatim code`


## <span class="section-num">3</span> Заголовки {#заголовки}

-   Markdown:
    ```markdown
    # Заголовок 1

    ## Заголовок 2

    ### Заголовок 3

    #### Заголовок 4

    ##### Заголовок 5

    ###### Заголовок 6
    ```


## <span class="section-num">4</span> Ссылки и изображения {#ссылки-и-изображения}

-   Markdown:
    ```markdown
    <https://quarto.org>

    [Quarto](https://quarto.org)

    ![Caption](elephant.png)

    [![Caption](elephant.png)](https://quarto.org)

    [![Caption](elephant.png "An elephant")](https://quarto.org)

    [![](elephant.png){fig-alt="Alt text"}](https://quarto.org)
    ```


## <span class="section-num">5</span> Списки {#списки}

-   Списки в Quarto требуют целой пустой строки над списком.
-   В противном случае список не будет отображаться в виде списка, а будет отображаться как обычный текст вдоль одной строки.
-   Markdown:
    ```markdown
    ​* unordered list
    ​    + sub-item 1
    ​    + sub-item 2
    ​        - sub-sub-item 1
    ```
-   Вывод:
    -   unordered list
        -   sub-item 1
        -   sub-item 2
            -   sub-sub-item 1

-   Markdown:
    ```markdown
    ​*   item 2

        Continued (indent 4 spaces)
    ```
-   Вывод:
    -   item 2

        Continued (indent 4 spaces)

-   Markdown:
    ```markdown
    1. ordered list
    2. item 2
        i) sub-item 1
             A.  sub-sub-item 1
    ```
-   Вывод:
    1.  ordered list
    2.  item 2
        1.  sub-item 1
            1.  sub-sub-item 1

-   Markdown:
    ```markdown
    ​- [ ] Task 1
    ​- [x] Task 2
    ```
-   Вывод:
    -   [ ] Task 1
    -   [X] Task 2


## <span class="section-num">6</span> Сноски {#сноски}

-   Pandoc поддерживает нумерацию и форматирование сносок:
    ```markdown
    Here is a footnote reference,[^1] and another.[^longnote]

    [^1]: Here is the footnote.

    [^longnote]: Here's one with multiple blocks.

        Subsequent paragraphs are indented to show that they
    belong to the previous footnote.

            { some.code }

        The whole paragraph can be indented, or just the first
        line.  In this way, multi-paragraph footnotes work like
        multi-paragraph list items.

    This paragraph won't be part of the note, because it
    isn't indented.
    ```

-   Можно писать сноски в виде отдельных абзацев:
    ```markdown
    Here is an inline note.^[Inlines notes are easier to write, since you don't have to pick an identifier and move down to type the note.]
    ```

-   Идентификаторы сносок должны быть уникальными в пределах документа.
-   В книгах Quarto главы объединяются в один документ для определённых форматов (включая PDF, DOCX и EPUB), поэтому идентификаторы сносок должны быть уникальными для всех глав.


## <span class="section-num">7</span> Таблицы {#таблицы}

-   Markdown:
    ```markdown
    | Right | Left | Default | Center |
    |------:|:-----|---------|:------:|
    |   12  |  12  |    12   |    12  |
    |  123  |  123 |   123   |   123  |
    |    1  |    1 |     1   |     1  |
    ```

-   Вывод:

    | Right | Left | Default | Center |
    |------:|:-----|---------|:------:|
    | 12    | 12   | 12      | 12     |
    | 123   | 123  | 123     | 123    |
    | 1     | 1    | 1       | 1      |


## <span class="section-num">8</span> Исходный код {#исходный-код}

-   Следует использовать `` ``` `` для разграничения блоков исходного кода:
    ````markdown
    ```
    code
    ```
    ````

-   Можно указать язык для подсветки синтаксиса блоков кода:
    ````markdown
    ```python
    1 + 1
    ```
    ````

-   Если ваш язык не поддерживается, вы можете использовать язык `default`, чтобы получить оформление по умолчанию:
    ````markdown
    ```default
    code
    ```
    ````

-   Эквивалентом краткой формы является длинная форма, которая использует язык как класс (например, `.python` ) внутри фигурных скобок:
    ````markdown
    ```{.python}
    1 + 1
    ```
    ````

-   Длинная форма позволяет добавлять атрибуты к блоку:
    ````markdown
    ```{.python filename="run.py"}
    code
    ```
    ````


## <span class="section-num">9</span> Аннотации кода {#аннотации-кода}

-   Аннотации ячеек кода включают в себя:

    -   Завершение каждой аннотированной строки комментарием и номером аннотации в угловых скобках (например, `# <2>` ). Используйте одно и то же число, чтобы охватить аннотацию на нескольких строках.
    -   Добавление упорядоченного списка сразу после ячейки кода, где каждый элемент соответствует номеру аннотации в коде.

    <!--listend-->

    ````markdown
    ```r
    x <- 1:10  # <1>
    y <- x^2   # <2>
    z <- x^3   # <2>
    ```
    1. Create a vector `x`, and then,
    2. compute `y` and `z`
    ````

-   Возможные позиции аннотаций для вывода HTML:
    -   `below` (по умолчанию): По умолчанию аннотации отображаются под ячейкой кода.
    -   `hover` : Аннотации отображаются при наведении мыши на маркер строки.
    -   `select` : Аннотации появляются при нажатии на маркер и могут быть удалены повторным нажатием.

-   Чтобы изменить положение аннотации по умолчанию, используйте поле метаданных `code-annotations` в заголовке документа:
    ````markdown
    ---
    code-annotations: hover
    ---
    ````


## <span class="section-num">10</span> Необработанный контент {#необработанный-контент}

-   Необработанный контент может быть включён напрямую без разбора Quarto, используя атрибут `raw`:
    ````markdown
    ```{=html}
    <iframe src="https://quarto.org/" width="500" height="400"></iframe>
    ```
    ````

-   Для вывода PDF используйте необработанный блок LaTeX:
    ````markdown
    ```{=latex}
    \renewcommand*{\labelitemi}{\textgreater}
    ```
    ````

-   Можно включить необработанный контент в строку:
    ````markdown
    Here's some raw inline HTML: `<a>html</a>`{=html}
    ````


## <span class="section-num">11</span> Уравнения {#уравнения}

-   Используйте разделители `$` для строчной математики и разделители `$$` выделенной математики.
-   Markdown:
    ````markdown
    inline math: $E = mc^{2}$
    ````
-   Вывод:
    inline math: \\(E = mc^{2}\\)
-   Markdown:
    ````markdown
    display math:

    $$E = mc^{2}$$
    ````
-   Вывод:
    display math:

\\[E = mc^{2}\\]

-   Если вы хотите определить пользовательские макросы TeX, включите их в разделители `$$`, заключенные в блок `.hidden`:
    ````markdown
    ::: {.hidden}
    $$
     \def\RR{{\bf R}}
     \def\bold#1{{\bf #1}}
    $$
    :::
    ````

Для MathJax (применяется по умолчанию) можно использовать команды `\def`, `\newcommand`, `\renewcommand`, `\newenvironment`, `\renewenvironment`, `\let`.


## <span class="section-num">12</span> Диаграммы {#диаграммы}

-   Quarto имеет встроенную поддержку для встраивания диаграммы Mermaid и Graphviz:
    ````markdown
    ```{mermaid}
    flowchart LR
      A[Hard edge] --> B(Round edge)
      B --> C{Decision}
      C --> D[Result one]
      C --> E[Result two]
    ```
    ````
    {{< figure src="/ox-hugo/20250323T203600-mermaid-example.png" >}}


## <span class="section-num">13</span> Разрывы страниц {#разрывы-страниц}

-   Шорткод `pagebreak` позволяет вставлять в документ собственный разрыв страницы (например, в LaTeX это будет `\newpage`, в MS Word --- собственный разрыв страницы docx, в HTML --- директива CSS `page-break-after: always`).
-   Собственные разрывы страниц поддерживаются для HTML, LaTeX, Context, MS Word, Open Document, ePub (для других форматов используется символ перевода страницы).
    ````markdown
    page 1

    {{</* pagebreak */>}}

    page 2
    ````


## <span class="section-num">14</span> Порядок атрибутов {#порядок-атрибутов}

-   `div` и `span` в pandoc могут иметь любую комбинацию идентификаторов, классов и атрибутов ключ-значение.
-   Чтобы pandoc распознал их, они должны быть предоставлены в определённом порядке: идентификаторы, классы, а затем атрибуты ключ-значение.
-   Любой из них может быть опущен, но должен следовать этому порядку, если они предоставлены.
-   Например, следующее является допустимым:
    ````markdown
    [This is good]{#id .class key1="val1" key2="val2"}
    ````
-   Следующее pandoc не распознает:
    ````markdown
    [This does *not* work!]{.class key="val" #id}
    ````


## <span class="section-num">15</span> Сочетания клавиш {#сочетания-клавиш}

-   Шорткод `kbd` можно использовать для описания сочетаний клавиш в документации.
    В форматах Javascript он попытается определить операционную систему формата и отобразит правильное сочетание клавиш.
    В форматах печати он выведет информацию о сочетаниях клавиш для всех операционных систем.
    ````markdown
    To print, press {{</* kbd Shift-Ctrl-P */>}}.
    To open an existing new project, press {{</* kbd mac=Shift-Command-O win=Shift-Control-O linux=Shift-Ctrl-L */>}}.
    ````
