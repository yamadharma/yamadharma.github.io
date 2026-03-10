---
title: "GNS3. Образы оборудования"
author: ["Dmitry S. Kulyabov"]
date: 2022-05-07T15:47:00+03:00
lastmod: 2023-10-23T15:50:00+03:00
tags: ["network", "education"]
categories: ["computer-science"]
draft: false
slug: "gns3-appliances"
---

-   Сам по себе GNS3 является интерфейсом к виртуальным машинам.
-   Для моделирования сетей необходимо иметь ещё и образы операционных систем для разного оборудования.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Образы эмулируемых систем доступны в магазине: <https://gns3.com/marketplace>.


## <span class="section-num">2</span> Сетевые сервисы {#сетевые-сервисы}


### <span class="section-num">2.1</span> Networkers' Toolkit {#networkers-toolkit}

-   Название: Toolkit.
-   Магазин: <https://gns3.com/marketplace/appliances/networkers-toolkit>.
-   Виртуализация: docker.
-   Предоставляет услуги:
    -   www (nginx);
    -   ftp (vsftpd);
    -   tftp (tftpd);
    -   syslog (rsyslog);
    -   dhcp (isc-dhcpd);
    -   snmp server (snmpd + snmptrapd).


## <span class="section-num">3</span> Клиенты {#клиенты}


### <span class="section-num">3.1</span> Webterm {#webterm}

-   Магазин: <https://www.gns3.com/marketplace/appliances/webterm>.
-   Виртуализация: docker.
-   ОС: Debian Linux.
-   Набор сетевых инструментов:
    -   веб-броузер Firefox;
    -   утилиты: net-tools, iproute2, ping, traceroute, curl, host, iperf3, mtr, socat, ssh client, tcpdump;
    -   инструменты тестирования многоадресной рассылки msend/mreceive.


## <span class="section-num">4</span> Коммутаторы {#коммутаторы}


### <span class="section-num">4.1</span> Arista EOS {#arista-eos}

-   [Arista EOS]({{< relref "2022-07-16-arista-eos" >}})
-   [GNS3. Установка Arista EOS]({{< relref "2022-07-16-gns3-install-arista-eos" >}})


#### <span class="section-num">4.1.1</span> Arista vEOS {#arista-veos}

-   Виртуализация: qemu.
-   Архитектура: i386 и amd64.
-   Необходимо RAM: 2048 MB.
-   Система команд похожа на Cisco.


#### <span class="section-num">4.1.2</span> Arista cEOS {#arista-ceos}

-   Виртуализация: docker.
-   Архитектура: i386 и amd64.
-   Система команд похожа на Cisco.


### <span class="section-num">4.2</span> EXOS {#exos}

-   Репозиторий: <https://github.com/extremenetworks/Virtual_EXOS>
-   Как устанавливать на GNS3: <https://github.com/extremenetworks/Virtual_EXOS/blob/master/GNS3_EXOS-VM_Guide.md>
-   Аналоги в других операционных системах для коммутаторов: <https://documentation.extremenetworks.com/CLI_X-Ref/1.0/CLI_X-Ref_Guide_1.0.pdf>


## <span class="section-num">5</span> Маршрутизаторы {#маршрутизаторы}


### <span class="section-num">5.1</span> FreeRTR {#freertr}

-   Сайт: <http://www.freertr.org/>.
-   Репозиторий: <https://github.com/rare-freertr/freeRtr>.
-   Виртуализация: qemu.
-   Необходимо RAM: 2048 MB.
-   Реализован на Java.
-   Система команд похожа на Cisco.


### <span class="section-num">5.2</span> FRRouting {#frrouting}

-   [Маршрутизация. FRRouting]({{< relref "2022-06-02-routing-frrouting" >}})
-   Магазин: <https://www.gns3.com/marketplace/appliances/frr>.
-   Сайт: <https://frrouting.org/>.
-   Репозиторий: <https://github.com/FRRouting/frr>
-   Виртуализация: qemu.
-   Необходимо RAM: 256 MB.
-   Система команд похожа на Cisco.


#### <span class="section-num">5.2.1</span> Образы для GNS3 {#образы-для-gns3}

-   Неофициальные образы делаются для GNS3: <https://sourceforge.net/projects/gns-3/files/Qemu%20Appliances/>.
-   Фактически это Debian  с подсистемой FRRouting. При запуске сразу открывается оболочка _vtysh_.


### <span class="section-num">5.3</span> VyOS {#vyos}

-   [Маршрутизация. VyOS]({{< relref "2022-06-03-routing-vyos" >}})
-   [GNS3. Образ VyOS]({{< relref "2022-07-14-gns3-vyos" >}})
-   Магазин: <https://www.gns3.com/marketplace/appliances/vyos>.
-   Сайт: <https://vyos.net/>.
-   Коммерческий сайт: <https://vyos.io/>.
-   Репозиторий: <https://github.com/vyos/vyos-1x>
-   Виртуализация: qemu.
-   Необходимо RAM: 512 MB.
-   Система команд похожа на Juniper.
-   Образы для vyos-1.1: <https://sourceforge.net/projects/gns-3/files/Qemu%20Appliances/>.
