---
title: "Расширение git lfs"
author: ["Dmitry S. Kulyabov"]
date: 2023-11-13T11:52:00+03:00
lastmod: 2024-02-14T15:51:00+03:00
tags: ["sysadmin", "programming", "git"]
categories: ["computer-science"]
draft: false
slug: "git-lfs"
---

Расширение для хранения больших бинарных файлов на git.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://git-lfs.com/>
-   Репозиторий: <https://github.com/git-lfs/git-lfs/>


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Linux {#linux}

-   Gentoo:
    ```shell
    emerge dev-vcs/git-lfs
    ```


## <span class="section-num">3</span> Использование {#использование}


### <span class="section-num">3.1</span> Инициализация {#инициализация}

-   Запускается однократно:
    ```shell
    git lfs install
    ```
-   Прописывает хуки и переменные в файл конфигурации.


### <span class="section-num">3.2</span> Подготовка нового репозитория {#подготовка-нового-репозитория}

-   После создания нового репозитория запустите в нём:
    ```shell
    git lfs install
    ```
-   При этом в репозитории появится специальный хук _git_ `pre-push`, который будет передавать файлы _git lfs_ на сервер при выполнении команды `git push`.
-   После инициализации хранилища _git lfs_ для репозитория нужно указать, какие файлы нужно отслеживать, например:
    ```shell
    git lfs track "*.pdf"
    ```
-   Информация будет занесена в файл `.gitattributes`.
-   После любого вызова `git-lfs-track` или `git-lfs-untrack` необходимо зафиксировать изменения в файле `.gitattributes`:
    ```shell
    git add .gitattributes
    git commit -m "track *.pdf files using Git LFS"
    ```
-   _Git lfs_ поддерживает те же шаблоны, что и `.gitignore`, например:
    ```shell
    # track all .ogg files in any directory
    $ git lfs track "*.ogg"

    # track files named music.ogg in any directory
    $ git lfs track "music.ogg"

    # track all files in the Assets directory and all subdirectories
    $ git lfs track "Assets/"

    # track all files in the Assets directory but *not* subdirectories
    $ git lfs track "Assets/*"

    # track all ogg files in Assets/Audio
    $ git lfs track "Assets/Audio/*.ogg"

    # track all ogg files in any directory named Music
    $ git lfs track "**/Music/*.ogg"

    # track png files containing "xxhdpi" in their name, in any directory
    $ git lfs track "*xxhdpi*.png"
    ```
-   Шаблоны задаются относительно каталога, из которого выполняется команда `git lfs track`.
-   В отличие от `.gitignore`, _git lfs_ не поддерживает отрицательные шаблоны.


### <span class="section-num">3.3</span> Миграция старых репозиториев {#миграция-старых-репозиториев}

-   Если в истории вашего репозитория уже есть большие файлы, они не будут отслеживаться _git lfs_.
-   Чтобы перенести существующие большие файлы в вашей истории на использование _git lfs_, нужно провести миграцию:
    ```shell
    git lfs migrate import --include="*.pdf" --everything
    ```
-   Это перезапишет историю и изменит все идентификаторы объектов _git_ в репозитории.
-   После этого придётся склонировать репозиторий повторно.


### <span class="section-num">3.4</span> Обратная миграция {#обратная-миграция}

-   Репозиторий с _git lfs_ можно преобразовать обратно в простой репозиторий _git_.
-   Следите за файлами, которые находятся в lfs:
    ```shell
    git lfs ls-files
    ```
-   Перенесите ссылки из _git lfs_ в _git_ (например, для pdf-файлов):
    ```shell
    git lfs migrate export --include="*.pdf" --everything
    ```
-   Это перезапишет историю и изменит все идентификаторы объектов _git_ в вашем репозитории.
-   После этого придётся склонировать репозиторий повторно.
-   Удалите хуки:
    ```shell
    git lfs uninstall --worktree
    ```
-   Удалить атрибут `lfs` из `.gitattributes`:
    ```shell
    sed -i -e "s/filter=lfs diff=lfs merge=lfs -text/binary/g" .gitattributes
    ```


### <span class="section-num">3.5</span> Мониторинг {#мониторинг}

-   Отображение полезной информацию о репозитории:
    ```shell
    git lfs env
    ```
-   Просмотр файлов под управлением _git lfs_:
    ```shell
    git lfs ls-files
    ```


### <span class="section-num">3.6</span> Клонировании репозитория {#клонировании-репозитория}

-   Команда клонирования репозитория скачивает только файлы размером до 100MB.
-   Для получения больших файлов следует использовать команду:
    ```shell
    git lfs  pull
    ```


### <span class="section-num">3.7</span> Перенос на другой хостинг {#перенос-на-другой-хостинг}

-   Для переноса репозитория _git lfs_ на другой хостинг можно использовать комбинацию команд `git lfs fetch` и `git lfs push` с параметром `--all`.
-   Например, перенесём репозиторий с сервера github на сервер bitbucket:
    ```shell
    # create a bare clone of the GitHub repository
    $ git clone --bare git@github.com:kannonboy/atlasteroids.git
    $ cd atlasteroids

    # set up named remotes for Bitbucket and GitHub
    $ git remote add bitbucket git@bitbucket.org:tpettersen/atlasteroids.git
    $ git remote add github git@github.com:kannonboy/atlasteroids.git

    # fetch all Git LFS content from GitHub
    $ git lfs fetch --all github

    # push all Git and Git LFS content to Bitbucket
    $ git push --mirror bitbucket
    $ git lfs push --all bitbucket
    ```
