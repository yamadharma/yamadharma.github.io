---
title: "Установка gitea"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-29T20:10:00+03:00
lastmod: 2024-07-20T16:15:00+03:00
tags: ["git", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "install-gitea"
---

Установка gitea.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Информация {#информация}


### <span class="section-num">1.1</span> Поддерживаемые базы данных {#поддерживаемые-базы-данных}

-   MySQL (&gt;=5.7)
-   PostgreSQL (&gt;=10)
-   SQLite3
-   MSSQL (&gt;=2008R2 SP3)
-   TiDB (MySQL protocol)


## <span class="section-num">2</span> Пререквизиты {#пререквизиты}

-   Установите базовый сервер (см. [Rocky Linux. Установка сервера]({{< relref "2022-08-12-rockylinux-server-installation" >}})).


### <span class="section-num">2.1</span> Пользователь {#пользователь}

-   Создадим пользователя для работы с gitea.
    -   Ubuntu/Debian:
        ```shell
        adduser \
                  --system \
                  --shell /bin/bash \
                  --gecos 'Git Version Control' \
                  --group \
                  --disabled-password \
                  --home /home/git \
                  git
        ```
    -   Fedora/RHEL/CentOS:
        ```shell
        groupadd --system git
        adduser \
                  --system \
                  --shell /bin/bash \
                  --comment 'Git Version Control' \
                  --gid git \
                  --home-dir /home/git \
                  --create-home \
                  git
        ```


### <span class="section-num">2.2</span> База данных {#база-данных}

-   Установите нужную базу данных.


#### <span class="section-num">2.2.1</span> SqLite {#sqlite}

-   Установите sqlite:
    ```shell
    dnf install sqlite
    ```
-   Настроек не требуется.


#### <span class="section-num">2.2.2</span> PostgreSQL {#postgresql}

-   Установите postgresql:
    ```shell
    dnf install postgresql-server postgresql
    ```
-   Создайте начальную базу данных:
    ```shell
    /usr/bin/postgresql-setup --initdb
    ```
-   Запустите PostgreSQL:
    ```shell
    systemctl enable --now postgresql
    ```
-   Если требуется удалённая настройка PostgreSQL, добавьте адрес для прослушивания вашего IP-адреса, отредактировав `listen_addresses` в `/var/lib/pgsql/data/postgresql.conf`:
    ```conf-unix
    listen_addresses = 'localhost, 203.0.113.3'
    ```
-   PostgreSQL по умолчанию использует схему запрос-ответ `md5` для аутентификации.
    -   В настоящее время эта схема не считается безопасной.
    -   Вместо этого используйте схему `SCRAM-SHA-256`, отредактировав `postgresql.conf`:
        ```conf-unix
        password_encryption = scram-sha-256
        ```
-   На сервере базы данных войдите в консоль базы данных как суперпользователь:
    ```shell
    su -c psql - postgres
    ```
-   Создайте пользователя базы данных с правами входа и паролем:
    ```shell
    CREATE ROLE gitea WITH LOGIN PASSWORD 'gitea';
    ```

    -   Замените имя пользователя и пароль соответствующим образом.
    -   Сменить пароль потом можно будет следующим образом:
        -   На сервере базы данных войдите в консоль базы данных как суперпользователь:
            ```shell
            su -c psql - postgres
            ```
        -   Смените пароль пользователю `gitea`:
            ```shell
            \password gitea
            ```

-   Создайте базу данных с кодировкой UTF-8, принадлежащую пользователю базы данных, созданному ранее:
    ```shell
    CREATE DATABASE gitea WITH OWNER gitea TEMPLATE template0 ENCODING UTF8 LC_COLLATE 'ru_RU.UTF-8' LC_CTYPE 'ru_RU.UTF-8';
    ```

    -   Замените имя базы данных соответствующим образом.
-   Разрешите пользователю базы данных доступ к базе данных, созданной выше, добавив следующее правило аутентификации в файл `/var/lib/pgsql/data/pg_hba.conf`.
    -   Для локальной базы данных:
        ```conf-unix
        local    gitea    gitea    scram-sha-256
        host     gitea    gitea    127.0.0.1/32    scram-sha-256
        ```
    -   Для удаленной базы данных:
        ```shell
        host    gitea    gitea    192.0.2.10/32    scram-sha-256
        ```
    -   Замените имя базы данных, пользователя и IP-адрес экземпляра Gitea на свои собственные.
-   Перезапустите PostgreSQL, чтобы применить новые правила аутентификации:
    ```shell
    systemctl restart postgresql.service
    ```
-   На вашем сервере Gitea проверьте соединение с базой данных.
    -   Для локальной базы данных:
        ```shell
        psql -U gitea -d giteadb
        ```
    -   Для удаленной базы данных:
        ```shell
        psql "postgres://gitea@203.0.113.3/giteadb"
        ```
    -   `gitea` : пользователь базы данных,
    -   `giteadb` : имя базы данных;
    -   203.0.113.3 : IP-адрес экземпляра вашей базы данных.
-   Вам будет предложено ввести пароль для пользователя базы данных и подключиться к базе данных.


### <span class="section-num">2.3</span> Брандмауэр {#брандмауэр}

-   Если не будете включать проксирование через web-сервер, то разрешите работать по порту 3000:
    ```shell
    firewall-cmd --permanent --zone=public --add-port=3000/tcp
    firewall-cmd --reload
    ```


## <span class="section-num">3</span> Установка {#установка}


### <span class="section-num">3.1</span> Установка бинарного пакета {#установка-бинарного-пакета}

-   Пакета `gitea` в Rocky Linux нет.
-   Устанавливать будем в локальную иерархию:
    ```shell
    cd /usr/local/bin
    ```
-   Скачаем последнюю версию `gitea`:
    ```shell
    curl -s  https://api.github.com/repos/go-gitea/gitea/releases/latest |grep browser_download_url  |  cut -d '"' -f 4  | grep '\linux-amd64$' | wget -i - -O /usr/local/bin/gitea
    ```
-   Установим права на выполнение файла:
    ```shell
    chmod +x /usr/local/bin/gitea
    ```
-   Восстановим метки безопасности:
    ```shell
    restorecon -rv /usr/local/bin/gitea
    ```


### <span class="section-num">3.2</span> Структура папок {#структура-папок}

-   Создадим рабочую структур папок:
    ```shell
    mkdir -p /etc/gitea /var/lib/gitea/{custom,data,indexers,public,log}
    chown git:git /var/lib/gitea/{data,indexers,log}
    chmod 750 /var/lib/gitea/{data,indexers,log}
    chown root:git /etc/gitea
    chmod 770 /etc/gitea
    ```


### <span class="section-num">3.3</span> Сервис systemd {#сервис-systemd}

-   Скачает файл сервиса:
    ```shell
    wget https://raw.githubusercontent.com/go-gitea/gitea/master/contrib/systemd/gitea.service -P /etc/systemd/system/
    ```
-   Перечитает файлы сервисов:
    ```shell
    systemctl daemon-reload
    ```


### <span class="section-num">3.4</span> Запуск gitea {#запуск-gitea}

-   Запустим gitea:
    ```shell
    systemctl enable --now gitea
    ```


## <span class="section-num">4</span> Проксирование {#проксирование}

-   Можно настроить проксирование gitea через nginx.
-   Это не обязательно.


### <span class="section-num">4.1</span> Установка nginx {#установка-nginx}

-   Установим nginx:
    ```shell
    dnf install nginx
    ```


### <span class="section-num">4.2</span> Брандмауэр {#брандмауэр}

-   Настроим брандмауэр:
    ```shell
    firewall-cmd --add-servic={http,https} --permanent
    firewall-cmd --reload
    ```


### <span class="section-num">4.3</span> SELinux {#selinux}

-   Разрешите nginx перенаправление:
    ```shell
    setsebool -P httpd_can_network_connect 1
    setsebool httpd_can_network_connect 1
    ```


### <span class="section-num">4.4</span> Конфигурация nginx {#конфигурация-nginx}

-   В файле `/etc/nginx/conf.d/gitea.conf` опишем конфигурацию для перенаправления:
    ```conf-unix
    server {
            server_name hub.example.com;

            location / {
                client_max_body_size 512M;
                proxy_pass http://localhost:3000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
    }
    ```


### <span class="section-num">4.5</span> Конфигурационный файл app.ini {#конфигурационный-файл-app-dot-ini}

-   Добавьте в `/etc/gitea/app.ini` в секцию `[security]` чтобы задать доверенные прокси-серверы:
    ```conf-unix
    [security]
    REVERSE_PROXY_LIMIT = 1
    REVERSE_PROXY_TRUSTED_PROXIES = 127.0.0.1/8
    ```


### <span class="section-num">4.6</span> Настройка SSL {#настройка-ssl}

-   Установите _certbot_ (см. [Клиенты ACME. Certbot]({{< relref "2022-05-02-acme-clients-certbot" >}}))
-   Создайте сертификат.
-   Конфигурационный файл _Nginx_ будет иметь вид:
    ```conf-unix
    server {
        listen              443 ssl http2;
        listen              [::]:443 ssl http2;

        server_name hub.example.com;

        ssl_certificate /etc/letsencrypt/live/hub.example.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/hub.example.com/privkey.pem;
        include /etc/letsencrypt/options-ssl-nginx.conf;
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

         charset utf-8;
         gzip on;
         gzip_types text/css application/javascript text/javascript application/x-javascript image/svg+xml text/plain text/xsd text/xsl text/xml image/x-icon;

         proxy_read_timeout 300;
         proxy_connect_timeout 300;
         proxy_send_timeout 300;


        location / {
            client_max_body_size 512M;
            proxy_pass http://localhost:3000;
            proxy_set_header Connection $http_connection;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }

    server {
        # Redirect HTTP traffic to HTTPS
        listen         80;
        listen         [::]:80;
        server_name hub.example.com;
        return         301 https://$server_name$request_uri;
    }
    ```


## <span class="section-num">5</span> Начальная конфигурация {#начальная-конфигурация}

-   Без проксирования: подключитесь к хосту с gitea по порту 3000 (`http://yourserver-ip-address:3000`).
-   C проксированием: подключитесь к хосту с gitea (`http://yourserver-ip-address`).
-   Заполните настройки gitea:
    -   Тип базы данных: PostgreSQL.
    -   Имя пользователя: gitea
    -   Пароль: пароль, который Вы задали.
    -   Имя базы данных: gitea


## <span class="section-num">6</span> Дополнительные настройки {#дополнительные-настройки}


### <span class="section-num">6.1</span> fail2ban {#fail2ban}

-   Настроим fail2ban (см. [fail2ban. Основные настройки]({{< relref "2023-10-30-fail2ban-basic-settings" >}}))
-   Документация: <https://docs.gitea.com/next/administration/fail2ban-setup>
-   Добавьте фильтр `/etc/fail2ban/filter.d/gitea.conf`:
    ```conf-unix
    # gitea.conf
    [Definition]
    failregex =  .*(Failed authentication attempt|invalid credentials|Attempted access of unknown user).* from <HOST>
    ignoreregex =
    ```
-   Добавьте ограничение `/etc/fail2ban/jail.d/80-gitea.conf`:
    ```conf-unix
    [gitea]
    enabled = true
    filter = gitea
    logpath = /var/log/gitea/gitea.log
    maxretry = 10
    findtime = 3600
    bantime = 900
    action = iptables-allports
    ```
-   Поправьте секцию `[log]` в `/etc/gitea/app.ini`:
    ```conf-unix
    [log]
    MODE = file
    LEVEL = info
    ROOT_PATH = /var/log/gitea
    ```
-   Создайте нужный каталог:
    ```shell
    mkdir -p /var/log/gitea
    chown git:git /var/log/gitea
    ```


### <span class="section-num">6.2</span> Имя ветки по умолчанию {#имя-ветки-по-умолчанию}

-   Gitea устанавливает имя главной ветки по умолчанию на `main`.
-   Имя ветка по умолчанию можно установить в файле `/etc/gitea/app.ini`:
    ```conf-unix
    [repository]
    DEFAULT_BRANCH = master
    ```
