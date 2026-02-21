---
title: "Рабочий процесс Gitflow"
author: ["Dmitry S. Kulyabov"]
date: 2021-04-18T20:14:00+03:00
lastmod: 2025-09-02T17:10:00+03:00
tags: ["programming", "education"]
categories: ["computer-science"]
draft: false
slug: "gitflow-workflow"
---

Рабочий процесс _Gitflow Workflow_. Будем описывать его с использованием пакета `git-flow`.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/petervanderdoes/gitflow-avh/>
-   Описание модели ветвления: <https://nvie.com/posts/a-successful-git-branching-model/>
-   Gitflow Workflow опубликована и популяризована Винсентом Дриссеном из компании vie.
-   Gitflow Workflow предполагает выстраивание строгой модели ветвления с учётом выпуска проекта.
-   Данная модель отлично подходит для организации рабочего процесса на основе релизов.
-   Работа по модели Gitflow включает создание отдельной ветки для исправлений ошибок в рабочей среде.
-   Последовательность действий при работе по модели Gitflow:
    -   Из ветки `master` создаётся ветка `develop`.
    -   Из ветки `develop` создаётся ветка `release`.
    -   Из ветки `develop` создаются ветки `feature`.
    -   Когда работа над веткой `feature` завершена, она сливается с веткой `develop`.
    -   Когда работа над веткой релиза `release` завершена, она сливается в ветки `develop` и `master`.
    -   Если в `master` обнаружена проблема, из `master` создаётся ветка `hotfix`.
    -   Когда работа над веткой исправления `hotfix` завершена, она сливается в ветки `develop` и `master`.


## <span class="section-num">2</span> Установка программного обеспечения {#установка-программного-обеспечения}

-   Для Windows используется пакетный менеджер Chocolatey.
-   Git-flow входит в состав пакета git.
    ```shell
    choco install git
    ```
-   Для MacOS используется пакетный менеджер [Homebrew](https://brew.sh/).
    ```shell
    brew install git-flow
    ```
-   Linux
    -   Gentoo
        ```shell
        emerge dev-vcs/git-flow
        ```
    -   Ubuntu
        ```shell
        apt-get install git-flow
        ```
    -   Centos
        -   Первоначально нужно установить репозиторий _epel_ (<https://fedoraproject.org/wiki/EPEL>):
            ```shell
            dnf install epel-release
            ```
        -   Затем, собственно, установить git-flow:
            ```shell
            dnf install gitflow
            ```
    -   Fedora
        -   Это программное обеспечение удалено из основного репозитория.
        -   Можно установить вручную или из коллекции репозиториев _Copr_.
        -   Установка из коллекции репозиториев _Copr_ (<https://copr.fedorainfracloud.org/coprs/elegos/gitflow/>):
            ```shell
            # Enable the copr repository
            dnf copr enable elegos/gitflow
            # Install gitflow
            dnf install gitflow
            ```
        -   Установка вручную:
            ```shell
            cd /tmp
            wget --no-check-certificate -q https://raw.github.com/petervanderdoes/gitflow/develop/contrib/gitflow-installer.sh
            chmod +x gitflow-installer.sh
            sudo ./gitflow-installer.sh install stable
            ```


## <span class="section-num">3</span> Поддержка завершения команды {#поддержка-завершения-команды}


### <span class="section-num">3.1</span> git-flow-completion {#git-flow-completion}

-   Репозиторий: <https://github.com/bobthecow/git-flow-completion>
-   Поддержка bash, zsh, fish.


### <span class="section-num">3.2</span> oh-my-fish/plugin-git-flow {#oh-my-fish-plugin-git-flow}

-   Репозиторий: <https://github.com/oh-my-fish/plugin-git-flow>
-   Завершение для fish в рамках фреймворка _Oh My Fish_.


## <span class="section-num">4</span> Процесс работы с Gitflow {#процесс-работы-с-gitflow}


### <span class="section-num">4.1</span> Основные ветки (master) и ветки разработки (develop) {#основные-ветки--master--и-ветки-разработки--develop}

Для фиксации истории проекта в рамках этого процесса вместо одной
ветки `master` используются две ветки. В ветке `master` хранится
официальная история релиза, а ветка `develop` предназначена для
объединения всех функций. Кроме того, для удобства рекомендуется
присваивать всем коммитам в ветке `master` номер версии.

При использовании библиотеки расширений `git-flow` нужно инициализировать структуру в существующем репозитории:

```shell
git flow init
```

Для github параметр `Version tag prefix` следует установить в `v`.

После этого проверьте, на какой ветке Вы находитесь:

```shell
git branch
```


### <span class="section-num">4.2</span> Функциональные ветки (feature) {#функциональные-ветки--feature}

-   Под каждую новую функцию должна быть отведена собственная ветка, которую можно отправлять в центральный репозиторий для создания резервной копии или совместной работы команды. Ветки `feature` создаются не на основе `master`, а на основе `develop`. Когда работа над функцией завершается, соответствующая ветка сливается обратно с веткой `develop`. Функции не следует отправлять напрямую в ветку `master`.

-   Как правило, ветки `feature` создаются на основе последней ветки `develop`.


#### <span class="section-num">4.2.1</span> Создание функциональной ветки {#создание-функциональной-ветки}

Создадим новую функциональную ветку:

```shell
git flow feature start feature_branch
```

-   Далее работаем как обычно.


#### <span class="section-num">4.2.2</span> Окончание работы с функциональной веткой {#окончание-работы-с-функциональной-веткой}

-   По завершении работы над функцией следует объединить ветку `feature_branch` с `develop`:

<!--listend-->

```shell
git flow feature finish feature_branch
```


### <span class="section-num">4.3</span> Ветки выпуска (release) {#ветки-выпуска--release}

-   Когда в ветке `develop` оказывается достаточно функций для выпуска, из ветки develop создаётся ветка `release`. Создание этой ветки запускает следующий цикл выпуска, и с этого момента новые функции добавить больше нельзя --- допускается лишь отладка, создание документации и решение других задач. Когда подготовка релиза завершается, ветка `release` сливается с `master` и ей присваивается номер версии. После нужно выполнить слияние с веткой `develop`, в которой с момента создания ветки релиза могли возникнуть изменения.

-   Благодаря тому, что для подготовки выпусков используется специальная ветка, одна команда может дорабатывать текущий выпуск, в то время как другая команда продолжает работу над функциями для следующего.

-   Создать новую ветку release можно с помощью следующей команды:

<!--listend-->

```shell
git flow release start 1.0.0
```

-   Для завершения работы на ветке `release` используются следующие команды:

<!--listend-->

```shell
git flow release finish 1.0.0
```


### <span class="section-num">4.4</span> Ветки исправления (hotfix) {#ветки-исправления--hotfix}

-   Ветки поддержки или ветки `hotfix` используются для быстрого внесения исправлений в рабочие релизы. Они создаются от ветки `master`. Это единственная ветка, которая должна быть создана непосредственно от master. Как только исправление завершено, ветку следует объединить с `master` и `develop`. Ветка `master` должна быть помечена обновленным номером версии.

-   Наличие специальной ветки для исправления ошибок позволяет команде решать проблемы, не прерывая остальную часть рабочего процесса и не ожидая следующего цикла релиза.

-   Ветку `hotfix` можно создать с помощью следующих команд:

<!--listend-->

```shell
git flow hotfix start hotfix_branch
```

-   По завершении работы ветка `hotfix` объединяется с `master` и `develop`:

<!--listend-->

```shell
git flow hotfix finish hotfix_branch
```
