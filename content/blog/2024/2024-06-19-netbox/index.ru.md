---
title: "Система управления сетью NetBox"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-19T17:52:00+03:00
lastmod: 2025-03-26T14:07:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "netbox"
---

Система управления сетью NetBox.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <http://netboxlabs.com/oss/netbox/>
-   Репозиторий: <https://github.com/netbox-community/netbox>
-   Документация: <https://netbox.readthedocs.io>
-   Приложение для управления и документирования компьютерных сетей.
-   Основные функции:
    -   IP address management (IPAM): IP сети и адреса, VRFs, и VLAN;
    -   DataCenter infrastructure management (DCIM): организация стоечного оборудования по группам и устройствам;
    -   устройства: типы устройств и место установки;
    -   соединения: сеть, консоль, силовые соединения;
    -   виртуализация: виртуальные машины и кластеры;
    -   схемы передачи данных: схемы дальней связи и провайдеры;
    -   секреты: зашифрованное хранение конфиденциальных учетных данных.
-   Стек приложений:
    -   HTTP service: nginx или Apache;
    -   WSGI service: gunicorn или uWSGI;
    -   application: Django/Python, &gt;= python-3.10;
    -   database: — PostgreSQL, &gt;=postgresql-9.12;
    -   task queuing: Redis/django-rq;
    -   live device access: NAPALM.


## <span class="section-num">2</span> Установка {#установка}

-   [NetBox. Установка]({{< relref "2024-06-19-netbox-install" >}})
-   [NetBox. Первоначальная настройка]({{< relref "2024-09-03-netbox-initial-setup" >}})


## <span class="section-num">3</span> Плагины {#плагины}

-   [NetBox. Плагины]({{< relref "2024-07-22-netbox-plugins" >}})


### <span class="section-num">3.1</span> DHCP {#dhcp}

-   [NetBox. Плагин netbox-kea]({{< relref "2024-07-22-netbox-plugin-netbox-kea" >}})
    -   Позволяет получать информацию о выданных адресах.


### <span class="section-num">3.2</span> DNS {#dns}

-   [Netbox. Плагин для DNS]({{< relref "2025-03-26--netbox-dns-plugin" >}})
