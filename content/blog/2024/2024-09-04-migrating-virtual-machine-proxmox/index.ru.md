---
title: "Перенос виртуальной машины на Proxmox"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-04T16:58:00+03:00
lastmod: 2025-08-12T12:07:00+03:00
tags: ["linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "migrating-virtual-machine-proxmox"
---

Перенос виртуальной машины на Proxmox.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Перенос образа kvm {#перенос-образа-kvm}


### <span class="section-num">1.1</span> Создание виртуальной машины {#создание-виртуальной-машины}

-   Создадим виртуальную машину в Proxmox с помощью графической утилиты или утилиты командной строки `qm`.


#### <span class="section-num">1.1.1</span> Графический интерфейс {#графический-интерфейс}

-   Вкладка _General_. Идентификатор виртуальной машины (VM ID) будет задан автоматически (следующий свободный).
-   Вкладка _OS_. Операционная система выбирает _Do Not Use Any Media_.
-   Вкладка _Disk_. Удалите диск по умолчанию `scsi0`.


#### <span class="section-num">1.1.2</span> Интерфейс командной строки {#интерфейс-командной-строки}

-   Выберите свободный идентификатор машины:
    ```shell
    qm list
    ```
-   Пусть идентификатор машины будет 111 (для определённости).
-   Рекомендуется использовать на всех виртуальных машинах _qemu agent_, для обеспечения взаимодействия между гипервизором и виртуальной машиной (см. [KVM. QEMU Guest Agent]({{< relref "2024-09-05-kvm-qemu-guest-agent" >}})).
-   Создадим виртуальную машину:
    ```shell
    qm create 111 --name vm111 --bootdisk scsi0 --net0 virtio,bridge=vmbr0,firewall=1,mtu=1,tag=100 --agent enabled=1 --scsihw virtio-scsi-pci
    ```

    -   здесь у нас используется VLAN=100;
    -   `mtu=1` : установить MTU таким же, как у родительского интерфейса (`vmbr0`).


### <span class="section-num">1.2</span> Копирование образа диска {#копирование-образа-диска}

-   Необходимо выключить исходную виртуальную машину на хосте источнике.
-   Найти образ жесткого диска, который используется в виртуальной машине.
-   Пусть образ диска называется `kvm_disk.qcow2`.
-   Скопируем образ на хост назначения (Proxmox):
    ```shell
    scp /var/lib/libvirt/images/kvm_disk.qcow2 proxmox.example.com:/var/lib/vz/images
    ```


### <span class="section-num">1.3</span> Импорт диска {#импорт-диска}

-   Импортируйте скопированный диск:
    ```shell
    qm importdisk 111 /var/lib/vz/images/kvm_disk.qcow2 local-lvm --format raw
    ```

    -   В результате будет выдано имя получившегося диска в виде `unused0:local-lvm:vm-111-disk-0`.
-   Подключите виртуальный диск к виртуальной машине:
    ```shell
    qm set 111 --scsi0 local-lvm:vm-111-disk-0
    ```

    -   Подключить можно и через графический интерфейс.
-   Зададим порядок загрузки (SCSI диск):
    ```shell
    qm set 111 --boot order='scsi0'
    ```
-   Зададим тип CPU:
    ```shell
    qm set 111 --cpu cputype=host
    ```
-   Подключим мышку:
    ```shell
    qm set 111 --tablet 1
    ```


### <span class="section-num">1.4</span> Загрузка через UEFI {#загрузка-через-uefi}

-   Установите тип загрузки в UEFI (если необходимо):
    ```shell
    qm set 111 --bios ovmf
    ```
-   Добавьте диск для партиции UEFI:
    ```shell
    qm set 111 --efidisk0 local-lvm:1,format=raw
    ```


### <span class="section-num">1.5</span> После переноса {#после-переноса}

-   Проверьте настройку виртуальной машины.
-   Проверьте ip-адрес машины (у вас изменился mac-адрес).
-   Установите, если надо, quemu-guest-agent (см. [KVM. QEMU Guest Agent]({{< relref "2024-09-05-kvm-qemu-guest-agent" >}})).
