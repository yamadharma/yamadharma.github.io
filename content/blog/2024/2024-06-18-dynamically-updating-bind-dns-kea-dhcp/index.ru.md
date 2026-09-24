---
title: "Динамическое обновление DNS-сервера BIND при помощи Kea DHCP"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-18T11:23:00+03:00
lastmod: 2026-09-17T18:10:00+03:00
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


#### <span class="section-num">3.3.1</span> Минимальная настройка {#минимальная-настройка}

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


#### <span class="section-num">3.3.2</span> Продвинутая настройка {#продвинутая-настройка}

-   Настройка DDNS в `kea-dhcp4.conf` имеет два уровня:
    -   глобальные параметры подключения к демону `kea-dhcp-ddns`;
    -   параметры поведения, которые можно задавать глобально, на уровне shared-network или subnet.

<!--list-separator-->

1.  Параметры подключения

    -   Параметры находятся в секции `dhcp-ddns` верхнего уровня.
    -   Определяют, как DHCP-сервер общается с DDNS.
    -   Они не могут быть переопределены на уровне подсети.
        ```json
        "Dhcp4": {
          "dhcp-ddns": {
            "enable-updates": true,
            "server-ip": "127.0.0.1",
            "server-port": 53001,
            "sender-ip": "",
            "sender-port": 0,
            "max-queue-size": 1024,
            "ncr-protocol": "UDP",
            "ncr-format": "JSON"
          }
        }
        ```

    | Параметр         | Назначение                                                                       | Значение по умолчанию |
    |------------------|----------------------------------------------------------------------------------|-----------------------|
    | `enable-updates` | Включает отправку NCR-запросов в DDNS. Должен быть `true` для работы DDNS.       | `false`               |
    | `server-ip`      | IP-адрес, на котором DDNS слушает запросы.                                       | `127.0.0.1`           |
    | `server-port`    | Порт DDNS.                                                                       | `53001`               |
    | `sender-ip`      | IP, с которого DHCP-сервер отправляет запросы (пусто --- выбрать автоматически). | `""`                  |
    | `sender-port`    | Порт отправителя (0 --- выбрать автоматически).                                  | `0`                   |
    | `max-queue-size` | Максимум запросов в очереди; при переполнении DDNS временно отключается.         | `1024`                |
    | `ncr-protocol`   | Протокол для NCR. Поддерживается только `UDP`.                                   | `UDP`                 |
    | `ncr-format`     | Формат пакета. Поддерживается только `JSON`.                                     | `JSON`                |

<!--list-separator-->

2.  Параметры поведения

    -   Начиная с Kea 1.7.1 эти параметры вынесены из секции `dhcp-ddns`.
    -   Они могут задаваться на трёх уровнях: глобально, в `shared-network` и в `subnet4`.
    -   Значения наследуются сверху вниз.
        ```json
        "Dhcp4": {
          "ddns-send-updates": true,
          "ddns-override-no-update": false,
          "ddns-override-client-update": false,
          "ddns-replace-client-name": "never",
          "ddns-generated-prefix": "myhost",
          "ddns-qualifying-suffix": "example.com",
          "hostname-char-set": "[^A-Za-z0-9.-]",
          "hostname-char-replacement": ""
        }
        ```

    | Параметр                      | Назначение                                                                      | Значение по умолчанию |
    |-------------------------------|---------------------------------------------------------------------------------|-----------------------|
    | `ddns-send-updates`           | Разрешает/запрещает DDNS на данном уровне.                                      | `true`                |
    | `ddns-override-no-update`     | Если `true`, сервер игнорирует запрос клиент не обновлять DNS.                  | `false`               |
    | `ddns-override-client-update` | Если `true`, сервер берёт на себя ответственность за обновление.                | `false`               |
    | `ddns-replace-client-name`    | Режим формирования FQDN: `never`, `always`, `when-present`, `when-not-present`. | `never`               |
    | `ddns-generated-prefix`       | Префикс для авто-генерируемых имён (по умолчанию `myhost`).                     | `myhost`              |
    | `ddns-qualifying-suffix`      | Суффикс домена, добавляемый к неполным именам.                                  | `""`                  |
    | `hostname-char-set`           | Регулярное выражение для недопустимых символов в имени хоста.                   | `[^A-Za-z0-9.-]`      |
    | `hostname-char-replacement`   | Строка замены для недопустимых символов (пусто --- удалять).                    | `""`                  |

    -   `enable-updates` в `dhcp-ddns` **и** `ddns-send-updates` на соответствующем уровне должны быть `true`, иначе обновления не будут отправляться.
    -   Режимы `ddns-replace-client-name`:
        -   `never` --- использовать имя клиента как есть (по умолчанию);
        -   `always` --- всегда генерировать имя на сервере;
        -   `when-present` --- заменять, только если клиент прислал имя;
        -   `when-not-present` --- использовать имя клиента, если оно есть, иначе генерировать.
    -   Параметр `ddns-qualifying-suffix` не имеет значения по умолчанию, и если он не задан, неполные имена клиентов не будут корректно преобразованы в FQDN.
        -   Его следует задать явно при включении DDNS.

<!--list-separator-->

3.  Пример

    ```json
    {
      "Dhcp4": {
        "dhcp-ddns": {
          "enable-updates": true,
          "server-ip": "127.0.0.1",
          "server-port": 53001
        },
        "ddns-send-updates": true,
        "ddns-override-client-update": true,
        "ddns-replace-client-name": "always",
        "ddns-generated-prefix": "host",
        "ddns-qualifying-suffix": "lan.example.com",
        "subnet4": [
          {
            "subnet": "192.168.1.0/24",
            "pools": [ { "pool": "192.168.1.100 - 192.168.1.200" } ],
            "ddns-send-updates": true,
            "ddns-qualifying-suffix": "office.lan.example.com"
          }
        ]
      }
    }
    ```

    -   Глобально DDNS включён, сервер всегда сам генерирует FQDN вида `host-192-168-1-100.lan.example.com`.
    -   Для подсети `192.168.1.0/24` суффикс переопределён на `office.lan.example.com`, поэтому клиенты этой подсети получат имена вида `host-192-168-1-100.office.lan.example.com`.


### <span class="section-num">3.4</span> Проверка {#проверка}

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
