---
title: "Indico. Обновление"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-24T11:23:00+03:00
lastmod: 2024-09-24T15:45:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "indico-update"
---

Обновление Indico.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Обновление пререквизитов {#обновление-пререквизитов}


### <span class="section-num">1.1</span> Postgres {#postgres}

-   Делается, если нужно изменить версию PostgreSQL.


#### <span class="section-num">1.1.1</span> Бэкап базы данных {#бэкап-базы-данных}

-   Сделайте бекап базы:
    ```shell
    sudo -u postgres pg_dump -U postgres indico > indico.sql
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
    CREATE DATABASE indico;
    CREATE USER indico WITH PASSWORD '<password>';
    CREATE USER indico;
    ALTER DATABASE indico OWNER TO indico;
    \connect indico;
    GRANT CREATE ON SCHEMA public TO indico;
    \q
    ```
-   Добавьте расширение:
    ```shell
    su - postgres -c 'psql indico -c "CREATE EXTENSION unaccent; CREATE EXTENSION pg_trgm;"'
    ```
-   Проверьте подключение к базе данных:
    ```shell
    psql --username indico --password --host localhost indico
    ```
-   После подключения посмотрите параметры соединения:
    ```sql
    \conninfo
    \q
    ```
-   Восстановите данные из резервной копии:
    ```shell
    sudo -u postgres psql -d indico -f indico.sql
    ```


## <span class="section-num">2</span> Обновление Indico {#обновление-indico}

-   Остановим Celery:
    ```shell
    sudo systemctl stop indico-celery.service
    ```
-   Теперь переключитесь на пользователя `indico` и активируйте virtualenv:
    ```shell
    su - indico
    source ~/.venv/bin/activate
    ```
-   Проверьте версию Python:
    ```shell
    python -V
    ```
-   Если версия &lt; 3.12, то установим необходимую версию Python:
    ```shell
    indico setup upgrade-python --force-version 3.12
    ```
-   Обновите indico:
    ```shell
    pip install setuptools
    pip install -U indico
    indico setup create-symlinks ~/web/
    ```
-   Обновите плагины:
    ```shell
    pip install -U indico-plugins
    ```
-   Обновите схемы базы данных:
    ```shell
    indico db upgrade
    indico db --all-plugins upgrade
    ```
-   Перезапустите uWSGI:
    ```shell
    touch ~/web/indico.wsgi
    ```
-   Снова запустите Celery:
    ```shell
    sudo systemctl start indico-celery.service
    ```


## <span class="section-num">3</span> Установка Indico {#установка-indico}

-   Если версия слишком старая, либо Вы обновили систему, лучше установить бинарники заново.
-   Удалите старую установку python:
    ```shell
    rm -rf /opt/indico/.pyenv
    ```
-   Теперь переключитесь на пользователя `indico`:
    ```shell
    su - indico
    ```
-   Загрузите установщик:
    ```shell
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    ```
-   Установите python-3.12:
    ```shell
    source ~/.bashrc
    pyenv install 3.12
    pyenv global 3.12
    ```
-   Установите indico:
    ```shell
    python -m venv --upgrade-deps --prompt indico ~/.venv
    source ~/.venv/bin/activate
    echo 'source ~/.venv/bin/activate' >> ~/.bashrc
    pip install setuptools wheel
    pip install uwsgi
    pip install indico
    ```


## <span class="section-num">4</span> Ресурсы {#ресурсы}

-   Документация: <https://docs.getindico.io/en/stable/installation/upgrade/>
