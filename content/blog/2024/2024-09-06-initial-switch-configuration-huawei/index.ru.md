---
title: "Начальная конфигурация коммутатора Huawei"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-06T15:31:00+03:00
lastmod: 2025-11-20T14:10:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "initial-switch-configuration-huawei"
---

Начальная конфигурация коммутатора Huawei.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Подготовка {#подготовка}

-   На Linux для конфигурации используется Minicom.
-   Запускайте по пользователем `root`.
-   Для первоначальной конфигурации задайте ключ `-s`:
    ```shell
    minicom -s
    ```
-   Выставите параметры Скорость/Четность/Биты (Bps/Par/Bits) = 9600 8N1.
-   Укажите последовательный порт:
    -   последовательный порт: `/dev/ttyS[0-3]`;
    -   порт USB: `/dev/ttyUSB0`.
-   Итоговая конфигурация:
    ```text
    A - Последовательный порт          : /dev/ttyUSB0
    B - Размещение lock-файла          : /var/lock
    C - Программа при выходе           :
    D - Программа при запуске          :
    E - Скорость/Чётность/Биты         : 9600 8N1
    F - Аппаратное управление потоком  : Да
    G - Программное управление потоком : Нет
    ```
-   После изменений в меню выбрать "Сохранить настройки как dfl" или под своим именем.


## <span class="section-num">2</span> Базовая конфигурация {#базовая-конфигурация}


### <span class="section-num">2.1</span> Переход в режим конфигурации {#переход-в-режим-конфигурации}

-   Получаем приглашение `<HUAWEI>`.
-   Переходим в режим конфигурации командой `system-view`.
-   Приглашение меняется на `[HUAWEI]`:
    ```shell
    <HUAWEI>system-view
    [HUAWEI]
    ```


### <span class="section-num">2.2</span> Зададим имя устройства {#зададим-имя-устройства}

-   Имя устройства имеет вид: &lt;тип устройства&gt;-&lt;помещение&gt;-&lt;номер устройства&gt;, например `sw-103-1`.
-   Зададим имя устройства:
    ```shell
    [HUAWEI]#sysname sw-103-1
    ```


### <span class="section-num">2.3</span> Административный пользователь {#административный-пользователь}

-   Зададим пользователя admin и пароль для него:
    ```shell
    [sw-103-1]aaa
    [sw-103-1-aaa]local-user admin password irreversible-cipher <пароль>
    ```
-   Назначаем пользователю уровень привилегий (15 самый высокий):
    ```shell
    [sw-103-1-aaa]local-user admin privilege level 15
    ```
-   Включаем доступ по SSH для пользователя:
    ```shell
    [sw-103-1-aaa]local-user admin service-type telnet terminal ssh
    ```
-   Отключаем запрос смены пароля по истечению определённого промежутка времени (опционально):
    ```shell
    [sw-103-1-aaa]undo local-aaa-user password policy administrator
    [sw-103-1-aaa]quit
    ```


### <span class="section-num">2.4</span> Настройка ssh {#настройка-ssh}

-   Включим ssh:
    ```shell
    [sw-103-1]stelnet server enable
    [sw-103-1]ssh server-source all-interface
    [sw-103-1]ssh authentication-type default password
    ```
-   Создадим ключ (необходимо, чтобы было настроено имя домена):
    ```shell
    [sw-103-1]rsa local-key-pair create
    ```
-   Задаём алгоритмы ssh:
    ```shell
    [sw-103-1]ssh server cipher aes256_ctr aes128_ctr
    [sw-103-1]ssh server hmac sha2_256
    [sw-103-1]ssh server key-exchange dh_group16_sha512 dh_group15_sha512 dh_group14_sha256 dh_group_exchange_sha256
    [sw-103-1]ssh client cipher aes256_ctr aes128_ctr
    [sw-103-1]ssh client hmac sha2_256
    [sw-103-1]ssh client key-exchange dh_group16_sha512 dh_group15_sha512 dh_group14_sha256 dh_group_exchange_sha256
    [sw-103-1]ssh server dh-exchange min-len 2048
    [sw-103-1]ssh server publickey rsa_sha2_512 rsa_sha2_256 ecc rsa
    ```
-   Задаём протокол для подключения:
    ```shell
    [sw-103-1]user-interface vty 0 4
    [sw-103-1-ui-vty0-4]authentication-mode aaa
    [sw-103-1-ui-vty0-4]protocol inbound ssh
    [sw-103-1-ui-vty0-4]quit
    ```


### <span class="section-num">2.5</span> DHCP snooping {#dhcp-snooping}

-   [DHCP snooping]({{< relref "2023-09-05-dhcp-snooping" >}})
-   Для использования DHCP snooping нам потребуется включить на коммутаторе глобально DHCP и DHCP snooping:
    ```shell
    [sw-103-1]dhcp enable
    [sw-103-1]dhcp snooping enable
    ```


### <span class="section-num">2.6</span> Uplink интерфейс {#uplink-интерфейс}

-   Сделаем последний порт транковым:
    ```shell
    [sw-103-1]interface GigabitEthernet1/0/48
    [sw-103-1-GigabitEthernet0/0/48]port link-type trunk
    [sw-103-1-GigabitEthernet0/0/48]port trunk allow-pass vlan all
    [sw-103-1-GigabitEthernet0/0/48]dhcp snooping trusted
    [sw-103-1-GigabitEthernet0/0/48]quit
    ```
-   Сделали порт доверенным для _DHCP snooping_.


### <span class="section-num">2.7</span> Сетевые настройки {#сетевые-настройки}

-   Зададим адрес 192.168.0.1/24,
    ```shell
    [sw-103-1]interface Vlanif 2
    [sw-103-1-Vlanif10]ip address 192.168.1.10 24
    [sw-103-1-Vlanif10]quit
    ```
-   Зададим шлюз 192.168.0.254:
    ```shell
    [sw-103-1]ip route-static 0.0.0.0 0.0.0.0 192.168.0.254
    ```


### <span class="section-num">2.8</span> Настройка VCMP {#настройка-vcmp}

-   [Huawei. Протокол VCMP]({{< relref "2024-09-21-huawei-vcmp" >}})
-   Подключаем как клиента:
    ```shell
    [sw-103-1]vcmp role client
    [sw-103-1]vcmp domain <domain>
    [sw-103-1]vcmp authentication sha2-256 password <пароль>
    ```


### <span class="section-num">2.9</span> Настройка lldp {#настройка-lldp}

-   Подключим поддержку протокола lldp:
    ```shell
    [sw-103-1]lldp enable
    ```
-   Подключим cdp на все порты:
    ```shell
    [sw-103-1]interface range GigabitEthernet 0/0/1 to GigabitEthernet 0/0/48
    [sw-103-1-port-group]lldp compliance cdp receive
    [sw-103-1-port-group]quit
    ```


### <span class="section-num">2.10</span> Настройка других портов {#настройка-других-портов}

-   Настроим другие порты для подключения клиентских устройств:
    ```shell
    [sw-103-1]interface range GigabitEthernet 0/0/1 to GigabitEthernet 0/0/46
    [sw-103-1-port-group]port link-type access
    [sw-103-1-port-group]port default vlan 100
    [sw-103-1-port-group]quit
    ```


### <span class="section-num">2.11</span> Сохранение конфигурации {#сохранение-конфигурации}

-   Сохраните конфигурацию:
    ```shell
    <sw-103-1>save
    ```


## <span class="section-num">3</span> Добавление в DNS {#добавление-в-dns}

-   Необходимо добавить коммутатор в DNS.


### <span class="section-num">3.1</span> nsupdate {#nsupdate}

-   [nsupdate: динамический редактор зон DNS]({{< relref "2023-10-28-nsupdate-dynamic-dns-editor" >}})
-   Добавьте адрес коммутатора в DNS:
    ```shell
    echo -e "update add sw-103-1.example.com 86400 a 192.168.0.1\nshow\nsend" | nsupdate -v -k /etc/named/keys/example.com.key
    ```


## <span class="section-num">4</span> Подключение к системе мониторинга {#подключение-к-системе-мониторинга}


### <span class="section-num">4.1</span> Настройка SNMP {#настройка-snmp}

-   Посмотреть статус SNMP:
    ```shell
    <sw-103-1>display snmp-agent sys-info
    ```
-   Укажем версию протокола по умолчанию для работы snmp:
    ```shell
    [sw-103-1]snmp-agent sys-info version v2c
    ```
-   Удалим 3 версию:
    ```shell
    [sw-103-1]undo snmp-agent sys-info version v3
    ```
-   Настроим представление MIB:
    ```shell
    [sw-103-1]snmp-agent mib-view included iso-view iso
    ```
-   Активируем на всех интерфейсах:
    ```shell
    [sw-103-1]snmp-agent protocol source-status all-interface
    ```
-   Чтобы можно было указать простые snmp комьюнити введем команду:
    ```shell
    [sw-103-1]snmp-agent community complexity-check disable
    ```

-   Настройте доступ к серверу мониторинга по SNMP.
-   Пусть сервер мониторинга имеет адрес: 192.168.0.5.
-   Имя коммьюнити для чтения: rocom.
    ```shell
    [sw-103-1]acl name SNMP 3999
    [sw-103-1-acl-adv-SNMP]rule 1 permit ip source 192.168.0.5 0
    [sw-103-1-acl-adv-SNMP]quit
    [sw-103-1]snmp community read rocom acl SNMP
    ```
-   Добавьте коммутатор в свой DNS.


### <span class="section-num">4.2</span> Пользователь для бекапа конфига {#пользователь-для-бекапа-конфига}

-   Добавим пользователя для бекапа конфига:
    ```shell
    [sw-103-1]aaa
    [sw-103-1-aaa]local-user readconf password irreversible-cipher <пароль>
    ```
-   Назначаем пользователю уровень привилегий (15 самый высокий):
    ```shell
    [sw-103-1-aaa]local-user readconf privilege level 15
    ```
-   Включаем доступ по SSH для пользователя:
    ```shell
    [sw-103-1-aaa]local-user readconf service-type telnet terminal ssh
    [sw-103-1-aaa]quit
    ```


### <span class="section-num">4.3</span> Подключение к Observium {#подключение-к-observium}

-   Подключитесь к Observium.
-   Добавьте коммутатор в список наблюдения в Observium:
    ```shell
    [root@observium ~]# /opt/observium/add_device.php sw-103-1 rocom
    [root@observium ~]# /opt/observium/discovery.php -h sw-103-1; /opt/observium/poller.php -h sw-103-1
    ```


### <span class="section-num">4.4</span> Подключение к Librenms {#подключение-к-librenms}

-   Подключитесь к Librenms (см. [Система мониторинга LibreNMS]({{< relref "2023-03-20-librenms-monitoring-system" >}})).
-   Добавьте коммутатор в список наблюдения в Librenms:
    ```shell
    sudo -u librenms env "PATH=$PATH" lnms device:add sw-103-1 -c rocom
    sudo -u librenms env "PATH=$PATH" lnms device:poll sw-103-1
    ```

-   Если есть в базе данное устройство, но под другим именем, то можно его переименовать:
    ```shell
    sudo -u librenms env "PATH=$PATH" lnms device:rename <old hostname> <new hostname>
    ```
