---
title: "DNS. PowerDNS Recursor"
author: ["Dmitry S. Kulyabov"]
date: 2023-05-23T10:08:00+03:00
lastmod: 2023-07-11T11:05:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "dns-powerdns-recursor"
---

PowerDNS Recursor.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Документация: <https://doc.powerdns.com/recursor/>
-   Сайт: <https://www.powerdns.com/powerdns-recursor>
-   Только кэширующий сервер DNS.


## <span class="section-num">2</span> Установка PowerDNS Recursor {#установка-powerdns-recursor}


### <span class="section-num">2.1</span> Rocky Linux {#rocky-linux}

-   Установите репозиторий _Epel_:
    ```shell
    dnf config-manager --set-enabled crb
    dnf -y install epel-release
    ```
-   Установите PowerDNS Recursor:
    ```shell
    dnf install powerdns-recursor
    ```


## <span class="section-num">3</span> Настройка PowerDNS Recursor {#настройка-powerdns-recursor}

-   Файл конфигурации: `recursor.conf`.
-   Находится в папке,определённой во время компиляции:
    -   `/etc/powerdns`,
    -   `/etc/pdns`,
    -   `/etc/pdns-recursor`,
    -   `/usr/local/etc`.
-   Можно найти эту папку, выполнив команду:
    ```shell
    pdns_recursor --config=default | grep config-dir
    ```
-   По умолчанию Recursor прослушивает локальный петлевой интерфейс, нужно задать нужные адреса.
-   В параметре `allow-from` перечислены подсети, которые могут взаимодействовать с Recursor.
-   Например:
    ```conf-unix
    local-address=192.0.2.25, 2001:DB8::1:25
    allow-from=192.0.2.0/24, 2001:DB8::1:/64
    ```
-   Чтобы принимать входящие запросы клиентов, разрешите службу DNS на брандмауэре:
    ```shell
    firewall-cmd --permanent --add-service=dns
    firewall-cmd --permanent --add-service=dns-over-tls
    ```
-   Перезапустите брандмауэр:
    ```shell
    firewall-cmd --reload
    ```
-   Запустите сервис:
    ```shell
    systemctl enable --now pdns-recursor.service
    ```
