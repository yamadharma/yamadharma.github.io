---
title: "Quarto. Таблицы"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-17T15:42:00+03:00
lastmod: 2026-05-04T13:27:00+03:00
tags: ["science-writing", "markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-table"
---

Quarto. Таблицы.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Таблицы без обрамления {#таблицы-без-обрамления}


### <span class="section-num">1.1</span> Для PDF-документов {#для-pdf-документов}

-   Переопределите LaTeX-правила в YAML-заголовке или перед таблицей:
    ```yaml
    format:
      pdf:
        header-includes: |
          % Отключаем booktabs для всех таблиц, чтобы вернуть стандартные линии
          \renewcommand{\toprule}[2]{}
          \renewcommand{\midrule}[2]{}
          \renewcommand{\bottomrule}[2]{}
    ```
-   Это удалит линии.


### <span class="section-num">1.2</span> Для HTML-вывода {#для-html-вывода}

-   Добавьте CSS-стили:
    ```css
    table, th, td {
      border: none !important;
      border-collapse: collapse;
    }
    ```

-   Можно вставить в отдельный блок `css` или в файл стилей.


### <span class="section-num">1.3</span> Описание таблицы {#описание-таблицы}

1.  Используйте параметр класса `borderless` в YAML-заголовке таблицы:
    ```markdown
    ::: {.borderless}
    | Column1 | Column2 |
    |---------|---------|
    | Data    | Data    |
    :::
    ```

2.  Для таблиц из кода добавьте опции:
    ```yaml
    #| tbl-cap-location: top
    #| tbl-class: borderless
    ```


### <span class="section-num">1.4</span> Вернуть обрамление {#вернуть-обрамление}

-   Измените YAML-заголовок так, чтобы сохранить исходные определения `booktabs` перед тем, как переопределять их для всех таблиц:

<!--listend-->

```markdown
---
title: "Ваш документ"
format:
  pdf:
    include-in-header:
      text: |
        % Сохраняем стандартные booktabs-команды
        \let\oldtoprule\toprule
        \let\oldmidrule\midrule
        \let\oldbottomrule\bottomrule
        % Убираем линии для всех таблиц
        \renewcommand{\toprule}[2]{}
        \renewcommand{\midrule}[2]{}
        \renewcommand{\bottomrule}[2]{}
        \setlength{\arrayrulewidth}{0.5pt}
---
```

-   Оберните нужную таблицу в LaTeX-группу `\begingroup...\endgroup`, внутри которой временно восстановите сохранённые команды:

<!--listend-->

```markdown
\begingroup
\let\toprule\oldtoprule
\let\midrule\oldmidrule
\let\bottomrule\oldbottomrule

| Column1 | Column2 |
|---------|---------|
| Data    | Data    |

\endgroup
```

-   Только эта таблица будет отрисована в стиле `booktabs`.


## <span class="section-num">2</span> Варианты {#варианты}

-   [Quarto. Таблицы-списки]({{< relref "2026-04-11--quarto-list-tables" >}})
