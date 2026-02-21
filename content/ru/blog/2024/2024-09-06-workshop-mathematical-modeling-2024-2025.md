---
title: "Семинар Математическое моделирование, 2024-2025"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-06T10:56:00+03:00
lastmod: 2025-06-05T15:57:00+03:00
tags: ["seedling", "rudn", "science-admin"]
categories: ["job", "science"]
draft: false
slug: "workshop-mathematical-modeling-2024-2025"
---

Заседания семинара Математическое моделирование, 2024-2025 учебный год.

<!--more-->

{{< toc >}}


## <span class="org-todo done DONE">DONE</span> <span class="section-num">1</span> Семинар Математическое моделирование, 2024-2 <code>[6/6]</code> {#семинар-математическое-моделирование-2024-2}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.1</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2024-09-18 Ср&gt; </span></span> Лисица Ю. Т. - О числах больших и малых (топологические поля чисел Конвея и их пополнения) {#лисица-ю-dot-т-dot-о-числах-больших-и-малых--топологические-поля-чисел-конвея-и-их-пополнения}


#### <span class="section-num">1.1.1</span> Докладчик {#докладчик}

-   Лисица Юрий Трофимович
-   доктор физико-математических наук
-   Институт Наследия, ведущий научный сотрудник отдела культурологии
-   Православный Свято-Тихоновский гуманитарный университет, профессор кафедры миссиологии Богословского факультета
-   <https://heritage-institute.ru/?employees=lisicza-yurij-trofimovich>


#### <span class="section-num">1.1.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/260/>
-   О числах больших и малых (топологические поля чисел Конвея и их пополнения)
-   Ю. Т. Лисица

