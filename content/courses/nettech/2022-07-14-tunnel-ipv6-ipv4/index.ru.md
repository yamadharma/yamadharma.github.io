---
title: "Туннель ipv6-ipv4"
author: ["Dmitry S. Kulyabov"]
date: 2022-07-14T16:27:00+03:00
lastmod: 2024-04-10T11:37:00+03:00
tags: ["network", "education"]
categories: ["computer-science"]
draft: false
weight: 221
toc: true
type: docs
slug: "tunnel-ipv6-ipv4"
summary: "Туннель ipv6-ipv4"
menu:
  "tunnel-ipv6-ipv4":
    parent: "nettech-gns3-lab"
    weight: 221
    identifier: "tunnel-ipv6-ipv4"
---

Настройка туннеля ipv6-ipv4.

<!--more-->


## <span class="section-num">1</span> Цель {#цель}

-   Ознакомиться с использованием сетевых туннелей.


## <span class="section-num">2</span> Дополнительные сведения {#дополнительные-сведения}


### <span class="section-num">2.1</span> 6in4 (sit) {#6in4--sit}

-   6in4 использует туннелирование для инкапсуляции трафика IPv6 в трафик IPv4.
-   Определён в RFC 4213.
-   Трафик 6in4 отправляется внутри пакетов IPv4, в заголовках IP которых номер протокола IP установлен на 41.
-   Накладные расходы инкапсуляции --- это размер заголовка IPv4 в 20 байт, поэтому при MTU 1500 байт пакеты IPv6 размером 1480 байт можно отправлять без фрагментации.
-   Этот метод туннелирования часто используется брокерами туннелей IPv6 (например, Hurricane Electric).


## <span class="section-num">3</span> Задание {#задание}


### <span class="section-num">3.1</span> Схема сети {#схема-сети}

{{< figure src="/ox-hugo/20220714162700-topology.png" caption="<span class=\"figure-number\">&#1056;&#1080;&#1089;. 1.: </span>Схема сети" >}}


### <span class="section-num">3.2</span> Адреса сетей {#адреса-сетей}

| Хост | Интерфейс | Адрес              |
|------|-----------|--------------------|
| R1   | eth0      | 1000::1/64         |
| R1   | eth1      | 10.0.0.1/255.0.0.0 |
| R1   | Tunnel0   | 1001::1/64         |
| R2   | eth0      | 1002::1/64         |
| R2   | eth1      | 20.0.0.2/255.0.0.0 |
| R2   | Tunnel0   | 1001::2/64         |
| R3   | eth0      | 10.0.0.2/255.0.0.0 |
| R3   | eth1      | 20.0.0.1/255.0.0.0 |
| PC1  |           | 1000::a/64         |
| PC2  |           | 1002::a/64         |


## <span class="section-num">4</span> Выполнение работы {#выполнение-работы}


### <span class="section-num">4.1</span> Конфигурация адресации {#конфигурация-адресации}


#### <span class="section-num">4.1.1</span> Настройка узлов {#настройка-узлов}

-   `PC1`:
    ```shell
    ip 1000::a/64
    save
    ```
-   `PC2`:
    ```shell
    ip 1002::a/64
    save
    ```
-   Проверьте конфигурацию IPv6 на узлах:
    ```shell
    show ipv6
    ```


#### <span class="section-num">4.1.2</span> Настройка маршрутизаторов {#настройка-маршрутизаторов}

-   `R1`:
    ```shell
    vyos@R1:~$ configure
    vyos@R1# set interfaces ethernet eth0 address 1000::1/64
    vyos@R1# set interfaces ethernet eth1 address 10.0.0.1/8
    vyos@R1# set service router-advert interface eth0 prefix 1000::/64

    vyos@R1# commit
    vyos@R1# save
    ```
