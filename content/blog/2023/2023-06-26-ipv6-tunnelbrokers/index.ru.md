---
title: "Брокеры IPv6"
author: ["Dmitry S. Kulyabov"]
date: 2023-06-26T12:57:00+03:00
lastmod: 2023-06-30T12:57:00+03:00
tags: ["ipv6", "network"]
categories: ["computer-science"]
draft: false
slug: "ipv6-tunnelbrokers"
---

Брокеры IPv6.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Брокеры 6in4 {#брокеры-6in4}


### <span class="section-num">1.1</span> Hurricane Electric {#hurricane-electric}

-   Сайт: <http://he.net/>
-   Точки присутствия (PoPs): 32
-   Расположение: Канада, Европа (8 стран), Гонконг, Япония, Сингапур, США (9 штатов)
-   Подсеть:
    -   /64 по умолчанию;
    -   /48 через автономную систему
-   Prefix: `2001:470::/32`


### <span class="section-num">1.2</span> IP4market {#ip4market}

-   [IPv6. Туннельные брокеры. Ip4market]({{< relref "2023-06-30-ipv6-tunnel-broker-ip4market" >}})
-   Сайт: <http://ipv6.ip4market.ru/>
-   Точки присутствия (PoPs): 1
-   Расположение: Россия
-   Подсеть: `/64` и `/48`
-   Prefix:
    -   `2a04:5200::/32`
    -   `2a03:e2c0::/32`
