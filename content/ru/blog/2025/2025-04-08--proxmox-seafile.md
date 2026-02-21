---
title: "Proxmox. Сервер Seafile"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-08T13:15:00+03:00
lastmod: 2025-04-12T17:22:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "proxmox-seafile"
---

Proxmox. Сервер Seafile.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   [Файловое хранилище Seafile]({{< relref "2025-04-08--seafile-file-server" >}})


## <span class="section-num">2</span> Установка {#установка}

-   Будем устанавливать в контейнер LXC с помощью скрипта (см. [Proxmox. Вспомогательные скрипты]({{< relref "2024-06-04-proxmox-helper-scripts" >}})):
    ```shell
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/seafile.sh)"
    ```
-   Можно оставить конфигурацию по умолчанию или задать свою.


## <span class="section-num">3</span> После установки {#после-установки}


### <span class="section-num">3.1</span> Параметры доступа {#параметры-доступа}

-   Зайдите в консоль виртуальной машины.
-   Посмотрите настройки сервера:
    ```shell
    cat ~/seafile.creds
    ```


### <span class="section-num">3.2</span> Домен {#домен}

-   Зайдите в консоль виртуальной машины.
-   По умолчанию сервер привязывается к ip-адресу.
-   Можно сменить адрес доступа к серверу:
    ```shell
    ~/domain.sh <FULL_DOMAIN_URL_WITH_HTTPS_OR_HTTP>
    ```
-   Например:
    ```shell
    ~/domain.sh https://seafile.example.com
    ```
-   Изменения вносятся в файл `/opt/seafile/conf/seahub_settings.py`.


### <span class="section-num">3.3</span> Хранилище {#хранилище}

-   Подключите внешнее хранилище.
-   Подключитесь к консоли proxmox.
-   Создадим точку монтирования и образ на файловой системе:
    ```shell
    pct set 100 -mp0 local-lvm:1000,mp=/n/data
    ```

    -   Номер виртуальной машины: 100.
    -   Выделенный объём диска: 1000G.
-   Подключитесь к консоли контейнера.
-   Задайте в файле `~/external-storage.sh` переменную `STORAGE_DIR`:
    ```shell
    STORAGE_DIR=/n/data
    ```
-   Перенесите файлы в новое хранилище:
    ```shell
    bash ~/external-storage.sh
    ```
-   Поправьте права доступа:
    ```shell
    chown -R seafile:seafile /n/data
    chown -R seafile:seafile /opt/seafile/seafile-dataseafile-data
    ```


## <span class="section-num">4</span> Подключение через обратный прокси {#подключение-через-обратный-прокси}

-   Будем использовать Nginx Proxy Manager.
-   [Обратный прокси-сервер Nginx Proxy Manager]({{< relref "2025-04-12--nginx-proxy-manager" >}})
-   Будем использовать настройки из шаблона <https://github.com/draga79/seafile-docker>.
-   После установки настроим proxy:
    -   <https://seafile.example.com/> -&gt; ip-address:8000
    -   <https://seafile.example.com/seafhttp> -&gt; ip-address:8082
    -   <https://seafile.example.com/webdav> -&gt; ip-address:8080


## <span class="section-num">5</span> Ошибки {#ошибки}


### <span class="section-num">5.1</span> sasl2 {#sasl2}

-   Seafile искал каталог `/usr/lib64/sasl2`, который отсутствовал.
-   Сделал симлинк:
    ```shell
    ln -sfn /usr/lib/x86_64-linux-gnu/sasl2/ /usr/lib64/sasl2
    ```
