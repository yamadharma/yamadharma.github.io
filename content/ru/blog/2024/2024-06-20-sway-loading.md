---
title: "Sway. Загрузка"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-20T21:29:00+03:00
lastmod: 2024-06-26T11:51:00+03:00
tags: ["sysadmin", "wayland"]
categories: ["computer-science"]
draft: false
slug: "sway-loading"
---

Загрузка сессии Sway.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Дисплей-менеджеры {#дисплей-менеджеры}


## <span class="section-num">2</span> Загрузка переменных среды перед сессией {#загрузка-переменных-среды-перед-сессией}

-   Для работоспособности Sway необходимо часть переменных загрузить перед сессией (см. [Sway. Совместимость приложений]({{< relref "2024-06-20-sway-application-compatibility" >}})).


### <span class="section-num">2.1</span> Скрипт загрузки Sway {#скрипт-загрузки-sway}

-   Можно использовать наработки Fedora.
-   Репозиторий: <https://gitlab.com/fedora/sigs/sway/sway-config-fedora>
-   Для запуска используется скрипт `/usr/bin/start-sway`:
    ```shell
    #!/bin/sh

    ## Internal variables
    readonly _SWAY_COMMAND="/usr/bin/sway"
    SWAY_EXTRA_ARGS=""

    ## General exports
    export XDG_CURRENT_DESKTOP=sway
    export XDG_SESSION_DESKTOP=sway
    export XDG_SESSION_TYPE=wayland

    ## Hardware compatibility
    # We can't be sure that the virtual GPU is compatible with Sway.
    # We should be attempting to detect an EGL driver instead, but that appears
    # to be a bit more complicated.
    case $(systemd-detect-virt --vm) in
        "none"|"")
            ;;
        "kvm")
            # There's two drivers we can get here, depending on the 3D acceleration
            # flag state: either virtio_gpu/virgl or kms_swrast/llvmpipe.
            #
            # The former one causes graphical glitches in OpenGL apps when using
            # 'pixman' renderer. The latter will crash 'gles2' renderer outright.
            # Neither of those support 'vulkan'.
            #
            # The choice is obvious, at least until we learn to detect the driver
            # instead of abusing the virtualization technology identifier.
            #
            # See also: https://gitlab.freedesktop.org/wlroots/wlroots/-/issues/2871
            export WLR_RENDERER=pixman
            # 'pixman' on virtio_gpu with recent kernels is glitchy. Appears that
            # it only affects atomic KMS, and legacy interface works.
            export WLR_DRM_NO_ATOMIC=1
            # WLR_NO_HARDWARE_CURSORS=1 is not needed with legacy DRM interface
            ;;
        *)
            # https://github.com/swaywm/sway/issues/6581
            export WLR_NO_HARDWARE_CURSORS=1
            ;;
    esac

    ## Apply `environment.d(5)` customizations
    # This can be used to share the custom environment configs with systemd --user.
    # Importing `systemd --user show-environment` here may have unexpected
    # consequences, such as getting a leftover `WAYLAND_DISPLAY` or `DISPLAY`
    # and breaking Sway startup. Thus, the direct call to a systemd generator.
    set -o allexport
    eval "$(/usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator)"
    set +o allexport

    ## Load Sway-specific system environment customizations
    if [ -f /etc/sway/environment ]; then
        set -o allexport
        # shellcheck source=/dev/null
        . /etc/sway/environment
        set +o allexport
    fi

    ## Load Sway-specific user environment customizations
    if [ -f "${XDG_CONFIG_HOME:-$HOME/.config}/sway/environment" ]; then
        set -o allexport
        # shellcheck source=/dev/null
        . "${XDG_CONFIG_HOME:-$HOME/.config}/sway/environment"
        set +o allexport
    fi

    ## Unexport internal variables
    # export -n is not POSIX :(
    _SWAY_EXTRA_ARGS="$SWAY_EXTRA_ARGS"
    unset SWAY_EXTRA_ARGS

    ## Log all exported WLR_ variables
    if _WLR_VARS=$(env | grep '^WLR_'); then
        printf 'environment variables for wlroots: %s' "$_WLR_VARS" |
            tr '\n' ' ' |
            systemd-cat -p notice -t "${_SWAY_COMMAND##*/}"
    fi

    # Start sway with extra arguments and send output to the journal
    # shellcheck disable=SC2086 # quoted expansion of EXTRA_ARGS can produce empty field
    exec systemd-cat -- $_SWAY_COMMAND $_SWAY_EXTRA_ARGS "$@"
    ```
-   Этот скрипт читает переменные для сессии Sway из файлов:
    -   `/etc/sway/environment`;
    -   `${XDG_CONFIG_HOME}/sway/environment` (`~/.config/sway/environment`).
-   Для запуска этого файла из стандартный дисплей-менеджеров нужно поправить файл `/usr/share/wayland-sessions/sway.desktop`:
    ```toml
    [Desktop Entry]
    Name=Sway
    Comment=An i3-compatible Wayland compositor
    Exec=start-sway
    Type=Application
    DesktopNames=sway
    ```
-   Эти патчи добавлены в оверлей _karma_ (см. [Gentoo. Дополнительные репозитории]({{< relref "2023-10-01-gentoo-additional-repositories" >}})).


### <span class="section-num">2.2</span> Локальные переменные среды для Sway {#локальные-переменные-среды-для-sway}

-   Файл с заданными локальными переменными находится в `~/.config/sway/environment`:
    ```shell
    # -*- mode: shell -*-
    # vim: set ft=sh:
    # This file will be sourced from /usr/bin/start-sway script.
    # User-specific variables should be placed in $XDG_CONFIG_HOME/sway/environment

    ## Pass extra arguments to the /usr/bin/sway executable

    #SWAY_EXTRA_ARGS="$SWAY_EXTRA_ARGS --unsupported-gpu"
    #SWAY_EXTRA_ARGS="$SWAY_EXTRA_ARGS --debug"

    ## Set environment variables

    # Useful variables for wlroots:
    # https://gitlab.freedesktop.org/wlroots/wlroots/-/blob/master/docs/env_vars.md
    #
    #WLR_NO_HARDWARE_CURSORS=1
    ```
-   Исправления для Java (см. [Sway. Совместимость приложений]({{< relref "2024-06-20-sway-application-compatibility" >}})):
    ```shell

    ## Java compatibility
    _JAVA_AWT_WM_NONREPARENTING=1
    ```
-   Исправления для Qt (см. [Sway. Совместимость приложений]({{< relref "2024-06-20-sway-application-compatibility" >}})):
    ```shell

    ## Qt tuning
    # QT_QPA_PLATFORM=wayland
    QT_QPA_PLATFORM=xcb
    QT_QPA_PLATFORMTHEME=qt6ct
    QT_WAYLAND_DISABLE_WINDOWDECORATION=1
    QT_WAYLAND_FORCE_DPI=physical
    ```
