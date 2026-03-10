---
title: "Модель Кэли–Кляйна"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-05T18:40:00+03:00
lastmod: 2024-11-07T17:04:00+03:00
tags: ["research", "relativity"]
categories: ["science"]
draft: false
slug: "cayley-klein-model"
---

Модель Кэли--Кляйна.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   [Кляйн, Феликс Христиан]({{< relref "2024-11-04-klein-felix-christian" >}})


## <span class="section-num">2</span> Модельная структура теории {#модельная-структура-теории}

<a id="figure--fig:model-generic"></a>

{{< figure src="/ox-hugo/20241105184000--model-generic.svg" caption="<span class=\"figure-number\">&#1056;&#1080;&#1089;. 1.: </span>Модельная структура теории" >}}

-   Пуанкаре: Везде один и тот же математический аппарат (Евклидова геометрия)
-   Пенроуз: В каждой части --- свой формализм


## <span class="section-num">3</span> Модель Кэли--Кляйна {#модель-кэли-кляйна}


### <span class="section-num">3.1</span> Мероопределения {#мероопределения}

-   Пространственные измерения сводятся к двум основным процедурам: к определению расстояния между двумя точками и к определению угла между двумя пересекающимися прямыми.
-   Эти задачи можно охарактеризовать как проблему мероопределения в проективной геометрии.
-   Согласно схеме Кэли--Клейна [<a href="#citeproc_bib_item_1">1</a>; <a href="#citeproc_bib_item_2">2</a>] имеется три типа мероопределения:
    -   эллиптическое,
    -   параболическое,
    -   гиперболическое.
-   Будем обозначать эллиптическое мероопределение символом `-`, параболическое мероопределение символом `0`, гиперболическое мероопределение символом `+`.


#### <span class="section-num">3.1.1</span> Эллиптическое мероопределение длин {#эллиптическое-мероопределение-длин}

<a id="figure--fig:length:elliptic"></a>

{{< figure src="/ox-hugo/20241105184000--length-elliptic.svg" caption="<span class=\"figure-number\">&#1056;&#1080;&#1089;. 2.: </span>Эллиптическое мероопределение длин" >}}

-   Эллиптическое мероопределение длин задаётся на прямой \\(o\\) следующим образом.
-   Зададим вне \\(o\\) некоторую точку \\(Q\\) и положим, что расстояние между точками \\(A\\) и \\(B\\) прямой \\(o\\) равно углу \\(\angle AQB\\):

\\[\tensor\*[^{-}]{\mathop{\mathrm{d}}}{\_{AB}} = \angle AQB.\\]

-   Для последовательных точек \\(A\\), \\(B\\), \\(C\\) справедливо следующее равенство:

\\[\tensor\*[^{-}]{\mathop{\mathrm{d}}}{\_{AC}} + \tensor\*[^{-}]{\mathop{\mathrm{d}}}{\_{CB}} = \tensor\*[^{-}]{\mathop{\mathrm{d}}}{\_{AB}}.\\]

-   Примером эллиптического мероопределения длин может служить геометрия Римана.


### <span class="section-num">3.2</span> Проективные геометрии Кэли--Кляйна {#проективные-геометрии-кэли-кляйна}

-   Согласно схеме Кэли--Кляйна на плоскости определяются девять проективных геометрий.

<a id="table--tab:ck-model"></a>
<div class="table-caption">
  <span class="table-number"><a href="#table--tab:ck-model">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1</a>:</span>
  Геометрии Кэли&#x2013;Кляйна на плоскости
</div>

|           | Угол (-)                               | Угол (0)                      | Угол (+)                                        |
|-----------|----------------------------------------|-------------------------------|-------------------------------------------------|
| Длина (-) | Эллиптическая геометрия Римана         | Антиевклидова геометрия       | Антигиперболическая геометрия (анти де Ситтера) |
| Длина (0) | Геометрия Евклида                      | Геометрия Галилея             | Псевдоевклидова геометрия Минковского           |
| Длина (+) | Гиперболическая геометрия Лобачевского | Антипсевдоевклидова геометрия | Дважды гиперболическая геометрия (де Ситтера)   |


### <span class="section-num">3.3</span> Модель Кэли--Кляйна и комплексные числа {#модель-кэли-кляйна-и-комплексные-числа}

