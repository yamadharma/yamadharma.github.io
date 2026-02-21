---
title: "Sway. Совместимость приложений"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-20T21:26:00+03:00
lastmod: 2024-06-23T16:29:00+03:00
tags: ["wayland", "sysadmin", "linux"]
categories: ["computer-science"]
draft: false
slug: "sway-application-compatibility"
---

Sway. Совместимость приложений.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Java {#java}


### <span class="section-num">1.1</span> Серое окно, приложения не меняют размер с помощью WM, меню сразу закрываются {#серое-окно-приложения-не-меняют-размер-с-помощью-wm-меню-сразу-закрываются}

-   В стандартных тулкитах для Java жестко зашит список оконных менеджеров.
-   Следует установить переменную окружения:
    ```shell
    export _JAVA_AWT_WM_NONREPARENTING=1
    ```


### <span class="section-num">1.2</span> Меню в приложениях плавает отдельно, им невозможно пользоваться {#меню-в-приложениях-плавает-отдельно-им-невозможно-пользоваться}

-   В выпусках Java до версии 9 GTK интерфейс ориентирован на GTK2, в последующих версиях на GTK3.
-   GTK LookAndFeel может работать с GTK версий 2, 2.2 и 3.
-   По умолчанию используется GTK3.
-   Следует явно задать более старую версию:
    ```shell
    export JAVA_TOOL_OPTIONS='-Djdk.gtk.version=2.2'
    ```
-   Например, в файле `~/.profile`:
    ```shell
    if [ "$XDG_SESSION_DESKTOP" = "sway" ] || [ "$XDG_SESSION_DESKTOP" = "i3" ]
    then
        # https://github.com/swaywm/sway/issues/595
        export _JAVA_AWT_WM_NONREPARENTING=1
        export JAVA_TOOL_OPTIONS='-Djdk.gtk.version=2.2'
    fi
    ```


## <span class="section-num">2</span> Приложения GTK+ запускаются с задержкой {#приложения-gtk-plus-запускаются-с-задержкой}

-   Приложения GTK+ ожидают запуск `xdg-desktop-portal` через D-Bus.
-   Ожидание прекращается по таймауту потому, что активированная служба D-Bus не знает, к какому `WAYLAND_DISPLAY` подключиться.
-   Это можно исправить, добавив в файл конфигурации следующее:
    ```shell
    exec systemctl --user import-environment DISPLAY WAYLAND_DISPLAY SWAYSOCK
    exec hash dbus-update-activation-environment 2>/dev/null && dbus-update-activation-environment --systemd DISPLAY WAYLAND_DISPLAY SWAYSOCK
    ```


## <span class="section-num">3</span> Qt приложения {#qt-приложения}

-   Qt по умолчанию использует бэкэнд X11 вместо собственного бэкэнда Wayland. Чтобы использовать бэкэнд Wayland, установите `QT_QPA_PLATFORM=wayland`.
-   Qt прорисовает оформление окон на стороне клиента. Чтобы отключить это, установите `QT_WAYLAND_DISABLE_WINDOWDECORATION="1"`.


## <span class="section-num">4</span> Avidemux {#avidemux}

-   При запуске Avidemux под Wayland не отображается окно просмотра.
-   Следует установить переменную окружения `QT_QPA_PLATFORM=xcb` или `WAYLAND_DISPLAY=0`:
    ```shell
    QT_QPA_PLATFORM=xcb avidemux3_qt5
    ```
-   Альтернативно можно задать опцию `--platform 'xcb'`:
    ```shell
    avidemux3_qt5 --platform 'xcb'
    ```
