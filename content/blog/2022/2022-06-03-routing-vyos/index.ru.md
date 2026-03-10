---
title: "Маршрутизация. VyOS"
author: ["Dmitry S. Kulyabov"]
date: 2022-06-03T12:24:00+03:00
lastmod: 2025-02-20T14:14:00+03:00
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
    -   <https://vyos.net/get/?dir=rolling/current/amd64>;
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


### <span class="section-num">4.1</span> Быстрая настройка {#быстрая-настройка}

-   Настроим шлюз NAT с двумя сетевыми интерфейсами (`eth0` и `eth1`).


#### <span class="section-num">4.1.1</span> Режим конфигурации {#режим-конфигурации}

-   В рабочем режиме в командной строке отображается символ `$`.
-   В режиме конфигурации в командной строке отображается `#`:
    ```shell
    vyos@vyos$ configure
    vyos@vyos#
    ```


#### <span class="section-num">4.1.2</span> Сохранение {#сохранение}

-   После каждого изменения конфигурации необходимо применить изменения:
    ```shell
    commit
    ```
-   В конце нужно сохранить конфигурацию:
    ```shell
    save
    ```


#### <span class="section-num">4.1.3</span> Конфигурация интерфейсов {#конфигурация-интерфейсов}

-   Внешний интерфейс: `eth0`. Он получает адрес по DHCP.
-   Внутренний интерфейс: `eth1`. Использует статический IP-адрес `192.168.0.1/24`.
-   После перехода в режим конфигурации введём следующие команды:
    ```shell
    set interfaces ethernet eth0 address dhcp
    set interfaces ethernet eth0 description 'OUTSIDE'
    set interfaces ethernet eth1 address '192.168.0.1/24'
    set interfaces ethernet eth1 description 'INSIDE'
    ```


#### <span class="section-num">4.1.4</span> SSH-сервер {#ssh-сервер}

-   Включим ssh-сервер:
    ```shell
    set service ssh port '22'
    ```


#### <span class="section-num">4.1.5</span> Сервисы DHCP и DNS {#сервисы-dhcp-и-dns}

-   Сетевые настройки:
    -   Шлюз по умолчанию и адрес сервера DNS: `192.168.0.1/24`.
    -   Диапазон адресов для статических назначений: `192.168.0.2/24`--`192.168.0.8/24`.
    -   Диапазон адресов для клиентов DHCP: `192.168.0.9`--`192.168.0.254`.
    -   Время аренды адреса DHCP: однин день (86400 секунд).
    -   Рекурсор DNS могут использовать только хосты из локальной сети.
-   Конфигурация:
    ```shell
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 default-router '192.168.0.1'
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 name-server '192.168.0.1'
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 domain-name 'vyos.net'
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 lease '86400'
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 range 0 start 192.168.0.9
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 range 0 stop '192.168.0.254'

    set service dns forwarding cache-size '0'
    set service dns forwarding listen-address '192.168.0.1'
    set service dns forwarding allow-from '192.168.0.0/24'
    ```


#### <span class="section-num">4.1.6</span> Настройка NAT {#настройка-nat}

-   Настроим правила SNAT для внутренней сети:
    ```shell
    set nat source rule 100 outbound-interface 'eth0'
    set nat source rule 100 source address '192.168.0.0/24'
    set nat source rule 100 translation address masquerade
    ```


#### <span class="section-num">4.1.7</span> Брандмауэр {#брандмауэр}

-   Блокируем весь трафик, который не был инициирован со стороны локальной сети:
    ```shell
    set firewall name OUTSIDE-IN default-action 'drop'
    set firewall name OUTSIDE-IN rule 10 action 'accept'
    set firewall name OUTSIDE-IN rule 10 state established 'enable'
    set firewall name OUTSIDE-IN rule 10 state related 'enable'

    set firewall name OUTSIDE-LOCAL default-action 'drop'
    set firewall name OUTSIDE-LOCAL rule 10 action 'accept'
    set firewall name OUTSIDE-LOCAL rule 10 state established 'enable'
    set firewall name OUTSIDE-LOCAL rule 10 state related 'enable'
    set firewall name OUTSIDE-LOCAL rule 20 action 'accept'
    set firewall name OUTSIDE-LOCAL rule 20 icmp type-name 'echo-request'
    set firewall name OUTSIDE-LOCAL rule 20 protocol 'icmp'
    set firewall name OUTSIDE-LOCAL rule 20 state new 'enable'
    ```
-   Разрешим SSH-доступ к маршрутизатору с внешнего интерфейса.
-   Ограничивают до 4 запросов в минуту (для блокировки взлома грубой силой):
    ```shell
    set firewall name OUTSIDE-LOCAL rule 30 action 'drop'
    set firewall name OUTSIDE-LOCAL rule 30 destination port '22'
    set firewall name OUTSIDE-LOCAL rule 30 protocol 'tcp'
    set firewall name OUTSIDE-LOCAL rule 30 recent count '4'
    set firewall name OUTSIDE-LOCAL rule 30 recent time '60'
    set firewall name OUTSIDE-LOCAL rule 30 state new 'enable'

    set firewall name OUTSIDE-LOCAL rule 31 action 'accept'
    set firewall name OUTSIDE-LOCAL rule 31 destination port '22'
    set firewall name OUTSIDE-LOCAL rule 31 protocol 'tcp'
    set firewall name OUTSIDE-LOCAL rule 31 state new 'enable'
    ```
-   Применим политики брандмауэра:
    ```shell
    set interfaces ethernet eth0 firewall in name 'OUTSIDE-IN'
    set interfaces ethernet eth0 firewall local name 'OUTSIDE-LOCAL'
    ```
-   Зафиксируем изменения, сохраним конфигурацию и выйдем из режима конфигурации:
    ```shell
    vyos@vyos# commit
    vyos@vyos# save
    Saving configuration to '/config/config.boot'...
    Done
    vyos@vyos# exit
    vyos@vyos$
    ```


#### <span class="section-num">4.1.8</span> Настройка безопасности {#настройка-безопасности}

-   Заменим системного пользователя по умолчанию:
    ```shell
    set system login user myvyosuser authentication plaintext-password mysecurepassword
    ```
-   Настроим аутентификацию на основе ключа:
    ```shell
    set system login user myvyosuser authentication public-keys myusername@mydesktop type ssh-rsa
    set system login user myvyosuser authentication public-keys myusername@mydesktop key contents_of_id_rsa.pub
    ```
-   Удалим исходного пользователя `vyos` полностью отключим аутентификацию по паролю для SSH:
    ```shell
    delete system login user vyos
    set service ssh disable-password-authentication
    ```
-   Зафиксируем изменения, сохраним конфигурацию и выйдем из режима конфигурации:
    ```shell
    vyos@vyos# commit
    vyos@vyos# save
    Saving configuration to '/config/config.boot'...
    Done
    vyos@vyos# exit
    vyos@vyos$
    ```


## <span class="section-num">5</span> Образы операционной системы {#образы-операционной-системы}

-   [GNS3. Образ VyOS]({{< relref "2022-07-14-gns3-vyos" >}})
-   [Сборка образа VyOS]({{< relref "2023-07-06-vyos-build" >}})
-   [Сборка образа VyOS. Репозиторий]({{< relref "2023-07-16-vyos-build-repository" >}})
