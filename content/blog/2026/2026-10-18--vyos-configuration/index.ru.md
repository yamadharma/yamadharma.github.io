---
title: "VyOS. Конфигурирование"
author: ["Dmitry S. Kulyabov"]
date: 2026-10-18T19:09:00+03:00
lastmod: 2026-10-24T21:28:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "vyos-configuration"
---

VyOS. Конфигурирование.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Быстрая настройка (старая) {#быстрая-настройка--старая}


### <span class="section-num">1.1</span> Конфигурация интерфейсов {#конфигурация-интерфейсов}

-   Внешний интерфейс: `eth0`. Он получает адрес по DHCP.
-   Внутренний интерфейс: `eth1`. Использует статический IP-адрес `192.168.0.1/24`.
-   После перехода в режим конфигурации введём следующие команды:
    ```shell
    set interfaces ethernet eth0 address dhcp
    set interfaces ethernet eth0 description 'OUTSIDE'
    set interfaces ethernet eth1 address '192.168.0.1/24'
    set interfaces ethernet eth1 description 'INSIDE'
    ```


### <span class="section-num">1.2</span> SSH-сервер {#ssh-сервер}

-   Включим ssh-сервер:
    ```shell
    set service ssh port '22'
    ```


### <span class="section-num">1.3</span> Сервисы DHCP и DNS {#сервисы-dhcp-и-dns}

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


### <span class="section-num">1.4</span> Настройка NAT {#настройка-nat}

-   Настроим правила SNAT для внутренней сети:
    ```shell
    set nat source rule 100 outbound-interface 'eth0'
    set nat source rule 100 source address '192.168.0.0/24'
    set nat source rule 100 translation address masquerade
    ```


### <span class="section-num">1.5</span> Брандмауэр {#брандмауэр}

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


### <span class="section-num">1.6</span> Настройка безопасности {#настройка-безопасности}

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


## <span class="section-num">2</span> Быстрая настройка {#быстрая-настройка}


### <span class="section-num">2.1</span> Предварительные условия {#предварительные-условия}

-   Настроим шлюз NAT с двумя сетевыми интерфейсами (`eth0` и `eth1`).
-   После установки VyOS войдите в систему используя учетные данные по умолчанию:
    -   username: `vyos`
    -   password: `vyos`


### <span class="section-num">2.2</span> Режим конфигурации {#режим-конфигурации}

-   В рабочем режиме в командной строке отображается символ `$`.
-   В режиме конфигурации в командной строке отображается `#`.
-   Для внесения изменений в конфигурацию необходимо войти в режим конфигурации:
    ```shell
    vyos@vyos:~$ configure
    [edit]
    vyos@vyos#
    ```


### <span class="section-num">2.3</span> Соранение конфигурации {#соранение-конфигурации}

-   Изменения в конфигурации не вступят в силу, пока не будет выполнена команда `commit`.
-   После каждого изменения конфигурации необходимо применить изменения:
    ```shell
    commit
    ```
-   В конце нужно сохранить конфигурацию:
    ```shell
    save
    ```

-   `commit` : применяет изменения конфигурации
-   `save`  : сохраняет конфигурацию на постоянной основе


### <span class="section-num">2.4</span> Конфигурация интерфейсов {#конфигурация-интерфейсов}


#### <span class="section-num">2.4.1</span> WAN интерфейс (eth0) {#wan-интерфейс--eth0}

-   Настройка внешнего интерфейса для получения IP-адреса через DHCP:
    ```shell
    set interfaces ethernet eth0 address dhcp
    set interfaces ethernet eth0 description 'WAN'
    ```


#### <span class="section-num">2.4.2</span> LAN интерфейс (eth1) {#lan-интерфейс--eth1}

-   Настройка внутреннего интерфейса со статическим IP-адресом:
    ```shell
    set interfaces ethernet eth1 address '192.168.0.1/24'
    set interfaces ethernet eth1 description 'LAN'
    ```


### <span class="section-num">2.5</span> Имя хоста {#имя-хоста}

-   Задайте имя хоста:
    ```shell
    set system host-name <hostname>
    ```


### <span class="section-num">2.6</span> Настройка SSH {#настройка-ssh}

-   Включение SSH для удаленного управления:
    ```shell
    set service ssh port 22
    ```


### <span class="section-num">2.7</span> Конфигурация DHCP и DNS {#конфигурация-dhcp-и-dns}


#### <span class="section-num">2.7.1</span> DHCP сервер {#dhcp-сервер}

-   Настройка DHCP-сервера для внутренней сети:
    ```shell
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 option default-router '192.168.0.1'
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 option name-server '192.168.0.1'
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 option domain-name 'internal-network'
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 range 0 start '192.168.0.9'
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 range 0 stop '192.168.0.254'
    set service dhcp-server shared-network-name LAN subnet 192.168.0.0/24 subnet-id 1
    ```

-   Параметры:
    -   `default-router` : шлюз по умолчанию для клиентов
    -   `name-server` : dns-сервер для клиентов
    -   `domain-name` : доменное имя
    -   `range` : диапазон выдаваемых IP-адресов (192.168.0.9 - 192.168.0.254)
    -   `lease` : время аренды адреса (по умолчанию 86400 секунд)


#### <span class="section-num">2.7.2</span> DNS forwarding {#dns-forwarding}

-   Настройка DNS-пересылки:
    ```shell
    set service dns forwarding listen-address '192.168.0.1'
    set service dns forwarding allow-from '192.168.0.0/24'
    ```


#### <span class="section-num">2.7.3</span> Системные DNS-серверы {#системные-dns-серверы}

-   VyOS использует DNS-серверы, указанные в конфигурации `system name-server` , для разрешения имён для собственных нужд (ping, обновления и т.д.).
-   Рекомендуется указывать не более трёх серверов.
-   Настройте DNS-серверы (например, Яндекс и Cloudflare):
    ```shell
    set system name-server 77.88.8.8
    set system name-server 1.1.1.1
    ```


### <span class="section-num">2.8</span> Конфигурация NAT {#конфигурация-nat}

-   Настройка Source NAT для доступа внутренней сети в интернет:
    ```shell
    set nat source rule 100 outbound-interface name 'eth0'
    set nat source rule 100 source address '192.168.0.0/24'
    set nat source rule 100 translation address 'masquerade'
    ```

-   Параметры:
    -   `rule 100` : номер правила
    -   `outbound-interface` : исходящий интерфейс (WAN)
    -   `source address` : адреса источника (внутренняя сеть)
    -   `masquerade` : IP-маскарадинг (замена адреса источника на адрес WAN-интерфейса)


### <span class="section-num">2.9</span> Конфигурация межсетевого экрана {#конфигурация-межсетевого-экрана}

-   VyOS использует nftables в качестве backend для firewall.


#### <span class="section-num">2.9.1</span> Настройка групп адресов {#настройка-групп-адресов}

-   Создание группы адресов для внутренней сети:
    ```shell
    set firewall group address-group LAN-NETWORKS address '192.168.0.0/24'
    ```


#### <span class="section-num">2.9.2</span> Правила для входящего трафика (eth0 → router) {#правила-для-входящего-трафика--eth0-router}

-   Создание правил для защиты самого маршрутизатора:

<!--listend-->

```shell
set firewall ipv4 input filter default-action 'drop'
set firewall ipv4 input filter rule 10 action 'accept'
set firewall ipv4 input filter rule 10 state established
set firewall ipv4 input filter rule 10 state related
set firewall ipv4 input filter rule 20 action 'drop'
set firewall ipv4 input filter rule 20 state invalid
set firewall ipv4 input filter rule 30 action 'accept'
set firewall ipv4 input filter rule 30 protocol 'icmp'
set firewall ipv4 input filter rule 40 action 'accept'
set firewall ipv4 input filter rule 40 source group address-group 'LAN-NETWORKS'
```

-   Логика правил:
    -   `default-action drop` : блокировка всего трафика по умолчанию
    -   `rule 10` : разрешение established/related соединений
    -   `rule 20` : отбрасывание invalid пакетов
    -   `rule 30` : разрешение ICMP (ping)
    -   `rule 40` : разрешение трафика из внутренней сети


#### <span class="section-num">2.9.3</span> Правила для транзитного трафика (eth0 → eth1) {#правила-для-транзитного-трафика--eth0-eth1}

-   Создание правил для трафика, проходящего через маршрутизатор:
    ```shell
    set firewall ipv4 forward filter default-action 'drop'
    set firewall ipv4 forward filter rule 10 action 'accept'
    set firewall ipv4 forward filter rule 10 state established
    set firewall ipv4 forward filter rule 10 state related
    set firewall ipv4 forward filter rule 20 action 'drop'
    set firewall ipv4 forward filter rule 20 state invalid
    set firewall ipv4 forward filter rule 30 action 'accept'
    set firewall ipv4 forward filter rule 30 source group address-group 'LAN-NETWORKS'
    ```


### <span class="section-num">2.10</span> Настройка времени {#настройка-времени}

-   Установите временную зону UTC (координированное всемирное время):
    ```shell
    set system time-zone UTC
    ```

-   Установите NTP серверы:
    ```shell
    set service ntp server 0.pool.ntp.org
    set service ntp server 1.pool.ntp.org
    ```


### <span class="section-num">2.11</span> Применение конфигурации {#применение-конфигурации}

-   Применение и сохранение изменений:
    ```shell
    commit
    save
    ```

-   После выполнения этих команд базовая конфигурация NAT-шлюза готова к работе.


### <span class="section-num">2.12</span> Усиление безопасности {#усиление-безопасности}


#### <span class="section-num">2.12.1</span> Замена пользователя по умолчанию {#замена-пользователя-по-умолчанию}

-   Создание нового пользователя с правами администратора:
    ```shell
    set system login user admin authentication plaintext-password 'secure_password'
    set system login user admin authentication public-keys user@host key 'AAAAB3Nz....'
    set system login user admin authentication public-keys user@host type 'ssh-rsa'
    ```

-   Удаление пользователя по умолчанию:
    ```shell
    delete system login user vyos
    ```


#### <span class="section-num">2.12.2</span> Отключение парольной аутентификации {#отключение-парольной-аутентификации}

-   Для повышения безопасности рекомендуется использовать только аутентификацию по SSH-ключам:
    ```shell
    set service ssh disable-password-authentication
    ```

-   Не забудьте применить изменения:
    ```shell
    commit
    save
    ```


### <span class="section-num">2.13</span> Проверка конфигурации {#проверка-конфигурации}

-   Проверка состояния интерфейсов:
    ```shell
    show interfaces
    ```

-   Проверка таблицы маршрутизации:
    ```shell
    show ip route
    ```

-   Проверка NAT:
    ```shell
    show nat source rules
    show nat source statistics
    ```

-   Проверка правил firewall:
    ```shell
    show firewall
    ```

-   Просмотр активных DHCP-аренд:
    ```shell
    show dhcp server leases
    ```


## <span class="section-num">3</span> Настройка часового пояса в VyOS {#настройка-часового-пояса-в-vyos}


### <span class="section-num">3.1</span> Базовая конфигурация {#базовая-конфигурация}


#### <span class="section-num">3.1.1</span> Установка часового пояса {#установка-часового-пояса}

```shell
# Установить часовой пояс (Москва)
set system time-zone Europe/Moscow

commit
save
```

-   Проверка:

<!--listend-->

```shell
# Показать текущее время и часовой пояс
show date

# Результат:
# Wed Oct 14 15:30:45 MSK 2025
```


#### <span class="section-num">3.1.2</span> Список доступных часовых поясов {#список-доступных-часовых-поясов}

```shell
# Показать все доступные часовые пояса
ls /usr/share/zoneinfo/

# Часовые пояса России
ls /usr/share/zoneinfo/Europe/ | grep -E "Moscow|Samara|Yekaterinburg|Omsk|Krasnoyarsk|Irkutsk|Yakutsk|Vladivostok|Magadan|Kamchatka"

# Другие регионы
ls /usr/share/zoneinfo/Europe/
ls /usr/share/zoneinfo/America/
ls /usr/share/zoneinfo/Asia/
ls /usr/share/zoneinfo/Africa/
ls /usr/share/zoneinfo/Australia/
```


#### <span class="section-num">3.1.3</span> Часовые пояса России {#часовые-пояса-россии}

-   Основные часовые пояса РФ:

-   `Europe/Kaliningrad`  - MSK-1 (UTC+2)
-   `Europe/Moscow`  - MSK (UTC+3) - Москва, Санкт-Петербург
-   `Europe/Samara`  - MSK+1 (UTC+4) - Самара, Ижевск, Ульяновск
-   `Asia/Yekaterinburg`  - MSK+2 (UTC+5) - Екатеринбург, Челябинск, Пермь
-   `Asia/Omsk`  - MSK+3 (UTC+6) - Омск
-   `Asia/Krasnoyarsk`  - MSK+4 (UTC+7) - Красноярск, Новосибирск, Кемерово
-   `Asia/Irkutsk`  - MSK+5 (UTC+8) - Иркутск, Улан-Удэ
-   `Asia/Yakutsk`  - MSK+6 (UTC+9) - Якутск, Чита
-   `Asia/Vladivostok`  - MSK+7 (UTC+10) - Владивосток, Хабаровск
-   `Asia/Magadan`  - MSK+8 (UTC+11) - Магадан, Сахалин
-   `Asia/Kamchatka`  - MSK+9 (UTC+12) - Петропавловск-Камчатский

<!--listend-->

```shell
# Установить для различных регионов России
set system time-zone Europe/Moscow      # Москва
set system time-zone Asia/Yekaterinburg # Екатеринбург
set system time-zone Asia/Vladivostok   # Владивосток

commit
save
```


#### <span class="section-num">3.1.4</span> Интеграция с NTP {#интеграция-с-ntp}

```shell
# Настроить NTP для автоматической синхронизации времени
set service ntp server 0.ru.pool.ntp.org
set service ntp server 1.ru.pool.ntp.org
set service ntp server 2.ru.pool.ntp.org

# Установить часовой пояс
set system time-zone Europe/Moscow

commit
save
```

-   Проверка синхронизации:

<!--listend-->

```c
# Статус NTP
show ntp

# Вывод:
#      remote           refid      st t when poll reach   delay   offset  jitter
# ==============================================================================
# *ntp1.example.com .GPS.            1 u   64   64  377    1.234   -0.123   0.045
# +ntp2.example.com .GPS.            1 u   32   64  377    2.345    0.234   0.067

# Показать текущее время
show date
```


### <span class="section-num">3.2</span> Расширенная конфигурация {#расширенная-конфигурация}


#### <span class="section-num">3.2.1</span> Настройка для распределенной инфраструктуры {#настройка-для-распределенной-инфраструктуры}

-   При наличии роутеров в разных часовых поясах:
    ```shell
    # Роутер в Москве
    set system host-name vyos-msk
    set system time-zone Europe/Moscow
    set service ntp server ntp1.yandex.ru
    set service ntp server ntp2.yandex.ru

    # Роутер в Екатеринбурге
    set system host-name vyos-ekb
    set system time-zone Asia/Yekaterinburg
    set service ntp server ntp1.yandex.ru
    set service ntp server ntp2.yandex.ru

    # Роутер во Владивостоке
    set system host-name vyos-vvo
    set system time-zone Asia/Vladivostok
    set service ntp server ntp1.yandex.ru
    set service ntp server ntp2.yandex.ru

    commit
    save
    ```


#### <span class="section-num">3.2.2</span> UTC для централизованного логирования {#utc-для-централизованного-логирования}

-   Для централизованных систем логирования и мониторинга рекомендуется использовать UTC:

<!--listend-->

```shell
# Установить UTC (координированное всемирное время)
set system time-zone UTC

# NTP серверы
set service ntp server 0.pool.ntp.org
set service ntp server 1.pool.ntp.org

commit
save
```


#### <span class="section-num">3.2.3</span> Автоматическая настройка часового пояса из DHCP {#автоматическая-настройка-часового-пояса-из-dhcp}

```shell
# Включить получение NTP серверов из DHCP (если WAN интерфейс)
set interfaces ethernet eth0 address dhcp

# DHCP опция 42 (NTP servers) будет автоматически применена
# Но часовой пояс все равно нужно настроить вручную
set system time-zone Europe/Moscow

commit
save
```


### <span class="section-num">3.3</span> Лучшие практики {#лучшие-практики}

-   Выбор часового пояса
    -   Использовать UTC для централизованных систем логирования
    -   Использовать локальное время для удобства администраторов
    -   Документировать выбранный часовой пояс
    -   Согласовать с командой DevOps/NOC
-   NTP конфигурация
    -   Использовать минимум 3 NTP сервера
    -   Предпочитать локальные NTP серверы для точности
    -   Использовать стратум 1-2 серверы для критичных систем
    -   Настроить fallback на публичные NTP pool
-   Мониторинг времени
    -   Мониторить NTP offset (порог 100ms для общих систем, 1ms для финансовых)
    -   Мониторить NTP jitter
    -   Алертинг на потерю синхронизации
    -   Логировать все коррекции времени
-   Аппаратные часы (RTC)
    -   Синхронизировать RTC с системным временем регулярно
    -   Проверять батарейку RTC раз в год
    -   Автоматически корректировать время при загрузке
-   Планирование задач
    -   Учитывать часовой пояс при настройке cron
    -   Избегать планирования критичных задач во время потенциального DST перехода
    -   Документировать время выполнения задач в комментариях
-   Распределенные системы
    -   Синхронизировать все устройства с одним источником времени
    -   Использовать централизованный NTP сервер
    -   Корпоративный NTP сервер должен синхронизироваться со стратум 1
-   Логирование
    -   Включать часовой пояс в timestamp логов
    -   Использовать ISO 8601 формат для экспорта логов
    -   Конвертировать время при анализе логов из разных часовых поясов
-   Backup и Recovery
    -   Проверять время перед выполнением backup
    -   Включать timestamp в имена backup файлов
    -   Не полагаться только на modification time файлов
-   Аудит
    -   Документировать источник времени
    -   Хранить логи синхронизации времени
    -   Доказать точность времени для аудиторов
    -   Соответствие требованиям регуляторов (PCI DSS, SOX)
-   Troubleshooting
    -   Всегда проверять время при возникновении проблем
    -   Сравнивать время на всех компонентах системы
    -   Использовать UTC для корреляции событий
    -   Документировать временные аномалии
