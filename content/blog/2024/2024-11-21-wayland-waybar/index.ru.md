---
title: "Wayland. Панель Waybar"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-21T15:11:00+03:00
lastmod: 2025-02-08T17:55:00+03:00
tags: ["wayland", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "wayland-waybar"
---

Wayland. Панель Waybar

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/Alexays/Waybar>
-   Wiki: <https://github.com/Alexays/Waybar/wiki>


## <span class="section-num">2</span> Конфигурация {#конфигурация}


### <span class="section-num">2.1</span> Общая информация {#общая-информация}

-   Wiki: <https://github.com/Alexays/Waybar/wiki/Configuration>
-   Конфигурация использует формат файла JSONC и называется `config` или `config.jsonc`.
-   Каталоги для этого файла:
    -   `$XDG_CONFIG_HOME/waybar/`
    -   `~/.config/waybar/`
    -   `~/waybar/`
    -   `/etc/xdg/waybar/`
    -   `SYSCONFDIR/xdg/waybar` (если `SYSCONFDIR` установленный во время сборки, отличается от `/etc`, например `/usr/local/etc`  в системах BSD).


### <span class="section-num">2.2</span> Файл конфигурации {#файл-конфигурации}


#### <span class="section-num">2.2.1</span> Начало {#начало}

```js-json
// vim:ft=json -*- mode: js-json -*-
{
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
  config
</div>


#### <span class="section-num">2.2.2</span> Общие настройки {#общие-настройки}

```js-json
// General
"layer": "top",
// Waybar position (top|bottom|left|right)
"position": "top",
// Waybar height (to be removed for auto height)
"height": 30,
// Gaps between modules (4px)
"spacing": 4,
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 2:</span>
  config
</div>


#### <span class="section-num">2.2.3</span> Расположение модулей {#расположение-модулей}

```js-json
// Modules
"modules-left": [
    "sway/workspaces",
    "custom/scratchpad",
    "sway/mode",
],
"modules-center": [
    "custom/pomm",
    "custom/weather",
    "custom/clipboard",
    "idle_inhibitor",
],
"modules-right": [
    "memory",
    "cpu",
    "temperature",
    "battery",
    "battery#bat1",
    "network",
    "backlight",
    "wireplumber",
    "clock",
    "sway/language",
    "keyboard-state",
    "tray",
    "custom/power",
],
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 3:</span>
  config
</div>


#### <span class="section-num">2.2.4</span> Конфигурация модулей {#конфигурация-модулей}

<!--list-separator-->

1.  Информационные модули

    <!--list-separator-->

    1.  Память

        ```js-json
        // Memory
        "memory": {
            "interval": 30,
            "format": " {used:0.1f}G/{total:0.1f}G",
            "tooltip": true,
            "tooltip-format": "Free {avail:0.1f}G\nUsed: {percentage}%\nSwap: {swapPercentage}%",
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 4:</span>
          config
        </div>

    <!--list-separator-->

    2.  Процессор

        ```js-json
        // Cpu
        "cpu": {
            "interval": 10,
            "format": " {usage}% {icon}",
            "max-length": 10,
            "format-icons": ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"],
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 5:</span>
          config
        </div>

    <!--list-separator-->

    3.  Батарея

        ```js-json
        // Battery
        "battery": {
            "bat": "BAT0",
            "states": {
              "full": 100,
              "good": 95,
              "warning": 30,
              "critical": 15
            },
            "format": "{icon}  {capacity}% ({time})",
            "format-charging": " {icon}  {capacity}% ({time})",
            "format-full": " {icon}  Full",
            "format-time": "{H}h{M}m",
            "interval": 30,
            "on-click": "gnome-power-statistics",
            "format-icons": [
              " ",
              " ",
              " ",
              " ",
              " "
            ]
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 6:</span>
          config
        </div>

    <!--list-separator-->

    4.  Температура подсистем

        -   Задаётся для температурных зон `/sys/class/thermal/` или для показаний сенсоров `/sys/class/hwmon/hwmon*/temp*_input`.
        -   Просмотреть все типы температурных зон:
            ```bash
            for i in /sys/class/thermal/thermal_zone*; do echo "$i: $(<$i/type)"; done
            ```
        -   Если нет тепловой зоны, можно использовать сенсоры (`sensors`), чтобы найти предпочтительный источник температуры:
            ```bash
            for i in /sys/class/hwmon/hwmon*/temp*_input; do echo "$(<$(dirname $i)/name): $(cat ${i%_*}_label 2>/dev/null || echo $(basename ${i%_*})) $(readlink -f $i)"; done
            ```
        -   Сама конфигурация выглядит следующим образом:

        <!--listend-->

        ```js-json
        // Themperature
        "temperature": {
            "critical-threshold": 80,
            "interval": 5,
            "thermal-zone": 1,
            "format": "{icon} {temperatureC}°C",
            "format-icons": [
                "", // Icon: temperature-empty
                "", // Icon: temperature-quarter
                "", // Icon: temperature-half
                "", // Icon: temperature-three-quarters
                ""  // Icon: temperature-full
            ],
            "tooltip": true
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 7:</span>
          config
        </div>

    <!--list-separator-->

    5.  Отображение времени

        ```js-json
        // Clock
        "clock": {
            "format": " {:%H:%M  %F, %a} ",
            "format-alt": " {:%A, %B %d, %Y (%R)}",
            "tooltip-format": "<tt><small>{calendar}</small></tt>",
            "calendar": {
                "mode"          : "year",
                "mode-mon-col"  : 3,
                "weeks-pos"     : "right",
                "on-scroll"     : 1,
                "format": {
                    "months":     "<span color='#ffead3'><b>{}</b></span>",
                    "days":       "<span color='#ecc6d9'><b>{}</b></span>",
                    "weeks":      "<span color='#99ffdd'><b>W{}</b></span>",
                    "weekdays":   "<span color='#ffcc66'><b>{}</b></span>",
                    "today":      "<span color='#ff6699'><b><u>{}</u></b></span>"
                }
            },
            "actions":  {
                "on-click-right": "mode",
                "on-scroll-up": "tz_up",
                "on-scroll-down": "tz_down",
                "on-scroll-up": "shift_up",
                "on-scroll-down": "shift_down"
            }
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 8:</span>
          config
        </div>

    <!--list-separator-->

    6.  Состояние клавиатуры

        ```js-json
        // Keyboard
        "keyboard-state": {
            "numlock": true,
            "capslock": true,
            "format": " {name} {icon}",
            "format-icons": {
                "locked": " ",
                "unlocked": " "
            }
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 9:</span>
          config
        </div>

    <!--list-separator-->

    7.  Сеть

        ```js-json
        // Network
        "network": {
            "format": "{ifname}",
            "format-wifi": " {essid}",
            "format-ethernet": " {ifname}",
            "format-disconnected": "", //An empty format will hide the module.
            "tooltip-format": "{ipaddr}/{cidr} via {gwaddr}",
            "tooltip-format-wifi": " {essid} ({signalStrength}%)",
            "tooltip-format-ethernet": "󰩠 {ipaddr}/{cidr} via {gwaddr}",
            "tooltip-format-disconnected": "󰲛 Disconnected",
            "max-length": 50,
            "on-click": "nm-connection-editor"
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 10:</span>
          config
        </div>

<!--list-separator-->

2.  Управляемые модули

    <!--list-separator-->

    1.  Звук

        <!--list-separator-->

        1.  Pulseaudio

            ```js-json
            // Sound (pulseaudio)
            "pulseaudio": {
                "format": "{icon} {volume}% {format_source}",
                "format-bluetooth": "{icon}  {volume}% {format_source}",
                "format-bluetooth-muted": "󰝟  {format_source}",
                "format-muted": "󰝟 {format_source}",
                "format-source": " {volume}%",
                "format-source-muted": " ",
                "format-icons": {
                  "headphone": " ",
                  "hands-free": " ",
                  "headset": "󰋎 ",
                  "phone": " ",
                  "portable": " ",
                  "car": " ",
                  "default": [
                        "",
                        " ",
                        " "
                  ]
                },
                "scroll-step": 5,
                "on-click": "pavucontrol",
                "on-click-right": "blueman-manager"
            },
            ```
            <div class="src-block-caption">
              <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 11:</span>
              config
            </div>

        <!--list-separator-->

        2.  Pipewire

            ```js-json
            // Sound (pipewire)
            "wireplumber": {
                "format": "{icon}{volume}%",
                "format-muted": " ",
                // "on-click": "helvum",
                "on-click": "pavucontrol",
                "on-click-middle": "wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle",
                "format-icons": ["", " ", " "],
                "max-volume": 200,
                // "scroll-step": 0.2,
            },
            ```
            <div class="src-block-caption">
              <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 12:</span>
              config
            </div>

    <!--list-separator-->

    2.  Трей

        ```js-json
        // Tray
        "tray": {
            "icon-size": 20,
            "spacing": 10
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 13:</span>
          config
        </div>

    <!--list-separator-->

    3.  Отключение засыпания экрана

        ```js-json
        // Idle inhibitor
        "idle_inhibitor": {
            "format": "{icon}",
            "format-icons": {
              "activated": "  ",
              "deactivated": "  "
            }
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 14:</span>
          config
        </div>

    <!--list-separator-->

    4.  Подсветка экрана

        ```js-json
        "backlight": {
            "device": "intel_backlight",
            "format": "{icon} {percent}% ",
            "format-icons": [" ", " "],
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 15:</span>
          config
        </div>

<!--list-separator-->

3.  Модули _Sway_

    <!--list-separator-->

    1.  Окна _Sway_

        ```js-json
        "sway/window": {
            "format": "{}",
            "max-length": 40
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 16:</span>
          config
        </div>

    <!--list-separator-->

    2.  Режим _Sway_

        ```js-json
        "sway/mode": {
            "format": "  {}",
            "max-length": 50
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 17:</span>
          config
        </div>

    <!--list-separator-->

    3.  Рабочие столы _Sway_

        ```js-json
        "sway/workspaces": {
            "disable-scroll": false,
            "disable-scroll-wraparound": true,
            "all-outputs": true,
            "format": "{index}:{name}",
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 18:</span>
          config
        </div>

    <!--list-separator-->

    4.  Переключатель языка _Sway_

        ```js-json
        "sway/language": {
            "format": " {short} ",
            "on-click": "swaymsg input type:keyboard xkb_switch_layout next",
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 19:</span>
          config
        </div>

<!--list-separator-->

4.  Самописные модули

    <!--list-separator-->

    1.  Погода

        ```js-json
        // Weather
        "custom/weather": {
            "format": "{icon} {text}",
            "tooltip": true,
            "interval": 3600,
            // accepts -c/--city <city> -t/--temperature <C/F> -d/--distance <km/miles>
            "exec": "~/.config/sway/scripts/weather.py",
            "return-type": "json",
            "format-icons": {
                "Unknown": "",
                "Cloudy": "󰖐",
                "Fog": "",
                "HeavyRain": "",
                "HeavyShowers": "",
                "HeavySnow": "",
                "HeavySnowShowers": "󰜗",
                "LightRain": "",
                "LightShowers": "",
                "LightSleet": "",
                "LightSleetShowers": "",
                "LightSnow": "",
                "LightSnowShowers": "󰙿",
                "PartlyCloudy": "",
                "Sunny": "",
                "ThunderyHeavyRain": "󰙾",
                "ThunderyShowers": "",
                "ThunderySnowShowers": "",
                "VeryCloudy": ""
            }
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 20:</span>
          config
        </div>

    <!--list-separator-->

    2.  Скратчпад

        ```js-json
        // Scratchpad
        "custom/scratchpad": {
            "interval": "once",
            "escape": true,
            "return-type": "json",
            "format": "{icon}",
            "format-icons": {
                "one": "󰖯 ",
                "many": "󰖲 "
            },
            "exec": "/bin/sh ~/.config/sway/scripts/scratchpad.sh",
            "on-click": "swaymsg 'scratchpad show'",
            "signal": 7
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 21:</span>
          config
        </div>

    <!--list-separator-->

    3.  Отключение машины

        ```js-json
        "custom/power": {
            "format" : "⏻ ",
            "tooltip": false,
            "menu": "on-click",
            "menu-file": "$HOME/.config/waybar/power_menu.xml", // Menu file in resources folder
            "menu-actions": {
              "shutdown": "shutdown",
              "reboot": "reboot",
              "suspend": "systemctl suspend",
              "hibernate": "systemctl hibernate"
            }
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 22:</span>
          config
        </div>

    <!--list-separator-->

    4.  Буфер обмена

        ```js-json
        // Clipboard
        "custom/clipboard": {
            "format": " ",
            "interval": "once",
            "return-type": "json",
            "on-click": "swaymsg -q exec '$clipboard'; pkill -RTMIN+9 waybar",
            "on-click-right": "swaymsg -q exec '$clipboard-del'; pkill -RTMIN+9 waybar",
            "on-click-middle": "swaymsg -q exec '$clipboard-del-all'",
            "exec": "printf '{\"tooltip\":\"%s\"}' $(cliphist list | wc -l)",
            "exec-if": "[ -x \"$(command -v cliphist)\" ] && [ $(cliphist list | wc -l) -gt 0 ]",
            "signal": 9
        },
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 23:</span>
          config
        </div>

    <!--list-separator-->

    5.  Мониторинг `pomm`

        -   [Emacs. Пакет pomm]({{< relref "2025-02-08--emacs-pomm" >}})
            ```js-json
            // pomm pomodoro timer
            "custom/pomm": {
                "interval": 1,
                "format": " {text}",
                "exec": "/bin/sh ~/.config/waybar/script/pomm.sh"
            },
            ```
            <div class="src-block-caption">
              <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 24:</span>
              config
            </div>


#### <span class="section-num">2.2.5</span> Конец {#конец}

```js-json
}
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 25:</span>
  config
</div>


## <span class="section-num">3</span> Стили {#стили}


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   Wiki: <https://github.com/Alexays/Waybar/wiki/Styling>
-   Стилизация выполняется с использованием формата файла CSS и файла с именем `style.css`.
-   Можно также использовать `style-light.css` и `style-dark.css` соответственно, чтобы следовать системной теме.
-   Каталоги для этого файла:
    -   `~/.config/waybar/`;
    -   `~/waybar/`;
    -   `/etc/xdg/waybar/`.
-   Можно указывать не конкретные цвета, а цвета из GTK-темы (<https://gitlab.gnome.org/GNOME/gtk/-/blob/gtk-3-24/gtk/theme/Adwaita/_colors-public.scss>).


### <span class="section-num">3.2</span> Стилевой файл {#стилевой-файл}

```css
/* Waybar configuration */

/* Keyframes */

@keyframes blink-warning {
    70% {
      color: white;
    }

    to {
      color: white;
      background-color: orange;
    }
}

@keyframes blink-critical {
    70% {
      color: white;
    }

    to {
      color: white;
      background-color: red;
    }
}

/* Base styles */

/* Reset all styles */
* {
    border: none;
    border-radius: 0;
    min-height: 0;
    margin: 0;
    padding: 0;
    font-family: "Iosevka Nerd Font Propo", "Font Awesome 6 Free", "Font Awesome 6 Brands", sans-serif;
    font-size: 14px;
}

/* The whole bar */
window#waybar {
    /* background: @theme_fg_color; */
    background: @theme_base_color;
    /* background: #323232; */
    border-bottom: 1px solid @unfocused_borders;
    color: @theme_text_color;
    /* color: black; */
    /* color: white; */
}

/* Each module */
#battery,
#clock,
#cpu,
#custom-keyboard-layout,
#memory,
#mode,
#network,
#pulseaudio,
#temperature,
#tray {
    padding-left: 4px;
    padding-right: 4px;
}

/* -----------------------------------------------------------------------------
 * Module styles
 * -------------------------------------------------------------------------- */

#battery {
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    animation-direction: alternate;
}

#battery.warning {
    color: orange;
}

#battery.critical {
    color: red;
}

#battery.warning.discharging {
    animation-name: blink-warning;
    animation-duration: 3s;
}

#battery.critical.discharging {
    animation-name: blink-critical;
    animation-duration: 2s;
}

#clock {
    font-weight: bold;
}

#cpu {
  /* No styles */
}

#cpu.warning {
    color: orange;
}

#cpu.critical {
    color: red;
}

#memory {
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    animation-direction: alternate;
}

#memory.warning {
    color: orange;
}

#memory.critical {
    color: red;
    animation-name: blink-critical;
    animation-duration: 2s;
}

#mode {
    background: #64727D;
    border-top: 2px solid white;
    /* To compensate for the top border and still have vertical centering */
    padding-bottom: 2px;
}

#network {
    /* No styles */
}

#network.disconnected {
    color: orange;
}

#pulseaudio {
    /* No styles */
}

#pulseaudio.muted {
    /* No styles */
}

#custom-spotify {
    color: rgb(102, 220, 105);
}

#temperature {
    /* No styles */
}

#temperature.critical {
    color: red;
}

#tray {
    /* No styles */
}

#window {
    font-weight: bold;
}

#workspaces button {
    border-top: 2px solid transparent;
    /* To compensate for the top border and still have vertical centering */
    padding-bottom: 2px;
    padding-left: 10px;
    padding-right: 10px;
    color: #888888;
}

#workspaces button.focused {
    border-color: #4c7899;
    color: white;
    background-color: #285577;
}

#workspaces button.urgent {
    border-color: #c9545d;
    color: #c9545d;
}
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 26:</span>
  style.css
</div>


## <span class="section-num">4</span> Вспомогательные файлы {#вспомогательные-файлы}


### <span class="section-num">4.1</span> Перезапуск Waybar {#перезапуск-waybar}

-   Для перезапуска можно использовать скрипт:
    ```shell
    ## Restart waybar

    run_waybar() {
        waybar
    }

    restart_waybar() {
        pid=$(pgrep waybar)
        [[ ! -z $pid ]] && kill $pid
        run_waybar
    }

    restart_waybar
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 27:</span>
      waybar.sh
    </div>


### <span class="section-num">4.2</span> Меню выключения компьютера {#меню-выключения-компьютера}

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkMenu" id="menu">
    <child>
      <object class="GtkMenuItem" id="suspend">
      <property name="label">Suspend</property>
      </object>
    </child>
    <child>
      <object class="GtkMenuItem" id="hibernate">
      <property name="label">Hibernate</property>
      </object>
    </child>
    <child>
      <object class="GtkMenuItem" id="shutdown">
      <property name="label">Shutdown</property>
      </object>
    </child>
    <child>
      <object class="GtkSeparatorMenuItem" id="delimiter1"/>
    </child>
    <child>
      <object class="GtkMenuItem" id="reboot">
      <property name="label">Reboot</property>
      </object>
    </child>
  </object>
</interface>
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 28:</span>
  power_menu.xml
</div>


### <span class="section-num">4.3</span> Мониторинг pomm {#мониторинг-pomm}

-   [Emacs. Пакет pomm]({{< relref "2025-02-08--emacs-pomm" >}})
-   Для мониторинга `pomm` можно использовать скрипт:
    ```shell
    ## Interface to pomm.el

    if ps -e | grep emacs >> /dev/null
    then
        emacsclient --eval "(if (boundp 'pomm-current-mode-line-string) pomm-current-mode-line-string \"\") " | xargs echo -e
    fi
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 29:</span>
      pomm.sh
    </div>


## <span class="section-num">5</span> Ресурсы {#ресурсы}

-   Дополнительные модули:
    -   <https://github.com/LawnGnome/waybar-custom-modules>
