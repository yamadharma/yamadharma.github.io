---
title: "Миграция с bitbucket на gitea"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-31T11:23:00+03:00
lastmod: 2024-02-09T13:56:00+03:00
tags: ["git", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "migration-bitbucket-gitea"
---

Миграция с bitbucket на gitea.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Пролегомены {#пролегомены}

-   В связи с тем, что Bitbucket начал блокировать учётные записи, было принято решение перейти на другой хостинг.
-   Поскольку однозначный выбор хостинга не удалось сделать, было решено:
    -   поднять свой хостинг git (см. [Установка gitea]({{< relref "2023-10-29-install-gitea" >}}));
    -   перенести все репозитории;
    -   перенести или пересоздать команды.


## <span class="section-num">2</span> Необходимая информация для миграции {#необходимая-информация-для-миграции}


### <span class="section-num">2.1</span> Gitea {#gitea}

-   Адрес экземпляра Gitea
    -   Например: <http://hub.example.com>
-   Токен аутентификации
    -   <http://hub.example.com/user/settings/applications>


### <span class="section-num">2.2</span> Bitbucket {#bitbucket}

-   Имя пользователя BitBucket:
    -   это не почтовый адрес, по которому вы подключаетесь к BitBucket, а заданное в настройках имя;
    -   <https://bitbucket.org/account/settings/>
-   Пароль BitBucket:
    -   лучше использовать не пароль подключения к BitBucket, а создать для этого токен:
    -   <https://bitbucket.org/account/settings/app-passwords/>
-   Название группы, если вы переносите команду.


## <span class="section-num">3</span> Варианты миграции {#варианты-миграции}


### <span class="section-num">3.1</span> gickup {#gickup}

-   Универсальный фреймворк по переносу git-репозиториев.
-   Репозиторий: <https://github.com/cooperspencer/gickup>
-   Документация: <https://cooperspencer.github.io/gickup-documentation/>
-   Пример файла конфигурации: <https://github.com/cooperspencer/gickup/blob/main/conf.example.yml>


#### <span class="section-num">3.1.1</span> Проблемы {#проблемы}

-   Репозитории просто не скачивались.
-   Хотя программы писала, что всё сделано.


### <span class="section-num">3.2</span> BitbucketToGitea {#bitbuckettogitea}

-   Скрипт по переносу репозиториев BitBucket в Gitea.
-   Репозиторий: <https://github.com/sIspravnikov/BitbucketToGitea>


#### <span class="section-num">3.2.1</span> Проблема {#проблема}

-   Никак не удалось устранить проблемы при авторизации в BitBucket.


## <span class="section-num">4</span> Реализация миграции {#реализация-миграции}

-   Использовал набор скриптов.
-   Репозиторий: <https://github.com/dstapp/bitbucket-to-gitea-migrator>
-   Скачайте репозиторий на свой компьютер:
    ```shell
    git clone https://github.com/dprandzioch/bitbucket-to-gitea-migrator.git
    ```
-   Создайте конфигурационный файл:
    ```shell
    cd bitbucket-to-gogs-migrator
    cp config.json.example config.json
    ```

<!--listend-->

-   Отредактируйте файл `config.json`:
    ```js
    {
        "base": {
            "check_exists": false
        },
        "gogs": {
            "url": "URL-адрес экземпляра Gitea в формате hub.example.com",
            "protocol": "http",
            "token": "токен аутентификации Gitea",
            "owner_id": 1
        },
        "bitbucket": {
            "user": "Имя пользователя BitBucket",
            "password": "Пароль BitBucket",
            "team": null
        }
    }
    ```
-   Установите необходимые пакеты:
    ```shell
    npm install
    ```
-   Проведите миграцию:
    ```shell
    npm start
    ```


## <span class="section-num">5</span> Репозитории у пользователей {#репозитории-у-пользователей}

-   Для того, чтобы переключить репозитории пользователей (из команды) на новый хостинг, добавил в репозитории скрипт:
    ```shell
    #!/bin/bash

    change_remote() {
        remote_orig=$(git remote get-url --all origin)
        echo "$remote_orig" | grep bitbucket.org &> /dev/null
        if [[ $? == 0 ]]
        then
            echo "Replace origin"
            git remote add bitbucket $remote_orig
            git remote set-url origin ${remote_orig/bitbucket.org/hub.example.com}
        fi
    }

    change_remote

    git remote get-url --all bitbucket &> /dev/null
    if [[ $? == 0 ]]
    then
        is_bitbucket=1
    fi

    [[ $is_bitbucket == 1 ]] && git pull bitbucket master
    git pull

    git add .
    git commit -am "chore(main): $(date)"
    git push --all
    [[ $is_bitbucket == 1 ]] && git push bitbucket

    # Сжатие git
    if [[ $1 == "compress" ]]
        then
        if [[ -d .git ]]
        then
            find . -type f -name "*Конфликтующая*" -delete
            find . -type f -name "*conflicted*" -delete
            find . -depth -path ./.stversions -prune -o -name ".syncthing.*.tmp"  -delete
            git fsck
            git gc --prune=now
            git gc --aggressive --prune=now
        fi
    fi
    ```
