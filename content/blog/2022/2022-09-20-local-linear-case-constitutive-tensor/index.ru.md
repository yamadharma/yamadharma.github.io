---
title: "Тензор проницаемостей для локального линейного случая"
author: ["Dmitry S. Kulyabov"]
date: 2022-09-20T17:51:00+03:00
lastmod: 2023-10-14T17:26:00+03:00
draft: false
slug: "local-linear-case-constitutive-tensor"
---

-   Тензор проницаемостей для локального линейного случая.

-   Статья:
    -   Тензор проницаемостей в геометризованной теории Максвелла.
    -   Constitutive tensor in the geometrized Maxwell theory [<a href="#citeproc_bib_item_1">1</a>].

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Соглашения и обозначения {#соглашения-и-обозначения}

1.  Будем использовать нотацию абстрактных индексов [<a href="#citeproc_bib_item_2">2</a>]. В данной нотации тензор как целостный объект обозначается просто индексом (например,  \\(x^{i}\\)), компоненты обозначаются подчёркнутым индексом (например,  \\(x^{\crd{i}}\\)).

2.  Будем придерживаться следующих соглашений. Греческие индексы (\\(\alpha\\), \\(\beta\\)) будут относиться к четырёхмерному пространству и в компонентном виде будут иметь следующие значения:  \\(\crd{\alpha} = \overline{0,3}\\). Латинские индексы из середины алфавита (\\(i\\), \\(j\\), \\(k\\)) будут относиться к трёхмерному  пространству и в компонентном виде будут иметь следующие значения:  \\(\crd{i} = \overline{1,3}\\).

3.  Прописными латинскими буквами обозначим индексы шестимерного пространства: \\(\crd{I} = \overline{1,6}\\).

4.  Запятой в индексе обозначается частная производная по соответствующей координате (\\(f\_{,i} := \partial\_{i} f\\)); точкой с запятой --- ковариантная производная (\\(f\_{;i} := \nabla\_{i}f\\)).

5.  Для записи уравнений электродинамики в работе используется система СГС симметричная [<a href="#citeproc_bib_item_3">3</a>].


## <span class="section-num">2</span> Варианты физической среды {#варианты-физической-среды}

-   Тензоры \\(F\_{\alpha \beta}\\) и \\(G^{\alpha \beta}\\) имеют смысл кривизны в кокасательном (\\(T^{\*}X\\)) и касательном (\\(TX\\)) расслоениях.
-   Линейный нелокальный случай при наличии трансляционной симметрии сводится к линейному локальному случаю с помощью преобразования Фурье.
-   Запишем нелокальную линейную связь между \\(F\\) и \\(G\\) следующим образом:

    \begin{equation}
    \label{eq:lambda:linear:nonlocal}
    G(x) = \int \lambda(x,s) \wedge F (s) \dd{s}.
    \end{equation}
-   Предполагая наличие трансляционной инвариантности \\(\lambda(x,s) = \lambda(x - s),\\) запишем связь между \\(F\\) и \\(G\\):

     \begin{equation}
     \label{eq:lambda:nonlinear:local:furier}
     G^{\alpha \beta} (\omega, k\_i) = \lambda^{\alpha \beta \gamma \delta} (\omega,k\_i) F\_{\gamma \delta}(\omega,k\_i).
    \end{equation}

    <div class="table-caption">
      <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
      Варианты тензора напряжённостей
    </div>

    |            | локальный                                                                          | нелокальный                                        |
    |------------|------------------------------------------------------------------------------------|----------------------------------------------------|
    | линейный   | \\(G^{\alpha \beta} =   \lambda^{\alpha \beta \gamma \delta} F\_{\gamma \delta}\\) | \\(G(x) = \int \lambda(x,s) \wedge F (s) \dd{s}\\) |
    | нелинейный | \\(G^{\alpha \beta} = \lambda (F\_{\gamma \delta})\\)                              | \\(G(x) = \int \lambda(x, F (s)) \dd{s}\\)         |


## <span class="section-num">3</span> Структура тензора проницаемостей {#структура-тензора-проницаемостей}


### <span class="section-num">3.1</span> Представление тензора проницаемостей в пространстве \\(\mathbb{R} ^{4}\\) {#представление-тензора-проницаемостей-в-пространстве-mathbb-r-4}

-   Тензор проницаемости \\(\lambda ^{\alpha \beta} \_{\gamma \delta} \\) представляет собой 4-тензор.
-   Будем считать, что отображение \\(\lambda : \Lambda^2 M \to \Lambda\_2 M\\) линейное и локальное. Тогда его можно представить в следующем виде:

    \begin{equation}
    \label{eq:g\_lambda\_f}
    G^{\alpha \beta} =
    %\frac{1}{2}
    \lambda^{\alpha \beta \gamma \delta} F\_{\gamma \delta},
    \end{equation}

    здесь \\(\lambda^{\alpha \beta \gamma \delta}\\) --- тензор проницаемостей, содержащий информацию как об диэлектрической и магнитной проницаемостях, так и об электромагнитной связи [<a href="#citeproc_bib_item_4">4</a>–<a href="#citeproc_bib_item_7">7</a>].
-   Видно, что \\(\lambda^{\alpha \beta \gamma \delta}\\) имеет следующую симметрию:
    \\[\lambda^{\alpha \beta \gamma \delta} = \lambda^{[\alpha \beta] [\gamma \delta]}\\]
-   Для уточнения симметрии, тензор \\(\lambda^{\alpha \beta \gamma \delta}\\) можно представить в следующем виде:
    \\[\lambda^{\alpha \beta \gamma \delta} = {}^{(1)} \lambda^{\alpha \beta \gamma \delta} + {}^{(2)} \lambda^{\alpha \beta \gamma \delta} + {}^{(3)} \lambda^{\alpha \beta \gamma \delta}.\\]
-   Компоненты имеют следующую симметрию:
    \\[
        {}^{(1)} \lambda^{\alpha \beta \gamma \delta} = \lambda^{([\alpha \beta] [\gamma \delta])}, \quad
        {}^{(2)} \lambda^{\alpha \beta \gamma \delta} = \lambda^{[[\alpha \beta] [\gamma \delta]]}, \quad
        {}^{(3)} \lambda^{\alpha \beta \gamma \delta} = \lambda^{[\alpha \beta \gamma \delta]}.
     \\]
-   Очевидно, что \\(\lambda^{\alpha \beta \gamma \delta}\\) имеет 36 независимых компонент, \\({}^{(1)}\lambda^{\alpha \beta \gamma \delta}\\) имеет 20 независимых компонент (основная часть, _principal part_), \\({}^{(2)}\lambda^{\alpha \beta \gamma \delta}\\) имеет 15 независимых компонент (_skewon_), \\({}^{(3)}\lambda^{\alpha \beta \gamma \delta}\\) имеет 1 независимую компоненту (_axion_).
-   Будем рассматривать только часть \\({}^{(1)}\lambda^{\alpha \beta \gamma \delta}\\).
-   Запишем материальные уравнения:

    \begin{equation}
    \label{eq:constraint}
      \begin{cases}
        D^{i} &= \varepsilon^{i j} E\_{j} + {}^{(1)}\gamma^{i}\_{j} B^{j},
        \\\\
        H\_{i} &= \qty(\mu^{-1})\_{i j} B^{j} + {}^{(2)}\gamma^{j}\_{i} E\_{j},
      \end{cases}
      \end{equation}

    где \\(\varepsilon^{i j}\\) и \\(\mu^{i j}\\) --- тензоры диэлектрической и магнитной проницаемостей, \\({}^{(1)}\gamma^{i}\_{j}\\) и \\({}^{(2)}\gamma^{i}\_{j}\\) --- перекрёстные члены.
-   Учитывая структуру тензоров \\(F\_{\alpha \beta}\\) и \\(G^{\alpha \beta}\\), а также уравнения связи, запишем:

    \begin{equation}
    \label{eq:f-g\_lambda}
    \begin{gathered}
      F\_{\crd{0}\crd{i}} = E\_{\crd{i}}, \quad
      G^{\crd{0}\crd{i}} = - D^{\crd{i}},
      \\\\
      G^{\crd{i}\crd{j}} = - e^{\crd{i} \crd{j} \crd{k}}
      H\_{\crd{k}},
      \quad
      F\_{\crd{i} \crd{j}}
       = - e\_{\crd{i} \crd{j} \crd{k}}
      B^{\crd{k}}.
      \end{gathered}
      \end{equation}
-   \\(e \_{ijk}\\) есть альтернирующий тензор.


### <span class="section-num">3.2</span> Представление тензора проницаемостей в пространствах \\(A \_{2} (\mathbb{R} ^{4})\\)  и \\(A ^{2} (\mathbb{R} ^{4\*})\\) {#представление-тензора-проницаемостей-в-пространствах-a-2--mathbb-r-4--и-a-2--mathbb-r-4}

-   Будем рассматривать векторные пространства \\(A ^{2} (\mathbb{R}^{4\*})\\) и \\(A \_{2} (\mathbb{R}^4)\\) как типичные слои расслоений \\(\Lambda ^{2} M\\) и \\(\Lambda \_{2} M\\).
-   Для его представления используем известный трюк перехода в шестимерное пространство.
-   Базис \\(A \_{2} (\mathbb{R}^4)\\) состоит имеет вид \\(\zeta \_{I}, I=1,\ldots,6 \\).
-   Базис \\(A ^{2} (\mathbb{R}^{4\*})\\) состоит имеет вид \\(\zeta ^{I}, I=1,\ldots,6 \\).
-   Пусть \\(\delta \_{\mu}, \mu = 0,\ldots,3\\) есть базис в \\(\mathbb{R}^{4}\\), \\(\delta ^{\mu}, \mu = 0,\ldots,3\\) есть базис в \\(\mathbb{R} ^{4\*}\\).
-   Определим базис  \\(\zeta \_{I}\\) в \\(A \_{2} (\mathbb{R}^4)\\):

    \begin{equation}
    \label{eq:xi\_I}
    \zeta \_{i} = \delta \_{0} \wedge \delta \_{i}, \quad \zeta \_{i+3} = \frac{1}{2} \varepsilon \_{ijk} \delta \_{j} \wedge \delta \_{k}, \quad i,j,k = 1,\ldots,3.
    \end{equation}

-   Определим базис  \\(\zeta ^{I}\\) в \\(A ^{2} (\mathbb{R} ^{4\*})\\):

    \begin{equation}
    \label{eq:xi^I}
    \zeta ^{i} = \delta ^{0} \wedge \delta ^{i}, \quad \zeta ^{i+3} = \frac{1}{2} \varepsilon ^{ijk} \delta ^{j} \wedge \delta ^{k}, \quad i,j,k = 1,\ldots,3.
    \end{equation}
-   В этом базисе можно представить напряжённость электромагнитного поля \\(F\\) следующим образом:

    \begin{equation}
    \label{eq:FasVector}
    F = E \_{i} \zeta ^{i} + B \_{i} \zeta ^{i+3}.
    \end{equation}
-   Разобъём тензор \\(\lambda ^{IJ}\\):
    \\[\lambda ^{I J} = {}^{(1)} \lambda ^{I J} + {}^{(2)} \lambda ^{I J} + {}^{(3)} \lambda ^{I J}.\\]
-   Компоненты имеют следующую симметрию:
    \\[
        {}^{(1)} \lambda ^{I J} = \lambda ^{(I J)} - \lambda ^{K} \_{K} \tilde{I} ^{I J}, \quad
        {}^{(2)} \lambda ^{I J} = \lambda ^{[I J]}, \quad
        {}^{(3)} \lambda ^{I J} = \lambda ^{K} \_{K} \tilde{I} ^{I J}, \quad \tilde{I} := \mqty(\admat[0]{I ^{ij},I ^{ij}}).
     \\]
-   Распишем основную часть тензора проницаемостей:

    \begin{equation}
    \label{eq:lambda1IJ-as-matrix}
    {}^{(1)} \lambda ^{I J} = \mqty(-\varepsilon ^{ij} & {}^{(1)}\gamma^{i}\_{j}  \\\ {}^{(2)}\gamma^{j}\_{i}  & \tilde{\mu} \_{i j} ), \quad \tilde{\mu} \_{i j} := \qty(\mu^{-1})\_{i j}.
    \end{equation}
-   Далее в этой статье будем опускать индекс у основной части тензора проницаемостей.


## <span class="section-num">4</span> Риманова геометризация уравнений Максвелла {#риманова-геометризация-уравнений-максвелла}

-   Будем считать, что расслоение имеет структуру риманового многообразия.
-   Мы можем ввести на многообразии риманову метрику, которая:
    -   симметрична: \\(g \_{\alpha\beta} := g \_{(\alpha\beta)}\\);
    -   метрика согласована со связностью: \\(\nabla \_{\alpha} g ^{\alpha\beta} := 0\\);
    -   это эквивалентно тому, что мы используем связность Леви--Чевиты.
-   Введём эффективную метрику на базе расслоения \\(g\_{\alpha \beta}\\).
-   Метрика индуцируется на слои.
-   Запишем лагранжиан электромагнитного поля в виде лагранжиана Янга--Миллса:
    \\[
      L = - \frac{1}{16 \pi c} G ^{\alpha\beta} F\_{\alpha \beta}  - \frac{1}{c^2}
      A\_{\alpha} j^{\alpha} \sqrt{-g}.
      \\]
-   Или, расписав тензор \\(G ^{\alpha\beta}\\):
    \\[L = - \frac{1}{16 \pi c} g^{\alpha \gamma} g^{\beta \delta}
      F\_{\alpha \beta} F\_{\gamma \delta} \sqrt{-g} - \frac{1}{c^2}
      A\_{\alpha} j^{\alpha} \sqrt{-g}.\\]

-   Построим тензор \\(\lambda^{\alpha \beta \gamma \delta}\\) следующим образом:

    \begin{equation}
    \label{eq:lambda-geom-tamm}
    \lambda^{\alpha \beta \gamma \delta} =
    \sqrt{-g} g^{\alpha \beta} g^{\gamma \delta} =
    \frac{\sqrt{-g}}{2}
    \qty(
    g^{\alpha \gamma} g^{\beta \delta} +
    g^{\alpha \delta} g^{\beta \gamma}
    )
    +
    \frac{\sqrt{-g}}{2}
    \qty(
    g^{\alpha \gamma} g^{\beta \delta} -
    g^{\alpha \delta} g^{\beta \gamma}
    ).
    \end{equation}

-   Тогда материальные уравнения примут следующий вид (из симметрийных соображений):
    \\[
      G^{\alpha \beta} =
      \frac{\sqrt{-g}}{2}
      \qty(
      g^{\alpha \gamma} g^{\beta \delta} -
      g^{\alpha \delta} g^{\beta \gamma}
      )
      F\_{\gamma \delta}.
      \\]

-   Распишем по компонентам, получим:

     \begin{equation}
     \begin{gathered}
     G^{0\crd{i}} =
     \frac{\sqrt{-g}}{2}
     \qty(g^{00} g^{\crd{i}\crd{j}} – g^{0\crd{i}} g^{0\crd{j}} )
     F\_{0\crd{j}} +
     \frac{\sqrt{-g}}{2}
     \qty(g^{0\crd{j}} g^{\crd{i}\crd{k}} – g^{0\crd{k}} g^{\crd{i}\crd{j}} ) F\_{\crd{j}\crd{k}} ,
     \\\\
     G^{\crd{i}\crd{j}} =
     \frac{\sqrt{-g}}{2}
     \qty(
     g^{\crd{i}0} g^{\crd{j}\crd{k}} – g^{0\crd{j}} g^{\crd{i}\crd{k}}
     )
     F\_{0\crd{k}}
     +
     \frac{\sqrt{-g}}{2}
     \qty(
     g^{\crd{i}\crd{k}} g^{\crd{j}\crd{l}} – g^{\crd{i}\crd{l}} g^{\crd{j}\crd{k}}
     )
     F\_{\crd{k}\crd{l}}.
    \end{gathered}
    \end{equation}

-   Можно формально выписать выражение для диэлектрической проницаемости:

    \begin{equation}
    \label{eq:e\_ij}
    \varepsilon^{\crd{i} \crd{j}} =
    -
     \sqrt{-g}
     \qty(g^{00} g^{\crd{i}\crd{j}} – g^{0\crd{i}} g^{0\crd{j}} )
     .
     \end{equation}

-   Можно формально выписать выражение для магнитной проницаемости:

    \begin{equation}
    \label{eq:mu\_ij}
    (\mu^{-1})\_{\crd{i} \crd{j}} =
    \sqrt{-g}
    \varepsilon\_{\crd{m}\crd{n}\crd{i}} \varepsilon\_{\crd{k}\crd{l}\crd{j}} g^{\crd{n}\crd{k}} g^{\crd{m}\crd{l}}.
    \end{equation}

-   Таким образом геометризованные уравнения связи координатах имеют следующий вид:

    \begin{equation}
    \label{eq:geom-maxwell:tamm:decart}
    \begin{gathered}
      D^{i} = \varepsilon^{i j} E\_{j} + {}^{(1)}\gamma^{i}\_{j} B^{j},
      \\\\
      H\_{i} = (\mu^{-1})\_{i j} B^{j} + {}^{(2)}\gamma^{j}\_{i} E\_{j}, \\\\
      \varepsilon^{\crd{i} \crd{j}} =
      -
      \sqrt{-g}
      \qty(g^{00} g^{\crd{i}\crd{j}} – g^{0\crd{i}} g^{0\crd{j}} )
      ,
      \\\\
      (\mu^{-1})\_{\crd{i} \crd{j}} =
      \sqrt{-g}
      \varepsilon\_{\crd{m}\crd{n}\crd{i}} \varepsilon\_{\crd{k}\crd{l}\crd{j}} g^{\crd{n}\crd{k}} g^{\crd{m}\crd{l}},
      \\\\
      {}^{(1)}\gamma^{i}\_{j} = {}^{(2)}\gamma^{i}\_{j}
      =
      \sqrt{-g}
      \varepsilon\_{\crd{k}\crd{l}\crd{j}} g^{0\crd{k}} g^{\crd{i}\crd{l}}.
      \end{gathered}
     \end{equation}
-   Пусть пространство имеет вид:

    \begin{equation}
    \label{eq:R4-TxR3}
    \mathbb{R} ^{4} = \mathbb{R} ^{1} \times \mathbb{R} ^{3}.
    \end{equation}
-   Тогда в римановой геометризации при условии \\(g^{0 \crd{i}} = 0\\) выполняется равенство

    \begin{equation}
    \label{eq:tamm:e=m}
      \varepsilon^{\crd{i} \crd{j}} = \mu^{\crd{i} \crd{j}}
    .
    \end{equation}

-   Доказательство.
    -   Заметим, что \\(\Delta\_{\crd{i} \crd{j}} = \varepsilon\_{\crd{m}\crd{n}\crd{i}}
            \varepsilon\_{\crd{k}\crd{l}\crd{j}} g^{\crd{n}\crd{k}}
            g^{\crd{m}\crd{l}}\\) есть алгебраическое дополнение для \\(g^{\crd{i}\crd{j}}\\).
    -   Запишем
        \\[\varepsilon^{\crd{i} \crd{j}} (\mu^{-1})\_{\crd{i} \crd{p}} =  - \sqrt{-g} g^{00} g^{\crd{i}\crd{j}} \sqrt{-g} \varepsilon\_{\crd{m}\crd{n}\crd{i}} \varepsilon\_{\crd{k}\crd{l}\crd{p}} g^{\crd{n}\crd{k}} g^{\crd{m}\crd{l}} = g g^{00} \det{g^{\crd{k} \crd{l}}} \delta^{\crd{j}}\_{\crd{p}} = \delta^{\crd{j}}\_{\crd{p}}.\\]
    -   Отсюда следует, что \\(\varepsilon^{\crd{i} \crd{j}} = \mu^{\crd{i} \crd{j}}\\).
-   Геометризованный тензор проницаемостей имеет следующий вид:

    \begin{equation}
    \label{eq:lambda-geometric}
    \lambda ^{I J} = \mqty( -\varepsilon ^{ij} & {} ^{(1)} \gamma ^{i} \_{j} \\\  {} ^{(2)} \gamma ^{j} \_{i}  & \qty(\varepsilon ^{-1}) \_{ij} )
    \end{equation}


### <span class="section-num">4.1</span> Обсуждение {#обсуждение}

-   Ограничения:
    1.  Поскольку метрический тензор \\(g \_{ij}\\) имеет 10 компонент, то и геометризованный тензор проницаемостей не может иметь более 10 независимых компонент.
    2.  Учитывая уравнение связи, можно рассматривать только среды с единичным импедансом.
-   Впрочем, геометризованный вариант можно применить для приближения геометрической оптики, когда не используются отдельно диэлектрическая \\(\varepsilon ^{ij}\\) и магнитная \\(\mu \_{ij}\\) проницаемости.
-   Вместо этого в приближении геометрической оптики используют показатель преломления среды:

    \begin{equation}
    \label{eq:n-epsilon-mu}
    n ^{i} \_{j} = \sqrt{ \varepsilon ^{i} \_{k} \mu ^{k} \_{j}}.
    \end{equation}
-   В этом случае геометризованный тензор проницаемостей имеет следующий вид:

    \begin{equation}
    \label{eq:lambda-geometric}
    \lambda ^{I J} = \mqty( - \qty(\sqrt {n}) ^{ij} & {} ^{(1)} \gamma ^{i} \_{j} \\\  {} ^{(2)} \gamma ^{j} \_{i}  & \qty(\frac{1}{\sqrt{n}}) \_{ij} )
    \end{equation}


## <span class="section-num">5</span> Примеры сред {#примеры-сред}


### <span class="section-num">5.1</span> Линейные изотропные среды {#линейные-изотропные-среды}

-   Наиболее элементарными электромагнитными средами являются линейные изотропные среды, например классический вакуум.
-   Термин _изотропный_ относится к инвариантности относительно пространственных вращений в выбранной системе отсчёта. Поворот любой замкнутой системы как целого не изменяет её физических свойств.
-   В пространстве нет какого-то выделенного направления, относительно которого существует какая-либо особая симметрия. Все направления равноправны.
-   Электромагнитные свойства среды не зависят от направления.
-   Элементы тензора \\(\lambda ^{IJ}\\) имеют вид:

    \begin{equation}
    \label{eq:lambda-isotropic-elements}
    \varepsilon ^{ij} = \varepsilon (x ^{i}) \delta ^{ij}, \quad \tilde{\mu} \_{i j} := \qty(\mu ^{-1}(x ^{i})) \delta \_{i j}, \quad {}^{(1)}\gamma^{i}\_{j} =0, \quad {}^{(2)}\gamma^{j}\_{i} =0.
    \end{equation}
-   Запишем \\(\lambda ^{IJ}\\) в виде матрицы:

    \begin{equation}
    \label{eq:lambda-isotropic}
    \lambda ^{I J} = \mqty(\mqty{\dmat{, -\varepsilon(x ^{i}) \delta ^{ij},}} & \mqty{\dmat{,0,}} \\\  \mqty{\dmat{,0,}}  & \mqty{\dmat{, \mu ^{-1}(x ^{i}) \delta \_{ij},}} )
    \end{equation}
-   В данной случае матрица проницаемостей содержит только две независимых компоненты в лабораторной системе отсчёта.
-   Функция \\(\varepsilon (x ^{i})\\) называется диэлектрической проницаемостью среды.
-   Функция \\(\mu (x ^{i})\\) называется магнитной проницаемостью среды.
-   Когда эти функции постоянны в выбранной системе отсчёта, то и среду называют _однородной_.
-   Классический электромагнитный вакуум предполагается линейным, изотропным и однородным. Его диэлектрическая проницаемость (в системе СИ) обозначается через \\(\varepsilon \_{0}\\), а магнитная проницаемость --- через \\(\mu \_{0}\\).


#### <span class="section-num">5.1.1</span> Случай геометрической оптики {#случай-геометрической-оптики}

-   Возможно применение геометризованного тензора проницаемостей в приближении геометрической оптики.
-   Запишем \\(\lambda ^{IJ}\\) для случая геометрической оптики:

    \begin{equation}
    \label{eq:lambda-isotropic-geom-optics}
    \lambda ^{I J} = \mqty(\mqty{\dmat{, -\sqrt{n(x ^{i})} \delta ^{ij}, }} & \mqty{\dmat{,0,}} \\\  \mqty{\dmat{,0,}}  & \mqty{\dmat{, \frac{1}{\sqrt{n(x ^{i})}} \delta \_{ij}, }} )
    \end{equation}
-   В данном случае матрица проницаемостей содержит только одну независимую компоненту.


### <span class="section-num">5.2</span> Линейные оптические среды {#линейные-оптические-среды}

-   Предполагается, что диэлектрическая проницаемость \\(\varepsilon ^{ij}\\) может быть неоднородной и (или) анизотропной.
-   Наиболее распространённая неоднородность: матричные компоненты являются кусочно-постоянными; они претерпевают скачкообразные разрывы на границах раздела разнородных сред.
-   Поскольку магнитной проницаемостью оптических сред пренебрегают, их принято считать диэлектрическими средами:

    \begin{equation}
    \label{eq:mu=1}
    \qty(\mu ^{-1}) \_{ij} = \delta \_{ij}.
    \end{equation}
-   Если диэлектрическая проницаемость \\(\varepsilon ^{ij}\\) анизотропна (но симметрична), то можно определить главный репер, в котором она становится диагональной матрицей:

    \begin{equation}
    \label{eq:epsilon-diag}
    \varepsilon ^{ij} := \mathrm{diag} (\varepsilon \_{x}, \varepsilon \_{y}, \varepsilon \_{z}).
    \end{equation}
-   Диагональные элементы, являющиеся главными диэлектрическими проницаемостями, являются собственными значениями матрицы

    \begin{equation}
    \label{eq:epsilon-matrix}
    \varepsilon ^{i} \_{j} = \varepsilon ^{i k} g \_{jk}
    \end{equation}
-   Поскольку матрица \\(\varepsilon ^{ij}\\) симметрична, собственные значения существуют и действительны, а собственные векторы ортогональны.
-   Варианты собственных значений:
    -   Когда все собственные значения равны, среду называют изотропной.
    -   Когда два собственных значения равны, а третье отлично от них, среда называется одноосной анизотропной.
    -   Когда все три собственных значения неравны, среда называется двуосной анизотропной.
-   В более общем случае магнитная проницаемость не единична:

    \begin{equation}
    \label{eq:mu-diag}
    \qty(\mu ^{-1}) \_{ij} = \mathrm{diag} ((\mu ^{-1}) \_{x}, (\mu ^{-1}) \_{y}, (\mu ^{-1}) \_{z}).
    \end{equation}
-   Запишем \\(\lambda ^{IJ}\\) в виде матрицы:

    \begin{equation}
    \label{eq:lambda-linear-optical}
    \lambda ^{I J} = \mqty(\mqty{\dmat{-\varepsilon \_{x}(x ^{i}), -\varepsilon \_{y}(x ^{i}), -\varepsilon \_{z}(x ^{i})}} & \mqty{\dmat{,0,}} \\\  \mqty{\dmat{,0,}}  & \mqty{\dmat{\mu ^{-1} \_{x}(x ^{i}), \mu ^{-1} \_{y}(x ^{i}), \mu ^{-1} \_{z}(x ^{i})}} )
    \end{equation}


#### <span class="section-num">5.2.1</span> Случай геометрической оптики {#случай-геометрической-оптики}

-   Возможно применение геометризованного тензора проницаемостей в приближении геометрической оптики.
-   Запишем \\(\lambda ^{IJ}\\) для случая геометрической оптики:

    \begin{equation}
    \label{eq:lambda-isotropic-geom-optics}
    \lambda ^{I J} = \mqty(\mqty{\dmat{-\sqrt{n \_{x}(x ^{i})}, -\sqrt{n \_{y}(x ^{i})}, -\sqrt{n \_{z}(x ^{i})}}} & \mqty{\dmat{,0,}} \\\  \mqty{\dmat{,0,}}  & \mqty{\dmat{\frac{1}{\sqrt{n \_{x}(x ^{i})}}, \frac{1}{\sqrt{n \_{y}(x ^{i})}}, \frac{1}{\sqrt{n \_{z}(x ^{i})}}}} )
    \end{equation}
-   В данном случае матрица проницаемостей содержит три независимых компонент.


### <span class="section-num">5.3</span> Биизотропные среды {#биизотропные-среды}

-   Особые свойства этих сред обусловлены связью между электрическими и магнитными полями, которая может быть описана некоторыми определяющими соотношениями.
-   Биизотропные среды могут изменять поляризацию света либо при преломлении, либо при пропускании [<a href="#citeproc_bib_item_8">8</a>].
-   Эти среды подобны изотропным средам, однако перекрёстные члены не равны нулю.
-   Уравнения связи имеют следующий вид:

    \begin{equation}
    \label{eq:maxwell:bi-isotropic}
    \begin{aligned}
      D^{i} & = \varepsilon g ^{i j} E\_{j} + \gamma g^{i}\_{j} B^{j},
      \\\\
      H\_{i} & = (\mu^{-1}) g\_{i j} B^{j} + \gamma g^{j}\_{i} E\_{j}.
      \end{aligned}
     \end{equation}
-   Элементы тензора \\(\lambda ^{IJ}\\) имеют вид:

    \begin{equation}
    \label{eq:lambda-bi-isotropic-elements}
    \varepsilon ^{ij} = \varepsilon (x ^{i}) g ^{ij}, \quad \qty(\mu ^{-1}) \_{i j} := \qty(\mu ^{-1}(x ^{i})) g \_{i j}, \quad {}^{(1)}\gamma^{i}\_{j} = \gamma (x ^{i}) g ^{i} \_{j}, \quad {}^{(2)}\gamma^{j}\_{i} = \gamma (x ^{i}) g ^{j} \_{i}.
    \end{equation}
-   Запишем \\(\lambda ^{IJ}\\) для биизотропной среды в виде матрицы:

    \begin{equation}
    \label{eq:lambda-bi-isotropic}
    \lambda ^{I J} = \mqty(\mqty{\dmat{,-\varepsilon(x ^{i}) g ^{ij},}} & \mqty{\dmat{,\gamma (x ^{i}) g ^{i} \_{j},}} \\\  \mqty{\dmat{,\gamma (x ^{i}) g ^{j} \_{i},}}  & \mqty{\dmat{,\mu ^{-1}(x ^{i}) g \_{ij},}} )
    \end{equation}


#### <span class="section-num">5.3.1</span> Случай геометрической оптики {#случай-геометрической-оптики}

-   Запишем \\(\lambda ^{IJ}\\) для биизотропной среды для случая геометрической оптики:

    \begin{equation}
    \label{eq:lambda-biisotropic-geom-optics}
    \lambda ^{I J} = \mqty(\mqty{\dmat{,-\sqrt{n(x ^{i})} g ^{ij},}} & \mqty{\dmat{,\gamma (x ^{i}) g ^{i} \_{j},}} \\\  \mqty{\dmat{,\gamma (x ^{i}) g ^{j} \_{i},}}  & \mqty{\dmat{, n ^{-1/2}(x ^{i}) g \_{ij},}} )
    \end{equation}
-   В данном случае матрица проницаемостей содержит две независимые компоненты.


### <span class="section-num">5.4</span> Бианизотропные среды {#бианизотропные-среды}

-   В бианизотропных средах диэлектрическая проницаемость, магнитная проницаемость и коэффициент связи представляют собой полные тензоры.
-   Уравнения связи имеют следующий вид:

    \begin{equation}
    \label{eq:maxwell:bi-anisotropic}
    \begin{aligned}
      D^{i} & = \varepsilon^{i j} E\_{j} + {}^{(1)}\gamma^{i}\_{j} B^{j},
      \\\\
      H\_{i} & = (\mu^{-1})\_{i j} B^{j} + {}^{(2)}\gamma^{j}\_{i} E\_{j}.
      \end{aligned}
     \end{equation}
-   Элементы тензора \\(\lambda ^{IJ}\\) имеют вид:

    \begin{equation}
    \label{eq:lambda-bi-anisotropic-elements}
    \varepsilon ^{ij} := \varepsilon ^{ij} (x ^{i}), \quad \qty(\mu ^{-1}) \_{i j} := \qty(\mu ^{-1}(x ^{i})) \_{i j} , \quad {}^{(1)}\gamma^{i}\_{j} = \gamma ^{i} \_{j} (x ^{i}) , \quad {}^{(2)}\gamma^{j}\_{i} = \gamma ^{j} \_{i} (x ^{i}).
    \end{equation}
-   Запишем \\(\lambda ^{IJ}\\) для биизотропной среды в виде матрицы:

    \begin{equation}
    \label{eq:lambda-bi-anisotropic}
    \lambda ^{I J} = \mqty(\mqty{\dmat{,-\varepsilon ^{ij}(x ^{i}) ,}} & \mqty{\dmat{,\gamma ^{i} \_{j} (x ^{i}) ,}} \\\  \mqty{\dmat{,\gamma ^{j} \_{i} (x ^{i}),}}  & \mqty{\dmat{,(\mu ^{-1})  \_{ij}(x ^{i}),}} )
    \end{equation}


#### <span class="section-num">5.4.1</span> Случай геометрической оптики {#случай-геометрической-оптики}

-   Запишем \\(\lambda ^{IJ}\\) для бианизотропной среды для случая геометрической оптики:

    \begin{equation}
    \label{eq:lambda-biisotropic-geom-optics}
    \lambda ^{I J} = \mqty(\mqty{\dmat{,-\qty(\sqrt{n}) ^{ij} (x ^{i}),}} & \mqty{\dmat{,\gamma ^{i} \_{j} (x ^{i}),}} \\\  \mqty{\dmat{,\gamma ^{j} \_{i} (x ^{i}) ,}}  & \mqty{\dmat{,\qty(n ^{-1/2}) \_{ij} (x ^{i}),}} )
    \end{equation}
-   В данном случае матрица проницаемостей содержит двадцать независимых компонент.


## <span class="section-num">6</span> Обсуждение результатов {#обсуждение-результатов}

-   В большинстве практических случаем число необходимых компонент менее десяти.
-   Для случая бианизатропной среды количество компонент тензора проницаемости превышает десять компонент.


## <span class="section-num">7</span> Заключение {#заключение}

-   Геометризованная теория Максвелла в случае римановой геометризации требует, чтобы среда обладала единичным импедансом.
-   Данное ограничение представляется слишком сильным в общем случае.
-   Представляется, что геометризованная теория Максвелла в случае римановой геометризации не применима в случае полной теории Максвелла и в случае приближения волнового уравнения.
-   Геометризованная теория Максвелла в случае римановой геометризации применима в основном для случая приближения геометрической оптики.
-   Ограничением применения геометризованной теории Максвелла является количество свободных компонент в тензоре проницаемостей.
-   В практически используемых случаях количество компонент меньше десяти.

## Литература

<div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>1.	Korolkova A. V. <a href="https://doi.org/10.22363/2658-4670-2022-30-4-305-317">Constitutive tensor in the geometrized Maxwell theory</a> / A. V. Korolkova // Discrete and continuous models and applied computational science. – 2022. – Т. 30. – № 4. – Сс. 305–317.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>2.	Пенроуз Р. Спиноры и пространство-время: Два-спинорное исчисление и релятивистские поля : in 2 т. Т. 1. Спиноры и пространство-время / Р.  Пенроуз, В.  Риндлер. – М. : Мир, 1987. – 527 сс.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>3.	Сивухин Д. В. <a href="https://doi.org/10.3367/UFNr.0129.197910h.0335">О Международной системе физических величин</a> / Д. В. Сивухин // Успехи физических наук. – 1979. – Т. 129. – № 10. – Сс. 335–338.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>4.	Тамм И. Е. Кристаллооптика теории относительности в связи с геометрией биквадратичной формы / И. Е. Тамм // Журнал Русского физико-химического общества. Часть физическая. – 1925. – Т. 57. – № 3-4. – Сс. 209–240.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_5"></a>5.	Тамм И. Е. Электродинамика анизотропной среды в специальной теории относительности / И. Е. Тамм // Журнал Русского физико-химического общества. Часть физическая. – 1924. – Т. 56. – № 2-3. – Сс. 248–262.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_6"></a>6.	Мандельштам Л. И. Электродинамика анизотропных сред в специальной теории относительности / Л. И. Мандельштам, И. Е. Тамм // Собрание научных трудов : in 2 т. – М. : Наука, 1975. – Т. 1.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_7"></a>7.	Ландау Л. Д. Теоретическая физика: Электродинамика сплошных сред : in 10 т. Т. 8. Теоретическая физика / Л. Д.  Ландау, Е. М.  Лифшиц. – 4-е. – М. : Физматлит, 2003. – 656 сс.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_8"></a>8.	Bolioli S. <a href="https://doi.org/10.1007/978-94-011-5734-6_3">Bi-Isotropic and Bi-Anisotropic Media</a> / S. Bolioli // Advances in complex electromagnetic materials : Nato asi series / ред. A. Priou [и др.]. – Springer Netherlands, 1997. – Т. 28.</div>
</div>
