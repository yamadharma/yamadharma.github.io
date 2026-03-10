---
title: "LaTeX. Класс статьи quantumarticle"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-07T20:53:00+03:00
lastmod: 2025-01-08T13:43:00+03:00
tags: ["latex"]
categories: ["science", "computer-science"]
draft: false
slug: "latex-class-quantumarticle"
---

LaTeX. Класс статьи quantumarticle.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   CTAN: <https://ctan.org/pkg/quantumarticle>
-   Репозиторий: <https://github.com/quantum-journal/quantum-journal>
-   Класс `quantumarticle` предназначен для открытого журнала по квантовой науке _Quantum_ (<https://quantum-journal.org/>).
-   Разработан для обеспечения плавного перехода от документов, набранных с использованием классов _article_, _revtex4-1_ и _elsarticle_ (см. [LaTeX. Шаблоны публикаций. Elsevier]({{< relref "2021-07-03-latex-publication-templates-elsevier" >}})).
-   Все статьи в Quantum должны быть представлены в _arXiv_.
-   Поэтому класс документов `quantumarticle` реализует ряд специфических для _arXiv_ проверок (можно отключить с помощью опции `noarxiv`).
-   Использует форматы авторов и аффилиаций и как в revtex, и как в elsarticle (см. [LaTeX. Авторы и аффилиации в статьях]({{< relref "2025-01-07--latex-authors-affiliations-articles" >}})).
