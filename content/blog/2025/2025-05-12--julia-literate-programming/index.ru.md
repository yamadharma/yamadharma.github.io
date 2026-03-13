---
title: "Julia. Литературное программирование"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-12T14:03:00+03:00
lastmod: 2025-05-15T10:57:00+03:00
tags: ["julia", "programming"]
categories: ["computer-science"]
draft: false
slug: "julia-literate-programming"
---

Julia. Литературное программирование.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Реализации {#реализации}


### <span class="section-num">1.1</span> Literate.jl {#literate-dot-jl}

-   Репозиторий: <https://github.com/fredrikekre/Literate.jl>
-   Документация: <https://fredrikekre.github.io/Literate.jl>
-   Позволяет генерировать Markdown-документы, Jupyter-ноутбуки и чистые скрипты из одного исходного файла с комментариями.
-   Интегрируется с Documenter.jl для автоматизации документации пакетов.
-   Поддерживает выполнение кода и вставку результатов.


### <span class="section-num">1.2</span> Weave.jl {#weave-dot-jl}

-   Репозиторий: <https://github.com/JunoLab/Weave.jl>
-   Документация: <https://weavejl.mpastell.com>
-   Генерирует научные отчёты в форматах LaTeX, HTML, Jupyter и других.
-   Выполняет код, встраивает результаты (текст, графики) в документ.
-   Поддерживает синтаксис Noweb и Markdown.


### <span class="section-num">1.3</span> Documenter.jl {#documenter-dot-jl}

-   Репозиторий: <https://github.com/JuliaDocs/Documenter.jl>
-   Документация: <https://documenter.juliadocs.org>


#### <span class="section-num">1.3.1</span> Documenter.jl + Entangled {#documenter-dot-jl-plus-entangled}

-   Связка для создания документации с поддержкой перекрёстных ссылок между блоками кода.
-   Entangled синхронизирует Markdown-файлы с исходным кодом, а Documenter.jl генерирует финальную документацию.
-   Подходит для сложных проектов.


### <span class="section-num">1.4</span> Entangled {#entangled}

-   Репозиторий: <https://entangled.github.io/>
-   Инструмент для отслеживания изменений в Markdown-файлах и автоматической генерации кода.
-   Поддерживает систему ссылок между блоками.
-   Работает с Pandoc и Documenter.jl.
-   Ресурсы:
    -   <https://forem.julialang.org/jhidding/literate-programming-using-documenterjl-and-entangled-3fmb>


### <span class="section-num">1.5</span> Jupyter Notebook/IJulia {#jupyter-notebook-ijulia}

-   Классический подход с интерактивными блокнотами, где код сочетается с Markdown-описаниями.
-   Позволяет визуализировать результаты вычислений.
-   Неудобен для автоматизации.


### <span class="section-num">1.6</span> Сравнение {#сравнение}

-   Literate.jl и Weave.jl фокусируются на преобразовании кода в документы с результатами.
-   Documenter.jl + Entangled подходит для проектов, где важна синхронизация кода и документации.
-   Jupyter идеален для интерактивных исследований, но требует ручного управления.
-   Literate.jl проста в интеграции с другими средствами.


## <span class="section-num">2</span> Связка Julia + Quarto {#связка-julia-plus-quarto}


### <span class="section-num">2.1</span> Literate.jl + QuartoFlavor {#literate-dot-jl-plus-quartoflavor}

-   Используйте `Literate.markdown` с `flavor = Literate.QuartoFlavor()`, чтобы конвертировать скрипты `.jl` в `.qmd` (Quarto Markdown).
-   В коде применяйте специальный синтаксис:
    ```julia
    # # Заголовок уровня 1 → станет # Заголовок уровня 1 в .qmd
    ##| echo: false → станет #| echo: false (параметры Quarto)
    ```
-   Шаги:
    -   Установите Quarto CLI и Jupyter.
    -   Сгенерируйте `.qmd` файл:
        ```julia
        Literate.markdown("script.jl", flavor=Literate.QuartoFlavor())
        ```

    -   Рендерите через Quarto:
        ```sh
        quarto render script.qmd --to html
        ```

-   Плюсы: Автоматизация, поддержка выполнения кода.


### <span class="section-num">2.2</span> Ручное создание .qmd с Julia-кодом {#ручное-создание-dot-qmd-с-julia-кодом}

-   Пишите `.qmd` файлы напрямую, вставляя блоки кода Julia:
    ````markdown
    ```{julia}
    #| echo: true
    x = 1 + 1
    println(x)
    ```
    ````

-   Рендерите через Quarto CLI.
-   Плюсы: Полный контроль над структурой документа.


### <span class="section-num">2.3</span> DocumenterQuarto.jl {#documenterquarto-dot-jl}

-   Плюсы: Подходит для пакетов, интеграция с CI.
-   Пакет объединяет Documenter.jl и Quarto для генерации сайтов документации.
-   Генерирует шаблоны Quarto-книг с автоматическим парсингом `@doc` из Julia.

-   Пример:
    ````julia
    using DocumenterQuarto
    DocumenterQuarto.generate()  # создает структуру Quarto-проекта
    ````
-   Репозиторий: <https://github.com/cadojo/DocumenterQuarto.jl>


### <span class="section-num">2.4</span> Jupyter + IJulia как бэкенд {#jupyter-plus-ijulia-как-бэкенд}

-   Quarto использует Jupyter-ядро для выполнения Julia-кода.
-   Настройте ядро через `kernel.json`, добавив параметры Julia (например, `--sysimage` для ускорения):
    ````js
    {
      "argv": ["julia", "--sysimage=myimage.so", "-i", ".../kernel.jl"]
    }
    ````

-   Плюсы: Интерактивность, кеширование результатов.


## <span class="section-num">3</span> Примеры порядка работ {#примеры-порядка-работ}


### <span class="section-num">3.1</span> Литературное программирование через Literate.jl {#литературное-программирование-через-literate-dot-jl}

-   Цель: Создать документ с исполняемыми примерами кода и пояснениями.
-   Создайте файл `example.jl` с комментариями в Markdown-стиле:
    ````julia
    # # Линейная регрессия
    # Пример реализации линейной регрессии.

    using LinearAlgebra

    # ## Генерация данных
    # Создаем синтетические данные:
    n = 100
    x = rand(n)
    y = 2x .+ 3 .+ 0.1randn(n)

    # ## Обучение модели
    # Решаем уравнение методом наименьших квадратов:
    X = [ones(n) x]
    β = X \ y
    println("Коэффициенты: ", β)
    ````

-   Конвертируйте в Markdown
    ````julia
    using Literate
    Literate.markdown("example.jl", "docs"; flavor=Literate.CommonMarkFlavor())
    ````

-   Рендерите через Documenter.jl:
    ````julia
    using Documenter
    makedocs(sitename="Пример регрессии")
    ````


### <span class="section-num">3.2</span> 2. Научные отчеты через Weave.jl {#2-dot-научные-отчеты-через-weave-dot-jl}

-   Цель: Сгенерировать PDF-отчет с графиками и вычислениями.

-   Создайте файл `report.jmd`:
    ````markdown
    # Анализ данных

    ```julia
    using Plots, CSV
    data = CSV.read("data.csv")
    plot(data.x, data.y, title="Зависимость Y от X")
    savefig("plot.png")
    ```

    ![](plot.png)
    ````

-   Запустите рендеринг:
    ````julia
    using Weave
    weave("report.jmd", doctype="md2pdf")
    ````

-   Результат: PDF-файл с графиком и кодом.


### <span class="section-num">3.3</span> 3. Интерактивная документация через Quarto + Julia {#3-dot-интерактивная-документация-через-quarto-plus-julia}

-   Цель: Создать интерактивную веб-страницу с исполняемыми блоками.
-   Создайте `analysis.qmd`:
    ````markdown
    ---
    title: "Анализ"
    jupyter: julia-1.9
    ---

    ```{julia}
    #| echo: true
    using DataFrames
    df = DataFrame(A=1:5, B=rand(5))
    ```

    ```{julia}
    #| echo: false
    println("Среднее B: ", mean(df.B))
    ```
    ````

-   Рендерите через Quarto:
    ````sh
    quarto render analysis.qmd --to html
    ````

-   Результат: HTML-страница с таблицей и скрытым выводом.


### <span class="section-num">3.4</span> 4. Jupyter + IJulia для исследований {#4-dot-jupyter-plus-ijulia-для-исследований}

-   Цель: Интерактивный анализ данных с визуализацией.
-   Установите ядро:
    ````julia
    using IJulia
    installkernel("Julia-1.11")
    ````

-   Создайте блокнот:
    ````julia
    # В Jupyter:
    using Plots
    plot(sin, 0, 2π, label="sin(x)")
    ````

-   Результат: Ноутбук с графиком и пояснениями.


## <span class="section-num">4</span> Сравнение подходов {#сравнение-подходов}

| Инструмент  | Форматы вывода      | Интерактивность    | Сложность |
|-------------|---------------------|--------------------|-----------|
| Literate.jl | HTML, Jupyter, PDF  | Нет                | Низкая    |
| Weave.jl    | HTML, PDF, Jupyter  | Нет                | Средняя   |
| Quarto      | HTML, PDF, RevealJS | Да (через браузер) | Средняя   |
| Jupyter     | .ipynb              | Да                 | Низкая    |

-   Для быстрого старта выбирайте Jupyter.
-   Для публикаций --- Quarto или Weave.jl.
-   Для документации пакетов --- Literate.jl + Documenter.
