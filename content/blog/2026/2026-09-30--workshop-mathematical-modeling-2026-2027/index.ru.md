---
title: "Семинар Математическое моделирование, 2026-2027"
author: ["Dmitry S. Kulyabov"]
date: 2026-09-30T19:49:00+03:00
lastmod: 2026-11-01T18:50:00+03:00
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


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.3</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2026-10-15 Чт&gt;</span></span> Бааж О. - Устойчивое решение смешанной задачи для уравнения Пуассона с неоднородными граничными условиями первого рода в приложении к обратной задаче термографии {#бааж-о-dot-устойчивое-решение-смешанной-задачи-для-уравнения-пуассона-с-неоднородными-граничными-условиями-первого-рода-в-приложении-к-обратной-задаче-термографии}


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


#### <span class="section-num">1.3.3</span> Видео {#видео}

{{< tabs "Бааж О. - Устойчивое решение смешанной задачи для уравнения Пуассона с неоднородными граничными условиями первого рода в приложении к обратной задаче термографии" >}}

{{< tab "RuTube" >}}{{< rutube bbc42575722f0243281089852a95cc3a >}}{{< /tab >}}

{{< tab "VKvideo" >}}{{< vkvideo oid=-230024722 id=456239699 hd=2 >}}{{< /tab >}}

{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.4</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2026-10-22 Чт&gt;</span></span> Геворкян М. Н. - Система ведения полезных заметок Zettelkasten {#геворкян-м-dot-н-dot-система-ведения-полезных-заметок-zettelkasten}


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


#### <span class="section-num">1.4.3</span> Видео {#видео}

{{< tabs "Геворкян М. Н. - Система ведения полезных заметок Zettelkasten" >}}

{{< tab "RuTube" >}}{{< rutube cdb658facf140fc9c4f2f13c1230195e >}}{{< /tab >}}

{{< tab "VKvideo" >}}{{< vkvideo oid=-230024722 id=456239703 hd=2 >}}{{< /tab >}}

{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.5</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2026-10-29 Чт&gt;</span></span> Геворкян М. Н. - Модель проективной геометрии RP3 {#геворкян-м-dot-н-dot-модель-проективной-геометрии-rp3}


#### <span class="section-num">1.5.1</span> Докладчик {#докладчик}

-   Геворкян Мигран Нельсонович
    -   доцент, к.ф.-м.н, доцент
    -   кафедра теории вероятностей и кибербезопасности РУДН


#### <span class="section-num">1.5.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/341/>
-   Модель проективной геометрии RP3
-   Геворкян Мигран Нельсонович
    -   доцент, к.ф.-м.н, доцент
    -   кафедра теории вероятностей и кибербезопасности РУДН

Доклад посвящен моделям проективной геометрии RPn. Данная модель строится для n-мерного проективного пространства с помощью (n+1)-мерного евклидова пространства. Последовательно рассмотрены модели для n=1,2,3. Основное внимание уделено RPn, как имеющей наибольшее прикладное значение. В рамках данной модели можно с помощью введения однородных координат развить аналитическую геометрию и описывать точки, прямые и плоскости в векторном виде.  Также рассмотрено проективное линейное преобразование, с помощью которого можно обобщить аффинные преобразования и, следовательно, преобразования подобия и движения (изометрии).

---

-   The RP3 model of projective geometry
-   Gevorkyan, Migran Nelsonovich
    -   Docent, PhD, Associate Professor
    -   Department of Probability Theory and Cybersecurity, RUDN University

The report is devoted to the RPn models of projective geometry. This model is constructed for an n-dimensional projective space using an (n+1)-dimensional Euclidean space. Models for n=1, 2, 3 are considered sequentially. The main focus is on RPn, as it has the greatest practical significance.  Within this model, it is possible to develop analytical geometry by introducing homogeneous coordinates and to describe points, lines, and planes in vector form.  The projective linear transformation is also considered, which can be used to generalize affine transformations and, consequently, similarity and motion (isometry) transformations.


#### <span class="section-num">1.5.3</span> Видео {#видео}

{{< tabs "Геворкян М. Н. - Модель проективной геометрии RP3" >}}

{{< tab "RuTube" >}}{{< rutube 227e3541c9d4a0fe6a4168d5bd16a61c >}}{{< /tab >}}

{{< tab "VKvideo" >}}{{< vkvideo oid=-230024722 id=456239708 hd=2 >}}{{< /tab >}}

{{< /tabs >}}


### <span class="org-todo todo TODO">TODO</span> <span class="section-num">1.6</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2026-11-05 Чт&gt;</span></span> Аррохо Э. Э. - Численное решение уравнения Моргана {#аррохо-э-dot-э-dot-численное-решение-уравнения-моргана}


#### <span class="section-num">1.6.1</span> Докладчик {#докладчик}

-   Аррохо Эрнандес Эноэль
    -   аспирант
    -   кафедра математического моделирования и искусственного интеллекта РУДН


#### <span class="section-num">1.6.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/344/>
-   Численное решение уравнения Моргана
-   Аррохо Эрнандес Эноэль
    -   аспирант
    -   кафедра математического моделирования и искусственного интеллекта РУДН

Уравнение Моргана играет важную роль в теории градиентных линз, оно связывает переменный показатель преломления и траектории лучей. В работе рассматривается задача численного решения уравнения Моргана для проектирования тонкопленочной волноводной линзы Люнеберга с гарантированной точностью.  Решение уравнения Моргана требует численного расчета несобственного интеграла, который вычисляется с помощью метода прямоугольников. Результаты, полученные методом прямоугольников на сгущающихся сетках, уточняются с помощью метода Эйткена. В рамках метода Эйткена получается как численное значение несобственного интеграла, так и погрешность. Решение уравнения Моргана проводится с помощью модифицированного метода деления отрезка пополам, адаптированного к тому, что несобственный интеграл в правой части уравнения известен с заданной точностью.  В работе построен метод приближенного решения уравнения Моргана с гарантированной точностью, проведена серия расчетов для различных фокусных расстояний, достигнутая точность приближенного решения .

---

-   Numerical solution of Morgan equation
-   Arrokho Ernandes Enoel
-   PhD student
-   Department of Computational Mathematics and Artificial Intelligence of RUDN University

The Morgan equation plays important role in the theory of gradient-index lenses, relating the variable refractive index and ray trajectories. This work examines the numerical solution of the Morgan equation for the design of a thin-film waveguide Luneberg lens with guaranteed accuracy, which is the focus of this work.  Solving Morgan equation requires a numerical calculation of the improper integral, which is calculated using the rectangle rule. The results obtained using the rectangle rule on progressively finer grids are refined using Aitken's delta-squared process. Aitken's method yields both the numerical value of the improper integral and the error. Morgan equation is solved using a modified bisection method, adapted to the fact that the improper integral on the right-hand side of the equation is known with a given accuracy.  In this work, a method for an approximate solution of the Morgan equation with guaranteed accuracy is developed, a series of calculations for various focal lengths is carried out, a guaranteed accuracy of solving Morgan equation does not exceed .


### <span class="org-todo todo TODO">TODO</span> <span class="section-num">1.7</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2026-11-19 Чт&gt;</span></span> Бельхеева Р.К.  - Термодинамическое уравнение состояния для описания поведения пористой смеси {#бельхеева-р-dot-к-dot-термодинамическое-уравнение-состояния-для-описания-поведения-пористой-смеси}


#### <span class="section-num">1.7.1</span> Докладчик {#докладчик}

-   Бельхеева Р.К.
    -   доцент
    -   кафедра математического моделирования и искусственного интеллекта РУДН


#### <span class="section-num">1.7.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/346/>
-   Термодинамическое уравнение состояния для описания поведения пористой смеси
-   Бельхеева Р.К.
    -   доцент
    -   кафедра математического моделирования и искусственного интеллекта РУДН

В работе представлено развитие предложенного автором метода построения уравнения состояния термодинамически равновесной пористой смеси нескольких конденсированных компонентов, основанного на гипотезе аддитивности объемов ее составляющих. Выполнены  численные расчеты ударно–волнового нагружения и изоэнтропической разгрузки сплошных и пористых смесей, содержащих два и три конденсированных компонента. Проведено сравнение расчетных и экспериментальных ударных адиабат и изоэнтроп разгрузки. Показано, что полученное уравнение смеси, параметры которого выражаются через соответствующие параметры и массовые концентрации составляющих, достаточно точно описывает поведение многокомпонентных сред при распространении в них ударных волн, волн разгрузки и волн двойного сжатия.

---

-   Thermodynamic equation of state for describing the behavior of a porous mixture
-   Belkheeva, R.K.
-   Associate Professor
-   Department of Computational Mathematics and Artificial Intelligence of RUDN University

This paper presents a development of the author's proposed method for constructing an equation of state for a thermodynamically equilibrium porous mixture of several condensed components, based on the hypothesis of additivity of the component volumes. Numerical calculations of shock-wave loading and isentropic unloading of solid and porous mixtures containing two and three condensed components are performed. A comparison of the calculated and experimental shock adiabats and unloading isentropes is conducted. It is shown that the resulting mixture equation, whose parameters are expressed in terms of the corresponding parameters and mass concentrations of the components, accurately describes the behavior of multicomponent media during the propagation of shock waves, unloading waves, and double compression waves.


### <span class="org-todo todo TODO">TODO</span> <span class="section-num">1.8</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2026-11-26 Чт&gt;</span></span> Кислицына М. Ю. - Математическая модель коррекции ошибки статистической классификации текстов методом n-грамм {#кислицына-м-dot-ю-dot-математическая-модель-коррекции-ошибки-статистической-классификации-текстов-методом-n-грамм}


#### <span class="section-num">1.8.1</span> Докладчик {#докладчик}

-   Кислицына Мария Юрьевна
    -   м.н.с.
    -   Институт прикладной математики им. М.В. Келдыша РАН


#### <span class="section-num">1.8.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/345/>
-   Численное решение уравнения Моргана
-   Кислицына Мария Юрьевна
    -   м.н.с.
    -   Институт прикладной математики им. М.В. Келдыша РАН

Доклад посвящён разработке и исследованию математической модели коррекции ошибок непараметрического распознавания текстов методом ближайшего эталона. Рассматриваемая задача приобретает особую актуальность в условиях большого числа классов, когда наряду с необходимостью повышения достоверности классификации возникает проблема распознавания объектов, не принадлежащих ни одному из известных классов. В связи с этим в работе предлагается подход, позволяющий оценивать надёжность результатов распознавания и корректировать ошибочные классификационные решения. Цель исследования состоит в построении математической модели, обеспечивающей такую коррекцию и выявление объектов открытого класса. Для теоретического обоснования и экспериментальной проверки модели рассматривается задача определения авторства художественных текстов на основе частотных распределений n-грамм.

В рамках исследования разработаны два непараметрических решающих правила, не требующих обучения на конкретной выборке, и сформулированы критерии оценки эффективности их применения в условиях закрытого и открытого классов. Предложенные методы реализованы в виде алгоритмов и программного комплекса, что позволило провести экспериментальное исследование на масштабном корпусе, включающем 8 287 авторов и 108 518 текстов общим объёмом около 34 млрд знаков. Результаты экспериментов подтвердили эффективность разработанной модели: её применение позволяет значительно снизить долю ошибочных ответов среди принятых решений. Полученные результаты имеют теоретическое значение для развития методов непараметрического распознавания и коррекции ошибок, а также могут быть использованы для повышения надёжности автоматической классификации текстовых данных.

---

-   A Mathematical Model for Correcting Errors in Statistical Text Classification Using n-Grams
-   Maria Kislitsyna
-   Junior Researcher
-   Keldysh Institute of Applied Mathematics, Russian Academy of Sciences

This paper is devoted to the development and investigation of a mathematical model for correcting errors in nonparametric text recognition using the nearest profile method. The problem is particularly relevant when the number of classes is large. For increasing classification accuracy, it becomes necessary to identify objects that do not belong to any of the known classes. Hence, the paper proposes an approach for assessing the reliability of recognition results and correcting erroneous classification decisions. The aim of the study is to construct a mathematical model that enables such corrections and the detection of objects belonging to an open-set class. For the theoretical justification and experimental validation of the model, the task of authorship attribution for literary texts is considered, based on the frequency distributions of character n-grams.

As part of the study, two nonparametric decision rules that do not require training on a specific sample were developed, and criteria were formulated for evaluating their effectiveness in closed-set and open-set settings. The proposed methods were implemented as algorithms and integrated into a software package, enabling an experimental study on a large-scale corpus comprising 8,287 authors and 108,518 texts, with a total volume of approximately 34 billion characters. The experimental results confirmed the effectiveness of the proposed model: its application substantially reduces the proportion of incorrect responses among accepted classification decisions. The findings are of theoretical significance for the development of nonparametric recognition and error-correction methods and may also be used to improve the reliability of automated text data classification.
