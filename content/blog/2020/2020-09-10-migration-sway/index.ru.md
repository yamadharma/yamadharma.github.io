---
title: "Переход на Sway"
author: ["Dmitry S. Kulyabov"]
date: 2020-09-10T10:33:15+03:00
lastmod: 2025-04-23T18:32:00+03:00
tags: ["wayland", "gentoo", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "migration-sway"
project: ["misc-utils"]
---

Решил попробовать [Wayland](https://wayland.freedesktop.org/). По этой причине пришлось [перейти](http://way-cooler.org/blog/2020/01/09/way-cooler-post-mortem.html) с [awesome](https://awesomewm.org/) на [sway](https://swaywm.org/).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   <https://swaywm.org/>
-   Создавался для замены i3 (см. [Window manager i3]({{< relref "2021-05-14-window-manager-i3" >}})) под Wayland.


## <span class="section-num">2</span> Установка `sway` {#установка-sway}

```shell
emerge -v gui-wm/sway
```


### <span class="section-num">2.1</span> Репозитории `gentoo` {#репозитории-gentoo}

-   Программы для Wayland есть как в основном репозитории, так и дополнительных.
-   Хочу порекомендовать для просмотра следующие репозитории (см. [Gentoo. Дополнительные репозитории]({{< relref "2023-10-01-gentoo-additional-repositories" >}})):
    -   [wayland-desktop](https://github.com/epsilon-0/wayland-desktop)

<!--listend-->

```shell
eselect repository enable wayland-desktop
emaint sync --repo wayland-desktop
```

-   [guru](https://wiki.gentoo.org/wiki/Project:GURU)

<!--listend-->

```shell
eselect repository enable guru
emaint sync --repo guru

```


## <span class="section-num">3</span> Первоначальная конфигурация {#первоначальная-конфигурация}

-   Файл конфигурации ищется в следующем порядке:
    -   `~/.sway/config`;
    -   `$XDG_CONFIG_HOME/sway/config`;
    -   `~/.i3/config`;
    -   `$XDG_CONFIG_HOME/i3/config`;
    -   `/etc/sway/config`;
    -   `/etc/i3/config`.
    -   Переменная окружения `$XDG_CONFIG_HOME` по умолчанию установлена в `~/.config/`.
-   Пакет устанавливает глобальную конфигурацию в `/etc/sway/config`.
-   При желании внести изменение в конфигурацию можно скопировать файл глобальной конфигурации в локальную:
    ```shell
    mkdir -p ~/.config/sway
    cp /etc/sway/config ~/.config/sway/
    ```


## <span class="section-num">4</span> Конфигурация устройств ввода {#конфигурация-устройств-ввода}


### <span class="section-num">4.1</span> Общая информация {#общая-информация}

-   Сводка доступных опций:
    ```shell
    man 5 sway-input
    ```
-   Список устройств ввода можно получить, запустив:
    ```shell
    swaymsg -t get_inputs
    ```
-   Идентификатор устройства используется в файле конфигурации:
    ```conf-unix
    input <identifier> {
            # ...config options...
    }
    ```
-   Можно иметь несколько конфигураций для разных устройств:
    ```conf-unix
    # default layout
    input "1:1:AT_Translated_Set_2_keyboard" {
       xkb_layout us
    }

    # custom layout for an external keyboard
    input "1452:591:Custom_Keyboard" {
       xkb_layout YourCustomLayout
    }
    ```


### <span class="section-num">4.2</span> Раскладка клавиатуры {#раскладка-клавиатуры}

-   Информация по параметрам:
    ```shell
    man 7 xkeyboard-config
    ```
-   Конфигурация раскладки:
    ```conf-unix
    # or input <identifier>
    input "type:keyboard" {
            xkb_layout us,de
            xkb_variant ,nodeadkeys
            xkb_options grp:alt_shift_toggle
    }
    ```
-   Настройка модификаций доступна через `xkb_options`.
-   Варианты можно найти в `/usr/share/X11/xkb/symbols/{altwin,capslock,compose,ctrl}`, соответствующее имя параметра находится в `/usr/share/X11/xkb/rules/base`.
-   Для команд `xkb_layout`, `xkb_model`, `xkb_options`, `xkb_rules`, `xkb_variant` несколько вариантов разделяются запятыми.
-   Чтобы активировать несколько опций, необходимо перечислить их через запятую, например `xkb_options caps:escape,altwin:swap_lalt_lwin;`.
-   Если записать опции в несколько строк,  будет действовать только последняя.


#### <span class="section-num">4.2.1</span> Примеры модификации {#примеры-модификации}

-   [Клавиатура. xkb]({{< relref "2025-04-22--keyboard-xkb" >}})
-   _Caps Lock_ работает как _Escape_: `xkb_options caps:escape`.
-   Поменять местами _Escape_ и _Caps Lock_: `xkb_options caps:swapescape`.
-   _Caps Lock_ меняется с _Control_: `xkb_options ctrl:nocaps`.
-   _Caps Lock_ становится дополнительным _Control_: `xkb_options caps:ctrl_modifier`.
-   Поменять местами _левый Alt_ и _Super_, установить _Caps Lock_ как _Escape_: `xkb_options altwin:swap_lalt_lwin,caps:escape`.
-   _Menu_ становится дополнительным _Super_: `xkb_options altwin:menu_win`.


## <span class="section-num">5</span> Комбинации клавиш {#комбинации-клавиш}


### <span class="section-num">5.1</span> Режимы и управление окнами {#режимы-и-управление-окнами}

| Клавиатурная комбинация                                 | Описание                                                                                    |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `Mod + Shift + Space`                                   | Переключение окна в плавающий режим и обратно                                               |
| `Mod + Shift + minus`                                   | Отправка окна в блокнот (scratchpad)                                                        |
| `Mod + minus`                                           | Сворачивание, вызов окна в блокноте (scratchpad)                                            |
| `Mod + b`                                               | Горизонтальное разделение                                                                   |
| `Mod + v`                                               | Вертикальное разделение                                                                     |
| `Mod + e`                                               | Переключить разделение                                                                      |
| `Mod + s`                                               | Стековое размещение (stacking layout)                                                       |
| `Mod + w`                                               | Размещение с табами (tabbed layout)                                                         |
| `Mod + r`                                               | И изменение размеров, используем `h`, `j`, `k` , `l` или ←,→,↑,↓, выход из режима --- `Esc` |
| `Mod + {←,→,↑,↓}` или `Mod + {h,j,k,l}`                 | Перемещение по окнам                                                                        |
| `Mod + Shift + {←,→,↑,↓}` или `Mod + Shift + {h,j,k,l}` | Меняет позицию окна                                                                         |
| `Mod + {0..9}`                                          | Переключение между workspace'ами                                                            |
| `Mod + Shift + {0..9}`                                  | Перемещение окна на заданный workspace                                                      |
| `Mod + =Shift + =q`                                     | Закрыть текущее окно                                                                        |
| `Mod + =f`                                              | Раскрыть окно во весь экран или свернуть его обратно                                        |


### <span class="section-num">5.2</span> Разное {#разное}

| Клавиатурная комбинация | Описание                                        |
|-------------------------|-------------------------------------------------|
| `Mod + Enter`           | открыть новый терминал                          |
| `Mod + d`               | запустить программу                             |
| `Mod + =Shift + =c`     | перечитать конфигурацию `sway` (перестартовать) |
| `Mod + Shift + e`       | Выйти из `sway`                                 |


## <span class="section-num">6</span> Совместимость приложений {#совместимость-приложений}

-   [Sway. Совместимость приложений]({{< relref "2024-06-20-sway-application-compatibility" >}})
