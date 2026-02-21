---
title: "DHCP. Установка сервера DHCP Kea"
author: ["Dmitry S. Kulyabov"]
date: 2024-05-07T11:39:00+03:00
lastmod: 2025-09-12T19:04:00+03:00
tags: ["network", "linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "dhcp-server-installation"
---

Установка сервера DHCP ISC Kea.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.isc.org/kea/>
-   Репозиторий:
    -   <https://gitlab.isc.org/isc-projects/kea>
    -   <https://github.com/isc-projects/kea>
-   Документация: <https://kea.readthedocs.io/en/latest/index.html>


### <span class="section-num">1.1</span> Особенности {#особенности}

-   Модульная конструкция компонентов
    -   Расширяется с помощью модулей-хуков.
    -   Дистрибутив Kea включает отдельные демоны для сервера DHCPv4, сервера DHCPv6 и модуля динамического DNS (DDNS).
-   Онлайн-реконфигурация с помощью REST API.
    -   Kea использует файл конфигурации JSON, который можно изменить удалённо без остановки и перезапуска сервера.
-   Панель управления через веб-интерфейс.
-   Поддерживает базы данных MySQL, PostgreSQL:
    -   упрощает интеграцию с другими системами;
    -   можно использовать один и тот же сервер резервирования хостов для нескольких DHCP-серверов;
    -   администрирование глобальных параметров из централизованной системы настройки.


## <span class="section-num">2</span> Опции DHCP {#опции-dhcp}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Список стандартных опций DHCPv4
</div>

| Название                               | Код | Type                                              | Массив | Returned if not requested? |
|----------------------------------------|-----|---------------------------------------------------|--------|----------------------------|
| time-offset                            | 2   | int32                                             | false  | false                      |
| routers                                | 3   | ipv4-address                                      | true   | true                       |
| time-servers                           | 4   | ipv4-address                                      | true   | false                      |
| name-servers                           | 5   | ipv4-address                                      | true   | false                      |
| domain-name-servers                    | 6   | ipv4-address                                      | true   | true                       |
| log-servers                            | 7   | ipv4-address                                      | true   | false                      |
| cookie-servers                         | 8   | ipv4-address                                      | true   | false                      |
| lpr-servers                            | 9   | ipv4-address                                      | true   | false                      |
| impress-servers                        | 10  | ipv4-address                                      | true   | false                      |
| resource-location-servers              | 11  | ipv4-address                                      | true   | false                      |
| boot-size                              | 13  | uint16                                            | false  | false                      |
| merit-dump                             | 14  | string                                            | false  | false                      |
| domain-name                            | 15  | fqdn                                              | false  | true                       |
| swap-server                            | 16  | ipv4-address                                      | false  | false                      |
| root-path                              | 17  | string                                            | false  | false                      |
| extensions-path                        | 18  | string                                            | false  | false                      |
| ip-forwarding                          | 19  | boolean                                           | false  | false                      |
| non-local-source-routing               | 20  | boolean                                           | false  | false                      |
| policy-filter                          | 21  | ipv4-address                                      | true   | false                      |
| max-dgram-reassembly                   | 22  | uint16                                            | false  | false                      |
| default-ip-ttl                         | 23  | uint8                                             | false  | false                      |
| path-mtu-aging-timeout                 | 24  | uint32                                            | false  | false                      |
| path-mtu-plateau-table                 | 25  | uint16                                            | true   | false                      |
| interface-mtu                          | 26  | uint16                                            | false  | false                      |
| all-subnets-local                      | 27  | boolean                                           | false  | false                      |
| broadcast-address                      | 28  | ipv4-address                                      | false  | false                      |
| perform-mask-discovery                 | 29  | boolean                                           | false  | false                      |
| mask-supplier                          | 30  | boolean                                           | false  | false                      |
| router-discovery                       | 31  | boolean                                           | false  | false                      |
| router-solicitation-address            | 32  | ipv4-address                                      | false  | false                      |
| static-routes                          | 33  | ipv4-address                                      | true   | false                      |
| trailer-encapsulation                  | 34  | boolean                                           | false  | false                      |
| arp-cache-timeout                      | 35  | uint32                                            | false  | false                      |
| ieee802-3-encapsulation                | 36  | boolean                                           | false  | false                      |
| default-tcp-ttl                        | 37  | uint8                                             | false  | false                      |
| tcp-keepalive-interval                 | 38  | uint32                                            | false  | false                      |
| tcp-keepalive-garbage                  | 39  | boolean                                           | false  | false                      |
| nis-domain                             | 40  | string                                            | false  | false                      |
| nis-servers                            | 41  | ipv4-address                                      | true   | false                      |
| ntp-servers                            | 42  | ipv4-address                                      | true   | false                      |
| vendor-encapsulated-options            | 43  | empty                                             | false  | false                      |
| netbios-name-servers                   | 44  | ipv4-address                                      | true   | false                      |
| netbios-dd-server                      | 45  | ipv4-address                                      | true   | false                      |
| netbios-node-type                      | 46  | uint8                                             | false  | false                      |
| netbios-scope                          | 47  | string                                            | false  | false                      |
| font-servers                           | 48  | ipv4-address                                      | true   | false                      |
| x-display-manager                      | 49  | ipv4-address                                      | true   | false                      |
| dhcp-option-overload                   | 52  | uint8                                             | false  | false                      |
| dhcp-server-identifier                 | 54  | ipv4-address                                      | false  | true                       |
| dhcp-message                           | 56  | string                                            | false  | false                      |
| dhcp-max-message-size                  | 57  | uint16                                            | false  | false                      |
| vendor-class-identifier                | 60  | hex                                               | false  | false                      |
| nwip-domain-name                       | 62  | string                                            | false  | false                      |
| nwip-suboptions                        | 63  | hex                                               | false  | false                      |
| nisplus-domain-name                    | 64  | string                                            | false  | false                      |
| nisplus-servers                        | 65  | ipv4-address                                      | true   | false                      |
| tftp-server-name                       | 66  | string                                            | false  | false                      |
| boot-file-name                         | 67  | string                                            | false  | false                      |
| mobile-ip-home-agent                   | 68  | ipv4-address                                      | true   | false                      |
| smtp-server                            | 69  | ipv4-address                                      | true   | false                      |
| pop-server                             | 70  | ipv4-address                                      | true   | false                      |
| nntp-server                            | 71  | ipv4-address                                      | true   | false                      |
| www-server                             | 72  | ipv4-address                                      | true   | false                      |
| finger-server                          | 73  | ipv4-address                                      | true   | false                      |
| irc-server                             | 74  | ipv4-address                                      | true   | false                      |
| streettalk-server                      | 75  | ipv4-address                                      | true   | false                      |
| streettalk-directory-assistance-server | 76  | ipv4-address                                      | true   | false                      |
| user-class                             | 77  | hex                                               | false  | false                      |
| slp-directory-agent                    | 78  | record (boolean, ipv4-address)                    | true   | false                      |
| slp-service-scope                      | 79  | record (boolean, string)                          | false  | false                      |
| nds-server                             | 85  | ipv4-address                                      | true   | false                      |
| nds-tree-name                          | 86  | string                                            | false  | false                      |
| nds-context                            | 87  | string                                            | false  | false                      |
| bcms-controller-names                  | 88  | fqdn                                              | true   | false                      |
| bcms-controller-address                | 89  | ipv4-address                                      | true   | false                      |
| client-system                          | 93  | uint16                                            | true   | false                      |
| client-ndi                             | 94  | record (uint8, uint8, uint8)                      | false  | false                      |
| uuid-guid                              | 97  | record (uint8, hex)                               | false  | false                      |
| uap-servers                            | 98  | string                                            | false  | false                      |
| geoconf-civic                          | 99  | hex                                               | false  | false                      |
| pcode                                  | 100 | string                                            | false  | false                      |
| tcode                                  | 101 | string                                            | false  | false                      |
| netinfo-server-address                 | 112 | ipv4-address                                      | true   | false                      |
| netinfo-server-tag                     | 113 | string                                            | false  | false                      |
| default-url                            | 114 | string                                            | false  | false                      |
| auto-config                            | 116 | uint8                                             | false  | false                      |
| name-service-search                    | 117 | uint16                                            | true   | false                      |
| subnet-selection                       | 118 | ipv4-address                                      | false  | false                      |
| domain-search                          | 119 | fqdn                                              | true   | false                      |
| vivco-suboptions                       | 124 | hex                                               | false  | false                      |
| vivso-suboptions                       | 125 | hex                                               | false  | false                      |
| pana-agent                             | 136 | ipv4-address                                      | true   | false                      |
| v4-lost                                | 137 | fqdn                                              | false  | false                      |
| capwap-ac-v4                           | 138 | ipv4-address                                      | true   | false                      |
| sip-ua-cs-domains                      | 142 | fqdn                                              | true   | false                      |
| rdnss-selection                        | 146 | record (uint8, ipv4-address, ipv4-address, fqdn)  | true   | false                      |
| v4-portparams                          | 159 | record (uint8, psid)                              | false  | false                      |
| v4-captive-portal                      | 160 | string                                            | false  | false                      |
| option-6rd                             | 212 | record (uint8, uint8, ipv6-address, ipv4-address) | true   | false                      |
| v4-access-domain                       | 213 | fqdn                                              | false  | false                      |

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 2:</span>
  Список стандартных типов опций DHCP
</div>

| Тип          | Описание                                                                                                                                                                                             |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hex          | An arbitrary string of bytes, specified as a set of hexadecimal digits.                                                                                                                              |
| boolean      | Boolean value with allowed values true or false                                                                                                                                                      |
| empty        | No value, data is carried in suboptions                                                                                                                                                              |
| fqdn         | Fully qualified domain name (e.g. www.example.com)                                                                                                                                                   |
| ipv4-address | IPv4 address in the usual dotted-decimal notation (e.g. 192.0.2.1)                                                                                                                                   |
| ipv6-address | IPv6 address in the usual colon notation (e.g. 2001:db8::1)                                                                                                                                          |
| ipv6-prefix  | IPv6 prefix and prefix length specified using CIDR notation, e.g. 2001:db8:1::/64. This data type is used to represent an 8-bit field conveying a prefix length and the variable length prefix value |
| psid         | PSID and PSID length separated by a slash                                                                                                                                                            |
| record       | Structured data that may be comprised of any types (except "record" and "empty"). The array flag applies to the last field only.                                                                     |
| string       | Any text                                                                                                                                                                                             |
| tuple        | A length encoded as a 8 (16 for DHCPv6) bit unsigned integer followed by a string of this length                                                                                                     |
| uint8        | 8 bit unsigned integer with allowed values 0 to 255                                                                                                                                                  |
| uint16       | 16 bit unsigned integer with allowed values 0 to 65535                                                                                                                                               |
| uint32       | 32 bit unsigned integer with allowed values 0 to 4294967295                                                                                                                                          |
| int8         | 8 bit signed integer with allowed values -128 to 127                                                                                                                                                 |
| int16        | 16 bit signed integer with allowed values -32768 to 32767                                                                                                                                            |
| int32        | 32 bit signed integer with allowed values -2147483648 to 2147483647                                                                                                                                  |


## <span class="section-num">3</span> Установка {#установка}

-   Устанавливаем сервер Linux (см. [Rocky Linux. Установка сервера]({{< relref "2022-08-12-rockylinux-server-installation" >}})).


### <span class="section-num">3.1</span> Установка из репозитория дистрибутива {#установка-из-репозитория-дистрибутива}


#### <span class="section-num">3.1.1</span> Rocky Linux {#rocky-linux}

-   Rocky Linux поддерживает Kea DHCP начиная с версии 10.
    ```shell
    dnf -y install kea
    ```


### <span class="section-num">3.2</span> Ручная установка {#ручная-установка}


#### <span class="section-num">3.2.1</span> Репозиторий RockyLinux {#репозиторий-rockylinux}

-   Текущая версия в репозитории: 2.2.x.
-   В версии 2.3.2 изменили систему именования.
-   Если в дальнейше планируется обновление, возможно стоит использовать репозитории ISC.
-   Подключаем репозиторий _EPEL_:
    ```shell
    dnf config-manager --set-enabled crb
    dnf -y install epel-release
    ```
-   Устанавливаем сервер _Kea_:
    ```shell
    dnf -y install kea kea-hooks
    ```


#### <span class="section-num">3.2.2</span> Репозиторий ISC {#репозиторий-isc}

-   Текущая стабильная версия в репозитории: 2.6.x.

<!--list-separator-->

1.  Kea-2.6

    -   Подключаем репозиторий:
        ```shell
        curl -1sLf 'https://dl.cloudsmith.io/public/isc/kea-2-6/setup.rpm.sh' | sudo -E bash
        ```
    -   Отключите старые репозитории, если они были установлены:
        ```shell
        dnf config-manager --disable isc-kea-2-4 isc-kea-2-4-noarch isc-kea-2-4-source
        dnf clean all
        ```
    -   Проверьте, что репозитории отключены:
        ```shell
        dnf repolist
        ```
    -   Устанавливаем сервер _Kea_:
        ```shell
        dnf -y install isc-kea isc-kea-hooks
        ```

<!--list-separator-->

2.  Kea-2.4

    -   Подключаем репозиторий:
        ```shell
        curl -1sLf 'https://dl.cloudsmith.io/public/isc/kea-2-4/setup.rpm.sh' | sudo -E bash
        ```
    -   Устанавливаем сервер _Kea_:
        ```shell
        dnf -y install isc-kea isc-kea-hooks
        ```


#### <span class="section-num">3.2.3</span> Инструментарий миграции keama {#инструментарий-миграции-keama}

-   При необходимости миграции с реализации ISC DHCP на ISC KEA можно установить помощник миграции.
-   Документация:
    -   <https://gitlab.isc.org/isc-projects/dhcp/-/wikis/kea-migration-assistant>
    -   <https://kb.isc.org/docs/migrating-from-isc-dhcp-to-kea-dhcp-using-the-migration-assistant>
-   Репозиторий: <https://gitlab.isc.org/isc-projects/dhcp/-/tree/master/keama>
-   Бинарные сборки:
    -   <https://cloudsmith.io/~isc/repos/keama/packages/>
    -   заблокирован доступ из России
-   Подключаем репозиторий бинарных файлов:
    ```shell
    curl -1sLf 'https://dl.cloudsmith.io/public/isc/keama/setup.rpm.sh' | sudo -E bash
    ```
-   Устанавливаем сервер _Kea_:
    ```shell
    dnf -y install isc-dhcp-keama
    ```


## <span class="section-num">4</span> Подготовка {#подготовка}


### <span class="section-num">4.1</span> Брандмауэр {#брандмауэр}

-   Сконфигурируем брандмауэр:
    ```shell
    firewall-cmd --add-service=dhcp --permanent
    firewall-cmd --reload
    ```


## <span class="section-num">5</span> Подготовка базы данных {#подготовка-базы-данных}


### <span class="section-num">5.1</span> PostgreSQL {#postgresql}

-   Установка базы данных:
    ```shell
    dnf install postgresql-server
    ```
-   Проверьте временную зону сервера:
    ```shell
    date +%Z
    ```
-   Рекомендуется использовать временную зону `UTC`.
-   Инициализируйте базу данных:
    ```shell
    postgresql-setup --initdb
    ```
-   Запустим базу данных:
    ```shell
    systemctl enable --now postgresql.service
    ```


#### <span class="section-num">5.1.1</span> Создание базы данных {#создание-базы-данных}

-   Подключимся к базе данных:
    ```shell
    sudo -i -u postgres psql postgres
    ```
-   Проверим временную зону базы:
    ```shell
    show timezone;
    SELECT * FROM pg_timezone_names WHERE name = current_setting('TIMEZONE');
    ```
-   Настройки временной зоны для postgresql находятся в файле `/var/lib/pgsql/data/postgresql.conf`:
    ```conf-unix
    timezone = 'Etc/UTC'
    ```
-   Можно использовать следующие названия:
    -   `database-name` : `kea`;
    -   `user-name` :  `kea`;
    -   `password` : сгенерите нужный пароль.
-   Создадим базу данных:
    ```shell
    CREATE DATABASE database-name;
    ```
-   Создадим пользователя и пароль для взаимодействия с базой:
    ```shell
    CREATE USER user-name WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE database-name TO user-name;
    ```
-   Выйдем из интерфейса базы данных:
    ```shell
    \q
    ```


#### <span class="section-num">5.1.2</span> Заполнение базы данных {#заполнение-базы-данных}

-   Настроим доступ к базе данных в файле `/var/lib/pgsql/data/pg_hba.conf`.
-   Добавьте эти записи до других записей:
    ```conf-unix
    local   database-name    user-name                                 password
    host    database-name    user-name          127.0.0.1/32           password
    host    database-name    user-name          ::1/128                password
    ```
-   Перезагрузите postgresql:
    ```shell
    systemctl restart postgresql.service
    ```

<!--list-separator-->

1.  Загрузка значений вручную

    -   Загрузим значения в базу данных:
        ```shell
        psql -d database-name -U user-name -f /usr/share/kea/scripts/pgsql/dhcpdb_create.pgsql
        ```

<!--list-separator-->

2.  Загрузка значений через `kea-admin`

    -   Загрузим значения в базу данных:
        ```shell
        kea-admin db-init pgsql -u database-user -p database-password -n database-name
        ```


#### <span class="section-num">5.1.3</span> Обновление базы данных {#обновление-базы-данных}

-   При переходе с предыдущей версии `kea` надо обновить базу данных.
-   Проверьте текущую версию базы данных:
    ```shell
    kea-admin db-version pgsql -u database-user -p database-password -n database-name
    ```
-   Обновите базу (при необходимости):
    ```shell
    kea-admin db-upgrade pgsql -u database-user -p database-password -n database-name
    ```


### <span class="section-num">5.2</span> Миграция с ISC DHCP на ISC Kea {#миграция-с-isc-dhcp-на-isc-kea}

-   Преобразуем конфигурационные файлы:
    ```shell
    keama -4 -i dhcpd.conf -o kea-dhcp4.conf
    ```


### <span class="section-num">5.3</span> Тьюнинг базы данных {#тьюнинг-базы-данных}

-   Отключите синхронные коммиты.
-   Можно отключить в базе данных:
    ```shell
    sudo -i -u postgres psql postgres
    ALTER SYSTEM SET synchronous_commit=OFF;
    \q
    ```
-   Можно задать в файле конфигурации `/var/lib/pgsql/data/postgresql.conf`:
    ```conf-unix
    synchronous_commit = off
    ```


### <span class="section-num">5.4</span> Конфигурация базы данных для Kea {#конфигурация-базы-данных-для-kea}

-   Добавим конфигурацию базы данных:
    ```js-json
    "Dhcp4": {
        "lease-database": {
            "type": "postgresql",
            "name": "database_name",
            "host" : "localhost",
            "user": "user_name",
            "password": "password"
        },

        "hosts-database": {
            "type": "postgresql",
            "name": "database_name",
            "host" : "localhost",
            "user": "user_name",
            "password": "password"
        },
    }
    ```


## <span class="section-num">6</span> Виртуальные интерфейсы {#виртуальные-интерфейсы}

-   Для подключения к сети использовал интерфейсы VLAN (см. [Linux. Настройка vlan]({{< relref "2024-05-13-linux-vlan-configuration" >}}))


### <span class="section-num">6.1</span> Миграция интерфейсов {#миграция-интерфейсов}

-   Файлы описания интерфейсов на старой системе имеют следующий вид (`/etc/sysconfig/network-scripts/ifcfg-eth1.200`):
    ```conf-unix
    VLAN=yes
    DEVICE=eth1.200
    BOOTPROTO=none
    ONBOOT=yes
    TYPE=Ethernet
    IPADDR=10.200.0.2
    NETMASK=255.255.0.0
    NETWORK=10.200.0.0
    BROADCAST=10.200.255.255
    ```
-   Для миграции сделал набор скриптов.
-   Скрипт для извлечения параметров интерфейсов (`mk-if-list`):
    ```bash
    #!/bin/bash

    OUTFILE=iflist
    [[ -f ${OUTFILE} ]] && rm ${OUTFILE}

    for i in ifcfg-eth*.*
    do
            vlan_id=$(grep DEVICE= ${i} | cut -d "." -f 2)
            ip=$(grep IPADDR= ${i} | cut -d "=" -f 2)
            mask=$(grep NETMASK= ${i} | cut -d "=" -f 2)
            prefix=$(ipcalc -p 1.1.1.1 ${mask}  | sed -n 's:^PREFIX=\(.*\):\1:p')
            echo ${vlan_id}" "${ip}"/"${prefix} >> ${OUTFILE}
    done
    ```

    -   Для скрипта необходима утилита `ipcalc`:
        ```shell
        dnf -y install ipcalc
        ```
-   Получившийся файл `iflist` имеет следующий формат:
    ```conf-unix
    200 10.200.0.2/16
    ```
-   Скрипт `mk-if-script` для получения команд генерации интерфейсов VLAN:
    ```awk
    #!/usr/bin/awk -f

    BEGIN { print "#!/bin/sh\n" }
    { print "nmcli connection add type vlan con-name vlan"$1"-con ifname vlan"$1"-if dev eno1 id "$1"\n""nmcli connection modify vlan"$1"-con ipv4.addresses "$2"\n""sudo nmcli connection modify vlan"$1"-con ipv4.method manual" }
    ```
-   Получим файл с командами интерфейсов:
    ```shell
    ./mk-if-script iflist > iflist-run
    ```
-   Сгенерим новые интерфейсы:
    ```shell
    chmod +x iflist-run
    ./iflist-run
    ```


### <span class="section-num">6.2</span> Конфигурация интерфейсов для Kea {#конфигурация-интерфейсов-для-kea}

-   Добавим интерфейсы в файл конфигурации `/etc/kea/kea-dhcp4.conf`:
    ```js-json
    "Dhcp4": {
        "interfaces-config": {
            "interfaces": [
                "vlan200-if",
                "vlan201-if",
                "vlan202-if"
            ],
            "dhcp-socket-type": "raw"
        },
    }
    ```


## <span class="section-num">7</span> Управляющий агент kea-ctrl-agent {#управляющий-агент-kea-ctrl-agent}


### <span class="section-num">7.1</span> По умолчанию {#по-умолчанию}

-   По умолчанию агент устанавливает unix-сокеты и доступ по сети для локального хоста.
-   Если ничего другого не надо, то дополнительной настройки не требуется.


### <span class="section-num">7.2</span> Доступ по сети {#доступ-по-сети}

-   Для доступа к управляющему агенту из вне необходимо настроить сетевой доступ.
-   Например, это может понадобиться для интеграции с Netbox (см. [NetBox. Плагин netbox-kea]({{< relref "2024-07-22-netbox-plugin-netbox-kea" >}})).


#### <span class="section-num">7.2.1</span> Брандмауэр {#брандмауэр}

-   Сконфигурируем брандмауэр:
    ```shell
    firewall-cmd --add-port=8000/tcp --permanent
    firewall-cmd --reload
    ```


#### <span class="section-num">7.2.2</span> Сертификаты {#сертификаты}

-   В качестве сертификатов можно использовать сертификаты ACME.
-   Если сертификаты не установлены, то используется протокол `http`.


#### <span class="section-num">7.2.3</span> Конфигурационный файл {#конфигурационный-файл}

-   Конфигурация в файле будет будет иметь вид:
    ```js-json
    {
        "Control-agent": {
            "http-host": "10.20.30.40",
            "http-port": 8000,
            "trust-anchor": "/path/to/the/ca-cert.pem",
            "cert-file": "/path/to/the/agent-cert.pem",
            "key-file": "/path/to/the/agent-key.pem",
            "cert-required": true,
            "authentication": {
                "type": "basic",
                "realm": "kea-control-agent",
                "clients": [
                    {
                        "user": "admin",
                        "password": "1234"
                    }
                ]
            },
            ...
        }
    ```


#### <span class="section-num">7.2.4</span> Пример запроса {#пример-запроса}

-   Пример запроса с использованием RESTful API:
    ```shell
    curl -u admin:1234 -X POST -H "Content-Type: application/json" -d '{ "command": "config-get", "service": [ "dhcp4" ] }' http://10.20.30.40:8000/
    ```


## <span class="section-num">8</span> Запуск {#запуск}

-   Запуск управляющего агента:
    ```shell
    systemctl enable --now kea-ctrl-agent.service
    ```
-   Запуск сервера DHCPv4:
    ```shell
    systemctl enable --now kea-dhcp4.service
    ```
-   Запуск сервиса DDNS:
    ```shell
    systemctl enable --now kea-dhcp-ddns.service
    ```


## <span class="section-num">9</span> Утилиты {#утилиты}


### <span class="section-num">9.1</span> Просмотр арендованных адресов {#просмотр-арендованных-адресов}

-   Арендованные адреса можно смотреть в базе данных.
-   Для разных баз данных существуют конкретные утилиты.


#### <span class="section-num">9.1.1</span> Postgres {#postgres}

<!--list-separator-->

1.  kea-list-leases

    -   Репозиторий: <https://git.sr.ht/~cstrotm/kea-list-leases>
    -   В репозитории скрипт и конфигурационный файл.

    <!--list-separator-->

    1.  Пререквизиты

        -   Нужно установить драйвер PostgreSQL для python : psycopg (<https://www.psycopg.org/>):
            ```shell
            dnf -y install python3-psycopg2
            ```

    <!--list-separator-->

    2.  Настройка

        -   Задайте конфигурационный файл `kea-list-leases.conf` (в том же каталоге, что и скрипт):
            ```toml
            [postgresql]
            host=127.0.0.1
            database=kea_lease_db
            user=kea
            password=password
            ```


## <span class="section-num">10</span> После установки {#после-установки}

-   Настройте DDNS (см. [Динамическое обновление DNS-сервера BIND при помощи Kea DHCP]({{< relref "2024-06-18-dynamically-updating-bind-dns-kea-dhcp" >}}))
