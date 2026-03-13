---
title: "rss. Сервер FreshRSS"
author: ["Dmitry S. Kulyabov"]
date: 2025-06-02T14:37:00+03:00
lastmod: 2025-08-07T14:15:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "rss-server-freshrss"
---

rss. Сервер FreshRSS.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://freshrss.org/>
-   Репозиторий: <https://github.com/FreshRSS/FreshRSS/>
-   Документация: <https://freshrss.github.io/FreshRSS/>
-   Образ docker: <https://hub.docker.com/r/freshrss/freshrss/>


## <span class="section-num">2</span> Установка в контейнер {#установка-в-контейнер}


### <span class="section-num">2.1</span> Создание контейнера {#создание-контейнера}

-   Будем делать конфигурацию в каталоге `~/containers/freshrss`:
    ```shell
    mkdir -p ~/containers/freshrss
    cd ~/containers/freshrss
    ```
-   Переменные поместим в файл `.env`:
    ```conf-unix
    # Example of environment file for docker-compose
    # Copy this file into your own `.env` file

    # ================================
    # FreshRSS
    # ================================

    ADMIN_EMAIL=admin@example.net

    # Published port for development or local use (optional)
    PUBLISHED_PORT=8280

    # =========================================
    # For automatic FreshRSS install (optional)
    # =========================================

    ADMIN_PASSWORD=freshrss
    ADMIN_API_PASSWORD=freshrss

    # Address at which the FreshRSS instance will be reachable:
    BASE_URL=https://freshrss.example.net

    # Database server (not relevant if using default SQLite)
    # Use the name of the Docker container if running on the same machine
    DB_HOST=freshrss-db

    # ===========================================================
    # Database credentials (not relevant if using default SQLite)
    # ===========================================================

    # Database to use
    DB_BASE=freshrss

    # User in the freshrss database
    DB_USER=freshrss

    # Password for the defined user
    DB_PASSWORD=freshrss
    ```

    -   Конфигурацию для docker делаем в файле `docker-compose.yml`:
        ```yaml
        volumes:
          data:
          extensions:

        services:
          freshrss:
            image: freshrss/freshrss:latest
            # # Optional build section if you want to build the image locally:
            # build:
            #   # Pick #latest (slow releases) or #edge (rolling release) or a specific release like #1.21.0
            #   context: https://github.com/FreshRSS/FreshRSS.git#latest
            #   dockerfile: Docker/Dockerfile-Alpine
            container_name: freshrss
            hostname: freshrss
            restart: unless-stopped
            logging:
              options:
                max-size: 10m
            volumes:
        ​      - data:/var/www/FreshRSS/data
        ​      - extensions:/var/www/FreshRSS/extensions
            environment:
              TZ: Europe/Paris
              CRON_MIN: '3,33'
              TRUSTED_PROXY: 172.16.0.1/12 192.168.0.1/16
        ```
    -   Собираем контейнеры:
        ```shell
        podman-compose up -d
        ```


### <span class="section-num">2.2</span> Обновление {#обновление}

-   Обновить:
    ```shell
    podman compose pull
    ```
-   Остановим и переименуем старый контейнер:
    ```shell
    podman stop freshrss
    podman rename freshrss freshrss.$(date -I)
    ```
-   Собираем контейнеры:
    ```shell
    podman-compose up -d
    ```
-   Если всё нормально, удаляем старый контейнер:
    ```shell
    podman rm freshrss.<дата>
    ```


### <span class="section-num">2.3</span> Обратный proxy {#обратный-proxy}

-   Настроим обратный proxy на nginx:
    ```conf-unix
    server {
           listen 443 ssl http2;
           listen [::]:443 ssl http2;
           server_name freshrss.example.net;

           ssl_certificate /etc/letsencrypt/live/freshrss.example.net/fullchain.pem;
           ssl_certificate_key /etc/letsencrypt/live/freshrss.example.net/privkey.pem;

           charset utf-8;
           gzip on;
           gzip_types text/css application/javascript text/javascript application/x-javascript image/svg+xml text/plain text/xsd text/xsl text/xml image/x-icon;

           location / {
                    proxy_pass http://localhost:8280/;
                    add_header X-Frame-Options SAMEORIGIN;
                    add_header X-XSS-Protection "1; mode=block";
                    proxy_redirect off;
                    proxy_buffering off;
                    proxy_set_header X-Forwarded-Host $server_name;
                    proxy_set_header X-Forwarded-Proto $scheme;
                    proxy_set_header X-Forwarded-For $remote_addr;
                    proxy_set_header Host $host;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_read_timeout 90;

                    # Forward the Authorization header for the Google Reader API.
                    proxy_set_header Authorization $http_authorization;
                    proxy_pass_header Authorization;
          }
    }

    server {
           listen         80;
           listen         [::]:80;
           server_name    freshrss.example.net;
           return         301 https://$server_name$request_uri;
    }
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      /etc/nginx/conf.d/rss.conf
    </div>


### <span class="section-num">2.4</span> Информация {#информация}

-   Узнать расположение каталога с данными:
    ```shell
    podman volume inspect freshrss_data | grep -i mountpoint
    ```
-   Обычно это каталог `/var/lib/containers/storage/volumes/freshrss_data/_data`.


## <span class="section-num">3</span> Клиенты {#клиенты}


### <span class="section-num">3.1</span> Подключение мобильного приложения {#подключение-мобильного-приложения}

-   Чтобы использовать FreshRSS с мобильным приложением, необходимо установить пароль для API в профиле FreshRSS.
-   Пароль API используется для аутентификации с помощью API FreshRSS, который позволяет мобильным приложениям получать и управлять вашими каналами.
-   Этот пароль отличается от вашего обычного пароля для входа и используется специально для доступа к API.
    -   Войдите в свой экземпляр FreshRSS через веб-браузер.
    -   Перейдите на страницу своего профиля ( обычно её можно найти под значком шестеренки в правом верхнем углу или перейдя в раздел «Настройки» &gt; «Профиль»).
    -   Найдите раздел «Управление API» в своем профиле.
    -   Введите желаемый пароль API в соответствующее поле и отправьте его.
    -   Используйте этот пароль API вместе со своим именем пользователя при входе в мобильное приложение.
