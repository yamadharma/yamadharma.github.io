---
title: "Netbox. Плагин для DNS"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-26T14:05:00+03:00
lastmod: 2025-03-26T16:06:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "netbox-dns-plugin"
---

Netbox. Плагин для DNS.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   NetBox DNS
-   Репозиторий: <https://github.com/peteeckel/netbox-plugin-dns>
-   Плагин хранит информацию о серверах имен DNS, представлениях и зонах DNS, а также записях DNS.
-   Регистрационная информация о регистраторах DNS и контакты для доменов DNS также могут храниться и связываться с зонами.
-   Механизмы проверки и автоматизации:
    -   проверка имен и значений записей;
    -   автоматическое ведение записей PTR для записей адресов IPv6 и IPv4;
    -   автоматическая генерация записей SOA, опционально включающая серийный номер данных зоны;
    -   проверка изменений в серийном номере SOA, независимо от того, выполняются ли они автоматически или вручную;
    -   проверка типов записей для обеспечения действительности зоны DNS;
    -   поддержка делегирования зон PTR RFC 2317 для подсетей IPv4 длиной более 24 бит.


## <span class="section-num">2</span> Установка {#установка}

-   [NetBox. Плагины]({{< relref "2024-07-22-netbox-plugins" >}})
-   Включите плагин в `/opt/netbox/netbox/netbox/configuration.py`:
    ```yaml
    PLUGINS = [
        "netbox_dns",
    ]
    ```
-   Чтобы плагин оставался установленным постоянно при обновлении NetBox через `upgrade.sh`:
    ```shell
    sudo -u netbox echo netbox-plugin-dns >> /opt/netbox/local_requirements.txt
    ```
-   Зайдите в виртуальное окружение:
    ```shell
    su - netbox
    source /opt/netbox/venv/bin/activate
    ```
-   Установите плагин:
    ```shell
    (venv) $ pip install netbox-plugin-dns
    ```
-   Добавьте необходимые таблицы `netbox_dns` в базу данных:
    ```shell
    (venv) $ /opt/netbox/netbox/manage.py migrate
    ```
-   Перезапустите службу WSGI:
    ```shell
    systemctl restart netbox netbox-rq
    ```
-   Переиндексация глобального поиска
-   Это можно сделать в любое время, особенно если элементы, которые должны отображаться в глобальном поиске, не отображаются.
-   Для того, чтобы существующие объекты NetBox DNS появились в глобальном поиске после первоначальной установки или некоторых обновлений NetBox DNS, необходимо перестроить индексы поиска:

<!--listend-->

```shell
sudo -u netbox /opt/netbox/netbox/manage.py reindex netbox_dns
```
