---
title: "NetBox. Установка"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-19T18:13:00+03:00
lastmod: 2025-03-26T13:52:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "netbox-install"
---

Установка NetBox.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Системные требования {#системные-требования}


## <span class="section-num">2</span> Предварительная подготовка {#предварительная-подготовка}

-   Будем устанавливать на отдельную операционную систему.
-   [Rocky Linux. Установка сервера]({{< relref "2022-08-12-rockylinux-server-installation" >}})


## <span class="section-num">3</span> Установка компонент {#установка-компонент}


### <span class="section-num">3.1</span> Python {#python}

-   Установим python-3.12:
    ```shell
    dnf -y install python3.12 python3.12-devel
    ```
-   Добавим варианты python в список альтернатив:
    ```shell
    alternatives --remove python /usr/bin/python3.9
    alternatives --install /usr/bin/python python /usr/bin/python3.12 1
    ```
-   Выберем необходимую версию python:
    ```shell
    alternatives --config python
    ```


### <span class="section-num">3.2</span> Postgres {#postgres}

-   Версии, которая идёт в комплекте с дистрибутивом, достаточно.
-   Но лучше установить версию поновее.
-   Смотрим, какие версии в наличии:
    ```shell
    dnf module list postgresql
    ```
-   Установим postgresql-16:
    ```shell
    dnf module -y install postgresql:16
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
-   Замените параметры внутреннего подключения:
    ```shell
    sed -i -e 's/^\(host[ ]*all.*\)ident/\1scram-sha-256/' /var/lib/pgsql/data/pg_hba.conf
    ```
-   Запустим postgres:
    ```shell
    systemctl enable --now postgresql
    ```
-   Подключимся к базе данных:
    ```shell
    sudo -u postgres psql
    ```
-   Создадим базу данных (укажите необходимый пароль):
    ```sql
    CREATE DATABASE netbox;
    CREATE USER netbox WITH PASSWORD '<password>';
    ALTER DATABASE netbox OWNER TO netbox;
    \connect netbox;
    GRANT CREATE ON SCHEMA public TO netbox;
    \q
    ```
-   Проверьте подключение к базе данных:
    ```shell
    psql --username netbox --password --host localhost netbox
    ```
-   После подключения посмотрите параметры соединения:
    ```sql
    \conninfo
    \q
    ```


### <span class="section-num">3.3</span> Redis {#redis}

-   Redis --- быстрое хранилище данных типа ключ‑значение в памяти.
-   С 2024 года сменила лицензию на SSPL (закрытую).
-   Установим redis:
    ```shell
    dnf -y install redis
    ```
-   Запустим redis:
    ```shell
    systemctl enable --now redis
    ```
-   Проверим, что сервер работает:
    ```shell
    redis-cli ping
    ```

    -   В качестве ответа должен быть `PONG`.


### <span class="section-num">3.4</span> NetBox {#netbox}


#### <span class="section-num">3.4.1</span> Предварительная установка NetBox {#предварительная-установка-netbox}

-   Установим необходимое программное обеспечение:
    ```shell
    dnf -y install gcc libxml2-devel libxslt-devel libffi-devel libpq-devel openssl-devel redhat-rpm-config git
    ```
-   Клонируем репозиторий:
    ```shell
    mkdir -p /opt/netbox/
    cd /opt/netbox
    git clone -b master --depth 1 https://github.com/netbox-community/netbox.git .
    ```
-   Создадим нового системного пользователя:
    ```shell
    groupadd --system netbox
    adduser --system -m -g netbox netbox
    chown -R netbox:netbox /opt/netbox
    chown --recursive netbox /opt/netbox/netbox/media/
    chown --recursive netbox /opt/netbox/netbox/reports/
    chown --recursive netbox /opt/netbox/netbox/scripts/
    ```


#### <span class="section-num">3.4.2</span> Конфигурация Netbox {#конфигурация-netbox}

-   Создадим файл конфигурации:
    ```shell
    cd /opt/netbox/netbox/netbox/
    cp configuration_example.py configuration.py
    ```
-   Сконфигурим необходимые параметры.

<!--list-separator-->

1.  ALLOWED_HOSTS

    -   Список допустимых имен хостов и IP-адресов, по которым можно связаться с этим сервером (имя вашего сервера).
    -   Необходимо указать хотя бы одно имя или IP-адрес, например:
        ```conf-unix
        ALLOWED_HOSTS = ['netbox.example.com', '192.0.2.123']
        ```
    -   Если вы еще не уверены, каким будет доменное имя и/или IP-адрес установки NetBox, вы можете установить подстановочный знак (звездочку), чтобы разрешить все значения хоста:
        ```shell
        ALLOWED_HOSTS = ['*']
        ```

<!--list-separator-->

2.  DATABASE

    -   Сведения о конфигурации базы данных.
    -   Нужно задать имя пользователя и пароль, используемые при настройке PostgreSQL.
    -   Если служба запущена на удалённом хосте, обновите параметры HOST и PORT:
        ```conf-unix
        DATABASE = {
            'NAME': 'netbox',               # Database name
            'USER': 'netbox',               # PostgreSQL username
            'PASSWORD': '<password>',           # PostgreSQL password
            'HOST': 'localhost',            # Database server
            'PORT': '',                     # Database port (leave blank for default)
            'CONN_MAX_AGE': 300,            # Max database connection age (seconds)
        }
        ```

<!--list-separator-->

3.  REDIS

    -   NetBox требует указания двух отдельных баз данных Redis: `tasks` и `caching`.
    -   Обе они могут предоставляться одной и той же службой Redis, однако каждый из них должен иметь уникальный числовой идентификатор базы данных.
        ```conf-unix
        REDIS = {
            'tasks': {
                'HOST': 'localhost',      # Redis server
                'PORT': 6379,             # Redis port
                'PASSWORD': '',           # Redis password (optional)
                'DATABASE': 0,            # Database ID
                'SSL': False,             # Use SSL (optional)
            },
            'caching': {
                'HOST': 'localhost',
                'PORT': 6379,
                'PASSWORD': '',
                'DATABASE': 1,            # Unique ID for second database
                'SSL': False,
            }
        }
        ```

<!--list-separator-->

4.  SECRET_KEY

    -   Этому параметру должен быть назначен случайно сгенерированный ключ, используемый в качестве соли для хеширования и связанных с ним криптографических функций.
    -   Этот ключ должен быть уникальным для данной установки, и его рекомендуется иметь длину не менее 50 символов. Его не следует использовать за пределами локальной системы.
    -   Простой скрипт Python с именем `generate_secret_key.py` предоставляется в родительском каталоге для помощи в создании подходящего ключа:
        ```shell
        python3 ../generate_secret_key.py
        ```
    -   В случае высокодоступной установки с несколькими веб-серверами `SECRET_KEY` должен быть одинаковым на всех серверах, чтобы поддерживать постоянное состояние сеанса пользователя.


#### <span class="section-num">3.4.3</span> Развёртывание NetBox {#развёртывание-netbox}

-   Скрипт обновления выполнит следующие действия:
    -   создание виртуального окружения Python;
    -   установка  необходимых пакетов Python;
    -   запуск миграции схемы базы данных;
    -   создание локальной документации;
    -   объединение статических файлов ресурсов на диске.
-   Запускаем скрипт установки Netbox:
    ```shell
    sudo -u netbox PYTHON=/usr/bin/python3.12 /opt/netbox/upgrade.sh
    ```


#### <span class="section-num">3.4.4</span> Суперпользователь {#суперпользователь}

-   NetBox не имеет предустановленных учётных записей пользователей.
-   Необходимо создать суперпользователя (административную учетную запись), чтобы иметь возможность войти в NetBox.
-   Войдём в виртуальную среду Python:
    ```shell
    source /opt/netbox/venv/bin/activate
    ```
-   Создадим учётную запись суперпользователя:
    ```shell
    cd /opt/netbox/netbox
    python3 manage.py createsuperuser
    ```
-   Указывать адрес электронной почты пользователя не обязательно.


#### <span class="section-num">3.4.5</span> Планирование очистки рабочей среды {#планирование-очистки-рабочей-среды}

-   NetBox включает в себя скрипт `housekeeping`, который выполняет повторяющиеся задачи очистки (очистка старых сеансов и записей об изменениях с истекшим сроком действия).
-   Установим его:
    ```shell
    sudo ln -s /opt/netbox/contrib/netbox-housekeeping.sh /etc/cron.daily/netbox-housekeeping
    ```


#### <span class="section-num">3.4.6</span> Брандмауэр {#брандмауэр}

-   Настроим брандмауэр:
    ```shell
    firewall-cmd --add-port=8000/tcp --permanent
    firewall-cmd --reload
    ```


### <span class="section-num">3.5</span> Gunicorn {#gunicorn}

-   NetBox работает как приложение WSGI для HTTP-сервера.
-   Можно использовать Gunicorn или uWSGI.
-   Скопируем файл конфигурации:
    ```shell
    sudo -u netbox cp /opt/netbox/contrib/gunicorn.py /opt/netbox/gunicorn.py
    ```
-   Установим скрипты для systemd:
    ```shell
    cp -v /opt/netbox/contrib/*.service /etc/systemd/system/
    systemctl daemon-reload
    ```
-   Запустим сервисы `netbox` и `netbox-rq`:
    ```shell
    systemctl enable --now netbox netbox-rq
    ```


### <span class="section-num">3.6</span> HTTP-сервер {#http-сервер}


#### <span class="section-num">3.6.1</span> Nginx {#nginx}

-   Установим nginx.
-   Выберем нужный модуль:
    ```shell
    dnf module list nginx
    dnf module switch-to nginx:1.24
    dnf -y install nginx
    ```
-   Скопируем шаблон файла конфигурации:
    ```shell
    cp /opt/netbox/contrib/nginx.conf /etc/nginx/conf.d/netbox.conf
    ```
-   Замените `netbox.example.com` именем домена или IP-адресом сервера.


#### <span class="section-num">3.6.2</span> SSL-сертификат {#ssl-сертификат}

-   Сгенерим самоподписанный SSL-сертификат в качестве заглушки:
    ```shell
    mkdir -p /etc/ssl/private /etc/ssl/certs
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/netbox.key -out /etc/ssl/certs/netbox.crt
    ```
-   Потом заменим его на нормальный.


#### <span class="section-num">3.6.3</span> SELinux {#selinux}

-   Настройте политики SELinux:
    ```shell
    setsebool httpd_can_network_connect 1
    setsebool -P httpd_can_network_connect 1
    ```


#### <span class="section-num">3.6.4</span> Брандмауэр {#брандмауэр}

-   Настроим брандмауэр:
    ```shell
    firewall-cmd --add-servic={http,https} --permanent
    firewall-cmd --reload
    ```


#### <span class="section-num">3.6.5</span> Запуск http-сервера {#запуск-http-сервера}

-   Запустим nginx:
    ```shell
    systemctl enable --now nginx
    ```


### <span class="section-num">3.7</span> Установка https-сертификата LetsEncrypt {#установка-https-сертификата-letsencrypt}

-   [Клиенты ACME. Certbot]({{< relref "2022-05-02-acme-clients-certbot" >}})


#### <span class="section-num">3.7.1</span> Установка _certbot_ {#установка-certbot}

-   Проверьте, что установлен репозитории EPEL:
    ```shell
    dnf -y install epel-release
    ```
-   Установите _certbot_:
    ```shell
    dnf -y install certbot
    ```
-   Для веб-сервера Apache:
    ```shell
    dnf -y install python3-certbot-apache
    ```
-   Для веб-сервера Nginx:
    ```shell
    dnf -y install python3-certbot-nginx
    ```


#### <span class="section-num">3.7.2</span> Сервер _Nginx_ {#сервер-nginx}

-   Плагин `certbot-nginx` предоставляет автоматическую настройку _Nginx HTTP Server_.
-   Он пытается найти конфигурацию каждого домена, а также добавляет рекомендованные для безопасности параметры, настройки использования сертификатов и пути к сертификатам Let's Encrypt.
-   Первоначальная настройка виртуальных хостов:
    ```shell
    certbot --nginx
    ```
-   Обновление сертификатов:
    ```shell
    certbot renew
    ```
-   Изменение сертификатов без изменения файлов конфигурации _nginx_:
    ```shell
    certbot --nginx certonly
    ```


#### <span class="section-num">3.7.3</span> Конфигурационный файл _Nginx_ {#конфигурационный-файл-nginx}

-   В файле `/etc/nginx/conf.d/netbox.conf` должны быть следующие записи:
    ```conf-unix
    ssl_certificate /etc/letsencrypt/live/yourwebsite.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourwebsite.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
    ```


## <span class="section-num">4</span> Обновление {#обновление}


### <span class="section-num">4.1</span> Пререквизиты {#пререквизиты}

-   Проверьте, что все компоненты соответствуют необходимым версиям.


### <span class="section-num">4.2</span> Скачайте релиз Git {#скачайте-релиз-git}

-   Сначала определите последнюю версию, посетив страницу (<https://github.com/netbox-community/netbox/releases>) или выполнив следующее команды:
    ```shell
    cd /opt/netbox
    sudo -u netbox git fetch --tags
    sudo -u netbox git describe --tags $(git rev-list --tags --max-count=1)
    ```
-   Установите нужный релиз, указав его тег:
    ```shell
    sudo -u netbox git checkout v4.2.6
    ```


### <span class="section-num">4.3</span> Запустите скрипт обновления {#запустите-скрипт-обновления}

-   Проверьте, что все необходимые дополнительные пакеты Python перечислены в `local_requirements.txt`.
-   Запустите скрипт обновления:
    ```shell
    sudo -u netbox PYTHON=/usr/bin/python3.12 ./upgrade.sh
    ```
-   Этот скрипт выполняет следующие действия:
    -   Уничтожает и восстанавливает виртуальную среду Python.
    -   Устанавливает все необходимые пакеты Python (перечислены в `requirements.txt` )
    -   Устанавливает любые дополнительные пакеты из `local_requirements.txt`
    -   Применяет все миграции базы данных, которые были включены в релиз
    -   Создает документацию локально (для использования в автономном режиме)
    -   Собирает все статические файлы, которые будут обслуживаться службой HTTP.
    -   Удаляет устаревшие типы контента из базы данных
    -   Удаляет все просроченные сеансы пользователей из базы данных


### <span class="section-num">4.4</span> Перезапустите службы NetBox {#перезапустите-службы-netbox}

-   Перезапустите службы gunicorn и RQ:
    ```shell
    sudo systemctl restart netbox netbox-rq
    ```
