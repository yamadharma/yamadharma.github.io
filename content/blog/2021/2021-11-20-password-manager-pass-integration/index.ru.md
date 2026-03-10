---
title: "Менеджер паролей pass. Интеграция с другими программами"
author: ["Dmitry S. Kulyabov"]
date: 2021-11-20T21:47:00+03:00
lastmod: 2024-12-01T18:58:00+03:00
tags: ["security"]
categories: ["computer-science"]
draft: false
slug: "password-manager-pass-integration"
---

Интеграция менеджера паролей _pass_ с другими программами (см. [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Launchers {#launchers}


### <span class="section-num">1.1</span> Linux {#linux}


#### <span class="section-num">1.1.1</span> rofi-pass {#rofi-pass}

-   [rofi-pass]({{< relref "2022-04-03-rofi-pass" >}})
-   Интеграция _pass_ с _rofi_ (см. [Запуск приложений. Rofi]({{< relref "2021-11-19-launcher_rofi" >}})).
-   Работает в X11.


#### <span class="section-num">1.1.2</span> tessen {#tessen}

-   [Менеджер паролей pass. Tessen]({{< relref "2024-12-01-password-manager-pass-tessen" >}})
-   Репозиторий: <https://github.com/ayushnix/tessen>
-   Работает в Wayland.


### <span class="section-num">1.2</span> Windows {#windows}


#### <span class="section-num">1.2.1</span> pass-winmenu {#pass-winmenu}

-   Репозиторий: <https://github.com/geluk/pass-winmenu>
-   Простой и удобный менеджер паролей для Windows.
-   Содержит собственную реализацию _pass_.
-   Установка (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
    ```shell
    choco install pass-winmenu
    ```

    -   Страница: <https://chocolatey.org/packages/pass-winmenu>


## <span class="section-num">2</span> Настройка интерфейса с броузером {#настройка-интерфейса-с-броузером}

-   Для взаимодействия с броузером используется интерфейс _native messaging_.
-   Поэтому кроме плагина к броузеру устанавливается программа, обеспечивающая интерфейс _native messaging_.


### <span class="section-num">2.1</span> pass {#pass}


#### <span class="section-num">2.1.1</span> Плагин [browserpass](https://github.com/browserpass/browserpass-extension) {#плагин-browserpass}

-   Репозиторий: <https://github.com/browserpass/browserpass-extension>
-   Плагин для брoузера
    -   Плагин для Firefox: <https://addons.mozilla.org/en-US/firefox/addon/browserpass-ce/>.
    -   Плагин для Chrome/Chromium: <https://chrome.google.com/webstore/detail/browserpass-ce/naepdomgkenhinolocfifgehidddafch>.
-   Интерфейс для взаимодействия с броузером (native messaging)
    -   Репозиторий: <https://github.com/browserpass/browserpass-native>
    -   Gentoo:
        ```shell
        emerge www-plugins/browserpass
        ```
    -   Ubuntu, Debian
        ```shell
        apt-get install webext-browserpass
        ```
    -   Fedora
        ```shell
        dnf copr enable maximbaz/browserpass
        dnf install browserpass
        dnf install browserpass-chromium
        dnf install browserpass-firefox
        ```


#### <span class="section-num">2.1.2</span> Плагин chrome-pass {#плагин-chrome-pass}

-   Репозиторий: <https://github.com/hsanson/chrome-pass>
-   Плагин для брoузера
    -   Плагин для Chrome/Chromium: <https://chrome.google.com/webstore/detail/chrome-pass-zx2c4/oblajhnjmknenodebpekmkliopipoolo>
-   Интерфейс для взаимодействия с броузером (native messaging)
    -   Установка для пользователя:
        ```shell
        pip3 install --user chrome-pass==0.3.0
        nativePass install
        ```


#### <span class="section-num">2.1.3</span> Плагин passff {#плагин-passff}

-   Репозиторий: <https://github.com/passff/passff>
-   Плагин для брoузера
    -   Плагин для Firefox: <https://addons.mozilla.org/ru/firefox/addon/passff/>
-   Интерфейс для взаимодействия с броузером (native messaging)
    -   Репозиторий: <https://github.com/passff/passff-host>
    -   Установка:
        ```shell
        curl -sSL github.com/passff/passff-host/releases/latest/download/install_host_app.sh | bash -s -- firefox
        ```

        -   Пользователям других поддерживаемых броузеров необходимо заменить последний аргумент (`firefox`) на `chrome`, `opera`, `chromium` или `vivaldi`.
        -   Скрипт загрузит хост-приложение (небольшой скрипт на _python_) и файл манифеста плагина (файл конфигурации _JSON_) и поместит их в нужное место.
        -   Можно загрузить файлы самостоятельно и запустить сценарий с параметром `--local` или установить файлы самостоятельно.


### <span class="section-num">2.2</span> gopass {#gopass}

-   Плагин для браузера называется [gopass bridge](https://github.com/gopasspw/gopassbridge)
    -   Firefox: <https://addons.mozilla.org/en-US/firefox/addon/gopass-bridge/>
    -   Chrome/Chromium: <https://chrome.google.com/webstore/detail/gopass-bridge/kkhfnlkhiapbiehimabddjbimfaijdhk>
-   Начиная с версии gopass-1.12.0 команда создания интерфейса взаимодействия с броузером выделена в отдельную утилиту.
-   Устанавливаем интерфейс для взаимодействия с броузером (native messaging):
    -   Gentoo
        ```shell
        emerge app-admin/gopass-jsonapi
        ```
    -   Fedora
        ```shell
        dnf install gopass-jsonapi
        ```
-   Для связки плагина с `gopass` необходимо создать вспомогательный скрипт и манифест:
    ```shell
    gopass-jsonapi configure
    ```
