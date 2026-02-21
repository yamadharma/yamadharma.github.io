---
title: "NetBox. Первоначальная настройка"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-03T19:19:00+03:00
lastmod: 2024-09-04T11:15:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "netbox-initial-setup"
---

NetBox. Первоначальная настройка.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Настройка организации {#настройка-организации}


### <span class="section-num">1.1</span> Регионы {#регионы}

-   Локальная ссылка: <https://netbox.example.com/dcim/regions/>
-   Можно делать иерархию.
-   Я задал в регионах:
    ```shell
    Moscow
    ```
-   Можно добавить родительский регион:
    ```shell
    Russia
    ```


### <span class="section-num">1.2</span> Сайты {#сайты}

-   Сделал сайты по территориям (зданиям):
    -   Donskaya
    -   Pavlovskaya


## <span class="section-num">2</span> IPAM {#ipam}


### <span class="section-num">2.1</span> VLAN {#vlan}

-   Локальная ссылка: <https://netbox.example.com/ipam/vlans/>
-   Загрузил VLAN в CSV-виде:
    ```csv
    vid,name,status,site
    1,default,active,donskaya
    2,management,active,donskaya
    ```


### <span class="section-num">2.2</span> Префиксы {#префиксы}

-   Локальная ссылка: <https://netbox.example.com/ipam/prefixes/>
-   Загрузил префиксы в CSV-виде:
    ```csv
    prefix,status,vlan,description
    10.128.0.0/16,active,1,"VLAN по умолчанию"
    10.129.0.0/16,active,2,"Коммутаторы"
    ```
