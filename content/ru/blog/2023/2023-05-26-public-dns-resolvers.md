---
title: "Общедоступные резольверы DNS"
author: ["Dmitry S. Kulyabov"]
date: 2023-05-26T12:14:00+03:00
lastmod: 2024-12-28T11:46:00+03:00
tags: ["network"]
categories: ["computer-science"]
draft: false
slug: "public-dns-resolvers"
---

Общедоступные резольверы DNS.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Google {#google}

-   Описание:
    -   <https://developers.google.com/speed/public-dns/docs/using>
    -   <https://developers.google.com/speed/public-dns/docs/isp>
-   8.8.8.8
-   8.8.4.4
-   2001:4860:4860::8888
-   2001:4860:4860::8844
-   Поддерживается DNS over TLS.


## <span class="section-num">2</span> CloudFlare {#cloudflare}

-   1.1.1.1
-   1.0.0.1
-   2606:4700:4700::1111
-   2606:4700:4700::1001
-   Поддерживается DNS over TLS.


## <span class="section-num">3</span> Quad9 {#quad9}

-   9.9.9.9
-   149.112.112.112
-   Блокируются вредоносные хосты и поддерживается DNS over TLS.


## <span class="section-num">4</span> Yandex {#yandex}

-   Сайт: <https://dns.yandex.ru/>


### <span class="section-num">4.1</span> Базовый {#базовый}


#### <span class="section-num">4.1.1</span> Информация {#информация}

-   Стандартный рекурсивный DNS.
-   Не предусмотрена блокировка каких-либо сайтов.


#### <span class="section-num">4.1.2</span> Список {#список}

-   77.88.8.8
-   77.88.8.1
-   2a02:6b8::feed:0ff
-   2a02:6b8:0:1::feed:0ff


### <span class="section-num">4.2</span> Безопасный {#безопасный}


#### <span class="section-num">4.2.1</span> Информация {#информация}

-   Блокируются вредоносные хосты.
-   Защита от мошенников.
-   Защита от ботнетов.


#### <span class="section-num">4.2.2</span> Список {#список}

-   77.88.8.88
-   77.88.8.2
-   2a02:6b8::feed:bad
-   2a02:6b8:0:1::feed:bad


### <span class="section-num">4.3</span> Семейный {#семейный}


#### <span class="section-num">4.3.1</span> Описание {#описание}

-   Блокировка сайтов для взрослых.
    -   База данных с порносайтами обновляется 2-3 раза в неделю.
-   Блокировка рекламы для взрослых.
-   Семейный поиск Яндекса.


#### <span class="section-num">4.3.2</span> Список {#список}

-   77.88.8.7
-   77.88.8.3
-   2a02:6b8::feed:a11
-   2a02:6b8:0:1::feed:a11


## <span class="section-num">5</span> OpenDNS/Cisco {#opendns-cisco}

-   208.67.222.222
-   208.67.220.220
-   Блокируются вредоносные хосты и сайты для взрослых.
-   Поддерживается DNSCrypt и DNS over TLS.


## <span class="section-num">6</span> Comodo {#comodo}

-   8.26.56.26
-   8.20.247.20
-   Блокируются вредоносные хосты.
-   Поддерживается DNSCrypt и DNS over TLS.


## <span class="section-num">7</span> CleanBrowsing.org {#cleanbrowsing-dot-org}

-   185.228.168.168
-   185.228.169.168
-   Блокируется хосты с сайтами для взрослых.
-   Поддерживается DNSCrypt.


## <span class="section-num">8</span> DNS Watch {#dns-watch}

-   84.200.69.80
-   84.200.70.40
-   Не ведутся логи.


## <span class="section-num">9</span> FreeDNS {#freedns}

-   37.235.1.174
-   37.235.1.177
-   Не ведутся логи.


## <span class="section-num">10</span> Fourth Estate {#fourth-estate}

-   45.77.165.194
-   45.32.36.36
-   Не ведутся логи.


## <span class="section-num">11</span> UncensoredDNS {#uncensoreddns}

-   91.239.100.100
    -   Anycast.
-   89.233.43.71
    -   Размещён в Дании.


## <span class="section-num">12</span> Verisign {#verisign}

-   64.6.64.6
-   64.6.65.6


## <span class="section-num">13</span> Level 3 Communications {#level-3-communications}

-   4.2.2.1
-   4.2.2.2
-   4.2.2.3
-   4.2.2.4
-   4.2.2.5
-   4.2.2.6


## <span class="section-num">14</span> AdGuard {#adguard}

-   Сайт: <https://adguard-dns.io/>
-   Ограниченный пробный тариф.


### <span class="section-num">14.1</span> Серверы по умолчанию {#серверы-по-умолчанию}

-   Если вы хотите блокировать рекламу и трекеры.
-   94.140.14.14
-   94.140.15.15
-   2a10:50c0::ad1:ff
-   2a10:50c0::ad2:ff


### <span class="section-num">14.2</span> Серверы без фильтрации {#серверы-без-фильтрации}

-   Если вы не хотите, чтобы AdGuard DNS блокировал рекламу, трекеры или любые другие DNS-запросы.
-   94.140.14.140
-   94.140.14.141
-   2a10:50c0::1:ff
-   2a10:50c0::2:ff


### <span class="section-num">14.3</span> Семейные серверы {#семейные-серверы}

-   Если вы хотите блокировать рекламу, трекеры и взрослый контент, включить безопасный поиск и безопасный режим.
-   94.140.14.15
-   94.140.15.16
-   2a10:50c0::bad1:ff
-   2a10:50c0::bad2:ff


## <span class="section-num">15</span> Comss.one DNS {#comss-dot-one-dns}


### <span class="section-num">15.1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.comss.ru/page.php?id=7315>
-   Как настраивать: <https://www.comss.ru/page.php?id=15310>
-   Также предоставляет доступ к популярным сайтам и сервисам.
    -   В частности, вы можете пользоваться ИИ-сервисами (ChatGPT и Sora, Microsoft Copilot, GitHub Copilot, Google Gemini и Google ImageFX, Claude AI), или устанавливать обновления антивирусов, инсайдерские сборки и обновления Windows, а также играть в Brawl Stars в России.


### <span class="section-num">15.2</span> Стандартные серверы {#стандартные-серверы}

-   IPv4-адреса:
    -   83.220.169.155
    -   195.133.25.16
-   IPv6-адреса:
    -   2a01:230:4:915::2
    -   2a03:6f00:a::3f24


### <span class="section-num">15.3</span> Серверы с шифрованием {#серверы-с-шифрованием}

-   DNS-over-HTTPS (DoH)
    -   <https://dns.comss.one/dns-query>
-   DNS-over-TLS (DoT)
    -   dns.comss.one
    -   tls://dns.comss.one
-   DNS-over-HTTPS (DoH) – для MikroTik
    -   <https://dns.comss.one/mikrotik>
    -   IP: 195.133.25.16
-   DNS-over-QUIC (DoQ)
    -   quic://dns.comss.one