-   \\(\Delta < 0\\), \\(z = a + \ii b\\), \\(\ii^2 = -1\\) ---  эллиптические комплексные числа (обыкновенные комплексные числа);
-   \\(\Delta = 0\\), \\(z = a + \iiz b\\), \\(\iiz^2 = 0\\), \\(\iiz \neq 0\\) --- параболические комплексные числа (дуальные числа);
-   \\(\Delta > 0\\), \\(z = a + \iip b\\), \\(\iip^2 = 1\\), \\(\iip \neq \pm 1\\) --- гиперболические комплексные числа (двойные числа).
-   Только обыкновенные комплексные числа имеют структуру поля.
-   Дуальные и двойные имеют структуру кольца, поскольку содержат нетривиальные делители нуля.


## <span class="section-num">4</span> Гиперболические комплексные числа {#гиперболические-комплексные-числа}


### <span class="section-num">4.1</span> Алгебраические свойства гиперболических чисел {#алгебраические-свойства-гиперболических-чисел}

-   Для двух гиперболических чисел \\(z\_1 = x\_1 + \iip y\_1\\) и \\(z\_2 = x\_2 + \iip y\_2\\) выполняются следующие операции:
-   Сложение: \\(z\_1 + z\_2 = (x\_1 + x\_2) + \iip (y\_1 + y\_2)\\).
-   Умножение:  \\(z\_1 z\_2 = (x\_1 x\_2 + y\_1 y\_2) + \iip (x\_1 y\_2 + x\_2 y\_1)\\).
-   Сопряжение: \\(z^{\ast} = x - \iip y\\).
-   Обратное число:  \\(z^{-1} = \dfrac{x}{x^2 + y^2} - \iip \dfrac{y}{x^2 - y^2}\\).
-   Деление: \\(\dfrac{z\_1}{z\_2} = \dfrac{x\_1 x\_2 - y\_1 y\_2}{x^2\_2 - y^2\_2} + \iip \dfrac{x\_1 y\_1 - x\_1 y\_2}{x^2\_2 - y^2\_2}\\).


### <span class="section-num">4.2</span> Матричное представление {#матричное-представление}

-   Гиперболические числа можно представить в матричном виде:

\\[x + \iip y \leftrightarrow
    \begin{pmatrix}
      x & y \\\\
      y & x
    \end{pmatrix}\\]

-   Тогда сложение, умножение чисел и нахождение обратного числа сводятся к сложению, умножению матриц и нахождению обратной матрицы.


### <span class="section-num">4.3</span> Аналог формулы Эйлера {#аналог-формулы-эйлера}

-   \\[e^{\iip\varphi} = \cosh{\varphi} + \iip \sinh{\varphi}, \varphi \in \mathbb{R}.\\]
-   Доказывается разложением в ряд экспоненты \\(e^{\iip}\varphi\\):

\\[e^{\iip}\varphi = 1 + \frac{\iip \varphi}{1!} + \frac{(\iip \varphi)^2}{2!} + \frac{(\iip \varphi)^3}{3!} + \ldots\\]

-   Используя свойства \\(\iip^2 = 1\\), \\(\iip^3 = \iip\\), \\(\iip^4 = 1\\), \\(\iip^5 = \iip\\) и т.д. получим:

\\[e^{\iip\varphi} = \underbrace{\left(1 + \frac{\varphi^2}{2!} + \frac{\varphi^4}{4!} + \ldots\right)}\_{\cosh\varphi} + \underbrace{\iip \left(\frac{\varphi}{1!} + \frac{\varphi^3}{3!} + \ldots\right)}\_{\sinh\varphi} = \cosh\varphi + \iip \sinh\varphi.\\]


### <span class="section-num">4.4</span> Модуль гиперболического числа {#модуль-гиперболического-числа}

-   Модуль \\(r\\) числа \\(z = x + \iip y\\) определяется формулой:

\\[|z| = r =
    \begin{cases}
      \sqrt{x^2 - y^2}, &|x| > |y|,\\\\
       0,  & |x| = |y|,\\\\
      \sqrt{y^2 - x^2}, &|x| < |y|.
    \end{cases}\\]


### <span class="section-num">4.5</span> Гиперболическое представление {#гиперболическое-представление}

-   Аналогично тригонометрическому представлению комплексных чисел можно ввести гиперболическое представление для гиперболических чисел:

\\[z = x + \iip y =
    \begin{cases}
      r(\cosh\varphi + \iip \sinh\varphi), &|x| > |y|,\\\\
      0 ,  &|x| = |y|,\\\\
      \iip r (\sinh\varphi + \iip \sinh\varphi), &|x| < |y|.
    \end{cases}\\]


### <span class="section-num">4.6</span> Экспоненциальное представление {#экспоненциальное-представление}

