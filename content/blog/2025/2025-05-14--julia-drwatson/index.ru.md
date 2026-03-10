---
title: "Julia. Пакет DrWatson"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-14T19:59:00+03:00
lastmod: 2025-05-14T20:11:00+03:00
tags: ["research", "julia", "programming"]
categories: ["science", "computer-science"]
draft: false
slug: "julia-drwatson"
---

Julia. Пакет DrWatson.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   DrWatson.jl --- фреймворк для организации научных проектов в Julia.
-   Репозиторий: <https://github.com/JuliaDynamics/DrWatson.jl>
-   Документация: <https://juliadynamics.github.io/DrWatson.jl>

---


## <span class="section-num">2</span> Установка и инициализация {#установка-и-инициализация}

-   Установка в REPL:
    ```julia
    # Установка
    using Pkg
    Pkg.add("DrWatson")

    # Создание проекта
    using DrWatson
    initialize_project("MyProject"; authors=["Ваше Имя"], git=true)
    ```

-   Создаваемая структура:
    ```text
    MyProject/
    ├── Project.toml
    ├── Manifest.toml
    ├── data/
    │ ├── sims/      # Результаты симуляций
    │ ├── exp_raw/   # Сырые экспериментальные данные
    │ └── exp_pro/   Обработанные данные
    ├── scripts/     # Скрипты для анализа
    ├── src/         # Исходный код проекта
    └── _research/   # Черновики и временные файлы
    ```

-   Активирует окружение проекта, загружает зависимости:
    ```julia
    @quickactivate :MyProject  # Автоматически находит Project.toml
    ```


## <span class="section-num">3</span> Пути {#пути}

-   Стандартные пути:
    ```julia
    datadir()       # → "data"
    plotsdir()      # → "plots"
    projectdir()    # → Корень проекта
    scriptdir("analysis.jl") → "scripts/analysis.jl"
    ```


## <span class="section-num">4</span> Сохранение результатов {#сохранение-результатов}

```julia
using DrWatson: savename, @dict, safesave

params = @dict(α=0.1, β=2.0)  # Автоматическое именование
results = Dict(:data => rand(10))

# Сохранение с уникальным именем
filename = savename(params, "jld2")  # → "α=0.1_β=2.0.jld2"
safesave(datadir("sims", filename), results)
```


## <span class="section-num">5</span> Загрузка данных {#загрузка-данных}

```julia
using DrWatson: load, @strdict

# Поиск файлов по параметрам
filter = @strdict(α=0.1)
file = getlatest(filter, datadir("sims"))  # Последний файл с α=0.1
data = load(file)["data"]
```


## <span class="section-num">6</span> Воспроизводимость {#воспроизводимость}

```julia
gitdescribe()  # Возвращает текущий коммит Git → "v0.1.0-5-gf7a2d"
tag!(filename) # Добавляет хеш коммита к имени файла
```


## <span class="section-num">7</span> Пакетная обработка {#пакетная-обработка}

```julia
using BSON

# Генерация параметров
all_params = Dict(:α => [0.1, 0.5], :β => 1:5)

# Запуск симуляций
for params in dict_list(all_params)
    result = simulate(params)
    safesave(datadir("sims", savename(params, "bson")), result)
end
```


## <span class="section-num">8</span> Анализ результатов {#анализ-результатов}

```julia
using DataFrames

# Сбор всех данных в DataFrame
df = collect_results(datadir("sims"))
select!(df, :α, :β, :result)
```


## <span class="section-num">9</span> Интеграция с Literate.jl {#интеграция-с-literate-dot-jl}

-   [Julia. Литературное программирование]({{< relref "2025-05-12--julia-literate-programming" >}})

<!--listend-->

```julia
# scripts/generate_report.jl
using Literate

Literate.markdown("scripts/analysis.jl", "docs"; flavor = Literate.QuartoFlavor())
```


## <span class="section-num">10</span> Makefile {#makefile}

-   Сделаем Makefile:
    ```makefile
    .PHONY: report clean

    report:
        julia --project=. scripts/run_simulations.jl
        julia --project=. scripts/generate_report.jl
        quarto render docs/report.qmd

    clean:
        rm -rf data/sims/*
        rm -rf plots/*
    ```


## <span class="section-num">11</span> Практики {#практики}

-   Структура кода
    -   Храните многократно используемые функции в `src/` как модуль:
        ```julia
        # src/MyProject.jl
        module MyProject
        export simulate

        function simulate(params)
          # ...
        end
        end
        ```

-   Версионирование данных
    -   Используйте Git LFS для больших файлов в `data/`

-   Шаблоны проектов
    -   Создайте шаблон через PkgTemplates.jl:
        ```julia
        using PkgTemplates
        t = Template(;
          dir="~/Projects",
          julia=v"1.9",
          plugins=[DrWatsonPlugin()]
        )
        t("MyNewProject")
        ```

-   Отладка
    -   Используйте `produce_or_load` для кэширования результатов:
        ```julia
        produce_or_load(params, datadir("cache")) do p
          compute_expensive_operation(p)
        end
        ```


## <span class="section-num">12</span> Пример рабочего процесса {#пример-рабочего-процесса}

-   `initialize_project()` → Создает структуру
-   `quickactivate()` → Активирует окружение
-   Редактируем скрипты в `scripts/`
-   `savename()` + `safesave()` → Сохраняем результаты
-   `collect_results()` → Анализируем данные
-   Literate.jl → Генерируем отчет
-   Quarto → Рендерим финальный документ
