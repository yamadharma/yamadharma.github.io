---
title: "Web консоль Cockpit"
author: ["Dmitry S. Kulyabov"]
date: 2022-01-18T17:23:00+03:00
lastmod: 2023-09-28T20:31:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "cockpit-web-console"
---

_Cockpit_ представляет собой инструмент для администрирования устройств под управлением Linux.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


## <span class="section-num">2</span> Функционал {#функционал}

-   управление службами;
-   менеджмент учетных записей;
-   настройка брандмауэра;
-   конфигурирование сетевых интерфейсов и подключений;
-   чтение системных логов;
-   контроль над виртуальными машинами;
-   формирование отчетов на базе результатов диагностики;
-   настройка дампа ядра;
-   администрирование SELinux (Security-Enhanced Linux);
-   обновление пакетов приложений;
-   управление подписками.


## <span class="section-num">3</span> Установка {#установка}


### <span class="section-num">3.1</span> Установка в RedHat и деривативах: {#установка-в-redhat-и-деривативах}

-   Centos 7
    ```shell
    yum install cockpit
    ```
-   Centos 8
    ```shell
    dnf install cockpit
    ```

    -   В CentOS 8 _cockpit_ устанавливается по умолчанию.
-   Запуск служб
    ```shell
    systemctl enable --now cockpit.socket
    ```
-   Настройка брандмауэра
    ```shell
    firewall-cmd --add-service=cockpit --permanent
    firewall-cmd --reload
    ```


### <span class="section-num">3.2</span> Дополнительные модули {#дополнительные-модули}

-   cockpit-composer
-   cockpit-dashboard
    -   Улучшенный дашборд для сервера.
-   cockpit-doc
-   cockpit-docker
-   cockpit-kubernetes
-   cockpit-machines
    -   Работа с виртуальными машинами KVM.
-   cockpit-machines-ovirt
-   cockpit-packagekit
    -   Работа с пакетами.
    -   Установка:
        ```shell
        yum install cockpit-packagekit
        ```
    -   Установка необходимого программного обеспечения:
        ```shell
        yum install virt-install
        ```
-   cockpit-pcp
-   cockpit-storaged
    -   Работа с устройствами хранения.
-   cockpit-subscriptions
-   cockpit-tests


## <span class="section-num">4</span> Веб-интерфейс приложения {#веб-интерфейс-приложения}

-   Используется порт `9090`.
-   По умолчанию используется самоподписанный сертификат SSL.
-   Язык лучше выбрать английский. Русский перевод крайне прискорбен.