-   Из формулы Эйлера получим:
    \\[z =
        \begin{cases}
          r e^{\iip \varphi}, &|x| > |y|,\\\\
           0, & |x| = |y|,\\\\
          \iip r e^{\iip \varphi}, &|x| < |y|.
        \end{cases}\\]


### <span class="section-num">4.7</span> Гиперболический угол {#гиперболический-угол}

-   Величина \\(\varphi\\) --- гиперболический угол или _аргумент числа \\(z\\)_ (\\(\varphi = \arg{z}\\)) выражается через гиперболический ареатангенс.

\\[\varphi =
    \begin{cases}
      \mathrm{arth}\\,{\frac{y}{x}}, & |x| > |y|,\\\\
      \mathrm{arth}\\,{\frac{x}{y}}, & |x| < |y|.
    \end{cases}\\]


### <span class="section-num">4.8</span> Гиперболические числа и пространство Минковского \\(\mathrm{E}^2\_{1,1}\\) {#гиперболические-числа-и-пространство-минковского-mathrm-e-2-1-1}

-   С помощью гиперболических чисел можно представить точку в двумерном пространстве Минковского \\(\mathrm{E}^2\_{1,1}\\):

\\[x^0 + \iip x^1 \leftrightarrow (x^0, x^1) \in \mathrm{E}^2\_{1,1}.\\]

-   Это возможно благодаря тому, что:

\\[|\Delta z|^2 = \Delta z \cdot \Delta z^{\ast} = (\Delta x^0)^2 - (\Delta x^1)^2.\\]


### <span class="section-num">4.9</span> Двумерные преобразования Лоренца и гиперболические числа {#двумерные-преобразования-лоренца-и-гиперболические-числа}

-   Преобразования Лоренца \\((ct, x) \to (ct^\prime, x^\prime)\\) в классическом виде:

\\[\begin{pmatrix}
      c t^\prime\\\\
      x^\prime
    \end{pmatrix}
    =
    \begin{pmatrix}
      \gamma & -\gamma\frac{v}{c}\\\\
      -\gamma\frac{v}{c} & \gamma\\\\
    \end{pmatrix} \times
    \begin{pmatrix}
      ct\\\\
      x
    \end{pmatrix},\\]
где \\(\gamma\\) --- коэффициент Лоренца:
\\[\gamma = \dfrac{1}{\sqrt{1 - v^2/c^2}}\\]


### <span class="section-num">4.10</span> Двумерные преобразования Лоренца и гиперболические числа {#двумерные-преобразования-лоренца-и-гиперболические-числа}

-   Так как
    \\[\cosh\varphi = 1 / \sqrt{1 - \tanh^2\varphi}, \tanh^2{\varphi} \leqslant 1,\\]

то положив \\(\tanh\varphi = v/c\\)
получим
\\[\cosh\varphi = \gamma\\]
и
\\[\sinh\varphi = \tanh\varphi\cosh\varphi = \gamma \frac{v}{c}.\\]

-   Эти соотношения позволяют перейти к гиперболическому виду матрицы преобразования Лоренца.


### <span class="section-num">4.11</span> Двумерные преобразования Лоренца и гиперболические числа {#двумерные-преобразования-лоренца-и-гиперболические-числа}

\begin{equation}
\begin{pmatrix}
      c t^\prime\\\\
      x^\prime
    \end{pmatrix}
    =
    \begin{pmatrix}
      \gamma & -\gamma\frac{v}{c}\\\\
      -\gamma\frac{v}{c} & \gamma\\\\
    \end{pmatrix}
    \times
    \begin{pmatrix}
      ct\\\\
      x
    \end{pmatrix}
    =
    \begin{pmatrix}
      \cosh\varphi & -\sinh\varphi\\\\
      -\sinh\varphi & \cosh\varphi\\\\
    \end{pmatrix}
    \times
    \begin{pmatrix}
      ct\\\\
      x
    \end{pmatrix}
\end{equation}

-   Используем матричное представление гиперболических чисел:

\begin{equation}
x + \iip y \leftrightarrow
    \begin{pmatrix}
      x & y \\\\
      y & x
    \end{pmatrix}.
\end{equation}

-   Заменяем матрицу преобразования Лоренца на соответствующее ей гиперболическое число:

\begin{equation}
\begin{pmatrix}
      \cosh\varphi & -\sinh\varphi\\\\
      -\sinh\varphi & \cosh\varphi\\\\
    \end{pmatrix}
    \leftrightarrow
    \cosh\varphi - \iip \sinh\varphi = e^{-\iip \varphi}.
\end{equation}


### <span class="section-num">4.12</span> Двумерные преобразования Лоренца и гиперболические числа {#двумерные-преобразования-лоренца-и-гиперболические-числа}

