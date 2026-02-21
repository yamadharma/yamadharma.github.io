---
title: "Moodle. Обновление"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-15T16:37:00+03:00
lastmod: 2026-02-08T11:06:00+03:00
tags: ["education", "sysadmin"]
categories: ["science", "computer-science"]
draft: false
slug: "moodle-upgrade"
---

Moodle. Обновление.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Обновление пререквизитов {#обновление-пререквизитов}


### <span class="section-num">1.1</span> Postgres {#postgres}

-   Делается, если нужно изменить версию PostgreSQL.


#### <span class="section-num">1.1.1</span> Бэкап базы данных {#бэкап-базы-данных}

-   Сделайте бекап базы:
    ```shell
    sudo -u postgres pg_dump -U postgres moodle > moodle.sql
    ```


#### <span class="section-num">1.1.2</span> Обновление Postgres {#обновление-postgres}

-   Версии, которая идёт в комплекте с дистрибутивом, достаточно.
-   Но лучше установить версию поновее.
-   Смотрим, какие версии в наличии:
    ```shell
    dnf module list postgresql
    ```
-   Установим postgresql-16:
    ```shell
    sudo dnf module reset postgresql
    sudo dnf module enable postgresql:16
    sudo dnf -y install postgresql-server postgresql-upgrade
    ```
-   Проверьте установленную версию:
    ```shell
    postgres -V
    ```
-   Инициализируем базу данных:
    ```shell
    postgresql-setup --initdb --unit postgresql
    ```
-   Проверим, что в `/var/lib/pgsql/data/postgresql.conf` установлен алгоритм шифрования:
    ```conf-unix
    password_encryption = scram-sha-256
    ```
-   Запустим postgres:
    ```shell
    systemctl enable --now postgresql
    ```


#### <span class="section-num">1.1.3</span> Восстановление базы данных {#восстановление-базы-данных}

-   Подключимся к базе данных:
    ```shell
    sudo -u postgres psql
    ```
-   Создадим базу данных (укажите необходимый пароль):
    ```sql
    CREATE DATABASE moodle;
    CREATE USER moodle WITH PASSWORD '<password>';
    ALTER DATABASE moodle OWNER TO moodle;
    \connect moodle;
    GRANT CREATE ON SCHEMA public TO moodle;
    \q
    ```
-   Проверьте подключение к базе данных:
    ```shell
    psql --username moodle --password --host localhost moodle
    ```
-   После подключения посмотрите параметры соединения:
    ```sql
    \conninfo
    \q
    ```
-   Восстановите данные из резервной копии:
    ```shell
    sudo -u postgres psql -d moodle -f moodle.sql
    ```


### <span class="section-num">1.2</span> PHP {#php}


#### <span class="section-num">1.2.1</span> Проверка расширений {#проверка-расширений}

-   Проверить установленные расширения:
    ```shell
    sudo dnf install php-pgsql php-gd php-intl php-xmlrpc php-soap php-opcache php-sodium php-fpm php-pecl-zip
    ```


#### <span class="section-num">1.2.2</span> Обновление php {#обновление-php}

-   Установим репозиторий remi:
    ```shell
    sudo dnf config-manager --set-enabled crb
    sudo dnf install epel-release
    sudo dnf install dnf-utils http://rpms.remirepo.net/enterprise/remi-release-9.rpm
    ```
-   Смотрим, какие версии в наличии:
    ```shell
    sudo dnf module list php
    ```
-   Установим php-8.2:
    ```shell
    sudo dnf module reset php
    sudo dnf module enable php:remi-8.2
    sudo dnf -y install php php-cli php-pgsql php-opcache php-pdo php-pecl-mcrypt php-sodium
    sudo dnf -y update
    ```
-   Перезапустим сервисы:
    ```shell
    sudo systemctl restart php-fpm.service
    sudo systemctl restart httpd.service
    ```


## <span class="section-num">2</span> Обновление Moodle {#обновление-moodle}

-   Перейдём в каталог с moodle:
    ```shell
    cd /var/www/moodle/web-git
    ```
-   Обновите git:
    ```shell
    sudo -u nginx git pull
    ```
-   Посмотрим ветки:
    ```shell
    sudo -u nginx git branch -a
    ```
-   Выберите нужную ветвь:
    ```shell
    sudo -u nginx git branch --track MOODLE_501_STABLE origin/MOODLE_501_STABLE
    sudo -u nginx git checkout MOODLE_501_STABLE
    ```
-   Исправьте разрешения:
    ```shell
    chown -R nginx:nginx /var/www/moodle/
    restorecon -vR /var/www/
    ```
-   Обновите установку:
    ```shell
    sudo -u nginx /usr/bin/php /var/www/moodle/web-git/admin/cli/upgrade.php
    ```


## <span class="section-num">3</span> Ресурсы {#ресурсы}


### <span class="section-num">3.1</span> Документация Moodle {#документация-moodle}

-   <https://docs.moodle.org/405/en/Git_for_Administrators>
-   <https://docs.moodle.org/405/en/Upgrading>
-   <https://docs.moodle.org/405/en/Administration_via_command_line>
