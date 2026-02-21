---
title: "Адресация IPv4 и IPv6. Настройка DHCPv6 для IPv6"
author: ["Dmitry S. Kulyabov"]
date: 2022-08-17T19:48:00+03:00
lastmod: 2022-08-17T20:32:00+03:00
tags: ["network", "education"]
categories: ["computer-science"]
draft: false
toc: true
type: docs
slug: "configuring-dhcpv6-ipv6"
summary: "Настройка DHCPv6 для ipv6"
menu:
  "configuring-dhcpv6-ipv6":
    parent: "nettech-gns3-lab"
    weight: 226
    identifier: "configuring-dhcpv6-ipv6"
---

Настройка DHCPv6 для IPv6. Продолжение [Адресация IPv4 и IPv6. Настройка DHCP для IPv4]({{< relref "2022-08-15-configuring-dhcp-ipv4" >}}).

<!--more-->


## <span class="section-num">1</span> Описание {#описание}


### <span class="section-num">1.1</span> Цель {#цель}

-   Овладеть принципами настройки сетей IPv6.


### <span class="section-num">1.2</span> Задачи {#задачи}

-   Настроить адресацию IPv6 на хостах и маршрутизаторе.
-   Настроить статическую маршрутизацию IPv6.


### <span class="section-num">1.3</span> Схема сети {#схема-сети}

{{< figure src="/ox-hugo/20220817194800-topology.png" caption="<span class=\"figure-number\">&#1056;&#1080;&#1089;. 1.: </span>Схема сети" >}}


### <span class="section-num">1.4</span> Исходные данные {#исходные-данные}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Таблица адресации
</div>

| Устройство     | Интерфейс | IPv6-адрес                          | Длина префикса | Шлюз по умолчанию           | DNS              |
|----------------|-----------|-------------------------------------|----------------|-----------------------------|------------------|
| username-gw-01 | eth1      | 2000::1                             | 64             | ---                         | ---              |
| username-gw-01 | eth2      | 2001::1                             | 64             | ---                         | ---              |
| PC2            | NIC       | Назначен протоколом SLAAC           | 64 (SLAAC)     | Назначен протоколом SLAAC   |                  |
| PC2            | NIC       | Назначен протоколами SLAAC и DHCPv6 | 64             | Назначен маршрутизатором R1 | 2000::1 (DHCPv6) |
| PC3            | NIC       | Назначен протоколом DHCPv6          | 64             | Назначен маршрутизатором R1 | 2001::1 (DHCPv6) |


### <span class="section-num">1.5</span> Общие сведения о сценариях настройки {#общие-сведения-о-сценариях-настройки}

-   Динамическое назначение глобальных индивидуальных IPv6-адресов можно настроить тремя способами:
    -   Только автоматическая настройка адреса без отслеживания состояния (SLAAC).
    -   DHCPv6 без отслеживания состояния.
    -   Адресация DHCPv6 с учётом состояний.
-   В случае использования SLAAC (произносится как «слэк»), сервер DHCPv6 не требуется для получения узлами IPv6-адресов.
    -   Сервер DHCPv6 можно использовать для получения дополнительной информации, необходимой узлу, например доменного имени или адреса сервера доменных имён (DNS).
    -   Когда SLAAC используется для назначения IPv6-адресов узлам, а DHCPv6 используется для получения других сетевых параметров, подобная настройка носит название DHCPv6 без отслеживания состояния.
-   При использовании DHCPv6 с отслеживанием состояния, сервер DHCP назначает всю информацию, включая IPv6-адрес узла.
-   Определение способа получения динамической IPv6-адресации зависит от установленных значений флагов, содержащихся в объявлениях маршрутизатора (сообщениях RA).


### <span class="section-num">1.6</span> Техническое обеспечение {#техническое-обеспечение}

-   В качестве сервера DHCPv6 используем маршрутизатор VyOS.
-   В качестве хоста (клиента) используем _Kali Linux CLI_.


#### <span class="section-num">1.6.1</span> Обоснование {#обоснование}

