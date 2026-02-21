---
title: "Резервное копирование. Restic"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-17T20:56:00+03:00
lastmod: 2025-08-18T12:46:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "backup-restic"
---

Резервное копирование. Restic.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://restic.net/>
-   Репозиторий: <https://github.com/restic/restic>


## <span class="section-num">2</span> Установка {#установка}

-   Debian:

<!--listend-->

```shell
sudo apt install restic
```

-   RHEL:

<!--listend-->

```shell
sudo dnf install restic
```

-   Gentoo:
    ```shell
    emerge app-backup/restic
    ```


## <span class="section-num">3</span> Сохранение пароля репозитория restic в `pass` {#сохранение-пароля-репозитория-restic-в-pass}

-   Для безопасности будем хранить пароль в pass.
-   [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})


### <span class="section-num">3.1</span> Пароль репозитория {#пароль-репозитория}

-   Создать пароль репозитория:

<!--listend-->

```shell
pass insert sysadmin/$(hostnamectl hostname)/restic
```

-   Введите пароль от репозитория Restic при запросе.


### <span class="section-num">3.2</span> Проверьте пароль {#проверьте-пароль}

```shell
pass show sysadmin/$(hostnamectl hostname)/restic
```


## <span class="section-num">4</span> Внешний сервер с доступом по SFTP {#внешний-сервер-с-доступом-по-sftp}


### <span class="section-num">4.1</span> Ключ ssh {#ключ-ssh}

-   Для возможности создания резервных копий с использованием sftp, необходимо настроить доступ на сервер ssh по ключу без пароля (т.к. restic не может подключиться к репозиторию, если сервер запрашивает учетные данные).
-   Для использования определённого ключа настройте конфигурационный файл `~/.ssh/config`:
    ```conf-unix
    Host foo
        IdentityFile ~/.ssh/foo-secret-key-file
    ```
-   Можно создать полную конфигурацию для соединения в `~/.ssh/config`:
    ```conf-unix
    Host foo-restic
        User username
        Port 22
        IdentityFile ~/.ssh/foo-secret-key-file
        Hostname foo
    ```
-   Тогда подключаться надо будет так:
    ```shell
    restic -r sftp://foo-restic//some/dir
    ```


### <span class="section-num">4.2</span> Инициализация репозитория на SFTP {#инициализация-репозитория-на-sftp}

-   Инициализация:
    ```shell
    restic -r sftp://user@example.com:22//path/to/backup-repo --password-command "pass sysadmin/$(hostnamectl hostname)/restic" init
    ```
-   Двойной слеш (`//`) для случая абсолютной адресации (от корня).


### <span class="section-num">4.3</span> Сделать резервную копию {#сделать-резервную-копию}

-   Сделать резервную копию:

<!--listend-->

```shell
restic -r sftp://user@example.com/backup-repo --ssh-command "ssh -i ~/.ssh/key" --password-command "pass sysadmin/$(hostnamectl hostname)/restic" backup /важные_данные
```


## <span class="section-num">5</span> Автоматизация бэкапов {#автоматизация-бэкапов}


### <span class="section-num">5.1</span> Создайте файл с паролем {#создайте-файл-с-паролем}

```shell
echo "ваш_пароль_репозитория" > ~/.restic-password
chmod 600 ~/.restic-password
```


### <span class="section-num">5.2</span> Скрипт для бэкапа {#скрипт-для-бэкапа}

-   Создайте файл `~/backup-script.sh`:

<!--listend-->

```shell
#!/bin/bash

# Настройки
REPO="sftp:user@example.com:/backup-repo"
SOURCE="/важные_данные"

# Команда бэкапа
restic -r $REPO \
       --password-command "pass sysadmin/$(hostnamectl hostname)/restic" \
       backup $SOURCE

# Очистка старых бэкапов (храним: 7 дневных, 4 недельных, 6 месячных)
restic -r $REPO \
       --password-command "pass sysadmin/$(hostnamectl hostname)/restic" \
       forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6

# Оптимизация репозитория
restic -r $REPO \
       --password-command "pass sysadmin/$(hostnamectl hostname)/restic" \
       prune
```

-   Сделайте скрипт исполняемым:

<!--listend-->

```shell
chmod +x ~/backup-script.sh
```


### <span class="section-num">5.3</span> Настройте cron для ежедневных бэкапов {#настройте-cron-для-ежедневных-бэкапов}

-   Добавьте строку (пример для ежедневного бэкапа в 2:00) в cron:

<!--listend-->

```shell
0 2 * * * /bin/bash /home/ваш_пользователь/backup-script.sh >> /var/log/restic.log 2>&1
```


## <span class="section-num">6</span> Обслуживание резервных копий {#обслуживание-резервных-копий}


### <span class="section-num">6.1</span> Проверка целостности {#проверка-целостности}

-   Проверим целостность резервной копии:

<!--listend-->

```shell
restic -r sftp://user@example.com/backup-repo --ssh-command "ssh -i ~/.ssh/key" --password-command "pass sysadmin/$(hostnamectl hostname)/restic" check
```


### <span class="section-num">6.2</span> Просмотр списка резервных копий {#просмотр-списка-резервных-копий}

-   Список резервных копий:

<!--listend-->

```shell
restic -r sftp://user@example.com/backup-repo --ssh-command "ssh -i ~/.ssh/key" --password-command "pass sysadmin/$(hostnamectl hostname)/restic" snapshots
```


## <span class="section-num">7</span> Восстановление данных {#восстановление-данных}


### <span class="section-num">7.1</span> Восстановление последнего снимка {#восстановление-последнего-снимка}

-   Восстановим последний снимок:

<!--listend-->

```shell
restic -r sftp://user@example.com/backup-repo --ssh-command "ssh -i ~/.ssh/key" --password-command "pass sysadmin/$(hostnamectl hostname)/restic" restore latest --target /путь/восстановления
```
