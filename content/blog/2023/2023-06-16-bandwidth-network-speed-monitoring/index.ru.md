---
title: "Мониторинг пропускной способности и скорости сети"
author: ["Dmitry S. Kulyabov"]
date: 2023-06-16T11:34:00+03:00
lastmod: 2024-03-02T20:54:00+03:00
tags: ["network"]
categories: ["computer-science"]
draft: false
slug: "bandwidth-network-speed-monitoring"
---

Утилиты мониторинга пропускной способности и скорости сети.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Утилиты мониторинга {#утилиты-мониторинга}


### <span class="section-num">1.1</span> speedtest-cli {#speedtest-cli}


#### <span class="section-num">1.1.1</span> Общая информация {#общая-информация}

-   Тестирование пропускной способности интернета с помощью сервиса <https://www.speedtest.net/>.
-   Репозитоий: <https://github.com/sivel/speedtest-cli>.


#### <span class="section-num">1.1.2</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge net-analyzer/speedtest-cli
    ```


#### <span class="section-num">1.1.3</span> Использование {#использование}

-   Простейшее использование:
    ```shell
    speedtest-cli
    ```


### <span class="section-num">1.2</span> NetHogs {#nethogs}


#### <span class="section-num">1.2.1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/raboof/nethogs>.
-   Группирует пропускную способность по процессам.
-   Берёт информацию из `/proc`.


#### <span class="section-num">1.2.2</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge net-analyzer/nethogs
    ```


#### <span class="section-num">1.2.3</span> Использование {#использование}

-   Простейшее использование:
    ```shell
    nethogs
    ```
-   Можно указать устройства после команды:
    ```shell
    nethogs eth0
    ```
-   Дополнительные опции:
    -   выбор задержки для частоты обновления (`-d`);
    -   режим трассировки (`-t`).


### <span class="section-num">1.3</span> nload {#nload}


#### <span class="section-num">1.3.1</span> Общая информация {#общая-информация}

-   Сайт: <http://www.roland-riegel.de/nload/index.html>
-   Отслеживает сетевой трафик и использование полосы пропускания в режиме реального времени.
-   Визуализирует входящий и исходящий трафик с помощью консольных графиков.


#### <span class="section-num">1.3.2</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge net-analyzer/nload
    ```


#### <span class="section-num">1.3.3</span> Использование {#использование}

-   Простейшее использование:
    ```shell
    nload
    ```


### <span class="section-num">1.4</span> vnStat {#vnstat}


#### <span class="section-num">1.4.1</span> Общая информация {#общая-информация}

-   Сайт: <https://humdi.net/vnstat/>
-   Консольный монитор сетевого трафика.
-   Использует в качестве источника информации статистику сетевого интерфейса, предоставляемую ядром (не перехватывает трафик).
-   Может быть запущена без прав `root`.


#### <span class="section-num">1.4.2</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge net-analyzer/vnstat
    ```


#### <span class="section-num">1.4.3</span> Использование {#использование}

-   Простейшее использование:
    ```shell
    vnstat
    ```


### <span class="section-num">1.5</span> iftop {#iftop}


#### <span class="section-num">1.5.1</span> Общая информация {#общая-информация}

-   Сайт: <http://www.ex-parrot.com/pdw/iftop/>
-   Репозитоий: <https://code.blinkace.com/pdw/iftop>
-   Выдаёт постоянно обновляемый список сетевых соединений между парами хостов.
-   По умолчанию соединения упорядочены по использованию полосы пропускания.


#### <span class="section-num">1.5.2</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge net-analyzer/iftop
    ```


#### <span class="section-num">1.5.3</span> Использование {#использование}

-   Простейшее использование:
    ```shell
    iftop
    ```


## <span class="section-num">2</span> Генераторы трафика {#генераторы-трафика}


### <span class="section-num">2.1</span> iPerf {#iperf}


#### <span class="section-num">2.1.1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/esnet/iperf>
-   Используется для измерения и настройки производительности сети.
-   Состоит из клиента и сервера.
-   Может создавать потоки данных для измерения пропускной способности.
-   Две реализации:
    -   `iPerf2` (оригинальный iPerf)
        -   Сайт: <https://sourceforge.net/projects/iperf2/>.
    -   `iPerf3`
        -   Репозиторий: <https://github.com/esnet/iperf>
-   Эти реализации несовместимы (<https://iperf2.sourceforge.io/IperfCompare.html>).


#### <span class="section-num">2.1.2</span> Установка {#установка}

-   Gentoo:
    -   `iPerf2`
        ```shell
        emerge net-misc/iperf:2
        ```
    -   `iPerf3`
        ```shell
        emerge net-misc/iperf:3
        ```


#### <span class="section-num">2.1.3</span> Использование {#использование}

-   Простейшее использование:
    -   Запустите сервер:
        ```shell
        iperf3 -s
        ```
    -   Запустите клиента:
        ```shell
        iperf3 -c <server_address>
        ```
