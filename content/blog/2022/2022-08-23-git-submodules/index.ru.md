---
title: "git submodules"
author: ["Dmitry S. Kulyabov"]
date: 2022-08-23T18:42:00+03:00
lastmod: 2023-09-28T16:19:00+03:00
tags: ["programming"]
categories: ["computer-science"]
draft: false
slug: "git-submodules"
---

Подмодули git.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


### <span class="section-num">1.1</span> Прагматика {#прагматика}

-   Нужно включить сторонний код в проект.
-   Простейший путь: скопировать код из git в свой проект.
-   Недостатки этого подхода:
    -   смешивание нескольких проектов в один;
    -   после обновления стороннего проекта придётся вручную обновлять код.
-   Общее правило в разработке программного обеспечения: держать отдельные вещи отдельно.
-   Преимущества подмодулей git:
    -   обеспечивается согласованный интерфейс для подключения стороннего кода.
-   Подмодули в git являются просто репозиториями git.
-   Подмодуль помещается в родительский репозиторий git.


## <span class="section-num">2</span> Операции с подмодулями {#операции-с-подмодулями}


### <span class="section-num">2.1</span> Добавление подмодуля {#добавление-подмодуля}

-   Для добавления нового подмодуля используется команду `git submodule add`:
    ```shell
    git submodule add https://github.com/chaconinc/DbConnector
    ```
-   Создаётся файл `.gitmodules`. Это конфигурационный файл, в котором хранится соответствие между URL проекта и локальным подкаталогом:
    ```ini
    [submodule "DbConnector"]
            path = DbConnector
            url = https://github.com/chaconinc/DbConnector
    ```


### <span class="section-num">2.2</span> Клонирование проекта с подмодулями {#клонирование-проекта-с-подмодулями}

-   Можно сначала склонировать проект, а потом склонировать подмодули.
-   Нужно выполнить команды:
    -   `git submodule init`: для инициализации локального конфигурационного файла;
    -   `git submodule update`: для получения всех данных этого проекта и извлечения соответствующего коммита, указанного в основном проекте.
-   Эти команды можно заменить одной: `git submodule update --init` или `git submodule update --init --recursive`.
-   Можно склонировать сразу с подмодулями, использую опцию `--recurse-submodules`:
    ```shell
    git clone --recurse-submodules https://github.com/chaconinc/MainProject
    ```


### <span class="section-num">2.3</span> Рекурсивное обновление подмодулей {#рекурсивное-обновление-подмодулей}

-   Обычно достаточно задать опцию `--recurse-submodules` при обновлении:
    ```shell
    git pull --recurse-submodules
    ```
-   В более сложных случаях для обновления подмодулей можно использовать следующие команды:
    ```shell
    git submodule init
    git submodule update
    git submodule foreach 'git fetch origin; git checkout $(git rev-parse --abbrev-ref HEAD); git reset --hard origin/$(git rev-parse --abbrev-ref HEAD); git submodule update --recursive; git clean -dfx'
    ```
-   При этом подмодули автоматически сразу устанавливается в `HEAD`.
