---
title: "Начальная конфигурация коммутатора Cisco"
author: ["Dmitry S. Kulyabov"]
date: 2022-11-15T14:51:00+03:00
lastmod: 2025-11-20T14:10:00+03:00
tags: ["cisco", "network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "initial-cisco-switch-configuration"
---

Начальная конфигурация коммутатора Cisco Catalist.

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


### <span class="section-num">2.1</span> Включение {#включение}

-   При первом включении, после долгой загрузки коммутатор выдает предложение запустить диалог стартовой конфигурации:
    ```text
    Would you like to enter the initial configuration dialog? [yes/no]:
    ```
-   Следует отказаться и выполнить конфигурацию вручную, поэтому отвечаем `no`.


### <span class="section-num">2.2</span> Переход в привилегированный режим {#переход-в-привилегированный-режим}

-   Получаем приглашение `Switch>`.
-   Переходим в привилегированный режим командой `enable`.
-   Приглашение меняется на `#`:
    ```shell
    Switch>enable
    Switch#
    ```


### <span class="section-num">2.3</span> Переход в режим конфигурации {#переход-в-режим-конфигурации}

-   Перейдём в режим конфигурации коммутатора:
    ```shell
    Switch#configure terminal
    ```


### <span class="section-num">2.4</span> Шифрование паролей {#шифрование-паролей}

-   Установим шифрование паролей, хранящиеся в устройстве в открытом виде:
    ```shell
    Switch(config)#service password-encryption
    ```


### <span class="section-num">2.5</span> Административный доступ {#административный-доступ}

-   Зададим пароль на _enable_:
    ```shell
    Switch(config)#enable secret <пароль>
    ```

    -   `secret` : указывает на то, что пароль будет храниться в зашифрованном виде[^fn:1].
-   После оператора `secret` можно задать представление пароля:
    -   `0` : незашифрованный текстовый пароль; используется по умолчанию, поэтому не обязателен;
    -   `4` : используется хеш SHA-256; считается устаревшим;
    -   `5` : используется хеш MD5;
    -   `8` : используется хеш SHA-256;
    -   `9` : используется алгоритм `scrypt`.


### <span class="section-num">2.6</span> Настройка нового режима аутентификации {#настройка-нового-режима-аутентификации}

-   Настроим режим _aaa_ (authentication, authorization, accounting):
    ```shell
    Switch(config)#aaa new-model
    Switch(config)#aaa authentication login default local
    ```
-   Настроим подключение по консоли:
    ```shell
    Switch(config)#line console 0
    Switch(config-line)#login authentication default
    Switch(config-line)#no password
    Switch(config-line)#exit
    ```

    -   Консоль настроена на использование локальной базы данных имён пользователей и паролей.
    -   `no password` : удалить старую модель паролей.


### <span class="section-num">2.7</span> Административный пользователь {#административный-пользователь}

-   Зададим пользователя admin и пароль для него:
    ```shell
    Switch(config)#username admin privilege 1 secret <пароль>
    ```

    -   `privelege` : уровень привилегий для данного пользователя от 0 до 15 (15 самый высокий);
    -   `secret` : пароль будет храниться в зашифрованном виде.


### <span class="section-num">2.8</span> Удалённый доступ {#удалённый-доступ}

-   Не во всех поставках IOS есть поддержка _ssh_. Поэтому приходится использовать _telnet_.
-   Настроим порядок аутентификации по _telnet_.
-   Настроим подключение по терминальным линиям.
    ```shell
    Switch(config)#line vty 0 4
    Switch(config-line)#login authentication default
    Switch(config-line)#transport input telnet
    Switch(config-line)#no password
    Switch(config-line)#exit
    Switch(config)#line vty 5 15
    Switch(config-line)#login authentication default
    Switch(config-line)#transport input telnet
    Switch(config-line)#no password
    Switch(config-line)#exit
    ```

    -   Терминальные линии, включая telnet, настроены на использование одной и той же локальной базы данных имён пользователей и паролей.
    -   `no password` : удалить старую модель паролей.


### <span class="section-num">2.9</span> Зададим имя устройства {#зададим-имя-устройства}

-   Имя устройства имеет вид: sw-&lt;помещение&gt;-&lt;номер устройства&gt;, например `sw-103-1`.
-   Зададим имя устройства:
    ```shell
    Switch(config)#hostname sw-103-1
    sw-103-1(config)#ip domain-name example.com
    ```


### <span class="section-num">2.10</span> Настройка ssh {#настройка-ssh}

-   Если устройство поддерживает ssh, то стоит его настроить.
-   Создадим ключ (необходимо, чтобы было настроено имя домена):
    ```shell
    sw-103-1(config)#crypto key generate rsa modulus 2048
    ```
-   Задаёт версию протокола для ssh:
    ```shell
    sw-103-1(config)#ip ssh version 2
    ```
-   Указываем время таймаута до автоматического закрытия SSH сессии в 60 минут:
    ```shell
    sw-103-1(config)#ip ssh time-out 60
    ```
-   Сбрасываем подключение после 3 неверных паролей:
    ```shell
    sw-103-1(config)#ip ssh authentication-retries 3
    ```
-   Задаём протокол для подключения:
    ```shell
    sw-103-1(config)#line vty 0 4
    sw-103-1(config-line)#transport input ssh
    ```
-   Можно также оставить и telnet:
    ```shell
    sw-103-1(config)#line vty 0 4
    sw-103-1(config-line)#transport input all
    ```


### <span class="section-num">2.11</span> Поднимем интерфейсы {#поднимем-интерфейсы}

-   Сделаем последний порт транковым:
    ```shell
    sw-103-1(config)#interface gigabitEthernet1/0/48
    sw-103-1(config-if-range)#switchport mode trunk
    sw-103-1(config-if-range)#exit
    ```


### <span class="section-num">2.12</span> Сетевые настройки {#сетевые-настройки}

-   Зададим адрес 192.168.0.1/24, шлюз 192.168.0.254:
    ```shell
    sw-103-1(config)#interface vlan1
    sw-103-1(config-if)#no shutdown
    sw-103-1(config-if)#ip address 192.168.0.1 255.255.255.0
    sw-103-1(config-if)#exit
    sw-103-1(config)#ip default-gateway 192.168.0.254
    ```
-   Настроим клиента DNS:
    ```shell
    sw-103-1(config)#ip name-server 192.168.0.254
    ```
-   Настроим NTP:
    ```shell
    sw-103-1(config)#ntp server pool.ntp.org
    ```
-   Проверим статус синхронизации:
    ```shell
    sw-103-1#sh ntp status
    ```


### <span class="section-num">2.13</span> Настройка vtp {#настройка-vtp}

-   Настройте vtp:
    ```shell
    sw-103-1(config)#vtp mode client
    ```
-   Проверьте статус vtp:
    ```shell
    sw-103-1#sh vtp status
    ```


### <span class="section-num">2.14</span> Настройка lldp {#настройка-lldp}

-   Если в сети присутствует не только оборудование Cisco, то есть смысл подключить поддержку протокола lldp:
    ```shell
    sw-103-1(config)#lldp run
    ```


### <span class="section-num">2.15</span> Безопасность {#безопасность}

-   Отключим сервер http:
    ```shell
    sw-103-1(config)#no ip http server
    sw-103-1(config)#no ip http secure-server
    ```


### <span class="section-num">2.16</span> Настройка других портов {#настройка-других-портов}

-   Настроим другие порты для подключения клиентских устройств:
    ```shell
    sw-103-1(config)#interface range GigabitEthernet1/0/1 - 46
    sw-103-1(config-if-range)#switchport mode access
    sw-103-1(config-if-range)#switchport access vlan 100
    sw-103-1(config-if-range)#exit
    ```


### <span class="section-num">2.17</span> Сохранение конфигурации {#сохранение-конфигурации}

-   Сохраните конфигурацию:
    ```shell
    sw-103-1#write mem
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

-   Настройте доступ к SNMP.
-   Пусть сервер мониторинга имеет адрес: 192.168.0.5.
-   Имя коммьюнити для чтения: rocom.
    ```shell
    sw-103-1(config)#access-list 90 permit 192.168.0.5
    sw-103-1(config)#snmp-server community rocom RO 90
    ```
-   Добавьте коммутатор в свой DNS.


### <span class="section-num">4.1</span> Подключение к Observium {#подключение-к-observium}

-   Подключитесь к Observium.
-   Добавьте коммутатор в список наблюдения в Observium:
    ```shell
    [root@observium ~]# /opt/observium/add_device.php sw-103-1 rocom
    [root@observium ~]# /opt/observium/discovery.php -h sw-103-1; /opt/observium/poller.php -h sw-103-1
    ```


### <span class="section-num">4.2</span> Подключение к Librenms {#подключение-к-librenms}

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

[^fn:1]: Установка пароля может быть выполнена двумя командами `password` и `secret`. В первом случае пароль хранится в конфигурационном файле в открытом виде, а во втором в зашифрованном. Если использовалась команда `password`, необходимо зашифровать пароли, хранящиеся в устройстве в открытом виде с помощью команды `service password-encryption` в режиме глобальной конфигурации.
