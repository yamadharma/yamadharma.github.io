---
title: "IPv6. Туннельные брокеры. Ip4market"
author: ["Dmitry S. Kulyabov"]
date: 2023-06-30T12:55:00+03:00
lastmod: 2023-07-11T11:31:00+03:00
tags: ["ipv6", "network"]
categories: ["computer-science"]
draft: false
slug: "ipv6-tunnel-broker-ip4market"
---

Туннельный брокер Ip4market.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт:
    -   <http://ipv6.ip4market.ru/>
    -   <http://tunnelbroker.ru/>
    -   <https://tb.ip4market.ru/>
-   Документация:
    -   <https://ipv6.ip4market.ru/?page=help>
-   Блог: <http://blog.ip4market.ru/>
-   Telegram-канал: [@ip4market](https://t.me/ip4market)
-   Точки присутствия (PoPs): 1
-   Сервер расположен в России (г. Москва).
-   Расположение: Россия
-   Подсеть: `/64` и `/48`
-   Prefix:
    -   `2a04:5200::/32`
    -   `2a03:e2c0::/32`


## <span class="section-num">2</span> Особенности {#особенности}

-   -   Для борьбы со спамерами введено ограничение по регистрации.
    -   Регистрировать можно один раз с одного домена.
    -   То есть практически следует иметь свой домен для регистрации.


## <span class="section-num">3</span> Адреса {#адреса}

-   При регистрации базово выделяется сеть `/48` : `2a03:e2c0:XXX::/48`.
-   Из неё выделяется 2 сети `/64` :
    -   `2a03:e2c0:XXX::/64`;
    -   `2a03:e2c0:XXX:5555::/64`
-   Первая сеть назначается для туннеля 6in4:
    -   адрес `::1` : принадлежит брокеру;
    -   адрес `::2` : выделяется для роутера пользователя.


## <span class="section-num">4</span> Настройка IPv6 туннеля {#настройка-ipv6-туннеля}

-   Сеть для раздачи клиентам: `2a03:e2c0:XXX:5555::/64`. Нужно указать её в роутере как полученный префикс IPv6.
-   IPv6-адрес клиента: `2a03:e2c0:XXXX::2/64`.
-   IPv6-адрес шлюза: `2a03:e2c0:XXXX::1/64`.
-   Сервер для подключения: `193.0.203.203`. На этот адрес роутер отправляет пакеты с IPv6 трафиком.
-   Своего DNS нет, рекомендуется использовать общедоступные резолверы (см. [Общедоступные резольверы DNS]({{< relref "2023-05-26-public-dns-resolvers" >}})).


## <span class="section-num">5</span> Примеры настройки {#примеры-настройки}

-   Настройка для Cisco (внешний IPv4: `Y.Y.Y.Y`):
    ```shell
    configure terminal

    ipv6 unicast-routing
    ipv6 cef

    ipv6 dhcp pool LAN-v6
     address prefix 2a03:e2c0:XXXX:5555::1/64
     dns-server 2a02:6b8::feed:0ff
     domain-name ipv6.orcinus.ru
     exit

    interface Tunnel1
     description IP4Market IPv6 (RUSSIA)
     no ip address
     ipv6 address 2a03:e2c0:XXXX::2/64
     ipv6 enable
     tunnel source Y.Y.Y.Y
     tunnel mode ipv6ip
     tunnel destination 193.0.203.203
     exit

    interface FastEthernet0/1
     ipv6 address 2a03:e2c0:XXXX:5555::/64
     ipv6 enable
     ipv6 nd managed-config-flag
     ipv6 dhcp server LAN-v6
     exit

    ipv6 route ::/0 Tunnel1
    ```
