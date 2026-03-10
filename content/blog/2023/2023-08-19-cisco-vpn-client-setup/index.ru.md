---
title: "Подключение к Cisco VPN"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-19T13:34:00+03:00
lastmod: 2024-12-17T12:47:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "cisco-vpn-client-setup"
---

<!--more-->

Подключение к Cisco AnyConnect VPN.
{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   В качестве клиента для Cisco AnyConnect VPN предлагается использовать OpenConnect.
-   Репозиторий: <https://gitlab.com/openconnect/openconnect>
-   Репозиторий модуля для Network Manager: <https://gitlab.gnome.org/GNOME/NetworkManager-openconnect>


## <span class="section-num">2</span> Установка в Linux {#установка-в-linux}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   Установите клиента для Network Manager:
    ```shell
    emerge net-vpn/networkmanager-openconnect
    ```


## <span class="section-num">3</span> Подключение {#подключение}

-   При создании соединения в Network Manager необходимо задать адрес шлюза.
-   При первом подключении у Вас запросят парольные данные.
-   Если Вы их сохраните, то более их не надо будет набирать.
-   Если у вас используется сертификат или нужно указать какие-то дополнительные параметры, то это необходимо сделать в этом же окне.


## <span class="section-num">4</span> DNS {#dns}

-   Обычно VPN настроены на раздельную маршрутизацию и раздельный DNS.
-   Для удобной работы с раздельным DNS рекомендуется использовать `systemd-resolved` в stub-режиме (режиме заглушки) `resolv.conf`.
-   Просмотр параметров работы `systemd-resolved` выполняется с помощью команды:
    ```shell
    resolvectl
    ```
