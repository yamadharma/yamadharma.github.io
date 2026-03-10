---
title: "Анализатор протоколов Wireshark"
author: ["Dmitry S. Kulyabov"]
date: 2021-08-18T18:29:00+03:00
lastmod: 2023-09-19T16:42:00+03:00
tags: ["network"]
categories: ["computer-science"]
draft: false
slug: "wireshark-protocol-analyzer"
---

Анализатор протоколов _Wireshark_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.wireshark.org/>
-   Впервые выпущен в 1998 году.
-   Первоначальное название --- _Ethereal_.
-   Разработчикам пришлось изменить название на _Wireshark_ в 2006 году из-за проблем с товарными знаками.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Установка в разных операционных системах {#установка-в-разных-операционных-системах}

-   Windows (менеджер пакетов Chocolatey: [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
    ```shell
    choco install wireshark
    choco install winpcap
    ```
-   Linux
    -   Gentoo
        ```shell
        emerge wireshark
        ```
    -   Ubuntu
        ```shell
        sudo apt-get install wireshark
        ```
    -   Fedora
        ```shell
        sudo dnf install wireshark
        ```


### <span class="section-num">2.2</span> Запуск без административных привилегий {#запуск-без-административных-привилегий}

-   Административные полномочия требуются для захвата пакетов.


#### <span class="section-num">2.2.1</span> Linux {#linux}

<!--list-separator-->

1.  Ограничение разрешения на захват для группы

    <!--list-separator-->

    1.  Произвольный дистрибутив Linux

        -   Необходимо установить права доступа к файлу `/usr/sbin/dumpcap`.
        -   Предположим, что это группа `wireshark`.
        -   Создайте группу `wirehark` и добавьте в неё пользователя `user_name`.
            ```shell
            sudo -i
            groupadd -s wireshark
            gpasswd -a -G wireshark user_name
            ```
        -   Изменим параметры файла `/usr/sbin/dumpcap`:
            ```shell
            sudo -i
            chgrp wireshark /usr/bin/dumpcap
            chmod 750 /usr/bin/dumpcap
            ```
        -   Кроме того, зададим _capabilities_ для этого файла:
            ```shell
            setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap
            ```

            -   Можно проверить, что параметры установлены правильно:
                ```shell
                getcap /usr/bin/dumpcap
                ```

        -   После этого можно перелогиниться или временно добавить себя в новую группу:
            ```shell
            newgrp wireshark
            ```

    <!--list-separator-->

    2.  Ubuntu

        -   Нужно выполнить следующие действия:
            ```shell
            sudo -i
            apt-get install wireshark
            apt-get install pcaputils
            dpkg-reconfigure wireshark-common
            groupadd wireshark
            usermod -a -G wireshark user_name
            ```
        -   После этого можно перелогиниться или временно добавить себя в новую группу:
            ```shell
            newgrp wireshark
            ```

    <!--list-separator-->

    3.  Gentoo

        -   В Gentoo для захвата используется группа `pcap`.
        -   Выполните следующее:
            ```shell
            sudo -i
            usermod -a -G pcap user_name
            ```
        -   После этого можно перелогиниться или временно добавить себя в новую группу:
            ```shell
            newgrp pcap
            ```


#### <span class="section-num">2.2.2</span> Windows {#windows}

-   Драйвер `WinPcap` (`NPF`) загружается Wireshark, когда он начинает собирать данные в реальном времени.
-   Для этого требуются права администратора.
-   Остановка Wireshark не останавливает драйвер WinPcap.
-   При установке драйвера WinPcap через Chocolatey он устанавливается для автоматического запуска с полномочиями администратора.

<!--list-separator-->

1.  Запуск Wireshark под администратором

    -   Самый простой вариант, но не безопасный.

<!--list-separator-->

2.  Запуск драйвера NPF под администратором вручную

    -   Запустите драйвер NPF:
        ```shell
        runas /u:administrator "net start npf"
        ```
    -   После этого можно работать с Wireshark.
    -   Остановите драйвер NPF:
        ```shell
        runas /u:administrator "net stop npf"
        ```

<!--list-separator-->

3.  Запуск драйвера NPF под администратором автоматически при старте системы

    -   Запустите под администратором:
        ```shell
        sc config npf start=auto
        ```
    -   Или в `Device Manager` выберите `View->Show hidden devices`, откройте `Non-Plug and Play Drivers`. Потом настройте запуск `NetGroup Packet Filter Driver`.


#### <span class="section-num">2.2.3</span> BSD, MacOS {#bsd-macos}

-   Для захвата пакетов необходим доступ для чтения к устройствам BPF в `/dev/bpf*`.
-   Поскольку в MacOS используется `devfs`, изменения не сохраняется между перезагрузками.


### <span class="section-num">2.3</span> Видео {#видео}


#### <span class="section-num">2.3.1</span> Установка на Windows {#установка-на-windows}

{{< youtube YZDTGFu4vGQ >}}


#### <span class="section-num">2.3.2</span> Установка на Ubuntu Linux {#установка-на-ubuntu-linux}

{{< youtube M-b_nox14io >}}


#### <span class="section-num">2.3.3</span> Установка на Fedora Linux {#установка-на-fedora-linux}

{{< youtube NtAGouu6ncU >}}


## <span class="section-num">3</span> Терминальный вариант Wireshark {#терминальный-вариант-wireshark}


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   Сайт: <https://tshark.dev/>
-   _TShark_ --- анализатор сетевых протоколов, терминальный вариант Wireshark.
-   Без настроек _TShark_ будет работать так же, как tcpdump.
-   Будет использовать библиотеку `pcap` для захвата трафика с первого доступного сетевого интерфейса и отображать сводную строку в стандартном выводе для каждого полученного пакета.


### <span class="section-num">3.2</span> Пример использования {#пример-использования}

-   Например, чтобы перехватить пакеты через указанный сетевой интерфейс и сохранить результаты, введите:
    ```shell
    tshark -i eth0 -w capture-eth0.pcap
    ```
-   Цветной вывод текста требуется терминал с поддержкой 24-битного цвета:
    ```shell
    tshark -i any --color
    ```
-   Показывать только типы файлов, начинающиеся с `test`:
    ```shell
    shark -Y 'http.content_type[0:4] == "text"'
    ```
-   Показать только _JavaScript_:
    ```shell
    tshark -Y tshark -i wlp2s0 -Y 'http.content_type contains "javascript"'
    ```
-   Показать все http с content-type="image/(gif|jpeg|png|etc)":
    ```shell
    tshark -Y 'http.content_type[0:5] == "image"'
    ```
-   Показать все http с content-type="image/gif":
    ```shell
    tshark -Y http.content_type == "image/gif"
    ```
-   Не показывать контент http, только заголовки:
    ```shell
    tshark -Y http.response !=0 || http.request.method != "TRACE"
    ```
-   Для сопоставления IP-адресов, заканчивающихся на 255, в блоке подсетей (от 172.16 до 172.31):
    ```shell
    tshark -Y string(ip.dst) matches r"^172\.(1[6-9]|2[0-9]|3[0-1])\.[0-9]{1,3}\.255
    ```
-   Для сопоставления нечетных номеров кадров:
    ```shell
    tshark -Y string(frame.number) matches "[13579]$"
    ```
-   Печать http-данных в вик дерева:
    ```shell
    tshark -q -i any -Y http -z http,tree
    ```
