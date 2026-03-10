---
title: "Тайловые оконные менеджеры"
author: ["Dmitry S. Kulyabov"]
date: 2023-06-19T09:37:00+03:00
lastmod: 2025-04-26T20:40:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "tiling-window-manager"
---

Тайловые оконные менеджеры.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Фреймовый (мозаичный, плиточный, тайловый) оконный менеджер --- это менеджер окон, разбивающий рабочее пространство экрана на взаимно не пересекающиеся прямоугольные области --- фреймы.
-   Каждый фрейм используется для вывода информации отдельным приложением, в противоположность традиционным менеджерам окон, которые создают области покоординатно и послойно («окна»), пытаясь следовать метафоре «рабочего стола».
-   Особенности:
    -   полное использование всего видимого пространства;
    -   минимизация использования мыши в операциях с окнами.


## <span class="section-num">2</span> X Window System {#x-window-system}

-   В системе X Window оконный менеджер представляет собой отдельную программу.


### <span class="section-num">2.1</span> Awesome {#awesome}

-   Сайт: <https://awesomewm.org/>
-   Репозиторий: <https://github.com/awesomeWM/awesome>
-   Основан на dwm.
-   Мозаичное расположение окон, плавающие элементы, теги.
-   Написан на C.
-   Конфигурация на Lua.
-   Хорошо задокументирован.
-   Нормально обращается с мышью.


### <span class="section-num">2.2</span> Bspwm {#bspwm}

-   Репозиторий: <https://github.com/baskerville/bspwm>
-   Представляет окна как листья полного бинарного дерева.
-   Не обрабатывает привязки клавиш сам по себе, требуя использование другой программы.
-   Настройка горячих клавиш производится с помощью отдельной программы sxhkd.
-   Конфигурация может быть написана на любом скриптовом языке.


### <span class="section-num">2.3</span> Dwm {#dwm}

-   Сайт: <http://dwm.suckless.org/>
-   По умолчанию используется схема «основная область + область стека».
-   Другие стандартные макеты представляют собой режим «монокля» с одним окном и плавающий макет без мозаики.


### <span class="section-num">2.4</span> Herbstluftwm {#herbstluftwm}

-   Сайт: <https://herbstluftwm.org/>
-   Использует концепцию независимых от монитора тегов в качестве рабочих пространств.
-   Одновременно можно просмотреть ровно один тег.
-   Настраивается во время выполнения с помощью вызовов IPC из herbstclient.


### <span class="section-num">2.5</span> i3 {#i3}

-   [Window manager i3]({{< relref "2021-05-14-window-manager-i3" >}})
-   Репозиторий: <https://github.com/i3/i3>
-   Основан на wmii.
-   Рассматривает дополнительные мониторы как дополнительные рабочие области.
-   Позволяет вертикальное и горизонтальное разделение, макеты с вкладками и стопкой, а также родительские контейнеры.
-   Можно управлять полностью с клавиатуры, но можно использовать и мышь.
-   Правила расположения окон можно настроить очень гибко.
-   Хорошая документация.


### <span class="section-num">2.6</span> Ion {#ion}

-   Сайт: <https://tuomov.iki.fi/software/ion/>
-   Каждый фрейм может содержать одно или несколько окон.
-   Только одно из этих окон видно и заполняет весь кадр.
-   Не развивается.


### <span class="section-num">2.7</span> Larswm {#larswm}

-   Сайт: <http://porneia.free.fr/larswm/larswm.html>
-   Динамический тайлинг.
-   Дисплей разделён по вертикали на две области.
-   Левая область заполнена одним окном, правая содержит все остальные окна, расположенные друг над другом.
-   Не развивается.


### <span class="section-num">2.8</span> LeftWM {#leftwm}

-   Репозиторий: <https://github.com/leftwm/leftwm>


### <span class="section-num">2.9</span> Qtile {#qtile}

-   Сайт: <http://qtile.org/>
-   Написан на Python.


### <span class="section-num">2.10</span> Ratpoison {#ratpoison}

-   Сайт: <https://www.nongnu.org/ratpoison/>


### <span class="section-num">2.11</span> Spectrwm {#spectrwm}

-   Репозиторий: <https://github.com/conformal/spectrwm>


### <span class="section-num">2.12</span> StumpWM {#stumpwm}

