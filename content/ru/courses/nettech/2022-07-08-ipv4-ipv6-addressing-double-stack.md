---
title: "Адресация IPv4 и IPv6. Двойной стек"
author: ["Dmitry S. Kulyabov"]
date: 2022-07-08T13:19:00+03:00
lastmod: 2022-09-08T16:29:00+03:00
tags: ["network", "education"]
categories: ["computer-science"]
draft: false
weight: 211
toc: true
type: docs
slug: "ipv4-ipv6-addressing-double-stack"
summary: "Адресация IPv4 и IPv6. Двойной стек"
menu:
  "ipv4-ipv6-addressing-double-stack":
    parent: "nettech-gns3-lab"
    weight: 211
    identifier: "ipv4-ipv6-addressing-double-stack"
---

Адресация IPv4 и IPv6. Двойной стек.

<!--more-->


## <span class="section-num">1</span> Описание {#описание}


### <span class="section-num">1.1</span> Цель {#цель}

-   Овладеть принципами настройки сетей IPv4 и IPv6.


### <span class="section-num">1.2</span> Задачи {#задачи}

-   Настроить адресацию IPv4 на хостах и маршрутизаторе.
-   Настроить статическую маршрутизацию IPv4.
-   Настроить адресацию IPv6 на хостах и маршрутизаторе.
-   Настроить статическую маршрутизацию IPv6.


### <span class="section-num">1.3</span> Схема сети {#схема-сети}

{{< figure src="/ox-hugo/20220708131900-topology.png" caption="<span class=\"figure-number\">&#1056;&#1080;&#1089;. 1.: </span>Схема сети" >}}


### <span class="section-num">1.4</span> Исходные данные {#исходные-данные}

-   К маршрутизаторам `gw-01` и `gw-02` подключены по две локальных сети.
-   Для настройки маршрутизации IPv6 будем использовать _routing advertisements_ (анонсирование маршрутов).

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Таблица адресации
</div>

| Устройство | Интерфейс | IP-адрес                      | Шлюз по умолчанию |
|------------|-----------|-------------------------------|-------------------|
| gw-01      | eth0      | 172.16.20.1/255.255.255.128   |                   |
| gw-01      | eth1      | 172.16.20.129/255.255.255.128 |                   |
| gw-01      | eth2      | 64.100.1.1/255.255.255.0      |                   |
| PC1        | NIC       | 172.16.20.10/255.255.255.128  | 172.16.20.1       |
| PC2        | NIC       | 172.16.20.138/255.255.255.128 | 172.16.20.129     |
| gw-02      | eth0      | 2001:db8:c0de:12::1/64        |                   |
| gw-02      | eth1      | 2001:db8:c0de:13::1/64        |                   |
| gw-02      | eth2      | 2001:db8:c0de:11::1/64        |                   |
| PC3        | NIC       | 2001:db8:c0de:12::a/64        | gw-02             |
| PC4        | NIC       | 2001:db8:c0de:13::a/64        | gw-02             |
| Server     | NIC       | 64.100.1.10/255.255.255.0     | 64.100.1.1        |
| Server     | NIC       | 2001:db8:c0de:11::a/64        | gw-02             |


### <span class="section-num">1.5</span> Задание {#задание}

-   Необходимо настроить соответствующую адресацию на каждом устройстве.
-   Необходимо проверить подключение из каждой сети к серверу с двойным стеком.


## <span class="section-num">2</span> Порядок выполнения {#порядок-выполнения}


### <span class="section-num">2.1</span> Настройка адресации IPv4 {#настройка-адресации-ipv4}


#### <span class="section-num">2.1.1</span> Настройка узлов {#настройка-узлов}

-   Руководствуясь таблицей адресации, настройте IPv4-адресацию для узлов PC1, PC2, Server:
    -   `PC1`:
        ```shell
        ip 172.16.20.10/25 172.16.20.1
        save
        ```
    -   `PC2`:
        ```shell
        ip 172.16.20.138/25 172.16.20.129
        save
        ```
    -   `Server`:
        ```shell
        ip 64.100.1.10/24 64.100.1.1
        save
        ```
-   Проверьте конфигурацию IPv4 на узлах:
    ```shell
    show ip
    ```


#### <span class="section-num">2.1.2</span> Настройка маршрутизатора {#настройка-маршрутизатора}

