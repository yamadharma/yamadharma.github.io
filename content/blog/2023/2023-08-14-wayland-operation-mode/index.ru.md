---
title: "Wayland. Режим работы"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-14T11:27:00+03:00
lastmod: 2023-09-16T17:43:00+03:00
tags: ["wayland", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "wayland-operation-mode"
---

Узнать режим работы приложений: Wayland или Xorg.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Тип сессии {#тип-сессии}

-   Можно вывести содержимое переменной окружения `XDG_SESSION_TYPE`:
    ```shell
    echo $XDG_SESSION_TYPE
    ```

    -   Результат:
        -   если используется Wayland, то будет выведено `wayland`;
        -   если используется Xorg, то будет выведено `X11`.
-   Можно узнать тип текущей сессии с помощью `loginctl`, получив идентификатор сессии из переменной окружения `XDG_SESSION_ID`:
    ```shell
    loginctl show-session "$XDG_SESSION_ID" -p Type
    ```


## <span class="section-num">2</span> Какие приложения используют XWayland {#какие-приложения-используют-xwayland}

-   Для того чтобы старые приложения X11 могли работать в Wayland, существует прослойка совместимости XWayland.
-   Команда `xlsclients` отображает все программы, которые используют Xwayland в данный момент:
    ```shell
    xlsclients
    ```
