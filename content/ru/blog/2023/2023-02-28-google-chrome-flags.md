---
title: "Флаги запуска Google Chrome"
author: ["Dmitry S. Kulyabov"]
date: 2023-02-28T15:31:00+03:00
lastmod: 2024-04-23T17:31:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "google-chrome-flags"
---

Флаги запуска Google Chrome и его деривативов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Флаги запуска {#флаги-запуска}


### <span class="section-num">1.1</span> Принудительное ускорение графического процессора {#принудительное-ускорение-графического-процессора}

-   Отключаем чёрный список графических процессов:
    ```shell
    --ignore-gpu-blocklist
    --enable-zero-copy
    ```


### <span class="section-num">1.2</span> Поддержка Wayland {#поддержка-wayland}

-   Включаем автовыбор графической системы:
    ```shell
    --ozone-platform-hint=auto
    ```
-   Если это не работает, можно явно указать желательную систему:
    ```shell
    --ozone-platform=wayland
    ```
-   Принудительно установить более новую версию GTK:
    ```shell
    --gtk-version=4
    ```


## <span class="section-num">2</span> Google Chrome {#google-chrome}


### <span class="section-num">2.1</span> Приложение по умолчанию {#приложение-по-умолчанию}

-   Установить броузер как броузер по умолчанию можно либо через графические настройки, либо через командную строку (см. [XDG. Приложения MIME]({{< relref "2023-04-02-xdg-mime-applications" >}}))
    ```shell
    xdg-settings set default-web-browser google-chrome.desktop
    ```


### <span class="section-num">2.2</span> Задание флагов в конфигурационном файле {#задание-флагов-в-конфигурационном-файле}


#### <span class="section-num">2.2.1</span> Расположение конфигурационных файлов {#расположение-конфигурационных-файлов}

-   Конфигурационный файл будет называться `chrome-flags.conf`.
-   Пользовательский файл конфигурации находится в каталоге `$HOME/.config/` (переменная среды `$XDG_CONFIG_HOME`).
-   Глобальный файл конфигурации находится в каталоге `/etc/`.
-   Специальный синтаксис не используется. Флаги определяются так, как если бы они были записаны в терминале.
-   Флаги можно размещать в отдельных строках для удобства чтения, но это не обязательно.
-   Строки, начинающиеся с символа решётки (`#`), пропускаются.


#### <span class="section-num">2.2.2</span> Пример конфигурационного файла {#пример-конфигурационного-файла}

-   Настроим перенос кэша броузера во временную файловую систему:
    ```conf-unix
    ## ~/.config/chrome-flags.conf
    # Cache in tmpfs
    --disk-cache-dir=$XDG_RUNTIME_DIR/google-chrome
    ```
-   Настроим конфигурацию параметров графики:
    ```conf-unix
    ## ~/.config/chrome-flags.conf
    --ignore-gpu-blocklist
    --enable-gpu-rasterization
    --enable-zero-copy
    --ozone-platform-hint=auto
    --enable-features=WaylandWindowDecorations
    --enable-webrtc-pipewire-capturer
    --gtk-version=4
    ```


#### <span class="section-num">2.2.3</span> Модификация файла запуска Google Chrome {#модификация-файла-запуска-google-chrome}

-   Добавим в файл запуска чтение файла конфигурации:
    ```shell
    XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

    # Allow users to override command-line options
    if [[ -f $XDG_CONFIG_HOME/chrome-flags.conf ]]
    then
       CHROME_USER_FLAGS="$(cat $XDG_CONFIG_HOME/chrome-flags.conf | grep -v "#" | xargs)"
       CHROME_USER_FLAGS=$(eval echo $CHROME_USER_FLAGS)
    elif [[ -f /etc/chrome-flags.conf ]]
    then
       CHROME_USER_FLAGS="$(cat /etc/chrome-flags.conf | grep -v "#" | xargs)"
       CHROME_USER_FLAGS=$(eval echo $CHROME_USER_FLAGS)
    fi
    ```
-   Соответственно заменим и строку запуска:
    ```shell
    # Launch
    # Note: exec -a below is a bashism.
    exec -a "$0" "$HERE/chrome" $CHROME_USER_FLAGS "$@"
    ```


## <span class="section-num">3</span> Yandex Browser {#yandex-browser}


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   Сайт: <https://browser.yandex.com/>
-   Репозиторий deb-файлов: <https://repo.yandex.ru/yandex-browser/deb/pool/main/y/>


### <span class="section-num">3.2</span> Приложение по умолчанию {#приложение-по-умолчанию}

-   Установить броузер как броузер по умолчанию можно либо через графические настройки, либо через командную строку (см. [XDG. Приложения MIME]({{< relref "2023-04-02-xdg-mime-applications" >}}))
    ```shell
    xdg-settings set default-web-browser yandex-browser.desktop
    ```


### <span class="section-num">3.3</span> Задание флагов в конфигурационном файле {#задание-флагов-в-конфигурационном-файле}


#### <span class="section-num">3.3.1</span> Расположение конфигурационных файлов {#расположение-конфигурационных-файлов}

-   Конфигурационный файл будет называться `yandex-browser-flags.conf`.
-   Пользовательский файл конфигурации находится в каталоге `$HOME/.config/` (переменная среды `$XDG_CONFIG_HOME`).
-   Глобальный файл конфигурации находится в каталоге `/etc/`.
-   Специальный синтаксис не используется. Флаги определяются так, как если бы они были записаны в терминале.
-   Флаги можно размещать в отдельных строках для удобства чтения, но это не обязательно.
-   Строки, начинающиеся с символа решётки (`#`), пропускаются.


#### <span class="section-num">3.3.2</span> Пример конфигурационного файла {#пример-конфигурационного-файла}

-   Настроим перенос кэша броузера во временную файловую систему:
    ```conf-unix
    ## ~/.config/yandex-browser-flags.conf
    # Cache in tmpfs
    --disk-cache-dir=$XDG_RUNTIME_DIR/yandex-browser
    ```
-   Настроим конфигурацию параметров графики:
    ```conf-unix
    ## ~/.config/yandex-browser-flags.conf
    --ignore-gpu-blocklist
    --enable-gpu-rasterization
    --enable-zero-copy
    --ozone-platform-hint=auto
    --enable-features=WaylandWindowDecorations
    --enable-webrtc-pipewire-capturer
    --gtk-version=4
    ```


#### <span class="section-num">3.3.3</span> Модификация файла запуска Yandex Browser {#модификация-файла-запуска-yandex-browser}

-   Добавим в файл запуска чтение файла конфигурации:
    ```shell
    XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

    # Allow users to override command-line options
    if [[ -f $XDG_CONFIG_HOME/yandex-browser-flags.conf ]]
    then
       CHROME_USER_FLAGS="$(cat $XDG_CONFIG_HOME/yandex-browser-flags.conf | grep -v "#" | xargs)"
       CHROME_USER_FLAGS=$(eval echo $CHROME_USER_FLAGS)
    elif [[ -f /etc/yandex-browser-flags.conf ]]
    then
       CHROME_USER_FLAGS="$(cat /etc/yandex-browser-flags.conf | grep -v "#" | xargs)"
       CHROME_USER_FLAGS=$(eval echo $CHROME_USER_FLAGS)
    fi
    ```
-   Соответственно заменим и строку запуска:
    ```shell
    if [ "${LD_LIBRARY_PATH+set}" = "set" ] ; then
            export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/lib64/yandex-browser-stable/lib"
    else
            export LD_LIBRARY_PATH="/usr/lib64/yandex-browser-stable/lib"
    fi
    export LD_LIBRARY_PATH

    ## Launch
    cd "/opt/yandex/browser" &&
    exec -a "$0" "./yandex-browser" $CHROME_USER_FLAGS "$@"
    ```


## <span class="section-num">4</span> Cromium {#cromium}


### <span class="section-num">4.1</span> Общая информация {#общая-информация}

-   Веб-браузер с открытым исходным кодом.
-   Разрабатывается сообществом The Chromium Authors, компанией Google и некоторыми другими компаниями (Opera Software, Яндекс, NVIDIA, Microsoft и другими).


### <span class="section-num">4.2</span> Приложение по умолчанию {#приложение-по-умолчанию}

-   Установить броузер как броузер по умолчанию можно либо через графические настройки, либо через командную строку (см. [XDG. Приложения MIME]({{< relref "2023-04-02-xdg-mime-applications" >}}))
    ```shell
    xdg-settings set default-web-browser chromium-browser-chromium.desktop
    ```


### <span class="section-num">4.3</span> Синхронизация настроек {#синхронизация-настроек}

-   С 15 марта 2021 года Google ограничивает доступ к своему API сторонним броузерам на базе Chromium.
-   Это блокирует доступ Chromium-браузеров к базе учётных записей Google.
-   Запуск Chromium с флагами, устанавливающими идентификатор oauth2 и секретное значение, может повторно включить синхронизацию Chromium с учетной записью Google (задав флаги запуска):
    ```conf-unix
    --oauth2-client-id=77185425430.apps.googleusercontent.com
    --oauth2-client-secret=OTJgUOQcT7lO7GsGZq2G4IlT
    ```
-   Google не рекомендует делать это.


### <span class="section-num">4.4</span> Задание флагов в конфигурационном файле {#задание-флагов-в-конфигурационном-файле}


#### <span class="section-num">4.4.1</span> Расположение конфигурационных файлов {#расположение-конфигурационных-файлов}

-   Пользовательский файл конфигурации: `$HOME/.config/chromium-flags.conf` (переменная среды `$XDG_CONFIG_HOME`).
-   Глобальный файл конфигурации находится в каталоге `/etc/chromium/default`.
-   В файле задаётся переменная окружения `CHROMIUM_FLAGS`.
-   Флаги можно размещать в отдельных строках для удобства чтения, но это не обязательно.
-   Строки, начинающиеся с символа решётки (`#`) использовать нельзя.


#### <span class="section-num">4.4.2</span> Пример конфигурационного файла {#пример-конфигурационного-файла}

-   Настроим перенос кэша броузера во временную файловую систему:
    ```conf-unix
    ## /etc/chromium/default

    CHROMIUM_FLAGS="
    --disk-cache-dir=$XDG_RUNTIME_DIR/chromium
    --ignore-gpu-blocklist
    --enable-gpu-rasterization
    --enable-zero-copy
    --ozone-platform-hint=auto
    --enable-features=WaylandWindowDecorations
    --enable-webrtc-pipewire-capturer
    --gtk-version=4
    --oauth2-client-id=77185425430.apps.googleusercontent.com
    --oauth2-client-secret=OTJgUOQcT7lO7GsGZq2G4IlT
    "
    ```