-   `R2`:
    ```shell
    vyos@R2:~$ configure
    vyos@R2# set interfaces ethernet eth0 address 1002::1/64
    vyos@R2# set interfaces ethernet eth1 address 20.0.0.2/8
    vyos@R2# set service router-advert interface eth0 prefix 1002::/64

    vyos@R2# commit
    vyos@R2# save
    ```
-   `R3`:
    ```shell
    vyos@R3:~$ configure
    vyos@R3# set interfaces ethernet eth0 address 10.0.0.2/8
    vyos@R3# set interfaces ethernet eth1 address 20.0.0.1/8

    vyos@R3# commit
    vyos@R3# save
    ```
-   Проверьте маршруты:
    ```shell
    vyos@R1:~$ ping 10.0.0.2
    vyos@R1:~$ ping 20.0.0.1
    vyos@R1:~$ ping 20.0.0.2
    ```


### <span class="section-num">4.2</span> Конфигурация маршрутизации IPv4 {#конфигурация-маршрутизации-ipv4}

-   `R1`:
    ```shell
    vyos@R1:~$ configure
    vyos@R1# set protocols rip network 10.0.0.0/8

    vyos@R1# commit
    vyos@R1# save
    ```
-   `R2`:
    ```shell
    vyos@R2:~$ configure
    vyos@R2# set protocols rip network 20.0.0.0/8

    vyos@R2# commit
    vyos@R2# save
    ```
-   `R3`:
    ```shell
    vyos@R3:~$ configure
    vyos@R3# set protocols rip network 10.0.0.0/8
    vyos@R3# set protocols rip network 20.0.0.0/8

    vyos@R3# commit
    vyos@R3# save
    ```
-   Проверьте маршруты:
    ```shell
    vyos@R1:~$ ping 10.0.0.2
    vyos@R1:~$ ping 20.0.0.1
    vyos@R1:~$ ping 20.0.0.2
    ```


### <span class="section-num">4.3</span> Создайте туннель IPv6 через сеть IPv4 {#создайте-туннель-ipv6-через-сеть-ipv4}

-   `R1`:
    ```shell
    vyos@R1:~$ configure
    vyos@R1# set interfaces tunnel tun0 encapsulation sit
    vyos@R1# set interfaces tunnel tun0 source-address 10.0.0.1
    vyos@R1# set interfaces tunnel tun0 remote 20.0.0.2
    vyos@R1# set interfaces tunnel tun0 address 1001::1/64

    vyos@R1# commit
    vyos@R1# save
    ```
-   `R2`:
    ```shell
    vyos@R2:~$ configure
    vyos@R2# set interfaces tunnel tun0 encapsulation sit
    vyos@R2# set interfaces tunnel tun0 source-address 20.0.0.2
    vyos@R2# set interfaces tunnel tun0 remote 10.0.0.1
    vyos@R2# set interfaces tunnel tun0 address 1001::2/64

    vyos@R2# commit
    vyos@R2# save
    ```


### <span class="section-num">4.4</span> Конфигурация статической маршрутизации IPv6 {#конфигурация-статической-маршрутизации-ipv6}

-   `R1`:
    ```shell
    vyos@R1:~$ configure
    vyos@R1# set protocols static route6 1002::0/64 next-hop 1001::2

    vyos@R1# commit
    vyos@R1# save
    ```
-   `R2`:
    ```shell
    vyos@R2:~$ configure
    vyos@R2# set protocols static route6 1000::0/64 next-hop 1001::1

    vyos@R2# commit
    vyos@R2# save
    ```


### <span class="section-num">4.5</span> Проверка {#проверка}

-   `PC1`:
    ```shell
    PC1> ping 1002::a
    PC1> trace 1002::a
    ```
-   `PC2`:
    ```shell
    PC2> ping 1000::a
    PC2> trace 1000::a
    ```


## <span class="section-num">5</span> Видео: Туннель ipv6-ipv4 {#видео-туннель-ipv6-ipv4}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 4af0cfdef4f35b000aefcc283c9865c0 >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube a0x0Ibyt7uE >}}

{{< /rtab >}}
{{< /tabs >}}