-   В экспоненциальном виде гиперболического числа преобразование Лоренца сводится к соотношению

\\[(ct^\prime, x^\prime) = e^{-\varphi \iip}(ct, x).\\]

-   То есть определяется гиперболическим углом \\(\varphi\\).


### <span class="section-num">4.13</span> Формула сложения скоростей {#формула-сложения-скоростей}

-   Формулу сложения скоростей можно вывести выполнив два преобразования Лоренца подряд.

\begin{equation}
\begin{gathered}
    (ct^\prime, x^\prime) = e^{-\iip\varphi\_1}(ct, x),\\\\
    (ct^{\prime\prime}, x^{\prime\prime}) = e^{-\iip\varphi\_2}(ct^\prime, x^\prime),\\\\
    (ct^{\prime\prime}, x^{\prime\prime}) = e^{-\iip\varphi\_2}e^{-\iip\varphi\_1}(ct^\prime, x^\prime) = e^{-\iip(\varphi\_1+\varphi\_2)}(ct, x) = e^{-\iip\varphi\_3}(ct, x).
\end{gathered}
\end{equation}

-   Композиция двух преобразований Лоренца свелось к сложению гиперболических углов:
    \\[\varphi\_3 = \varphi\_1 + \varphi\_2.\\]


### <span class="section-num">4.14</span> Формула сложения скоростей {#формула-сложения-скоростей}

-   Учитывая, что \\(\tanh\varphi = v/c\\) получим:

\\[\tanh\varphi\_3 = \tanh(\varphi\_1 + \varphi\_2) = \dfrac{\tanh\varphi\_1 + \tanh\varphi\_2}{1 - \tanh\varphi\_1\tanh\varphi\_2} = \dfrac{v\_1/c + v\_2/c}{1 - v\_1v\_2/c^2}.\\]

-   Заменяя \\(\tanh\varphi\_3 = v\_3/c\\) получим правило сложения скоростей

\\[v\_3 = c \dfrac{v\_1/c + v\_2/c}{1 - v\_1v\_2/c^2} = \dfrac{v\_1 + v\_2}{1 - v\_1v\_2/c^2}.\\]


### <span class="section-num">4.15</span> Умножение скорости на число {#умножение-скорости-на-число}

-   Рассмотрим операцию умножения вектора скорости на скаляр (\\(\alpha \in \mathbb{R}\\)), что эквивалентно умножению гиперболического угла на число: \\[\varphi\_2 = \alpha \varphi\_1.\\]
-   Выражая гиперболический тангенс через экспоненту, получаем:

\\[\tanh\varphi\_2 = \tanh\alpha\varphi\_1 = \dfrac{e^{2\alpha\varphi\_1} - 1}{e^{2\alpha\varphi\_1} + 1} = \dfrac{e^{\alpha\ln\dfrac{1 + v/c}{1 - v/c}} - 1}{e^{\alpha\ln\dfrac{1 + v/c}{1 - v/c}} + 1} = \dfrac{\left(\dfrac{1 + v/c}{1-v/c}\right)^\alpha - 1}{\left(\dfrac{1 + v/c}{1-v/c}\right)^\alpha + 1}\\]

-   Учитывая \\(\tanh\varphi = v / c\\) получаем:

\\[v\_2 = c \dfrac{(1 + v/c)^\alpha - (1 - v/c)^\alpha}{(1 + v/c)^\alpha + (1 - v/c)^\alpha}.\\]


### <span class="section-num">4.16</span> Умножение скорости на число {#умножение-скорости-на-число}

-   В качестве проверки данной формулы можно вычислить \\(2v\\) как \\(v + v\\) и сравнить результаты.
-   Пользуясь формулой умножения скорости на скаляр, получим:

\\[2v  = c \dfrac{(1 + v/c)^2 - (1 - v/c)^2}{(1 + v/c)^2 + (1 - v/c)^2} = c\dfrac{4\frac{v}{c}}{2\left(1 + \frac{v^2}{c^2}\right)} = \dfrac{2v}{1 + \frac{v^2}{c^2}}.\\]

-   Используя же сложение скоростей, также получим:
    \\[v + v = \dfrac{2v}{1+\frac{v^2}{с^2}}.\\]
-   Откуда видно, что результаты совпадают.


## <span class="section-num">5</span> Релятивистские операции {#релятивистские-операции}

