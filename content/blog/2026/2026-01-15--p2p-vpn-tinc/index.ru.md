---
title: "Пиринговые VPN. tinc"
author: ["Dmitry S. Kulyabov"]
date: 2026-01-15T16:24:00+03:00
lastmod: 2026-10-25T14:12:00+03:00
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


### <span class="section-num">3.2</span> VyOS {#vyos}

-   [VyOS. Установка tinc]({{< relref "2026-10-24--vyos-tinc-install" >}})


## <span class="section-num">4</span> Настройка {#настройка}

-   [VPN. Настройка tinc]({{< relref "2026-10-25--vpn-tinc-configure" >}})


## <span class="section-num">5</span> Команды {#команды}


### <span class="section-num">5.1</span> Просмотр топологии и состояния сети {#просмотр-топологии-и-состояния-сети}

-   Команды следует дополнить именем сети: `-n $VPNNMAME`.
-   `tinc top` : открывает терминальный интерфейс, показывающий пакеты и трафик по каждому узлу.
-   `tinc dump nodes` : выводит список всех известных узлов в VPN
-   `tinc dump reachable nodes` : только те узлы, которые доступны прямо сейчас.
-   `tinc dump edges` : список всех известных прямых соединений (рёбер) между узлами в сети.
-   `tinc dump subnets` : список всех подсетей, привязанных к конкретным узлам.
-   `tinc dump connections` : мета-соединения (управляющие каналы) между вашим узлом и другими демонами.
-   `tinc dump graph` (или `digraph`) : выводит граф VPN-сети в формате `dotty` (Graphviz):
    ```shell
    sudo tinc -n $VPNNMAME dump graph | dot -Tpng -o /tmp/tinc_topology.png
    sudo tinc -n $VPNNMAME dump graph | dot -Tsvg | swayimg -v -
    ```
