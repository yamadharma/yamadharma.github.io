---
title: "bittorrent. Трекер opentracker"
author: ["Dmitry S. Kulyabov"]
date: 2024-01-31T21:15:00+03:00
lastmod: 2024-02-04T19:18:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "bittorrent-opentracker"
---

Трекер Opentracker.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://erdgeist.org/arts/software/opentracker/>
-   Репозиторий: <https://erdgeist.org/gitweb/opentracker/>


### <span class="section-num">1.1</span> Трекер {#трекер}

-   BitTorrent --- пиринговый (P2P) сетевой протокол для кооперативного обмена файлами через Интернет.
-   Файлы передаются частями, каждый torrent-клиент, получая (скачивая) эти части, в то же время отдаёт (закачивает) их другим клиентам, что снижает нагрузку и зависимость от каждого клиента-источника и обеспечивает избыточность данных.
-   Перед началом скачивания клиент подсоединяется к трекеру по адресу, указанному в торрент-файле, сообщает ему свой адрес и хеш-сумму торрент-файла, на что в ответ клиент получает адреса других клиентов, скачивающих или раздающих этот же файл.
-   Торрент-трекер по сути представляет собой http-сервер, который собирает IP-адреса всех клиентов в пулы, отсортированные по одному из параметров строки запроса, и отвечает всем остальным клиентам, которые указали этот же самый параметр, списком всех других недавних клиентов.


## <span class="section-num">2</span> Установка {#установка}

-   Устанавливается из исходников.
-   Установите окружение для разработки.
    -   RockyLinux (см. [Rocky Linux. Установка сервера]({{< relref "2022-08-12-rockylinux-server-installation" >}})):
        ```shell
        dnf -y group install "Development Tools"
        dnf -y install git
        dnf -y install cvs
        ```
-   Подготовьте opentracker к компиляции:
    ```shell
    cvs -d :pserver:cvs@cvs.fefe.de:/cvs -z9 co libowfat
    cd libowfat
    make
    cd ..
    git clone git://erdgeist.org/opentracker
    cd opentracker
    ```
-   Настройте параметры `FEATURES` в `Makefile`.
    -   `-DWANT_V6` : делает opentracker трекером только для IPv6;
    -   `-DWANT_COMPRESSION_GZIP` : использовать сжатие gzip;
    -   `-DWANT_ACCESSLIST_BLACK`, `-DWANT_ACCESSLIST_WHITE` : обычно opentracker отслеживает любой анонсированный ему торрент, но можно использовать белый и чёрный списки (файл белого списка при этом обязателен);
    -   `-DWANT_SYNC_LIVE` : работа в кластере (необходимо обязательно настроить кластер);
    -   `-DWANT_RESTRICT_STATS` : ограничение доступа к статистике;
    -   `-DWANT_FULLSCRAPE` : возможность запросить у трекера все отслеживаемые торренты (включено по умолчанию);
    -   `-DWANT_IP_FROM_QUERY_STRING` : клиенты могут указывать IP-адрес в строке запроса (по умолчанию opentracker разрешает объявлять только IP-адрес подключающейся конечной точки).
-   Настроек по умолчанию чаще всего будет достаточно.
-   Скомпилируйте opentracker:
    ```shell
    make
    ```
-   Скопируйте исполняемый файл:
    ```shell
    cp opentracker /usr/local/bin/
    ```
-   Скопируйте конфигурационный файл:
    ```shell
    mkdir -p /etc/opentracker
    cp opentracker.conf.sample /etc/opentracker/opentracker.conf
    ```
-   Создайте юнит systemd:
    ```conf-unix
    # /etc/systemd/system/opentracker.service
    [Unit]
    Description=Opentracker
    Wants=network-online.target
    After=network.target network-online.target

    [Service]
    ExecStart=/usr/local/bin/opentracker -f /etc/opentracker/opentracker.conf
    ExecReload=/bin/kill -s HUP $MAINPID
    Restart=on-abort

    [Install]
    WantedBy=multi-user.target
    ```
-   Запустите сервис:
    ```shell
    systemctl enable --now opentracker.service
    ```
