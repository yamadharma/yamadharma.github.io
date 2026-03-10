---
title: "Мультимедиа сервер PipeWire"
author: ["Dmitry S. Kulyabov"]
date: 2021-04-28T16:28:00+03:00
lastmod: 2025-08-28T16:37:00+03:00
tags: ["gentoo", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "pipewire-multimedia-server"
---

PipeWire есть новый аудио и видео сервер. В основном для Wayland. Должен заменить другие видео-серверы.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий проекта: <https://gitlab.freedesktop.org/pipewire/pipewire>
-   Wiki проекта: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/home>


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   Чтобы использовать PipeWire вместо PulseAudio для звукового сервера, включите USE-флаг `USE=sound-server` для `media-video/pipewire` и отключите USE-флаг `USE=daemon` для `media-sound/pulseaudio`.
-   Добавьте в файл `/etc/portage/package.use`:
    ```conf-unix
    media-video/pipewire sound-server
    media-sound/pulseaudio -daemon
    ```

-   Удалите `media-sound/pulseaudio-daemon`:
    ```shell
    emerge -Cv media-sound/pulseaudio-daemon
    emerge -Cv media-sound/paprefs
    ```

-   Установить само приложение:
    ```shell
    emerge media-video/pipewire
    emerge media-video/wireplumber
    ```


## <span class="section-num">3</span> Настройка пользовательской сессии {#настройка-пользовательской-сессии}


### <span class="section-num">3.1</span> Права пользователя {#права-пользователя}

-   Желательно добавить пользователя в группу `audio`:
    ```shell
    usermod -aG audio <user>
    ```


### <span class="section-num">3.2</span> Настройка запуска на уровне пользователя {#настройка-запуска-на-уровне-пользователя}

-   По умолчанию _PipeWire_ настроен на использование _systemd_.
-   Следует настроить его запуск для пользователя.
-   Флаг `--now` позволяет одновременно активировать и запускать сервис.
-   Отключите `pulseaudio`:
    ```shell
    systemctl --user disable --now pulseaudio.socket pulseaudio.service
    ```
-   Для каждого пользователя можно установить активацию по обращению к сокету:
    ```shell
    systemctl --user enable --now pipewire.socket pipewire-pulse.socket
    ```
-   В качестве альтернативы можно сразу запускать необходимый процесс:
    ```shell
    systemctl --user enable --now pipewire.service pipewire-pulse.service
    ```
-   Отключите демон сессии `pipewire-media-session.service` и запустите `wireplumber`:
    ```shell
    systemctl --user disable pipewire-media-session.service
    systemctl --user --force enable --now wireplumber.service
    ```


### <span class="section-num">3.3</span> Настройка запуска на уровне системы {#настройка-запуска-на-уровне-системы}

-   Под пользователем `root` можно настроить запуск сервисов на уровне системы, заменив `--user` на `--global`:
    ```shell
    systemctl --global enable pipewire.socket pipewire-pulse.socket
    systemctl --global --force enable wireplumber.service
    ```
-   При выборе этого варианта службы должны быть запущены вручную под пользователем пользователем.


## <span class="section-num">4</span> Использование с другими серверами {#использование-с-другими-серверами}


### <span class="section-num">4.1</span> Замена PulseAudio {#замена-pulseaudio}


#### <span class="section-num">4.1.1</span> PulseAudio с поддержкой запуска как демон {#pulseaudio-с-поддержкой-запуска-как-демон}

-   Ранее _PulseAudio_ собиралась только с поддержкой запуска как демон.
-   Если _PulseAudio_ настроено с поддержкой запуска как демона[^fn:1], то его необходимо отключить:
    -   запретить запуск `pulseaudio`;
    -   отключить запуск в файле конфигурации:
        -   отредактируйте файл `/etc/pulse/daemon.conf` и замените `daemonize` на `daemonize = no`.
-   Одновременно отключим _PulseAudio_ и включим _PipeWire_ для каждого пользователя:
    ```shell
    systemctl --user disable --now pulseaudio.socket pulseaudio.service
    systemctl --user enable --now pipewire.socket pipewire-pulse.socket wireplumber.service
    ```
-   Можно замаскировать PulseAudio (но он всё равно может стартовать автоматически):
    ```shell
    systemctl --user mask pulseaudio.socket pulseaudio.service
    ```
-   Кроме того, рекомендуется удалить файлы, оставшиеся от PulseAudio:
    ```shell
    rm -r ~/.config/pulse/
    ```


#### <span class="section-num">4.1.2</span> PulseAudio без поддержки запуска кок демон {#pulseaudio-без-поддержки-запуска-кок-демон}

-   Теперь _PulseAudio_ рекомендуется собирать без поддержки демона.
-   В этом случае всё работает сразу.
-   Напомним, что на уровне пользователя следует подключить `pipewire-pulse.socket`:
    ```shell
    systemctl --user disable --now pulseaudio.socket pulseaudio.service
    systemctl --user enable --now pipewire.socket pipewire-pulse.socket wireplumber.service
    ```


### <span class="section-num">4.2</span> Замена Jack {#замена-jack}

-   Для маршрутизации клиентов Jack через PipeWire в настоящее время
    предпочтительно запускать их через `pw-jack`, который использует
    `LD_PRELOAD` для использования библиотек PipeWire вместо Jack, например:
    ```shell
    pw-jack <application>
    ```

-   Можно задать собственный размер буфера, установив размер_буфера/частота_дискретизации:
    ```shell
    PIPEWIRE_LATENCY="128/48000" pw-jack <application>
    ```


## <span class="section-num">5</span> Проверка работы {#проверка-работы}

-   Для _PipeWire_ возможно посмотреть информацию по серверу `pipewire`:
    ```shell
    LANG=C pactl info | grep "Server Name"
    ```

    -   В результате должна присутствовать строчка типа такой:
        ```shell
        Server Name: PulseAudio (on PipeWire 0.3.56)
        ```


## <span class="section-num">6</span> Конфигурация {#конфигурация}


### <span class="section-num">6.1</span> Конфигурационные файлы {#конфигурационные-файлы}

-   Конфигурация, идущая в комплекте с дистрибутивом, находится в `/usr/share/pipewire`.
-   Для изменения параметров скопируйте файлы конфигурации в:
    -   `/etc/pipewire`: уровень системы;
    -   `~/.config/pipewire`: уровень пользователя.


### <span class="section-num">6.2</span> Профили устройств {#профили-устройств}

-   Профили устройств хранятся в каталоге `~/.local/state/pipewire/media-session.d/`.
-   При запуске в первый раз с подключёнными внешними устройствами (например, usb-устройствами), профили для них не создаются. Необходимо их переподключить в этом случае.


### <span class="section-num">6.3</span> Изменение частоты дискретизации {#изменение-частоты-дискретизации}

-   По умолчанию _PipeWire_ глобально устанавливает частоту дискретизации равную 48 КГц.
-   Для изменения нужно отредактировать строку `default.clock.rate = 48000` в файле конфигурации `/etc/pipewire/pipewire.conf` или `~/.config/pipewire/pipewire.conf`.
-   Например, если вы хотите частоту дискретизации в 192 КГц, раскомментируйте строку и поменяйте её на `default.clock.rate = 192000`.

[^fn:1]: В Gentoo это означает, что `pulseaudio` скомпилирован с флагом `daemon`.
