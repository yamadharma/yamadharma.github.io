---
title: "Sway. Конфигурация"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-12T20:02:00+03:00
lastmod: 2025-06-26T10:43:00+03:00
tags: ["configuration", "linux"]
categories: ["computer-science"]
draft: false
slug: "sway-configuration"
---

Конфигурация Sway.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


### <span class="section-num">1.1</span> Расположение {#расположение}

-   Конфигурация находится в:
    -   `/usr/share/sway/`;
    -   `/etc/sway/`;
    -   `~/.config/sway`.


### <span class="section-num">1.2</span> Переменные среды {#переменные-среды}

-   Переменные среды задаются в:
    -   `/etc/sway/environment`;
    -   `~/.config/sway/environment`.


### <span class="section-num">1.3</span> Разделы {#разделы}

-   Файлы конфигурации сгруппированы в разделы.
-   50-59 ( `50-rules-*.conf` )
    -   Оконные правила( `for_window`, `assign`  и соответствующую конфигурацию).
-   60-69 ( `60-bindings-*.conf`, `65-mode-.conf`)
    -   Привязки клавиш и режимы привязки
-   90-94 ( `90-*.conf` )
    -   Системные приложения: панели, демоны простоя и другие компоненты.
-   95-99 ( `95-*.conf` )
    -   Автозапуск приложений


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   Пакет идёт в основном репозитории:

<!--listend-->

```shell
emerge gui-wm/sway
```


## <span class="section-num">3</span> Конфигурация Sway {#конфигурация-sway}


### <span class="section-num">3.1</span> Сочетания клавиш {#сочетания-клавиш}

-   [Sway. Сочетания клавиш]({{< relref "2024-08-24-sway-keybindings" >}})


### <span class="section-num">3.2</span> Статусные панели {#статусные-панели}

-   Конфигурационный файл: `config.d/80-bar.conf`.

<!--listend-->

```conf-unix
## Status Bar
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
  config.d/80-bar.conf
</div>


#### <span class="section-num">3.2.1</span> Sway-bar {#sway-bar}

-   Sway-bar идёт в составе Sway.

<!--listend-->

```conf-unix
### sway-bar
## Read `man 5 sway-bar` for more information about this section.

# bar {
#    font pango:Iosevka Nerd Font Propo, Font Awesome 6 Free, Font Awesome 6 Brands, sans-serif 12
#    position top

# When the status_command prints a new line to stdout, swaybar updates.
# The default just shows the current date and time.
# status_command while date +'%Y-%m-%d %H:%M:%S'; do sleep 1; done
# status_command i3status
#    status_command i3blocks

#      colors {
#      	    statusline #ffffff
#             background #323232
# 	    inactive_workspace #32323200 #32323200 #5c5c5c
# 	}
# }
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 2:</span>
  config.d/80-bar.conf
</div>


#### <span class="section-num">3.2.2</span> Waybar {#waybar}

-   [Wayland. Панель Waybar]({{< relref "2024-11-21-wayland-waybar" >}})

<!--listend-->

```conf-unix
### Waybar
## https://github.com/Alexays/Waybar

## Waybar Tooltips don't steel focus

# no_focus [app_id="waybar"]
# for_window [app_id="waybar" floating] {
# 	   move position cursor
# 	   move down 60px # adjust if some menus still don't fit
# }
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 3:</span>
  config.d/80-bar.conf
</div>

-   Запускать можно разными способами.
-   Запуск скриптом. Скрипт убивает waybar и запускает заново:
    ```shell
    exec_always ~/.config/waybar/waybar.sh
    ```
-   Запуск через `waybar.service`:
    ```conf-unix
    # exec_always systemctl --user restart waybar.service
    ```
-   Запуск через инфраструктуру _Swaybar_:
    ```conf-unix
    # bar {
    #     position top
    #     # Execute Waybar; Waybar restarts when Sway reloads.
    #     status_command waybar
    #     # Hide Sway's builtin status bar.
    #     mode invisible
    # }
    ```

    -   При этом после перезапуска _Sway_ waybar не перезапускается, а запускает новый экземпляр.


#### <span class="section-num">3.2.3</span> Nwg-panel {#nwg-panel}

```conf-unix
### nwg-panel
## GTK3-based panel for sway and Hyprland Wayland compositors
## https://nwg-piotr.github.io/nwg-shell/nwg-panel
## https://github.com/nwg-piotr/nwg-panel

# exec_always nwg-panel -c preset-1 -s preset-1.css
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 4:</span>
  config.d/80-bar.conf
