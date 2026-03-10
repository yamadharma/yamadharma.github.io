---
title: "git. Несколько удалённых репозиториев"
author: ["Dmitry S. Kulyabov"]
date: 2021-03-27T14:08:00+03:00
lastmod: 2026-02-02T21:55:00+03:00
tags: ["programming"]
categories: ["computer-science"]
draft: false
slug: "git-multiple-remote-repositories"
---

-   Я использую несколько серверов репозиториев: github, gitlab, bitbucket.
-   Возникает необходимость использовать несколько удалённых репозиториев в проекте.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Локальный репозиторий можно связать с несколькими удалёнными репозиториями. Однако только одна из этих ссылок может называться `origin`. Остальные ссылки должны иметь другие имена.
-   Команда `git remote -v` отображает все удалённые репозитории, связанные с вашим локальным репозиторием.
-   Для отправки или получения кода из вашего удалённого репозитория по умолчанию используется короткое имя `origin`.


## <span class="section-num">2</span> Несколько удалённых репозиториев {#несколько-удалённых-репозиториев}

-   Можно добавить несколько удалённых репозиториев по `https`:
    ```shell
    git remote add github https://github.com/your_name/repository_name.git
    git remote add gitlab https://gitlab.com/your_name/repository_name.git
    git remote add bitbucket https://bitbucket.org/your_name/repository_name.git
    ```
    или по `ssh`:
    ```shell
    git remote add github git@github.com:your_name/repository_name.git
    git remote add gitlab git@gitlab.com:your_name/repository_name.git
    git remote add bitbucket git@bitbucket.org:your_name/repository_name.git
    ```
-   По команде `git remote -v` получим список репозиториев:
    ```shell
    github git@github.com:your_name/repository_name.git (fetch)
    github git@github.com:your_name/repository_name.git (push)
    gitlab git@gitlab.com:your_name/repository_name.git (fetch)
    gitlab git@gitlab.com:your_name/repository_name.git (push)
    bitbucket git@bitbucket.org:your_name/repository_name.git (fetch)
    bitbucket git@bitbucket.org:your_name/repository_name.git (push)
    ```
-   Для отправки кода в репозиторий необходимо указать его имя:
    ```shell
    git push github master
    git push gitlab master
    git push bitbucket master
    ```


## <span class="section-num">3</span> Замена репозитория по умолчанию {#замена-репозитория-по-умолчанию}

-   Любой из репозиториев можно назвать `origin`, тогда он будет репозиторием по умолчанию.
-   Также можно заменить текущий удалённый репозиторий:
    ```shell
    git remote set-url <remote_name> <remote_url>
    ```
    Например:
    ```shell
    git remote set-url origin https://github.com/your_name/repository_name.git
    ```


## <span class="section-num">4</span> Submodules {#submodules}

-   Если репозиторий содержит подмодули, то желательно, чтобы они находились на том же хостинге.


### <span class="section-num">4.1</span> Скрипт для автоматической замены URL {#скрипт-для-автоматической-замены-url}

-   Можно сделать с помощью хуков.
-   Создайте скрипт `.git/hooks/post-checkout`:

<!--listend-->

```shell
#!/bin/bash
# fix-submodules.sh

# Определяем текущий origin URL
ORIGIN_URL=$(git remote get-url origin)

if [[ $ORIGIN_URL == *"github.com"* ]]; then
    git submodule set-url lib/mylib https://github.com/user/mylib.git
elif [[ $ORIGIN_URL == *"gitlab.com"* ]]; then
    git submodule set-url lib/mylib https://gitlab.com/user/mylib.git
fi

git submodule sync
```

-   Сделайте файл исполняемым:
    ```shell
    chmod +x .git/hooks/post-checkout
    ```
-   Впрочем, поскольку хуки не отправляются в репозиторий, они действуют только локально.
