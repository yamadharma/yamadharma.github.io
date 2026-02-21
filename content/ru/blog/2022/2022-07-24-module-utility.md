---
title: "Утилита module"
author: ["Dmitry S. Kulyabov"]
date: 2022-07-24T16:14:00+03:00
lastmod: 2023-09-29T19:48:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "module-utility"
---

Утилита управления переменными окружения.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Для удобства управления переменными окружения используется утилита `module`.
-   Каждому приложению соответствует конфигурационный файл (модуль), описывающий, как необходимо изменить переменные окружения для работы данного приложения.
-   Состояния модуля:
    -   загружен: необходимые значения добавляются к текущим переменным окружения;
    -   выгружен: настройки, соответствующие данному приложению, удаляются из переменных окружения.
-   Возможно независимо управлять несколькими модулями.
-   Существует несколько программ, реализующих утилиту `module`.


### <span class="section-num">1.1</span> Environment Modules {#environment-modules}

-   Сайт: <http://modules.sourceforge.net/>.
-   Докуменация на английском языке: <http://modules.sourceforge.net/man/module.html>.
-   Оригинальная утилита.
-   Создана примерно в 1990 году.


### <span class="section-num">1.2</span> Lmod {#lmod}

-   Сайт: <https://www.tacc.utexas.edu/research-development/tacc-projects/lmod>.
-   Докуменация на английском языке: <https://lmod.readthedocs.io/>.
-   Развитие _Environment Modules_.
    -   Поддерживает файлы конфигурации _Environment Modules_;
    -   совместимая на уровне параметров командной строки.


## <span class="section-num">2</span> Использование {#использование}


### <span class="section-num">2.1</span> Основные команды {#основные-команды}

-   `module avail` : вывести список доступных модулей;
-   `module list` : вывести список загруженных модулей;
-   `module load module1` : загрузить модуль module1 версии version;
-   `module unload module1` : выгрузить модуль module1 версии version;
-   `module swap module1 module2` : заменить загруженный модуль module1 на module2;
-   `module purge` : выгрузить все загруженные модули;
-   `module whatis module1` : показать информацию о модуле module1;
-   `module save [env_name]` : сохранить текущий набор загруженных модулей под именем env_name. Если не указывать имя, то набор будет перезаписан набор по умолчанию;
-   `module restore [env_name]` : загрузить набор сохранённых модулей;
-   `module describe [env_name]` : показать состав набора сохранённых модулей


### <span class="section-num">2.2</span> Примеры использования {#примеры-использования}

-   Просмотр загруженных модулей:
    ```shell
    $ module list
    Currently Loaded Modules:
    1) autotools    2) prun/1.2    3) gnu7/7.3.0    4) openmpi3/3.1.3    5) ohpc
    ```

-   Просмотр доступных модулей:
    ```shell
    $ module avail
    ​- /opt/ohpc/pub/modulefiles -
    CUDA/10.0                   cnpy_lib/1.0           hpcx/hpcx-stack
    Python/Anaconda_v10.2019    gnu7/7.3.0 (L)         hpcx/hpcx (D)
    EasyBuild/3.7.1             fltk/v1.3.5            hwloc/1.11.10
    Где:
    D: модуль, загружаемый по умолчанию;
    L: модуль, загруженный в настоящий момент.
    ```

-   Пример: выгрузка всех модулей и загрузка модулей CUDA/10.2 и Python/Anaconda_v10.2019:
    ```shell
    $ module purge
    $ module load CUDA/10.2 Python/Anaconda_v10.2019
    $ module list
    Currently Loaded Modules:
    1) CUDA/10.2    2) Python/Anaconda_v10.2019
    ```
-   Сохранение набора модулей по умолчанию:
    ```shell
    $ module save
    Saved current collection of modules to: "default"
    ```