-   Клиент VPCS не поддерживает DHCPv6.


### <span class="section-num">1.7</span> Задание {#задание}

-   Мониторинг трафика производится на сетевом интерфейсе PC2.
-   Мониторинг трафика производится на сетевом интерфейсе PC3.


## <span class="section-num">2</span> Порядок выполнения {#порядок-выполнения}


### <span class="section-num">2.1</span> Настройка адресации IPv6 на маршрутизаторе {#настройка-адресации-ipv6-на-маршрутизаторе}

-   После перехода в режим конфигурации введём следующие команды:
    ```shell
    username@username-gw-01# set interfaces ethernet eth1 address '2000::1/64'
    username@username-gw-01# set interfaces ethernet eth2 address '2001::1/64'
    ```
-   Проверим конфигурацию интерфейсов:
    ```text
    username@username-gw-01# show interfaces
    ```


### <span class="section-num">2.2</span> DHCPv6 без отслеживания состояния (DHCPv6 Stateless configuration) {#dhcpv6-без-отслеживания-состояния--dhcpv6-stateless-configuration}


#### <span class="section-num">2.2.1</span> Настройка маршрутизатора {#настройка-маршрутизатора}

-   Настроим объявления о маршрутизаторах (Router Advertisements --- RA) на интерфейсе `eth1`:
    ```shell
    username@username-gw-01# set service router-advert interface eth1 prefix 2000::/64
    username@username-gw-01# set service router-advert interface eth1 other-config-flag
    ```

    -   Опция `other-config-flag` означает, что для конфигурации не адресных параметров использует протокол с сохранением состояния.
-   Добавим конфигурацию DHCP-сервера на маршрутизаторе:
    ```shell
    username@username-gw-01# set service dhcpv6-server shared-network-name username-stateless
    username@username-gw-01# set service dhcpv6-server shared-network-name username-stateless subnet 2000::0/64
    username@username-gw-01# set service dhcpv6-server shared-network-name username-stateless common-options nameserver 2000::1
    username@username-gw-01# set service dhcpv6-server shared-network-name username-stateless common-options domain-search username.net

    username@username-gw-01# commit
    username@username-gw-01# save
    ```
-   Здесь мы создали:
    -   разделяемую сеть (`shared-network-name`) `username` (следует заменить на Ваш логин).
-   Задали информацию:
    -   информация задана в общих опциях (`common-options`) для разделяемой сети;
    -   подсеть (`subnet`) `2000::/64` нам конфигурировать не нужно, поскольку никакой информации в ней не будет.


#### <span class="section-num">2.2.2</span> Проверка работоспособности {#проверка-работоспособности}

-   Подключитесь к хосту `PC2`.
-   Проверьте настройки сети:
    ```shell
    root@PC2:/# ifconfig
    root@PC2:/# route -n -A inet6
    ```
-   Пропингуйте маршрутизатор:
    ```shell
    root@PC2:/# ping 2000::1
    ```
-   Проверьте настройки DNS:
    ```shell
    root@PC2:/# cat /etc/resolv.conf
    ```
-   Получите адрес по DHCPv6:
    ```shell
    root@PC2:/# dhclient -6 -S -v eth0
    ```

    -   опция `-6`: протокол DHCPv6;
    -   опция `-S`: запрос только информации DHCPv6, не адреса;
    -   опция `-v`: подробная информация;
    -   операнд `eth0`: наименование интерфейса.
-   Проверьте настройки сети:
    ```shell
    root@PC2:/# ifconfig
    root@PC2:/# route -n -A inet6
    ```
-   Пропингуйте маршрутизатор:
    ```shell
    root@PC2:/# ping 2000::1
    ```
-   Проверьте настройки DNS:
    ```shell
    root@PC2:/# cat /etc/resolv.conf
    ```
-   Посмотрите статистику DHCP-сервера и выданные адреса:
    ```shell
    username@username-gw-01# show dhcpv6 server leases
    ```


