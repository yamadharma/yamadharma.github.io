---
title: "Linux. Установка в kvm"
author: ["Dmitry S. Kulyabov"]
date: 2024-12-28T18:27:00+03:00
lastmod: 2025-04-17T14:37:00+03:00
tags: ["linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "linux-installation-kvm"
---

Linux. Установка в kvm.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Будем устанавливать (для определённости) в каталог `/var/vm/fedora-sway`:
    ```shell
    mkdir -p /var/vm/fedora-sway
    ```
-   Для примера будем устанавливать дистрибутив Fedora Sway (`Fedora-Sway-Live-x86_64-42-1.1.iso`):
    ```shell
    cd /var/vm/fedora-sway
    wget https://download.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-Sway-Live-x86_64-42-1.1.iso
    ```


## <span class="section-num">2</span> Установка Linux на qemu {#установка-linux-на-qemu}


### <span class="section-num">2.1</span> Создание образа {#создание-образа}

-   Создадим образ виртуального диска: `80GB`, формат `qcow2`:
    ```shell
    qemu-img create -f qcow2 fedora-sway.qcow2 80G
    ```

-   Запустите виртуальную машину:
    ```shell
    qemu-system-x86_64 -boot menu=on -m 2048 -cpu max -smp 2 \
        -cdrom Fedora-Sway-Live-x86_64-42-1.1.iso \
        -drive file=fedora-sway.qcow2,format=qcow2,if=virtio,aio=native,cache=none \
        -bios /usr/share/edk2-ovmf/OVMF_CODE.fd \
        -enable-kvm -machine q35 -device intel-iommu \
        -device virtio-balloon \
        -chardev qemu-vdagent,id=vdagent0,name=vdagent,clipboard=on,mouse=off \
        -display default,show-cursor=on \
        -vga none -device virtio-gpu-pci
    ```

    -   Видео-устройств подключено на видеокарту компьютера.
-   Выберите `Start Fedora-Sway-Live 42`.
-   Загрузится графический режим.
-   Если вы запускаете из-под Sway, включите `Passthrough mode`.
-   Также можно использовать режим захвата, переключая его по комбинации `Ctrl+Alt+g`.
-   Установите систему.
-   После установке остановите систему:
    ```shell
    sudo systemctl halt
    ```


### <span class="section-num">2.2</span> Запуск системы {#запуск-системы}

-   Для удобства создайте командный файл `fedora-sway-start.sh`:
    ```shell
    touch fedora-sway-start.sh
    chmod +x fedora-sway-start.sh
    ```
-   В файл запишите команду для запуска:
    ```shell
    #!/bin/bash

    qemu-system-x86_64 -boot menu=on -m 2048 \
       -cpu max -smp 2 \
        -drive file=fedora-sway.qcow2,format=qcow2,if=virtio,aio=native,cache=none \
        -bios /usr/share/edk2-ovmf/OVMF_CODE.fd \
        -enable-kvm -machine q35 -device intel-iommu \
        -device virtio-balloon \
        -device virtio-serial \
        -chardev spicevmc,id=vdagent,debug=0,name=vdagent \
        -device virtio-serial,packed=on,ioeventfd=on \
        -device virtserialport,name=com.redhat.spice.0,chardev=vdagent0 \
        -chardev qemu-vdagent,id=vdagent0,name=vdagent,clipboard=on,mouse=off \
        -display default,show-cursor=on \
        -vga none -device virtio-gpu-pci
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      fedora-sway-start.sh
    </div>


### <span class="section-num">2.3</span> Видео: Установка Linux на qemu {#видео-установка-linux-на-qemu}

{{< tabs "Установка Linux на qemu" >}}
{{< tab "RuTube" >}}

{{< rutube 50903a2181f564a0a207ace60067ad3d >}}

{{< /tab >}}
{{< tab "Платформа" >}}

{{< plvideo W5741K4QRBi1 >}}

{{< /tab >}}
{{< tab "VKvideo" >}}

{{< vkvideo 606414976 456239663 2 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube zdGOCVWmnWo >}}

{{< /tab >}}
{{< /tabs >}}


## <span class="section-num">3</span> Установка Linux с помощью libvirt {#установка-linux-с-помощью-libvirt}


### <span class="section-num">3.1</span> Libvirt {#libvirt}

-   Можно использовать для управления образом libvirt (см. [Виртуализация. Libvirt]({{< relref "2024-11-26-virtualization-libvirt" >}}))


### <span class="section-num">3.2</span> Создание образа {#создание-образа}

-   Создайте образ виртуального диска с помощью утилиты `qemu-img` (`60GB`, формат `qcow2`):
    ```shell
    qemu-img create -f qcow2 fedora-sway.qcow2 60G
    ```
-   Запустите виртуальную машину:
    ```shell
    virt-install \
        --connect qemu:///session \
        --virt-type kvm \
        --name fedora-sway \
        --memory 2048 \
        --vcpus 2 \
        --boot uefi \
        --cdrom Fedora-Sway-Live-x86_64-41-1.4.iso \
        --disk bus=virtio,format=qcow2,path=fedora-sway.qcow2 \
        --graphics spice,gl.enable=yes,listen=none \
        --video virtio --channel spicevmc \
        --network default,model=virtio \
        --os-variant fedora40
    ```
-   Выберите `Start Fedora-Sway-Live 41`.
-   Загрузится графический режим.
-   Если вы запускаете из-под Sway, включите `Passthrough mode`.
-   Установите систему.
-   Выполните следующую команду на хосте, чтобы получить список определённых в данный момент доменов (флаг `--all` перечисляет все домены):
    ```shell
    virsh list --all
    ```
-   После завершения установки выключите домен.


### <span class="section-num">3.3</span> Запуск {#запуск}

-   Запустить домен:
    ```shell
    virsh start fedora-sway
    ```
-   Отключить домен:
    ```shell
    virsh shutdown fedora-sway
    ```
-   Принудительно отключить домен:
    ```shell
    virsh destroy fedora-sway
    ```
-   Подключиться к домену можно с помощью `virt-manager`.
-   Уничтожить домен:
    ```shell
    virsh undefine fedora-sway --remove-all-storage
    ```