Джон Конвей построил [1] числа, названные его именем, используя одновременно две известные в арифметики конструкции -- сечение Дедекинда (A,A') в области рациональных чисел и ординальные числа Мириманова-фон Неймана:

{}=ø=0, {ø}=1, {ø,{ø}}=2, {ø,{ø},{ø,{ø}}}=3,..., {0,1,2,3,...}=ω, {0,1,2,3,...,ω}= ω+1,...

Конвей строит свои числа по трансфинитной индукции ординальных чисел {0,1,2,3,...,α,...}, 0≤α&lt;Ω, и расслаивает их по «дням рождения»: 0-день, 1-день, 2-день, ..., α -день, ... .

Определение числа Конвея следующее: если L, R любые два множества чисел Конвея, такие что ни один элемент из L не ≥ каждого элемента из R, то существует единственное число Конвея такого вида: {L | R} и все числа имеют такую форму. Если x={L | R}, то типичный элемент их L обозначается через x<sup>L</sup>, а типичный элемент из R обозначается через x<sup>R</sup> и тогда число Конвея кратко записывается так: x={x<sup>L</sup> | x<sup>R</sup>}.

Мы говорим, что x≥y тогда и только тогда, когда ни для одного элемента x<sup>R</sup> нет неравенства x<sup>R</sup>≤y и ни для одного элемента x<sup>L</sup> нет неравенства x≤y<sup>L</sup>. Равенство чисел Конвея x=y тогда и только тогда, когда x≥y и y≥x. Строгие неравенства x&gt;y тогда и только тогда, когда (x≥y &amp; x≠y).

Определение суммы чисел x+y:

x+y={x<sup>L</sup>+y, x+y<sup>L</sup> | x<sup>R</sup>+y, x+y<sup>R</sup>}.

Определение обратного числа --x:

--x={--x<sup>R</sup> | --x<sup>L</sup>}.

Определение произведения чисел xy:

xy={x<sup>L</sup>y+xy<sup>L</sup>--x<sup>L</sup>y<sup>L</sup>, x<sup>R</sup>y+xy<sup>R</sup>--x<sup>R</sup>y<sup>R</sup> |
x<sup>L</sup>y+xy<sup>R</sup>--x<sup>L</sup>y<sup>R</sup>, x<sup>R</sup>y+xy<sup>L</sup>--x<sup>R</sup>y<sup>L</sup> }.

Для любого числа x не равного нулю Конвей дал корректное и нетривиальное определение обратного числа 1/x.

Таким образом все числа Конвея составляют вполне упорядоченное Поле **No**, но с областью определения не на множестве, а на Несобственном классе.

Конвей дает очень важное и единственное(!) определения возведение в любую степень числа ω, т. е. для любого x из **No** имеется единственное число y=ω<sup>x</sup>.

Главные результаты Конвея:

Теорема 1. Для любого многочлена Ax<sup>2n+1</sup>+Bx<sup>2n</sup>+...+Cx+D с коэффициентами A,B,...,C,D из No и натурального числа n=0,1,2,...  имеется корень x<sub>0</sub> в No.

Теорема 2. Для любого положительного числа Конвея x имеется корень n-й степени для любого натурального числа n≥2.

Следствие 1. Присоединяя к No мнимую единицу i, получим замкнутое алгебраическое Поле (Основная Теорема Алгебры для всех чисел Конвея).

Результаты в настоящей работе см. в [2]. Для всех порядковых чисел ξ=ω<sup>ω^μ</sup>, 0≤μ&lt;Ω, Строится подмножество O<sub>ξ</sub> -- всех числе Конвея, чей день рождения предшествует ξ-дню, которое после локализации в нуле является подполем Поля No и в нем вводится порядковая топология, а его пополнение является также подполем R<sub>ξ</sub> Поля No. Если μ=0, то поле R<sub>ω</sub> является одномерным полем действительных чисел; если 0&lt;μ&lt;Ω, то получаются нульмерные вполне упорядоченные подполя R<sub>ξ</sub> всех чисел Конвея, для которых верны Теоремы 1 и 2 и Следствие 1. Более того, в этих полях определяются классические функции математического анализа и доказывается, что для конечных чисел эти функции непрерывны, а для бесконечных чисел Конвея они разрывны в каждой точке. Определяются также показательные функции a<sup>x</sup> для любых конечных положительных чисел a≠1 и всех чисел Конвея a так и для некоторых положительных бесконечных чисел Конвея x. Рассматриваются соответствующие обратные функции -- логарифмы с этими основаниями. Это монотонные функции и они разрывны в каждой своей точке определения. При этом _конечное_ число Конвея x -- это такое число, для которого найдется такое натуральное число n, что --n&lt;x&lt;n. В противном случае число Конвея a называется _бесконечным_ числом. Мы здесь называем бесконечные числа x _большими_, а обратное к ним 1/x -- _малыми_.

Для больших и малых чисел возникают совершенно _новые_ явления: сколько раз не прибавляй малое число 1/x к себе, оно не выйдет за некоторый предел, который можно называть здесь условно «черной дырой». Например, малое число 1/ω&lt;1/n для любого натурального числа n. Но 1/ω &lt;2/ω&lt;3/ω&lt;...&lt; k/ω&lt;... &lt;1/n для любого натурального числа n. А 1/ω &lt;2/ω, 3/ω,..., k/ω,... &lt;1/√ω, 2/√ω, 3/√ω,... &lt;1/n для любого натурального числа n. И вообще, для любого ординала 0&lt;α&lt;Ω имеют место неравенства 1/ω &lt;2/ω, 3/ω,..., k/ω,... &lt;1/ω<sup>1/α</sup>&lt;2/ω<sup>1/α</sup>&lt;3/ω<sup>1/α</sup>&lt;k/ω<sup>1/α</sup>&lt;...&lt; 1/ω<sup>1/α+1</sup>&lt;2/ω<sup>1/α+1</sup>&lt;3/ω<sup>1/α+1</sup>&lt;k/ω<sup>1/α+1</sup>&lt;...&lt; 1/n для любого натурального числа n. То есть, даже постоянно увеличивающиеся малые числа взятые максимально в данном случае раз не может выйти в область конечных чисел {1/n}, 0&lt;n&lt; ω.

И таких непреодолимых «ям» в Поле чисел Конвея огромное количество, а именно, любая монотонно возрастающая или монотонно убывающая последовательность чисел Конвея является «ямой» для некоторого класса малых чисел.

_Действительные числа_ -- это конечные числа x, для которых

x={x--1, x--1/2, x--1/3, ... | x+1, x+1/2, x+1/3, ... }.

_Ординальные числа_ -- это числа α вида

α ={L |}.

Техника в работе [2] -- это определение трансфинитных последовательностей x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub> как отображений x:(0,ξ)→ O<sub>ξ</sub>.

Определение 1. Трансфинитная последовательность x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub> сходится к числу Конвея a из O<sub>ξ</sub>, если для любого числа ε&gt;0, ε из множества O<sub>ξ</sub>, найдется такой ординал α<sub>0</sub>, что для всех ординалов α<sub>0</sub>&lt;α&lt;ξ выполняется неравенство:

​|x<sub>α</sub>--a|&lt; ε.

Определение 2. Трансфинитная последовательность x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub> чисел Конвея из O<sub>ξ</sub> называется ξ-фундаментальной, если для любого числа ε&gt;0, ε из множества O<sub>ξ</sub>, найдется такой ординал α<sub>0</sub>, что для всех ординалов α<sub>0</sub>&lt;α, α'&lt;ξ выполняется неравенство:

​|x<sub>α</sub>--x<sub>α'</sub>|&lt; ε.

Определение 3. Две ξ-фундаментальные последовательности x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub> и y=(y<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub> называются _эквивалентными_, если для любого числа ε&gt;0, ε из множества O<sub>ξ</sub>, найдется такой ординал α<sub>0</sub>, что для всех ординалов α<sub>0</sub>&lt;α&lt;ξ выполняется неравенство:

​|x<sub>α</sub>--y<sub>α</sub>|&lt; ε.

Определение 4. Множество [x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub>] всех классов эквивалентных ξ-фундаметнальных последовательностей в множестве O<sub>ξ</sub> называется пополнением этого множества и обозначается через R<sub>ξ.</sub>

Теорема 3. Любая ξ-фундаментальные последовательности x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub> в R<sub>ξ</sub> сходится в R<sub>ξ.</sub>

Теорема 4. R<sub>ξ</sub> является подполем Поля No.

Теорема 5. Для любого многочлена Ax<sup>2n+1</sup>+Bx<sup>2n</sup>+...+Cx+D с коэффициентами A,B,...,C,D из R<sub>ξ</sub> и натурального числа n=0,1,2,...  имеется корень x<sub>0</sub> в R<sub>ξ</sub>.

Теорема 6. Для любого положительного числа Конвея x из R<sub>ξ</sub> имеется корень n-й степени x<sup>1/n</sup> для любого натурального числа n≥2, который принадлежит полю R<sub>ξ</sub>.

Следствие 2. Присоединяя к R<sub>ξ</sub> мнимую единицу i, получим замкнутое алгебраическое Поле (Основная Теорема Алгебры для всех чисел Конвея из поля R<sub>ξ</sub>).

Основные ссылки

1.  John H. Conway, On Numbers and Games, London Mathematical Society Monographs, No. 6, Academic Press, London-New-San Francisco, 1976.

2.  Ju. T. Lisica, On all numbers great and small (topological fiels of Conway's numbers and their completions) [Читай статью on all numbers great and small (topological fields of conway's numbers and their completions) на архив орг (arxivorg.ru)](https://arxivorg.ru/mathematics/aeromekhanika/20240520000000000001/)

---

-   On numbers large and small (Topological fields of Conway numbers and their completions)
-   Ju. T. Lisica
-   St. Tikhon’s Orthodox University of Humanities Department of Missiology
-   Doctor of Physical and Mathematical Sciences Professor

John Conway constructed [1] the numbers named after him using simultaneously two constructions known in arithmetic -- the Dedekind section (A,A') in the field of rational numbers and the Mirimanov-von Neumann ordinal numbers: {}=ø=0, {ø}=1, {ø,{ø}}=2, {ø,{ø},{ø,{ø}}}=3,..., {0,1,2,3,...}= ω, {0,1,2,3,...,ω}= ω+1,... Conway builds his numbers by transfinite induction of ordinal numbers {0,1,2,3,...,α,...}, 0≤α&lt;Ω, and stratifies them by "birthdays": born on day 0, born on day 1, born on day 2, ..., born on day α, ... .

The definition of the Conway number is as follows: if L, R are any two sets of Conway numbers, and no element of L is ≥ any member of R, then there is a Conway number {L | R} and all numbers are constructed in this way. If x={L | R} we write x<sup>L</sup> for the typical member of L, and x<sup>R</sup> for the typical member of R. For x itself we then write x={x<sup>L</sup> ​|x<sup>R</sup>}.

We say that x≥y iff no x<sup>R</sup>≤y and x≤ no y<sup>L</sup>. The equality of Conway numbers x=y iff x≥y and y≥x. Strict inequalities x&gt;y if and only if (x≥y &amp; x≠y).

The definition of the sum of the numbers x+y:

x+y={x<sup>L</sup>+y, x+y<sup>L</sup> | x<sup>R</sup>+y, x+y<sup>R</sup>}.

The definition of the inverse number is x:

--x={--x<sup>R</sup> | --x<sup>L</sup>}.

Definition of the product of the numbers xy:

xy={x<sup>L</sup>y+xy<sup>L</sup>--x<sup>L</sup>y<sup>L</sup>, x<sup>R</sup>y+xy<sup>R</sup>--x<sup>R</sup>y<sup>R</sup> |
x<sup>L</sup>y+xy<sup>R</sup>--x<sup>L</sup>y<sup>R</sup>, x<sup>R</sup>y+xy<sup>L</sup>--x<sup>R</sup>y<sup>L</sup> }.

For any number x not equal to zero, Conway gave a correct and nontrivial definition of the inverse number 1/x. Thus, all Conway numbers make up a completely ordered Field **No**, but with the domain of definition not on the set, but on a Proper class. Conway gives a very important and unique(!) definition of the exponent of the number ω, i.e. for any x of **No** there is a unique number y=ωx.

Conway's main results:

Theorem 1. For any polynomial Ax<sup>2n+1</sup>+Bx<sup>2n</sup>+...+Cx+D with coefficients A, B, ..., C, D of **No** and a natural number n=0,1,2,...  there is a root x<sub>0</sub> in **No**.

Theorem 2. For any positive Conway number x, there is an n-th degree root for any natural number n≥2.

Corollary 1. By attaching an imaginary unit **i** to **No**, we obtain a closed algebraic Field (the basic Theorem of Algebra for all Conway numbers).

For the results in this paper, see [2]. For all ordinal numbers ξ=ω<sup>ω^μ</sup>, 0≤μ&lt;Ω, a subset O<sub>ξ</sub> of all Conway numbers born before day ξ is constructed, which, after localization at zero, is a subfield of the Field **No** and an ordinal topology is introduced on it, and its completion **R<sub>ξ</sub> is also a subfield of the Field \*No**. If μ=0, then the field **R<sub>ω</sub> is a one-dimensional field of real numbers \*R**; if 0&lt;μ&lt;Ω, then zero-dimensional completely ordered subfields R<sub>ξ</sub> of all Conway numbers are obtained, for which Theorems 1 and 2 and Corollary 1 are true. Moreover, classical mathematical analysis functions are determined in these fields and it is proved that for _finite_ These functions are continuous, and for _infinite_ Conway numbers they are discontinuous at every point. The exponential functions a<sup>x</sup> are also defined for any finite positive numbers a≠1 and as well as for all Conway numbers a but for some positive infinite Conway numbers x. The corresponding inverse logarithm functions with these bases are considered. These are monotone functions and they are discontinuous at each of their definition points. In this case, a _finite_ Conway number x is a number for which there is such a natural number n that --n&lt;x&lt;n.  Otherwise, the Conway number a is called an _infinite_ number. Here we call the infinite numbers x _large_, and the inverse of them 1/x -- _small_. For large and small numbers, completely new phenomena arise: no matter how many times you add a small number 1/x to itself, it will not go beyond a certain limit, which can be conditionally called a "black hole" here. For example, a small number 1/ω&lt;1/n for any natural number n. But 1/ω &lt;2/ω&lt;3/ω&lt;...&lt; k/ω&lt;... &lt;1/n for any natural number n. And 1/ω &lt;2/ω, 3/ω,..., k/ω,... &lt;1/√ω, 2/√ω, 3/√ω,... &lt;1/n for any natural number n. And in general, for any ordinal 0&lt;α&lt;Ω there are inequalities 1/ω &lt;2/ω, 3/ω,..., k/ω,... &lt;1/ω<sup>1/α</sup>&lt;2/ω<sup>1/α</sup>&lt;3/ω<sup>1/α</sup>&lt;k/ω<sup>1/α</sup>&lt;...&lt; 1/ω<sup>1/α+1</sup>&lt;2/ω<sup>1/α+1</sup>&lt;3/ω<sup>1/α+1</sup>&lt;k/ω<sup>1/α+1</sup>&lt;...&lt; 1/n for any natural number n.

That is, even constantly increasing small numbers taken as many times as possible in this case cannot reach the range of finite numbers {1/n}, 0&lt;n&lt; ω.

And there are a huge number of such insurmountable "pits" in the Field of Conway numbers, namely, any monotonously increasing or monotonously decreasing sequence of Conway numbers is a "pit" for some class of small numbers.

The _real numbers_ are the finite numbers x for which x={x--1, x--1/2, x--1/3, ... | x+1, x+1/2, x+1/3, ... }.

The _ordinal numbers_ are α numbers of the form α ={L |}.

The technique in [2] is the definition of transfinite sequences x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub> as maps of x:(0,ξ)→ O<sub>ξ</sub>.

Definition 1. The transfinite sequence x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub> converges to the Conway number a of O<sub>ξ</sub> if for any number ε&gt;0, ε from the set O<sub>ξ</sub>, there is such an ordinal α<sub>0</sub> that for all ordinals α<sub>0</sub>&lt;α&lt;ξ the inequality holds: |x<sub>α</sub>--a|&lt; ε.

Definition 2. A transfinite sequence x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub> of Conway numbers from O<sub>ξ</sub> is called ξ-fundamental if for any number ε&gt;0, ε from the set O<sub>ξ</sub>, there is such an ordinal α<sub>0</sub> that for all ordinals α<sub>0</sub>&lt;α, α'&lt;ξ the inequality holds: |x<sub>α</sub>--x<sub>α'</sub>|&lt; ε.

Definition 3. Two ξ-fundamental sequences x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub> and y=(y<sub>a</sub>)<sub>0&lt;α&lt;ξ</sub> are called _equivalent_ if for any number ε&gt;0, ε from the set O<sub>ξ</sub>, there is such an ordinal α<sub>0</sub> that for all ordinals α<sub>0</sub>&lt;α&lt;ξ is satisfied inequality: |x<sub>α</sub>--y<sub>α</sub>|&lt; ε.

Definition 4. The set [x=(x<sub>α</sub>)<sub>0&lt;α&lt;ξ</sub>] of all classes of equivalent ξ-fundamental sequences in the set O<sub>ξ</sub> is called a _completion_ of this set and is denoted by R<sub>ξ</sub>.

Theorem 3. Any ξ-fundamental sequence x=(x<sub>α</sub>)0&lt;α&lt;ξ in R<sub>ξ</sub> converges in R<sub>ξ</sub>.

Theorem 4. R<sub>ξ</sub> is a subfield of Field No.

Theorem 5. For any polynomial Ax<sup>2n+1</sup>+Bx<sup>2n</sup>+...+Cx+D with coefficients A, B, ..., C, D of R<sub>ξ</sub> and a natural number n=0,1,2,...  there is a root x<sub>0</sub> in R<sub>ξ</sub>.

Theorem 6. For any positive Conway number x of R<sub>ξ</sub>, there is a root of the n-th degree x1/n for any natural number n≥2, which belongs to the field R<sub>ξ</sub>.

Corollary 2. By attaching an imaginary unit i to R<sub>ξ</sub>, we obtain a closed algebraic Field (the basic Theorem of Algebra for all Conway numbers from the field R<sub>ξ</sub>).

The main references

1.  John H. Conway, On Numbers and Games, London Mathematical Society Monographs, No. 6, Academic Press, London-New-San Francisco, 1976.

2.  Ju. T. Lisica, On all numbers great and small (topological fiels of Conway's numbers and their completions) [Читай статью on all numbers great and small (topological fields of conway's numbers and their completions) на архив орг (arxivorg.ru)](https://arxivorg.ru/mathematics/aeromekhanika/20240520000000000001/)


#### <span class="section-num">1.1.3</span> Видео {#видео}

{{< tabs "Лисица Ю. Т. - О числах больших и малых" >}}
{{< tab "RuTube" >}}

{{< rutube e9eef2a7d551fee5fda1a3f204c45f4b >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube 4ilRtoJ-vuY >}}

{{< /tab >}}
{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.2</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2024-10-10 Чт&gt; </span></span> Блинков Ю. А. - Представление PyGinv. Установка. Полиномиальный случай {#блинков-ю-dot-а-dot-представление-pyginv-dot-установка-dot-полиномиальный-случай}


#### <span class="section-num">1.2.1</span> Докладчик {#докладчик}

-   Блинков Ю.А.
-   доктор физико-математических наук
-   зав. каф. СГУ


#### <span class="section-num">1.2.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/263/>
-   Представление PyGinv. Установка. Полиномиальный случай
-   Блинков Ю.А.
-   д.ф.м.-н., зав. каф. СГУ
-   <https://github.com/blinkovua/GInv/tree/master/pyginv>

PyGInv представляет собой «легковесную» версию GIinv (сокращение от Gröbner INVolutive), библиотеки на C++ разработаную для исследования и решения систем алгебраических, дифференциальных и разностных уравнений полиномиального типа. Написана на «чистом» Python и использует систему компьютерной алгебры SymPy для работы с параметрами. Полностью платформ-независимая библиотека и удобная для использования в учебном процессе.
В полиномиальном случае в докладе будет рассмотрена установка, работа с мономами, полиномами и модулями. Построение дерева Janet, его визуализация и использование для программирования различных инволюционных делений. Вычисление размерностного полинома Гильберта, построение факторкольца и матричное представление элементов фактора полиномиального кольца по нульмерному идеалу.

---

-   Presentation of PyGInv. Installation. Polynomial case
-   Blinkov Yu.A., Doctor of Physics and Mathematics
-   Head. department SSU
-   <https://github.com/blinkovua/GInv/tree/master/pyginv>

PyGInv is a “lightweight” version of GIinv (an abbreviation for Gröbner INVolutive), a C++ library developed to investigate and solve systems of algebraic, differential, and difference equations of polynomial type. It was written in “pure” Python and uses the computer algebra system SymPy to work with parameters. This fully platform-independent library is convenient for use in educational process. In the polynomial case, the report will consider installation, working with monomials, polynomials, and modules. Construction of Janet tree, its visualization, and usage for programming various involutory divisions. Calculating Hilbert dimension polynomial, constructing factor ring, and matrix representation of elements of factor polynomial ring over zero-dimensional ideal.


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.3</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2024-09-18 Ср&gt; </span></span> Кулябов Д. С. - Релятивистские операции на основе модели Кэли--Кляйна {#кулябов-д-dot-с-dot-релятивистские-операции-на-основе-модели-кэли-кляйна}


#### <span class="section-num">1.3.1</span> Докладчик {#докладчик}

-   Кулябов Дмитрий Сергеевич
-   доктор физико-математических наук
-   кафедра теории вероятностей и кибербезопасности РУДН


#### <span class="section-num">1.3.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/268/>
-   Релятивистские операции на основе модели Кэли--Кляйна
-   Кулябов Д. С.
-   доктор физико-математических наук
-   Кафедра теории вероятностей и кибербезопасности РУДН

Рассматриваются формализмы, порождённые моделью Кэли--Кляйна. Приводятся примеры их применения к описанию операций в пространстве Минковского.

---

-   Relativistic operations based on the Cayley--Klein model
-   Dmitry S. Kulyabov
-   Doctor of Sciences in Physics and Mathematics, Professor
-   Department of Probability Theory and Cybersecurity, RUDN University

Formalisms generated by the Cayley-Klein model are considered. Examples of their application to the generation of operations in Minkowski space are given.ф


#### <span class="section-num">1.3.3</span> Видео {#видео}

{{< tabs "Кулябов Д. С. - Релятивистские операции на основе модели Кэли--Кляйна" >}}
{{< tab "RuTube" >}}

{{< rutube 91c2525ad4cc13493e7f305954abe935 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube 9s5QRN4E6bQ >}}

{{< /tab >}}
{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.4</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2024-11-21 Чт&gt; </span></span> Цирулев А. Н. - Вычисление экспонент от операторов с помощью интеграла Данфорда-Коши {#цирулев-а-dot-н-dot-вычисление-экспонент-от-операторов-с-помощью-интеграла-данфорда-коши}


#### <span class="section-num">1.4.1</span> Докладчик {#докладчик}

-   Цирулев А.Н.
-   доктор физико-математических наук
-   профессор кафедры общей математики и математической физики Тверской государственный университет


#### <span class="section-num">1.4.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/267/>
-   Вычисление экспонент от операторов с помощью интеграла Данфорда-Коши
-   Цирулев А.Н.
-   д.ф.м.-н., профессор кафедры общей математики и математической физики, Тверской государственный университет

Предложен новый алгоритм для вычисления экспонент операторов в базисе Паули. Алгоритм основан на представлении операторной экспоненты интегралом Данфорда-Коши и применим для гамильтонианов, разреженных в базисе Паули. Практическая эффективность алгоритма демонстрируется двумя иллюстративными примерами.

---

-   Computation of operator exponentials using Danford-Cauchy integral
-   Alexander Tsirulev
-   Professor of Department of General Mathematics and Mathematical Physics, Tver State University, Tver, Russia

A new algorithm for classical computing operator exponentials in the Pauli basis is proposed. The algorithm is based on the representation of the operator exponential by the Dunford-Cauchy integral and is suitable for Hamiltonians that sparse in the Pauli basis. The practical efficiency of the algorithm is demonstrated by two illustrative examples.


#### <span class="section-num">1.4.3</span> Видео {#видео}

{{< tabs "Цирулев А.Н. - Вычисление экспонент от операторов с помощью интеграла Данфорда-Коши" >}}
{{< tab "RuTube" >}}

{{< rutube ab56fa97a72c38f5c9a18c1bd68d0629 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube QIzBe_0qtuY >}}

{{< /tab >}}
{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.5</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2024-12-11 Ср&gt; </span></span> Кадров В. М. - Изучение дискретных многообразий на примере решения уравнений вращения твердого тела в случае Ковалевской {#кадров-в-dot-м-dot-изучение-дискретных-многообразий-на-примере-решения-уравнений-вращения-твердого-тела-в-случае-ковалевской}


#### <span class="section-num">1.5.1</span> Докладчик {#докладчик}

-   Кадров Виктор Максимович
-   студент 3 курса бакалавриата
-   кафедра Математического моделирования и искусственного интеллекта РУДН


#### <span class="section-num">1.5.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/271/>
-   Изучение дискретных многообразий на примере решения уравнений вращения твердого тела в случае Ковалевской
-   Кадров Виктор Максимович
-   студент 3 курса бакалавриата
-   кафедра Математического моделирования и искусственного интеллекта РУДН

В работе рассматриваются особенности и форма многообразий, которые получаются при решении уравнений вращения твердого тела в случае Ковалевской с использованием обратимой разностной схемы. Для определения количественных различий таких многообразий был использован метод расчета корреляционной размерности. В ходе исследования была выявлена зависимость качественной структуры решения от шага по времени и малых колебаний параметров системы.

---

-   The study of discrete manifolds through the example of solving the equations of rotation of a rigid body in the Kovalevskaya case
-   Viktor Maksimovich Kadrov
-   3rd year undergraduate student
-   Department of Mathematical Modeling and Artificial Intelligence, RUDN University

This paper examines the characteristics and shapes of manifolds obtained by solving the rotation equations of a rigid body in the Kovalevskaya case using a reversible finite difference method. To quantify the differences between these manifolds, we employed the method of correlation dimension calculation. The investigation revealed a dependence of the qualitative nature of the solution on the time step and minor fluctuations in system parameters.


#### <span class="section-num">1.5.3</span> Видео {#видео}

{{< tabs "Кадров В. М. - Изучение дискретных многообразий на примере решения уравнений вращения твердого тела в случае Ковалевской" >}}
{{< tab "RuTube" >}}

{{< rutube 2ed8ca8f44bad68f879964ff5d0e5654 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube lGz-x5ycKdc >}}

{{< /tab >}}
{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">1.6</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2024-12-12 Чт&gt; </span></span> Блинков Ю. А. - PyGinv. Случай дифференциальных уравнений {#блинков-ю-dot-а-dot-pyginv-dot-случай-дифференциальных-уравнений}


#### <span class="section-num">1.6.1</span> Докладчик {#докладчик}

-   Блинков Ю.А.
-   доктор физико-математических наук
-   зав. каф. СГУ


#### <span class="section-num">1.6.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/270/>
-   PyGinv. Случай дифференциальных уравнений
-   Блинков Ю. А.
-   д.ф.м.-н., зав. каф. СГУ
-   <https://github.com/blinkovua/GInv/tree/master/pyginv>

В докладе рассматривается случай отыскания решений линейных дифференциальных уравнений с переменными коэффициентами, представленными в виде полиномов. На основе построения инволюционного базиса (расширенного базиса Грёбнера) вычисляется полином Гильберта, что позволяет точно определить пространство решений. А в ряде случаев знание базиса Грёбнера позволяет построить точные решения.

Также рассматривается вычисление симметрий для нелинейных дифференциальных уравнений полиномиального типа. Уравнения симметрии и их решения строятся исключительно на использовании базисов Грёбнера, что позволяет практически полностью автоматизировать вычислительный процесс.

---

-   PyGinv. Case of Differential Equations
-   Blinkov, Yu. A.
-   Doctor of Physics and Mathematics
-   Head. department SSU
-   <https://github.com/blinkovua/GInv/tree/master/pyginv>

The report considers the case of finding solutions to linear differential equations with variable coefficients presented as polynomials. Based on the construction of an involutionary basis (extended Gröbner basis), the Hilbert polynomial is calculated, which allows us to accurately determine the solution space. And in some cases, knowledge of the Gröbner basis allows us to construct exact solutions.

The calculation of symmetries for nonlinear differential equations of polynomial type is also considered. Symmetry equations and their solutions are constructed exclusively using Gröbner bases, which allows us to almost completely automate the computational process.


#### <span class="section-num">1.6.3</span> Видео {#видео}

{{< tabs "Блинков Ю. А. - PyGinv. Случай дифференциальных уравнений" >}}
{{< tab "RuTube" >}}

{{< rutube 2841bae6e0a3d3dc8b0a3cf27497fcbb >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube pQ-nel9miyM >}}

{{< /tab >}}
{{< /tabs >}}


## <span class="org-todo done DONE">DONE</span> <span class="section-num">2</span> Семинар Математическое моделирование, 2025-1 <code>[8/8]</code> {#семинар-математическое-моделирование-2025-1}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">2.1</span> <span class="timestamp-wrapper"><span class="timestamp">[2025-01-30 Чт] </span></span> Блинков Ю. А. - PyGInv. Генерация и исследование разностных схем {#блинков-ю-dot-а-dot-pyginv-dot-генерация-и-исследование-разностных-схем}


#### <span class="section-num">2.1.1</span> Докладчик {#докладчик}

-   Блинков Ю.А.
-   доктор физико-математических наук
-   зав. каф. СГУ


#### <span class="section-num">2.1.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/275/>
-   PyGInv. Генерация и исследование разностных схем
-   Блинков Ю. А.
-   д.ф.м.-н., зав. каф. СГУ
-   <https://github.com/blinkovua/GInv/tree/master/pyginv>

Современные системы компьютерной алгебры обладают встроенными функциями для построения базисов Грёбнера для систем полиномиальных уравнений. Однако в случае дифференциальных уравнений и разностных схем реализация алгоритмов построения таких базисов обычно отсутствует. В докладе будут представлены алгоритмы генерации известных разностных схем и алгоритмы построения консервативных разностных схем. Один из алгоритмических подходов к исследованию разностных схем заключается в построении первого дифференциального приближения. Для этого будут использоваться базисы Грёбнера для работы с формальными рядами Тейлора. На многочисленных примерах будет показано применение первого дифференциального приближения для исследования разностных схем на точных решениях исходной системы дифференциальных уравнений и численных решений с оценкой локальной и глобальной погрешностей.

---

-   PyGInv. Generation and investigation of difference schemes
-   Blinkov, Yu. A.
-   Doctor of Physics and Mathematics
-   Head. department SSU
-   <https://github.com/blinkovua/GInv/tree/master/pyginv>

Modern computer algebra systems have built-in functions for constructing Gröbner bases for systems of polynomial equations. However, in the case of differential equations and difference schemes, the implementation of algorithms for building such bases is usually absent. The presentation will cover algorithms for generating well-known difference schemes and algorithms for constructing conservative difference schemes. One algorithmic approach to investigating difference schemes involves constructing the first differential approximation. For this purpose, Gröbner bases will be used to work with formal Taylor series. Numerous examples will demonstrate the application of the first differential approximation to study difference schemes on exact solutions of the original system of differential equations and numerical solutions with estimates of local and global errors.


#### <span class="section-num">2.1.3</span> Видео {#видео}

{{< tabs "Блинков Ю. А. - PyGInv. Генерация и исследование разностных схем" >}}
{{< tab "RuTube" >}}

{{< rutube 8e39e354a82f6e990f4cf9a985a88665 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube lWr4kpYUFHA >}}

{{< /tab >}}
{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">2.2</span> <span class="timestamp-wrapper"><span class="timestamp">[2025-02-20 Чт] </span></span> Смирнов-Мальцев Е. Д., Дужин В. С. - Некоторые геометрические свойства диаграмм Юнга максимальных размерностей {#смирнов-мальцев-е-dot-д-dot-дужин-в-dot-с-dot-некоторые-геометрические-свойства-диаграмм-юнга-максимальных-размерностей}


#### <span class="section-num">2.2.1</span> Докладчик {#докладчик}

-   Егор Д. Смирнов-Мальцев
    -   студент 4 курса бакалавриата
    -   кафедра Математического моделирования и искусственного интеллекта РУДН


#### <span class="section-num">2.2.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/278/>
-   Некоторые геометрические свойства диаграмм Юнга максимальных размерностей
-   Егор Д. Смирнов-Мальцев
    -   студент 4 курса бакалавриата
    -   кафедра Математического моделирования и искусственного интеллекта РУДН
-   Дужин Василий Сергеевич
    -   кандидат физ-мат наук
    -   ассистент кафедры алгоритмической математики факультета компьютерных технологий и информатики СПбГЭТУ «ЛЭТИ»

Работа посвящена задаче поиска диаграмм Юнга с максимальными размерностями, т.е. обладающих наибольшим количеством таблиц Юнга среди всех диаграмм из заданного количества клеток. Предложен алгоритм, позволяющий преобразовать исходную диаграмму, отличающуюся от симметричной не более чем на одну клетку в каждой строке и каждом столбце, в другую диаграмму того же размера, но с большей или равной размерностью. Сформулирована гипотеза, обобщающая указанный выше факт на случай произвольных диаграмм Юнга. Это геометрическое свойство использовано при создании алгоритма поиска диаграмм Юнга, который позволил получить новые, неизвестные ранее диаграммы Юнга с большими и максимальными размерностями.

---

-   Some geometric properties of Young diagrams of maximum dimensions
    -   Egor Smirnov-Maltsev
    -   4th year undergraduate student
    -   Department of Mathematical Modeling and Artificial Intelligence, RUDN University
-   Vasilii S. Duzhin
    -   Candidate of Physical and Mathematical Sciences
    -   Assistant of the Department of Algorithmic Mathematics of the Faculty of Computer Technology and Informatics of St. Petersburg Electrotechnical University "LETI"

We study the problem of finding Young diagrams of maximum dimensions, i.e., those that have the largest number of Young tableaux among all diagrams with a given number of boxes.  We consider a diagram that differs from the symmetrical one by no more than one box in each row and each column. We propose an algorithm that transforms such a diagram into another one of the same size but with a greater or equal dimension.  We formulate a conjecture that generalizes this result to arbitrary Young diagrams. This geometric property is used in an algorithm for finding Young diagrams with maximum dimensions. Using this algorithm, we obtained new, previously unknown Young diagrams with large and maximum numbers of Young tableaux.


#### <span class="section-num">2.2.3</span> Видео {#видео}

{{< tabs "Смирнов-Мальцев Е. Д., Дужин В. С. - Некоторые геометрические свойства диаграмм Юнга максимальных размерностей" >}}
{{< tab "RuTube" >}}

{{< rutube 3c7bbd6cba8dfad65b77bd73f6e88633 >}}

{{< /tab >}}
{{< tab "Платформа" >}}

{{< plvideo 0p3G2qaQzjtM >}}

{{< /tab >}}
{{< tab "VKvideo" >}}

{{< vkvideo 606414976 456239706 2 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube izkyPTjtukQ >}}

{{< /tab >}}
{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">2.3</span> <span class="timestamp-wrapper"><span class="timestamp">[2025-02-26 Ср] </span></span> Васильева И. И. - Построение, стохастизация и компьютерное исследование многомерных миграционно-популяционных моделей с конкуренцией {#васильева-и-dot-и-dot-построение-стохастизация-и-компьютерное-исследование-многомерных-миграционно-популяционных-моделей-с-конкуренцией}


#### <span class="section-num">2.3.1</span> Докладчик {#докладчик}

-   Васильева Ирина Ивановна
    -   Аспирант, старший преподаватель кафедры математического моделирования, компьютерных технологий и информационной безопасности, Елецкий государственный университет им. И.А. Бунина


#### <span class="section-num">2.3.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/282/>
-   Построение, стохастизация и компьютерное исследование многомерных миграционно-популяционных моделей с конкуренцией
-   Васильева Ирина Ивановна
    -   Аспирант, старший преподаватель кафедры математического моделирования, компьютерных технологий и информационной безопасности, Елецкий государственный университет им. И.А. Бунина

При изучении детерминированных и стохастических популяционных моделей высокой размерности важной задачей является формализация процессов с учетом новых факторов, возникающих вследствие взаимодействия между видами, а также разработка вычислительных подходов к исследованию таких систем. В докладе рассматриваются многомерные миграционно-популяционные модели с учетом конкуренции видов. На основе дифференциальной эволюции и других метаэвристических алгоритмов глобальной оптимизации решена задача параметрической идентификации с учетом критериев оптимальности, обеспечивающих совместное существование популяций в условиях межвидовой конкуренции в пределах основного ареала обитания, а также существование вида в ареале миграции. Проведены серии численных экспериментов, исследованы траектории динамики системы, получены проекции фазовых портретов на плоскости и в неотрицательном ортанте пространства. Выявлены характерные особенности и проведен сравнительный анализ результатов для различных модификаций рассматриваемых моделей. Получены условия существования положительных состояний равновесия. Исследована устойчивость в смысле Ляпунова. Выполнена стохастизация, проведен сравнительный анализ детерминированного и стохастического случаев. Разработаны алгоритмы и создан программный комплекс для исследования миграционно-популяционных моделей. Результаты исследования могут найти применение в задачах прогнозирования динамики развития экосистем и социально-экономических структур, а также для моделирования физико-химических процессов.

---

-   Construction, stochastization, and computer research of multidimensional migration and population models with competition
-   Vasilyeva, Irina Ivanovna
    -   Postgraduate, Senior Lecturer of the Postgraduate Department of Mathematical Modeling, Computer Technologies and Information Security, Bunin Yelets State University

When studying deterministic and stochastic population models of high dimension, an important problem is to formalize processes taking into account new factors arising from interactions between species, as well as to develop computational approaches to the study of such systems. The report examines multidimensional migration and population models taking into account the competition of species. Based on differential evolution and other metaheuristic algorithms of global optimization, the problem of parametric identification is solved taking into account the criteria of optimality ensuring the co-existence of populations in conditions of interspecific competition within the main habitat, as well as the existence of a species in the area of migration. A series of numerical experiments is carried out, the trajectories of the system dynamics are investigated, and projections of phase portraits on the plane and in the non-negative orthant of space are obtained. The characteristic features are revealed and a comparative analysis of the results for various modifications of the models under consideration is carried out. The conditions for the existence of positive equilibrium states are obtained. Stability in the Lyapunov sense is investigated. Stochastization is performed, a comparative analysis of deterministic and stochastic cases is carried out. Algorithms are developed and a software package is created for the study of migration and population models. The results of the research can be used in forecasting the dynamics of ecosystem development and socio-economic structures, as well as for modeling physics and chemical processes.


#### <span class="section-num">2.3.3</span> Видео {#видео}

{{< tabs "Васильева И. И. - Построение, стохастизация и компьютерное исследование многомерных миграционно-популяционных моделей с конкуренцией" >}}
{{< tab "RuTube" >}}

{{< rutube 8f6a69c3d7ba4b1187d9d42ae1540db6 >}}

{{< /tab >}}
{{< tab "Платформа" >}}

{{< plvideo 8jCvgMjLL7Ax >}}

{{< /tab >}}
{{< tab "VKvideo" >}}

{{< vkvideo 606414976 456239710 2 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube vuMvSbeF_BQ >}}

{{< /tab >}}
{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">2.4</span> <span class="timestamp-wrapper"><span class="timestamp">[2025-03-20 Чт] </span></span> Степанцов М. Е. - Метод замены дифференциальных уравнений клеточными автоматами в задачах социально-экономической динамики {#степанцов-м-dot-е-dot-метод-замены-дифференциальных-уравнений-клеточными-автоматами-в-задачах-социально-экономической-динамики}


#### <span class="section-num">2.4.1</span> Докладчик {#докладчик}

-   Степанцов Михаил Евгеньевич
    -   старший научный сотрудник, к.ф.-м.н, доцент
    -   Институт прикладной математики им. М.В. Келдыша РАН


#### <span class="section-num">2.4.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/285/>
-   Метод замены дифференциальных уравнений клеточными автоматами в задачах социально-экономической динамики
-   Степанцов Михаил Евгеньевич
    -   старший научный сотрудник, к.ф.-м.н, доцент
    -   Институт прикладной математики им. М.В. Келдыша РАН

Доклад посвящен представлению диссертации на соискание учёной степени доктора наук, посвящённой разработке и использованию метода замены дифференциальных уравнений клеточными автоматами в определённом классе задач.
В задачах социально-экономической динамики моделируемая реальность существенно дискретна, поэтому моделирование таких процессов уместно осуществлять при помощи дискретных моделей, в частности –клеточных автоматов. В то же время при моделировании социально-экономических процессов уже широко используются созданные по аналогии с физикой модели на основе дифференциальных уравнений. В докладе предложен общий метод замены дифференциальных уравнений клеточными автоматами в моделях, сводимых к задачам Коши для обыкновенных дифференциальных уравнений, что позволяет расширить область применимости исходных моделей и повысить эффективность вычислений. Изложена теорема о сходимости решения, полученного при помощи клеточного автомата, к решению исходной задачи и следствие из неё. Представлена апробация этого метода на шести математических моделях социально-экономической динамики и решения соответствующих прикладных задач, которые было затруднительно либо вообще невозможно получить аналитически или численно на основе исходных непрерывных моделей.

---

-   Method of replacing differential equations with cellular automata in problems of socio-economic dynamics
-   Stepantsov Mikhail Evgenievich
    -   Senior Researcher, PhD, Associate Professor
    -   Keldysh Institute of Applied Mathematics, Russian Academy of Sciences

The report is the presentation of a doctoral thesis considering the method of replacing differential equations with cellular automata in a certain class of problems.
When we study socio-economic dynamics, the modeled reality is essentially discrete, therefore such processes should be described using discrete models, in particular, cellular automata. On the other hand a lot of socio-economic processes are widely modeled basing on differential equations by analogy with physical processes. The report proposes a general method for replacing differential equations with cellular automata in models that can be reduced to Cauchy problems for ordinary differential equations. This allows expanding the applicability of the original models and increasing the efficiency of calculations. A theorem on the convergence of a solution obtained with a cellular automaton to a solution to the original problem is presented as well as its corollary. Report also includes presentation of approbation of this method on six mathematical models of socio-economic dynamics. Solutions are obtained to corresponding applied problems that were difficult or even impossible to obtain analytically or numerically while using classical approach.


#### <span class="section-num">2.4.3</span> Видео {#видео}

{{< tabs "Степанцов М. Е. - Метод замены дифференциальных уравнений клеточными автоматами в задачах социально-экономической динамики" >}}
{{< tab "RuTube" >}}

{{< rutube 0bc3e9764a7da962e37a4e1a6ddae361 >}}

{{< /tab >}}
{{< tab "Платформа" >}}

{{< plvideo PPAyw6cLiua2 >}}

{{< /tab >}}
{{< tab "VKvideo" >}}

{{< vkvideo 606414976 456239715 2 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube X32YD-o0k4o >}}

{{< /tab >}}
{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">2.5</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2025-03-31 Пн&gt; </span></span> Ловецкий К. П. - История развития вычислительной техники {#ловецкий-к-dot-п-dot-история-развития-вычислительной-техники}


#### <span class="section-num">2.5.1</span> Докладчик {#докладчик}

-   Ловецкий Константин Петрович
    -   доцент, к.ф.-м.н, доцент
    -   кафедра математического моделирования и искусственного интеллекта, РУДН


#### <span class="section-num">2.5.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/287/>
-   История развития вычислительной техники
-   Ловецкий Константин Петрович
    -   доцент, к.ф.-м.н, доцент
    -   кафедра математического моделирования и искусственного интеллекта, РУДН

Даётся очерк развития вычислительной техники с древних времён до появления компьютерных клубов.  Рассказ об истории развития вычислительной техники. Об этапах трансформации счётных палочек, абака - простейших устройств, облегчающих элементарные вычисления - к современным компьютерам, которые позволяют не только решать сложные математические и физические задачи, но и позволяют организовать взаимодействие людей на основе информационных технологий. Речь пойдет и о первом детском компьютерном клубе на Рождественском бульваре, созданным братьями Степаном и Георгием Пачиковыми и Антоном Чижовым при участии и поддержке многих энтузиастов.  И о детском летнем компьютерном центре Института Программных Систем РАН, основанным родоначальником компьютерного образования в России Академиком Е. П. Велиховым. И о первых успехах отечественных программистов в области распознавания рукописных текстов (наладонник «Ньютон» - фирма Параграф), создания игр («Тетрис» - Пажитнов), русификатор операционной системы IBM PC (Чижов).

---

-   History of development of computer technology
-   K. P. Lovetskiy
    -   Docent, PhD, Associate Professor
    -   Department of Mathematical Modeling and Artificial Intelligence, RUDN University

A story about the history of computer technology development. About the stages of transformation of counting sticks, abacus - the simplest devices that facilitate elementary calculations - to modern computers that allow not only to solve complex mathematical and physical problems, but also to organize interaction between people based on information technology. We will also talk about the first children's computer club on Rozhdestvensky Boulevard, created by brothers Stepan and Georgy Pachikov and Anton Chizhov with the participation and support of many enthusiasts. And about the children's summer computer center of the Institute of Program Systems of the Russian Academy of Sciences, founded by the founder of computer education in Russia, Academician E. P. Velikhov. And about the first successes of domestic programmers in the field of handwriting recognition (the Newton palmtop - Paragraph company), game creation (Tetris - Pajitnov), the Russifier of the IBM PC operating system (Chizhov).


### <span class="org-todo done DONE">DONE</span> <span class="section-num">2.6</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2025-04-17 Чт&gt; </span></span> Геворкян М. Н. - Применение алгебры винтов и бикватернионов для вычисления конечного винтового движения точек, прямых и плоскостей {#геворкян-м-dot-н-dot-применение-алгебры-винтов-и-бикватернионов-для-вычисления-конечного-винтового-движения-точек-прямых-и-плоскостей}


#### <span class="section-num">2.6.1</span> Докладчик {#докладчик}

-   Геворкян Мигран Нельсонович
    -   доцент, к.ф.-м.н, доцент
    -   кафедра теории вероятностей и кибербезопасности РУДН


#### <span class="section-num">2.6.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/287/>
-   Применение алгебры винтов и бикватернионов для вычисления конечного винтового движения точек, прямых и плоскостей
-   Геворкян Мигран Нельсонович
    -   доцент, к.ф.-м.н, доцент
    -   кафедра теории вероятностей и кибербезопасности РУДН

В данном докладе представлено применение алгебры винтов и бикватернионов для вычисления винтового движения аффинных точек, свободных векторов, прямых и плоскостей. Алгебра винтов была разработана еще в конце 19 начале 20 веков, однако в настоящее время мало известна, хотя представляет собой весьма удобный и эффективный способ описания винтового движения. Особое внимание в докладе уделяется принципу перенесения Котельникова--Штуди, упоминания которого, судя по всему, практически не встречается в современных западных источниках. Доклад в целом носит методологический характер и призван устранить данный пробел, дав не только представления об основах математического аппарата перечисленных алгебр, но и проиллюстрировав применение данного аппарата на конкретных наглядных геометрических примерах.

---

-   Application of the screw algebra and dual quaternions algebra for screw motion of points, lines and planes
-   Gevorkyan, Migran Nelsonovich
    -   Docent, PhD, Associate Professor
    -   Department of Probability Theory and Cybersecurity, RUDN University

We present the application of the screw algebra and dual quaternions algebra for screw motion of affine points, free vectors, lines and planes. The screw algebra was developed in the late 19th and early 20th centuries, but is currently little known, although it is a very convenient and effective way to describe screw motion. Special attention in the report is given to the principle of Kotelnikov--Study transfer, which, apparently, is practically not mentioned in modern Western sources. The report as a whole is methodological in nature and is intended to eliminate this gap, giving not only an idea of the basics of the mathematical apparatus of the listed algebras, but also illustrating the application of this apparatus with concrete illustrative geometric examples.


#### <span class="section-num">2.6.3</span> Видео {#видео}

{{< tabs "Геворкян М. Н. - Применение алгебры винтов и бикватернионов для вычисления конечного винтового движения точек, прямых и плоскостей" >}}
{{< tab "RuTube" >}}

{{< rutube 48ae643878b202a2a63e39c2d4dc6dfd >}}

{{< /tab >}}
{{< tab "Платформа" >}}

{{< plvideo Rp4CROrgEVO9 >}}

{{< /tab >}}
{{< tab "VKvideo" >}}

{{< vkvideo -230024722 456239025 2 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube ZWlI7bDPRAU >}}

{{< /tab >}}
{{< /tabs >}}


### <span class="org-todo done DONE">DONE</span> <span class="section-num">2.7</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2025-05-22 Чт&gt; </span></span> Малышев К. Ю. - О суммировании в конечном виде и ускорении сходимости рядов Фурье в системах компьютерной алгебры {#малышев-к-dot-ю-dot-о-суммировании-в-конечном-виде-и-ускорении-сходимости-рядов-фурье-в-системах-компьютерной-алгебры}


#### <span class="section-num">2.7.1</span> Докладчик {#докладчик}

-   Малышев, Ксаверий Юрьевич
    -   аспирант
    -   кафедра математического моделирования и искусственного интеллекта, РУДН


#### <span class="section-num">2.7.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/291/>
-   О суммировании в конечном виде и ускорении сходимости рядов Фурье в системах компьютерной алгебры
-   Малышев, Ксаверий Юрьевич
    -   аспирант
    -   кафедра математического моделирования и искусственного интеллекта, РУДН

Разложения по собственным функциям дифференциальных операторов и их суммирование – важная часть математического моделирования. При этом возникает необходимость как суммирования рядов в конечном виде, так и ускорения сходимости. В работе рассматриваются тригонометрические ряды Фурье, в которых коэффициенты разложения являются рациональными функциями номера гармоники. Стандартные конечные выражения для указанных рядов, использующиеся в системах компьютерной алгебры (CAS), содержат специальные функции. Вместе с тем, в некоторых случаях данные ряды допускают выражение в конечном виде элементарных функций вещественной переменной. Даются достаточные условия представимости указанных рядов в элементарных функциях, алгоритм получения указанного представления, основанный на теории обобщённых функций. Полученные результаты используются для работы с рядами, ускорение сходимости которых по способу А.Н. Крылова является невозможным и нельзя получить иных выражений, кроме как в специальных функциях. Значительная часть предлагаемых конструкций допускает обобщение на разложения по системам собственных функций, отличных от тригонометрической.

---

-   On summation in finite form and acceleration of convergence of Fourier series in CAS
-   K. Yu. Malyshev
    -   PhD student
    -   Department of Mathematical Modeling and Artificial Intelligence, RUDN University

The eigenfunction expansions are important part of mathematical modeling. There is a need for both summation of series in finite form and acceleration of convergence. We consider trigonometric Fourier series with rational functions of the harmonic number in coefficients. Standard finite expressions for these series used in computer algebra systems contain higher transcendental functions. At the same time, in some cases, these series allow expression in finite form of piecewise elementary functions of a real variable. Sufficient conditions for the representability of these series in elementary functions and algorithm for obtaining the elementary representation based on the theory of generalized functions are are given. The obtained results are used to work with series, the acceleration of convergence of which is based on the method of A.N. Krylov is impossible and it is impossible to obtain other expressions except in special functions. A significant part of the proposed constructions allows generalization to expansions in systems of eigenfunctions other than trigonometric.


### <span class="org-todo done DONE">DONE</span> <span class="section-num">2.8</span> <span class="timestamp-wrapper"><span class="timestamp">&lt;2025-06-05 Чт&gt; </span></span> Сергеев С. В. - Спектральная реализация модифицированного метода Чебышевской коллокации {#сергеев-с-dot-в-dot-спектральная-реализация-модифицированного-метода-чебышевской-коллокации}


#### <span class="section-num">2.8.1</span> Докладчик {#докладчик}

-   Сергеев, Степан Викторович
    -   аспирант
    -   кафедра математического моделирования и искусственного интеллекта, РУДН


#### <span class="section-num">2.8.2</span> Информация {#информация}

-   <https://events.rudn.ru/event/293/>
-   Спектральная реализация модифицированного метода Чебышевской коллокации решения двухточечных задач для ЛОДУ второго порядка с использованием спектральных матриц дифференцирования и интегрирования
-   Сергеев, Степан Викторович
    -   аспирант
    -   кафедра математического моделирования и искусственного интеллекта, РУДН

Реализуется алгоритм численного решения граничных задач для обыкновенных дифференциальных уравнений, основанный на методе коллокации и представлении решения в виде разложения по полиномам Чебышева. Предлагается вместо традиционного подхода - слияния всех условий (дифференциальных и граничных) в одну систему линейных алгебраических уравнений (СЛАУ) - перейти к методике решения задачи в несколько отдельных этапов. Вначале определяются выделяются спектральные коэффициенты, описывающие «общее» решение исходной задачи. Возможны спектральные реализации метода Чебышевских коллокаций с помощью спектральных матриц дифференцирования и спектральных матриц интегрирования. Матрица формируемой во втором случае СЛАУ оказывается хорошо обусловленной даже при больших размерностях системы. Высокая точность решения достигается при достаточно малом количестве точек коллокации. Метод на основе матриц интегрирования следует выбирать в случаях, когда имеется запрос на высокую точность и устойчивость решения задачи. На втором этапе учет граничных условий выделяет «частное» искомое решение, однозначно доопределяя недостающие коэффициенты искомого разложения.

---

-   Spectral implementation of the modified Chebyshev collocation method for solving two-point problems for second-order LODEs using spectral matrices of differentiation and integration
-   Sergeev Stepan Viktorovich
    -   PhD student
    -   Department of Mathematical Modeling and Artificial Intelligence, RUDN University

An algorithm for numerically solving boundary value problems for ordinary differential equations is implemented, based on the collocation method and representation of the solution in the form of an expansion in Chebyshev polynomials. Instead of the traditional approach - merging all conditions (differential and boundary) into one system of linear algebraic equations (SLAE) - it is proposed to move to a method for solving the problem in several separate stages. First, spectral coefficients are determined that describe the "general" solution of the original problem. Spectral implementations of the Chebyshev collocation method are possible using spectral matrices of differentiation and spectral matrices of integration. The matrix of the SLAE formed in the second case turns out to be well-conditioned even for large dimensions of the system. High accuracy of the solution is achieved with a sufficiently small number of collocation points. The method based on integration matrices should be chosen in cases where there is a request for high accuracy and stability of the solution to the problem. At the second stage, taking into account the boundary conditions identifies a "particular" desired solution, uniquely determining the missing coefficients of the desired expansion.
