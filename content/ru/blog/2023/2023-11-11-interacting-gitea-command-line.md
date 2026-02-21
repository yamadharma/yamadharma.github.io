---
title: "Взаимодействие с gitea из командной строки"
author: ["Dmitry S. Kulyabov"]
date: 2023-11-11T20:31:00+03:00
lastmod: 2025-01-22T13:01:00+03:00
tags: ["sysadmin", "git"]
categories: ["computer-science"]
draft: false
slug: "interacting-gitea-command-line"
---

-   Взаимодействие с gitea из командной строки.
-   На данный момент рекомендуется использовать утилиту `tea`.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://gitea.com/gitea/tea>


## <span class="section-num">2</span> Примеры использования {#примеры-использования}


### <span class="section-num">2.1</span> Подключение к серверу {#подключение-к-серверу}

-   Вначале необходимо подключиться к серверу Gitea.
-   Войти на сервер Gitea:
    ```shell
    tea login add --name "Условное имя подключения" --url "Server url" --token "token"
    ```
-   Можно установить подключение как подключение по умолчанию:
    ```shell
    tea login default "Условное имя подключения"
    ```


### <span class="section-num">2.2</span> Репозитории {#репозитории}

-   Показать все репозитории:
    ```shell
    tea repos ls
    ```
-   Создать репозиторий:
    ```shell
    tea repo create --name "Название репозитория"
    ```
-   Создать частный репозиторий:
    ```shell
    tea repo create --name "Название репозитория" --private
    ```
-   Создать репозиторий для организации:
    ```shell
        tea repo create --name "Название репозитория" --private --owner имя_организации
      #+end_src--name "Название репозитория" --private --owner имя_организации
    ​- Создать репозиторий из шаблона:
      #+begin_src shell
        tea repos create-from-template --name "Название репозитория" --private --owner имя_организации --template <template_name>
    ```


### <span class="section-num">2.3</span> Issues {#issues}

-   Отображение списка issues:
    ```shell
    tea issues ls
    ```

-   Отобразить список issues для конкретного репозитория:
    ```shell
    tea issues ls --repo "repository"
    ```

-   Создать новую задачу:
    ```shell
    tea issues create --title "title" --body "body"
    ```

-   Отобразить список открытых pull-запросов:
    ```shell
    tea pulls ls
    ```

-   Открыть текущий репозиторий в броузере:
    ```shell
    tea open
    ```