-   Руководствуясь таблицей адресации, настройте IPv4-адресацию для интерфейсов локальной сети маршрутизатора `gw-01`:
    ```conf-unix
    Router# configure terminal
    Router(config)# hostname gw-01
    gw-01(config)# exit
    gw-01# write memory

    gw-01# configure terminal
    gw-01(config)# interface eth0
    gw-01(config-if)# ip address 172.16.20.1/25
    gw-01(config-if)# no shutdown
    gw-01(config-if)# exit

    gw-01(config)# interface eth1
    gw-01(config-if)# ip address 172.16.20.129/25
    gw-01(config-if)# no shutdown
    gw-01(config-if)# exit

    gw-01(config)# interface eth2
    gw-01(config-if)# ip address 64.100.1.1/24
    gw-01(config-if)# no shutdown
    gw-01(config-if)# exit
    gw-01(config)# exit
    gw-01# write memory
    ```
-   Проверьте конфигурацию маршрутизатора и настройки IPv4-адресации:
    ```shell
    gw-01# show running-config
    gw-01# show interface brief
    ```


#### <span class="section-num">2.1.3</span> Проверка подключения {#проверка-подключения}

-   Проверьте подключение. Узлы PC1 и PC2 должны успешно отправлять эхо-запросы друг другу и на сервер с двойным стеком (Dual Stack Server).


### <span class="section-num">2.2</span> Настройка адресации IPv6 {#настройка-адресации-ipv6}


#### <span class="section-num">2.2.1</span> Настройка узлов {#настройка-узлов}

-   Руководствуясь таблицей адресации, настройте IPv6-адресацию для узлов PC3, PC4, Server:
    -   `PC3`:
        ```shell
        ip 2001:db8:c0de:12::a/64
        save
        ```
    -   `PC4`:
        ```shell
        ip 2001:db8:c0de:13::a/64
        save
        ```
    -   `Server`:
        ```shell
        ip 2001:db8:c0de:11::a/64
        save
        ```
-   Проверьте конфигурацию IPv6 на узлах:
    ```shell
    show ipv6
    ```


#### <span class="section-num">2.2.2</span> Настройка маршрутизатора {#настройка-маршрутизатора}

-   Назначьте IPv6-адреса маршрутизатору `gw-02`:
    ```conf-unix
    Router>enable
    Router# configure terminal
    Router(config)# hostname gw-02
    gw-02(config)# exit
    gw-02# write memory

    gw-02# configure terminal
    gw-02(config)# interface eth0
    gw-02(config-if)# ipv6 address 2001:db8:c0de:12::1/64
    gw-02(config-if)# no ipv6 nd suppress-ra
    gw-02(config-if)# ipv6 nd prefix 2001:db8:c0de:12::/64
    gw-02(config-if)# no shutdown
    gw-02(config-if)# exit

    gw-02# configure terminal
    gw-02(config)# interface eth1
    gw-02(config-if)# ipv6 address 2001:db8:c0de:13::1/64
    gw-02(config-if)# no ipv6 nd suppress-ra
    gw-02(config-if)# ipv6 nd prefix 2001:db8:c0de:13::/64
    gw-02(config-if)# no shutdown
    gw-02(config-if)# exit

    gw-02# configure terminal
    gw-02(config)# interface eth2
    gw-02(config-if)# ipv6 address 2001:db8:c0de:11::1/64
    gw-02(config-if)# no ipv6 nd suppress-ra
    gw-02(config-if)# ipv6 nd prefix 2001:db8:c0de:11::/64
    gw-02(config-if)# no shutdown
    gw-02(config-if)# exit

    gw-02(config)# ipv6 forwarding
    gw-02(config)# exit
    gw-02# write memory
    ```
-   Проверьте конфигурацию маршрутизатора и настройки IPv6-адресации:
    ```shell
    gw-02# show running-config
    gw-02# show interface brief
    ```
-   Проверьте интерфейсы, на которых рассылается сообщение о маршрутизаторе (_Router Advertisement_):
    ```shell
    gw-02# show ipv6 nd ra-interfaces
    ```


#### <span class="section-num">2.2.3</span> Проверка подключения {#проверка-подключения}

-   Проверьте подключение. Узлы PC3 и PC4 должны успешно отправлять эхо-запросы друг другу и на сервер с двойным стеком (Dual Stack Server).


## <span class="section-num">3</span> Видео: Адресация IPv4 и IPv6. Двойной стек {#видео-адресация-ipv4-и-ipv6-dot-двойной-стек}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 440cf57b3d880ed66dcfcb31ce469df3 >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube 7GYg0MC2NGI >}}

{{< /rtab >}}
{{< /tabs >}}
