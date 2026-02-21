---
title: "LaTeX. Авторы и аффилиации в статьях"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-07T21:08:00+03:00
lastmod: 2025-01-07T21:28:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex-authors-affiliations-articles"
---

LaTeX. Авторы и аффилиации в статьях.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Форматы задания авторов и аффилиаций {#форматы-задания-авторов-и-аффилиаций}


### <span class="section-num">1.1</span> revtex {#revtex}

-   Класс revtex.
-   CTAN: <https://ctan.org/pkg/revtex>
-   Сайт: <https://journals.aps.org/revtex>
-   Аффилиация задаётся с помощью позиционирования относительно автора.
-   Используется запись авторов и аффилиаций в виде:
    ```latex
    \author{Author1}
    \author{Author2}
    \affiliation{Affiliation1}
    \author{Author3}
    \affiliation{Affiliation2}
    \author{Author4}
    \affiliation{Affiliation1}
    \affiliation{Affiliation3}
    ```
-   В этом примере _Affiliation1_ будет связана с авторами 1, 2 и 4, _Affiliation2_ --- с автором 3, _Affiliation3_ --- с автором 4.
-   Повторяющиеся аффилиации распознаются автоматически.


### <span class="section-num">1.2</span> elsarticle {#elsarticle}

-   Поддерживается в классе _elsarticle_, пакете _authblk_.
-   authblk
    -   CTAN: <https://ctan.org/pkg/authblk>
-   elsarticle
    -   CTAN: <https://ctan.org/pkg/elsarticle>
-   Отношение принадлежности указывается явно.
-   Используется запись авторов и аффилиаций в виде:
    ```latex
    \author[1]{Author1}
    \author[1]{Author2}
    \author[2]{Author3}
    \author[1,3]{Author4}
    \affil[1]{Affiliation1}
    \affil[2]{Affiliation2}
    \affil[3]{Affiliation3}
    ```
