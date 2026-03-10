---
title: "Динамическое обновление DNS-сервера BIND при помощи Kea DHCP"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-18T11:23:00+03:00
lastmod: 2024-06-19T16:02:00+03:00
tags: ["sysadmin", "network", "linux"]
categories: ["computer-science"]
draft: false
slug: "dynamically-updating-bind-dns-kea-dhcp"
---

Динамическое обновление DNS-сервера BIND при помощи Kea DHCP.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Ключи {#ключи}

-   Создадим ключ на сервере с BIND9:
    ```shell
    tsig-keygen -a HMAC-SHA512 DHCP_UPDATER > /etc/named/keys/dhcp_updater.key
    ```
-   Файл `/etc/named/keys/dhcp_updater.key` будет иметь следующий вид:
    ```conf-unix
    key "DHCP_UPDATER" {
        algorithm hmac-sha512;
        secret "psFFSGdUIwK36l1G82LOw15PuIH4W5uB8h/cw7F0XDsjniBbwm/59tM+V3ydcCs15VLpe2pxlUlggWilytQqgg==";
    };
    ```
-   Поправим права доступа:
    ```shell
    chown -R named:named /etc/named/keys
    ```


## <span class="section-num">2</span> Настройка DNS Bind {#настройка-dns-bind}

-   Настройка происходит в файле `/etc/named.conf`.
-   Ключ находится в файле `/etc/named/keys/dhcp_updater.key`.
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
         update-policy {
              grant DHCP_UPDATER wildcard *.local.zone A DHCID;
         };
    };

    zone "0.168.192.in-addr.arpa" IN {
         type master;
         file "192.168.0.db";
         update-policy {
               grant DHCP_UPDATER wildcard *.0.168.192.in-addr.arpa PTR DHCID;
         };
    };
    ```
-   Сделаем проверку конфигурационного файла:
    ```shell
    named-checkconf
    ```
-   Перестартуйте сервер DNS:
    ```shell
    systemctl restart named.service
    ```


## <span class="section-num">3</span> Настройка Kea DHCP {#настройка-kea-dhcp}


### <span class="section-num">3.1</span> Ключ {#ключ}

-   Файл ключа назовём `/etc/kea/tsig-keys.json`:
    ```shell
    touch /etc/kea/tsig-keys.json
    ```
-   Перенесём ключ на сервер Kea DHCP и перепишем его в формате json:
    ```js
    "tsig-keys": [
        {
           "name": "DHCP_UPDATER",
           "algorithm": "hmac-sha512",
           "secret": "psFFSGdUIwK36l1G82LOw15PuIH4W5uB8h/cw7F0XDsjniBbwm/59tM+V3ydcCs15VLpe2pxlUlggWilytQqgg=="
        }
    ],
    ```
-   Сменим владельца:
    ```shell
    chown kea:root /etc/kea/tsig-keys.json
    ```
-   Поправим права доступа:
    ```shell
    chmod 640 /etc/kea/tsig-keys.json
    ```


### <span class="section-num">3.2</span> Сервис ddns {#сервис-ddns}

-   Настройка происходит в файле `/etc/kea/kea-dhcp-ddns.conf`.
-   Файл будет иметь следующий вид:
    ```js
    {
        "DhcpDdns":
        {
            "ip-address": "127.0.0.1",
            "port": 53001,
            "control-socket": {
                "socket-type": "unix",
                "socket-name": "/tmp/kea-ddns-ctrl-socket"
            },
            <?include "/etc/kea/tsig-keys.json"?>

            "forward-ddns" : {
                "ddns-domains" : [
                    {
                        "name": "local.zone.",
                        "key-name": "DHCP_UPDATER",
                        "dns-servers": [
                            { "ip-address": "192.168.0.1" }
                        ]
                    }
                ]
            },

            "reverse-ddns" : {
                "ddns-domains" : [
                    {
                        "name": "0.168.192.in-addr.arpa.",
                        "key-name": "DHCP_UPDATER",
                        "dns-servers": [
                            { "ip-address": "192.168.0.1" }
                        ]
                    }
                ]
            },

            "loggers": [
                {
                    "name": "kea-dhcp-ddns",
                    "output_options": [
                        {
                            "output": "stdout",
                            "pattern": "%-5p %m\n"
                        }
                    ],
                    "severity": "INFO",

                    "debuglevel": 0
                }
            ]
        }
    }
    ```
-   Обратите особое внимание на точку в конце имени зоны, иначе DDNS завершится сбоем и сообщит, что не удалось найти соответствующее полное доменное имя.
-   Можно определить несколько DNS-серверов.
-   Раздел журналирования оставлен из шаблона.
-   Изменим владельца файла:
    ```shell
    chown kea:root /etc/kea/kea-dhcp-ddns.conf
    ```
-   Проверим файл на наличие возможных синтаксических ошибок:
    ```shell
    kea-dhcp-ddns -t /etc/kea/kea-dhcp-ddns.conf
    ```
-   Запустим службу ddns:
    ```shell
    systemctl enable --now kea-dhcp-ddns.service
    ```
-   Проверим статус работы службы:
    ```shell
    systemctl status kea-dhcp-ddns.service
    ```


### <span class="section-num">3.3</span> Сервис dhcp4 {#сервис-dhcp4}

-   Настройка происходит в файле `/etc/kea/kea-dhcp4.conf`.
-   Включим динамическое обновление:
    ```js
    "dhcp-ddns": {
        "enable-updates": true
    },

    "ddns-qualifying-suffix": "local.zone",
    "ddns-override-client-update": true,
    ```
-   Включаем обновления DDNS.
-   Затем мы сообщаем DHCP-серверу, каким будет DNS-суффикс по умолчанию.
    -   Если клиент предоставляет только своё имя хоста, это вызывает проблемы для DDNS, поскольку он не будет знать, что такое полное доменное имя, и поэтому не будет знать, какую зону обновлять.
    -   Другими словами, команда `ddns-qualifying-suffix` используется для указания того, какое доменное имя должно быть добавлено к имени хоста.
    -   Можно определить это для каждой подсети.
-   Для параметра `ddns-override-client-update` устанавливается значение `true`, поскольку мы не хотим, чтобы клиент решал, какие записи обновлять.
-   Проверим файл на наличие возможных синтаксических ошибок:
    ```shell
    kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
    ```
-   Перезапустим службу, чтобы изменения вступили в силу:
    ```shell
    systemctl restart kea-dhcp4.service
    ```
-   Проверим статус:
    ```shell
    systemctl status kea-dhcp4.service
    ```
