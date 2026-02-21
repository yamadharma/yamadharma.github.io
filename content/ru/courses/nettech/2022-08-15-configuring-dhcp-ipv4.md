---
title: "Адресация IPv4 и IPv6. Настройка DHCP для IPv4"
author: ["Dmitry S. Kulyabov"]
date: 2022-08-15T20:21:00+03:00
lastmod: 2024-06-19T15:25:00+03:00
tags: ["network", "education"]
categories: ["computer-science"]
draft: false
toc: true
type: docs
slug: "configuring-dhcp-ipv4"
summary: "Настройка DHCP для IPv4"
menu:
  "configuring-dhcp-ipv4":
    parent: "nettech-gns3-lab"
    weight: 225
    identifier: "configuring-dhcp-ipv4"
---

Настройка DHCP для IPv4.

<!--more-->


## <span class="section-num">1</span> Описание {#описание}


### <span class="section-num">1.1</span> Цель {#цель}

-   Получение навыков настройки службы DHCP на сетевом оборудовании для распределения адресов IPv4.


### <span class="section-num">1.2</span> Задачи {#задачи}

-   Сделать предварительную настройку маршрутизатора.
    -   Удалить стандартное имя системного пользователя маршрутизатора.
    -   Настроить интерфейс маршрутизатора: `10.0.0.1/24`.
-   Поднять на маршрутизаторе DHCP-сервис по распределению IPv4-адресов из диапазона `10.0.0.2` -– `10.0.0.253`.
-   Настроить получение адреса по DHCP на хосте.
-   Исследовать пакеты DHCP.


### <span class="section-num">1.3</span> Схема сети {#схема-сети}

{{< figure src="/ox-hugo/20220815202100-topology.png" caption="<span class=\"figure-number\">&#1056;&#1080;&#1089;. 1.: </span>Схема сети" >}}


### <span class="section-num">1.4</span> Исходные данные {#исходные-данные}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Таблица адресации
</div>

| Устройство     | Интерфейс | IPv4-адрес               | Длина префикса | Шлюз по умолчанию | DNS             |
|----------------|-----------|--------------------------|----------------|-------------------|-----------------|
| username-gw-01 | eth0      | 10.0.0.1                 | 24             | ---               | ---             |
| PC1            | NIC       | Назначен протоколом DHCP | 24 (DHCP)      | 10.0.0.1 (DHCP)   | 10.0.0.1 (DHCP) |


### <span class="section-num">1.5</span> Техническое обеспечение {#техническое-обеспечение}

-   В качестве сервера DHCP используем маршрутизатор VyOS.
-   В качестве хоста (клиента) используем VPCS.


### <span class="section-num">1.6</span> Задание {#задание}

-   Мониторинг трафика производится на сетевом интерфейсе PC1.


## <span class="section-num">2</span> Порядок выполнения {#порядок-выполнения}


### <span class="section-num">2.1</span> Настройка образа VyOS {#настройка-образа-vyos}


#### <span class="section-num">2.1.1</span> Вход в систему {#вход-в-систему}

-   Для входа в систему используем пользователя `vyos` и пароль `vyos`.


#### <span class="section-num">2.1.2</span> Установка образа {#установка-образа}

-   После загрузки установите систему на диск:
    ```shell
    vyos@vyos:~$ install image
    ```
-   После этого перегрузите маршрутизатор:
    ```shell
    vyos@vyos:~$ reboot
    ```


#### <span class="section-num">2.1.3</span> Режим конфигурации {#режим-конфигурации}

-   В рабочем режиме в командной строке отображается символ `$`.
-   В режиме конфигурации в командной строке отображается `#`:
    ```shell
    vyos@vyos$ configure
    vyos@vyos#
    ```


#### <span class="section-num">2.1.4</span> Сохранение {#сохранение}

-   Посмотреть, какие изменения внесены:
    ```shell
    vyos@vyos# compare
    ```
-   После каждого изменения конфигурации необходимо применить изменения:
    ```shell
    vyos@vyos# commit
    ```
-   В конце нужно сохранить конфигурацию:
    ```shell
    vyos@vyos# save
    ```


#### <span class="section-num">2.1.5</span> Имя устройства {#имя-устройства}

