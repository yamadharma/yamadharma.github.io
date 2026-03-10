---
title: "Julia. Утилита juliaup"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-18T19:49:00+03:00
lastmod: 2025-05-19T09:25:00+03:00
tags: ["julia", "programming"]
categories: ["computer-science"]
draft: false
slug: "julia-juliaup"
---

Julia. Утилита juliaup.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/JuliaLang/juliaup>
-   Кроссплатформенный установщик для языка программирования Julia.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Windows {#windows}

-   Winget (см. [Пакетный менеджер для Windows. WinGet]({{< relref "2023-10-01-package-manager-windows-winget" >}})):
    ```shell
    winget install --name Julia --id 9NJNWW8PVKMN -e -s msstore
    ```


### <span class="section-num">2.2</span> Unix {#unix}

-   Juliaup можно установить на Unix-подобных платформах, выполнив команду:
    ```shell
    curl -fsSL https://install.julialang.org | sh
    ```


### <span class="section-num">2.3</span> MacOS {#macos}

-   HomeBrew:
    ```shell
    brew install juliaup
    ```


### <span class="section-num">2.4</span> Linux {#linux}

-   Arch Linux:
    ```shell
    pacman -Su juliaup
    ```


## <span class="section-num">3</span> Основные операции {#основные-операции}


### <span class="section-num">3.1</span> Управление версиями {#управление-версиями}

-   Добавить версию:
    ```shell
    juliaup add 1.10   # Установка конкретной версии (например, 1.10)
    juliaup add lts    # Установка LTS-версии
    ```

-   Список доступных версий:
    ```shell
    juliaup list
    ```

-   Сменить версию по умолчанию:
    ```shell
    juliaup default 1.11   # По умолчанию будет запускаться Julia 1.11
    juliaup default release # Использовать последний стабильный релиз
    ```

-   Удаление версий:
    ```shell
    juliaup remove 1.5.3   # Удалить Julia 1.5.3
    ```


### <span class="section-num">3.2</span> Запуск Julia {#запуск-julia}

-   Стандартный запуск:
    ```shell
    julia   # Запуск версии, заданной по умолчанию
    ```

-   Запуск конкретной версии:
    ```shell
    julia +1.8   # Запуск Julia 1.8.x
    julia +nightly # Запуск ночной сборки
    ```


### <span class="section-num">3.3</span> Обновление {#обновление}

-   Обновить все версии:
    ```shell
    juliaup update
    ```

-   Обновить канал релиза:
    ```shell
    juliaup update release   # Обновить до последнего стабильного релиза
    ```


### <span class="section-num">3.4</span> Работа с проектами {#работа-с-проектами}

-   Привязать версию к каталогу:
    ```shell
    cd /path/to/project
    juliaup override set 1.6   # Для текущей папки использовать Julia 1.6
    ```

-   Удалить привязку:
    ```shell
    juliaup override unset
    ```


### <span class="section-num">3.5</span> Примеры использования {#примеры-использования}

-   Для CI/CD используйте GitHub Action [`julia-actions/install-juliaup`](https://github.com/julia-actions/install-juliaup).
-   Чтобы проверить текущую версию:
    ```shell
    julia --version
    ```

-   Пример рабочего процесса:
    ```shell
    juliaup add 1.10   # Установить Julia 1.10
    juliaup default 1.10
    juliaup override set lts --path ~/projects/legacy   # Для проекта legacy использовать LTS
    julia -e 'using Pkg; Pkg.test()'   # Запустить тесты в текущей версии
    ```
