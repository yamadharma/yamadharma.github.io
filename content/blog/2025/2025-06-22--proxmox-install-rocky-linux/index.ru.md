---
title: "Proxmox. Установка Rocky Linux"
author: ["Dmitry S. Kulyabov"]
date: 2025-06-22T13:47:00+03:00
lastmod: 2025-12-11T09:19:00+03:00
tags: ["linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "proxmox-install-rocky-linux"
---

Proxmox. Установка Rocky Linux.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   [Linux. Дистрибутив Proxmox]({{< relref "2024-06-04-linux-proxmox-distribution" >}})
-   [Замена Centos]({{< relref "2021-05-25-replacing-centos" >}})


## <span class="section-num">2</span> Установка Rocky Linux в Proxmox из командной строки {#установка-rocky-linux-в-proxmox-из-командной-строки}

1.  Загрузите ISO-образ Rocky Linux:
    -   Откройте терминал и подключитесь к серверу Proxmox.
    -   Загрузите ISO-образ на сервер Proxmox, если он ещё не загружен.
    -   Это можно сделать через веб-интерфейс Proxmox или с помощью команды:
        ```shell
        wget https://download.rockylinux.org/pub/rocky/10/isos/x86_64/Rocky-10.1-x86_64-minimal.iso -O /var/lib/vz/template/iso/Rocky-10.1-x86_64-minimal.iso
        ```

2.  Создайте виртуальную машину в Proxmox:
    -   Посмотрите уже используемые идентификаторы виртуальных машин:
        ```shell
        qm list
        ```
    -   Выберите свободный идентификатор.

    -   Используйте команду для создания VM:
        ```shell
        qm create <VMID> --name <VMName> --agent enabled=1 --cpu host --memory 4096 --cores 2 --net0 bridge=vmbr0,model=virtio,tag=100 --scsi0 local-lvm:80 --scsihw virtio-scsi-pci --boot order=scsi0 --onboot yes
        ```
    -   Замените `<VMID>` на уникальный идентификатор VM и `<VMName>` на имя виртуальной машины.
    -   Здесь VLAN=100
    -   Размер создаваемого диска --- 80G.

3.  Настройте параметры виртуальной машины:
    -   Можно добавить или исправить параметры, такие как количество ядер процессора, объём оперативной памяти и размер диска:
        ```shell
        qm set <VMID> --cpu host --memory 8192 --cores 4
        ```

    -   Подключите ISO-образ к виртуальной машине:
        ```shell
        qm set <VMID> --cdrom local:iso/Rocky-10.1-x86_64-minimal.iso
        ```
    -   Можно добавить дополнительный диск:
        ```shell
        qm disk add <VMID> local-lvm:vm-<VMID>-disk-1 size=50G
        ```

4.  Установите Rocky Linux интерактивно:
    -   Запустите VM:
        ```shell
        qm start <VMID>
        ```
    -   Подключитесь к консоли VM через веб-интерфейс Proxmox и следуйте инструкциям по установке Rocky Linux.
    -   [Rocky Linux. Установка сервера]({{< relref "2022-08-12-rockylinux-server-installation" >}})
5.  Guest agent
    -   Установите quemu-guest-agent (см. [KVM. QEMU Guest Agent]({{< relref "2024-09-05-kvm-qemu-guest-agent" >}})).
