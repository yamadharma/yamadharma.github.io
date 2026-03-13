---
title: "gopass. Интеграция с git"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-19T15:56:00+03:00
lastmod: 2025-11-21T10:43:00+03:00
tags: ["sysadmin", "git", "programming"]
categories: ["computer-science"]
draft: false
slug: "gopass-integration-git"
---

gopass. Интеграция с git.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   git-credential-gopass
-   Репозиторий: <https://github.com/gopasspw/git-credential-gopass>
-   Позволяет безопасно хранить и автоматически подставлять учётные данные (логины, пароли, токены) для работы с Git-репозиториями.


## <span class="section-num">2</span> Установка {#установка}

-   Gentoo
    ```shell
    emerge app-admin/git-credential-gopass
    ```
-   Для Windows (с помощью Chocolatey):

<!--listend-->

```shell
choco install git-credential-gopass
```


## <span class="section-num">3</span> Настройка Git {#настройка-git}

-   Добавьте helper в глобальную конфигурацию Git:
    ```shell
    git config --global credential.helper gopass
    ```
-   Проверьте конфигурацию Git:
    ```shell
    git config --global --get credential.helper
    ```
-   Должно вернуть: `gopass`.
-   Можно сохранить учётные данные в хранилище группы для совместного использования:

<!--listend-->

```shell
git config credential.helper "gopass --store=ci-team"
```


## <span class="section-num">4</span> Сохранение учётных данных {#сохранение-учётных-данных}

-   `git-credential-gopass` будет использоваться `git` для запроса и сохранения учетных данных, когда они необходимы.
-   После клонирования репозитория Git, требующего HTTP-аутентификации, автоматически будет создана новая запись по шаблону `git/HOST_PORT/USERNAME`.
-   Секрет должен как минимум содержать пароль и имя пользователя.

<!--listend-->

```shell
gopass insert git/<hostname>/<username>
```

Формат:

-   Пароль: ваш токен или пароль
-   Доп. поля (через `key: value`):
    ```yaml
    Пароль
    user: your_login
    url: https://github.com/your_username/repo.git
    ```


## <span class="section-num">5</span> Примеры использования {#примеры-использования}


### <span class="section-num">5.1</span> Клонирование репозитория {#клонирование-репозитория}

-   Gopass автоматически подставит логин и токен:

<!--listend-->

```shell
git clone https://github.com/your_username/repo.git
```


### <span class="section-num">5.2</span> Отправка изменений {#отправка-изменений}

-   Gopass автоматически подставит логин и токен:

<!--listend-->

```shell
git push origin main
```


## <span class="section-num">6</span> Расширенные настройки {#расширенные-настройки}


### <span class="section-num">6.1</span> Для разных аккаунтов на одном хосте {#для-разных-аккаунтов-на-одном-хосте}

-   Создайте отдельные записи:

<!--listend-->

```shell
gopass insert git/github.com/work-account
gopass insert git/github.com/personal-account
```


### <span class="section-num">6.2</span> Привязка к конкретному URL {#привязка-к-конкретному-url}

```shell
git config --global credential.https://github.com.helper gopass
```
