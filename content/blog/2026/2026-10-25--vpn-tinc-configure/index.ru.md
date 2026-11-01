---
title: "VPN. Настройка tinc"
author: ["Dmitry S. Kulyabov"]
date: 2026-10-25T13:52:00+03:00
lastmod: 2026-10-25T13:54:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "vpn-tinc-configure"
---

VPN. Настройка tinc 1.1.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Обозначения {#обозначения}

-   &lt;VPNNAME&gt; : имя, которое вы хотите присвоить вашей сети.
-   &lt;IPNET&gt; внутренняя IP сеть для сети &lt;VPNNAME&gt;.
-   &lt;IPNET&gt; внутренний IP адрес, который вы хотите присвоить вашему текущему устройству.
    -   Распределение IP-адресов в режиме маршрутизатора (по умолчанию) осуществляется вручную, поэтому вам необходимо следить за назначенными адресами.
-   &lt;FQDNORIP&gt; : полное доменное имя или IP-адрес хоста, который вы настраиваете.
-   &lt;HOSTNAME&gt; : имя хоста.


## <span class="section-num">2</span> Брандмауэр {#брандмауэр}

-   Открыть порт 655/udp.
-   firewalld:
    ```shell
    firewall-cmd --add-service=tinc --permanent
    firewall-cmd --reload
    ```


## <span class="section-num">3</span> Настройка интерфейса Linux {#настройка-интерфейса-linux}

-   Настраивается на всех машинах.
-   Создайте файл запуска интерфейса:
    ```shell
    sudo cat>/etc/tinc/${VPNNAME}/tinc-up <<EOL
    #!/bin/bash

    ip link set \${INTERFACE} up
    ## Change this address per-host to match the hosts/hostname file!
    ip addr add <IP>/32 dev \${INTERFACE}
    ip route add <IPNET> dev \${INTERFACE}

    ## add domain per interface
    resolvectl domain ${VPNNAME} ~${VPNNAME}.internal
    EOL
    ```
-   Создайте файл остановки интерфейса:
    ```shell
    sudo cat>/etc/tinc/${VPNNAME}/tinc-down <<EOL
    #!/bin/bash

    ip route del <IPNET> dev \${INTERFACE}

    # Change this address per-host to match the hosts/hostname file!
    ip addr del <IP>/32 dev \${INTERFACE}

    ip link set \${INTERFACE} down
    EOL
    ```


## <span class="section-num">4</span> Первая машина {#первая-машина}

-   Машина должна иметь внешний IP-адрес.


### <span class="section-num">4.1</span> Создание сети {#создание-сети}

-   Создайте сеть:
    ```shell
    sudo tinc -n <VPNNAME> init <HOSTNAME>
    ```
-   Запустите сервер с включённой отладкой:
    ```shell
    sudo tincd -n <VPNNAME> -D -d3
    ```
-   Подключите сеть:
    ```shell
    sudo tinc -n <VPNNAME> add subnet <IP>/32
    ```
-   Подключите текущую машину:
    ```shell
    sudo tinc -n <VPNNAME> add address=<FQDNORIP>
    ```
-   Остановите демон и поместите его в автозагрузку:
    ```shell
    systemctl enable --now tinc.service
    systemctl enable --now tinc@<VPNAME>.service
    ```


## <span class="section-num">5</span> Подключение других устройств {#подключение-других-устройств}

-   В следующих командах замените &lt;CLIENTNAME&gt; именем, которое вы хотите присвоить устройству.
-   Сгенерируйте ссылку-приглашение на компьютере, к которому вы хотите подключиться:
    ```shell
    sudo tinc -n <VPNNAME> invite <CLIENTNAME>
    ```
-   Это выведет &lt;INVITEURL&gt;.
-   Подключитесь к приглашению:
    ```shell
    sudo tinc -n <VPNNAME> join <INVITEURL>
    ```
-   Подключитесь к VPN (с отладкой):
    ```shell
    sudo tincd -n <VPNNAME> -D
    ```
-   Подключите хост:
    ```shell
    sudo tinc -n <VPNNAME> add subnet <IP>/32
    ```
-   Создайте скрипты для интерфейса.
-   Остановите демон и поместите его в автозагрузку:
    ```shell
    systemctl enable --now tinc.service
    systemctl enable --now tinc@<VPNAME>.service
    ```
