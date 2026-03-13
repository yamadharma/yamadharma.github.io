---
title: "Контейнеры. podman"
author: ["Dmitry S. Kulyabov"]
date: 2024-12-04T20:13:00+03:00
lastmod: 2024-12-10T08:44:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "containers-podman"
---

Контейнеры. podman.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Совместимая с Docker среда выполнения контейнеров.


## <span class="section-num">2</span> Установка {#установка}

-   Rocky:
    ```shell
    dnf -y install podman
    ```
-   Установим podman-compose:
    ```shell
    dnf -y install podman-compose
    ```
-   Дополнительно можно установить текстовый интерфейс:
    ```shell
    dnf -y install podman-tui
    ```
-   Плагин для Cockpit:
    ```shell
    dnf -y install cockpit-podman
    ```


## <span class="section-num">3</span> Запуск {#запуск}

-   Запустите сервис:
    ```shell
    systemctl enable --now podman.service
    ```
-   Запустите сервис автообновления:
    ```shell
    systemctl enable --now podman-auto-update.timer
    ```


## <span class="section-num">4</span> Добавление контейнера {#добавление-контейнера}

-   В качестве примера установим [Nextcloud](https://nextcloud.com/):
    ```shell
    podman run -d -p 8080:80 nextcloud
    ```
-   Вы получите приглашение выбрать реестр контейнеров для загрузки.
-   Можно выбрать `docker.io/library/nextcloud:latest`.
-   После загрузки контейнера Nextcloud он запустится.
-   Введите `ip_address:8080` в веб-браузере и настройте Nextcloud.


## <span class="section-num">5</span> Запуск контейнеров как сервисов `systemd` {#запуск-контейнеров-как-сервисов-systemd}

-   Информация: <https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html>
-   [Quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html): генератор systemd, который может создавать юнит-файлы для служб systemd без root и с root-доступом.
-   Файлы для сервисов с root-доступом можно поместить в каталоги:
    -   `/etc/containers/systemd/`.
    -   `/usr/share/containers/systemd/`
-   Файлы для сервисов без root-доступа могут быть помещены в каталоги:
    -   `$XDG_CONFIG_HOME/containers/systemd/` (`~/.config/containers/systemd/`);
    -   `/etc/containers/systemd/users/$(UID)`;
    -   `/etc/containers/systemd/users/`.
-   Например, для Nextcloud создадим файл `~/.config/containers/systemd/nextcloud.container`:
    ```conf-unix
    [Container]
    Image=nextcloud
    PublishPort=8080:80
    ```
-   По умолчанию контейнер podman имеет то же имя, что и модуль, но с префиксом `systemd-`.
-   Опция `ContainerName`  позволяет переопределить это имя по умолчанию на имя, предоставленное пользователем.
-   Запустим генератор и сообщим systemd о запуске новой службы:
    ```shell
    systemctl --user daemon-reload
    ```
-   Запустим службу:
    ```shell
    systemctl --user start nextcloud.service
    ```
-   Для системных сервисов опустите флаг `--user`.
-   Чтобы автоматически запускать контейнер при запуске системы или входе пользователя в систему, можно добавить раздел в файл `nextcloud.container`:
    ```conf-unix
    [Install]
    WantedBy=default.target
    ```
-   Поскольку сгенерированные служебные файлы считаются временными, их нельзя включить с помощью systemd.
-   Чтобы избежать этого, генератор вручную применяет установки во время генерации.
