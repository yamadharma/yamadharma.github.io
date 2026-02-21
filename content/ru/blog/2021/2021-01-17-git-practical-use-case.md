---
title: "Практический сценарий использования git"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-17T20:06:00+03:00
lastmod: 2025-09-06T18:47:00+03:00
tags: ["programming", "education"]
categories: ["computer-science"]
draft: false
slug: "git-practical-use-case"
---

-   Предлагается следующий практический сценарий использование git.
-   В нём мы используем стратегию _git flow_, скрипты для генерации общепринятых коммитов, журнала изменений.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Используемые стандарты и программные продукты {#используемые-стандарты-и-программные-продукты}

-   Стандарт Git Flow (см. [Варианты Git Workflow]({{< relref "2020-10-30-git-workflow" >}})).
-   Стандарт [Семантическое версионирование]({{< relref "2020-12-11-semantic-versioning" >}}).
-   Стандарт [Общепринятые коммиты]({{< relref "2020-12-11-conventional-commits" >}}).


## <span class="section-num">2</span> Установка программного обеспечения {#установка-программного-обеспечения}

-   Для Windows используется пакетный менеджер Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})).
-   Для MacOS используется пакетный менеджер [Homebrew](https://brew.sh/).


### <span class="section-num">2.1</span> Установка Node.js {#установка-node-dot-js}

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


### <span class="section-num">2.2</span> Настройка Node.js {#настройка-node-dot-js}

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


### <span class="section-num">2.3</span> Установка git-flow {#установка-git-flow}

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
            sudo dnf -y install epel-release
            ```
        -   Затем, собственно, установить git-flow:
            ```shell
            sudo dnf -y install gitflow
            ```
    -   Fedora
        -   Устанавливается из COPR:
            ```shell
            sudo dnf -y copr enable elegos/gitflow
            sudo dnf install gitflow
            ```
        -   Можно устанавливать вручную:
            ```shell
            cd /tmp
            wget --no-check-certificate -q https://raw.github.com/petervanderdoes/gitflow/develop/contrib/gitflow-installer.sh
            chmod +x gitflow-installer.sh
            sudo ./gitflow-installer.sh install stable
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


### <span class="section-num">2.4</span> Общепринятые коммиты {#общепринятые-коммиты}


#### <span class="section-num">2.4.1</span> commitizen {#commitizen}

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


#### <span class="section-num">2.4.2</span> standard-version {#standard-version}

-   Данная программа автоматизирует изменение номера версии.
    -   pnpm:
        ```shell
        pnpm add -g standard-version
        ```
    -   yarn:
        ```shell
        yarn global add standard-version
        ```


## <span class="section-num">3</span> Настройка git {#настройка-git}


### <span class="section-num">3.1</span> Первичная настройка параметров git {#первичная-настройка-параметров-git}

-   Зададим имя и email владельца репозитория:
    ```shell
    git config --global user.name "Name Surname"
    git config --global user.email "work@mail"
    ```
-   Настроим utf-8 в выводе сообщений git:
    ```shell
    git config --global core.quotepath false
    ```
-   Настройте верификацию и подписание коммитов git (см. [Верификация коммитов git с помощью GPG]({{< relref "2021-01-28-verifying-git-commits-gpg" >}})).
-   Зададим имя начальной ветки (будем называть её `master`):
    ```shell
    git config --global init.defaultBranch master
    ```


### <span class="section-num">3.2</span> Дополнительные настройки {#дополнительные-настройки}


#### <span class="section-num">3.2.1</span> Работа с переносами строк {#работа-с-переносами-строк}

-   В разных операционных системах приняты разные символы для перевода строк:
    -   Windows: `\r\n` (`CR` и `LF`);
    -   Unix: `\n` (`LF`);
    -   Mac: `\r` (`CR`).
-   Посмотреть значения переносов строк в репозитории можно командой:
    ```shell
    git ls-files --eol
    ```

<!--list-separator-->

1.  Параметр `autocrlf`

    -   Настройка `core.autocrlf` предназначена для того, чтобы в главном репозитории все переводы строк текстовых файлах были одинаковы.
    -   Настройка `core.autocrlf` с параметрами `true` и `input` делает все переводы строк текстовых файлов в главном репозитории одинаковыми.
        -   `core.autocrlf true`: конвертация `CRLF->LF` при коммите и обратно `LF->CRLF` при выгрузке кода из репозитория на файловую систему (обычно используется в Windows).
        -   `core.autocrlf input`: конвертация `CRLF->LF` только при коммитах (используются в MacOS/Linux).
    -   Варианты конвертации

        <div class="table-caption">
          <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
          Варианты конвертации для разных значений параметра core.autocrlf
        </div>

        | core.autocrlf | false           | input           | true            |
        |---------------|-----------------|-----------------|-----------------|
        | git commit    | LF -&gt; LF     | LF -&gt; LF     | LF -&gt; CRLF   |
        |               | CR -&gt; CR     | CR -&gt; CR     | CR -&gt; CR     |
        |               | CRLF -&gt; CRLF | CRLF -&gt; LF   | CRLF -&gt; CRLF |
        | git checkout  | LF -&gt; LF     | LF -&gt; LF     | LF -&gt; CRLF   |
        |               | CR -&gt; CR     | CR -&gt; CR     | CR -&gt; CR     |
        |               | CRLF -&gt; CRLF | CRLF -&gt; CRLF | CRLF -&gt; CRLF |
    -   Установка параметра:
        -   Для Windows
            ```shell
            git config --global core.autocrlf true
            ```
        -   Для Linux
            ```shell
            git config --global core.autocrlf input
            ```

<!--list-separator-->

2.  Параметр `safecrlf`

    -   Настройка `core.safecrlf`  предназначена для проверки, является ли окончаний строк обратимым для текущей настройки `core.autocrlf`.
        -   `core.safecrlf true`: запрещается необратимое преобразование `lf<->crlf`. Полезно, когда существуют бинарные файлы, похожие на текстовые файлы.
        -   `core.safecrlf warn`: печать предупреждения, но коммиты с необратимым переходом принимаются.
    -   Установка параметра:
        ```shell
        git config --global core.safecrlf warn
        ```


## <span class="section-num">4</span> Практический сценарий использования git {#практический-сценарий-использования-git}


### <span class="section-num">4.1</span> Создание репозитория git {#создание-репозитория-git}


#### <span class="section-num">4.1.1</span> Подготовка каталога {#подготовка-каталога}

-   Рабочий каталог будем обозначать как `workdir`. Вначале нужно перейти в этот каталог:
    ```shell
    cd workdir
    ```
-   Создаём заготовку для файла `README.md`:
    ```shell
    echo "# test-repo" >> README.md
    git add README.md
    ```
-   Добавим шаблон игнорируемых файлов. Просмотрим список имеющихся шаблонов:
    ```shell
    curl -L -s https://www.gitignore.io/api/list
    ```
    Затем скачаем шаблон, например, для C и C++:
    ```shell
    curl -L -s https://www.gitignore.io/api/c >> .gitignore
    curl -L -s https://www.gitignore.io/api/c++ >> .gitignore
    ```
    Можно это же сделать через web-интерфейс на сайте <https://www.gitignore.io/>.
-   Добавим файл лицензии. В данном случае мы выбираем лицензию `CC-BY-4.0` (см. [Выбор лицензии для научной работы]({{< relref "2021-02-22-scientific-work-choosing-license" >}})):
    ```shell
    wget https://creativecommons.org/licenses/by/4.0/legalcode.txt -O LICENSE
    ```
-   Если выбирается лицензия `CC-BY-SA-4.0`, то нужно выполнить:
    ```shell
    wget https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt -O LICENSE
    ```
-   Инициализируем системы git:
    ```shell
    git init
    ```


#### <span class="section-num">4.1.2</span> Подключение репозитория к github {#подключение-репозитория-к-github}

-   Создайте репозиторий на GitHub. Для примера назовём его `test-repo`.

-   Делаем первый коммит и выкладываем на github:
    ```shell
    git commit -m "first commit"
    git remote add origin git@github.com:<username>/test-repo.git
    git push -u origin master
    ```


#### <span class="section-num">4.1.3</span> Конфигурация общепринятых коммитов {#конфигурация-общепринятых-коммитов}

-   Конфигурация для пакетов Node.js
    ```shell
    yarn init
    ```
    Необходимо заполнить несколько параметров пакета.

    -   Название пакета.
    -   Лицензия пакета. Список лицензий для npm: <https://spdx.org/licenses/>. Предлагается выбирать лицензию `CC-BY-4.0`.
-   Сконфигурим формат коммитов. Для этого добавим в файл `package.json` команду для формирования коммитов:
    ```js
    "config": {
            "commitizen": {
                "path": "cz-conventional-changelog"
            }
    }
    ```
    Таким образом, файл `package.json` приобретает вид:
    ```js
    {
            "name": "test-repo",
            "version": "1.0.0",
            "description": "Git repo for educational purposes",
            "main": "index.js",
            "repository": "git@github.com:username/test-repo.git",
            "author": "Name Surname <username@gmail.com>",
            "license": "CC-BY-4.0",
            "config": {
                "commitizen": {
                    "path": "cz-conventional-changelog"
                }
            }
    }
    ```

-   Добавим новые файлы:
    ```shell
    git add .
    ```
-   Выполним коммит:
    ```shell
    git cz
    ```
-   Отправим на github:
    ```shell
    git push
    ```


#### <span class="section-num">4.1.4</span> Конфигурация git-flow {#конфигурация-git-flow}

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
-   Создадим релиз на github. Для этого будем использовать утилиты работы с github (см. [github: утилиты командной строки]({{< relref "2021-08-04-github-command-line-utilities" >}})):
    ```shell
    gh release create v1.0.0 -F CHANGELOG.md
    ```


### <span class="section-num">4.2</span> Работа с репозиторием git {#работа-с-репозиторием-git}


#### <span class="section-num">4.2.1</span> Разработка новой функциональности {#разработка-новой-функциональности}

-   Создадим ветку для новой функциональности:
    ```shell
    git flow feature start feature_branch
    ```
-   Далее, продолжаем работу c git как обычно.
-   По окончании разработки новой функциональности следующим шагом следует объединить ветку `feature_branch` c `develop`:
    ```shell
    git flow feature finish feature_branch
    ```


#### <span class="section-num">4.2.2</span> Создание релиза git-flow {#создание-релиза-git-flow}

-   Создадим релиз с версией `1.2.3`:
    ```shell
    git flow release start 1.2.3
    ```
-   Обновите номер версии в файле `package.json`. Установите её в `1.2.3`.
-   Создадим журнал изменений
    ```shell
    standard-changelog
    ```
-   Добавим журнал изменений в индекс
    ```shell
    git add CHANGELOG.md
    git commit -am 'chore(site): update changelog'
    ```
-   Зальём релизную ветку в основную ветку
    ```shell
    git flow release finish 1.2.3
    ```
-   Отправим данные на github
    ```shell
    git push --all
    git push --tags
    ```
-   Создадим релиз на github с комментарием из журнала изменений:
    ```shell
    gh release create v1.2.3 -F CHANGELOG.md
    ```
