---
title: "Ansible. Графический интерфейс Semaphore UI"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-31T20:11:00+03:00
lastmod: 2025-12-11T14:51:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "ansile-semaphore-ui"
---

Ansible. Графический интерфейс Semaphore UI.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт:
    -   <https://www.semaphoreui.ru/>
    -   <https://semaphoreui.com/>
-   Коммерческий вариант:
    -   <https://www.semaphoreui.ru/prof/>
-   Репозиторий: <https://github.com/semaphoreui/semaphore>
-   Документация: <https://docs.semaphoreui.com/>
-   Лицензия: MIT.
-   Упрощённый интерфейс для Ansible.
-   Интуитивный интерфейс с drag-and-drop для создания рабочих процессов.
-   Изоляция проектов через независимые среды выполнения.
-   Контроль доступа с детализированной настройкой прав.
-   Аудит активности для отслеживания изменений.
-   Поддержка Terraform и Bash-скриптов.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Бинарные пакеты {#бинарные-пакеты}


#### <span class="section-num">2.1.1</span> Общая информация {#общая-информация}

-   Страница: <https://www.semaphoreui.ru/install/binary>
-   Там же находится конструктор для файлов конфигурации.


#### <span class="section-num">2.1.2</span> База данных {#база-данных}

-   Предварительно следует установить необходимую базу данных, например, postgres.
-   [PostgreSQL. Установка]({{< relref "2025-12-11--postgresql-install" >}})


#### <span class="section-num">2.1.3</span> Установка пакета {#установка-пакета}

-   Установите пакет `rpm`:
    ```shell
    dnf -y install $(curl -s https://api.github.com/repos/semaphoreui/semaphore/releases/latest | grep browser_download_url | cut -d '"' -f 4 | grep amd64.rpm)
    ```


### <span class="section-num">2.2</span> Docker {#docker}


#### <span class="section-num">2.2.1</span> Общая информация {#общая-информация}

-   Страница: <https://www.semaphoreui.ru/install/docker>


#### <span class="section-num">2.2.2</span> Пререквизиты {#пререквизиты}

-   Установите docker или podman:
    ```shell
    sudo dnf -y install podman podman-compose podman-tui
    ```


### <span class="section-num">2.3</span> Файл docker compose {#файл-docker-compose}

-   Сделайте файл `docker-compose.yml`:
    ```yaml
    services:
        semaphore_db:
            image: postgres
            environment:
                POSTGRES_USER: semaphore
                POSTGRES_PASSWORD: ysusfd9t1g
                POSTGRES_DB: semaphore
            volumes:
    ​            - semaphore_postgres:/var/lib/postgresql/data
            networks:
    ​            - semaphore_network
        semaphore:
            ports:
    ​            - 3000:3000
            depends_on:
    ​            - semaphore_db
            image: semaphoreui/semaphore:v2.16.18
            environment:
                SEMAPHORE_DB_DIALECT: postgres
                SEMAPHORE_DB_HOST: semaphore_db
                SEMAPHORE_DB_NAME: semaphore
                SEMAPHORE_DB_USER: semaphore
                SEMAPHORE_DB_PASS: ysusfd9t1g
                SEMAPHORE_ADMIN: admin
                SEMAPHORE_ADMIN_PASSWORD: changeme
                SEMAPHORE_ADMIN_NAME: Admin
                SEMAPHORE_ADMIN_EMAIL: admin@localhost
            volumes:
    ​            - semaphore_data:/var/lib/semaphore
    ​            - semaphore_config:/etc/semaphore
    ​            - semaphore_tmp:/tmp/semaphore
            networks:
    ​            - semaphore_network
    volumes:
        semaphore_data:
        semaphore_config:
        semaphore_tmp:
        semaphore_postgres:
    networks:
        semaphore_network: {driver: "bridge"}
    ```
-   Создайте нужные каталоги:
    ```shell
    sudo mkdir -p /var/lib/postgresql/data
    ```


### <span class="section-num">2.4</span> Запуск {#запуск}

-   Запустите:
    ```shell
    podman compose up
    ```
