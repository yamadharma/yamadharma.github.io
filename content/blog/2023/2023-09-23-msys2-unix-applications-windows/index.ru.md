---
title: "MSYS2. Приложения Unix под Windows"
author: ["Dmitry S. Kulyabov"]
date: 2023-09-23T15:55:00+03:00
lastmod: 2025-04-17T12:57:00+03:00
tags: ["sysadmin", "windows"]
categories: ["computer-science"]
draft: false
slug: "msys2-unix-applications-windows"
---

MSYS2. Приложения Unix под Windows

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.msys2.org/>
-   Набор инструментов и библиотек, предоставляющий unix-среду для создания, установки и запуска собственного программного обеспечения на Windows.
-   Частично использует Cygwin.
    -   Подобно Cygwin делается замена путей в стиле UNIX, маскируется расширение `.exe`, поддерживаются псевдотерминалы, UNIX-сигналы.
-   Содержит:
    -   терминал командной строки mintty;
    -   bash;
    -   системы контроля версий (git, subversion);
    -   базовые инструменты (tar, awk);
    -   пакетный менеджер `packman` (из Arch Linux).
-   Дополнительное программное обеспечение используется из проекта Mingw-w64 (см. [MinGW-w64. Приложения Unix под Windows]({{< relref "2023-09-22-mingw-w64-unix-applications-windows" >}})).


## <span class="section-num">2</span> Установка {#установка}

-   Установка с помощью Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
    ```shell
    choco install msys2 -y
    ```
-   Далее, возможно, придётся перелогиниться или перегрузиться.
-   Запустите `msys2` (через ярлык или через поиск).
-   Возможно будет необходимо обновить основные системные пакеты MSYS2 и базу данных с информацией об доступных пакетах:
    ```shell
    pacman -Syu
    ```
-   Также может потребоваться обновить другие установленные пакеты:
    ```shell
    pacman -Su
    ```


## <span class="section-num">3</span> Настройка {#настройка}


### <span class="section-num">3.1</span> Команды запуска {#команды-запуска}

-   По умолчанию создаются несколько команд запуска.
-   Все они запускают команду `msys2_shell.cmd` с разными параметрами.
-   Этот пакетный фал запускает необходимое окружение в параметрами, заданными в соответствующем `.ini`-файле.
-   Например, ярлык `MSYS2 MinGW x64` содержит в себе следующую командную строку запуска:
    ```shell
    C:\tools\msys64\msys2_shell.cmd -mingw64
    ```
-   Будем использовать окружение `mingw64`.


### <span class="section-num">3.2</span> Автозапуск команд при старте MSYS {#автозапуск-команд-при-старте-msys}

