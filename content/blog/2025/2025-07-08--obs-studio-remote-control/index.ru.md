---
title: "OBS Studio. Удалённое управление"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-08T20:16:00+03:00
lastmod: 2026-01-07T13:55:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "obs-studio-remote-control"
---

OBS Studio. Удалённое управление.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Прагматика {#прагматика}

-   Под Wayland невозможно задать для приложения глобальные сочетания клавиш.
-   Приходится использовать утилиты удалённого управления.


## <span class="section-num">2</span> obs-control {#obs-control}

-   Репозиторий: <https://github.com/hirak99/obs-control>


## <span class="section-num">3</span> obs-cli {#obs-cli}

-   Репозиторий: <https://github.com/muesli/obs-cli>
-   Использует Websocket.
-   Но не работает с текущей версией websocket5 из поставки OBS studio.


## <span class="section-num">4</span> obs-cmd {#obs-cmd}

-   Репозиторий: <https://github.com/grigio/obs-cmd>
-   Использует obs-websocket v5.
-   Для работы следует настроить Websocket в интерфейсе OBS studio.


### <span class="section-num">4.1</span> Список команд {#список-команд}

-   `obs-cmd --help`


#### <span class="section-num">4.1.1</span> Сцены {#сцены}

-   `obs-cmd scene switch <scene>`
-   `obs-cmd scene switch @cam-front`
-   `obs-cmd scene-collection switch <collection>`
-   `obs-cmd scene-item toggle <scene> <item>`


#### <span class="section-num">4.1.2</span> Запись {#запись}

-   `obs-cmd recording start`
-   `obs-cmd recording stop`
-   `obs-cmd recording toggle`
-   `obs-cmd recording pause`
-   `obs-cmd recording resume`
-   `obs-cmd recording toggle-pause`
-   `obs-cmd recording status`
-   `obs-cmd recording status-active`


#### <span class="section-num">4.1.3</span> Разное {#разное}

-   `obs-cmd toggle-mute Mic/Aux`
-   `obs-cmd streaming start`
-   `obs-cmd virtualcam start`
-   `obs-cmd save-screenshot <source> <format> <file_path> [--width WIDTH] [--height HEIGHT] [--compression-quality COMPRESSION_QUALITY]`
-   `obs-cmd replay toggle`
-   `obs-cmd replay save`
-   `obs-cmd replay status`
-   `obs-cmd replay last-replay`
-   `obs-cmd trigger-hotkey`
-   `obs-cmd fullscreen-projector [--monitor-index INDEX]`
-   `obs-cmd source-projector <source-name> [--monitor-index INDEX]`
-   `obs-cmd info`
-   ``obs-cmd --websocket obsws://localhost:4455/secret info # You can override the default `obsws` url``
-   `OBS_WEBSOCKET_URL=obsws://localhost:4455/secret obs-cmd info`


### <span class="section-num">4.2</span> Аутентификация {#аутентификация}

-   Пароль задаётся в строке подключения.
-   Строку подключения можно задать или в командной строке, или в переменной среды `OBS_WEBSOCKET_URL`.
-   Например, `OBS_WEBSOCKET_URL=obsws://localhost:4455/secret`.
-   Зашитый в код пароль: `secret`.
-   Можно, при желании, отключить аутентификацию в Websocket в OBS studio.


### <span class="section-num">4.3</span> Установка {#установка}


#### <span class="section-num">4.3.1</span> Gentoo {#gentoo}

-   Репозиторий karma (см. [Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
    ```shell
    emerge obs-cmd
    ```
