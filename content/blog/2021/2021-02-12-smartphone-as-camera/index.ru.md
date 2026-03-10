---
title: "Использование смартфона в качестве камеры"
author: ["Dmitry S. Kulyabov"]
date: 2021-02-12T18:38:00+03:00
lastmod: 2023-08-27T18:22:00+03:00
tags: ["sysadmin", "education"]
categories: ["computer-science", "science"]
draft: false
slug: "smartphone-as-camera"
---

При отсутствии компьютерной камеры можно в качестве камеры использовать смартфон.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Droidcam {#droidcam}

Программный пакет [Droidcam](https://www.dev47apps.com/) предполагает установку приложений как на смартфон, так и на компьютер.


### <span class="section-num">1.1</span> Установка программного обеспечения {#установка-программного-обеспечения}

Для работы следует установить клиента на смартфон и на операционную систему компьютера.


#### <span class="section-num">1.1.1</span> Смартфон {#смартфон}

На смартфон следует установить приложение [DroidCam](https://play.google.com/store/apps/details?id=com.dev47apps.droidcam).

-   Домашняя страница: <https://www.dev47apps.com/>.
-   Google Play (версия Free): <https://play.google.com/store/apps/details?id=com.dev47apps.droidcam>.
    -   Поддержка разрешения видео 640x480, 320x240.
-   Google Play (версия Pro): <https://play.google.com/store/apps/details?id=com.dev47apps.droidcamx>.
    -   Нет рекламы.
    -   Поддержка высокого разрешения видео (720p/1080p в HD Mode).
    -   Настройки камеры: вспышка, авто-фокусировка, увеличение изображения и другое.
-   Есть вариант для iPhone.
-   Инструкция от разработчика: <https://www.dev47apps.com/droidcam/connect/>.
-   Help по программе: <https://www.dev47apps.com/droidcam/help/>.


#### <span class="section-num">1.1.2</span> Windows {#windows}

-   Установка с помощью менеджера пакетов Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})).
    ```shell
    choco install droidcamclient
    ```
-   Можно скачать и установить вручную, скачав приложение по адресу: <https://www.dev47apps.com/droidcam/windows/>.


#### <span class="section-num">1.1.3</span> Linux {#linux}

-   Необходима поддержка `Video4Linux loopback` в ядре:
    ```conf-unix
    Device Drivers --->
      <M> Multimedia support --->
        [*] Cameras/video grabbers support
        [*] Media Controller API
        [*] V4L2 sub-device userspace API
    ```
-   Пакет устанавливает утилиты и модуль ядра.
-   Репозиторий клиента: <https://github.com/dev47apps/droidcam>.

<!--list-separator-->

1.  Дистрибутивы

    -   Gentoo
        -   Пакет отсутствует в основном дереве portage. Следует использовать overlay:
            -   nex-overlay <https://gitlab.com/NexAdn/nex-overlay>;
            -   thegreatmcpain
                ```shell
                layman -a thegreatmcpain
                ```
            -   guru
                ```shell
                layman -a guru
                ```
        -   Установка:
            ```shell
            emerge droidcam
            ```

<!--list-separator-->

2.  Настройка

    -   В результате будет установлен модуль ядра `v4l2loopback_dc`.
    -   По умолчанию разрешение установлено в 640x480.
    -   Для настройки разрешения необходимо задать опции для модуля.
    -   Опции задаются в соответствующих файлах. В зависимости от дистрибутива они называются:
        -   `/etc/modprobe.d/v4l2loopback-dc.conf`;
        -   `/etc/modprobe.d/droidcam.conf`.
    -   Формат записи:
        ```conf-unix
        options v4l2loopback-dc width=640 height=480
        ```
    -   Поддерживаемые разрешения: 320×240, 480×360, 640×480, 960×720, 1280×720, 1920x1080.


### <span class="section-num">1.2</span> Использование программы {#использование-программы}

После запуска программы на смартфоне возможно переключения камер телефона.


#### <span class="section-num">1.2.1</span> Подключение по Wi-Fi {#подключение-по-wi-fi}

-   Запускаем `droidcam` на компьютере и на телефоне.
-   Выбираем подключение по Wi-Fi (нужно подключаться обязательно к одной и той же сети с телефона и с компьютера).
-   После подключения к Wi-Fi в программе на смартфоне отобразиться IP.
-   На компьютере в программе выберите тип подключения "Connect over WiFi (LAN)", введите IP и порт из приложения на смартфоне, нажмите Start.


#### <span class="section-num">1.2.2</span> Подключение по Wi-Fi (через броузер) {#подключение-по-wi-fi--через-броузер}

-   Запускаем `droidcam` на телефоне.
-   Открываем броузер на любом устройстве и вводим в адресную строку `http://ip:port`, где `ip` и `port` --- это IP-адрес и порт из приложения на андроиде.


#### <span class="section-num">1.2.3</span> Подключение по Wi-Fi (создав Wi-Fi сервер) {#подключение-по-wi-fi--создав-wi-fi-сервер}

-   На компьютере в программе выбирается режим `Create WiFi Server`, нажмите Start.
-   На смартфоне в приложении:
    -   откройте опции, выберите `Connect to Server`, `Add new`;
    -   в поле `Name` введите любое название;
    -   в поле `IP Address` введите адрес компьютера;
    -   нажимает `Save`;
    -   выбираем созданный сервер.


#### <span class="section-num">1.2.4</span> Подключение по USB {#подключение-по-usb}

-   На смартфоне включить `Отладка по USB`.
-   На компьютере в программе выбрать режим `Connect over USB` (на компьютере должны быть установлены драйвера ADB).
-   Подключить смартфон по USB кабелю.
-   На компьютере нажать `Start`.
