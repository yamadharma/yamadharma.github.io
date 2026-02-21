---
title: "Рабочее пространство для лабораторной работы"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-16T12:51:00+03:00
lastmod: 2026-02-01T21:37:00+03:00
tags: ["education"]
categories: ["computer-science", "science"]
draft: false
slug: "workspace-laboratory-work"
---

При выполнении лабораторной работы следует придерживаться структуры рабочего пространства.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Основные идеи {#основные-идеи}

-   Стандартные соглашения об именах
-   Стандартное соглашение для путей к файлам
-   Стандартная настройка курса внутри шаблона курса


## <span class="section-num">2</span> Используемые стандарты и программные продукты {#используемые-стандарты-и-программные-продукты}

-   Стандарт Git Flow (см. [Варианты Git Workflow]({{< relref "2020-10-30-git-workflow" >}})).
-   Стандарт [Семантическое версионирование]({{< relref "2020-12-11-semantic-versioning" >}}).
-   Стандарт [Общепринятые коммиты]({{< relref "2020-12-11-conventional-commits" >}}).


## <span class="section-num">3</span> Дополнительное программное обеспечение {#дополнительное-программное-обеспечение}


### <span class="section-num">3.1</span> Средства разработки {#средства-разработки}


#### <span class="section-num">3.1.1</span> Fedora {#fedora}

-   Установите средства разработки:
    ```shell
    sudo dnf -y group install development-tools
    ```


### <span class="section-num">3.2</span> Quarto {#quarto}


#### <span class="section-num">3.2.1</span> Установка {#установка}

<!--list-separator-->

1.  Windows

    -   Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
        ```shell
        choco install quarto
        ```

<!--list-separator-->

2.  Linux

    <!--list-separator-->

    1.  Linux в общем

        -   Установка с помощью скрипта:
            ```shell
            #!/bin/bash

            ## Система
            TARGET=/opt
            TARGET_BIN=/usr/local/bin
            ## Домашний каталог
            # TARGET=~/opt
            # TARGET_BIN=~/.local/bin


            ## Получить тег
            TAG=`basename $(curl -sL -o /dev/null -w %{url_effective} https://github.com/quarto-dev/quarto-cli/releases/latest)`
            TAG=${TAG/v/}

            ## Скачать
            cd /tmp
            wget https://github.com/quarto-dev/quarto-cli/releases/download/v${TAG}/quarto-${TAG}-linux-amd64.tar.gz

            ## Распаковать
            mkdir -p ${TARGET}
            tar -C ${TARGET} -xvzf /tmp/quarto-${TAG}-linux-amd64.tar.gz
            mv ${TARGET}/quarto-${TAG} ${TARGET}/quarto

            ## Симлинк на исполняемый файл
            mkdir -p ${TARGET_BIN}
            ln -s ${TARGET}/quarto/bin/quarto ${TARGET_BIN}/quarto
            ```

    <!--list-separator-->

    2.  Gentoo

        -   Gentoo, репозиторий karma (см. [Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
            ```shell
            emerge quarto
            ```

    <!--list-separator-->

    3.  Arch

        -   Arch linux:
            ```shell
            pacman -S quarto-cli-bin
            ```
        -   Manjaro linux:
            ```shell
            pamac install quarto-cli-bin
            ```

    <!--list-separator-->

    4.  Fedora

        -   Установка из CORP:
            ```shell
            sudo dnf -y copr enable iucar/rstudio
            sudo dnf -y install quarto
            sudo dnf -y install libxcrypt-compat
            ```


### <span class="section-num">3.3</span> Общепринятые коммиты {#общепринятые-коммиты}


#### <span class="section-num">3.3.1</span> Установка Node.js {#установка-node-dot-js}

-   На Node.js базируется программное обеспечение для семантического версионирования и общепринятых коммитов.
-   Для управления пакетами лучше использовать `pnpm`, но можно и `yarn`.
-   Gentoo
    -   Node.js:
        ```shell
        emerge nodejs
        emerge yarn
        ```
    -   pnpm ставим из оверлея `guru` (см. [Gentoo. Дополнительные репозитории]({{< relref "2023-10-01-gentoo-additional-repositories" >}})):
        ```shell
        eselect repository enable guru
        emerge --sync guru
        emerge pnpm-bin
        ```
-   Ubuntu
    ```shell
    apt-get install nodejs
    apt-get install yarn
    apt-get install pnpm
    ```
-   Fedora
    ```shell
    sudo dnf -y install nodejs
    sudo dnf -y install yarn pnpm
    ```
-   Windows
    -   Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
        ```shell
        choco install nodejs
        choco install yarn
        choco install pnpm
        ```
-   MacOS
    ```shell
    brew install node
    ```


#### <span class="section-num">3.3.2</span> Настройка Node.js {#настройка-node-dot-js}

Для работы с Node.js добавим каталог с исполняемыми файлами, устанавливаемыми пакетным менеджером, в переменную `PATH`.

-   Linux
    -   `pnpm`
        -   Запустите:
            ```shell
            pnpm setup
            ```
        -   Перелогиньтесь, или выполните:
            ```shell
            source ~/.bashrc
            ```
    -   `yarn`
        -   В файле `~/.bashrc` добавьте к переменной `PATH`:
            ```conf-unix
            PATH=~/.yarn/bin:$PATH
            ```


#### <span class="section-num">3.3.3</span> Установка git-flow {#установка-git-flow}

-   Linux
    -   Gentoo
        ```shell
        emerge dev-vcs/git-flow
        ```
    -   Ubuntu
        ```shell
        apt-get install git-flow
        ```
    -   Fedora
        -   Устанавливается из COPR:
            ```shell
            sudo dnf -y copr enable elegos/gitflow
            sudo dnf install gitflow
            ```

-   Windows
    Git-flow входит в состав пакета git.
    ```shell
    choco install git
    ```
-   MacOS
    ```shell
    brew install git-flow
    ```


#### <span class="section-num">3.3.4</span> Общепринятые коммиты {#общепринятые-коммиты}

<!--list-separator-->

1.  commitizen

    -   Данная программа используется для помощи в форматировании коммитов.
        -   pnpm:
            ```shell
            pnpm add -g commitizen
            ```
        -   yarn:
            ```shell
            yarn global add commitizen
            ```
    -   При этом устанавливается скрипт `git-cz`, который мы и будем использовать для коммитов.

<!--list-separator-->

2.  standard-version

    -   Данная программа автоматизирует изменение номера версии.
        -   pnpm:
            ```shell
            pnpm add -g standard-version
            ```
        -   yarn:
            ```shell
            yarn global add standard-version
            ```


## <span class="section-num">4</span> Общие правила {#общие-правила}

-   Для именования каталогов и файлов будем использовать соглашение Denote (см. [Denote. Соглашение об именовании]({{< relref "2025-01-03--denote-naming-convention" >}})).
-   Рабочее пространство по предмету располагается в следующей иерархии:
    ```bash
    ~/work/study/
    └── <учебный год>/
        └── <учебный год>==<код предмета>/
    ```

-   Например, для 2025-2026 учебного года (второй семестр) и предмета «Операционные системы» (код предмета `os-intro`) структура каталогов примет следующий вид:
    ```bash
    ~/work/study/
    └── 2026-1/
        └── 2026-1==os-intro/
    ```
-   Название проекта на хостинге git имеет вид:
    ```text
    <учебный год>--study--<код предмета>
    ```
-   Например, для 2025-2026 учебного года и предмета «Операционные системы» (код предмета `os-intro`) название проекта примет следующий вид:
    ```text
    2026-1--study--os-intro
    ```

-   Каталог для лабораторных работ имеет вид `labs`.
-   Каталоги для лабораторных работ имеют вид `lab<номер>`, например: `lab01`, `lab02` и т.д.
-   Каталог для групповых проектов имеет вид `group-project`.
-   Каталог для персональных проектов имеет вид `personal-project`.
-   Каталог для внешнего курса имеет вид `external-course`.
-   Если проектов несколько, то они нумеруются подобно лабораторным работам.
-   Этапы проекта обозначаются как `stage<номер>`.


## <span class="section-num">5</span> Шаблон для рабочего пространства {#шаблон-для-рабочего-пространства}

-   Репозиторий:
    -   <https://gitverse.ru/dharma/course-directory-student-template>
    -   <https://github.com/yamadharma/course-directory-student-template>.


### <span class="section-num">5.1</span> Сознание репозитория курса на основе шаблона {#сознание-репозитория-курса-на-основе-шаблона}

-   Репозиторий на основе шаблона можно создать либо вручную, через web-интерфейс, либо с помощью утилит `gh` для github (см. [github: утилиты командной строки]({{< relref "2021-08-04-github-command-line-utilities" >}})).


#### <span class="section-num">5.1.1</span> Создание с помощью утилит {#создание-с-помощью-утилит}

-   Создание выглядит следующим образом:
    ```shell
    gh repo create <new-repo-name> --template="<owner/template-repo>"
    ```
-   Например, для 2025-2026 учебного года и предмета «Операционные системы» (аббревиатура предмета --- `os-intro`) создание репозитория примет следующий вид:
    ```shell
    mkdir -p ~/work/study/2026-1/2026-1==study--os-intro
    cd ~/work/study/2026-1/2026-1==study--os-intro
    gh repo create 2026-1--study--os-intro --template=yamadharma/course-directory-student-template --public
    git clone --recursive git@github.com:<owner>/2026-1--study--os-intro.git
    ```


#### <span class="section-num">5.1.2</span> Создание вручную {#создание-вручную}

-   Сделать свой репозиторий на основе шаблона можно и вручную: <https://docs.github.com/ru/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template>.
-   Авторизуйтесь на <https://gitverse.ru>.
-   Перейдите в репозиторий <https://gitverse.ru/dharma/course-directory-student-template>.
-   Найдите кнопку (ссылку) «Использовать как шаблон» <https://gitverse.ru/new?template_id=195300>.
-   После нажатия откроется форма для создания нового репозитория.
-   Укажите название и описание для вашего нового проекта.
-   Выберите уровень доступа (публичный).
-   Нажмите кнопку для подтверждения создания.


### <span class="section-num">5.2</span> Структура шаблона {#структура-шаблона}

-   Посмотреть доступные цели `make`:
    ```shell
    make help
    ```
-   Посмотреть список доступных курсов:
    ```shell
    make list
    ```
-   При создании структуры название курса берётся из следующих мест:
    -   название курса находится в файле `COURSE`;
    -   каталог курса называется как аббревиатура курса.


### <span class="section-num">5.3</span> Настройка каталога курса {#настройка-каталога-курса}

-   Перейдите в каталог курса:
    ```shell
    cd ~/work/study/2026-1/2026-1==study--os-intro/2026-1--study--os-intro
    ```
-   Создайте необходимые каталоги:
    ```shell
    echo os-intro > COURSE
    make prepare
    ```
-   Отправьте файлы на сервер:
    ```shell
    git add .
    git commit -am 'feat(main): make course structure'
    git push
    ```


### <span class="section-num">5.4</span> Использование git flow {#использование-git-flow}

-   Будем использовать для работы git flow (см. [Рабочий процесс Gitflow]({{< relref "2021-04-18-gitflow-workflow" >}})).
-   [Практический сценарий использования git]({{< relref "2021-01-17-git-practical-use-case" >}})


#### <span class="section-num">5.4.1</span> Конфигурация git-flow {#конфигурация-git-flow}

-   Инициализируем git-flow
    ```shell
    git flow init
    ```
    Префикс для ярлыков установим в `v`.
-   Проверьте, что Вы на ветке `develop`:
    ```shell
    git branch
    ```
-   Загрузите весь репозиторий в хранилище:
    ```shell
    git push -u --all
    ```
-   Создадим релиз с версией 1.0.0
    ```shell
    git flow release start 1.0.0
    ```
-   Создадим журнал изменений
    ```shell
    standard-changelog --first-release
    ```
-   Добавим журнал изменений в индекс
    ```shell
    git add CHANGELOG.md
    git commit -am 'chore(site): add changelog'
    ```
-   Зальём релизную ветку в основную ветку
    ```shell
    git flow release finish 1.0.0
    ```
-   Отправим данные на github
    ```shell
    git push --all
    git push --tags
    ```
-   Скопируем CHANGELOG.md в каталог `release`:
    ```shell
    mkdir -p ../release
    cp CHANGELOG.md ../release
    ```
-   Создадим релиз на github. Для этого будем использовать утилиты работы с github (см. [github: утилиты командной строки]({{< relref "2021-08-04-github-command-line-utilities" >}})):
    ```shell
    gh release create v1.0.0 -F ../release/CHANGELOG.md
    ```


## <span class="section-num">6</span> Видео {#видео}

{{< tabs "Рабочее пространство для лабораторной работы" >}}

{{< tab "RuTube" >}}{{< rutube 90a6233297bc6de30acb3af992eaedc8 >}}{{< /tab >}}

{{< tab "Платформа" >}}{{< plvideo Jjf4mXm-h65_ >}}{{< /tab >}}

{{< tab "VKvideo" >}}{{< vkvideo oid=-230024722 id=456239047 hd=2 >}}{{< /tab >}}

{{< tab "Youtube" >}}{{< youtube 39bu5avPoDU >}}{{< /tab >}}

{{< /tabs >}}
