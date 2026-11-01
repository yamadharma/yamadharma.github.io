---
title: "Маршрутизация. VyOS"
author: ["Dmitry S. Kulyabov"]
date: 2022-06-03T12:24:00+03:00
lastmod: 2026-10-18T19:10:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "routing-vyos"
---

Программный маршрутизатор _VyOS_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайты.
    -   Сайт: <https://vyos.net/>.
    -   Коммерческий сайт: <https://vyos.io/>.
    -   Репозиторий: <https://github.com/vyos/vyos-1x>.
    -   Документация: <https://docs.vyos.io/>.
    -   Документация в `pdf`: <https://buildmedia.readthedocs.org/media/pdf/vyos/latest/vyos.pdf>.
    -   Блог: <https://blog.vyos.io/>.
-   Поддержка Vagrant (см. [Использование vagrant]({{< relref "2021-11-12-using-vagrant" >}})).
    -   Образы для Vagrant: <https://app.vagrantup.com/vyos/>.
    -   Плагин для Vagrant: <https://github.com/higebu/vagrant-vyos>.
-   Форк проекта _Vyatta_.
-   Реализовано на основе дистрибутива Debian.
-   Система команд похожа на Juniper.
-   Подсистема маршрутизации основывается на проекте FRRouting (см. [Маршрутизация. FRRouting]({{< relref "2022-06-02-routing-frrouting" >}})).
-   Можно купить аппаратную платформу, на которой возможно развернуть маршрутизатор:
    -   <https://aliexpress.ru/popular/vyos-router.html>
    -   <https://aliexpress.ru/item/1005003378019857.html>


## <span class="section-num">2</span> Модель распространения {#модель-распространения}

-   Можно собрать самому из исходного кода (см. [Сборка образа VyOS]({{< relref "2023-07-06-vyos-build" >}})).
-   Образы LTS можно скачивать за плату.
    -   Для учебных заведений и некоммерческих организаций предоставляется бесплатный доступ к релизам.
-   Образы для rolling релизов можно скачивать бесплатно.
-   Rolling релизы:
    -   <https://vyos.net/get/nightly-builds/>;
    -   <https://community.vyos.net/get/>;
    -   <https://vyos.net/get/stream/>.
-   Блокируются российский ip-адреса.


## <span class="section-num">3</span> Функционал {#функционал}

-   VPN: Dynamic Multipoint VPN (DMVPN), GRE, IPSec, IPSec VTI, OpenVPN (server и client), WireGuard.
-   Туннели: L2TP, L2TPv3, VXLAN, PPTP, GRE, IPIP, SIT, IPIP, IPIP6, IP6IP6.
-   Интерфейсы L2/L3: Ethernet Bridge, 802.1Q VLAN, QinQ, Агрегация портов (LACP и статическая).
-   Маршрутизация: BGP, OSPF, OSPFv3, RIP, RIPng протоколов динамической маршрутизации.
-   Статическая маршрутизация и Policy-Based Routing (PBR)
-   QoS для приоритизации трафика.
-   Высокая доступность: VRRP, WAN load-balancing, Conntrack-Sync, Clustering.
-   Сетевые сервисы: DHCP, DNS recursive server, Network Address Translation, IGMP-Proxy, NTP, LLDP, mDNS repeater, PPPoE server, TFTP сервер.
-   Фильтрация трафика: Zone-based firewall, stateful firewall.
-   Политики: Shaping, Rate limiting, Priority-based queues.


## <span class="section-num">4</span> Конфигурирование {#конфигурирование}

-   [VyOS. Конфигурирование]({{< relref "2026-10-18--vyos-configuration" >}})


## <span class="section-num">5</span> Ресурсы {#ресурсы}


### <span class="section-num">5.1</span> Документация {#документация}

-   <https://opennix.org/docs/vyos/>


## <span class="section-num">6</span> Скачать образ {#скачать-образ}


### <span class="section-num">6.1</span> VyOS Stream 2026.03 {#vyos-stream-2026-dot-03}

-   <https://community-downloads.vyos.dev/stream/2026.03/vyos-2026.03-generic-amd64.iso>
-   <https://community-downloads.vyos.dev/stream/2026.03/circinus-2026.03.tar.gz>


## <span class="section-num">7</span> Образы операционной системы {#образы-операционной-системы}

-   [GNS3. Образ VyOS]({{< relref "2022-07-14-gns3-vyos" >}})
-   [Сборка образа VyOS]({{< relref "2023-07-06-vyos-build" >}})
-   [Сборка образа VyOS. Репозиторий]({{< relref "2023-07-16-vyos-build-repository" >}})
