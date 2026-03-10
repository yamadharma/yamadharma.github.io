---
title: "Quarto. Презентации"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-13T14:24:00+03:00
lastmod: 2025-05-13T16:00:00+03:00
tags: ["markdown", "science-writing"]
categories: ["computer-science"]
draft: false
slug: "quarto-presentation"
---

Quarto. Презентации.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Поддерживаемые форматы презентаций:
    -   `revealjs` (HTML);
    -   `pptx` (MS Office);
    -   `beamer` (LaTeX/PDF).


## <span class="section-num">2</span> Общее для разных форматов {#общее-для-разных-форматов}


### <span class="section-num">2.1</span> Структура слайдов {#структура-слайдов}

-   В markdown слайды разграничиваются с помощью заголовков.
-   Например, простое слайд-шоу с двумя слайдами, каждый из которых определен заголовком уровня 2 (`##`):
    ```markdown
    ---
    title: "Habits"
    author: "John Doe"
    format: revealjs
    ---

    ## Getting up

    - Turn off alarm
    ​- Get out of bed

    ## Going to sleep

    - Get in bed
    ​- Count sheep
    ```

-   Можно разделить слайд-шоу на разделы с титульными слайдами, используя заголовок 1-го уровня (`#`):
    ```markdown
    ---
    title: "Habits"
    author: "John Doe"
    format: revealjs
    ---

    # In the morning

    ## Getting up

    - Turn off alarm
    ​- Get out of bed

    ## Breakfast

    - Eat eggs
    ​- Drink coffee

    # In the evening

    ## Dinner

    - Eat spaghetti
    ​- Drink wine

    ## Going to sleep

    - Get in bed
    ​- Count sheep
    ```

-   Также можно разграничить слайды с помощью горизонтальных линий (например, если слайд без заголовка):
    ```markdown
    ---
    title: "Habits"
    author: "John Doe"
    format: revealjs
    ---

    - Turn off alarm
    ​- Get out of bed

    ---

    - Get in bed
    ​- Count sheep
    ```

-   Уровень исподьзуемых заголовков можно настроить с помощью `slide-level`.


### <span class="section-num">2.2</span> Инкрементные списки {#инкрементные-списки}

-   По умолчанию нумерованные и маркированные списки в слайдах отображаются все одновременно.
-   Можно переопределить это глобально с помощью `incremental`:
    ```yaml
    title: "My Presentation"
    format:
      revealjs:
        incremental: true
      beamer:
        incremental: true
    ```

-   Можно явно сделать любой список инкрементным или неинкрементным, заключив его в `div` с явным классом, который определяет режим:
    ```markdown
    ::: {.incremental}

    - Eat spaghetti
    ​- Drink wine

    :::
    ```

-   Сделать список неинкрементным:
    ```markdown
    ::: {.nonincremental}

    - Eat spaghetti
    ​- Drink wine

    :::
    ```


### <span class="section-num">2.3</span> Несколько столбцов {#несколько-столбцов}

-   Чтобы разместить материал в столбцах рядом, можно использовать контейнер `div` с классом `.columns`, содержащий два или более контейнеров `div` с классом `.column` и атрибутом `width`:
    ```markdown
    :::: {.columns}

    ::: {.column width="40%"}
    contents...
    :::

    ::: {.column width="60%"}
    contents...
    :::

    ::::
    ```


## <span class="section-num">3</span> Слайды beamer {#слайды-beamer}


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   По умолчанию в формате beamer используются параметры `echo: false` и `warning: false`.
    -   В результате ячейки исполняемого кода в стандартных документах Beamer не будут показывать сам код или сгенерированные предупреждения.
    -   Как и в случае с другими параметрами, вы можете переопределить это поведение в метаданных документа или индивидуально в каждой исполняемой ячейке.


### <span class="section-num">3.2</span> Структура слайдов {#структура-слайдов}

-   В Beamer заголовки ниже `slide-level` будут размещать контент внутри `block`:
    ```markdown
    ---
    title: "Habits"
    author: "John Doe"
    format:
      beamer:
        slide-level: 2
    ---

    ## Slide

    ### Simple block

    Content
    ```

