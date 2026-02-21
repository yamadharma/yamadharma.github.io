---
title: "github: утилиты командной строки"
author: ["Dmitry S. Kulyabov"]
date: 2021-08-04T14:40:00+03:00
lastmod: 2024-08-14T22:06:00+03:00
tags: ["programming"]
categories: ["computer-science"]
draft: false
slug: "github-command-line-utilities"
---

Утилиты работы с _github_ из командной строки.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/cli/cli>
-   Документация: <https://cli.github.com/manual/>
-   Ранее для этих же целей разрабатывалась программа _Hub_ (<https://hub.github.com/>), но её забросили (см. <https://mislav.net/2020/01/github-cli/>).


## <span class="section-num">2</span> Установка программного обеспечения {#установка-программного-обеспечения}


### <span class="section-num">2.1</span> Linux {#linux}

-   Gentoo:
    ```shell
    emerge dev-util/github-cli
    ```
-   Fedora:
    ```shell
    sudo dnf install gh
    ```


### <span class="section-num">2.2</span> Windows {#windows}

-   Chocolatey
    ```shell
    choco install gh
    ```


## <span class="section-num">3</span> Порядок работы {#порядок-работы}


### <span class="section-num">3.1</span> Начало работы {#начало-работы}

-   Для начала необходимо авторизоваться
    ```shell
    gh auth login
    ```

    -   Утилита задаст несколько наводящих вопросов.
    -   Авторизоваться можно через броузер.


## <span class="section-num">4</span> Основные задачи {#основные-задачи}


### <span class="section-num">4.1</span> Релизы (releases) {#релизы--releases}


#### <span class="section-num">4.1.1</span> Список релизов {#список-релизов}

-   Команда:
    ```shell
    gh release list [flags]
    ```
-   Параметры:
    -   `-L`, `--limit int`: максимальное количество элементов для выборки (по умолчанию 30).


#### <span class="section-num">4.1.2</span> Информация о релизе {#информация-о-релизе}

-   Команда:
    ```shell
    gh release view [<tag>] [flags]
    ```
-   Параметры:
    -   `-q`, `--jq expression`: фильтровать вывод JSON с использованием выражения _jq_;
    -   `--json fields`: выводить JSON с указанными полями;
    -   `-t`, `--template string`: форматировать вывод JSON с использованием шаблона _Go_;
    -   `-w`, `--web`: открыть выпуск в броузере.


#### <span class="section-num">4.1.3</span> Создание релиза {#создание-релиза}

-   Команда:
    ```shell
    gh release create <tag> [<files>...]
    ```
-   Параметры:
    -   `-d`, `--draft`: сохранить релиз как черновик вместо его публикации;
    -   `-n`, `--notes string`: примечания к выпуску;
    -   `-F`, `--notes-file file`: взять примечания к выпуску из файла;
    -   `-p`, `--prerelease`: отметить выпуск как предварительный;
    -   `--target branch`: задать целевую ветку;
    -   `-t`, `--title string`: задать название выпуска.
-   Примеры:
    -   Интерактивное создание выпуска:
        ```shell
        gh release create v1.2.3
        ```
    -   Создание релиза в неинтерактивном режиме:
        ```shell
        gh release create v1.2.3 --notes "bugfix release"
        ```
    -   Использовать примечания к выпуску из файла:
        ```shell
        gh release create v1.2.3 -F CHANGELOG.md
        ```


#### <span class="section-num">4.1.4</span> Загрузка ресурсов в выпуск {#загрузка-ресурсов-в-выпуск}

-   Команда:
    ```shell
    gh release upload <tag> <files>... [flags]
    ```

    -   Чтобы задать отображаемую метку для ресурса, добавьте текст, начинающийся с символа `#`, после имени файла.
-   Параметры:
    -   `--clobber`: перезаписать существующие ресурсы с тем же именем.

-   Загрузить ресурсные файлы можно и при создании релиза.
    -   Загрузите все архивы из каталога как ресурсы выпуска:
        ```shell
        gh release create v1.2.3 ./dist/*.tar.gz
        ```
    -   Загрузить ресурс выпуска с отображаемой меткой:
        ```shell
        gh release create v1.2.3 '/path/to/asset.zip#My display label'
        ```


#### <span class="section-num">4.1.5</span> Скачать ресурсы выпуска {#скачать-ресурсы-выпуска}

-   Команда:
    ```shell
    gh release download [<tag>] [flags]
    ```
-   Параметры:
    -   `-p`, `--pattern`: задать шаблон имени файла.
-   Примеры.
    -   Скачать все ресурсы из определенного выпуска:
        ```shell
        gh release download v1.2.3
        ```
    -   Скачать файлы по шаблону из последнего релиза:
        ```shell
        gh release download -p '*.deb' -p '*.rpm'
        ```


#### <span class="section-num">4.1.6</span> Удаление выпуска {#удаление-выпуска}

-   Команда:
    ```shell
    gh release delete <tag> [flags]
    ```
-   Параметры:
    -   `-y`, `--yes`: пропустить запрос на подтверждение.


### <span class="section-num">4.2</span> Проблемы (issues) {#проблемы--issues}


### <span class="section-num">4.3</span> Репозитории (repo) {#репозитории--repo}


#### <span class="section-num">4.3.1</span> Создание репозитория {#создание-репозитория}

-   Создать репозиторий в интерактивном режиме:
    ```shell
    gh repo create
    ```
-   Чтобы создать удалённый репозиторий в неинтерактивном режиме, укажите имя репозитория и один из ключей: `--public`, `--private`, `--internal`.
    -   С ключом `--clone` репозиторий клонируется локально.
-   Чтобы создать удалённый репозиторий из существующего локального репозитория, укажите исходный каталог с ключом `--source`.
    -   По умолчанию именем удалённого репозитория будет имя исходного каталога.
    -   Задайте ключ `--push`, чтобы отправить любые локальные коммиты в новый репозиторий.


#### <span class="section-num">4.3.2</span> Параметры {#параметры}

-   `--add-readme` : добавьте файл README в новый репозиторий;
-   `-c`, `--clone` : клонируйте новый репозиторий в текущий каталог;
-   `-d`, `--description <string>` : описание репозитория;
-   `--disable-issues` : отключить проблемы в новом репозитории;
-   `--disable-wiki` ; отключить вики в новом репозитории;
-   `-g`, `--gitignore <string>` : шаблон `gitignore` для репозитория;
-   `-h`, `--homepage <URL>` : адрес домашней страницы репозитория;
-   `--include-all-branches` : включить все ветки из репозитория шаблонов;
-   `--internal` :  внутренний репозиторий;
-   `-l`, `--license <string>` : лицензию открытого исходного кода для репозитория;
-   `--private` : приватный репозиторий;
-   `--public` : общедоступный репозиторий;
-   `--push` : отправить локальные коммиты в новый репозиторий;
-   `-r`, `--remote <string>` : удалённое имя для нового репозитория;
-   `-s`, `--source <string>` : путь к локальному репозиторию, который будет использоваться в качестве источника;
-   `-t`, `--team <name>` : название организационной группы, которой будет предоставлен доступ;
-   `-p`, `--template <repository>` : новый репозиторий на основе репозитория шаблонов.


#### <span class="section-num">4.3.3</span> Примеры {#примеры}

-   Интерактивное создание репозитория:
    ```shell
    gh repo create
    ```
-   Создать репозиторий и клонировать его:
    ```shell
    gh repo create my-project --public --clone
    ```
-   Создать репозиторий из текущего каталога:
    ```shell
    gh repo create my-project --private --source=. --remote=upstream
    ```


### <span class="section-num">4.4</span> Управление ключами ssh {#управление-ключами-ssh}

-   Список ключей ssh в учётной записи GitHub:
    ```shell
    gh ssh-key list
    ```
-   Удалить ключ ssh из учётной записи GitHub:
    ```shell
    gh ssh-key delete <id>
    ```
-   Добавить ключ ssh в учётную запись GitHub:
    ```shell
    gh ssh-key add [<key-file>] [flags]
    ```

    -   Флаги:
        -   `-t`, `--title <string>` : название нового ключа;
        -   `--type <string>` : тип ssh-ключа:
            -   `authentication` (значение по умолчанию);
            -   `signing`.
