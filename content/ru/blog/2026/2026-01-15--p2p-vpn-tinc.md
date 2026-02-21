---
title: "Пиринговые VPN. tinc"
author: ["Dmitry S. Kulyabov"]
date: 2026-01-15T16:24:00+03:00
lastmod: 2026-02-03T11:09:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "p2p-vpn-tinc"
---

Пиринговые VPN. tinc.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://tinc-vpn.org>
-   Репозиторий: <https://github.com/gsliepen/tinc>


### <span class="section-num">1.1</span> Android {#android}

-   Сайт: <https://tincapp.euxane.eu>


### <span class="section-num">1.2</span> Особенности {#особенности}

-   Распределенная топология (нет необходимости в отдельном сервере VPN).
-   Работает поверх сетей любой топологии, в том числе за NAT и поверх других VPN.
-   Поддерживает активное соединение даже после переключения сети (например с wi-fi на 4g) или при входе и выходе из других VPN.
-   Реализации для большинства операционных систем.


## <span class="section-num">2</span> Версии {#версии}

-   Две версии:
    -   tinc-1.0, стабильная (все операции по обмену ключами делаются вручную);
    -   tinc-1.1 (большая часть операций автоматизирована).
-   Для автоматизации операций для tinc-1.0. можно использовать проект tinc-boot.


### <span class="section-num">2.1</span> tinc-boot {#tinc-boot}

-   Репозиторий: <https://github.com/reddec/tinc-boot>


## <span class="section-num">3</span> Установка {#установка}


### <span class="section-num">3.1</span> Gentoo {#gentoo}

-   Находится в основном репозитории:
    ```shell
    emerge --ask net-vpn/tinc
    ```


## <span class="section-num">4</span> Настройка tinc 1.1 {#настройка-tinc-1-dot-1}


### <span class="section-num">4.1</span> Обозначения {#обозначения}

-   &lt;VPNNAME&gt; : имя, которое вы хотите присвоить вашей сети.
-   &lt;IPNET&gt; внутренняя IP сеть для сети &lt;VPNNAME&gt;.
-   &lt;IPNET&gt; внутренний IP адрес, который вы хотите присвоить вашему текущему устройству.
    -   Распределение IP-адресов в режиме маршрутизатора (по умолчанию) осуществляется вручную, поэтому вам необходимо следить за назначенными адресами.
-   &lt;FQDNORIP&gt; : полное доменное имя или IP-адрес хоста, который вы настраиваете.
-   &lt;HOSTNAME&gt; : имя хоста.


### <span class="section-num">4.2</span> Брандмауэр {#брандмауэр}

-   Открыть порт 655/udp.
-   firewalld:
    ```shell
    firewall-cmd --add-service=tinc --permanent
    firewall-cmd --reload
    ```


### <span class="section-num">4.3</span> Настройка интерфейса Linux {#настройка-интерфейса-linux}

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


### <span class="section-num">4.4</span> Первая машина {#первая-машина}

-   Машина должна иметь внешний IP-адрес.


#### <span class="section-num">4.4.1</span> Создание сети {#создание-сети}

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


### <span class="section-num">4.5</span> Подключение других устройств {#подключение-других-устройств}

-   В следующих командах замените &lt;CLIENTNAME&gt; именем, которое вы хотите присвоить устройству.
-   Сгенерируйте ссылку-приглашение на компьютере, к которому вы хотите подключиться:
    ```shell
    sudo tinc -n <VPNNAME> invite <CLIENTNAME>
    ```
-   Это выведет &lt;INVITEURL&gt;.
-   Подключитесь к приглашению:
    ```shell
    sudo tinc join <INVITEURL>
    ```
-   Подключитесь к VPN (с отладкой):
    ```shell
    sudo tincd -n <VPNNAME>
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
