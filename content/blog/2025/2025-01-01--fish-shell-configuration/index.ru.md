---
title: "Конфигурация командной оболочки fish"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-01T19:22:00+03:00
lastmod: 2025-01-01T19:53:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "fish-shell-configuration"
---

Конфигурация командной оболочки fish.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Дополнительные функции {#дополнительные-функции}

-   Дополнительные функции находятся в каталоге `~/.config/fish/functions`.


### <span class="section-num">1.1</span> Поддержка Midnight Commander {#поддержка-midnight-commander}

-   Конфигурационный файл: `~/.config/fish/functions/mc.fish`.
-   Источник <https://gist.github.com/halicki/58cedaf90f3e85277a799cef8217fc72>.
-   Поддержка смены каталога в `mc`:
    ```fish
    function mc
        set SHELL_PID %self
        set MC_PWD_FILE "/tmp/mc-$USER/mc.pwd.$SHELL_PID"

        /usr/bin/mc -P $MC_PWD_FILE $argv

        if test -r $MC_PWD_FILE

            set MC_PWD (cat $MC_PWD_FILE)
            if test -n "$MC_PWD"
                and test -d "$MC_PWD"
                cd (cat $MC_PWD_FILE)
            end

            rm $MC_PWD_FILE
        end
    end
    ```