-   Можно добавить класс `.alert` или `.example` для размещения контента внутри `alertblock` или `exampleblock`:
    ```markdown
    ---
    title: "Habits"
    author: "John Doe"
    format:
      beamer:
        slide-level: 2
    ---

    ## Slide

    ### Alert block {.alert}

    Content

    ### Example block {.example}

    Content
    ```


### <span class="section-num">3.3</span> Инкрементные списки {#инкрементные-списки}

-   Можно вставить паузу в слайд (скрыв содержимое после паузы), вставив три точки, разделенные пробелами:
    ```markdown
    ## Slide with a pause

    content before the pause

    . . .

    content after the pause
    ```


### <span class="section-num">3.4</span> Несколько столбцов {#несколько-столбцов}

-   Контейнеры `div` с классами `columns` и `column` могут опционально иметь атрибут `align`. Класс `columns` может опционально иметь атрибуты `totalwidth` или `onlytextwidth`:
    ```markdown
    :::: {.columns align=center totalwidth=8em}

    ::: {.column width="40%"}
    contents...
    :::

    ::: {.column width="60%" align=bottom}
    contents...
    :::

    ::::
    ```

-   Атрибуты `align` для `columns` и `column` может использоваться со значениями `top`, `top-baseline`, `center` и `bottom` для вертикального выравнивания столбцов. По умолчанию используется `top`.
-   Атрибут `totalwidth` ограничивает ширину столбцов заданным значением.
-   Класс `onlytextwidth` устанавливает `totalwidth` в `\textwidth`:
    ```markdown
    ::::  {.columns align=top .onlytextwidth}

    ::: {.column width="40%" align=center}
    contents...
    :::

    ::: {.column width="60%"}
    contents...
    :::

    ::::
    ```


### <span class="section-num">3.5</span> Опции beamer {#опции-beamer}

-   Можно задать опции для презентации `beamer`:
    ```yaml
    ---
    title: "Presentation"
    format:
      beamer:
        aspectratio: 32
        navigation: horizontal
        theme: AnnArbor
        colortheme: lily
    ---
    ```

-   `aspectratio` : Соотношение сторон слайда: `43` для 4:3 (по умолчанию), `169` для 16:9, `1610` для 16:10, `149` для 14:9, `141` для 1,41:1, `54` для 5:4, `32` для 3:2
-   `beamerarticle` : создать статью из слайдов Beamer
-   `beameroption` : дополнительные опции `\setbeameroption{}`
-   `institute` : принадлежность автора: может быть списком, если авторов несколько.
-   `logo` : изображение логотипа для слайдов
-   `navigation` : символы навигации (по умолчанию `empty` --- отсутствие навигационных символов; другие допустимые значения: `frame`, `vertical`, `horizontal`)
-   `section-titles` : включает «титульные страницы» для новых разделов (по умолчанию `true`)
-   `theme, colortheme, fonttheme, innertheme, outertheme` : темы для Beamer
-   `themeoptions` : опции для тем
-   `titlegraphic` :  изображение для титульного слайда


### <span class="section-num">3.6</span> Атрибуты фрейма {#атрибуты-фрейма}

-   Иногда необходимо добавить LaTeX вариант `fragile` для кадра (например, при использовании среда `minted`).
-   Это можно сделать принудительно, добавив класс `fragile` к заголовку:
    ```markdown
    # Fragile slide {.fragile}
    ```
-   Можно использовать атрибуты `allowdisplaybreaks`, `allowframebreaks`, `b`, `c`, `t`, `environment`, `label`, `plain`, `shrink`, `standout`, `noframenumbering`.


### <span class="section-num">3.7</span> Фоновые изображения {#фоновые-изображения}

-   Для общего фонового изображения для всех слайдов презентации Beamer используйте `background-image`:
    ```yaml
    ---
    format:
      beamer:
        background-image: background.png
    ---
    ```
