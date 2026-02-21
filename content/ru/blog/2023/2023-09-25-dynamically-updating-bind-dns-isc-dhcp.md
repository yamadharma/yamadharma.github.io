---
title: "Динамическое обновление DNS-сервера BIND при помощи ISC DHCP"
author: ["Dmitry S. Kulyabov"]
date: 2023-09-25T13:26:00+03:00
lastmod: 2023-10-28T19:26:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "dynamically-updating-bind-dns-isc-dhcp"
---

Динамическое обновление DNS-сервера BIND при помощи ISC DHCP.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Ключи {#ключи}

-   Создадим ключ:
    ```shell
    tsig-keygen -a HMAC-SHA512 DHCP_UPDATER > /etc/dhcp/keys/dhcp_updater.key
    ```
-   Файл `/etc/dhcp/keys/dhcp_updater.key` будет иметь следующий вид:
    ```conf-unix
    key DHCP_UPDATER {
        algorithm hmac-md5;
        secret "EgxIOyQglf4KAUF7lgu9yA==";
    };
    ```


## <span class="section-num">2</span> Настройка DHCP {#настройка-dhcp}

-   Настройка происходит в файле `/etc/dhcp/dhcpd.conf`.
-   Включим динамическое обновление:
    ```conf-unix
    ddns-updates on;
    ddns-update-style interim;
    ignore client-updates;
    update-static-leases on;
    ```

    -   Данные опции включают динамическое обновление DNS и предписывают делать это в том числе и для статических записей.
-   Подключим ключ к dhcp:
    ```conf-unix
    include "/etc/dhcp/keys/dhcp_updater.key";
    ```
-   Добавим зоны, которые мы обновляем:
    ```conf-unix
    zone local.zone. {
         primary 127.0.0.1;
         key DHCP_UPDATER;
    }

    zone 0.168.192.in-addr.arpa. {
          primary 127.0.0.1;
           key DHCP_UPDATER;
    }
    ```

    -   Имена зон мы пишем в абсолютном формате, т. е. с точкой на конце.
    -   Внутри каждой секции указываем адрес первичного DNS-сервера и ключ доступа к нему.
-   Можно увеличить время аренды адреса:
    ```shell
    default-lease-time 604800;
    max-lease-time 1814400;
    ```
-   Проверяем конфигурацию на ошибки:
    ```shell
    dhcpd -t -cf /etc/dhcp/dhcpd.conf
    ```


## <span class="section-num">3</span> Настройка DNS Bind {#настройка-dns-bind}

-   Настройка происходит в файле `/etc/named.conf`.
-   Ключ скопируем на хост с DNS-сервером (если это другой сервер).
-   Поместим его в файл `/etc/named/keys/dhcp_updater.key`.
-   Подключим ключ:
    ```conf-unix
    include "/etc/named/keys/dhcp_updater.key";
    ```
-   Разрешим обновление зон:
    ```conf-unix
    zone "local.zone" IN {
         type master;
         file "local.zone.db";
         allow-update { key DHCP_UPDATER; };
    };

    zone "0.168.192.in-addr.arpa" IN {
         type master;
         file "192.168.0.db";
         allow-update { key DHCP_UPDATER; };
    };
    ```
