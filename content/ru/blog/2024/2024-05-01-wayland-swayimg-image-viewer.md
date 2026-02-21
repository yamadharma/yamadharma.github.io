---
title: "Wayland. Просмотрщик изображений Swayimg"
author: ["Dmitry S. Kulyabov"]
date: 2024-05-01T18:44:00+03:00
lastmod: 2024-05-01T21:15:00+03:00
tags: ["wayland", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "wayland-swayimg-image-viewer"
---

Wayland. Просмотрщик изображений Swayimg.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/artemsen/swayimg/>
-   Легковесный просмотрщик изображений.
-   Управляется с клавиатуры.
-   По умолчанию раскладка клавиатуры vi-подобная.
-   Поддерживаемые форматы:
    -   JPEG;
    -   JPEG XL;
    -   PNG;
    -   GIF;
    -   SVG;
    -   WebP;
    -   HEIF/AVIF;
    -   AV1F/AVIFS;
    -   TIFF;
    -   EXR;
    -   BMP;
    -   PNM;
    -   TGA.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   Репозиторий guru (см. [Gentoo. Дополнительные репозитории]({{< relref "2023-10-01-gentoo-additional-repositories" >}})).
-   Установка репозитория:
    ```shell
    eselect repository enable guru
    emaint sync -r guru
    ```
-   Установка пакета:
    ```shell
    emerge media-gfx/swayimg
    ```


## <span class="section-num">3</span> Конфигурации {#конфигурации}

-   Каталоги поиска конфигурации (файл `config`):
    -   `$XDG_CONFIG_HOME/swayimg`;
    -   `$HOME/.config/swayimg`;
    -   `$XDG_CONFIG_DIRS/swayimg`;
    -   `/etc/xdg/swayimg`.
-   Конфигурация по умолчанию `/usr/share/swayimg/swayimgrc`:
    ```conf-unix
    # Swayimg configuration file.

    # This file contains the default configuration.
    # The viewer searches for the config file in the following locations:
    # 1. $XDG_CONFIG_HOME/swayimg/config
    # 2. $HOME/.config/swayimg/config
    # 3. $XDG_CONFIG_DIRS/swayimg/config
    # 4. /etc/xdg/swayimg/config

    # Any of these options can be overridden using the --config argument
    # on the command line, for instance:
    # $ swayimg --config="general.scale=real"

    ################################################################################
    # General options
    ################################################################################
    [general]

    # Initial scale (optimal/fit/width/height/fill/real)
    scale = optimal

    # Start in full screen mode (yes/no)
    fullscreen = no

    # Anti-aliasing (yes/no)
    antialiasing = no

    # Background for transparent images (none/grid/RGB, e.g. #112233)
    transparency = grid

    # Window position (parent or absolute coordinates, e.g. 100,200)
    position = parent
    # Window size (parent, image, or absolute size, e.g. 800,600)
    size = parent
    # Window background mode/color (none/RGB, e.g. #112233)
    background = none

    # Run slideshow at startup (yes/no)
    slideshow = no
    # Slideshow image display time (seconds)
    slideshow_time = 3

    ################################################################################
    # Image list configuration
    ################################################################################
    [list]
    # Default order (none/alpha/random)
    order = alpha
    # Looping list of images (yes/no)
    loop = yes
    # Read directories recursively (yes/no)
    recursive = no
    # Open all files in the start directory (yes/no)
    all = yes

    ################################################################################
    # Font configuration
    ################################################################################
    [font]
    # Font name
    name = monospace
    # Font size (in pt)
    size = 14
    # Font color
    color = #cccccc
    # Drop shadow (none/RGB, e.g. #112233)
    shadow = #000000

    ################################################################################
    # Image meta info scheme (format, size, EXIF, etc)
    ################################################################################
    [info]
    # Mode on startup (off/brief/full)
    mode = full
    # Display scheme for the "full" mode: position = content
    full.topleft = name,format,filesize,imagesize,exif
    full.topright = index
    full.bottomleft = scale,frame
    full.bottomright = status
    # Display scheme for the "brief" mode: position = content
    brief.topleft = index
    brief.topright = none
    brief.bottomleft = none
    brief.bottomright = status

    ################################################################################
    # Key binding section: key = action [parameters]
    # Key can be specified with modifiers, e.g "Ctrl+Alt+Shift+x"
    # Use the `xkbcli` tool to get key name: `xkbcli interactive-wayland`
    ################################################################################
    [keys]
    F1 = help
    Home = first_file
    End = last_file
    Prior = prev_file
    Next = next_file
    Space = next_file
    Shift+d = prev_dir
    d = next_dir
    Shift+o = prev_frame
    o = next_frame
    Shift+s = slideshow
    s = animation
    f = fullscreen
    Left = step_left 10
    Right = step_right 10
    Up = step_up 10
    Down = step_down 10
    Equal = zoom +10
    Plus = zoom +10
    Minus = zoom -10
    w = zoom width
    Shift+w = zoom height
    z = zoom fit
    Shift+z = zoom fill
    0 = zoom real
    BackSpace = zoom optimal
    bracketleft = rotate_left
    bracketright = rotate_right
    m = flip_vertical
    Shift+m = flip_horizontal
    a = antialiasing
    r = reload
    i = info
    e = exec echo "Image: %"
    Escape = exit
    q = exit

    ################################################################################
    # Mouse / touchpad configuration, same format as in [keys]
    ################################################################################
    [mouse]
    ScrollLeft = step_right 5
    ScrollRight = step_left 5
    ScrollUp = step_down 5
    ScrollDown = step_up 5
    Ctrl+ScrollUp = zoom +10
    Ctrl+ScrollDown = zoom -10
    Shift+ScrollUp = prev_file
    Shift+ScrollDown = next_file
    Alt+ScrollUp = prev_frame
    Alt+ScrollDown = next_frame

    # vim: filetype=dosini
    ```


## <span class="section-num">4</span> Установка по умолчанию {#установка-по-умолчанию}

-   Можно установить swayimg как просмотрщик по умолчанию (см. [XDG. Приложения MIME]({{< relref "2023-04-02-xdg-mime-applications" >}})).
-   Проверим, какие ассоциации актуальны:
    ```shell
    cat /usr/share/applications/swayimg.desktop | grep -i MimeType | cut -d "=" -f 2 | tr ';' '\n' | xargs -l1 xdg-mime query default
    ```
-   Установим для всех типов ассоциацию с _swayimg_:
    ```shell
    cat /usr/share/applications/swayimg.desktop | grep -i MimeType | cut -d "=" -f 2 | tr ';' '\n' | xargs -l1 xdg-mime default swayimg.desktop
    ```
