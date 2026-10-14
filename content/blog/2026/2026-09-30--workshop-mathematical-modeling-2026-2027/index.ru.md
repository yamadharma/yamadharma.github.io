---
title: "Семинар Математическое моделирование, 2026-2027"
author: ["Dmitry S. Kulyabov"]
date: 2026-09-30T19:49:00+03:00
lastmod: 2026-10-13T16:21:00+03:00
tags: ["modeling"]
categories: ["science"]
draft: false
slug: "workshop-mathematical-modeling-2026-2027"
---

Семинар Математическое моделирование, 2026-2027.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Семинар Математическое моделирование, 2026-2 {#семинар-математическое-моделирование-2026-2}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.1</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2026-10-01 Чт&gt;</span></span> Кулябов Д. С. - Структура научного семинара {#кулябов-д-dot-с-dot-структура-научного-семинара}


#### <span class="section-num">1.1.1</span> Докладчик {#докладчик}

-   Кулябов, Дмитрий Сергеевич
-   доктор физико-математических наук
-   профессор кафедры ТВиК


#### <span class="section-num">1.1.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/335/>
-   Структура научного семинара
-   Кулябов, Д. С.
-   д.ф.м.-н., профессор кафедры ТВиК ФФМиЕН РУДН

Обсуждаются цели и задачи научных семинаров.
Предлагаются варианты модификации семинара Математическое моделирование.

---

-   Structure of the research seminar
-   Kulyabov, D. S.
-   Doctor of Physical and Mathematical Sciences, Professor, Department of Probability Theory and Cybernetics, Faculty of Physics, Mathematics and Natural Sciences, RUDN University

The goals and objectives of research seminars are discussed.
Options for modifying the Mathematical Modeling seminar are proposed.


#### <span class="section-num">1.1.3</span> Видео {#видео}

{{< tabs "Кулябов Д. С. - Структура научного семинара" >}}

{{< tab "RuTube" >}}{{< rutube 5c4236703dd626a373cd296da4571d8b >}}{{< /tab >}}

{{< tab "VKvideo" >}}{{< vkvideo oid=-230024722 id=456239688 hd=2 >}}{{< /tab >}}

{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.2</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2026-10-08 Чт&gt;</span></span> Блинков Ю. А. - Ленивые вычисления для полиномов: структура Lazy и PolyLazy {#блинков-ю-dot-а-dot-ленивые-вычисления-для-полиномов-структура-lazy-и-polylazy}


#### <span class="section-num">1.2.1</span> Докладчик {#докладчик}

-   Блинков Ю.А.
-   доктор физико-математических наук
-   зав. каф. СГУ
-   e-mail: blinkovua@info.sgu.ru


#### <span class="section-num">1.2.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/334/>
-   Ленивые вычисления для полиномов: структура Lazy и PolyLazy
-   Блинков Ю. А.
-   д.ф.м.-н., зав. каф. СГУ
-   <https://github.com/blinkovua/GInv>

Доклад посвящён применению ленивых вычислений в задачах компьютерной алгебры при работе с полиномами. Рассматривается структура Lazy, представляющая отложенное умножение полинома на моном и коэффициент, и структура PolyLazy, организующая множество таких отложенных вычислений в кучу (max-heap) по старшему моному. Основная идея подхода состоит в том, чтобы не вычислять полином целиком сразу, а продвигаться по нему покомпонентно лишь по мере необходимости. Это позволяет эффективно обрабатывать сокращения членов полинома, избегать лишних умножений и сложений коэффициентов, а также работать с потенциально бесконечными рядами. В докладе описываются ключевые операции: метод next(), продвигающий ленивое вычисление на один шаг; канонизация вершины кучи (canonicalize_top()), объединяющая одинаковые мономы; операция редукции PolyLazy; а также алгоритм to_poly() для преобразования ленивого представления обратно в обычный полином. Приводится полный цикл работы и обсуждаются преимущества ленивого подхода.

---

-   Lazy Computations for Polynomials: The Lazy and PolyLazy Structures
-   Blinkov, Yu. A.
-   Doctor of Physics and Mathematics
-   Head. department SSU
-   <https://github.com/blinkovua/GInv>

The talk addresses the application of lazy computations to polynomials in computer algebra. We consider the Lazy structure, which represents a deferred multiplication of a polynomial by a monomial and a coefficient, and the PolyLazy structure, which organizes a collection of such deferred computations into a max-heap ordered by the leading monomial. The key idea is to avoid computing the entire polynomial at once and instead advance through it component by component only as needed. This enables efficient handling of term cancellations, avoids redundant multiplications and additions of coefficients, and supports work with potentially infinite series. The talk describes the main operations: the next() method, which advances the lazy computation by one step; canonicalization of the heap top (canonicalize_top()), which merges equal monomials; the PolyLazy reduction operation; and the to_poly() algorithm for converting the lazy representation back into an ordinary polynomial. A complete workflow is presented and the advantages of the lazy approach are discussed.


#### <span class="section-num">1.2.3</span> Видео {#видео}

{{< tabs "Блинков Ю. А. - Ленивые вычисления для полиномов: структура Lazy и PolyLazy" >}}

{{< tab "RuTube" >}}{{< rutube b2f4e99d0916aca2917d46c7e1639fb5 >}}{{< /tab >}}

{{< tab "VKvideo" >}}{{< vkvideo oid=-230024722 id=456239693 hd=2 >}}{{< /tab >}}

{{< /tabs >}}


### <span class="org-todo todo TODO">TODO</span> <span class="section-num">1.3</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2026-10-15 Чт&gt;</span></span> Бааж О. - Устойчивое решение смешанной задачи для уравнения Пуассона с неоднородными граничными условиями первого рода в приложении к обратной задаче термографии {#бааж-о-dot-устойчивое-решение-смешанной-задачи-для-уравнения-пуассона-с-неоднородными-граничными-условиями-первого-рода-в-приложении-к-обратной-задаче-термографии}


#### <span class="section-num">1.3.1</span> Докладчик {#докладчик}

-   Обаида Бааж
-   аспирант Математического института им. С. М. Никольского, РУДН


#### <span class="section-num">1.3.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/336/>
-   Устойчивое решение смешанной задачи для уравнения Пуассона с неоднородными граничными условиями первого рода в приложении к обратной задаче термографии
-   Обаида Бааж
-   аспирант Математического института им. С. М. Никольского, РУДН

Рассматривается вариант обратной задачи термографии, приводящий к некорректно поставленной смешанной краевой задаче для уравнения Пуассона с данными Коши на поверхности достаточно общего вида. Предложен метод решения, основанный на сведении задачи к интегральному уравнению первого рода и использующий метод регуляризации Тихонова. Предлагаемый метод включает вычисление интеграла по поверхности, с которой снимается термограмма. В том случае, когда поверхность задана с погрешностью, возникает задача о вычислении нормали к поверхности, заданной приближенно. Для устойчивого вычисления нормали используется метод регуляризации в формулировке Морозова. Для приближенного решения обратной задачи доказана теорема сходимости к точному решению при стремлении к нулю погрешности в данных. Приводятся численные примеры решения задачи.

---

-   Stable solution of the mixed problem for the Poisson equation with non‑homogeneous boundary conditions of the first kind, applied to the inverse thermography problem
-   Obaida Baaj
-   Post Graduate Student of Nikolsky Mathematical Institute, RUDN University

A variant of the inverse thermography problem is considered, which leads to an ill-posed mixed boundary value problem for the Poisson equation with Cauchy data on a surface of a fairly general type. A solution method is proposed, based on reducing the problem to an integral equation of the first kind and using Tikhonov regularization. The proposed method involves calculating an integral over the surface from which the thermogram is taken. In the case where the surface is given with an error, a problem arises of calculating the normal to the surface, which is given approximately. For stable calculation of the normal, the regularization method in Morozov’s formulation is used. For an approximate solution to the inverse problem, a convergence theorem to the exact solution is proven as the error in the data approaches zero. Numerical examples of solving the problem are provided.


### <span class="org-todo todo TODO">TODO</span> <span class="section-num">1.4</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2026-10-22 Чт&gt;</span></span> Геворкян М. Н. - Система ведения полезных заметок Zettelkasten {#геворкян-м-dot-н-dot-система-ведения-полезных-заметок-zettelkasten}


#### <span class="section-num">1.4.1</span> Докладчик {#докладчик}

-   Геворкян Мигран Нельсонович
    -   доцент, к.ф.-м.н, доцент
    -   кафедра теории вероятностей и кибербезопасности РУДН


#### <span class="section-num">1.4.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/340/>
-   Система ведения полезных заметок Zettelkasten
-   Геворкян Мигран Нельсонович
    -   доцент, к.ф.-м.н, доцент
    -   кафедра теории вероятностей и кибербезопасности РУДН

В небольшом докладе рассказывается о системе организации и ведения заметок под названием Zettelkasten (от немецкого Zettel --- записка и Kasten --- коробка). Изобретение основных принципов системы приписывается немецкому социологу Никласу Луману (1927-1998), который отличался большой публикационной активностью. В докладе описываются основные принципы системы, указываются некоторые тонкие места. Основные принципы довольно просты, но допускают различную реализацию как в электронном виде,так и вы аналоговом (бумажном).  Доклад может быть полезен студентам и аспирантам для организации своей научной работы.

---

-   The Zettelkasten system for keeping useful notes
-   Gevorkyan, Migran Nelsonovich
    -   Docent, PhD, Associate Professor
    -   Department of Probability Theory and Cybersecurity, RUDN University

A short report describes a system for organizing and taking notes called Zettelkasten (from the German word Zettel--- note and Kasten --- box). The invention of the basic principles of the system is attributed to the German sociologist Niklas Luhmann (1927-1998), who was notable for his great publishing activity. The report describes the basic principles of the system and points out some subtle points. The basic principles are quite simple, but they can be implemented in various ways, both electronically and in analog (paper) form. The report can be useful for students and postgraduates to organize their scientific work.
