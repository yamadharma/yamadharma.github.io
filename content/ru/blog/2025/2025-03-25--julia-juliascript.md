---
title: "Julia. JuliaScript"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-25T16:07:00+03:00
lastmod: 2025-03-25T16:41:00+03:00
tags: ["programming", "julia"]
categories: ["computer-science"]
draft: false
slug: "julia-juliascript"
---

Julia. JuliaScript.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/jolin-io/JuliaScript.jl>
-   Кэширование для быстрого запуска скриптов на Julia.


## <span class="section-num">2</span> Установка {#установка}

-   Нужно установить обёртку juliascript.
-   Если используется juliaup, то устанавливать надо в `~/.juliaup/bin/juliascript`.
-   Установим в `~/bin`:
    ```shell
    curl -o ~/bin/juliascript -fsSL https://raw.githubusercontent.com/jolin-io/JuliaScript.jl/main/bin/juliascript
    chmod +x ~/bin/juliascript
    ```
-   При первом запуске он установит пакет `JuliaScript.jl`.


## <span class="section-num">3</span> Прекомпиляция {#прекомпиляция}

-   Можно вручную создать sysimage, чтобы ещё больше повысить производительность:
    ```shell
    juliascript packagecompile yourscript.jl
    ```
-   Каждый последующий вызов `juliascript yourscript.jl` будет использовать полученный sysimage (пока вы не внесете изменения в скрипт).
-   Можно также установить переменную среды:
    ```shell
    JULIASCRIPT_PACKAGECOMPILE_ALWAYS=true
    ```
-   Тогда при запуске `juliascript myscript.jl` будет автоматически скомпилирован новый или изменённый пакет `myscript.jl`.
-   Создание системного образа выполняется в фоновом режиме.