-   Для реализации математического аппарата операций в пространстве Минковского предлагается использовать систему гиперболических комплексных чисел.
-   Для простоты описания мы рассматриваем только одномерные движения.
-   При описании полного пространства Минковского необходимо будет перейти от комплексных чисел к более сложным объектам, например, к соответствующего типа кватернионам [<a href="#citeproc_bib_item_3">3</a>–<a href="#citeproc_bib_item_6">6</a>].
-   Релятивистские расчёты в общем случае некоммутативны [<a href="#citeproc_bib_item_7">7</a>; <a href="#citeproc_bib_item_8">8</a>].

-   Гиперболическое комплексное число \\(z = r \exp{\iip \varphi}\\) соответствует точке в пространстве Минковского.
-   Аргумент \\(\varphi\\) комплексного числа \\(z\\) представляет собой угол между касательной к мировой линии частицы и осью времени в базовой системе отсчёта.
-   Аргумент связан со скоростью следующим соотношением:

\\[\varphi = \artanh \frac{v}{c}.\\]

-   Он также имеет название быстроты [<a href="#citeproc_bib_item_7">7</a>; <a href="#citeproc_bib_item_9">9</a>].

-   Последовательность действий следующая (будем рассматривать только времениподобные интервалы):

-   В рамках операциональной части приготовления системы обычные величины переводятся в форму гиперболических комплексных чисел \\({}^{+}\mathbb{C}\\).
    Поскольку скорости переводятся во вращения во временной плоскости (бусты), необходимо выполнить следующую операцию:  \\[\frac{v}{c} \to \tanh \varphi,\\]
-   Получим соответствующее комплексное число: \\[z = \exp{\iip \artanh \frac{v}{c}}.\\]
-   Здесь \\(\varphi\\) --- аргумент соответствующего комплексного числа, модулем комплексного числа мы пренебрегаем.
-   В теоретической части производятся вычисления над получившимися комплексными числами.
-   В рамках измерительной операциональной части производится перевод выражений в гиперболических комплексных числах \\({}^{+}\mathbb{C}\\) в выражения в действительных числах, описывающих релятивистские соотношения \\(\Lambda\\): \\[\varphi \to \artanh \frac{v}{c}.\\]
-   Соответствующая релятивистская скорость будет иметь вид:
    \\[\label{eq:v=c\_tanh\_varphi} v\_{\Lambda} = c \tanh \varphi.\\]
-   Для удобства, в рамках одномерных движений мы можем ввести символ эйнштейновских операций \\(\rel\\), непосредственно преобразующий операцию \\(\mathrm{Op}\_{\mathrm{Gal}}\\) в пространстве Галилея в операцию \\(\mathrm{Op}\_{\Lambda}\\) в пространстве Лоренца:

\\[\mathrm{Op}\_{\Lambda} = \rel(\mathrm{Op}\_{\mathrm{Gal}}).\\]

-   Данная операция маскирует полный цикл перехода от нерелятивистских выражений \\(\mathrm{Gal}\\) к релятивистским \\(\Lambda\\) посредством гиперболических комплексных чисел.


## <span class="section-num">6</span> Основные алгебраические операции {#основные-алгебраические-операции}

-   Выпишем основные операции.


### <span class="section-num">6.1</span> Сложение скоростей {#сложение-скоростей}

-   Продемонстрируем операцию сложения, как выполняя полный цикл преобразования, так и выполняя короткое релятивистское преобразование \\(\rel\\).
-   Преобразование Лоренца определяется умножением на гиперболическое комплексное число с единичным модулем \\(\exp{\iip \psi}\\), в результате плоскость Минковского поворачивается на угол \\(\psi\\):

\\[\label{eq:rel:sum:rapidity}
  z\_{1}(\varphi) z\_{2}(\psi) = \exp{\iip \varphi} \exp{\iip \psi} =
  \exp{\iip (\varphi + \psi)} = z(\varphi + \psi).\\]

-   Заменив быстроты на скорости, получим:

\\[z\qty(\artanh{\frac{v\_{1}}{c}} + \artanh{\frac{v\_{2}}{c}}) =
  \exp{\iip \qty(\artanh{\frac{v\_{1}}{c}} + \artanh{\frac{v\_{2}}{c}})}.\\]

-   Перейдём к действительным релятивистским скоростям:

\\[(v\_{1} + v\_{2})\_{\Lambda} = c \tanh(\artanh{\frac{v\_{1}}{c}} + \artanh{\frac{v\_{2}}{c}}).\\]

-   Продемонстрируем то же самое с помощью операции \\(\rel\\).
-   Запишем операцию сложения:

