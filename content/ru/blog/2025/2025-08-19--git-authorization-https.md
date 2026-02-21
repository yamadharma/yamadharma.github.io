---
title: "git. Авторизация по https"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-19T14:10:00+03:00
lastmod: 2025-08-20T11:18:00+03:00
tags: ["git", "sysadmin", "programming"]
categories: ["computer-science"]
draft: false
slug: "git-authorization-https"
---

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Создание токена доступа {#создание-токена-доступа}


### <span class="section-num">1.1</span> Для GitHub {#для-github}

-   Перейдите в `Settings → Developer Settings → Personal Access Tokens → Generate new token`.
-   Выберите права (минимум `repo` для работы с репозиториями).
-   Скопируйте токен (отображается только один раз).


### <span class="section-num">1.2</span> Для GitLab {#для-gitlab}

-   `Preferences → Access Tokens`
-   Выберите `read_repository` и `write_repository`.
-   Скопируйте токен (отображается только один раз).


### <span class="section-num">1.3</span> Для Gitea {#для-gitea}

-   Зайдите в настройки профиля
    -   Кликните на аватар в правом верхнем углу.
    -   Выберите `Settings`.
    -   В левом меню выберите `Applications` → `Manage Access Tokens`.
-   Создайте новый токен
    -   В поле `Token Name` укажите название (например, `my-token` ).
    -   Выберите права
        -   Для работы с репозиториями: `read:repository`, `write:repository`.
        -   Для доступа к API: `read:user`, `write:user`.
    -   Нажмите `Generate Token`.
-   Скопируйте токен (отображается только один раз).


## <span class="section-num">2</span> Клонирование репозитория с HTTPS {#клонирование-репозитория-с-https}

-   Клонируйте репозиторий:

<!--listend-->

```shell
git clone https://github.com/username/repo.git
```

-   При запросе данных введите:
    -   `username` : ваш логин на платформе.
    -   `password` : вставьте токен (не пароль).


## <span class="section-num">3</span> Хранение учётных данных {#хранение-учётных-данных}


### <span class="section-num">3.1</span> Ручное указание токена в URL {#ручное-указание-токена-в-url}

-   Для клонирования:

<!--listend-->

```shell
git clone https://username:your_token@github.com/username/repo.git
```

-   Для существующего репозитория:

<!--listend-->

```shell
git remote set-url origin https://username:your_token@github.com/username/repo.git
```


### <span class="section-num">3.2</span> Использование переменных окружения (для скриптов) {#использование-переменных-окружения--для-скриптов}

-   Linux

<!--listend-->

```shell
export GIT_USERNAME="ваш_логин"
export GIT_PASSWORD="ваш_токен"
```

-   Windows (PowerShell)

<!--listend-->

```shell
$env:GIT_USERNAME = "ваш_логин"
$env:GIT_PASSWORD = "ваш_токен"
```

-   Использование в командах:

<!--listend-->

```shell
git clone https://$GIT_USERNAME:$GIT_PASSWORD@github.com/user/repo.git
```


### <span class="section-num">3.3</span> Настройка автоматической аутентификации {#настройка-автоматической-аутентификации}

-   Git Credential Helper --- это инструмент для безопасного хранения и автоматической подстановки учётных данных (логина, пароля, токенов) при работе с Git.
-   Он избавляет от необходимости вводить данные при каждом взаимодействии с удалённым репозиторием.


#### <span class="section-num">3.3.1</span> Вариант. Кэширование учётных данных {#вариант-dot-кэширование-учётных-данных}

-   Хранит данные в памяти 15 минут
    ```shell
    git config --global credential.helper cache
    ```
-   Кэшировать в памяти на 1 час (3600 секунд)

<!--listend-->

```shell
git config --global credential.helper "cache --timeout=3600"
```

-   Проверка настроек

<!--listend-->

```shell
git config --global --get credential.helper
```


#### <span class="section-num">3.3.2</span> Вариант. Постоянное хранение (для доверенных устройств) {#вариант-dot-постоянное-хранение--для-доверенных-устройств}

-   Сохранить в файл `~/.git-credentials`.

<!--listend-->

```shell
git config --global credential.helper store
```

-   Первая операция запросит логин/токен, последующие --- нет.

<!--listend-->

```shell
git pull
```


#### <span class="section-num">3.3.3</span> Вариант. Хранение в менеджере паролей gopass {#вариант-dot-хранение-в-менеджере-паролей-gopass}

-   [gopass. Интеграция с git]({{< relref "2025-08-19--gopass-integration-git" >}})


## <span class="section-num">4</span> Рекомендации по безопасности {#рекомендации-по-безопасности}

-   Никогда не коммитьте токены в код.
-   Для публичных репозиториев используйте токены с ограниченными правами.
-   Регулярно обновляйте токены (рекомендуется каждые 3-6 месяцев).
-   Используйте `.gitignore` для файлов с чувствительными данными.


## <span class="section-num">5</span> Миграция репозитория с SSH на HTTPS {#миграция-репозитория-с-ssh-на-https}


### <span class="section-num">5.1</span> Изменение URL удалённого репозитория {#изменение-url-удалённого-репозитория}

-   Для каждого репозитория выполните в терминале:

<!--listend-->

```shell
git remote set-url origin https://github.com/username/repo.git
```

-   Замените:
    -   `username` → ваш логин на GitHub
    -   `repo` → название репозитория

-   Например, для репозитория `my-project`:

<!--listend-->

```shell
git remote set-url origin https://github.com/ivanov/my-project.git
```


### <span class="section-num">5.2</span> Массовое изменение {#массовое-изменение}

-   Создайте скрипт `git-ssh-to-https.sh`:

<!--listend-->

```shell
#!/bin/bash
for dir in *
do
    if [[ -d ${dir} ]]
       then
           cd "$dir" || exit
           repo_url=$(git remote get-url origin)
           new_url=$(echo "$repo_url" | sed 's/git@github.com:/https:\/\/github.com\//; s/\.git$//').git
           git remote set-url origin "$new_url"
           echo "Updated: $dir → $new_url"
    fi
done
```

-   Или однострочник:

<!--listend-->

```shell
find . -type d -name .git -exec sh -c 'cd "{}" && cd .. && git remote set-url origin $(git remote get-url origin | sed "s/git@/https:\/\//; s/.com:/.com\//")' \;
```
