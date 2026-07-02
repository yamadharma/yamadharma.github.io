---
title: "Синхронизация файлов с помощью syncthing"
author: ["Dmitry S. Kulyabov"]
date: 2021-08-01T15:58:00+03:00
lastmod: 2026-05-25T17:13:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "synchronizing-files-syncthing"
---

Синхронизация файлов между хостами с помощью _syncthing_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Позволяет синхронизировать файлы между несколькими устройствами.
-   Лиценизия: MPL-2.0.
-   Сайт: <https://syncthing.net/>.
-   Синхронизация происходит по дате изменения файла.
-   Есть поддержка синхронизации на уровне блоков, то есть при небольших изменениях в файле будут синхронизированы только изменившиеся блоки, а не весь файл.
-   _Syncthing_ фактически является заменой _BitTorrent Sync_ (сейчас _Resilio Sync_) (<https://www.resilio.com/>).


## <span class="section-num">2</span> Порты {#порты}

-   Порты прописаны в файле `config.xml`.


### <span class="section-num">2.1</span> Порт синхронизации (по умолчанию `22000`) {#порт-синхронизации--по-умолчанию-22000}

-   Элемент `<listenAddress>` внутри секции `<options>`.
-   Если значение стоит `default`, замените его на явный список адресов с новым портом. Например, для смены на `22001`:

<!--listend-->

```xml
<options>
    <listenAddress>tcp://0.0.0.0:22001, quic://0.0.0.0:22001</listenAddress>
    ...
</options>
```

-   Так вы принудительно назначите и TCP, и QUIC на порт `22001`.


### <span class="section-num">2.2</span> Порт веб-интерфейса (по умолчанию `8384`) {#порт-веб-интерфейса--по-умолчанию-8384}

-   Элемент `<address>` внутри секции `<gui>`.

<!--listend-->

```xml
<gui enabled="true" tls="false" debugging="false">
    <address>127.0.0.1:8385</address>
    ...
</gui>
```


### <span class="section-num">2.3</span> Порт локального обнаружения (по умолчанию `21027`) {#порт-локального-обнаружения--по-умолчанию-21027}

-   Элемент `<localAnnouncePort>` внутри `<options>`.

<!--listend-->

```xml
<options>
    <localAnnouncePort>21028</localAnnouncePort>
    ...
</options>
```

-   После изменения порта локального обнаружения также имеет смысл скорректировать `<localAnnounceMCAddr>`, если он задан вручную, но обычно достаточно только номера порта.


## <span class="section-num">3</span> Варианты приложения {#варианты-приложения}

-   Официальный клиент:
    -   Сайт: <https://syncthing.net/>.
    -   Репозиторий: <https://github.com/syncthing/syncthing>.
-   syncthing-android --- версия для Android:
    -   Репозиторий: <https://github.com/syncthing/syncthing-android>.
    -   Google Play: <https://play.google.com/store/apps/details?id=com.nutomic.syncthingandroid>.
    -   F-Droid: <https://f-droid.org/ru/packages/com.nutomic.syncthingandroid/>.


## <span class="section-num">4</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge syncthing
    ```
-   Fedora:
    ```shell
    dnf install syncthing
    ```
-   Debian:
    ```shell
    apt install syncthing
    ```
-   Manjaro:
    ```shell
    pamac install syncthing
    ```


## <span class="section-num">5</span> Настройка синхронизации {#настройка-синхронизации}

-   [Syncthing. Командная строка]({{< relref "2024-05-29-syncthing-cli" >}})
-   [Syncthing. Частный релей]({{< relref "2026-05-25--syncthing-private-relay" >}})