\\[\begin{gathered}
  \label{eq:rel\_v+v}
  \rel ( v\_{1} + v\_{2} ) =
  c \tanh(\artanh{\frac{v\_{1}}{c}} + \artanh{\frac{v\_{2}}{c}})
  = \\\ {}
  =
  c \frac{\tanh{\artanh{\dfrac{v\_{1}}{c}}}+\tanh{\artanh{\dfrac{v\_{2}}{c}}}}
  {1 + \tanh{\artanh{\dfrac{v\_{1}}{c}}}\tanh{\artanh{\dfrac{v\_{2}}{c}}}}
  % = \\\ {}
  =
  \frac{v\_{1} + v\_{2}}{1 + \dfrac{v\_{1} v\_{2}}{c^2}}.
\end{gathered}\\]

-   Данную операцию можно записать для произвольного количества операндов.
-   Для трёх операндов получим следующее выражение:

\\[\label{eq:rel\_v+v+v}
  \rel ( v\_{1} + v\_{2} + v\_{3} )
  % \\\ {}
  =
  \frac{v\_{1} + v\_{2} + v\_{3} + \dfrac{v\_{1} v\_{2} v\_{3}}{c^2}}
  {1 +
    \dfrac{v\_{1} v\_{2} + v\_{1} v\_{3} + v\_{2} v\_{3} }{c^2}
  }.\\]

-   Операция сложения в предложенном формализме совпадает с общепринятой, но при этом проще в применении.


### <span class="section-num">6.2</span> Умножение скоростей {#умножение-скоростей}

-   Операция умножения скоростей обычно не используется при релятивистских расчётах.
-   Однако мы введём её для полноты изложения.
-   Заметим, что поскольку мы конструируем релятивистские операции не для собственно скоростей, а для быстрот, то в правой части мы получаем множитель \\(c^{2}\\) (сравните с [<a href="#citeproc_bib_item_10">10</a>; <a href="#citeproc_bib_item_11">11</a>]):

\\[\begin{gathered}
  \label{eq:rel\_vv}
  \rel ( v\_{1} v\_{2} ) =
  c^{2} \tanh(\artanh{\frac{v\_{1}}{c}} \artanh{\frac{v\_{2}}{c}})
  = \\\ {}
  =
  c^{2} \tanh(
  \frac {1}{2} \ln(\frac{1+\flatfrac{v\_{1}}{c}}{1-\flatfrac{v\_{1}}{c}})
  \frac {1}{2} \ln(\frac{1+\flatfrac{v\_{2}}{c}}{1-\flatfrac{v\_{2}}{c}})
  )
  = \\\ {}
  =
  c^{2} \frac{
    \exp[\dfrac {1}{2}
    \ln(\dfrac{1+\flatfrac{v\_{1}}{c}}{1-\flatfrac{v\_{1}}{c}})
    \ln(\dfrac{1+\flatfrac{v\_{2}}{c}}{1-\flatfrac{v\_{2}}{c}})
    ] - 1
  }{
    \exp[\dfrac {1}{2}
    \ln(\dfrac{1+\flatfrac{v\_{1}}{c}}{1-\flatfrac{v\_{1}}{c}})
    \ln(\dfrac{1+\flatfrac{v\_{2}}{c}}{1-\flatfrac{v\_{2}}{c}})
    ] + 1
  }.
\end{gathered}\\]


### <span class="section-num">6.3</span> Умножение на число {#умножение-на-число}

-   Рассмотрим умножение вектора скорости на число \\(k \in \mathbb{R}\\) в предложенном представлении (сравните с [<a href="#citeproc_bib_item_12">12</a>; <a href="#citeproc_bib_item_13">13</a>]):

\begin{equation}
\begin{gathered}
  \label{eq:rel\_kv}
  \rel ( k v ) =
  c \tanh(k \artanh{\frac{v}{c}})
  = \\\ {} =
  % =
  c \frac{
    \exp[k
    \ln(\frac{1+\flatfrac{v}{c}}{1-\flatfrac{v}{c}})
    ] - 1
  }{
    \exp[k
    \ln(\frac{1+\flatfrac{v}{c}}{1-\flatfrac{v}{c}})
    ] + 1
  }
  =
  c \frac{
    \qty(\frac{1+\flatfrac{v}{c}}{1-\flatfrac{v}{c}})^{k}
    - 1
  }{
    \qty(\frac{1+\flatfrac{v}{c}}{1-\flatfrac{v}{c}})^{k}
    + 1
  }
  = \\\ {} =
  % =
  c \frac{
    \qty(1+\frac{v}{c})^{k}
    -
    \qty(1-\frac{v}{c})^{k}
  }{
    \qty(1+\frac{v}{c})^{k}
    +
    \qty(1-\frac{v}{c})^{k}
  }.
