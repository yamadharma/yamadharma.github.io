---
title: "Quarto. Таблицы-списки"
author: ["Dmitry S. Kulyabov"]
date: 2026-04-11T17:52:00+03:00
lastmod: 2026-04-11T18:16:00+03:00
tags: ["markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-list-tables"
---

Quarto. Таблицы-списки.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Первоначально было реализовано в виде плагина.
-   Репозиторий: <https://github.com/pandoc-ext/list-table>
-   В quarto 1.9 интегрировано в основной код.


## <span class="section-num">2</span> Синтаксис {#синтаксис}

-   Таблицы-списки предоставляют альтернативный синтаксис для создания таблиц со сложным содержимым, таким как несколько абзацев, блоки кода или списки.
-   Используют привычный синтаксис маркированных списков, что упрощает их написание и сопровождение.
-   Таблица-список представляет собой div-элемент с классом `.list-table`.
-   Содержит маркированный список.
-   Каждый маркер верхнего уровня представляет собой строку, а вложенные маркеры представляют собой ячейки:

<!--listend-->

```markdown
::: {.list-table}
- - Fruit
  - Price

- - Apple
  - 1.20

- - Orange
  - 0.90
:::
```

| Фрукты   | Цена |
|----------|------|
| Яблоко   | 1.20 |
| Апельсин | 0,90 |

-   Таблицы-списки поддерживают блочные элементы внутри ячеек, включая блоки кода и списки:

<!--listend-->

````markdown
::: {.list-table}
- - Function
  - Description

- - `sum()`
  - Add values:

    ```python
    sum([1, 2, 3])
    ```

- - `len()`
  - Count items:

    - Works on lists
    - Works on strings
:::
````


## <span class="section-num">3</span> Заголовок {#заголовок}

-   По умолчанию первая строка рассматривается как заголовок.
-   Чтобы изменить это, установите параметр `header-rows=0`:

<!--listend-->

````markdown
::: {.list-table header-rows=0}
- - Apple
  - 1.20

- - Orange
  - 0.90
:::
````

| Яблоко   | 1.20 |
|----------|------|
| Апельсин | 0,90 |


## <span class="section-num">4</span> Выравнивание в колонках {#выравнивание-в-колонках}

-   Выравнивание столбцов задаётся с помощью атрибута `aligns` с вариантами: `d` (по умолчанию), `l` (на лево), `r` (на право), `c` (центрировать):

<!--listend-->

````markdown
::: {.list-table aligns="l,r"}
- - Fruit
  - Price

- - Apple
  - 1.20

- - Orange
  - 0.90
:::
````


## <span class="section-num">5</span> Ширина столбцов {#ширина-столбцов}

-   Можно указать относительную ширину столбцов, добавив соответствующий атрибут `tbl-colwidths`:

<!--listend-->

````markdown
::: {.list-table tbl-colwidths="[75,25]"}
- - Fruit
  - Price

- - Apple
  - 1.20

- - Orange
  - 0.90
:::
````


## <span class="section-num">6</span> Подписи и перекрестные ссылки {#подписи-и-перекрестные-ссылки}

-   Добавьте подпись, включив абзац в начало элемента `div`:

<!--listend-->

````markdown
::: {.list-table}
Fruit prices

- - Fruit
  - Price

- - Apple
  - 1.20
:::
````

-   Чтобы сделать таблицу-список перекрестно связанной, добавьте идентификатор с указанием префикса `tbl-`:

<!--listend-->

````markdown
::: {#tbl-fruits .list-table}
Fruit prices

- - Fruit
  - Price

- - Apple
  - 1.20
:::

See @tbl-fruits.
````


## <span class="section-num">7</span> Атрибуты ячейки {#атрибуты-ячейки}

-   Чтобы добавить атрибуты к ячейке, начните ячейку с пустого тега `<span>`, содержащего эти атрибуты.
-   Например, используйте: `rowspan` и `colspan` для переноса ячеек на несколько строк или столбцов:

<!--listend-->

````markdown
::: {.list-table}
- - []{colspan=2} Item
  - Price

- - []{rowspan=2} Citrus
  - Orange
  - 0.90

- - Lemon
  - 0.80

- - []{rowspan=2} Stone Fruit
  - Peach
  - 1.20

- - Plum
  - 1.00
:::
````
