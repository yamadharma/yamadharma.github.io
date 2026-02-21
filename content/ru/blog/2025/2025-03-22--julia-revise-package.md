---
title: "Julia. Пакет Revise"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-22T19:29:00+03:00
lastmod: 2025-03-22T19:45:00+03:00
tags: ["programming", "julia", "research"]
categories: ["computer-science"]
draft: false
slug: "julia-revise-package"
---

Julia. Пакет Revise.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Пакет Julia, который позволяет автоматически перезагружать изменённые файлы модулей во время работы сессии.
-   Репозиторий: <https://github.com/timholy/Revise.jl>
-   Документация: <https://timholy.github.io/Revise.jl/stable>
-   Revise.jl работает лучше всего, когда вы разрабатываете код в интерактивном режиме, например, в Julia REPL или Jupyter Notebook.
-   Когда вы работаете над проектом и вносите изменения в файлы модулей, Revise.jl автоматически перезагрузит эти изменения, когда вы снова вызовете соответствующие функции или методы в REPL.
    -   Не нужно перезапускать сессию Julia каждый раз, когда вы вносите изменения в код.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Установка {#установка}

-   Установите пакет Revise.jl.
-   Установка в Julia REPL:
    ```julia
    using Pkg
    Pkg.add("Revise")
    ```


### <span class="section-num">2.2</span> Загрузка {#загрузка}

-   После установки пакета, загрузите его в вашу текущую сессию Julia:
    ```julia
    using Revise
    ```


### <span class="section-num">2.3</span> Отключение Revise.jl для модуля {#отключение-revise-dot-jl-для-модуля}

-   Если нужно отключить Revise.jl для определённого модуля или файла, можно использовать функцию `Revise.disable_revise(mod)`:
    ```julia
    Revise.disable_revise(MyModule)
    ```


### <span class="section-num">2.4</span> Автозагрузка {#автозагрузка}


#### <span class="section-num">2.4.1</span> Автозагрузка для REPL {#автозагрузка-для-repl}

-   Можно запускать Revise при каждом запуске julia, запустив его из файла `~/.julia/config/startup.jl`:
    ```julia
    try
        using Revise
    catch e
        @warn "Error initializing Revise" exception=(e, catch_backtrace())
    end
    ```
-   Можно добавить из командной строки:
    ```bash
    mkdir -p ~/.julia/config/ && tee -a  ~/.julia/config/startup.jl << END
    try
        @eval using Revise
    catch e
        @warn "Error initializing Revise" exception=(e, catch_backtrace())
    end
    END
    ```


#### <span class="section-num">2.4.2</span> Автозагрузка для Jupyter {#автозагрузка-для-jupyter}

-   Для загрузки Revise в IJulia запишите в файл `.julia/config/startup_ijulia.jl`:
    ```julia
    try
        @eval using Revise
    catch e
        @warn "Error initializing Revise" exception=(e, catch_backtrace())
    end
    ```
-   Можно добавить из командной строки:
    ```bash
    mkdir -p ~/.julia/config/ && tee -a  ~/.julia/config/startup_ijulia.jl << END
    try
        @eval using Revise
    catch e
        @warn "Error initializing Revise" exception=(e, catch_backtrace())
    end
    END
    ```
