---
title: "GNS3. Установка Arista EOS"
author: ["Dmitry S. Kulyabov"]
date: 2022-07-16T12:14:00+03:00
lastmod: 2023-07-19T15:54:00+03:00
tags: ["network", "modeling"]
categories: ["computer-science"]
draft: false
slug: "gns3-install-arista-eos"
---

Установка Arista EOS в GNS3.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий образов: <https://www.arista.com/en/support/software-download>.
    -   Требуется регистрация.
    -   Блокируются российские ip-адреса.


## <span class="section-num">2</span> Особенности конфигурации {#особенности-конфигурации}

-   В старших версиях (наверное, начиная с 4.21) конфигурация по умолчанию скорее похожа на маршрутизатор, чем на коммутатор.
-   Например, на всех портах установлен режим `no switchposrt`.


## <span class="section-num">3</span> Варианты образов {#варианты-образов}


### <span class="section-num">3.1</span> Arista vEOS {#arista-veos}

-   Виртуализация: qemu.
-   Архитектура: i386 и amd64.
-   Необходимо RAM: 2048 MB.
-   Система команд похожа на Cisco.


#### <span class="section-num">3.1.1</span> Порядок установки {#порядок-установки}

-   Для примера будем рассматривать образы:
    -   `Aboot-veos-serial-8.0.0.iso`: <https://www.arista.com/custom_data/aws3-explorer/download-s3-file.php?f=/support/download/vEOS-lab/Aboot/Aboot-veos-serial-8.0.0.iso>
    -   `vEOS-lab-4.18.10M`: <https://www.arista.com/custom_data/aws3-explorer/download-s3-file.php?f=/support/download/vEOS-lab/4.18/vEOS-lab-4.18.10M.vmdk>
-   Не следует устанавливать сохранение для образов _Qemu_ в _GNS3_.


#### <span class="section-num">3.1.2</span> Видео: Установка Arista vEOS на GNS3 {#видео-установка-arista-veos-на-gns3}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube b793370d31c54e74d18e7c6a1aff51e2 >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube jWBFlSdN8Lc >}}

{{< /rtab >}}
{{< /tabs >}}


### <span class="section-num">3.2</span> Arista cEOS {#arista-ceos}

-   Виртуализация: docker.
-   Архитектура: i386 и amd64.
-   Система команд похожа на Cisco.


#### <span class="section-num">3.2.1</span> Порядок установки {#порядок-установки}

-   Скачать образ.
-   Скопируйте файл на виртуальную машину.

<!--list-separator-->

1.  cEOS 4.20.5F

    -   Для примера будем рассматривать `cEOS-lab-4.20.5F`: <https://www.arista.com/custom_data/aws3-explorer/download-s3-file.php?f=/support/download/cEOS-lab/EOS-4.20.5F/cEOS-lab-4.20.5F.tar.xz>
    -   Для версии `4.20.5F`:
        ```shell
        docker import cEOS-lab-4.20.5F.tar.xz ceosimage:4.20.5F
        echo "rm /etc/systemd/system/getty.target.wants/getty@tty1.service" | \
        docker run --name=ceos-container -e CEOS=1 -e container=docker -e EOS_PLATFORM=ceossim -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e ETBA=1 -e INTFTYPE=eth -i ceosimage:4.20.5F sh
        docker commit --change='CMD ["/sbin/init"]' --change='VOLUME /mnt/flash' ceos-container ceosimage:GNS3
        docker rm ceos-container
        ```
    -   Для работы следует залогиниться под учётной записью `admin`.

<!--list-separator-->

2.  cEOS новее, чем 4.20.5F

    -   Установите docker-образ (для произвольной версии):
        ```shell
        docker import cEOS-lab-<version>.tar.xz ceosimage:<version>
        echo "rm /etc/systemd/system/getty.target.wants/getty@tty1.service" | \
        docker run --name=ceos-container -e CEOS=1 -e container=docker -e EOS_PLATFORM=ceoslab -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e ETBA=1 -e INTFTYPE=eth -i ceosimage:<version> sh
        docker commit --change='CMD ["/sbin/init"]' --change='VOLUME /mnt/flash' ceos-container ceosimage:GNS3
        docker rm ceos-container
        ```
    -   Для примера будем рассматривать `cEOS-lab-4.28.1F`: <https://www.arista.com/custom_data/aws3-explorer/download-s3-file.php?f=/support/download/cEOS-lab/EOS-4.28.1F/cEOS-lab-4.28.1F.tar.xz>
    -   Например, для версии `4.28.1F` команды выглядят следующим образом:
        ```shell
        docker import cEOS-lab-4.28.1F.tar.xz ceosimage:4.28.1F
        echo "rm /etc/systemd/system/getty.target.wants/getty@tty1.service" | \
        docker run --name=ceos-container -e CEOS=1 -e container=docker -e EOS_PLATFORM=ceoslab -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e ETBA=1 -e INTFTYPE=eth -i ceosimage:4.28.1F sh
        docker commit --change='CMD ["/sbin/init"]' --change='VOLUME /mnt/flash' ceos-container ceosimage:GNS3
        docker rm ceos-container
        ```
    -   У меня возникли проблемы при загрузке.


#### <span class="section-num">3.2.2</span> Видео: Установка Arista cEOS на GNS3 {#видео-установка-arista-ceos-на-gns3}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube b970b6b886687d7a4cf5429b9251b09e >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube X3Rd-mSZPQk >}}

{{< /rtab >}}
{{< /tabs >}}
