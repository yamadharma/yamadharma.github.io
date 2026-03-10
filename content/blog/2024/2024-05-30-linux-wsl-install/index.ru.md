---
title: "Установка Linux в WSL"
author: ["Dmitry S. Kulyabov"]
date: 2024-05-30T16:16:00+03:00
lastmod: 2025-05-02T21:48:00+03:00
tags: ["windows", "linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "linux-wsl-install"
---

Установка Linux в WSL.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


### <span class="section-num">1.1</span> Ссылки {#ссылки}


#### <span class="section-num">1.1.1</span> Документация {#документация}

-   <https://learn.microsoft.com/ru-ru/windows/wsl/>
-   <https://learn.microsoft.com/ru-ru/windows/wsl/install>
-   <https://learn.microsoft.com/ru-ru/windows/wsl/setup/environment>
-   <https://learn.microsoft.com/en-us/windows/wsl/systemd>
-   <https://learn.microsoft.com/en-us/windows/wsl/wsl-config>
-   <https://github.com/mikeroyal/WSL-Guide>


## <span class="section-num">2</span> Настройка {#настройка}

-   Для настройки среды WSL используется утилита _WSL Settings_.


## <span class="section-num">3</span> Основные команды {#основные-команды}

-   Список возможных дистрибутивов:
    ```shell
    wsl -l -o
    ```
-   Установка дистрибутива:
    ```shell
    wsl --install <дистрибутив>
    ```
-   Остановка WSL из консоли Windows:
    ```shell
    wsl.exe --shutdown
    ```
-   Остановка исполнения сеанта Linux:
    ```shell
    systemctl halt
    ```


## <span class="section-num">4</span> Установка {#установка}


### <span class="section-num">4.1</span> WSL {#wsl}

-   Установите wsl:
    ```shell
    wsl --install
    ```
-   Включает дополнительные компоненты WSL и платформы виртуальных машин.
-   Скачивает и устанавливает последнюю версию ядра Linux.
-   Задаёт WSL 2 в качестве среды по умолчанию.
-   Во время установки потребуется перезапустить компьютер.
-   Если WSL уже установлен, его можно обновить:
    ```shell
    wsl --update
    ```


### <span class="section-num">4.2</span> Ubuntu {#ubuntu}

-   Установите Ubuntu:
    ```shell
    wsl --install Ubuntu
    ```
-   Скачивает и устанавливает дистрибутив Ubuntu Linux.
-   Во время установки потребуется перезапустить компьютер.


### <span class="section-num">4.3</span> Fedora {#fedora}

-   Репозиторий: <https://github.com/VSWSL/Fedora-WSL>
-   Misrosoft Store: <https://www.microsoft.com/store/apps/9NPCP8DRCHSN>
-   Можно установить из Misrosoft Store.
-   Установите Fedora:
    ```shell
    wsl --install FedoraLinux-42
    ```
-   Скачивает и устанавливает дистрибутив Fedora Linux.
-   Запуск дистрибутива:
    ```shell
    wsl.exe -d FedoraLinux-42
    ```


### <span class="section-num">4.4</span> Arch {#arch}

-   Репозиторий: <https://github.com/VSWSL/Arch-WSL>
-   Misrosoft Store: <https://www.microsoft.com/store/apps/9MZNMNKSM73X>
-   Можно установить из Misrosoft Store.
-   Установите Arch Linux:
    ```shell
    wsl --install archlinux
    ```
-   Скачивает и устанавливает дистрибутив Arch Linux.
-   Во время установки потребуется перезапустить компьютер.


## <span class="section-num">5</span> Первичная настройка {#первичная-настройка}


### <span class="section-num">5.1</span> Учётные данные {#учётные-данные}

-   При первом запуске дистрибутива будет предложено создать имя пользователя и пароль для дистрибутива Linux.
-   Для каждого дистрибутива Linux используются свои имя пользователя и пароль, и они не связаны с именем пользователя Windows.


### <span class="section-num">5.2</span> Поддержка systemd {#поддержка-systemd}

-   Сейчас поддержка systemd устанавливается по умолчанию и настройки не требует.
-   Убедитесь, что версия WSL: 0.67.6 или более поздняя:
    ```shell
    wsl --version
    ```
-   В консоли Linux перейдите под суперпользователя:
    ```shell
    sudo -i
    ```
-   Откройте для редактирования файл `/etc/wsl.conf`:
    ```shell
    vi /etc/wsl.conf
    ```
-   Активируйте systemd:
    ```toml
    [boot]
    systemd=true
    ```
-   Из консоли Windows остановите выполнение WSL:
    ```shell
    wsl.exe --shutdown
    ```
-   После повторного запуска WSL проверьте работу systemd:
    ```shell
    systemctl list-unit-files --type=service
    ```


### <span class="section-num">5.3</span> Установка базового программного обеспечения {#установка-базового-программного-обеспечения}

-   В консоли Linux перейдите под суперпользователя:
    ```shell
    sudo -i
    ```


#### <span class="section-num">5.3.1</span> Fedora {#fedora}

-   Обновите систему:
    ```shell
    sudo dnf -y update
    ```
-   Установка системных библиотек:
    ```shell
    sudo dnf -y install vulkan
    ```
-   Библиотеки Wayland:
    ```shell
    sudo dnf -y install libwayland-cursor libwayland-egl libwayland-server
    sudo dnf -y install egl-wayland
    ```
-   Установите средства Wayland:
    ```shell
    sudo dnf -y install wl-clipboard
    ```
-   Устанавливаем утилиту для удобства работы _tmux_ (см. [Терминальный мультиплексор tmux]({{< relref "2024-02-19-terminal-multiplexer-tmux" >}})):
    ```shell
    sudo dnf -y install tmux
    ```
-   Устанавливаем утилиту для удобства работы _mc_:
    ```shell
    sudo dnf -y install mc
    ```
-   Автодополнение для bash:
    ```shell
    sudo dnf -y install bash-completion
    ```
-   Установите git и gh (см. [github: утилиты командной строки]({{< relref "2021-08-04-github-command-line-utilities" >}})):
    ```shell
    sudo dnf -y install git gh
    ```
-   Просмотр pdf:
    ```shell
    sudo dnf -y install evince
    ```
-   Терминал kitty:
    ```shell
    sudo dnf -y install kitty
    ```
-   Установите libreoffice:
    ```shell
    sudo dnf -y install libreoffice
    ```


#### <span class="section-num">5.3.2</span> Arch {#arch}

-   Используется пакетный менеджер _pacman_ (<https://wiki.archlinux.org/title/Pacman_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)>).
-   Обновите систему:
    ```shell
    pacman -Suy
    ```
-   Устанавливаем утилиту для удобства работы _tmux_:
    ```shell
    pacman -S tmux
    ```
-   Устанавливаем утилиту для удобства работы _mc_:
    ```shell
    pacman -S mc
    ```
-   Автодополнение для bash:
    ```shell
    pacman -S bash-completion
    ```
-   Просмотр pdf:
    ```shell
    pacman -S evince
    ```
-   Терминал kitty:
    ```shell
    pacman -S kitty
    ```
-   Установите libreoffice:
    ```shell
    pacman -S libreoffice-fresh
    ```


## <span class="section-num">6</span> Emacs {#emacs}


### <span class="section-num">6.1</span> Fedora {#fedora}

-   Установите emacs:
    ```shell
    dnf -y install emacs
    ```


### <span class="section-num">6.2</span> Arch {#arch}

-   Установите emacs:
    ```shell
    pacman -S emacs
    ```
