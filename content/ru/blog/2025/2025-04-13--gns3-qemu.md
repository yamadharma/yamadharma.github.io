---
title: "GNS3 на Qemu"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-13T15:12:00+03:00
lastmod: 2025-04-13T17:41:00+03:00
tags: ["modeling", "education"]
categories: ["science", "computer-science"]
draft: false
slug: "gns3-qemu"
---

GNS3 на Qemu

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Подготовка {#подготовка}

-   Скачайте образ виртуальной машины GNS3:
    ```shell
    export GNS3_VERSION=3.0.4; \
    wget https://github.com/GNS3/gns3-gui/releases/download/v${GNS3_VERSION}/GNS3.VM.KVM.${GNS3_VERSION}.zip; \
    unzip GNS3.VM.KVM.${GNS3_VERSION}.zip; \
    rm GNS3.VM.KVM.${GNS3_VERSION}.zip
    ```


## <span class="section-num">2</span> Запуск {#запуск}

-   В комплекте идёт скрипт для запуска.
-   Часть, ответственная за запуск виртуальной машины:
    ```shell
    qemu-system-x86_64 -name "GNS3 VM" -m 2048M -cpu host -enable-kvm -machine smm=off -boot order=c \
    -drive file="GNS3 VM-disk001.qcow2",if=virtio,index=0,media=disk \
    -drive file="GNS3 VM-disk002.qcow2",if=virtio,index=1,media=disk \
    -device virtio-net-pci,netdev=nic0 -netdev tap,id=nic0,ifname=tap-gns3vm,script=no,downscript=no
    ```
-   Параметры:
    -   `-name` : имя виртуальной машины;
    -   `-drive` : - путь к образу диска;
    -   `-m` : объём оперативной памяти.
-   Рекомендуется изменить объём оперативной памяти для машины (например, 8G):
    ```shell
    -m 8196M
    ```
-   Можно добавить ещё количество ядер (например, 2 ядра):
    ```shell
    -smp 2
    ```
-   Запустите скрипт `start-gns3vm.sh`:
    ```shell
    ./start-gns3vm.sh
    ```
-   Пропингуйте адрес машины.
-   Если не пингуется, то перегрузите виртуальную машину.


## <span class="section-num">3</span> Конфигурация GNS3 {#конфигурация-gns3}

-   При конфигурации используйте опцию _Connect to remote controller_.
-   Настройте адрес виртуальной машины на основе информационной заставки виртуальной машины (пример):
    -   Host: 192.168.122.76
    -   Port: 80 TCP


## <span class="section-num">4</span> Проблемы {#проблемы}


### <span class="section-num">4.1</span> Элемент NAT {#элемент-nat}

-   При попытке добавить элемент NAT получаем ошибку:

    > Error while creating node from template: NAT interface virbr0 is missing, please install libvirt
-   Так и не разобрался.
-   Вместо NAT использовал Cloud.
