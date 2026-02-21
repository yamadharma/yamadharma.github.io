---
title: "Командная оболочка fish"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-01T16:09:00+03:00
lastmod: 2025-02-14T21:39:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "fish-shell"
---

Командная оболочка fish.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://fishshell.com/>
-   Обучающая информация: <https://fishshell.com/docs/current/tutorial.html>
-   Не является POSIX-совместимой.


## <span class="section-num">2</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge app-shells/fish
    ```


## <span class="section-num">3</span> Интеграция с системой {#интеграция-с-системой}

-   fish может устанавливаться:
    -   как оболочка по умолчанию (запускаться сразу при входе в систему);
    -   запускается вручную как дочерний процесс текущей оболочки по умолчанию.


### <span class="section-num">3.1</span> Установка fish в качестве оболочки по умолчанию {#установка-fish-в-качестве-оболочки-по-умолчанию}

-   Этот режим требует понимания функционирования fish и её скриптового языка.
-   Текущие скрипты инициализации и переменные окружения пользователя должны быть перенесены в новое окружение fish.
-   Установите оболочку конкретного пользователя на `/usr/bin/fish`:
    ```shell
    $ chsh -s /usr/bin/fish
    ```
-   Если вы используете `systemd-homed`:
    ```shell
    $ homectl update --shell=/usr/bin/fish
    ```
-   Необходимо перенести настройки из скриптов инициализации bash: `/etc/profile`, `~/.bash_profile`, `/etc/bash.bashrc`, `~/.bashrc`.


### <span class="section-num">3.2</span> Установка fish только в качестве интерактивной оболочки {#установка-fish-только-в-качестве-интерактивной-оболочки}

-   Все скрипты инициализации Bash запускаются как обычно.
-   fish работает поверх Bash в интерактивном режиме, подключённом к терминалу.
-   При входе будут выполняться текущие скрипты bash.
-   Переменные окружения текущего пользователя остаются неизменными и экспортируются в fish, которая затем запускается как дочерний процесс bash.


#### <span class="section-num">3.2.1</span> Запуск fish через .bashrc {#запуск-fish-через-dot-bashrc}

-   Это наиболее универсальное решение.
-   Добавьте строку `exec fish` в подходящий файл настроек Bash, например `~/.bashrc`.
-   Можно использовать команду `bash --norc`, чтобы вручную войти в _bash_ без выполнения команд из `~/.bashrc` (чтобы не запускать _fish_).
-   Чтобы команды наподобие `bash -c 'echo test'` выполняли команду в _bash_ вместо запуска _fish_, можно написать `if [ -z "$BASH_EXECUTION_STRING" ]; then exec fish; fi` вместо простого `exec`.
-   Можно настроить вход в fish только в том случае, если родительский процесс не является fish. Это позволяет быстро войти в bash, вызвав команду bash, без потери настроек из `~/.bashrc`:
    ```shell
    if [[ $(ps --no-header --pid=$PPID --format=comm) != "fish" && -z ${BASH_EXECUTION_STRING} ]]
    then
        SHELL=/bin/fish exec fish
    fi
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      ~/.bashrc
    </div>


#### <span class="section-num">3.2.2</span> Использование настроек эмулятора терминала {#использование-настроек-эмулятора-терминала}

-   В большинстве терминалов для запуска оболочки используется аргумент `-e`.
-   Например, для _gnome-terminal_:
    ```shell
    gnome-terminal -e fish
    ```
-   В эмуляторах терминала, которые не поддерживают установку оболочки (например, lilyterm):
    ```shell
    SHELL=/usr/bin/fish lilyterm
    ```


#### <span class="section-num">3.2.3</span> Использование настроек терминального мультиплексора {#использование-настроек-терминального-мультиплексора}

-   Для _tmux_ добавьте следующее в файл `~/.tmux.conf`:
    ```shell
    set-option -g default-shell "/usr/bin/fish"
    ```


## <span class="section-num">4</span> Интеграция с разным программным обеспечением {#интеграция-с-разным-программным-обеспечением}


### <span class="section-num">4.1</span> Midnight Commander {#midnight-commander}


#### <span class="section-num">4.1.1</span> Выход в текущий каталог {#выход-в-текущий-каталог}

-   При выходе командная оболочка вернёт вас в тот каталог, в котором вы запустили Midnight Commander.
-   Если вы хотите, чтобы оставался текущий каталог, выбранный в Midnight Commander, можно использовать специальный скрипт-обёртку, который выполнит переход в текущий каталог после закрытия `mc`.
-   Используйте код <https://gist.github.com/halicki/58cedaf90f3e85277a799cef8217fc72>.
-   Поместите его в `~/.config/fish/functions/mc.fish`.
-   Можно также выполнить его в командной оболочке _fish_ и сохраните функцию:
    ```shell
    funcsave mc
    ```


## <span class="section-num">5</span> Настройка {#настройка}


### <span class="section-num">5.1</span> Общая информация {#общая-информация}

-   Файл настроек `~/.config/fish/config.fish` запускается при каждом входе.
-   Если переменная должна быть сохранена, её следует установить как универсальную, а не определять в вышеупомянутом файле настроек.
-   Пользовательские функции находятся в каталоге `~/.config/fish/functions/` в файлах `function_name.fish`.


### <span class="section-num">5.2</span> Веб-интерфейс {#веб-интерфейс}

-   Цвета терминала fish, строка приглашения, функции, переменные, история, привязки и сокращения могут быть настроены через интерактивный веб-интерфейс:
    ```shell
    fish_config
    ```


## <span class="section-num">6</span> Менеджеры плагинов {#менеджеры-плагинов}

-   [Fish. Полезные плагины]({{< relref "2025-02-14--fish-useful-plugins" >}})


### <span class="section-num">6.1</span> Oh My Fish {#oh-my-fish}

-   Фреймворк расширения Fish.
-   Репозиторий: <https://github.com/oh-my-fish/oh-my-fish>


### <span class="section-num">6.2</span> Fisher {#fisher}

-   [Fish. Менеджер плагинов Fisher]({{< relref "2025-02-14--fish-plugin-manager-fisher" >}})
-   Менеджер плагинов.
-   Репозиторий: <https://github.com/jorgebucaran/fisher>


### <span class="section-num">6.3</span> Fundle {#fundle}

-   Менеджер пакетов для Fish.
-   Репозиторий:  <https://github.com/danhper/fundle>


## <span class="section-num">7</span> Ресурсы {#ресурсы}

-   <https://github.com/jorgebucaran/awsm.fish>
