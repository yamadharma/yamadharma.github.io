---
title: "DavMail"
author: ["Dmitry S. Kulyabov"]
date: 2022-04-10T19:02:00+03:00
lastmod: 2022-10-13T14:00:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "davmail"
---

DavMail --- прокси-сервер, позволяющая взаимодействовать с сервером Microsoft Exchange.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <http://davmail.sourceforge.net/>


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Пакетная установка {#пакетная-установка}

-   Gentoo
    ```shell
    emerge net-mail/davmail-bin
    ```

    -   Не в основном дереве portage.
    -   Используйте оверлей _pentoo_.


## <span class="section-num">3</span> Файлы конфигурации {#файлы-конфигурации}

-   Два варианта работы:
    -   запуск под пользователем;
    -   запуск на системном уровне.


### <span class="section-num">3.1</span> Запуск под пользователем {#запуск-под-пользователем}

-   Конфигурационный файл: `~/.davmail.properties`.
-   Запуск:
    ```shell
    davmail
    ```
-   В трее появляется значок.
-   Можно сконфигурить в графическом режиме, а после скопировать конфигурационный файл на системный уровень.
-   Если сконфигурирована аутентификация Oauth2, то конфигурационный файл содержит токен доступа.
    -   В таком виде использовать конфигурационный файл на системном уровне вряд ли получится.
-   _systemd-скрипт_ `/usr/lib/systemd/user/davmail.service` для запуска под пользователем:
    ```conf-unix
    [Unit]
    Description=Davmail Exchange gateway for %i
    Documentation=http://davmail.sourceforge.net/serversetup.html
    Documentation=http://davmail.sourceforge.net/advanced.html
    Documentation=http://davmail.sourceforge.net/sslsetup.html
    After=network.target

    [Service]
    ExecStart=/usr/bin/davmail %h/.davmail.properties
    Restart=on-failure

    [Install]
    WantedBy=default.target
    DefaultInstance=davmail
    ```
-   Можно поместить этот скрипт в каталог `~/.config/systemd/user`.
-   Запуск скрипта:
    ```shell
    systemctl --user enable --now davmail
    ```


### <span class="section-num">3.2</span> Запуск на системном уровне {#запуск-на-системном-уровне}

-   Конфигурационный файл: `/etc/davmail.properties`.
-   Запускается системным init-скриптом:
    ```shell
    systemctl enable --now davmail
    ```
-   _systemd-скрипт_ `/usr/lib/systemd/system/davmail.service` для запуска:
    ```conf-unix
    [Unit]
    Description=Davmail Exchange gateway
    Documentation=http://davmail.sourceforge.net/serversetup.html
    Documentation=http://davmail.sourceforge.net/advanced.html
    Documentation=http://davmail.sourceforge.net/sslsetup.html
    After=network.target

    [Service]
    Type=simple
    User=davmail
    PermissionsStartOnly=true
    ExecStartPre=/usr/bin/touch /var/log/davmail.log
    ExecStartPre=/bin/chown davmail:davmail /var/log/davmail.log
    ExecStart=/usr/bin/davmail -server /etc/davmail.properties
    SuccessExitStatus=143
    Restart=on-failure

    [Install]
    WantedBy=multi-user.target
    ```


## <span class="section-num">4</span> Параметры настройки {#параметры-настройки}


### <span class="section-num">4.1</span> Протокол Exchange {#протокол-exchange}

-   Параметр: `davmail.mode`.
-   `O365Modern` : Современная проверка подлинности Office 365  (Oauth2).
-   `O365Interactive` : Современная проверка подлинности Office 365 с интерактивным окном браузера:
    -   недоступно в автономном режиме (headless mode);
    -   требуется OpenJFX.
-   `O365Manual` : Современная проверка подлинности Office 365 с интерактивным диалогом:
    -   недоступно в автономном режиме (headless mode).
-   `O365` : EWS режим Office 365.
-   `EWS` : Exchange 2007 и более поздние версии.
-   `WebDav` : Exchange 2007 и более ранний с режимом WebDav.
-   `Auto` : Автоматический режим WebDav с переключением в режим `EWS` при ошибке.


### <span class="section-num">4.2</span> URL-адрес OWA {#url-адрес-owa}

-   Параметр: `davmail.url`:
    ```conf-unix
    davmail.url=https://outlook.office365.com/EWS/Exchange.asmx
    ```
-   URL-адрес Outlook Web Access для доступа к серверу Exchange.
-   `https://outlook.office365.com/EWS/Exchange.asmx` : значение по умолчанию для Office 365;
-   `https://Your.Exchange.Server/EWS/Exchange.asmx` : для своего Exchange-сервера.
-   Значение зависит от версии Microsoft Exchange.


### <span class="section-num">4.3</span> Порты {#порты}

-   Значение локальных портов обычно равно стандартному порту + 1000:
    ```conf-unix
    davmail.smtpPort=1025
    davmail.imapPort=1143
    davmail.popPort=1110
    davmail.ldapPort=1389
    davmail.caldavPort=1080
    ```


## <span class="section-num">5</span> Конфигурирование {#конфигурирование}


### <span class="section-num">5.1</span> Протокол `O365Modern` {#протокол-o365modern}

-   Для настройки используйте `O365Interactive` или `O365Manual`.
-   Для работы используйте `O365Modern`.
-   При запуске в режиме `O365Interactive` откроется окно с web-ссылкой и полем для заполнения.
    -   Перейдите по ней и разрешите приложению доступ.
    -   После этого откроется пустое окно.
    -   Адресную строку из этого окна перенесите в поле в исходном окне.
    -   Сохраните конфигурацию.
