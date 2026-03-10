---
title: "Конфигурация командной оболочки bash"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-01T18:33:00+03:00
lastmod: 2025-01-01T19:04:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "bash-shell-configuration"
---

Конфигурация командной оболочки bash.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Основной файл {#основной-файл}

-   Конфигурация `~/.bashrc`:
    ```bash
    ## .bashrc

    ## Test for an interactive shell.  There is no need to set anything
    ## past this point for scp and rcp, and it's important to refrain from
    ## outputting anything in those cases.
    # if [[ $- != *i* ]] ; then
    # 	# Shell is non-interactive.  Be done now!
    # 	return
    # fi
    ```

<!--listend-->

-   Загрузка глобальных настроек:
    ```bash
    ## Source global definitions
    if [ -f /etc/bash/bashrc ]; then
        . /etc/bash/bashrc
    fi

    # Source global definitions
    if [ -f /etc/profile ]; then
        . /etc/profile
    fi

    ## Uncomment the following line if you don't like systemctl's auto-paging feature:
    # export SYSTEMD_PAGER=
    ```
-   Загрузка дополнений командной строки:
    ```bash
    ## Uncomment the following to activate bash-completion:
    [ -f /etc/profile.d/bash-completion ] && source /etc/profile.d/bash-completion
    ```
-   Дополнительные функции:
    ```bash
    ## User specific aliases and functions
    if [ -d ~/.bashrc.d ]; then
        for rc in ~/.bashrc.d/*; do
            if [ -f "$rc" ]; then
                . "$rc"
            fi
        done
    fi

    unset rc
    ```
-   Загрузка командной оболочки fish (см. [Командная оболочка fish]({{< relref "2025-01-01--fish-shell" >}})):
    ```bash
    ## Run fish as interrective shell
    if [[ $(ps --no-header --pid=$PPID --format=comm) != "fish" && -z ${BASH_EXECUTION_STRING} ]]
    then
        SHELL=/bin/fish exec fish
    fi
    ```


## <span class="section-num">2</span> Дополнительные функции {#дополнительные-функции}

-   Дополнительные функции находятся в каталоге `~/.bashrc.d`.


### <span class="section-num">2.1</span> Поддержка wayland {#поддержка-wayland}

-   Конфигурационный файл: `~/.bashrc.d/wayland.bash`.
-   Загружается, если сессия wayland:
    ```bash
    if [[ $XDG_SESSION_TYPE == "wayland" ]]
    then
        ## qt wayland
        # export QT_QPA_PLATFORM=xcb
        export QT_QPA_PLATFORM="wayland"
        export QT_WAYLAND_DISABLE_WINDOWDECORATION="1"

        ## Most pure GTK3 apps use wayland by default, but some,
        ## such as Firefox, require the backend to be explicitly selected.
        export MOZ_ENABLE_WAYLAND=1
        export MOZ_DBUS_REMOTE=1
        export GTK_CSD=0

        ## Java XWayland blank screens fix
        export _JAVA_AWT_WM_NONREPARENTING=1

        ## set ozone platform to wayland
        export ELECTRON_OZONE_PLATFORM_HINT=wayland

        ## Disable hardware cursors. This might fix issues with
        ## disappearing cursors
        if systemd-detect-virt -q
        then
        ## if the system is running inside a virtual machine, disable hardware cursors
        export WLR_NO_HARDWARE_CURSORS=1
        fi

        ## Disable warnings by OpenCV
        export OPENCV_LOG_LEVEL=ERROR
    fi
    ```