\end{gathered}
\end{equation}

-   Это выражение никогда не превысит скорость света \\(c\\): \\[\label{eq:rel\_kv:lim}
      \lim\_{k \to \infty} \rel ( k v ) = c.\\]

-   В качестве примера можно записать выражение для \\(\rel(2v)\\).
-   Учтём: \\[\label{eq:rel\_v+v:test}
      \rel ( 2 v ) =
      \rel ( v + v )
      =
      \frac{2 v}{1 + \dfrac{v^2}{c^2}}.\\]
-   Получим:

\begin{equation}
\label{eq:rel\_2v:test}
  \rel ( 2 v )
  =
  c \frac{
    \qty(1+\frac{v}{c})^{2}
  -
    \qty(1-\frac{v}{c})^{2}
  }{
    \qty(1+\frac{v}{c})^{2}
  +
    \qty(1-\frac{v}{c})^{2}
  }
  % \\\ {}
  =
  c \frac{4 \dfrac{v}{c}}
  {2 \qty(1 + \dfrac{v^2}{c^2})} =
  \frac{2 v}{1 + \dfrac{v^2}{c^2}}.
\end{equation}

-   Предлагаемое представление не вносит противоречия в процедуру сложения скоростей.
-   Процедура умножения скорости на число согласована с процедурой сложения скоростей.
-   Аналогично, можно записать выражение для \\(\rel(3v)\\).
-   Учитывая: \\[\label{eq:rel\_v+v+v:test}
      \rel ( 3 v ) =
      \rel ( v + v + v )
      =
      \frac{3 v + \dfrac{v^3}{c^2}}{1 + 3 \dfrac{v^2}{c^2}}.\\]
-   Получим:

    \begin{equation}
    \label{eq:rel\_3v:test}
    \rel ( 3 v )
    =
    c \frac{
      \qty(1+\frac{v}{c})^{3}
      -
      \qty(1-\frac{v}{c})^{3}
    }{
      \qty(1+\frac{v}{c})^{3}
      +
      \qty(1-\frac{v}{c})^{3}
    }
    =
    \frac{3 v + \dfrac{v^3}{c^2}}{1 + 3 \dfrac{v^2}{c^2}}.
    \end{equation}


## <span class="section-num">7</span> Снятие несогласованностей релятивистских операций {#снятие-несогласованностей-релятивистских-операций}


### <span class="section-num">7.1</span> Пример несогласованности математического аппарата частной теории относительности {#пример-несогласованности-математического-аппарата-частной-теории-относительности}

-   При умножении формальная скорость \\(v\\) превосходит скорость света \\(c\\).
-   Наклонное падение луча \\[v = c / (n\sin\alpha)\\].
-   Световой зайчик (пятно) \\[v = \omega r\\]


### <span class="section-num">7.2</span> Наклонное падение {#наклонное-падение}

-   Перепишем соотношение \\(v = c / (n\sin\alpha)\\) в релятивистском случае:

    \begin{equation}
    \label{eq:v=c/sin:rel}
    v = \rel \left( \frac{c}{\sin{\varphi}} \right)
    =
    c \frac{
      \qty(1+\frac{c}{c})^{{1}/{\sin{\varphi}}}
      -
      \qty(1-\frac{c}{c})^{{1}/{\sin{\varphi}}}
    }{
      \qty(1+\frac{c}{c})^{{1}/{\sin{\varphi}}}
      +
      \qty(1-\frac{c}{c})^{{1}/{\sin{\varphi}}}
    }
    =
    c.
    \end{equation}


### <span class="section-num">7.3</span> Фазовая скорость {#фазовая-скорость}

-   Заменим в \\(v = \omega r\\) обычное умножение на релятивистское:

\begin{equation}
\label{eq:phase-velocity:rel}
  v\_{p}(\varphi) = \rel \qty( \frac{v\_{p}(0)}{\cos{\varphi}} )
  =
  c \frac{
    \qty(1+\frac{v\_{p}(0)}{c})^{\flatfrac{1}{\cos{\varphi}}}
    -
    \qty(1-\frac{v\_{p}(0)}{c})^{\flatfrac{1}{\cos{\varphi}}}
  }{
    \qty(1+\frac{v\_{p}(0)}{c})^{\flatfrac{1}{\cos{\varphi}}}
    +
    \qty(1-\frac{v\_{p}(0)}{c})^{\flatfrac{1}{\cos{\varphi}}}
  }.
  \end{equation}

-   Запишем предел:

\\[\lim\_{\cos{\varphi} \to 0} v\_{p}(\varphi) = c.\\]

