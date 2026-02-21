---
title: "Клавиатура. xkb"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-22T14:17:00+03:00
lastmod: 2025-05-21T10:34:00+03:00
tags: ["linux", "hard"]
categories: ["computer-science"]
draft: false
slug: "keyboard-xkb"
---

Клавиатура. xkb.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая инфорация {#общая-инфорация}


## <span class="section-num">2</span> Переключение раскладок {#переключение-раскладок}

-   Клавиши-модификаторы:
    -   `grp:alt_shift_toggle` --- Alt + Shift;
    -   `grp:ctrl_shift_toggle` --- Ctrl + Shift;
    -   `grp:win_switch` --- Клавиша Super (Win);
    -   `grp:menu_toggle` --- Клавиша Menu;
    -   `grp:caps_toggle` --- Caps Lock (одиночное нажатие);
    -   `grp:shift_caps_toggle` --- Shift + Caps Lock;
    -   `grp:alt_space_toggle` --- Alt + Space;
    -   `grp:lswitch` --- Правый Ctrl (циклическое переключение);
    -   `grp:rswitch` --- Правый Alt (циклическое переключение);
    -   `grp:toggle` --- Fn + специальная клавиша (зависит от модели)
-   Экзотические комбинации:
    -   `grp:lalt_lshift_toggle` --- Левый Alt + Левый Shift;
    -   `grp:alt_caps_toggle` --- Alt + Caps Lock;
    -   `grp:sclk_toggle` --- Scroll Lock;
    -   `grp:ctrl_alt_toggle` --- Ctrl + Alt;
    -   `grp:rctrl_switch` --- Правый Ctrl (удерживать)
-   Индикация:
    -   `grp_led:scroll` --- Индикация через Scroll Lock LED;
    -   `grp_led:caps` --- Индикация через Caps Lock LED;
    -   `grp_led:num` --- Индикация через Num Lock LED


## <span class="section-num">3</span> Третий уровень символов (level3) {#третий-уровень-символов--level3}

-   Активация:
    -   `lv3:ralt_switch` --- Правый Alt (AltGr);
    -   `lv3:switch` --- Клавиша Menu;
    -   `lv3:win_switch` --- Win + AltGr;
    -   `lv3:caps_switch` --- Caps Lock (удерживать);
    -   `lv3:enter_switch` --- Enter (удерживать);
    -   `lv3:bksl_switch` --- Backslash (удерживать);
    -   `lv3:lsgt_switch` --- Клавиша "&lt; &gt; |" (удерживать)


## <span class="section-num">4</span> Compose Key {#compose-key}

-   `compose:ralt` --- Правый Alt;
-   `compose:rwin` --- Правая Win;
-   `compose:lwin` --- Левая Win;
-   `compose:menu` --- Клавиша Menu;
-   `compose:caps` --- Caps Lock;
-   `compose:prsc` --- Print Screen


## <span class="section-num">5</span> Переназначение клавиш {#переназначение-клавиш}

-   `ctrl:nocaps` --- Caps Lock → Ctrl;
-   `ctrl:swapcaps` --- Поменять местами Caps Lock и Ctrl;
-   `altwin:swap_alt_win` --- Alt ↔ Win;
-   `altwin:menu` --- Win → Menu;
-   `caps:swapescape` --- Caps Lock ↔ Esc


## <span class="section-num">6</span> Управление из командной строки {#управление-из-командной-строки}

-   Просмотр всех доступных параметров:
    ```shell
    localectl list-x11-keymap-options
    ```


### <span class="section-num">6.1</span> Настройки в x11 {#настройки-в-x11}

-   Переключение раскладок через Caps Lock + Shift с индикацией через Scroll Lock LED:
    ```shell
    setxkbmap -option "grp:shift_caps_toggle,grp_led:scroll"
    ```

-   Третий уровень на правом Alt + Compose на Menu:
    ```shell
    setxkbmap -option "lv3:ralt_switch,compose:menu"
    ```

-   Замена Caps Lock на Ctrl + завершение Xorg через Ctrl+Alt+Backspace:
    ```shell
    setxkbmap -option "ctrl:nocaps,terminate:ctrl_alt_bksp"
    ```


### <span class="section-num">6.2</span> Настройки в sway {#настройки-в-sway}

-   Переключить на английский:
    ```shell
    swaymsg input 'type:keyboard' xkb_layout us
    ```
-   Переключить на русский:
    ```shell
    swaymsg input 'type:keyboard' xkb_layout ru
    ```
