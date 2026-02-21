---
title: "Window manager i3"
author: ["Dmitry S. Kulyabov"]
date: 2021-05-14T11:32:00+03:00
lastmod: 2023-12-30T20:11:00+03:00
tags: ["gentoo", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "window-manager-i3"
---

Менеджер окон _i3_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Тайловый менеджер окон.
-   <https://i3wm.org/>


## <span class="section-num">2</span> Репозиторий конфигурации {#репозиторий-конфигурации}

-   Я сделал репозиторий со своей конфигурацией: <https://github.com/yamadharma/config-i3>


## <span class="section-num">3</span> Файл конфигурации {#файл-конфигурации}

-   Файлы конфигурации просматриваются в следующем порядке:
    -   `$XDG_CONFIG_HOME/i3/config` (`~/.config/i3/config`);
    -   `~/.i3/config`;
    -   `$XDG_CONFIG_DIRS/i3/config` (`/etc/xdg/i3/config`);
    -   `/etc/i3/config`.
-   Начиная с версии 4.20, можно подключать другие файлы конфигурации из основного файла конфигурации _i3_.
    -   Примеры использования директивы `include`:
        ```cfg
        # Тильда преобразуется в домашний каталог пользователя
        include ~/.config/i3/assignments.conf

        # Переменные среды разыменовываются
        include $HOME/.config/i3/assignments.conf

        # Символы подстановки раскрываются
        include ~/.config/i3/config.d/*.conf

        # Можно выполнять команду
        include ~/.config/i3/`hostname`.conf

        # Каждый путь загружается только один раз
        include ~/.config/i3/config

        # Относительные пути интерпретируются относительно каталога конфигурационного файла
        include assignments.conf
        ```


## <span class="section-num">4</span> Навигация {#навигация}


### <span class="section-num">4.1</span> Клавиша-модификатор {#клавиша-модификатор}

-   В качестве модификатора обычно используется:
    -   `Alt`:
        ```conf-unix
        set $mod Mod1
        ```
    -   `Super` (Клавиша со значком _Windows_):
        ```conf-unix
        set $mod Mod4
        ```
    -   Предпочитаю `Super`, чтобы не конфликтовать с Emacs.


### <span class="section-num">4.2</span> Основные комбинации клавиш {#основные-комбинации-клавиш}

-   `Mod` + `Enter`: открыть терминал.


### <span class="section-num">4.3</span> Перемещение фокуса {#перемещение-фокуса}

-   Фокус можно перемещать как с помощью стрелок, так и с помощью буквенных клавиш, как в редакторе _vi_.
    -   `Mod` + `h` или `Mod` + `Left`: сдвиг фокуса влево.
    -   `Mod` + `j` или `Mod` + `Down`: сдвиг фокуса вниз.
    -   `Mod` + `k` или `Mod` + `Up`: сдвиг фокуса вверх.
    -   `Mod` + `l` или `Mod` + `Right`: сдвиг фокуса вправо.
-   Конфигурация выглядит следующим образом:
    ```conf-unix
    ## Home row direction keys, like vim
    set $left h
    set $down j
    set $up k
    set $right l
    ## Move your focus around
    bindsym $mod+$left focus left
    bindsym $mod+$down focus down
    bindsym $mod+$up focus up
    bindsym $mod+$right focus right
    ## Or use $mod+[up|down|left|right]
    bindsym $mod+Left focus left
    bindsym $mod+Down focus down
    bindsym $mod+Up focus up
    bindsym $mod+Right focus right
    ```
-   Впрочем, следует заметить, что также могут использоваться и другие соглашения:
    -   `j`: влево;
    -   `k`: вниз;
    -   `l`: вверх;
    -   `;`: вправо.
-   Поскольку в данном менеджере окон поддерживаются контейнеры, то можно переключить фокус на родительский контейнер:
    -   `Mod` + `a`: переключить фокус на родительский контейнер.
    -   Конфигурация:
        ```conf-unix
        ## Move focus to the parent container
        bindsym $mod+a focus parent
        ```
-   `Mod` + `Space`: переключить режим фокуса.


### <span class="section-num">4.4</span> Перемещение окон {#перемещение-окон}

-   Делается аналогично перемещению фокуса, но с добавлением модификатора `Shift`:
    -   `Mod` + `Shift` + `h` или `Mod` + `Shift` + `Left`: перемещение влево;
    -   `Mod` + `Shift` + `j` или `Mod` + `Shift` + `Down`: перемещение вниз;
    -   `Mod` + `Shift` + `k` или `Mod` + `Shift` + `Up`: перемещение вверх;
    -   `Mod` + `Shift` + `l` или `Mod` + `Shift` + `Right`: перемещение вправо.
-   Конфигурация выглядит следующим образом:
    ```conf-unix
    ## Move the focused window with the same, but add Shift
    bindsym $mod+Shift+$left move left
    bindsym $mod+Shift+$down move down
    bindsym $mod+Shift+$up move up
    bindsym $mod+Shift+$right move right
    ## Ditto, with arrow keys
    bindsym $mod+Shift+Left move left
    bindsym $mod+Shift+Down move down
    bindsym $mod+Shift+Up move up
    bindsym $mod+Shift+Right move right
    ```


### <span class="section-num">4.5</span> Modifying windows {#modifying-windows}

-   `Mod` + f	toggle fullscreen
-   `Mod` + v	split a window vertically
-   `Mod` + h	split a window horizontally
-   `Mod` + r	resize mode


### <span class="section-num">4.6</span> Структура расположения контейнеров {#структура-расположения-контейнеров}

-   Поддерживаются следующие расположения контейнеров:
    -   `Mod` + `e`: переключение разделённого расположения (split layout);
    -   `Mod` + `s`: стековое размещение (stacking layout);
    -   `Mod` + `w`: размещение с табами (tabbed layout).
-   Конфигурация:
    ```conf-unix
    ## Switch the current container between different layout styles
    bindsym $mod+s layout stacking
    bindsym $mod+w layout tabbed
    bindsym $mod+e layout toggle split
    ```
-   Для раскладки по умолчанию я использую табы:
    ```conf-unix
    ### Layout mode for new containers
    ## default|stacking|tabbed
    workspace_layout tabbed
    ```


### <span class="section-num">4.7</span> Floating {#floating}

-   `Mod` + Shift + Space	toggle floating
-   `Mod` + Left click	drag floating


### <span class="section-num">4.8</span> Рабочие области (workspaces) {#рабочие-области--workspaces}

-   Сконфигурим рабочие области:
    ```conf-unix
    ## Define names for workspaces
    set $ws1    1
    set $ws2    2
    set $ws3    3
    set $ws4    4
    set $ws5    5
    set $ws6    6
    set $ws7    7
    set $ws8    8
    set $ws9    9
    set $ws10   10
    ```
-   `Mod` + `0` -- `9`: переключиться на соответствующую рабочую область:
    ```conf-unix
    ## Switch to workspace
    bindsym $mod+1 workspace $ws1
    bindsym $mod+2 workspace $ws2
    bindsym $mod+3 workspace $ws3
    bindsym $mod+4 workspace $ws4
    bindsym $mod+5 workspace $ws5
    bindsym $mod+6 workspace $ws6
    bindsym $mod+7 workspace $ws7
    bindsym $mod+8 workspace $ws8
    bindsym $mod+9 workspace $ws9
    bindsym $mod+0 workspace $ws10
    ```
-   `Mod` + `Shift` + `0` -- `9`: перенести окно на соответствующую рабочую область:
    ```conf-unix
    ## Move focused container to workspace
    bindsym $mod+Shift+1 move container to workspace $ws1
    bindsym $mod+Shift+2 move container to workspace $ws2
    bindsym $mod+Shift+3 move container to workspace $ws3
    bindsym $mod+Shift+4 move container to workspace $ws4
    bindsym $mod+Shift+5 move container to workspace $ws5
    bindsym $mod+Shift+6 move container to workspace $ws6
    bindsym $mod+Shift+7 move container to workspace $ws7
    bindsym $mod+Shift+8 move container to workspace $ws8
    bindsym $mod+Shift+9 move container to workspace $ws9
    bindsym $mod+Shift+0 move container to workspace $ws10
    ```


### <span class="section-num">4.9</span> Opening applications / Closing windows {#opening-applications-closing-windows}

-   `Mod` + d	open application launcher (dmenu)
-   `Mod` + Shift + q	kill a window


### <span class="section-num">4.10</span> Выход/Перезапуск {#выход-перезапуск}

-   `Mod` + `Shift` + `c`: перечитать конфигурационный файл.
    ```conf-unix
    ## ~/.config/i3/config

    ## reload the configuration file
    bindsym $mod+Shift+c reload
    ```
-   `Mod` + `Shift` + `r`: перестартовать _i3_, сохранив сессию.
    ```conf-unix
    ## ~/.config/i3/config

    ## restart i3 inplace (preserves your layout/session, can be used to upgrade i3)
    bindsym $mod+Shift+r restart
    ```
-   `Mod` + `Shift` + `e`: выход из _i3_.
    ```conf-unix
    ## ~/.config/i3/config

    ## exit i3 (logs you out of your X session)
    bindsym $mod+Shift+e exec "i3-nagbar -t warning -m 'You pressed the exit shortcut. Do you really want to exit i3? This will end your X session.' -B 'Yes, exit i3' 'i3-msg exit'"
    ```


## <span class="section-num">5</span> Настройка {#настройка}


### <span class="section-num">5.1</span> Терминал {#терминал}

-   В качестве терминала я использую kitty.
-   Конфигурация запуска терминала:
    ```conf-unix
    set $term kitty
    bindsym $mod+Return exec $term
    ```

    -   В этом случае запускается одно окно терминала.
-   Для работы я использую специальную настройку сессии терминала. Я её запускаю при входе в сессию. Для этого я приспособил комбинацию `Mod` + `Shift` + `Enter`:
    ```conf-unix
    bindsym $mod+Shift+Return exec kitty --session ~/.config/kitty/startup
    ```


### <span class="section-num">5.2</span> Управление окном с помощью мышки {#управление-окном-с-помощью-мышки}

-   Можно управлять окнами с помощью мышки.
-   Привязка осуществляется следующей командой:
    ```conf-unix
    bindsym [--release] [--border] [--whole-window] [--exclude-titlebar] [<Modifiers>+]button<n> command
    ```

    -   По умолчанию привязка запускается только при нажатии на строку заголовка окна.
    -   Если указан флаг `--release`, он запустится, когда кнопка мыши будет отпущена.
    -   Если указан флаг `--whole-window`, то привязка также будет выполняться при щелчке по любой части окна, за исключением границы.
    -   Чтобы привязка выполнялась при щелчке границы, нужно указать флаг `--border`.
    -   Если задан флаг `--exclude-titlebar`, заголовок не будет учитываться для привязки клавиш.
-   Примеры.
    -   Средняя кнопка на заголовке закрывает окно:
        ```conf-unix
        bindsym --release button2 kill
        ```
    -   Средняя кнопка и модификатор над любой частью окна закрывает окно:
        ```conf-unix
        bindsym --whole-window $mod+button2 kill
        ```
    -   Правая кнопка мыши переключает плавающий режим:
        ```conf-unix
        bindsym button3 floating toggle
        bindsym $mod+button3 floating toggle
        ```
    -   Боковые кнопки мыши перемещают окно:
        ```conf-unix
        bindsym button9 move left
        bindsym button8 move right
        ```


### <span class="section-num">5.3</span> Строка статуса {#строка-статуса}


#### <span class="section-num">5.3.1</span> i3bar {#i3bar}

-   Отрисовку панели осуществляет утилита `i3bar`.
-   Отображается вверху или внизу экрана.
-   Содержит:
    -   область с кнопками переключения рабочих областей _i3_;
    -   системную строку, генерируемую при помощи `i3status` или аналогов;
    -   системный трей с иконками программ.
-   В конфигурационном файле задаётся следующим образом (<https://i3wm.org/docs/userguide.html#_configuring_i3bar>):
    ```conf-unix
    # ~/.config/i3/config -*- mode: conf-unix; -*-
    ## Start i3bar to display a workspace bar
    bar {
        status_command i3status
        position top
    }
    ```

<!--list-separator-->

1.  Поддержка иконок в i3bar

    -   В `i3bar` можно использовать шрифты иконок (см. [Моноширинные шрифты]({{< relref "2021-05-21-monospace-fonts" >}})).
    -   Наиболее распространённым является шрифт [Font Awesome](https://fontawesome.com/).
    -   Установка:
        -   Gentoo
            ```shell
            emerge media-fonts/fontawesome
            ```
    -   Для вставки шрифта в файл можно использовать список кодов для иконок <https://fontawesome.com/cheatsheet>.
    -   Шрифт лучше явно обозначить в конфигурации:
        ```conf-unix
        ## ~/.config/i3/config
        bar {
            …
            font pango:Source Sans Pro, FontAwesome 5 Free 10
            …
        }
        ```
    -   Для набора символа по его коду следует использовать конфигурации клавиш. Например, для набора символа с кодом `0xf004`, требуется набрать:
        -   приложения на основе GTK: `Ctrl` + `Shift` + `u`, `f004`, `Enter`;
        -   emacs: `Ctrl` + `x`, `8`, `Enter`, `f004`, `Enter`;
        -   vim: `Ctrl` + `v`, `uf004`;
        -   urxvt: удерживая `Ctrl` + `Shift`, наберите `f004`.

<!--list-separator-->

2.  i3status

    -   Использовано <https://igancev.ru/2020-05-11-configuring-i3status-in-i3wm>.
    -   `i3status` генерирует строку состояния для `i3bar`.
    -   Содержит встроенные модули:
        -   IPv6 --- получает и выводит IPv6 адрес.
        -   Disk --- отображает информацию о занятом и свободном месте в файловой системе.
        -   Run-watch --- мониторинг определённого процесса в системе.
        -   Path-exists --- проверяет на существование путь в файловой системе.
        -   Wireless --- позволяет выводить подключения к WIFI сети, уровень сигнала, имя точки доступа.
        -   Ethernet --- предоставляет IP адрес и скорость соединения сетевого интерфейса.
        -   Battery --- показ уровня заряда батареи.
        -   CPU-Temperature --- показ температуры процессора.
        -   CPU Usage --- использование процессора в процентах.
        -   Memory --- использование оперативной памяти.
        -   Load --- среднее значение загрузки системы за 1, 5 и 15 минут (Load Overage).
        -   Time --- время в текущей временной зоне.
        -   TzTime --- время в заданной временной зоне.
        -   DDate --- дата.
        -   Volume --- управление громкостью звука.
        -   File Contents --- вывод содержимого указанного файла.
    -   Модули в строке можно переиспользовать по нескольку раз, управляя порядком вывода.
    -   Конфигурацию условно можно разделить на 3 части:
        -   блок `general` --- содержит общие параметры;
        -   переменная `order` --- в неё записывается порядок вывода интересующих модулей;
        -   блоки конфигурации модулей --- непосредственно настройки самих блоков с метриками.
    -   В конфигурации i3bar задаётся конфигурационный файл для i3status:
        ```conf-unix
        # ~/.config/i3/config -*- mode: conf-unix; -*-
        ## Start i3bar to display a workspace bar
        bar {
            font pango:Source Sans Pro, FontAwesome 5 Free 10
            status_command	i3status --config ~/.config/i3/i3status/config
            position		top
        }
        ```
    -   Структура информационной панели задаётся в конфигурационном файле:
        ```conf-unix
        ### -*- mode: conf-unix; -*-
        ## ~/.config/i3/i3status/config

        general {
            colors = true # включение/выключение поддержки цветов true/false
            interval = 1 # интервал обновления строки статуса, в секундах
            output_format = "i3bar" # формат вывода, устанавливаем i3bar (JSON)
        }

        # порядок вывода модулей
        order += "run_watch openvpn"
        order += "run_watch openconnect"
        order += "volume master"
        order += "wireless _first_"
        order += "battery all"
        order += "disk /"
        order += "memory"
        order += "cpu_usage"
        order += "cpu_temperature 0"
        order += "tztime local"

        # отслеживание процесса openvpn
        # служит как индикатор работы openvpn клиента
        # при запуске openvpn необходимо
        # указывать параметр --writepid /var/run/openvpn.pid
        run_watch openvpn {
            pidfile = "/var/run/openvpn.pid"
            format = " openvpn"
            # если пареметр format_down оставить пустым,
            # то при неактивном процессе блок будет отсутствовать
            format_down=""
        }

        # аналогичный блок индикатор openconnect vpn клиента
        # требуется запуск клиента с параметром --pid-file=/var/run/openconnect.pid
        run_watch openconnect {
            pidfile = "/var/run/openconnect.pid"
            format = " openconnect vpn"
            format_down=""
        }

        # управление громкостью звука
        volume master {
            format = " %volume" # шаблон громкости в активном состоянии
            format_muted = " %volume" # шаблон громкости в состоянии muted (без звука)
            device = "default"
            mixer = "Master"
            mixer_idx = 0
        }

        # индикатор WIFI
        wireless _first_ {
            # шаблон вывода, можно дополнить
            # наименованием подключения %essid
            # и ip адресом %ip
            format_up = "%quality %frequency"
            format_down = ""
        }

        # состояние заряда батареи
        battery all {
            # шаблон вывода, можно дополнить
            # оставшимся временем работы %emptytime
            # энергопотреблением %consumption в ваттах
            format = "%status %percentage"

            # true - показ процента заряда от 0 до 100
            # false - показ процента заряда от 0 до n, с учетом
            # изношенности аккумулятора
            last_full_capacity = true
            format_down = ""
            status_chr = "" # статус подзарядки
            status_bat = "" # статус в режиме работы от батареи
            status_unk = "? UNK" # неизвестный статус
            status_full = "" # статус полного заряда
            path = "/sys/class/power_supply/BAT%d/uevent"

            # нижний порог заряда, после которого блок
            # будет окрашен в "color_bad" (по умолчанию красный)
            # подробнее в man i3status
            low_threshold = 10
        }

        # отслеживаемый накопитель
        disk "/" {
            # доступные переменные:
            # %used, %percentage_used - занятое пространство
            # %free, %percentage_free - свободное пространство
            # %avail, %percentage_avail - доступное пространство
            # %total - всего
            format = " %avail"

            # будет окрашен в "color_bad" (по умолчанию красный)
            # при достижении нижнего порога менее 10GB доступного пространства
            low_threshold = "10"
            threshold_type = "gbytes_avail"
            format_below_threshold = " Warning: %avail"
        }

        # миниторинг оперативной памяти
        memory {
            # доступные переменные:
            # %total, percentage_total
            # %used, percentage_used
            # %free, percentage_free
            # %available, percentage_available
            # %shared, percentage_shared
            format = " %used"

            # порог, при котором вывод окрасится в
            # желтый (degraded) или красный (critical)
            # а формат вывода изменится на format_degraded
            threshold_degraded = "1G"
            threshold_critical = "200M"
            format_degraded = "MEMORY < %available"
        }

        # температура процессора
        cpu_temperature 0 {
            format = " %degrees"

            # верхний порог температуры, при достижении которого
            # вывод окрасится красным,
            # и формат изменится на format_above_threshold
            max_threshold = "80"
            format_above_threshold = " %degrees"
            path = "/sys/class/thermal/thermal_zone0/temp"
        }

        # использование центрального процессора
        cpu_usage {
            # %usage - процентное использование ЦП
            # %cpu<N> - начиная с %cpu0 и далее показывает использование ядер
            format = " %usage"

            # доступны параметры:
            # degraded_threshold, окрас в желтый, по умолчанию 90
            # max_threshold, окрас в красный, по умолчанию 95
            # и кастомные форматы для них
            # format_above_degraded_threshold и format_above_threshold
        }

        # вывод даты и времени по заданному формату
        tztime local {
            format = " %d %b %Y  %H:%M:%S"
        }
        ```


#### <span class="section-num">5.3.2</span> py3status {#py3status}

-   `py3status` --- это расширяемая оболочка для `i3status`, написанная на python.
-   Сайт: <https://py3status.readthedocs.io/>.
-   Репозиторий: <https://github.com/ultrabug/py3status>.
-   Можно управлять `i3bar`:
    -   используя один из доступных модулей, поставляемых с `py3status`;
    -   группировать несколько модулей и автоматически или вручную циклически отображать их отображение;
    -   писать свои собственные модули и отображать их вывод на панели;
    -   обрабатывать события кликов на `i3bar`.
-   Отображается вверху или внизу экрана.
-   Содержит:
    -   область с кнопками переключения рабочих областей _i3_;
    -   системную строку;
    -   системный трей с иконками программ.

<!--list-separator-->

1.  Запуск py3status

    -   Запускается вместо `i3bar`:
        ```conf-unix
        # ~/.config/i3/config -*- mode: conf-unix; -*-
        ## Start py3status to display a workspace bar
        bar {
            font pango:Iosevka Nerd Font 12
            status_command py3status
            position top
        }
        ```
    -   Использует конфигурационный файл от `i3status` или собственную конфигурацию.
    -   Порядок поиска конфигурационного файла:
        -   `$XDG_CONFIG_HOME/py3status/config`;
        -   `$XDG_CONFIG_HOME/i3status/config`;
        -   `$XDG_CONFIG_HOME/i3/i3status.conf`;
        -   `~/.i3status.conf`;
        -   `~/.i3/i3status.conf`;
        -   `$XDG_CONFIG_DIRS/i3status/config`;
        -   `/etc/i3status.conf`.


#### <span class="section-num">5.3.3</span> polybar {#polybar}

-   Отдельное приложение для строки статуса.
-   Применяется для замены _i3bar_.
-   <https://polybar.github.io/>
-   <https://github.com/polybar/polybar>
-   Темы для _polybar_: <https://github.com/adi1090x/polybar-themes>
-   Одним из побудительных мотивов установки _polybar_ может быть то, что здесь можно без проблем настроить индикатор раскладки клавиатуры.
-   Установка
    -   Gentoo:
        ```shell
        USE="i3wm" emerge x11-misc/polybar
        ```

-   Конфигурационный файл:
    -   стандартное расположение:  `~/.config/polybar/config` (`$XDG_CONFIG_HOME/polybar/config`);
    -   использую для локальных настроек только для _i3_: `~/.config/i3/polybar/config`.

<!--list-separator-->

1.  Скрипт запуска

    -   Создадим скрипт запуска `polybar`.
        ```shell
        #!/bin/bash
        # ~/.config/i3/polybar/launch.sh

        # Terminate already running bar instances
        killall -q polybar
        # If all your bars have ipc enabled, you can also use
        # polybar-msg cmd quit

        # Wait until the processes have been shut down
        while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

        # Launch Polybar, using config location ~/.config/i3/polybar/config
        polybar --config=~/.config/i3/polybar/config i3 &

        echo "Polybar launched..."
        ```
    -   Установим права на исполнение:
        ```shell
        chmod +x ~/.config/i3/polybar/launch.sh
        ```
    -   Добавим вызов `polybar` в файл конфигурации _i3_. Конфигурацию для _i3bar_ следует закомментировать.
        ```conf-unix
        ## ~/.config/i3/config

        ## Start i3bar to display a workspace bar
        # bar {
        #     font pango:Source Sans Pro, FontAwesome 5 Free 10
        #     status_command	i3status --config ~/.config/i3/i3status/config
        #     position		top
        # }

        ## Start polybar
        exec_always --no-startup-id ~/.config/i3/polybar/launch.sh
        ```


### <span class="section-num">5.4</span> Запуск приложений {#запуск-приложений}

-   По умолчанию используется `dmenu`.
-   Можно заменить на `rofi` (см. [Запуск приложений. Rofi]({{< relref "2021-11-19-launcher_rofi" >}})).


#### <span class="section-num">5.4.1</span> rofi {#rofi}

-   Используется для запуска приложений, переключения окон.
-   <https://github.com/davatorium/rofi>
-   Конфигурация по умолчанию находится в `~/.config/rofi/config`.
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


### <span class="section-num">5.5</span> Блокировка экрана {#блокировка-экрана}

-   Для отключения экрана можно использовать DPMS:
    ```cfg
    exec --no-startup-id xset dpms 1800
    ```

    -   Отключается через 30 минут.


#### <span class="section-num">5.5.1</span> Блокировщик экрана `i3lock` {#блокировщик-экрана-i3lock}

-   В качестве блокировщика экрана используем `i3lock`.
    -   Установка
        -   Gentoo
            ```shell
            emerge x11-misc/i3lock
            ```
-   Использование в конфигурационном файле:
    ```cfg
    set $Locker i3lock --color=000000 && sleep 1
    ```

    -   `sleep 1` добавляет небольшую задержку, чтобы предотвратить возможное состояние гонки.
-   Для блокировки экрана после заданного периода времени можно использовать `xautolock` или `xss-lock`.
-   Использование `xautolock`.
-   Установка
    -   Gentoo
        ```shell
        emerge x11-misc/xautolock
        ```
-   Использование в конфигурационном файле:
    ```cfg
    exec --no-startup-id xautolock -time 10 -locker "$Locker"
    ```

    -   Блокирует через 10 минут.
-   Использование `xss-lock`.
-   Установка
    -   Gentoo
        ```shell
        emerge x11-misc/xss-lock
        ```
-   Использование в конфигурационном файле:
    ```cfg
    exec --no-startup-id xss-lock -- "$Locker"
    ```


#### <span class="section-num">5.5.2</span> Блокировщик экрана `i3lock-color` {#блокировщик-экрана-i3lock-color}

-   Репозиторий: <https://github.com/Raymo111/i3lock-color>

<!--list-separator-->

1.  Дополнительные возможности в i3lock-color

    -   Дополнительное управление цветом элементов.
    -   Размытие текущего экрана и использование его в качестве фона блокировки.
    -   Отображение часов в индикаторе.
    -   Обновление по таймеру, а не при каждом нажатии клавиши.
    -   Отображение раскладки клавиатуры.

<!--list-separator-->

2.  Установка

    -   Gentoo
        -   Порт находится в оверлее `guru`:
            ```shell
            emerge x11-misc/i3lock-color
            ```


## <span class="section-num">6</span> Приложения {#приложения}


### <span class="section-num">6.1</span> Снимки экрана {#снимки-экрана}

-   Для скриншотов можно использовать [scrot](https://github.com/resurrecting-open-source-projects/scrot).
    -   Gentoo
        ```shell
        emerge media-gfx/scrot
        ```
-   Добавим в конфигурационный файл:
    ```conf-unix
    ## Screenshot

    ## Screenshot active display
    bindsym --release Print exec --no-startup-id scrot '%Y-%m-%d_%H-%M-%S_$wx$h.png' -e 'mv $f `xdg-user-dir PICTURES` 2>/dev/null'

    ## Screenshot current window
    bindsym --release $mod+Print exec --no-startup-id scrot -u '%Y-%m-%d_%H-%M-%S_$wx$h.png' -e 'mv $f `xdg-user-dir PICTURES` 2>/dev/null'

    ## Screenshot selected region
    bindsym --release $mod+Shift+Print exec --no-startup-id scrot -s '%Y-%m-%d_%H-%M-%S_$wx$h.png' -e 'mv $f `xdg-user-dir PICTURES` 2>/dev/null'
    ```

    -   По клавише `PrtScr` делается скриншот.
    -   По клавише `mod` + `PrtScr` делается скриншот активного окна.
    -   По клавише `mod` + `Shift` + `PrtScr` предлагается выделить область экрана, скриншот которой следует сделать.
    -   Скриншоты переносятся в каталог $XDG_PICTURES_DIR (обычно `~/Pictures` или `~/Изображения`) (см. [XDG. Пользовательские каталоги]({{< relref "2021-09-16-xdg-user-directories" >}})).


## <span class="section-num">7</span> Совместимость приложений {#совместимость-приложений}


### <span class="section-num">7.1</span> Java {#java}


#### <span class="section-num">7.1.1</span> Серое окно, приложения не меняют размер с помощью WM, меню сразу закрываются {#серое-окно-приложения-не-меняют-размер-с-помощью-wm-меню-сразу-закрываются}

-   В стандартных тулкитах для Java жестко зашит список оконных менеджеров.
-   Следует установить переменную окружения:
    ```shell
    export _JAVA_AWT_WM_NONREPARENTING=1
    ```


#### <span class="section-num">7.1.2</span> Меню в приложениях плавает отдельно, им невозможно пользоваться {#меню-в-приложениях-плавает-отдельно-им-невозможно-пользоваться}

-   В выпусках Java до версии 9 GTK интерфейс ориентирован на GTK2, в последующих версиях на GTK3.
-   GTK LookAndFeel может работать с GTK версий 2, 2.2 и 3.
-   По умолчанию используется GTK3.
-   Следует явно задать более старую версию:
    ```shell
    export JAVA_TOOL_OPTIONS='-Djdk.gtk.version=2.2'
    ```