-   Фазовая скорость не превышает скорость света.

-   Таким образом, при последовательном применении предложенных релятивистских операций никаких несогласованностей не возникает.


## <span class="section-num">8</span> Библиография {#библиография}

## Литература

<div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>1.	Cayley, A. IV. A sixth memoir upon quantics / A. Cayley // Philosophical Transactions of the Royal Society of London. – 1859. – Т. 149. – Сс. 61–90. DOI: <a href="https://doi.org/10.1098/rstl.1859.0004">10.1098/rstl.1859.0004</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>2.	Klein, F.C. <a href="https://doi.org/10.1007/978-3-7091-9511-6_5">Über die sogenannte Nicht-Euklidische Geometrie</a> / F.C. Klein // Gauß und die Anfänge der nicht-euklidischen Geometrie : Teubner-Archiv zur Mathematik. – Wien : Springer-Verlag Wien, 1985. – Т. 4. – Сс. 224–238.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>3.	Buchheim, A. A Memoir on Biquaternions / A. Buchheim // American Journal of Mathematics. – 1885. – Т. 7. – № 4. – Сс. 293–326. DOI: <a href="https://doi.org/10.2307/2369176">10.2307/2369176</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>4.	Silberstein, L. Quaternionic form of relativity / L. Silberstein // The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, Series 6. – 1912. – Т. 23. – № 137. – Сс. 790–809. DOI: <a href="https://doi.org/10.1080/14786440508637276">10.1080/14786440508637276</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_5"></a>5.	Girard, P.R. The quaternion group and modern physics / P.R. Girard // European Journal of Physics. – 1984. – Т. 5. – № 1. – Сс. 25–32. DOI: <a href="https://doi.org/10.1088/0143-0807/5/1/007">10.1088/0143-0807/5/1/007</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_6"></a>6.	Yefremov, A.P. <a href="http://arxiv.org/abs/math-ph/0501055">Quaternions and Biquaternions: Algebra, Geometry and Physical Theories</a>. Quaternions and Biquaternions / A.P. Yefremov. – 2005.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_7"></a>7.	Зоммерфельд, А.И.В. О сложении скоростей в теории относительности / А.И.В. Зоммерфельд // Успехи физических наук. – 2010. – Т. 180. – № 9. – Сс. 970–972. DOI: <a href="https://doi.org/10.3367/UFNr.0180.201009e.0970">10.3367/UFNr.0180.201009e.0970</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_8"></a>8.	Малыкин, Г.Б. Некоммутативность сложения неколлинеарных скоростей в специальной теории относительности и метод геометрической фазы (к столетию со дня публикации работы А. Зоммерфельда) / Г.Б. Малыкин // Успехи физических наук. – 2010. – Т. 180. – № 9. – Сс. 965–969. DOI: <a href="https://doi.org/10.3367/UFNr.0180.201009d.0965">10.3367/UFNr.0180.201009d.0965</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_9"></a>9.	Varićak, V. Anwendung der Lobatschefskijschen Geometrie in der Relativtheorie / V. Varićak // Physikalische Zeitschrift. – 1910. – Т. 11. – Сс. 93–96.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_10"></a>10.	Baker, G.A. Jr. Einstein Numbers / G.A. Baker Jr // The American Mathematical Monthly. – 1954. – Т. 61. – № 1. – Сс. 39–41. DOI: <a href="https://doi.org/10.2307/2306894">10.2307/2306894</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_11"></a>11.	Gregor, T. Generalizations of Einstein Numbers by Adding New Dimensions to Domains Preserving Commutativity and Associativity / T. Gregor, J. Haluška // Journal of Advanced Mathematics and Applications. – 2015. – Т. 4. – № 1. – Сс. 3–10. DOI: <a href="https://doi.org/10.1166/jama.2015.1067">10.1166/jama.2015.1067</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_12"></a>12.	Ungar, A.A. Einstein’s velocity addition law and its hyperbolic geometry / A.A. Ungar // Computers and Mathematics with Applications. – 2007. – Т. 53. – № 8. – Сс. 1228–1250. DOI: <a href="https://doi.org/10.1016/j.camwa.2006.05.028">10.1016/j.camwa.2006.05.028</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_13"></a>13.	Ungar, A.A. <a href="https://arxiv.org/abs/1302.6961">Einstein’s Special Relativity: the Hyperbolic Geometric Viewpoint</a> / A.A. Ungar // Conference on Mathematics, Physics and Philosophy on the Interpretations of Relativity. – Budapest, 2009. – Einstein’s Special Relativity. – Сс. 1–35.</div>
</div>
