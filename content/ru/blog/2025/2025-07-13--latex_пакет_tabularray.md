---
title: "LaTeX. Пакет tabularray"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-13T15:57:00+03:00
lastmod: 2025-10-22T22:29:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex_пакет_tabularray"
---

LaTeX. Пакет tabularray.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   CTAN: <https://ctan.org/pkg/tabularray>
-   Репозиторий: <https://github.com/lvjr/tabularray>
-   Написан на LaTeX3.
-   Напрямую использует функции LaTeX3 для разбора таблицы.
-   Разделяет содержание и стиль таблицы.
-   Стиль таблицы может быть полностью задан с помощью ключей.
-   Полезен при создании сложных таблиц с нестандартным оформлением, где требуется точный контроль над каждым элементом.
-   Его синтаксис сокращает время на настройку и упрощает поддержку кода.


## <span class="section-num">2</span> Особенности {#особенности}

-   Синтаксис с ключевыми параметрами
    -   Настройка таблиц осуществляется через ключевые параметры в окружении `tblr`, что делает код более читаемым:
        ```tex
        \begin{tblr}{
          colspec = {rX},
          colsep = 8mm,
          hlines = {2pt, white},
          row{odd} = {azure8},
          row{even} = {gray8},
        }
        ```

-   Гибкие настройки столбцов и строк
    -   Динамическое выравнивание: автоматическое определение ширины столбцов с возможностью ручной настройки.
    -   Цвет и форматирование: встроенные команды для заливки ячеек и изменения шрифта:
        ```tex
        \SetCell{bg=green9} Yes & \SetCell{bg=red8} No
        ```
-   Поддержка сложных конструкций.
-   Расширение макросов: позволяет использовать сложные конструкции внутри таблиц, включая динамические данные.
-   Интеграция с `booktabs`: совместим с профессиональным оформлением таблиц через пакет `booktabs`.


## <span class="section-num">3</span> Базовые принципы построения таблиц {#базовые-принципы-построения-таблиц}

-   Используйте `colspec` для определения типов столбцов:
    ```tex
    \begin{tblr}{colspec={X[l] X[c] X[r]}}
    ```

    -   `X[l]`: столбец с выравниванием по левому краю и автоматической шириной.
    -   `c`, `r`: центрированное и правое выравнивание соответственно.

-   Настройка внешнего вида:
    -   Горизонтальные линии: `hlines`, `hline{1}={blue, dashed}`.
    -   Вертикальные линии: `vlines`, `vline{1,4}={3pt}`.
    -   Цвет фона ячеек: `\SetCell{bg=green9}`.


## <span class="section-num">4</span> Примеры применения {#примеры-применения}

-   Простая таблица с цветом:

<!--listend-->

```tex
\usepackage{tabularray}
\begin{document}
\begin{tblr}{colspec={ccc}, hlines, vlines}
  Header 1 & Header 2 & Header 3 \\
  Data 1   & Data 2   & Data 3   \\
\end{tblr}
\end{document}
```

-   Таблица с динамическими данными:

<!--listend-->

```tex
\newcommand{\introrow}{Cat & Dog \\}
\begin{tblr}[expand=\introrow]{cc}
  \introrow
  Crow & Hawk \\
\end{tblr}
```


## <span class="section-num">5</span> Интеграция с booktab {#интеграция-с-booktab}


### <span class="section-num">5.1</span> Загрузка библиотеки `booktabs` {#загрузка-библиотеки-booktabs}

-   Добавьте в преамбулу документа команду:

<!--listend-->

```tex
\UseTblrLibrary{booktabs}
```

-   Это активирует совместимость с `booktabs`, позволяя использовать его команды внутри среды `tblr`.
-   Для многостраничных таблиц используйте среду `longtblr` с теми же настройками стиля.
-   Избегайте вертикальных линий --- они противоречат принципам профессионального оформления.
-   Настройте толщину линий через параметр `rule thickness` для точного соответствия стилю `booktabs`.


### <span class="section-num">5.2</span> Основные элементы стиля `booktabs` {#основные-элементы-стиля-booktabs}

-   Команды для горизонтальных линий:
    -   `\toprule` --- верхняя линия;
    -   `\midrule` --- средняя линия;
    -   `\bottomrule` --- нижняя линия.

-   Пример настройки:

<!--listend-->

```tex
\begin{tblr}{
  colspec = {ccc},
  hline = {white}, % Отключение стандартных горизонтальных линий
  vlines = {0pt},  % Отключение вертикальных линий (в стиле booktabs их нет)
}
\toprule
Header 1 & Header 2 & Header 3 \\
\midrule
Data 1 & Data 2 & Data 3 \\
\bottomrule
\end{tblr}
```


### <span class="section-num">5.3</span> Сравнение с `booktabs` {#сравнение-с-booktabs}

| Функция                 | tabularray                            | booktabs                         |
|-------------------------|---------------------------------------|----------------------------------|
| Синтаксис               | Ключевые параметры в среде `tblr`     | Традиционный синтаксис `tabular` |
| Линии                   | `\toprule`, `\midrule`, `\bottomrule` | Те же команды                    |
| Вертикальные линии      | Запрещены по умолчанию                | Не рекомендуются                 |
| Многостраничные таблицы | Среда `longtblr`                      | Пакет `longtable`                |


### <span class="section-num">5.4</span> Пример полной таблицы {#пример-полной-таблицы}

```tex
\usepackage{tabularray}
\UseTblrLibrary{booktabs}

\begin{document}
\begin{table}
  \centering
  \caption{Пример таблицы в стиле booktabs}
  \label{tab:example}
  \begin{tblr}{
    colspec = {X[l] X[r] X[c]},
    hline = {white},
    vlines = {0pt},
    row{1} = {font=\bfseries}, % Жирный шрифт для заголовков
  }
    \toprule
    Параметр & Значение & Единица \\
    \midrule
    Длина & 10.5 & м \\
    Ширина & 2.3 & см \\
    Высота & 5.1 & мм \\
    \bottomrule
  \end{tblr}
\end{table}
\end{document}
```


## <span class="section-num">6</span> Интеграция с siunitx {#интеграция-с-siunitx}

-   Загрузка:
    ```tex
    \UseTblrLibrary{siunitx}
    ```
-   Добавляются:
    -   ключ `si` для типа столбца `Q`;
    -   тип столбца `S` (как сахар для столбцов `Q`, центрируют по умолчанию).
-   Служат для выравнивания по десятичной точки.
    ```tex
    \begin{tblr}{
      hlines, vlines,
      colspec={Q[si={table-format=3.2},c]Q[si={table-format=3.2},c]},
      row{1} = {guard}
      }
      Head  & Head \\
      111 & 111 \\
      2.1 & 2.2 \\
      33.11 & 33.22 \\
    \end{tblr}
    ```
