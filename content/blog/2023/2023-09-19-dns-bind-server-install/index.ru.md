---
title: "DNS. Bind. Установка сервера"
author: ["Dmitry S. Kulyabov"]
date: 2023-09-19T14:35:00+03:00
lastmod: 2024-06-18T14:05:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "dns-bind-server-install"
---

Установка сервера DNS _Bind_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Установка Bind {#установка-bind}

-   Устанавливаем DNS-сервер следующей командой:

<!--listend-->

```shell
dnf -y install bind
```


## <span class="section-num">2</span> Актуальные версии Bind {#актуальные-версии-bind}

-   Можно устанавливать не версию bind, поставляемую с системой, а актуальную.
-   Сайт: <https://copr.fedorainfracloud.org/coprs/isc/bind/>


### <span class="section-num">2.1</span> Установка {#установка}

-   Подключить репозиторий:
    ```shell
    dnf copr enable isc/bind
    ```
-   Установить коллекцию программного обеспечения:
    ```shell
    dnf install isc-bind
    ```
-   Коллекция программного обеспечения BIND 9 состоит из нескольких пакетов:
    -   `isc-bind-bind` : содержит `named`, `rndc`, утилиты DNSSEC и соответствующие конфигурационные файлы;
    -   `isc-bind-bind-utils` : содержит другие утилиты BIND 9 (`dig`, `nsupdate`).
-   Файл конфигурации:
    -   `/etc/opt/isc/scls/isc-bind/named.conf`.
-   Параметры командной строки для демона можно указать в файле:
    -   `/etc/opt/isc/scls/isc-bind/sysconfig/named`.
-   Запустить демон:
    ```shell
    systemctl start isc-bind-named
    ```
-   Утилита BIND 9, установленные пакетами SCL, недоступны в `$PATH` по умолчанию.
-   Чтобы иметь возможность их использовать, сделайте следующее:
    -   включить коллекцию программного обеспечения для текущей оболочки:
        ```shell
        scl enable isc-bind bash
        ```
    -   чтобы включить коллекцию программного обеспечения внутри сценария оболочки, добавьте следующую строку:
        ```shell
        source scl_source enable isc-bind
        ```


## <span class="section-num">3</span> Настройка брандмауэра {#настройка-брандмауэра}

-   Настроим правила брандмауэра:
    ```shell
    firewall-cmd --zone=public --add-service=dns
    firewall-cmd --runtime-to-permanent
    firewall-cmd --reload
    ```


## <span class="section-num">4</span> Запуск Bind {#запуск-bind}

-   Запускаем _bind_ и включаем автозапуск:
    ```shell
    systemctl enable --now named
    ```
