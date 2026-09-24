---
title: "Linux. Поддержка LLDP"
author: ["Dmitry S. Kulyabov"]
date: 2026-09-18T21:33:00+03:00
lastmod: 2026-09-21T08:50:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "linux-lldp"
---

Linux. Поддержка LLDP.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   LLDP (Link Layer Discovery Protocol).


## <span class="section-num">2</span> Поддержка LLDP {#поддержка-lldp}


### <span class="section-num">2.1</span> Демоны {#демоны}

-   Основная логика работы с LLDP реализована в пользовательских демонах.
-   Наиболее распространены два:
    -   `lldpd`
        -   Универсальный демон, реализующий стандарт IEEE 802.1AB.
        -   Умеет отправлять и принимать LLDP-пакеты, а также поддерживает совместимость с проприетарными протоколами (CDP от Cisco, EDP от Extreme, SONMP от Nortel).
        -   Управление осуществляется через утилиту `lldpcli`.
    -   `lldpad`
        -   Демон, изначально созданный Intel для поддержки Data Center Bridging (DCB).
        -   Он также реализует LLDP и DCBX (расширение для обмена параметрами DCB).
        -   Управляется с помощью утилиты `lldptool`.


### <span class="section-num">2.2</span> Поддержка в ядре Linux {#поддержка-в-ядре-linux}

-   Для работы некоторых функций, особенно связанных с DCB и аппаратной обработкой LLDP на высокоскоростных сетевых картах, требуется поддержка в ядре.
-   Параметр: `CONFIG_DCB`.
-   Если он не включен, некоторые сетевые карты (например, Intel) могут блокировать работу LLDP-агента на уровне прошивки.


### <span class="section-num">2.3</span> Интеграция с `NetworkManager` {#интеграция-с-networkmanager}

-   NetworkManager с версии 1.47.91 включает собственную библиотеку для приема LLDP-пакетов, основанную на коде из systemd.
-   nmstate начиная с версии 0.3.2 предоставляет возможность включать и настраивать LLDP через бэкенд NetworkManager.


### <span class="section-num">2.4</span> Утилиты {#утилиты}

-   `ethtool` для некоторых сетевых карт (например, Intel) позволяет управлять настройками FW-LLDP (Firmware LLDP).


## <span class="section-num">3</span> Использование `lldpd` {#использование-lldpd}

-   `lldpd` является наиболее популярным решением.


### <span class="section-num">3.1</span> Установка {#установка}


#### <span class="section-num">3.1.1</span> Debian/Ubuntu {#debian-ubuntu}

```shell
sudo apt install lldpd
```


#### <span class="section-num">3.1.2</span> RHEL {#rhel}

```shell
sudo dnf -y install lldpd
```


#### <span class="section-num">3.1.3</span> Gentoo {#gentoo}

```shell
emerge net-misc/lldpd
```


### <span class="section-num">3.2</span> Конфигурация {#конфигурация}


#### <span class="section-num">3.2.1</span> Ключи {#ключи}

-   `-x` : Включает SNMP-субагент.
-   `-c` : Включает совместимость с Cisco Discovery Protocol (CDP).
-   `-s` : Включает совместимость с Nortel (SONMP).
-   `-e` : Включает совместимость с Extreme (EDP).


#### <span class="section-num">3.2.2</span> Debian/Ubuntu {#debian-ubuntu}

-   Файл `/etc/default/lldpd`:
    ```shell
    DAEMON_ARGS="-x -c -s -e"
    ```


#### <span class="section-num">3.2.3</span> RHEL {#rhel}

-   Файл `/etc/sysconfig/lldpd`:
    ```shell
    LLDPD_OPTIONS="-x -c -s -e"
    ```

-   Каталог `/etc/default/lldpd.d`.


#### <span class="section-num">3.2.4</span> Gentoo {#gentoo}

-   Файл `/etc/conf.d/lldpd`:
    ```shell
    LLDPD_OPTS="-c"
    ```

-   Юнит systemd не поддерживает конфигурацию из `/etc/conf.d/lldpd` для OpenRC.
-   Используем механизм drop-in для systemd.

-   Создайте drop-in файл:

<!--listend-->

```shell
sudo systemctl edit lldpd
```

-   В открывшемся редакторе добавьте:

<!--listend-->

```ini
[Service]
EnvironmentFile=-/etc/conf.d/lldpd
ExecStart=
ExecStart=/usr/sbin/lldpd $LLDPD_OPTS
```

-   Пустая строка `ExecStart=`  необходима, чтобы сбросить исходную команду запуска.
-   Без неё systemd добавит вторую команду, что приведёт к ошибке.


#### <span class="section-num">3.2.5</span> Каталог `/etc/default/lldpd.d`. {#каталог-etc-default-lldpd-dot-d-dot}


### <span class="section-num">3.3</span> Запуск службы {#запуск-службы}

```shell
sudo systemctl enable --now lldpd
```

-   Проверить статус можно командой `sudo systemctl status lldpd`.


### <span class="section-num">3.4</span> Просмотр информации о соседях {#просмотр-информации-о-соседях}

-   Для управления демоном и просмотра информации используется утилита `lldpcli`.

-   Просмотр всех соседей:
    ```shell
    sudo lldpcli show neighbors
    ```

-   Детальная информация о соседях:
    ```shell
    sudo lldpcli show neighbors details
    ```

-   Информация о локальных интерфейсах:
    ```shell
    sudo lldpcli show interfaces
    ```

-   Просмотр информации о локальном устройстве:
    ```shell
    sudo lldpcli show chassis
    ```


## <span class="section-num">4</span> Использование `NetworkManager` {#использование-networkmanager}


### <span class="section-num">4.1</span> Включение LLDP через `nmcli` {#включение-lldp-через-nmcli}

-   Необходимо установить свойство `connection.lldp` для нужного сетевого соединения.

-   Имя соединения:
    ```shell
    nmcli connection show
    ```

-   Включите LLDP для соединения:
    ```shell
    sudo nmcli connection modify <имя_соединения> connection.lldp enable
    ```

-   Перезапустите соединение:
    ```shell
    sudo nmcli connection up <имя_соединения>
    ```


### <span class="section-num">4.2</span> Просмотр информации о соседях {#просмотр-информации-о-соседях}

-   Показать всех соседей LLDP для всех интерфейсов:

<!--listend-->

```shell
nmcli device lldp list
```

-   Показать соседей для конкретного интерфейса:

<!--listend-->

```shell
nmcli device lldp list ifname eth0
```


### <span class="section-num">4.3</span> Декларативная настройка через `nmstate` {#декларативная-настройка-через-nmstate}

-   [Nmstate. Декларативное управление сетевыми настройками]({{< relref "2026-09-12--nmstate-declarative-network-configuration" >}})

-   Пример YAML-файла для включения LLDP на интерфейсе (`enable-lldp.yml`):
    ```yaml
    interfaces:
    ​  - name: enp1s0
        type: ethernet
        lldp:
          enabled: true
    ```

-   Примените конфигурацию командой:

<!--listend-->

```shell
sudo nmstatectl apply enable-lldp.yml
```

-   Далее можно использовать утилиту `nmstate-autoconf` для автоматического создания VLAN-интерфейсов на основе данных LLDP от коммутатора.
