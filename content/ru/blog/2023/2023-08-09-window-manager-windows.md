---
title: "Window manager для Windows"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-09T22:09:00+03:00
lastmod: 2023-11-29T13:10:00+03:00
tags: ["windows", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "window-manager-windows"
---

Альтернативные window manager для Windows.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> BlackBox {#blackbox}

-   Базирующиеся на Black Box.


### <span class="section-num">1.1</span> xoblite {#xoblite}

-   Сайт: <https://xoblite.net/>
-   Репозиторий: <https://github.com/xoblite>


## <span class="section-num">2</span> Тайловые оконные менеджеры для Windows {#тайловые-оконные-менеджеры-для-windows}


### <span class="section-num">2.1</span> b3 {#b3}

-   Вариант i3 (см. [Window manager i3]({{< relref "2021-05-14-window-manager-i3" >}})) для Windows.
-   Репозиторий: <https://github.com/ritschmaster/b3>


### <span class="section-num">2.2</span> komorebi {#komorebi}

-   Репозиторий: <https://github.com/LGUG2Z/komorebi>


### <span class="section-num">2.3</span> GlazeWM {#glazewm}

-   Вдохновлён i3 (см. [Window manager i3]({{< relref "2021-05-14-window-manager-i3" >}})) для Windows и Polybar.
-   Репозиторий: <https://github.com/glazerdesktop/GlazeWM>
-   Конфигурация в _yaml_.
-   Установка:
    -   Winget
        ```shell
        winget install GlazeWM
        ```
-   Устанавливается в `%LOCALAPPDATA%\Microsoft\Winget\Packages\` по умолчанию.


### <span class="section-num">2.4</span> bug.n {#bug-dot-n}

-   Репозиторий: <https://github.com/fuhsjr00/bug.n>
-   Создан как скрипт AutoHotKey.


### <span class="section-num">2.5</span> MaxTo {#maxto}

-   Сайт: <https://maxto.net/>
-   Триальная версия


### <span class="section-num">2.6</span> Stack {#stack}

-   Сайт: <https://losttech.software/stack.html>


### <span class="section-num">2.7</span> Plumb {#plumb}

-   Сайт: <http://palatialsoftware.com/>


### <span class="section-num">2.8</span> workspacer {#workspacer}

-   Сайт: <https://workspacer.org/>
-   Репозиторий: <https://github.com/workspacer/workspacer>
-   Установка
    -   Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
        ```shell
        choco install workspacer
        ```


### <span class="section-num">2.9</span> dwm-win32 {#dwm-win32}

-   Сайт: <https://www.brain-dump.org/projects/dwm-win32/>
-   Порт dwm на Windows.
-   Не развивается (2009).
