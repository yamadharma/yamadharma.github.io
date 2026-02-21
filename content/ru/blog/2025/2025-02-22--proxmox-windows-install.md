---
title: "Proxmox. Установка Windows"
author: ["Dmitry S. Kulyabov"]
date: 2025-02-22T19:20:00+03:00
lastmod: 2025-02-23T18:16:00+03:00
tags: ["windows"]
categories: ["computer-science"]
draft: false
slug: "proxmox-windows-install"
---

Proxmox. Установка Windows.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Устанавливается виртуальная машина Windows на kvm (см. [Windows. Установка в kvm]({{< relref "2024-05-29-windows-install-kvm" >}}))
-   В качестве реализации управления виртуальными машинами используется Proxmox (см. [Linux. Дистрибутив Proxmox]({{< relref "2024-06-04-linux-proxmox-distribution" >}}))
-   Информация:
    -   <https://pve.proxmox.com/wiki/Windows_2022_guest_best_practices>
    -   <https://pve.proxmox.com/wiki/Windows_10_guest_best_practices>
    -   <https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers>


## <span class="section-num">2</span> Подготовка {#подготовка}

-   Скачаем драйвера для qemu:
    ```shell
    wget https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/latest-virtio/virtio-win.iso -O /var/lib/vz/template/iso/virtio-win.iso
    ```
-   Необходимо подключить также образ Windows.
-   Его можно подключить через nfs, а можно загрузить в `/var/lib/vz/template/iso`.


## <span class="section-num">3</span> Установка {#установка}

-   Создадим виртуальную машину:
    ```shell
    qm create 200 --name pdc2 --memory 16000 --cores 4 --sockets 1 --net0 virtio,bridge=vmbr1,firewall=1,mtu=1,tag=180 --agent enabled=1
    ```

    -   `tag` задаёт используемый vlan.
-   Установим тип операционной системы.
-   Можно выбрать из списка: wxp, w2k, w2k3, w2k8, wvista, win7, win8, win10, win11.
    ```shell
    qm set 200 --ostype win10
    ```
-   Подключим QEMU Guest Agent (см. [KVM. QEMU Guest Agent]({{< relref "2024-09-05-kvm-qemu-guest-agent" >}})):
    ```shell
    qm set 200 --agent enabled=1,fstrim_cloned_disks=1
    ```
-   Создадим диск (160GB):
    ```shell
    pvesm alloc local-lvm 200 vm-200-disk-0 160G
    ```
-   Зададим драйвер диска:
    ```shell
    qm set 200 --scsihw virtio-scsi-single
    ```
-   Подключим диск:
    ```shell
    qm set 200 --virtio0 local-lvm:vm-200-disk-0
    ```
-   Подключим CDROM:
    ```shell
    qm set 200 --ide2 local:iso/windows-server-2019.iso,media=cdrom
    ```
-   Подключим диск с драйверами VirtIO:
    ```shell
    qm set 200 --ide3 local:iso/virtio-win.iso,media=cdrom
    ```
-   Зададим порядок загрузки (CD-ROM, затем диск)
    ```shell
    qm set 200 --boot c --bootdisk virtio0
    qm set 200 --boot order='ide2;ide3;virtio0'
    ```
-   Зададим тип CPU:
    ```shell
    qm set 200 --cpu cputype=host
    ```
-   Подключим для мышки:
    ```shell
    qm set 200 --tablet 1
    ```


## <span class="section-num">4</span> Скрипт установки {#скрипт-установки}

