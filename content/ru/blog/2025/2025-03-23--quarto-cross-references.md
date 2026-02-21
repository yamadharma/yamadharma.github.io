---
title: "Quarto. Перекрёстные ссылки"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-23T20:33:00+03:00
lastmod: 2025-03-27T16:31:00+03:00
tags: ["science-writing", "markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-cross-references"
---

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Перекрёстные ссылки облегчают навигацию по документу, предоставляя пронумерованные ссылки и гиперссылки на различные сущности, такие как рисунки и таблицы.
-   Каждая сущность, на которую можно ссылаться перекрестно, требует метки --- уникального идентификатора с префиксом типа перекрёстной ссылки, например `#fig-element`.
-   Например, это перекрестно-ссылочный рисунок:
    ```markdown
    ![Elephant](elephant.png){#fig-elephant}
    ```
-   Наличие метки (`#fig-elephant`) делает этот рисунок ссылочным.
-   Это позволяет ссылаться на него в другом месте документа:
    ```markdown
    See @fig-elephant for an illustration.
    ```

-   Идентификаторы перекрёстных ссылок должны начинаться с их типа (например, `fig-` или `tbl-`).
-   Так, идентификатор `#fig-elephant` действителен для перекрёстной ссылки, но идентификаторы `#elephant` и `#elephant-fig` такими не являются.


## <span class="section-num">2</span> Зарезервированные префиксы {#зарезервированные-префиксы}

-   Метка устанавливается с помощью символа `#` в атрибуте (например, `#fig-elephant`).
-   Зарезервированные префиксы: `fig`, `tbl`, `lst`, `tip`, `nte`, `wrn`, `imp`, `cau`, `thm`, `lem`, `cor`, `prp`, `cnj`, `def`, `exm`, `exr`, `sol`, `rem`, `eq`, `sec`.
-   Префикс отделяется от содержания метки дефисом (`-`).
-   Избегайте использования подчёркиваний (`_`) в метках и идентификаторах, так как это может вызвать проблемы при преобразовании в PDF с помощью LaTeX.


## <span class="section-num">3</span> Ссылки {#ссылки}

-   Синтаксис по умолчанию для встроенных ссылок (например, `@fig-elephant` ) приводит к тексту ссылки «Рисунок 1», «Таблица 1» и т. д.
-   Вы можете настроить внешний вид встроенных ссылок, либо изменив синтаксис встроенной ссылки, либо установив параметры.

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Различные способы составления перекрестной ссылки и их результирующий вывод
</div>

| Тип                      | Синтаксис             | Выход     |
|--------------------------|-----------------------|-----------|
| По умолчанию             | `@fig-elephant`       | Рисунок 1 |
| Заглавные буквы          | `@Fig-elephant`       | Рисунок 1 |
| Пользовательский префикс | `[Fig @fig-elephant]` | Рис 1     |
| Без префикса             | `[-@fig-elephant]`    | 1         |

-   Синтаксис с заглавными буквами не имеет значения для выходных данных по умолчанию, но сделал бы первую букву заглавной, если бы префикс по умолчанию был изменен с помощью опции использования нижнего регистра (например, `fig.`).
-   Эти варианты синтаксиса работают не только для рисунков, но и для всех перекрестно-ссылочных элементов в Quarto, таких как таблицы, уравнения, теоремы и т. д.
-   Можете группировать перекрёстные ссылки, используя следующий синтаксис:
    ```markdown
    As illustrated in [@fig-elephant; @fig-panther; @fig-rabbit].
    ```


## <span class="section-num">4</span> Списки {#списки}

-   Для вывода LaTeX / PDF вы можно использовать необработанные команды LaTeX `\listoffigures`, `\listoftables` и `\listoflistings` для создания списков всех рисунков, таблиц и т. д. в документе.
-   Вы можете использовать параметры `lof-title`, `lot-title`, `lol-title` для настройки заголовка листинга:
    ```yaml
    ---
    title: "My Document"
    crossref:
      lof-title: "List of Figures"
    format: pdf
    ---

    \listoffigures
    ```


## <span class="section-num">5</span> Изображения {#изображения}

-   Создания ссылки на изображение:
    ```markdown
    ![Elephant](elephant.png){#fig-elephant}

    See @fig-elephant for an illustration.
    ```

-   Идентификаторы перекрестных ссылок должны начинаться с их типа (например, `#fig-` ) и что идентификаторы перекрестных ссылок должны быть написаны строчными буквами.
-   Чтобы создать перекрестную ссылку на рисунок с использованием синтаксиса `div`, создайте `div` с идентификатором, начинающимся с `fig-`, включите изображение и подпись внутри `div`:
    ```markdown
    ::: {#fig-elephant}

    ![](elephant.png)

    An Elephant
    :::
    ```


### <span class="section-num">5.1</span> Подфигуры {#подфигуры}

-   Можно создать рисунок, состоящий из нескольких подрисунков.
-   Для этого заключите рисунки в `div` (с собственной меткой и подписью) и дайте каждому подрисунку собственную метку и (необязательно) подпись.
-   Затем можно ссылаться либо на весь рисунок в ссылке, либо на отдельный подрисунок:
    ```markdown
    ::: {#fig-elephants layout-ncol=2}

    ![Surus](surus.png){#fig-surus}

    ![Hanno](hanno.png){#fig-hanno}

    Famous Elephants
    :::

    See @fig-elephants for examples. In particular, @fig-hanno.
    ```
-   Тут использован атрибут `layout-ncol` для указания на двуколоночную вёрстку для расположения рисунков.


### <span class="section-num">5.2</span> Вычисления {#вычисления}

-   Можно сделать ссылку на изображение, полученное в результате вычисления.
-   Для этого добавьте опции `label` и `fig-cap` в верхней части блока кода:
    ````markdown
    ```{python}
    #| label: fig-plot
    #| fig-cap: "Plot"

    import matplotlib.pyplot as plt
    plt.plot([1,23,2,4])
    plt.show()
    ```

    For example, see @fig-plot.
    ````

-   Можно создать несколько фигур в ячейке кода и ссылаться на них как на подфигуры.
-   Для этого используйте `fig-cap` для основного заголовка и `fig-subcap` для подзаголовков:
    ````markdown
    ```{python}
    #| label: fig-plots
    #| fig-cap: "Plots"
    #| fig-subcap:
    #|   - "Plot 1"
    #|   - "Plot 2"
    #| layout-ncol: 2

    import matplotlib.pyplot as plt
    plt.plot([1,23,2,4])
    plt.show()

    plt.plot([8,65,23,90])
    plt.show()
    ```

    See @fig-plots for examples. In particular, @fig-plots-2.
    ````
-   Справочные метки подрисунков создаются автоматически на основе метки основного фрагмента (например, `@fig-plots-1`, `@fig-plots-2` и т. д.).
-   Если вы хотите, чтобы подписи к подрисункам включали только идентификатор, например `(a)`, а не текстовую подпись, укажите `fig-subcap: true` вместо предоставления явного текста подписи:
    ````markdown
    ```{python}
    #| label: fig-plots
    #| fig-cap: "Plots"
    #| fig-subcap: true
    #| layout-ncol: 2
    ```
    ````


## <span class="section-num">6</span> Таблицы {#таблицы}

-   Для таблиц с разметкой добавьте подпись под таблицей, а затем включите метку `#tbl-` в фигурных скобках в конце подписи:
    ````markdown
    | Col1 | Col2 | Col3 |
    |------|------|------|
    | A    | B    | C    |
    | E    | F    | G    |
    | A    | G    | G    |

    : My Caption {#tbl-letters}

    See @tbl-letters.
    ````


### <span class="section-num">6.1</span> Префикс метки {#префикс-метки}

-   Для того чтобы таблица была перекрестно-ссылочной, ее метка должна начинаться с префикса `tbl-`.
-   Чтобы создать перекрёстную ссылку на таблицу с использованием синтаксиса `div`, создайте `div` с идентификатором, начинающимся с `tbl-`, включите таблицу и подпись внутри `div`:
    ````markdown
    ::: {#tbl-letters}

    | Col1 | Col2 | Col3 |
    |------|------|------|
    | A    | B    | C    |
    | E    | F    | G    |
    | A    | G    | G    |

    My Caption

    :::
    ````


### <span class="section-num">6.2</span> Подтаблицы {#подтаблицы}

-   Можно расположить несколько подтаблиц.
-   Для этого создайте `div` с основным идентификатором, затем примените подидентификаторы (и необязательный текст заголовка) к содержащимся таблицам:
    ````markdown
    ::: {#tbl-panel layout-ncol=2}
    | Col1 | Col2 | Col3 |
    |------|------|------|
    | A    | B    | C    |
    | E    | F    | G    |
    | A    | G    | G    |

    : First Table {#tbl-first}

    | Col1 | Col2 | Col3 |
    |------|------|------|
    | A    | B    | C    |
    | E    | F    | G    |
    | A    | G    | G    |

    : Second Table {#tbl-second}

    Main Caption
    :::

    See @tbl-panel for details, especially @tbl-second.
    ````

-   Основная подпись для таблицы указана в качестве последнего блока внутри содержащего её `div`.


### <span class="section-num">6.3</span> Вычисления {#вычисления}

-   Можно перекрестно ссылаться на таблицы, созданные из кода, выполненного с помощью вычислений.
-   Для этого добавьте параметры `label` и `tbl-cap`:
    ````markdown
    ```{r}
    #| label: tbl-iris
    #| tbl-cap: "Iris Data"

    library(knitr)
    kable(head(iris))
    ```
    ````

-   Можно создать несколько таблиц в ячейке кода и ссылаться на них как на подтаблицы.
-   Для этого добавьте `tbl-subcap` с массивом подписей:
    ````markdown
    ```{r}
    #| label: tbl-tables
    #| tbl-cap: "Tables"
    #| tbl-subcap:
    #|   - "Cars"
    #|   - "Pressure"
    #| layout-ncol: 2

    library(knitr)
    kable(head(cars))
    kable(head(pressure))
    ```
    ````
-   Если вы хотите, чтобы подписи к подтаблицам включали только идентификатор, например `(a)`, а не текстовую подпись, укажите `tbl-subcap: true` вместо предоставления явного текста подписи:
    ````markdown
    ```{r}
    #| label: tbl-tables
    #| tbl-cap: "Tables"
    #| tbl-subcap: true
    #| layout-ncol: 2

    library(knitr)
    kable(head(cars))
    kable(head(pressure))
    ```
    ````


## <span class="section-num">7</span> Листинги {#листинги}

-   Чтобы создать блок кода, на который можно ссылаться, добавьте атрибут `#lst-` вместе с `lst-cap`:
    ````markdown
    ```{#lst-customers .sql lst-cap="Customers Query"}
    SELECT * FROM Customers
    ```

    Then we query the customers database (@lst-customers).
    ````
-   Чтобы создать перекрестную ссылку на листинг кода с использованием синтаксиса `div`, создайте `div` с идентификатором, начинающимся с `lst-`, включите ячейку кода, за которой следует заголовок внутри `div`:
    ````markdown
    ::: {#lst-customers}

    ```{.sql}
    SELECT * FROM Customers
    ```

    Customers Query

    :::
    ````


### <span class="section-num">7.1</span> Вычисления {#вычисления}

-   Чтобы создать перекрёстную ссылку на код из исполняемого блока кода, добавьте параметры ячейки кода `lst-label` и `lst-cap`.
-   Вариант `lst-label` предоставляет идентификатор перекрёстной ссылки и должен начинаться с префикса `lst-`. Значение `lst-cap` предоставляет заголовок для листинга кода:
    ````markdown
    ```{python}
    #| lst-label: lst-import
    #| lst-cap: Import pyplot

    import matplotlib.pyplot as plt
    ```

    @lst-import
    ````

-   Если ячейка кода создаёт рисунок или таблицу, вы можете объединить варианты `lst-` с `label` и `fig-cap` и `tbl-cap` для создания перекрёстных ссылок на код и вывод:
    ````markdown
    ```{python}
    #| label: fig-plot
    #| fig-cap: Figure caption
    #| lst-label: lst-plot
    #| lst-cap: Listing caption

    plt.plot([1,23,2,4])
    plt.show()
    ```

    The code in @lst-plot produces the figure in @fig-plot.
    ````


## <span class="section-num">8</span> Выноски {#выноски}

-   Чтобы сделать перекрестную ссылку на выноску, добавьте атрибут ID, который начинается с соответствующего префикса выноски.
-   Затем вы можете ссылаться на выноску, используя обычный синтаксис `@`.
-   Например, здесь мы добавляем ID `#tip-example` к выноске, а затем ссылаемся на неё:
    ````markdown
    ::: {#tip-example .callout-tip}
    ## Cross-Referencing a Tip

    Add an ID starting with `#tip-` to reference a tip.
    :::

    See @tip-example
    ````

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 2:</span>
  Префиксы для перекрестных ссылок выносок
</div>

| Тип выноски | Префикс |
|-------------|---------|
| `note`      | `#nte-` |
| `tip`       | `#tip-` |
| `warning`   | `#wrn-` |
| `important` | `#imp-` |
| `caution`   | `#cau-` |


## <span class="section-num">9</span> Теоремы и доказательства {#теоремы-и-доказательства}

-   Чтобы включить теорему, на которую можно ссылаться, создайте `div` с меткой `#thm-` (или одним из других теорийных тегов).
-   Необходимо указать название теоремы через первый заголовок в блоке.
-   Можно включить любой контент в `div`:
    ````markdown
    ::: {#thm-line}

    ## Line

    The equation of any straight line, called a linear equation, can be written as:

    $$
    y = mx + b
    $$
    :::

    See @thm-line.
    ````

-   Для вывода LaTeX используется пакет `amsthm`.

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 3:</span>
  Метки разных вариантов теорем
</div>

| **Префикс метки** | **Печатное имя** | **Среда LaTeX** |
|-------------------|------------------|-----------------|
| `#thm-`           | Теорема          | теорема         |
| `#lem-`           | Лемма            | лемма           |
| `#cor-`           | Следствие        | следствие       |
| `#prp-`           | Предложение      | предложение     |
| `#cnj-`           | Догадка          | предположение   |
| `#def-`           | Определение      | определение     |
| `#exm-`           | Пример           | пример          |
| `#exr-`           | Упражнение       | упражнение      |
| `#sol-`           | Решение          | решение         |
| `#rem-`           | Замечание        | замечание       |

-   Доказательства (`proof`) получает такой же набор, как и теоремы, однако не нумеруется (и, следовательно, не может иметь перекрестной ссылки).
-   Чтобы создать доказательство, добавьте класс `.proof` к `div`:
    ````markdown
    ::: {.proof}
    By induction.
    :::
    ````

-   Как и в случае с теоремами, можно по желанию включить заголовок в качестве первого элемента `div` (или в атрибут `name`).


## <span class="section-num">10</span> Уравнения {#уравнения}

-   Метку `#eq-` поставьте сразу после уравнения, чтобы на него можно было ссылаться:
    ````markdown
    Black-Scholes (@eq-black-scholes) is a mathematical model that seeks to explain the behavior of financial derivatives, most commonly options:

    $$
    \frac{\partial \mathrm C}{ \partial \mathrm t } + \frac{1}{2}\sigma^{2} \mathrm S^{2}
    \frac{\partial^{2} \mathrm C}{\partial \mathrm S^2}
    ​  + \mathrm r \mathrm S \frac{\partial \mathrm C}{\partial \mathrm S}\ =
      \mathrm r \mathrm C
    $$ {#eq-black-scholes}
    ````


## <span class="section-num">11</span> Разделы {#разделы}

-   Чтобы сослаться на раздел, добавьте метку `#sec-` к любому заголовку:
    ````markdown
    ## Introduction {#sec-introduction}

    See @sec-introduction for additional context.
    ````

-   При использовании перекрестных ссылок разделов вам также необходимо включить вариант `number-sections`:
    ````yaml
    ---
    title: "My Document"
    number-sections: true
    ---
    ````
