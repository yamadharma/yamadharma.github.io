---
title: "Запуск приложений. Rofi"
author: ["Dmitry S. Kulyabov"]
date: 2021-11-19T20:00:00+03:00
lastmod: 2023-09-21T15:14:00+03:00
categories: ["computer-science"]
draft: false
slug: "launcher_rofi"
---

Запуск приложений. Rofi.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Используется для запуска приложений, переключения окон.
-   <https://github.com/davatorium/rofi>
-   Конфигурация по умолчанию находится в `~/.config/rofi/config`.


## <span class="section-num">2</span> Ответвления {#ответвления}


### <span class="section-num">2.1</span> С поддержкой Wayland {#с-поддержкой-wayland}

-   Оригинальный _rofi_ работает в wayland через XWayland.
-   Репозиторий: <https://github.com/lbonn/rofi>
-   Установка
    -   Gentoo
        ```shell
        emerge x11-misc/rofi-wayland
        ```

        -   Находится в репозитории [swirl](http://gpo.zugaina.org/Overlays/swirl).
        -   Добавить репозиторий:
            ```shell
            layman -a swirl
            ```
        -   Придётся удалить `x11-misc/rofi`.


## <span class="section-num">3</span> Темы {#темы}

-   Для выбора темы можно использовать команду:
    ```shell
    rofi-theme-selector
    ```
-   Для запуска программ используется несколько мод:
    -   `run`: запускать приложения из пути (`$PATH`) с возможностью запуска в терминале.
    -   `drun`: запускать приложения на основе desctop-файлов (по стандарту XDG).
    -   `window`: переключение между окнами в оконном менеджере, совместимом со спецификацией EWMH.
    -   `ssh`: подключение к удаленному хосту через `ssh`.
    -   `file-browser`: базовый файловый броузер для открытия файлов.
    -   `keys`: список внутренних привязок клавиш.
    -   `script`: использование простых скриптов.
    -   `combi`: объединяет несколько мод в одну.


## <span class="section-num">4</span> Специфика разных windowmanagers {#специфика-разных-windowmanagers}


### <span class="section-num">4.1</span> i3wm {#i3wm}

-   Использование запятых в файле настроек _i3_ может привести к проблемам. Лучше использовать файл настроек _rofi_ или замените запятые символом `#`, например, заменить строку
    ```conf-unix
    rofi -combi-modi window,drun,ssh
    ```
    на
    ```conf-unix
    rofi -combi-modi window#drun#ssh
    ```
-   Возможная конфигурация в командной строке команды `rofi`:
    ```conf-unix
    ## ~/.config/i3/config
    set $menu rofi -combi-modi window#drun -show combi -modi combi -show-icons
    ```
-   Конфигурация с помощью конфигурационного файла (поместим его в `~/.config/i3/rofi/config`).


## <span class="section-num">5</span> Плагины {#плагины}


### <span class="section-num">5.1</span> rofi-pass {#rofi-pass}

-   Плагин для работы с _pass_ (см. [Менеджер паролей pass. Интеграция с другими программами]({{< relref "2021-11-20-password-manager-pass-integration" >}})).
