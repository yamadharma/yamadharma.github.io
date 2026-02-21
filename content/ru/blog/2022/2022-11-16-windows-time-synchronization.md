---
title: "Windows. Синхронизация времени"
author: ["Dmitry S. Kulyabov"]
date: 2022-11-16T20:26:00+03:00
lastmod: 2023-07-08T16:19:00+03:00
tags: ["sysadmin", "windows"]
categories: ["computer-science"]
draft: false
slug: "windows-time-synchronization"
---

Синхронизация времени на Windows.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Синхронизация со сторонним NTP-сервером {#синхронизация-со-сторонним-ntp-сервером}


### <span class="section-num">1.1</span> Проблема {#проблема}

-   NTP-сервер по умолчанию для Windows (`time.windows.com`) часто сбоит.
-   При попытке синхронизировать Microsoft Windows с сервером протокола сетевого времени (NTP), который не работает под управлением Microsoft Windows, синхронизация может завершиться неудачно.


### <span class="section-num">1.2</span> Причина {#причина}

-   Иногда Windows отправляет запросы на синхронизацию в симметричном активном режиме (например, контроллеры домена Windows Server).
-   Зачастую серверы NTP отвечают только на запросы от клиентов, а не серверов.


### <span class="section-num">1.3</span> Решение {#решение}

-   В командной строке (с правами администратора) наберите:
    ```shell
    w32tm /config /manualpeerlist:pool.ntp.org,0x8 /syncfromflags:MANUAL
    net stop w32time
    net start w32time
    w32tm /resync
    ```

    -   `0x08` задаёт режим клиента.
