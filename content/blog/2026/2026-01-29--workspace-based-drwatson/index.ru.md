---
title: "Рабочее пространство на основе DrWatson"
author: ["Dmitry S. Kulyabov"]
date: 2026-01-29T14:39:00+03:00
lastmod: 2026-01-29T22:08:00+03:00
draft: false
slug: "workspace-based-drwatson"
---

Рабочее пространство на основе DrWatson.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Подходы организации рабочего пространства {#подходы-организации-рабочего-пространства}

-   Подходы:
    -   один проект на все работы;
    -   отдельный проект на каждую работу.

| Критерий               | Один проект на все работы                                  | Отдельный проект на каждую работу                       |
|------------------------|------------------------------------------------------------|---------------------------------------------------------|
| Изоляция зависимостей  | Риск конфликтов версий пакетов между работами              | Полная изоляция, каждая работа автономна                |
| Управление пакетами    | Сложно, если работы требуют разных версий пакетов          | Просто, каждая работа имеет свой `Project.toml`         |
| Структура проекта      | Может стать громоздкой (много папок `data_*`, `scripts_*`) | Чисто, стандартная структура DrWatson                   |
| Общие утилиты          | Легко делиться общим кодом через `src/`                    | Приходится копировать или выносить в отдельный пакет    |
| Запуск всех работ      | Просто запустить последовательно                           | Нужно переключать активацию проектов                    |
| Версионность (Git)     | Один репозиторий для всего                                 | Отдельные репозитории или подмодули                     |
| Сдача на проверку      | Сложно выделить одну работу                                | Просто отправить папку проекта                          |
| Долгосрочная поддержка | Риск распухания проекта                                    | Легко архивировать, удалять, обновлять отдельные работы |

-   Выберите отдельные проекты, если:
    -   Лабораторные работы тематически разные
    -   Требуются разные версии пакетов
    -   Работы будут сдаваться по отдельности
    -   Планируете использовать работы в будущих курсах

-   Выберите единый проект, если:
    -   Все работы используют одинаковые пакеты
    -   Лабораторные последовательно развивают одну тему
    -   Много общего кода между работами
    -   Упрощенное управление --- приоритет


### <span class="section-num">1.1</span> Оптимальная стратегия {#оптимальная-стратегия}

-   Начинайте с отдельных проектов --- это безопаснее
-   Стандартизируйте структуру (одинаковые имена скриптов в каждой работе)
-   Создайте метапроект для удобного запуска всех работ
-   Выносите общий код в отдельный пакет (если появится много общего):
    ```julia
    # В каждом проекте
    using Pkg
    Pkg.add(url="https://github.com/yourname/CourseUtils.jl")
    using CourseUtils  # Общие функции для всех работ
    ```


## <span class="section-num">2</span> Гибридный подход "Метапроект + Изолированные подпроекты" {#гибридный-подход-метапроект-plus-изолированные-подпроекты}


### <span class="section-num">2.1</span> Структура {#структура}

```text
LabCourse_2024/                    # Метапроект (обычная папка, не DrWatson)
├── README.md                      # Описание всего курса
├── run_all_labs.jl               # Скрипт для запуска всех работ
├── common/                       # Общие утилиты (если нужны)
│   ├── plotting_utils.jl
│   └── data_helpers.jl
├── lab1_exponential_growth/      # Проект DrWatson для лабы 1
│   ├── Project.toml
│   ├── scripts/
│   ├── data/
│   └── ...
├── lab2_logistic_growth/         # Проект DrWatson для лабы 2
│   ├── Project.toml
│   ├── scripts/
│   └── ...
├── lab3_sir_model/              # Проект DrWatson для лабы 3
│   └── ...
└── submissions/                  # Готовые отчеты для сдачи
    ├── lab1_report.pdf
    ├── lab2_report.qmd
    └── ...
```


### <span class="section-num">2.2</span> Реализация гибридного подхода {#реализация-гибридного-подхода}


#### <span class="section-num">2.2.1</span> Создание метапроекта и первой лабораторной работы {#создание-метапроекта-и-первой-лабораторной-работы}

```julia
# В директории курса создаем первую лабораторную
cd("LabCourse_2024")

using DrWatson
initialize_project("lab1_exponential_growth"; authors="Ваше Имя")

# Аналогично для последующих работ
initialize_project("lab2_logistic_growth"; authors="Ваше Имя")
initialize_project("lab3_sir_model"; authors="Ваше Имя")
```


#### <span class="section-num">2.2.2</span> Скрипт для управления всеми работами `run_all_labs.jl` {#скрипт-для-управления-всеми-работами-run-all-labs-dot-jl}

```julia
# run_all_labs.jl - Запуск всех лабораторных работ последовательно

labs = [
    "lab1_exponential_growth",
    "lab2_logistic_growth",
    "lab3_sir_model"
]

println("Запуск всех лабораторных работ курса")
println("="^50)

for lab in labs
    println("\n▶ Запуск лабораторной работы: $lab")
    println("-"^40)

    # Переходим в директорию проекта
    cd(lab) do
        # Активируем окружение проекта
        using Pkg
        Pkg.activate(".")

        # Запускаем основной скрипт лабораторной
        try
            include("scripts/main.jl")
            println("✅ $lab завершена успешно")
        catch e
            println("❌ Ошибка в $lab: $e")
        end
    end
end

println("\n" * "="^50)
println("Все работы завершены!")
```


#### <span class="section-num">2.2.3</span> Стандартизация структуры каждой лабораторной {#стандартизация-структуры-каждой-лабораторной}

-   В каждой лабораторной создайте единую структуру.
-   Файл `scripts/main.jl` (точка входа для каждой работы):
    ```julia
    # scripts/main.jl - Главный скрипт лабораторной работы

    using DrWatson
    @quickactivate "lab1_exponential_growth"  # имя проекта

    println("="^50)
    println("ЛАБОРАТОРНАЯ РАБОТА 1: Экспоненциальный рост")
    println("="^50)

    # 1. Загрузка параметров
    include("scripts/01_parameters.jl")

    # 2. Запуск экспериментов
    include("scripts/02_run_experiments.jl")

    # 3. Анализ результатов
    include("scripts/03_analysis.jl")

    # 4. Генерация отчета
    include("scripts/04_generate_report.jl")

    println("Лабораторная работа завершена!")
    ```

-   Файл `scripts/01_parameters.jl` (единый формат для всех работ):
    ```julia
    # scripts/01_parameters.jl - Параметры лабораторной работы

    # Базовый эксперимент
    base_params = Dict(
        :experiment_name => "exponential_growth",
        :u0 => [1.0],
        :α => 0.3,
        :tspan => (0.0, 10.0),
        :solver => Tsit5(),
        :saveat => 0.1,
        :description => "Базовый экспоненциальный рост"
    )

    # Сетка для параметрического исследования
    param_grid = Dict(
        :u0 => [[1.0]],
        :α => [0.1, 0.3, 0.5, 0.8, 1.0],
        :tspan => [(0.0, 10.0)],
        :solver => [Tsit5()],
        :saveat => [0.1],
        :experiment_name => ["parametric_scan"]
    )

    println("Параметры загружены:")
    println("Базовый эксперимент: ", keys(base_params))
    println("Параметрическая сетка: ", keys(param_grid))
    ```


#### <span class="section-num">2.2.4</span> Шаблон для быстрого создания новых лабораторных {#шаблон-для-быстрого-создания-новых-лабораторных}

-   Создайте `template_make_new_lab.jl`:
    ```julia
    # template_make_new_lab.jl - Создание шаблона новой лабораторной

    function create_new_lab(lab_name, lab_number, description)
        # Создаем проект DrWatson
        initialize_project(lab_name; authors="Ваше Имя")

        # Стандартная структура папок
        mkdir(scriptsdir("utils"))
        mkdir(datadir("raw"))
        mkdir(datadir("processed"))
        mkdir(plotsdir("figures"))
        mkdir(projectdir("reports"))

        # Создаем стандартные файлы
        files_to_create = [
            ("scripts/main.jl", main_template(lab_name)),
            ("scripts/01_parameters.jl", params_template()),
            ("scripts/02_run_experiments.jl", experiments_template()),
            ("scripts/03_analysis.jl", analysis_template()),
            ("scripts/04_generate_report.jl", report_template()),
            ("README.md", readme_template(lab_name, lab_number, description))
        ]

        for (path, content) in files_to_create
            open(projectdir(path), "w") do f
                write(f, content)
            end
        end

        println("Создана новая лабораторная: $lab_name")
    end

    # (Здесь должны быть функции-шаблоны для каждого файла)

    # Использование:
    create_new_lab("lab4_predator_prey", 4, "Модель Лотки-Вольтерры")
    ```


### <span class="section-num">2.3</span> Пошаговое руководство для учебного курса {#пошаговое-руководство-для-учебного-курса}


#### <span class="section-num">2.3.1</span> Для студентов (сдача отдельных работ) {#для-студентов--сдача-отдельных-работ}

-   Для каждой новой лабораторной:
    ```shell
    # Создаем отдельный проект
    julia -e 'using DrWatson; initialize_project("lab2_logistic")'

    # Работаем внутри проекта
    cd lab2_logistic
    julia --project=. scripts/main.jl

    # Генерируем отчет для сдачи
    julia --project=. scripts/04_generate_report.jl
    ```

-   Сдача работы: просто заархивируйте папку проекта и отправьте преподавателю.


#### <span class="section-num">2.3.2</span> Для преподавателей (управление всем курсом) {#для-преподавателей--управление-всем-курсом}

-   Создайте репозиторий курса:
    ```shell
    Course_Computational_Modelling/
    ├── labs/               # Подмодули Git для каждой лабораторной
    │   ├── lab1/
    │   ├── lab2/
    │   └── ...
    ├── assignments/        # Формулировки заданий
    ├── solutions/          # Решения (отдельные проекты)
    └── run_course.jl       # Запуск всех демонстраций
    ```

-   Используйте Git подмодули для изоляции:
    ```shell
    git submodule add https://github.com/yourcourse/lab1.git labs/lab1
    git submodule add https://github.com/yourcourse/lab2.git labs/lab2
    ```


## <span class="section-num">3</span> Основные функции и использование {#основные-функции-и-использование}


### <span class="section-num">3.1</span> Активация проекта и пути {#активация-проекта-и-пути}

-   Каждый скрипт в проекте должен начинаться так:
    ```julia
    using DrWatson
    @quickactivate "MyProject"  # Активирует окружение проекта
    ```
-   После активации вы можете использовать функции для получения путей, которые будут работать независимо от местоположения проекта:
    -   `projectdir()`  — путь к корню проекта.

    -   `datadir("sims", "file.jld2")` → `".../MyProject/data/sims/file.jld2"` .

    -   `srcdir()`, `plotsdir()` — для папок `src` и `plots` .


### <span class="section-num">3.2</span> Организация параметров и запуск симуляций {#организация-параметров-и-запуск-симуляций}

-   Удобно хранить параметры в словарях.
-   Макрос `@strdict` создает словарь из существующих переменных, а `dict_list`  генерирует список словарей для перебора параметров:
    ```julia
    a, b = 1, 2
    params = @strdict a b  # Создает Dict("a"=>1, "b"=>2)

    # Генерация сетки параметров
    allparams = Dict("a" => [1, 2], "b" => [3, 4])
    dicts = dict_list(allparams)  # Вектор из 4 словарей
    ```


### <span class="section-num">3.3</span> Автоматическое сохранение и загрузка результатов {#автоматическое-сохранение-и-загрузка-результатов}

-   Функция `produce_or_load`  — ключевой инструмент.
-   Она проверяет, был ли уже рассчитан и сохранен результат для данного набора параметров.
-   Если файл существует, он загружается; если нет — запускается ваша функция расчета и результат сохраняется:
    ```julia
    function run_simulation(params::Dict)
        @unpack a, b = params
        result = a + b  # Ваши вычисления
        return merge(params, @strdict result)
    end

    for params in dicts
        data, filepath = produce_or_load(
            datadir("sims"),  # Папка для сохранения
            params,           # Параметры
            run_simulation,   # Функция-расчет
            prefix="exp"      # Префикс в имени файла
        )
    end
    ```

-   Имя файла автоматически формируется из параметров (например, `exp_a=1_b=3.jld2` ).


### <span class="section-num">3.4</span> Сбор результатов в таблицу {#сбор-результатов-в-таблицу}

-   После запуска симуляций вы можете легко собрать все результаты из папки в одну таблицу (DataFrame):
    ```julia
    using DataFrames
    df = collect_results(datadir("sims"))
    ```


## <span class="section-num">4</span> Создание проекта {#создание-проекта}

-   Запустите `julia` и установите DrWatson:
    ```julia
    using Pkg
    Pkg.add("DrWatson")
    ```
-   Чтобы начать, установите и инициализируйте проект:
    ```julia
    # Создайте структуру проекта в текущей директории
    using DrWatson
    initialize_project("project"; authors="Dmitry S. Kulyabov", git = false )
    ```
-   Эта команда создаст папку `project` со стандартной структурой: data/, plots/, scripts/, src/ и другие.