-   Все действия по установке можно собрать в виде скрипта (нужно править):
    ```bash
    #!/bin/bash

    # Configuration variables
    NODE="pve"
    VMID="200"                    # Change this to your desired VM ID
    VM_NAME="win11-test"           # Change this to your desired VM name
    VM_MEMORY="4096"              # Memory in MB
    VM_CORES="2"                  # Number of CPU cores
    VM_SOCKET="1"                 # Number of CPU sockets
    STORAGE="local-lvm"           # Storage location
    DISK_SIZE="160G"              # Disk size
    ISO_STORAGE="/mnt/pve/nfs/template/iso"           # Storage location for ISOs
    WIN_ISO="Win11_23H2_x64v2_auto.iso"         # Windows ISO filename
    VIRTIO_ISO="virtio-win.iso"   # VirtIO drivers ISO filename
    OS_TYPE="win10"               # Options: wxp, w2k, w2k3, w2k8, wvista, win7, win8, win10, win11

    # Function to check if VM ID already exists
    check_vmid() {
        if qm status $VMID &>/dev/null; then
            echo "Error: VM ID $VMID already exists"
            exit 1
        fi
    }

    # Function to check storage availability
    check_storage() {
        if ! pvesm status | grep -q "^$STORAGE"; then
            echo "Error: Storage '$STORAGE' not found"
            exit 1
        fi
    }

    # Function to check ISO files
    check_isos() {
        if [ ! -f "/mnt/pve/nfs/template/iso/$WIN_ISO" ]; then
            echo "Warning: Windows ISO not found at /var/lib/vz/template/iso/$WIN_ISO"
        fi
        if [ ! -f "/mnt/pve/nfs/template/iso/$VIRTIO_ISO" ]; then
            echo "Warning: VirtIO ISO not found at /var/lib/vz/template/iso/$VIRTIO_ISO"
        fi
    }

    # Run checks
    check_vmid
    check_storage
    check_isos

    # Create and add main disk using VirtIO Block
    echo "Creating disk with size $DISK_SIZE..."
    pvesm alloc $STORAGE $VMID vm-$VMID-disk-2 $DISK_SIZE || {
        echo "Error: Failed to create disk"
        qm destroy $VMID
        exit 1
    }

    # Create VM
    echo "Creating VM with ID $VMID..."
    qm create $VMID --name $VM_NAME --memory $VM_MEMORY --cores $VM_CORES --sockets $VM_SOCKET --net0 virtio,bridge=vmbr0
    qm set $VMID --ostype "$OS_TYPE"

    qm set $VMID --virtio0 $STORAGE:vm-$VMID-disk-2

    # Add Windows installation media
    qm set $VMID --ide2 nfs:iso/$WIN_ISO,media=cdrom

    # Add VirtIO drivers
    qm set $VMID --ide3 nfs:iso/$VIRTIO_ISO,media=cdrom

    # Configure boot order (CD-ROM first, then disk)
    #qm set $VMID --boot c --bootdisk virtio0
    #qm set $VMID --boot order='ide2;ide3;virtio0'

    # Enable QEMU Guest Agent
    qm set $VMID --agent enabled=1,fstrim_cloned_disks=1

    #create TPM
    pvesm alloc local-lvm 1022 vm-1022-disk-1.raw 4M

    #create EFI Disk
    pvesm alloc local-lvm 1022 vm-1022-disk-0.qcow2 4M

    # Add TPM support (required for Windows 11)
    echo "Configuring Windows 11 specific settings (TPM, UEFI)..."
    qm set $VMID --tpmstate0 local-lvm:vm-1022-disk-1.raw,size=4M,version=v2.0
    qm set $VMID --machine q35
    qm set $VMID --bios ovmf
    qm set 1022 --efidisk0 local-lvm:vm-1022-disk-0.qcow2,size=528K,efitype=4m,pre-enrolled-keys=1

    # Configure boot order (CD-ROM first, then disk)
    qm set $VMID --boot c --bootdisk virtio0
    qm set $VMID --boot order='ide2;ide3;virtio0'

    # Configure CPU type for better performance
    qm set 1022 --cpu cputype=host

    # Add tablet device for better mouse handling
    qm set 1022 --tablet 1

    echo "VM $VMID created successfully. Before starting the VM, ensure:"
    echo "1. Windows ISO ($WIN_ISO) is present in $ISO_STORAGE:iso/"
    echo "2. VirtIO drivers ISO ($VIRTIO_ISO) is present in $ISO_STORAGE:iso/"
    echo ""
    echo "During Windows installation, when prompted for drivers, browse the VirtIO ISO (IDE3) and select:"
    echo "- For storage: /viostor/w10/amd64/"
    echo ""
    echo "To download the latest VirtIO drivers:"
    echo "wget https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/latest-virtio/virtio-win.iso -O /var/lib/vz/template/iso/virtio-win.iso"
    echo ""
    echo "To start the VM:"
    echo "qm start $VMID"
    ```
