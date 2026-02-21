---
title: "BibLaTeX. Уточнение типа публикации"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-30T17:32:00+03:00
lastmod: 2025-08-30T17:58:00+03:00
tags: ["latex", "bib"]
categories: ["computer-science"]
draft: false
slug: "biblatex-clarifying-publication-type"
---

BibLaTeX. Уточнение типа публикации.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Поле `entrysubtype` {#поле-entrysubtype}

-   Поле `entrysubtype` в biblatex --- это пользовательское поле, которое позволяет добавлять дополнительную классификацию к библиографическим записям.
-   Оно не является стандартным для всех стилей, но может быть настроено для отображения в любом стиле.
-   Уточняет жанр публикации.
-   Значения: произвольные строки, которые вы задаете сами:
    ```bibtex
    entrysubtype = {research},
    entrysubtype = {review},
    entrysubtype = {editorial}
    ```


## <span class="section-num">2</span> Жанры публикации {#жанры-публикации}

-   Научная статья/Research article
-   Обзорная статья/Review
-   Редакционная статья/Editorial
-   Рецензия на книгу/Book Review
-   Информационная статья/Information article


## <span class="section-num">3</span> Добавить `entrysubtype` в запись `.bib` {#добавить-entrysubtype-в-запись-dot-bib}

-   Укажите поле `entrysubtype` в вашей библиографической записи:

<!--listend-->

```bibtex
@article{smith2023,
  author       = {John Smith},
  title        = {Advances in Quantum Computing},
  journal      = {Journal of Physics},
  year         = {2023},
  entrysubtype = {research}  % Произвольное значение
}
```


## <span class="section-num">4</span> Добавить `entrysubtype` в библиографию {#добавить-entrysubtype-в-библиографию}

-   Чтобы `entrysubtype` отображался во всех стилях, добавьте в преамбулу:

<!--listend-->

```tex
\renewbibmacro{finentry}{%
  \printfield{entrysubtype}%  Выводим entrysubtype
  \finentry
}
```


## <span class="section-num">5</span> Настройка отображения {#настройка-отображения}

-   В квадратных скобках, курсивом:
    ```tex
    \DeclareFieldFormat{entrysubtype}{[\mkbibemph{#1}]}
    ```

-   Локализация (если нужно перевести значения на русский):
    ```tex
    \NewBibliographyString{research,review}
    \DefineBibliographyStrings{russian}{
      research = {исследование},
      review   = {обзор},
    }
    ```
