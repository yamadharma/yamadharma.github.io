---
title: "Wayland. Удалённый доступ. VNC"
author: ["Dmitry S. Kulyabov"]
date: 2025-02-21T20:45:00+03:00
lastmod: 2025-02-21T21:19:00+03:00
tags: ["wayland", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "wayland-remote-desktop-vnc"
---

Wayland. Удалённый доступ. VNC.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> wayvnc {#wayvnc}

-   Сервер VNC для композиторов на основе wlroots.
-   Репозиторий: <https://github.com/any1/wayvnc>


### <span class="section-num">1.1</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge gui-apps/wayvnc
    ```


### <span class="section-num">1.2</span> Запуск {#запуск}

-   Сервер принимает по умолчанию подключения только от localhost.
-   Чтобы принимать подключения через любой интерфейс, установите в командной строке адрес на `0.0.0.0`:
    ```shell
    wayvnc 0.0.0.0
    ```
-   Чтобы подключиться к существующей сессии не из-под ней (например, из-под ssh), необходимо экспортировать переменную `WAYLAND_DISPLAY`:
    ```shell
    export WAYLAND_DISPLAY=wayland-1; wayvnc 0.0.0.0
    ```


### <span class="section-num">1.3</span> Управление сокетом {#управление-сокетом}

-   Для управления во время выполнения, Wayvnc открывает unix-сокет `$XDG_RUNTIME_DIR/wayvncctl` (или `/tmp/wayvncctl-$UID`).
-   Можно подключаться и обмениваться сообщениеми в формате JSON.
-   Используется утилита `wayvncctl`.


## <span class="section-num">2</span> Подключение {#подключение}

-   Для подключения можно использовать любой клиент.
-   Я использую Remmina.