-   Имя хоста может содержать до 63 символов. Имя хоста должно начинаться и заканчиваться буквой или цифрой и содержать в качестве внутренних символов только буквы, цифры или дефис.
-   Установите имя хоста в `username-gw-01`, где `username` --- имя учётной записи:
    ```shell
    set system host-name username-gw-01
    ```
-   Доменное имя должно начинаться и заканчиваться буквой или цифрой и содержать в качестве внутренних символов только буквы, цифры или дефис.
-   Установите доменное имя в `username.net`:
    ```shell
    set system domain-name username.net
    ```


#### <span class="section-num">2.1.6</span> Замена системного пользователя {#замена-системного-пользователя}

-   Заменим системного пользователя по умолчанию:
    ```shell
    set system login user <username> authentication plaintext-password <mysecurepassword>

    commit
    save
    ```
-   Отлогинимся:
    ```shell
    # exit
    $ exit
    ```
-   Залогинимся под новым пользователем.
-   Удалим исходного пользователя `vyos`:
    ```shell
    delete system login user vyos
    ```
-   Зафиксируем изменения, сохраним конфигурацию и выйдем из режима конфигурации:
    ```shell
    # commit
    # save

    # exit
    $
    ```


### <span class="section-num">2.2</span> Настройка адресации IPv4 на маршрутизаторе {#настройка-адресации-ipv4-на-маршрутизаторе}

-   Интерфейс `eth0`. Использует статический IP-адрес `10.0.0.1/24`.
-   После перехода в режим конфигурации введём следующие команды:
    ```shell
    username@username-gw-01# set interfaces ethernet eth0 address '10.0.0.1/24'
    ```


### <span class="section-num">2.3</span> Настройка адресации DHCP на маршрутизаторе {#настройка-адресации-dhcp-на-маршрутизаторе}

-   Добавим конфигурацию DHCP-сервера на маршрутизаторе:
    ```shell
    username@username-gw-01# set service dhcp-server shared-network-name username domain-name username.net
    username@username-gw-01# set service dhcp-server shared-network-name username name-server 10.0.0.1
    username@username-gw-01# set service dhcp-server shared-network-name username subnet 10.0.0.0/24 default-router 10.0.0.1
    username@username-gw-01# set service dhcp-server shared-network-name username subnet 10.0.0.0/24 range hosts start 10.0.0.2
    username@username-gw-01# set service dhcp-server shared-network-name username subnet 10.0.0.0/24 range hosts stop 10.0.0.253

    username@username-gw-01# commit
    username@username-gw-01# save
    ```
-   Здесь мы создали:
    -   разделяемую сеть (`shared-network-name`) `username`;
    -   подсеть (`subnet`) `10.0.0.0/24`;
    -   диапазон адресов (`range`) с именем `hosts`, содержащий адреса `10.0.0.2`--`10.0.0.253`.
-   Посмотрите статистику DHCP-сервера и выданные адреса:
    ```shell
    username@username-gw-01$ show dhcp server statistics
    username@username-gw-01$ show dhcp server leases
    ```


### <span class="section-num">2.4</span> Настройка хоста {#настройка-хоста}

-   `PC1`:
    ```shell
    PC1> ip dhcp -d
    PC1> save
    ```

    -   Опцию `-d` мы добавили, чтобы видеть декодированные запросы DHCP.
-   Проверьте конфигурацию IPv4 на узле:
    ```shell
    PC1> show ip
    ```


### <span class="section-num">2.5</span> Проверка работоспособности {#проверка-работоспособности}

-   Пропингуйте маршрутизатор с хоста:
    ```shell
    PC1> ping 10.0.0.1
    ```
-   Посмотрите статистику DHCP-сервера и выданные адреса:
    ```shell
    username@username-gw-01$ show dhcp server statistics
    username@username-gw-01$ show dhcp server leases
    ```
-   Посмотрите журнал работы DHCP-сервера:
    ```shell
    username@username-gw-01$ show log | grep dhcp
    ```


## <span class="section-num">3</span> Видео: Адресация IPv4 и IPv6. Настройка DHCP для IPv4 {#видео-адресация-ipv4-и-ipv6-dot-настройка-dhcp-для-ipv4}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 371ec8f0d7f915d84eac93e9ad3d1150 >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube M_x5hbQ5PYU >}}

{{< /rtab >}}
{{< /tabs >}}