#### <span class="section-num">2.2.3</span> Видео: Адресация IPv4 и IPv6. Настройка DHCPv6 Stateless для IPv6 {#видео-адресация-ipv4-и-ipv6-dot-настройка-dhcpv6-stateless-для-ipv6}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 6702b8ed46fa55cf77447fc691a9f7f1 >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube MXN5e1B-8TI >}}

{{< /rtab >}}
{{< /tabs >}}


### <span class="section-num">2.3</span> DHCPv6 с отслеживанием состояния (DHCPv6 Stateful configuration) {#dhcpv6-с-отслеживанием-состояния--dhcpv6-stateful-configuration}


#### <span class="section-num">2.3.1</span> Настройка маршрутизатора {#настройка-маршрутизатора}

-   Настроим объявления о маршрутизаторах (Router Advertisements --- RA) на интерфейсе `eth2`:
    ```shell
    username@username-gw-01# set service router-advert interface eth2 managed-flag
    ```

    -   Опция `managed-flag` означает, что хосты использует администрируемый (отслеживающий состояние) протокол для автоматической настройки адресов в дополнение к любым адресам, автоматически настраиваемым с помощью SLAAC.
-   Добавим конфигурацию DHCP-сервера на маршрутизаторе:
    ```shell
    username@username-gw-01# set service dhcpv6-server shared-network-name username-stateful
    username@username-gw-01# set service dhcpv6-server shared-network-name username-stateful subnet 2001::0/64
    username@username-gw-01# set service dhcpv6-server shared-network-name username-stateful subnet 2001::0/64 name-server 2001::1
    username@username-gw-01# set service dhcpv6-server shared-network-name username-stateful subnet 2001::0/64 domain-search username.net
    username@username-gw-01# set service dhcpv6-server shared-network-name username-stateful subnet 2001::0/64 address-range start 2001::100 stop 2001::199

    username@username-gw-01# commit
    username@username-gw-01# save
    ```
-   Здесь мы создали:
    -   разделяемую сеть (`shared-network-name`) `username`;
    -   подсеть (`subnet`) `2001::/64`;
    -   диапазон адресов (`range`) с именем `hosts`, содержащий адреса `2001::100` -- `2001::199`.
-   Посмотрите статистику DHCP-сервера и выданные адреса:
    ```shell
    username@username-gw-01# show dhcpv6 server leases
    ```


#### <span class="section-num">2.3.2</span> Проверка работоспособности {#проверка-работоспособности}

-   Подключитесь к хосту `PC3`.
-   Проверьте настройки сети:
    ```shell
    root@PC3:/# ifconfig
    root@PC3:/# route -n -A inet6
    ```
-   Проверьте настройки DNS:
    ```shell
    root@PC3:/# cat /etc/resolv.conf
    ```
-   Получите адрес по DHCPv6:
    ```shell
    root@PC3:/# dhclient -6 -v eth0
    ```

    -   опция `-6`: протокол DHCPv6;
    -   опция `-v`: подробная информация;
    -   операнд `eth0`: наименование интерфейса.
-   Проверьте настройки сети:
    ```shell
    root@PC3:/# ifconfig
    root@PC3:/# route -n -A inet6
    ```
-   Пропингуйте маршрутизатор:
    ```shell
    root@PC3:/# ping 2001::1
    ```
-   Проверьте настройки DNS:
    ```shell
    root@PC3:/# cat /etc/resolv.conf
    ```
-   Посмотрите статистику DHCP-сервера и выданные адреса:
    ```shell
    username@username-gw-01# show dhcpv6 server leases
    ```


#### <span class="section-num">2.3.3</span> Видео: Адресация IPv4 и IPv6. Настройка DHCPv6 Stateful для IPv6 {#видео-адресация-ipv4-и-ipv6-dot-настройка-dhcpv6-stateful-для-ipv6}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 01cffa5c0d70841abe46eb1ae129322c >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube 2sQrBsF3lms >}}

{{< /rtab >}}
{{< /tabs >}}
