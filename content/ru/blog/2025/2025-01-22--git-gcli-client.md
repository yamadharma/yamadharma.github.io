---
title: "git. Клиент gcli"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-22T11:14:00+03:00
lastmod: 2025-01-22T12:39:00+03:00
tags: ["programming"]
categories: ["computer-science"]
draft: false
slug: "git-gcli-client"
---

git. Клиент gcli.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/herrhotzenplotz/gcli>
-   Сайт: <https://herrhotzenplotz.de/gcli/>
-   Взаимодействует с API нескольких сервисов git-хостинга.
-   Поддерживает API: GitHub, GitLab, Gitea, Bugzilla.


## <span class="section-num">2</span> Установка {#установка}

-   Gentoo (репозиторий karma, см. [Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
    ```shell
    emerge -v dev-vcs/gcli
    ```


## <span class="section-num">3</span> Использование {#использование}

---


### <span class="section-num">3.1</span> Подключение учётной записи {#подключение-учётной-записи}


#### <span class="section-num">3.1.1</span> github {#github}

<!--list-separator-->

1.  Создайте токен аутентификации для gcli

    -   Войдите в свою учетную запись GitHub.
    -   Щелкните значок своей учетной записи (верхний правый угол).
    -   Выберите вариант `Settings`.
    -   Прокрутите вниз и выберите `Developer settings` в нижней части левого столбца.
    -   В пункте `Personal access tokens` выберите `Tokens (classic)`.
    -   Нажмите на `Generate new token (classic)`.
    -   Задайте имя, например `gcli` в поле `Note`.
    -   Установите срок действия в `No expiration`.
    -   Разрешите следующее `Scopes`:
        -   `repo`
        -   `workflow`
        -   `admin:public_key`
        -   `gist`
    -   Создайте токен. Он будет напечатан зеленым цветом.

<!--list-separator-->

2.  Конфигурация gcli

    -   Создайте файл конфигурации для gcli:
        ```shell
        mkdir -p $HOME/.config/gcli
        touch $HOME/.config/gcli/config
        ```
    -   Запишите в этот файл (`$HOME/.config/gcli/config`):
        ```conf-unix
        defaults {
            editor=vi
            github-default-account=my-github-account
        }

        my-github-account {
            token=<token-goes-here>
            account=<account-name>
            forge-type=github
        }
        ```
    -   Замените `<token-goes-here>` ранее сгенерированным токеном, `<account>`  именем вашей учётной записи.
    -   Запустите:
        ```shell
        gcli -t github repos
        ```
    -   Вы должны получить список ваших репозиториев.


#### <span class="section-num">3.1.2</span> gitea {#gitea}

<!--list-separator-->

1.  Создайте токен аутентификации для gcli

    -   Нажмите на свой аватар в правом верхнем углу.
    -   Выбирите `Settings` во всплывающем меню.
    -   Выбирите `Applications` в меню слева.
    -   Под `Generate new token`  введите имя токена (например, `gcli`).
    -   Установите все разрешения.
    -   Нажмите кнопку `Generate token`.


#### <span class="section-num">3.1.3</span> Конфигурация gcli {#конфигурация-gcli}

-   Создайте файл конфигурации для gcli:
    ```shell
    mkdir -p $HOME/.config/gcli
    touch $HOME/.config/gcli/config
    ```
-   Запишите в этот файл (`$HOME/.config/gcli/config`):
    ```conf-unix
    defaults {
            gitea-default-account=codeberg-org
            ...
    }

    codeberg-org {
            account=<your-username-at-gitea>
            token=<the-token-you-just-created>
            forge-type=gitea
            api-base=https://codeberg.org/api/v1
    }
    ```

    -   В примере используется хостер Codeberg.
-   Запустите:
    ```shell
    gcli -t gitea repos
    ```
-   Вы должны получить список ваших репозиториев.


### <span class="section-num">3.2</span> Создание репозитория {#создание-репозитория}


#### <span class="section-num">3.2.1</span> Создание репозитория {#создание-репозитория}

-   Создадим репозиторий:
    ```shell
    gcli -t gitea repos create -r <repo_name> -d <repo_description>
    ```