</div>


#### <span class="section-num">3.2.4</span> Yambar {#yambar}

-   <https://codeberg.org/dnkl/yambar>

<!--listend-->

```conf-unix
### yambar
## https://codeberg.org/dnkl/yambar

# exec_always yambar
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 5:</span>
  config.d/80-bar.conf
</div>


### <span class="section-num">3.3</span> Менеджер паролей {#менеджер-паролей}


#### <span class="section-num">3.3.1</span> Tessen {#tessen}

-   [Менеджер паролей pass. Tessen]({{< relref "2024-12-01-password-manager-pass-tessen" >}})

<!--listend-->

```conf-unix
## A bash script to handle Simple Password Store in a convenient way using rofi
## https://github.com/ayushnix/tessen

## Dmenu // Password Manager // ◆ Super ⎈ Ctrl p ##
$bindsym $mod+Ctrl+p exec "tessen"
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 6:</span>
  config.d/80-pass.conf
</div>


### <span class="section-num">3.4</span> Рабочие пространства {#рабочие-пространства}

-   Конфигурационный файл: `config.d/03-workspace.conf`

<!--listend-->

```conf-unix
# To enable floating windows or window assignments, open the application
# and then use the app_id, the class, the instance and the title
# attributes to enable floating windows/window assignments. The
# following command will list the properties of all the open windows.

# ```bash
# swaymsg -t get_tree
# ```

# To get only the `app_id`'s of all open windows use:

# ```bash
# swaymsg -t get_tree | grep "app_id"
# ```

# To get the `app_id` of the focused window use:

# ```bash
# swaymsg -t get_tree | jq -r '..|try select(.focused == true)'
# ```

# If the `app_id` happens to be null for some windows, you might have to
# use the class and/or the instance attributes to enable floating
# mode/window assignments. You can search the output and create fine
# grained rules for your windows.
```


#### <span class="section-num">3.4.1</span> Именование рабочих пространств {#именование-рабочих-пространств}

```conf-unix
### Define names for workspaces
set $ws1   "1: "
set $ws2   "2: "
set $ws3   "3: "
set $ws4   "4:󱫋 "
set $ws5   "5:󰊻 "
set $ws6   "6: "
set $ws7   7
set $ws8   8
set $ws9   "9:󰨜 "
set $ws10  10
```


#### <span class="section-num">3.4.2</span> Перемещение по рабочим пространствам {#перемещение-по-рабочим-пространствам}

```conf-unix
### Switch to workspace

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

### Move focused container to workspace

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


#### <span class="section-num">3.4.3</span> Распределение программ по рабочим пространствам {#распределение-программ-по-рабочим-пространствам}

```conf-unix
### Assign program to workspace
## `swaymsg -t get_tree`

## ws1
assign [window_role="^browser$"] $ws1
assign [class="Firefox"] $ws1
assign [class="firefox"] $ws1
assign [app_id="firefox"] $ws1
assign [app_id="google-chrome"] $ws1
assign [class="Google-chrome"] $ws1
assign [class="Thunderbird"] $ws1
assign [app_id="thunderbird"] $ws1
assign [app_id="evolution"] $ws1
assign [app_id="chromium-browser-chromium"] $ws1
assign [app_id="chromium-browser.*"] $ws8

## ws2
assign [class="Emacs"] $ws2
assign [app_id="emacs"] $ws2

## ws3
assign [app_id="kitty"] $ws3

## ws4
assign [class="VirtualBox*"] $ws4
assign [app_id="virt-manager"] $ws4

## ws5
assign [class="teams-for-linux"] $ws5
assign [class="zoom"] $ws5
assign [app_id=".*Яндекс.*Браузер"] $ws1

## ws6
assign [app_id="whatsapp-for-linux"] $ws6
assign [app_id="org.telegram.desktop"] $ws6
assign [app_id="wasistlos"] $ws6
assign [app_id="ferdium"] $ws6

## ws9
assign [app_id="com.obsproject.Studio"] $ws9
```


#### <span class="section-num">3.4.4</span> Распределение рабочих пространств по мониторам {#распределение-рабочих-пространств-по-мониторам}

```conf-unix
### Assign workspace to monitor
# workspace $ws1 output eDP-1
# workspace $ws2 output DP-4
# workspace $ws3 output DP-5
```


#### <span class="section-num">3.4.5</span> Макет контейнеров по умолчанию {#макет-контейнеров-по-умолчанию}

```conf-unix
### Layout mode for new containers
## default|stacking|tabbed
workspace_layout tabbed
```
