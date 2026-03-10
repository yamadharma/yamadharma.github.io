---
title: "Julia. DifferentialEquations.jl. Callback functions"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-02T14:04:00+03:00
lastmod: 2023-09-11T16:49:00+03:00
tags: ["julia", "programming"]
categories: ["computer-science"]
draft: false
slug: "julia-differentialequations-callback-functions"
---

Использование обратного вызова функций в пакете _DifferentialEquations.jl_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Типы обратных вызовов {#типы-обратных-вызовов}

-   `ContinuousCallback` (непрерывный): срабатывает, когда непрерывная функция условия достигает нуля. В других средствах реализуется как событие (event).
-   `DiscreteCallback` (дискретный): срабатывает, когда функция условия истинна.
-   `VectorContinuousCallback` (векторный): эквивалентен вектору непрерывных обратных вызовов. Позволяет указать, когда вызывается какой обратный вызов.


### <span class="section-num">1.1</span> Непрерывный обратный вызов {#непрерывный-обратный-вызов}

```julia
ContinuousCallback(condition,affect!,affect_neg!;
                   initialize = INITIALIZE_DEFAULT,
                   idxs = nothing,
                   rootfind=true,
                   save_positions=(true,true),
                   interp_points=10,
                   abstol=10eps(),reltol=0)
```


### <span class="section-num">1.2</span> Дискретный обратный вызов {#дискретный-обратный-вызов}

```julia
DiscreteCallback(condition,affect!;
                 initialize = INITIALIZE_DEFAULT,
                 save_positions=(true,true))
```

-   `condition` - функция `condition(u,t,integrator)`, определяющая, когда следует использовать обратный вызов. Обратный вызов инициируется, если условие истинно (`true`).
-   `affect!` - функция `affect!(integrator)`, которая может изменять текущее состояние интегратора.
-   `save_positions` - логический кортеж для сохранения до или после `affect!`. Это сохранение может происходить непосредственно до, после события, во время события. Оно не зависит от таких параметров, как `saveat`, `save_everystep` и т.д. (например, если `saveat = [1.0,2.0,3.0]`, то можно добавить точку сохранения в `2.1`, если условие верно). Чтобы прерывистые изменения обрабатывались правильно (без ошибок), необходимо установить `save_positions = (true, true)`.
-   `initialize` - функция `function(c,u,t,integrator)`, которая может использоваться для инициализации состояния обратного вызова `c`.


### <span class="section-num">1.3</span> Векторный непрерывный обратный вызов {#векторный-непрерывный-обратный-вызов}

```julia
VectorContinuousCallback(condition,affect!,affect_neg!,len;
                         initialize = INITIALIZE_DEFAULT,
                         idxs = nothing,
                         rootfind=true,
                         save_positions=(true,true),
                         interp_points=10,
                         abstol=10eps(),reltol=0)
```

```julia
VectorContinuousCallback(condition,affect!,len;
                   initialize = INITIALIZE_DEFAULT,
                   idxs = nothing,
                   rootfind=true,
                   save_positions=(true,true),
                   affect_neg! = affect!,
                   interp_points=10,
                   abstol=10eps(),reltol=0)
```


### <span class="section-num">1.4</span> Набор обратных вызовов {#набор-обратных-вызовов}

-   Несколько обратных вызовов можно объединить в один набор:

<!--listend-->

```julia
CallbackSet(cb1,cb2,cb3)
```

-   Можно передать столько угодно обратных вызовов. Когда решатели обнаруживают несколько обратных вызовов, применяются следующие правила:
-   `ContinuousCallbacks` и `VectorContinuousCallbacks` применяются перед `DiscreteCallbacks` (потому, что они часто реализуют обнаружение событий, которое возвращает временной шаг на величину, меньшему, чем `dt`).
-   Для `ContinuousCallbacks` и `VectorContinuousCallbacks` применяется только первый из них (шаг времени рассчитывается только по первому).
-   Затем по порядку применяются `DiscreteCallbacks`. Порядок имеет значение только для условий: если предыдущий обратный вызов изменяет функция таким образом, что следующий обратный вызов больше не считает условие истинным, он не будет применяться.


## <span class="section-num">2</span> Применение обратных вызовов {#применение-обратных-вызовов}

-   Обратный вызов передаётся решателю:

<!--listend-->

```julia
sol = solve(prob,alg,callback=cb)
```

-   Когда используется обратный вызов, режим сохранения по умолчанию отключён. Это потому, что в противном случае события дважды сохраняли бы одно из значений. Чтобы снова включить стандартное поведение при сохранении, необходимо, чтобы первое значение `save_positions` было истинным хотя бы для одного обратного вызова.
-   Общая проблема обратных вызовов заключается в том, что они вызывают большие изменения шага, поэтому после такого изменения может быть разумным уменьшить `dt`. Например, `set_proposed_dt!` используется для установки следующего шага и `terminate!` используется для остановки моделирования.


## <span class="section-num">3</span> Примеры {#примеры}
