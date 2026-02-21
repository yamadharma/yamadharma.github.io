---
title: "Wayland. Аналоги приложений"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-11T14:23:00+03:00
lastmod: 2024-11-21T15:52:00+03:00
tags: ["sysadmin", "wayland"]
categories: ["computer-science"]
draft: false
slug: "wayland-applications"
---

Аналоги приложений для Wayland.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Аналоги приложений {#аналоги-приложений}


### <span class="section-num">1.1</span> Просмотр изображений {#просмотр-изображений}

-   [Wayland. Просмотрщик изображений Swayimg]({{< relref "2024-05-01-wayland-swayimg-image-viewer" >}})
    -   Легковесный просмотрщик изображений.
    -   Управляется с клавиатуры.
    -   По умолчанию раскладка клавиатуры vi-подобная.


### <span class="section-num">1.2</span> Снимки экрана {#снимки-экрана}

-   [Sway. Скриншоты]({{< relref "2023-11-05-sway-screenshots" >}})


### <span class="section-num">1.3</span> Видеозапись экрана (скринкаст) {#видеозапись-экрана--скринкаст}

Ранее использовался [SimpleScreenRecorder](https://www.maartenbaert.be/simplescreenrecorder/).


#### <span class="section-num">1.3.1</span> Видеозапись экрана -- командная строка {#видеозапись-экрана-командная-строка}

Для записи из командной строки используем [wf-recorder](https://github.com/ammen99/wf-recorder):

```shell
emerge -v gui-apps/wf-recorder
```

Варианты использования:

-   Запись всего экрана в файл `recording.mkv` (только видео):

<!--listend-->

```shell
wf-recorder -f recording$(date +%Y-%m-%d_%H-%M-%S).mkv
```

Если файл не указывать, запись будет в текущий каталог.

-   Запись фрагмента экрана (тут имя файла задаётся по времени начала
    записи):

<!--listend-->

```shell
wf-recorder -g "$(slurp)" -f $(date +%Y-%m-%d_%H-%M-%S).mkv
```

-   Запись со звуком:

<!--listend-->

```shell
wf-recorder --audio -f $(date +%Y-%m-%d_%H-%M-%S).mkv
```

-   Запись с использование GPU (VAAPI интерфейс):

<!--listend-->

```shell
wf-recorder --audio -f $(date +%Y-%m-%d_%H-%M-%S).mkv -c h264_vaapi -d /dev/dri/renderD128
```


#### <span class="section-num">1.3.2</span> Видеозапись экрана -- графическое приложение {#видеозапись-экрана-графическое-приложение}

Для захвата десктопа в Wayland используется плагин [wlrobs](https://hg.sr.ht/~scoopta/wlrobs).


### <span class="section-num">1.4</span> Строка состояний {#строка-состояний}

-   Swaybar
    -   Sway поддерживает свою строку состояний `sway-bar`. Удобное и минималистическое приложение. Однако, удручает, что иконки в трее не активны.
-   Waybar
    -   [Wayland. Панель Waybar]({{< relref "2024-11-21-wayland-waybar" >}})


### <span class="section-num">1.5</span> Уведомления {#уведомления}

Используется [mako](https://github.com/emersion/mako).

```shell
emerge -v gui-apps/mako
```

Сконфигурировал следующим образом:

```conf-unix
# ~/.config/sway/config.d/80-mako.conf
# Light
exec_always mako --font 'Source Code Pro 10' --background-color '#fdf6e3' --text-color '#657b83' --default-timeout 5000 --width 400 --markup 1 --border-radius 5

# Dark
# exec_always mako --font 'Source Code Pro 10' --background-color '#002b36' --text-color '#839496' --default-timeout 5000 --width 400 --markup 1 --border-radius 5
```


### <span class="section-num">1.6</span> Настройка вывода {#настройка-вывода}

В XWindow используется программа `xrandr` (с её помощью можно изменять параметры вывода изображения RandR). В `sway` можно управлять с помощью `swaymsg output` или с помощью утилиты [wlr-randr](https://github.com/emersion/wlr-randr).

```shell
emerge -v gui-apps/wlr-randr
```


### <span class="section-num">1.7</span> Меню программ (launcher) {#меню-программ--launcher}

Для запуска программы используется `dmenu`. Если не нравится, можно заменить.

-   [wofi](https://hg.sr.ht/~scoopta/wofi) --- аналог `rofi` для Wayland. Попроще, конечно.

<!--listend-->

```shell
emerge -v gui-apps/wofi
```

В отличии от `dmenu` запоминает последние выбранные команды.

Общая конфигурация:

```conf-unix
# ~/.config/sway/config.d/80-launcher.conf

# dmenu

set $menu dmenu_path | dmenu | xargs swaymsg exec --

# wofi
# --show <mode>
# <mode>:
# - `run` - searches $PATH for executables and allows them to be run by selecting them.
# - `drun` - searches $XDG_DATA_HOME/applications and $XDG_DATA_DIRS/applications for desktop files and allows them to be run by selecting them.
# - `dmenu` - reads from stdin and displays options which when selected will be output to stdout.

# set $menu dmenu_path | wofi -c ~/.config/sway/other/wofi/config -s ~/.config/sway/other/wofi/style.css --show dmenu | xargs swaymsg exec --

# rofi

# set $menu rofi -combi-modi window#drun -show combi -modi combi -show-icons
# set $menu rofi -m $(swaymsg -t get_outputs | jq 'map(select(.active) | .focused) | index(true)') -show combi -modi combi -combi-modi window#drun -show-icons -run-command 'swaymsg exec -- {cmd}'

# gmenu

# set $menu gtkmenu --width 500 --height 260 -no-generic
# set $menu nwggrid

# bemenu

# set $menu j4-dmenu-desktop --dmenu="bemenu-run.sh -l 30" --term="alacritty" --no-generic

# Start your launcher

bindsym $mod+d exec $menu
```


### <span class="section-num">1.8</span> Буфер обмена {#буфер-обмена}

Предлагается использовать [wl-clipboard](https://github.com/bugaevc/wl-clipboard).

```shell
emerge -v gui-apps/wl-clipboard
```

Пакет содержит две утилиты: `wl-copy` и `wl-paste`.

Пример использования:

```shell
# copy a simple text message
$ wl-copy Hello world!

# copy the list of files in Downloads
$ ls ~/Downloads | wl-copy

# copy an image file
$ wl-copy < ~/Pictures/photo.png

# paste to a file
$ wl-paste > clipboard.txt

# grep each pasted word in file source.c
$ for word in $(wl-paste); do grep $word source.c; done

# copy the previous command
$ wl-copy "!!"

# replace the current selection with the list of types it's offered in
$ wl-paste --list-types | wl-copy
```


### <span class="section-num">1.9</span> Блокировка экрана {#блокировка-экрана}


#### <span class="section-num">1.9.1</span> swaylock {#swaylock}

<!--list-separator-->

1.  Общая информация

    -   Официальное приложение для блокировки экрана для _Sway_ --- _swaylock_.
    -   Репозиторий: <https://github.com/swaywm/swaylock>
    -   Установка:
        -   Gentoo:
            ```shell
            emerge gui-apps/swaylock
            ```
    -   В информационной панеле _waybar_ есть опция для отключения блокировки при простое (например, для демонстрации слайдов).

<!--list-separator-->

2.  Блокировка при простое

    -   Заблокировать экран после 300 секунд бездействия.
    -   Затем выключить дисплей ещё через 300 секунд.
    -   Включить экран при возобновлении работы.
    -   Также заблокировать экран перед тем, как компьютер перейдет в спящий режим.
    -   Конфигурационный файл:
        ```conf-unix
        ### ~/.config/sway/config.d/80-lock.conf

        ### Idle lock
        ## - Lock your screen after 300 seconds of inactivity
        ## - Then turn off your displays after another 300 seconds
        ## - Turn your screens back on when resumed
        ## - Also lock your screen before your computer goes to sleep

        exec swayidle -w \
                 timeout 300 'swaylock -f -c 000000 -k' \
                 timeout 600 'swaymsg "output * dpms off"' \
                 resume 'swaymsg "output * dpms on"' \
                 before-sleep 'swaylock -f -c 000000 -k'
        ```

<!--list-separator-->

3.  Ручная блокировка

    -   `Mod` + `Ctrl` + `l` для немедленной блокировки экрана.
    -   Через 10 секунд выключить экран.
    -   Конфигурационный файл:
        ```conf-unix
        ### ~/.config/sway/config.d/80-lock.conf

        ### Manual lock
        ## - Mod + Ctrl + l to lock the screen immediately
        ## - In 10 sec also switch the screen off

        set $lockman exec bash ~/.config/sway/scripts/lockman.sh
        bindsym $mod+Ctrl+l exec $lockman
        ```
    -   Скрипт блокировки:
        ```shell
        #!/bin/bash
        # ~/.config/sway/scripts/lockman.sh

        # Times the screen off and puts it to background
        swayidle \
            timeout 10 'swaymsg "output * dpms off"' \
            resume 'swaymsg "output * dpms on"' &
        # Locks the screen immediately
        swaylock -c 550000 -k
        # Kills last background task so idle timer doesn't keep running
        kill %%
        ```


#### <span class="section-num">1.9.2</span> swaylock-effects {#swaylock-effects}

-   _swaylock-effects_ является форком _swaylock_:
    -   Репозиторий: <https://github.com/mortie/swaylock-effects>
    -   Добавляет встроенные скриншоты и эффекты манипулирования изображениями, такие как размытие.


### <span class="section-num">1.10</span> Демонстрация нажатия клавиш {#демонстрация-нажатия-клавиш}


#### <span class="section-num">1.10.1</span> Show Me The Key {#show-me-the-key}

-   Страница: <https://showmethekey.alynx.one/>
-   Репозиторий: <https://github.com/AlynxZhou/showmethekey>

<!--list-separator-->

1.  Установка

    -   Gentoo, оверлей `guru` (см. [Gentoo. Дополнительные репозитории]({{< relref "2023-10-01-gentoo-additional-repositories" >}})):
        ```shell
        emerge gui-apps/showmethekey
        ```

<!--list-separator-->

2.  Особенности

    -   Нужно включить переключатель в панели настроек, чтобы запустить отображение нажатия клавиш.
    -   Нужно разрешение суперпользователя для чтения событий клавиатуры.
        -   Пользователи в группе `wheel` могут пропустить аутентификацию по паролю.
    -   Wayland не позволяет клиенту устанавливать своё положение, поэтому область отображения нажатия клавиш следует перетащить в нужное место.


## <span class="section-num">2</span> Ресурсы по миграции с X Window {#ресурсы-по-миграции-с-x-window}

-   <https://github.com/swaywm/sway/wiki/i3-Migration-Guide>
-   <https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway>
-   <https://wiki.gentoo.org/wiki/List_of_software_for_Wayland>
-   <https://github.com/natpen/awesome-wayland>
-   <https://arewewaylandyet.com/>
