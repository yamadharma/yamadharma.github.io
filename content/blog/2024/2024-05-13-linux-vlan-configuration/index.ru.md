---
title: "Linux. Настройка vlan"
author: ["Dmitry S. Kulyabov"]
date: 2024-05-13T10:34:00+03:00
lastmod: 2025-03-13T15:08:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "linux-vlan-configuration"
---

Linux. Настройка vlan

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   VLAN (Virtual Local Area Network) позволяет разделить сеть на канальном уровне на несколько изолированных широковещательных доменов.
-   С помощью VLAN можно настроить несколько сетей на одном физическом порту сервера.
-   При использовании 802.1Q VLAN сетевым пакетам добавляется специальный тег (тегированный трафик) с номером VLAN (`VLAN ID`, 1--4094).
-   Предназначение VLAN:
    -   сегментирование сети (разделение устройств на изолированные группы);
    -   уменьшение количества сетевого оборудования;
    -   снижение нагрузки на сеть для уменьшения широковещательного трафика;
    -   улучшение безопасности и управляемости сети.


## <span class="section-num">2</span> Поддержка VLAN ядром {#поддержка-vlan-ядром}

-   Проверьте загрузку модуля ядра Linux 8021q:
    ```shell
    lsmod | grep 8021q
    ```
-   Загрузите модуль ядра Linux 8021q:
    ```shell
    modprobe 8021q
    ```
-   Добавьте модуль в автозагрузку:
    ```shell
    echo 8021q >> /etc/modules-load.d/8021q.conf
    ```


## <span class="section-num">3</span> NetworkManager для настройки VLAN интерфейса {#networkmanager-для-настройки-vlan-интерфейса}


### <span class="section-num">3.1</span> Создание интерфейса {#создание-интерфейса}

-   Команда для создания VLAN-соединения:
    ```shell
    nmcli connection add type vlan con-name <con-name> ifname <ifname> dev <device> id <vlan_id>
    ```
-   Будем придерживаться следующих соглашений:
    -   Тег VLAN : &lt;vlan_id&gt; (число от 0 до 4095);
    -   con-name :vlan&lt;vlan_id&gt;-con
    -   ifname : vlan&lt;vlan_id&gt;-if
    -   device: ens5 (какой в системе);
-   Создадим VLAN интерфейс с номером VLAN 10 на устройстве `ens5`:
    ```shell
    nmcli connection add type vlan con-name vlan10-con ifname vlan10-if dev ens5 id 10
    ```
-   Проверьте, что устройство создано:
    ```shell
    nmcli device
    ```
-   Проверьте сетевые интерфейсы:
    ```shell
    nmcli connection show
    ```
-   После настройки выполните перезагрузку NetworkManager:

<!--listend-->

```shell
systemctl restart NetworkManager
```


### <span class="section-num">3.2</span> Назначение IP-адреса {#назначение-ip-адреса}

-   Зададим следующие значения:
    -   соединение: `vlan10-con`;
    -   ip-адрес и сетевая маска: `192.168.10.10/24`;
    -   шлюз по умолчанию: `192.168.10.254`.
-   Назначим IP-адрес:
    ```shell
    nmcli connection modify vlan10-con ipv4.addresses '192.168.10.10/24' ipv4.gateway '192.168.10.254'
    ```
-   Изменим настройку DHCP по умолчанию:
    ```shell
    sudo nmcli connection modify vlan10-con ipv4.method manual
    ```
-   Просмотрим адрес:
    ```shell
    ip addr
    ```


### <span class="section-num">3.3</span> Удаление интерфейса VLAN {#удаление-интерфейса-vlan}

-   Деактивируйте соединение:
    ```shell
    sudo nmcli connection down vlan10-con
    ```
-   Запустите команду `ip addr`, чтобы убедиться, что устройства больше нет в списке:
    ```shell
    ip addr
    ```
-   Запустите команду `sudo nmcli connection`, чтобы просмотреть список доступных подключений:
    ```shell
    nmcli connection
    ```
-   Удалите соединение:
    ```shell
    nmcli connection delete vlan10-con
    ```
-   Запустите команду `sudo nmcli connection`, чтобы просмотреть список доступных подключений:
    ```shell
    nmcli connection
    ```
