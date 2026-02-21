---
title: "Сетевые технологии. Лабораторные работы"
author: ["Dmitry S. Kulyabov"]
date: 2022-07-14T12:27:00+03:00
lastmod: 2025-08-23T14:52:00+03:00
tags: ["network", "education"]
categories: ["computer-science"]
draft: false
weight: 200
toc: true
type: "docs"
slug: "nettech-lab"
summary: "Лабораторные работы"
menu:
  "nettech-gns3-lab":
    parent: "nettech"
    weight: 200
    identifier: "nettech-gns3-lab"
---

Лабораторные работы по курсу _Сетевые технологии_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Лабораторные работы {#лабораторные-работы}

1.  Методы кодирования и модуляция сигналов
    -   Построение графиков в Octave
    -   Разложение импульсного сигнала в частичный ряд Фурье
    -   Определение спектра и параметров сигнала
    -   Амплитудная модуляция
    -   Кодирование сигнала. Исследование свойства самосинхронизации сигнала
2.  Расчёт сети Fast Ethernet

3.  Анализ трафика в Wireshark
    -   [Анализатор протоколов Wireshark]({{< relref "2021-08-18-wireshark-protocol-analyzer" >}})
    -   MAC-адресация. Анализ структуры MAC-адреса
    -   Анализ кадров канального уровня в Wireshark
    -   Анализ протоколов транспортного уровня в Wireshark
    -   Анализ handshake протокола TCP в Wireshark
4.  Подготовка экспериментального стенда GNS3
    -   [GNS3 на Virtualbox]({{< relref "2022-06-25-gns3-virtualbox" >}})
    -   [Основы работы в GNS3]({{< relref "2022-06-30-gns3-basics" >}})
    -   [Маршрутизация. FRRouting]({{< relref "2022-06-02-routing-frrouting" >}})
    -   [GNS3. Образ VyOS]({{< relref "2022-07-14-gns3-vyos" >}})
5.  Простые сети в GNS3. Анализ трафика
    -   Моделирование простейшей сети на базе коммутатора в GNS3
    -   Анализ трафика в GNS3 посредством Wireshark
    -   Моделирование простейшей сети на базе маршрутизатора FRR в GNS3
    -   Моделирование простейшей сети на базе маршрутизатора VyOS в GNS3
6.  Адресация IPv4 и IPv6. Двойной стек
    -   Разбиение сети на подсети
    -   [Адресация IPv4 и IPv6. Двойной стек]({{< relref "2022-07-08-ipv4-ipv6-addressing-double-stack" >}})
7.  Адресация IPv4 и IPv6. Настройка DHCP
    -   [Адресация IPv4 и IPv6. Настройка DHCP для IPv4]({{< relref "2022-08-15-configuring-dhcp-ipv4" >}})
    -   [Адресация IPv4 и IPv6. Настройка DHCPv6 для IPv6]({{< relref "2022-08-17-configuring-dhcpv6-ipv6" >}})
8.  Адресация IPv4 и IPv6. Настройка маршрутизации
    -   Настройка динамической маршрутизации в сетях IPv4 и IPv6. Протоколы RIP, OSPF
    -   [Туннель ipv6-ipv4]({{< relref "2022-07-14-tunnel-ipv6-ipv4" >}})