-   Автоматически запускемые команды можно прописать двумя способами:
    -   если их добавить в конец файла `.bash_profile`, который находится в домашнем каталоге пользователя (домашние каталоги пользователей хранятся в каталогах папки `c:\tools\msys64\home\`);
    -   если их добавить в конец файла `c:\tools\msys64\etc\profile`.


### <span class="section-num">3.3</span> Переменная окружения PATH {#переменная-окружения-path}


#### <span class="section-num">3.3.1</span> Изменение переменной PATH {#изменение-переменной-path}

-   `PATH` можно поменять командой `export`.
-   Самый простой способ добавить что-либо в конец `PATH` (на примере добавления каталога `c:\opt\Нужные программы`):
    ```shell
    export PATH=$PATH:'/c/opt/Нужные программы'
    ```
-   Следует обратить внимание на нотацию Cygwin:
    -   в команде перед именем диска `C:` стоит прямой слеш;
    -   после имени диска нет двоеточия;
    -   в качестве разделителя для элементов пути (директорий) используются прямые слеши;
    -   если имена файлов и папок содержат пробелы, то весь путь обрамляется кавычками `'`;
    -   завершающий прямой слеш в пути отсутствует.


#### <span class="section-num">3.3.2</span> Импорт $PATH из переменной %Path% Windows {#импорт-path-из-переменной-path-windows}

-   Можно в ini-файле `msys2.ini` раскомментировать строчку с переменной `MSYS2_PATH_TYPE`, в результате чего в $PATH будут наследоваться значения из системной переменной окружения %Path% Windows:
    ```shell
    set MSYS2_PATH_TYPE=inherit
    ```
-   То же самое нужно сделать для ini-файла запускаемого профиля, например, отредактировать файл `mingw64.ini`.


## <span class="section-num">4</span> Дополнительные пакеты {#дополнительные-пакеты}


### <span class="section-num">4.1</span> Средства разработки {#средства-разработки}


#### <span class="section-num">4.1.1</span> Базовые средства разработки {#базовые-средства-разработки}

-   Средства разработки содержит группа `mingw-w64-x86_64-toolchain`:
    ```shell
    pacman -S mingw-w64-x86_64-toolchain
    ```

    -   Будут предложены для установки несколько пакетов.
    -   Можно установить все сразу, или избранные.


#### <span class="section-num">4.1.2</span> git {#git}

-   Установка git:
    ```shell
    pacman -S git
    ```


### <span class="section-num">4.2</span> Терминалы {#терминалы}


#### <span class="section-num">4.2.1</span> Mintty {#mintty}

-   Сайт: <https://mintty.github.io/>
-   `Mintty` является терминальным приложением по умолчанию в MSYS2 и включено в установщик.


#### <span class="section-num">4.2.2</span> Konsole {#konsole}

-   Сайт: <https://konsole.kde.org/>.
-   Установите терминал _Konsole_:
    ```shell
    pacman -S mingw-w64-x86_64-konsole
    ```
-   По умолчанию `konsole` запускает powershell.
-   Заменим оболочку на mingw64.
-   В строке меню окна Konsole выберите _Настройки_ &gt; _Создать новый профиль_.
-   Выберите его в качестве профиля по умолчанию, чтобы всегда открывать среду _msys2_ при запуске.
-   Добавьте имя профиля и следующую команду:
    ```shell
    C:\tools\msys64\msys2_shell.cmd -defterm -here -no-start -mingw64
    ```
-   Закройте и перезапустите Konsole.


### <span class="section-num">4.3</span> Файловые менеджеры {#файловые-менеджеры}


#### <span class="section-num">4.3.1</span> Midnight commander {#midnight-commander}

-   Установите Midnight commander:
    ```shell
    pacman -S mc
    ```


### <span class="section-num">4.4</span> Просмотр Pdf {#просмотр-pdf}


#### <span class="section-num">4.4.1</span> Evince {#evince}

-   Установите _Evince_:
    ```shell
    pacman -S mingw-w64-x86_64-evince
    ```


#### <span class="section-num">4.4.2</span> Okular {#okular}

-   Установим okular:
    ```shell
    pacman -S mingw-w64-x86_64-okular
    ```


### <span class="section-num">4.5</span> Шрифты {#шрифты}


#### <span class="section-num">4.5.1</span> Iosevka {#iosevka}

-   Шрифты Iosevka с патчами от nerd-fonts:
    ```shell
    pacman -S mingw-w64-x86_64-ttf-iosevka-nerd mingw-w64-x86_64-ttf-iosevkaterm-nerd
    ```
-   Подключить эти шрифты к оформлению Konsole у меня не получилось, поэтому я установил шрифты через Chocolatey:
    ```shell
    choco install nerd-fonts-iosevka nerd-fonts-iosevkaterm -y
    ```


### <span class="section-num">4.6</span> Редакторы {#редакторы}


#### <span class="section-num">4.6.1</span> Neovim {#neovim}

-   Установим _neovim_:
    ```shell
    pacman -S mingw-w64-x86_64-neovim
    ```
-   Также можно установить его графический вариант:
    ```shell
    pacman -S mingw-w64-x86_64-neovim-qt
    ```


### <span class="section-num">4.7</span> Утилиты для удобства {#утилиты-для-удобства}


#### <span class="section-num">4.7.1</span> tmux {#tmux}

-   Установим tmux:
    ```shell
    pacman -S tmux
    ```
