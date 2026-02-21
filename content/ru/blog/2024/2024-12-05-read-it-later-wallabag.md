---
title: "Отложенное чтение. Wallabag"
author: ["Dmitry S. Kulyabov"]
date: 2024-12-05T11:58:00+03:00
lastmod: 2025-11-07T12:42:00+03:00
tags: ["sysadmin", "read"]
categories: ["computer-science", "self-management"]
draft: false
slug: "read-it-later-wallabag"
---

Отложенное чтение. Wallabag.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Позволяет сохранять веб-страницы для последующего чтения.
-   Лицензия: MIT license
-   Сайт с платной подпиской: <https://www.wallabag.it/>.
-   Сайт: [wallabag.org.](https://wallabag.org)
-   Репозиторий: <https://github.com/wallabag/wallabag>
-   Приложение для Android:
    -   Репозиторий: <https://github.com/wallabag/android-app>
    -   Магазин приложений:
        -   Google: <https://play.google.com/store/apps/details?id=fr.gaulupeau.apps.InThePoche>
        -   FDroid: <https://f-droid.org/packages/fr.gaulupeau.apps.InThePoche/>
-   Приложение для iOS:
    -   Репозиторий: [wallabag/ios-app](https://github.com/wallabag/ios-app)
-   Расширение браузера:
    -   Репозиторий: <https://github.com/wallabag/wallabagger>
    -   Сайт: <http://wallabag.github.io/wallabagger/>
    -   Firefox: <https://addons.mozilla.org/firefox/addon/wallabagger/>
    -   Chrome: <https://chrome.google.com/webstore/detail/wallabagger/gbmgphmejlcoihgedabhgjdkcahacjlj>
-   Приложения для Linux:
    -   Read It Later: <https://gitlab.gnome.org/World/read-it-later>
-   Ссылки по экосистеме: <https://github.com/wallabag/wallabag/wiki/wallabag-ecosystem>
-   Emacs:
    -   wallabag.el:
        -   [Emacs. Отложенное чтение. wallabag.el]({{< relref "2025-01-03--emacs-wallabagel" >}})
        -   Репозиторий: <https://github.com/chenyanming/wallabag.el>
    -   wombag:
        -   Репозиторий: <https://github.com/karthink/wombag>


## <span class="section-num">2</span> Особенности {#особенности}

-   Клиенты wallabag скачивают всю базу.
-   При разрастании базы происходит деградация производительности.
-   И в конце концов клиент просто перестаёт работать.
-   Рекомендуется удалять прочитанные статьи с сервера.


## <span class="section-num">3</span> Утилиты {#утилиты}


### <span class="section-num">3.1</span> cleanABag {#cleanabag}

-   Репозиторий: <https://git.sr.ht/~bacardi55/cleanABag>
-   cli-инструмент для удаления статей старше указанной даты из wallabag.
-   Оставляет помеченные и непрочтённые сообщения по умолчанию.
-   Конфигурационный файл credentials.json:
    ```js
    {
      "WallabagURL": "https://your.wallabag.tld",
      "ClientId": "client ID generate in your profile on wallabag",
      "ClientSecret": "client secrete generate in your profile on wallabag",
      "UserName": "your username",
      "UserPassword": "your password"
    }
    ```
-   Пример запуска.
    ```shell
    # Удалите архивные статьи старше 2021-12-31 (дата в формате YYYY-MM-DD), не затрагивая непрочтённые и отмеченные
    # Протестировать
    cleanABag prune -c /path/to/credentials.json -d "2021-12-31"
    # Удалить
    cleanABag prune -c /path/to/credentials.json -d "2021-12-31" --delete
    ```
-   Удалить статьи старше 3 месяцев:
    ```shell
    cleanABag -v -c credentials.json prune -d $(date -d "-3 month" +"%F") --delete
    ```


### <span class="section-num">3.2</span> wallabag-client {#wallabag-client}

-   [Wallabag. Консольный склиент. wallabag-client]({{< relref "2025-11-07--wallabag-cli-wallabag-client" >}})
-   Репозиторий:
-   Клиент командной строки.


## <span class="section-num">4</span> Установка {#установка}

-   Документация: <https://doc.wallabag.org/en/admin/installation/installation.html>
-   При первом логине используются следующие параметры:
    -   login: wallabag
    -   password: wallabag


## <span class="section-num">5</span> Контейнер {#контейнер}


### <span class="section-num">5.1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/wallabag/docker>
-   Dockerhub: <https://hub.docker.com/r/wallabag/wallabag/>
-   Учётные данные по умолчанию: `wallabag:wallabag`.
-   При первом запуске необходимо будет сконфигурить приложение.
-   Пусть доменное имя установки будет `wallabag.example.com`


### <span class="section-num">5.2</span> Podman {#podman}


#### <span class="section-num">5.2.1</span> Общая информация {#общая-информация}

-   [Контейнеры. podman]({{< relref "2024-12-04-containers-podman" >}})


#### <span class="section-num">5.2.2</span> Загрузка {#загрузка}

-   Скачайте контейнер:
    ```shell
    podman pull wallabag/wallabag
    ```


### <span class="section-num">5.3</span> Nginx {#nginx}

-   Настройте _nginx_:
    ```conf-unix
    server {
           listen 443 ssl http2;
           listen [::]:443 ssl http2;

           server_name wallabag.example.com;

           ssl_certificate /etc/letsencrypt/live/wallabag.example.com/fullchain.pem;
           ssl_certificate_key /etc/letsencrypt/live/wallabag.example.com/privkey.pem;

            charset utf-8;
            gzip on;
            gzip_types text/css application/javascript text/javascript application/x-javascript image/svg+xml text/plain text/xsd text/xsl text/xml image/x-icon;

            location / {
                    proxy_pass http://localhost:40401;
                    proxy_set_header X-Forwarded-Host $server_name;
                    proxy_set_header X-Forwarded-Proto https;
                    proxy_set_header X-Forwarded-For $remote_addr;
            }

    }

    server {
           listen         80;
           listen         [::]:80;
           server_name    wallabag.example.com;
           return         301 https://$server_name$request_uri;
    }
    ```


### <span class="section-num">5.4</span> Обновление {#обновление}

-   Обновление контейнера:
    ```shell
    podman pull wallabag/wallabag
    podman stop wallabag
    podman compose --file wallabag-sqlite.yaml up --detach
    ```


### <span class="section-num">5.5</span> Система на базе SQLite {#система-на-базе-sqlite}


#### <span class="section-num">5.5.1</span> Запуск вручную {#запуск-вручную}

-   Создайте каталоги для постоянных данных:
    ```shell
    mkdir -p /opt/wallabag/{data,images}
    chown -R nobody:nobody /opt/wallabag
    ```
-   Необходимо указать том для контейнера (для постоянного хранения):
    ```shell
    podman run --name wallabag -v /opt/wallabag/data:/var/www/wallabag/data -v /opt/wallabag/images:/var/www/wallabag/web/assets/images -p 40401:80 -e "SYMFONY__ENV__DOMAIN_NAME=https://wallabag.example.com" wallabag/wallabag
    ```
-   Сервер будет доступен по `http://localhost:40401`.


#### <span class="section-num">5.5.2</span> docker-compose {#docker-compose}

-   Создадим файл для docker-compose `docker-compose.yml`:
    ```yaml
    version: '3'

    networks:
        proxy-network:
            external: true

    services:
      wallabag:
        image: wallabag/wallabag:latest
        container_name: wallabag
        restart: unless-stopped
        environment:
    ​      - TZ=Etc/UTC
    ​      - SYMFONY__ENV__MAILER_DSN=smtp://127.0.0.1
    ​      - SYMFONY__ENV__MAILER_HOST=mail.example.com
    ​      - SYMFONY__ENV__FROM_EMAIL="wallabag@example.com"
    ​      - SYMFONY__ENV__SERVER_NAME="wallabag.example.com"
    ​      - SYMFONY__ENV__DOMAIN_NAME=https://wallabag.example.com
    ​      - PHP_MEMORY_LIMIT=512M
    ​      - SYMFONY__ENV__MAILER_USER=""
    ​      - SYMFONY__ENV__MAILER_PASSWORD=""
    ​      - SYMFONY__ENV__FOSUSER_REGISTRATION=false
    ​      - SYMFONY__ENV__FOSUSER_CONFIRMATION=false
    ​      - SYMFONY__ENV__TWOFACTOR_AUTH=false
        ports:
    ​      - 40401:80
        volumes:
    ​      - /opt/wallabag/images:/var/www/wallabag/web/assets/images
    ​      - /opt/wallabag/data:/var/www/wallabag/data
        networks:
    ​      - proxy-network
        healthcheck:
          test: ["CMD", "wget" ,"--no-verbose", "--tries=1", "--spider", "http://localhost/api/info"]
          interval: 1m
          timeout: 3s
    ```
-   Запуск будет выполняться следующим образом:
    ```shell
    podman compose --file wallabag-sqlite.yaml up --detach
    ```


#### <span class="section-num">5.5.3</span> Скрипт systemd {#скрипт-systemd}

-   Создаём файл сервиса `/etc/containers/systemd/wallabag.container`:
    ```conf-unix
    [Unit]
    Description=A templated wallabag container

    [Container]
    Image=wallabag
    ContainerName=wallabag
    PublishPort=40401:80

    [Service]
    # Restart service when sleep finishes
    Restart=always

    [Install]
    WantedBy=default.target

    ```
-   Запустим генератор и сообщим _systemd_ о запуске новой службы:
    ```shell
    systemctl daemon-reload
    ```
-   Запустим службу:
    ```shell
    systemctl start wallabag.service
    ```


#### <span class="section-num">5.5.4</span> Обновление через compose {#обновление-через-compose}

-   Обновить:
    ```shell
    podman compose pull
    ```
-   Остановим и переименуем старый контейнер:
    ```shell
    podman stop wallabag
    podman rename wallabag wallabag.$(date -I)
    ```
-   Собираем контейнеры:
    ```shell
    podman-compose up -d
    ```
-   Если всё нормально, удаляем старый контейнер:
    ```shell
    podman rm wallabag.<дата>
    ```


### <span class="section-num">5.6</span> Система на базе PostgreSQL {#система-на-базе-postgresql}


#### <span class="section-num">5.6.1</span> docker-compose {#docker-compose}

-   Создадим файл docker-compose `wallabag-pgsql.yaml`:
    ```yaml
    version: '3'
    services:
      wallabag:
        image: wallabag/wallabag:latest
        container_name: wallabag-pgsql
        restart: unless-stopped
        environment:
    ​      - TZ=Etc/UTC
    ​      - SYMFONY__ENV__MAILER_DSN=smtp://127.0.0.1
    ​      - SYMFONY__ENV__FROM_EMAIL=wallabag@example.com
    ​      - SYMFONY__ENV__DOMAIN_NAME=https://wallabag.example.com
    ​      - SYMFONY__ENV__SERVER_NAME=wallabag.example.com
    ​      - PHP_MEMORY_LIMIT=1024M
    ​      - PHP_MAX_EXECUTION_TIME=600
    ​      - PHP_MAX_INPUT_TIME=600
    ​      - POSTGRES_PASSWORD=<password1>
    ​      - POSTGRES_USER=postgres
    ​      - SYMFONY__ENV__DATABASE_DRIVER=pdo_pgsql
    ​      - SYMFONY__ENV__DATABASE_HOST=wallabag-db-pgsql
    ​      - SYMFONY__ENV__DATABASE_PORT=5432
    ​      - SYMFONY__ENV__DATABASE_NAME=wallabag
    ​      - SYMFONY__ENV__DATABASE_USER=wallabag
    ​      - SYMFONY__ENV__DATABASE_PASSWORD=<password2>
        ports:
    ​      - "40401:80"
        depends_on:
    ​      - wallabag-db-pgsql
      wallabag-db-pgsql:
        image: postgres:14
        container_name: wallabag-db-pgsql
        restart: unless-stopped
        environment:
    ​      - POSTGRES_PASSWORD=<password1>
    ​      - POSTGRES_USER=postgres
    ```
-   Используем postgres-14, посколку в версии 15 были сделаны исправления безопасности (<https://www.cybertec-postgresql.com/en/error-permission-denied-schema-public/>).
-   Но docker-образ для wallabag не поддерживает этого.
-   Запуск будет выполняться следующим образом:
    ```shell
    podman compose --file wallabag-pgsql.yaml up --detach
    ```


## <span class="section-num">6</span> Импорт и экспорт {#импорт-и-экспорт}


### <span class="section-num">6.1</span> Импорт Omnivore {#импорт-omnivore}

-   Экспортировал записи с Omnivore.
-   Скачал архив с большим количеством файлов json (более 600).
-   Загружать каждый файл через web-интерфейс не представлялось возможным.
-   Скопировал архив на сервер.
-   Поскольку каталог `/opt/wallabag/images` уже подмонтирован к контейнеру в каталог `/var/www/wallabag/web/assets/images`, сделал в нём каталог `omnivore` и распаковал туда архив.
-   Запустил скрипт:
    ```shell
    #!/bin/bash

    cd /opt/wallabag/images/omnivore
    for i in metadata*
    do
        podman exec -it <container-id> sh -c "cd /var/www/wallabag/web/assets/images/omnivore; /var/www/wallabag/bin/console --env=prod wallabag:import -v --importer=omnivore --markAsRead=true -- <username> ${i} "
    done
    ```


### <span class="section-num">6.2</span> Импорт Instapaper {#импорт-instapaper}

-   Скопировал файл на сервер.
-   Поскольку каталог `/opt/wallabag/images` уже подмонтирован к контейнеру в каталог `/var/www/wallabag/web/assets/images`, сделал в нём каталог `instapaper` и поместил туда файл.
-   Структура файла:
    ```csv
    URL,Title,Selection,Folder,Timestamp,Tags
    ```
-   Запустил скрипт:
    ```shell
    #!/bin/bash

    cd /opt/wallabag/images/instapaper
    for i in *.csv
    do
        podman exec -it <container-id> sh -c "cd /var/www/wallabag/web/assets/images/instapaper; /var/www/wallabag/bin/console --env=prod wallabag:import -v --importer=instapaper --markAsRead=true -- <username> ${i} "
    done
    ```


### <span class="section-num">6.3</span> Импорт Pocket {#импорт-pocket}

-   [Отложенное чтение. Pocket]({{< relref "2023-09-06-deferred-reading-pocket" >}})
-   Сохранить архив можно на странице: <https://getpocket.com/export>.
-   Скопировал архив на сервер.
-   Поскольку каталог `/opt/wallabag/images` уже подмонтирован к контейнеру в каталог `/var/www/wallabag/web/assets/images`, сделал в нём каталог `pocket` и поместил туда архив.
-   Распаковал архив.
-   Там файлы `.csv`, структура файлов:
    ```csv
    title,url,time_added,tags,status
    ```
-   Нет отметки, что файл в избранном.
-   Импортер `--importer=pocket` их не читает.
-   Переделал из под формат _Instapaper_.
-   Установил csvkit (см. [Формат CSV. csvkit]({{< relref "2023-07-06-csv-csvkit" >}})):
    ```shell
    pipx install csvkit
    ```
-   Распаковал файл `pocket.zip` в каталог `/opt/wallabag/images/pocket/in`:
    ```shell
    mkdir -p /opt/wallabag/images/pocket/in
    cp pocket.zip /opt/wallabag/images/pocket/in
    cd /opt/wallabag/images/pocket/in
    unzip pocket.zip
    ```
-   Преобразовал формат:
    ```shell
    cd /opt/wallabag/images/pocket/in
    for i in *.csv; do echo "," | csvjoin "${i}" - | csvcut -c 2,1,6,5,3,4 > ../${i}; done
    cd ../
    ```
-   Запустил скрипт:
    ```shell
    #!/bin/bash

    cd /opt/wallabag/images/instapaper
    for i in *.csv
    do
    podman exec -it <container-id> sh -c "cd /var/www/wallabag/web/assets/images/pocket; /var/www/wallabag/bin/console --env=prod wallabag:import -v --importer=instapaper --markAsRead=true -- <username> ${i} "
    done
    ```


### <span class="section-num">6.4</span> Экспорт всех записей {#экспорт-всех-записей}


#### <span class="section-num">6.4.1</span> Экспорт {#экспорт}

-   Перейдите в директорию установки wallabag.
-   Выполните команду:
    ```shell
    bin/console wallabag:export --env=prod <имя_пользователя> [<путь_к_файлу>]
    ```

    -   `<имя_пользователя>` - имя пользователя, чьи записи нужно экспортировать;
    -   `<путь_к_файлу>` - опциональный параметр, указывающий путь к файлу экспорта.

-   Пример использования:
    ```shell
    bin/console wallabag:export --env=prod john.doe /var/www/wallabag/exports/export.json
    ```
-   После выполнения команды все записи указанного пользователя будут экспортированы в выбранный файл в формате JSON.


#### <span class="section-num">6.4.2</span> Импорт {#импорт}

-   Для импорта используем следующую команду:
    ```shell
    bin/console wallabag:import --env=prod username export.json
    ```


#### <span class="section-num">6.4.3</span> Экспорта из контейнера {#экспорта-из-контейнера}

-   Получите идентификатор контейнера:
    ```shell
    podman container list
    ```
-   Поскольку каталог `/opt/wallabag/images` уже подмонтирован к контейнеру в каталог `/var/www/wallabag/web/assets/images`, будем экспортировать в его.
-   Подключитесь к контейнеру и выполните экспорт:
    ```shell
    podman exec -it <container-id> sh -c "bin/console wallabag:export --env=prod john.doe /var/www/wallabag/web/assets/images/$(date -I).json"
    ```
