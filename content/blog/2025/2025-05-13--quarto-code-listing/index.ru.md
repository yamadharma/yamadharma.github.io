---
title: "Quarto. Листинги"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-13T16:04:00+03:00
lastmod: 2026-01-27T19:13:00+03:00
tags: ["science-writing"]
categories: ["computer-science"]
draft: false
slug: "quarto-code-listing"
---

Quarto. Листинги.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Скрытый код {#скрытый-код}

-   Можно скрыть весь исходный код.
-   Необходимо указать `echo: false` как вариант в `execute`:
    ```yaml
    ---
    title: "My Document"
    execute:
      echo: false
    jupyter: python3
    ---
    ```

-   Можно переопределить эту опцию в блоке кода:
    ````markdown
    ```{python}
    #| echo: true

    import matplotlib.pyplot as plt
    plt.plot([1,2,3,4])
    plt.show()
    ```
    ````

-   Параметры блока кода включаются в специальный комментарий в верхней части блока (строки в верхней части начинаются с `#|` и рассматриваются как варианты).


## <span class="section-num">2</span> Перенос строк {#перенос-строк}

-   Ширина исходного кода может выходить за пределы доступного горизонтального пространства отображения.
-   В _html_ по умолчанию это приведёт к горизонтальной полосе прокрутки для блока кода.
-   Можно вместо этого сделать перенос длинных строк.
-   Чтобы задать глобальное поведение по умолчанию, используйте `code-overflow`:
    ````yaml
    format:
      html:
        code-overflow: wrap
    ````

-   Допустимые значения для `code-overflow`:
    -   `scroll` : прокрутить блоки кода, которые превышают доступную ширину (по умолчанию, соответствует `white-space: pre` );
    -   `wrap` :  переносить строки кода, которые превышают доступную ширину (соответствует `white-space: pre-wrap` ).
-   Можно переопределить глобальное значение по умолчанию для блока кода с помощью `code-overflow`:
    ````markdown
    ```{python}
    #| code-overflow: wrap

    # very long line of code....
    ```
    ````

-   Можно добавить классы `.code-overflow-scroll` или `.code-overflow-wrap`:
    ````markdown
    ```{.python .code-overflow-wrap}
    # very long line of code....
    ```
    ````


## <span class="section-num">3</span> Имя файла кода {#имя-файла-кода}

-   Можно использовать атрибут `filename` в блоках кода:
    ````markdown
    ```{.python filename="matplotlib.py"}
    import matplotlib.pyplot as plt
    plt.plot([1,23,2,4])
    plt.show()
    ```
    ````


## <span class="section-num">4</span> Аннотация кода {#аннотация-кода}


### <span class="section-num">4.1</span> Общая информация {#общая-информация}

-   Блоки кода и исполняемые ячейки кода в Quarto могут включать построчные аннотации.
-   Параметр `code-annotations` управляет тем, как аннотации отображаются в формате HTML (`below` (по умолчанию), `hover` или `select`), а также во всех форматах, отключены ли аннотации (`false`), или если аннотации следует удалить из вывода ( `none` ).


### <span class="section-num">4.2</span> Синтаксис аннотации {#синтаксис-аннотации}

-   Аннотации для ячейки кода состоят из двух связанных элементов:
    -   Каждая аннотированная строка должна заканчиваться комментарием (используя символ комментария языка ячейки кода), за которым следует пробел, а затем номер аннотации, заключенный в угловые скобки (например, `# <2>` ).
    -   Можно повторить номер аннотации, если аннотация занимает несколько строк.
    -   Упорядоченный список, который появляется сразу после ячейки кода, которая включает содержимое каждой аннотации.
    -   Каждый пронумерованный элемент в упорядоченном списке будет соответствовать строке кода с тем же номером аннотации.
-   Например:
    ````markdown
    ```r
    library(tidyverse)
    library(palmerpenguins)
    penguins |>                                      # <1>
      mutate(                                        # <2>
        bill_ratio = bill_depth_mm / bill_length_mm, # <2>
        bill_area  = bill_depth_mm * bill_length_mm  # <2>
      )                                              # <2>
    ```
    1. Take `penguins`, and then,
    2. add new columns for the bill ratio and bill area.
    ````


### <span class="section-num">4.3</span> Стиль аннотации {#стиль-аннотации}

-   Для вывода HTML есть три стиля аннотаций, которые можно задать с помощью `code-annotations` вариант документа:
    -   `below` : по умолчанию, текст аннотации кода будет отображаться под ячейкой кода;
    -   `hover` : текст аннотации кода будет отображаться при наведении курсора на маркер аннотации строки кода;
    -   `select` : текст аннотации кода будет отображаться, когда пользователь нажимает на маркер аннотации (выбирает его). Текст аннотации можно убрать, нажав на маркер аннотации еще раз.

-   Например:
    ````markdown
    ---
    code-annotations: hover
    ---

    ```r
    library(tidyverse)
    library(palmerpenguins)
    penguins |>                                      # <1>
      mutate(                                        # <2>
        bill_ratio = bill_depth_mm / bill_length_mm, # <2>
        bill_area  = bill_depth_mm * bill_length_mm  # <2>
      )                                              # <2>
    ```
    1. Take `penguins`, and then,
    2. add new columns for the bill ratio and bill area.
    ````


## <span class="section-num">5</span> Номера строк {#номера-строк}

-   Если вы хотите отобразить номера строк рядом с блоком кода, добавьте `code-line-numbers`:
    ````yaml
    format:
      html:
        code-line-numbers: true
    ````

-   Можно включить номера строк для отдельного блока кода с помощью `code-line-numbers`:
    ````markdown
    ``` {.python code-line-numbers="true"}
    import matplotlib.pyplot as plt
    plt.plot([1,23,2,4])
    plt.show()
    ```
    ````


## <span class="section-num">6</span> Исполняемые блоки {#исполняемые-блоки}

-   Иногда нужно включить блок кода исключительно в качестве документации (не исполняемого).
-   Вы можете сделать это, используя двойные фигурные скобки вокруг языка (например, `python`, `r` и т. д.):
    ````markdown
    ```{{python}}
    1 + 1
    ```
    ````

-   Если необходимо показать пример с несколькими блоками кода и другой разметкой, просто заключите весь пример в 4 обратных кавычки (например, `` ```` `` ) и используйте синтаксис с двумя фигурными скобками для блоков кода внутри:
    `````markdown
    ````
    ---
    title: "My document"
    ---

    Some markdown content.

    ```{{python}}
    1 + 1
    ```

    Some additional markdown content.

    ````
    `````


## <span class="section-num">7</span> Подключение внешних файлов {#подключение-внешних-файлов}

-   Для подключения листингов из внешнего файла можно использовать плагины.


### <span class="section-num">7.1</span> quarto-ext/include-code-files {#quarto-ext-include-code-files}

-   Репозиторий: <https://github.com/quarto-ext/include-code-files>
-   На данный момент поддерживаются следующие языки: python, r, julia, html, js, ojs, css.


#### <span class="section-num">7.1.1</span> Установка {#установка}

`````shell
quarto add quarto-ext/include-code-files
`````


#### <span class="section-num">7.1.2</span> Подключение {#подключение}

-   Добавьте в файл `_quarto.yml`:
    `````yaml
    filters:
    ​   - include-code-files
    `````


#### <span class="section-num">7.1.3</span> Использование {#использование}

-   Подключите код из внешнего файла:
    `````markdown
    ```{.python include="script.py"}
    ```
    `````
