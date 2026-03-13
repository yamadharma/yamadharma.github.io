---
title: "Wayland. Настройка приложений"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-14T13:59:00+03:00
lastmod: 2024-05-18T21:20:00+03:00
tags: ["wayland", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "wayland-application-setup"
---

Настройка приложений для Wayland.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Chrome {#chrome}

-   Поддержка Wayland включается флагом:
    ```shell
    --ozone-platform-hint=auto
    ```
-   Если это не срабатывает, можно указать явно:
    ```shell
    --ozone-platform=wayland
    ```
-   Если возникают проблемы с методами ввода, можно принудительно установить версию GTK:
    ```shell
    --gtk-version=4
    ```
-   Отсутствие верхних баров может быть решено путем дополнительного использования следующего флага:
    ```shell
    --enable-features=WaylandWindowDecorations
    ```
-   Для захвата экрана на Wayland:
    ```shell
    --enable-webrtc-pipewire-capturer
    ```
-   Можно установить флаги запуска в конфигурационном файле (см. [Флаги запуска Google Chrome]({{< relref "2023-02-28-google-chrome-flags" >}})):
    ```shell
    ## /etc/chrome-flags.conf
    --ozone-platform-hint=auto
    --enable-features=WaylandWindowDecorations
    --enable-webrtc-pipewire-capturer
    --gtk-version=4
    ```
