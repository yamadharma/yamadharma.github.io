---
title: "Wayland. Удалённый доступ. Waypipe"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-01T19:22:00+03:00
lastmod: 2024-12-19T12:31:00+03:00
tags: ["sysadmin", "wayland"]
categories: ["computer-science"]
draft: false
slug: "wayland-remote-desktop-waypipe"
---

Wayland. Удалённый доступ. Waypipe.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://gitlab.freedesktop.org/mstoeckl/waypipe/>
-   Описание: <https://mstoeckl.com/notes/gsoc/blog.html>
-   Позволяет запускать приложения на другом хосте.
-   Waypipe обеспечивает трансляцию на другой хост через один сетевой сокет сообщений Wayland и сериализированных изменений в буферах разделяемой памяти и DMABUF.
-   В качестве транспорта может применяться SSH по аналогии со встроенным в SSH перенаправлением протокола X11 (`ssh -X`).
-   Waypipe должен быть установлен как на стороне клиента, так и на стороне сервера - один экземпляр выступает в роли сервера Wayland, а второй клиента Wayland.


## <span class="section-num">2</span> Использование {#использование}

-   Для запуска программы `weston-terminal` с другого хоста и отображения интерфейса на текущей системе достаточно выполнить команду:
    ```shell
    waypipe ssh -C user@server weston-terminal
    ```
-   Аргументы командной строки:
    -   до `ssh` применяются только к `waypipe`;
    -   после `ssh` применяются к `ssh`.