-   Репозиторий: <https://github.com/stumpwm/stumpwm>
-   Ответвление ratpoison.
-   Управляется клавиатурой, поддерживает несколько дисплеев (например, xrandr).
-   Язык настройки --- Common Lisp.
-   По умолчанию использует совместимые с Emacs сочетания клавиш.


### <span class="section-num">2.13</span> Wmii {#wmii}

-   Мозаичное и групповое управление окнами с помощью клавиатуры и мыши.
-   Идеология тегов.
-   Конфигурация по умолчанию использует сочетания клавиш, заимствованные из текстового редактора vi.
-   Настройка через виртуальную файловую систему с использованием протокола файловой системы 9P.


### <span class="section-num">2.14</span> Xmonad {#xmonad}

-   Сайт: <https://xmonad.org/>
-   Репозиторий: <https://github.com/xmonad/xmonad>
-   Расширяемый WM, написанный на Haskell.
-   Ориентируется на dwm.


## <span class="section-num">3</span> Wayland {#wayland}


### <span class="section-num">3.1</span> Hyprland {#hyprland}

-   Сайт: <https://hyprland.org/>
-   Репозиторий: <https://github.com/hyprwm/Hyprland>
-   Динамический мозаичный компоновщик.


### <span class="section-num">3.2</span> Sway {#sway}

-   [Переход на Sway]({{< relref "2020-09-10-migration-sway" >}})
-   Репозиторий: <https://github.com/swaywm/sway>
-   Замена оконного менеджера i3 для Wayland.
-   Использует конфигурацию i3.


### <span class="section-num">3.3</span> River {#river}

-   Репозиторий: <https://github.com/riverwm/river>
-   Динамический тайлинговый менеджер Wayland.


### <span class="section-num">3.4</span> CageBreak {#cagebreak}

-   Репозиторий: <https://github.com/project-repo/cagebreak>
-   Основан на Cage и Ratpoison.


### <span class="section-num">3.5</span> dwl {#dwl}

-   Репозиторий: <https://github.com/djpohly/dwl>
-   Вдохновлён dwm.
-   Не имеет никакого другого интерфейса настройки, кроме редактирования исходного кода.


## <span class="section-num">4</span> Тайловые оконные менеджеры для Windows {#тайловые-оконные-менеджеры-для-windows}


### <span class="section-num">4.1</span> GlazeWM {#glazewm}

-   Вдохновлён i3 (см. [Window manager i3]({{< relref "2021-05-14-window-manager-i3" >}})) для Windows и Polybar.
-   Репозиторий: <https://github.com/glazerdesktop/GlazeWM>
-   Конфигурация в _yaml_.
-   Установка:
    -   Winget
        ```shell
        winget install GlazeWM
        ```
    -   Cocolatey:
        ```shell
        choco install glazewm
        ```
-   Устанавливается в `%LOCALAPPDATA%\Microsoft\Winget\Packages\` по умолчанию.


### <span class="section-num">4.2</span> b3 {#b3}

-   Вариант i3 (см. [Window manager i3]({{< relref "2021-05-14-window-manager-i3" >}})) для Windows.
-   Репозиторий: <https://github.com/ritschmaster/b3>


### <span class="section-num">4.3</span> komorebi {#komorebi}

-   Репозиторий: <https://github.com/LGUG2Z/komorebi>


### <span class="section-num">4.4</span> bug.n {#bug-dot-n}

-   Репозиторий: <https://github.com/fuhsjr00/bug.n>
-   Создан как скрипт AutoHotKey.


### <span class="section-num">4.5</span> MaxTo {#maxto}

-   Сайт: <https://maxto.net/>
-   Триальная версия


### <span class="section-num">4.6</span> Stack {#stack}

-   Сайт: <https://losttech.software/stack.html>


### <span class="section-num">4.7</span> Plumb {#plumb}

-   Сайт: <http://palatialsoftware.com/>


### <span class="section-num">4.8</span> workspacer {#workspacer}

-   Сайт: <https://workspacer.org/>
-   Репозиторий: <https://github.com/workspacer/workspacer>
-   Установка
    -   Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
        ```shell
        choco install workspacer
        ```


### <span class="section-num">4.9</span> dwm-win32 {#dwm-win32}

-   Сайт: <https://www.brain-dump.org/projects/dwm-win32/>
-   Порт dwm на Windows.
-   Не развивается (2009).
