---
title: "Linux. Установка в kvm"
author: ["Dmitry S. Kulyabov"]
date: 2024-12-28T18:27:00+03:00
lastmod: 2026-04-30T18:53:00+03:00
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
-   Для примера будем устанавливать дистрибутив Fedora Sway (`Fedora-Sway-Live-44-1.7.x86_64.iso`):
    ```shell
    cd /var/vm/fedora-sway
    wget https://download.fedoraproject.org/pub/fedora/linux/releases/44/Spins/x86_64/iso/Fedora-Sway-Live-44-1.7.x86_64.iso
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
        -cdrom Fedora-Sway-Live-44-1.7.x86_64.iso \
        -drive file=fedora-sway.qcow2,format=qcow2,if=virtio,aio=native,cache=none \
        -bios /usr/share/edk2-ovmf/OVMF_CODE.fd \
        -enable-kvm -machine q35 -device intel-iommu \
        -device virtio-balloon \
        -chardev qemu-vdagent,id=vdagent0,name=vdagent,clipboard=on,mouse=off \
        -display default,show-cursor=on \
        -vga none -device virtio-gpu-pci
    ```

    -   Видео-устройств подключено на видеокарту компьютера.
-   Выберите `Start Fedora-Sway-Live 44`.
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


### <span class="section-num">3.2</span> Использование virt-install {#использование-virt-install}

-   Конфигурацию можно создать с помощью virt-install:
    ```shell
    virt-install \
        --connect qemu:///system \
        --disk /var/lib/libvirt/images/Fedora-Sway-Live-44-1.7.x86_64.iso,device=cdrom \
        --disk pool=default,size=60,bus=virtio,format=qcow2 \
        --name fedora-sway \
        --os-variant=fedora42 \
        --machine q35 \
        --ram 4096 \
        --memballoon driver.iommu=on \
        --vcpus=2 \
        --network network=default,model=virtio \
        --graphics spice \
        --channel spicevmc \
        --hvm \
        --virt-type=kvm \
        --features kvm_hidden=on,smm=on \
        --tpm backend.type=emulator,backend.version=2.0,model=tpm-tis \
        --boot uefi \
        --check path_in_use=off \
        --boot cdrom,hd,menu=on \
        --memorybacking source.type=memfd,access.mode=shared \
        --filesystem type=mount,source=$HOME,target=hostshare,driver.type=virtiofs
    ```

    -   `--name fedora-sway` : название виртуальной машины;
    -   `--os-type=fedora42` : тип ОС;
    -   `--cdrom /var/lib/libvirt/images/Fedora-Sway-Live-44-1.7.x86_64.iso` : путь к ISO-образу установочного диска ОС;
    -   `--graphics spice` : графическая консоль;
    -   `--disk pool=default,size=60,bus=virtio,format=qcow2` : хранилище;
        -   образ виртуальной машины будет создана в пространстве хранения объёмом 60 ГБ, которое автоматически выделяется из пула хранилищ default;
        -   образ диска для этой виртуальной машины будет создан в формате qcow2;
    -   `--ram 4096` : объём оперативной памяти;
    -   `--vcpus=2` : количество процессоров;
    -   `--network network=default` : виртуальная сеть default;
    -   `--hvm` : полностью виртуализированная система;
    -   `--virt-type=kvm` : использовать модуль ядра KVM, который задействует аппаратные возможности виртуализации процессора.
-   В качестве видео-интерфейса ставим QXL.


### <span class="section-num">3.3</span> Установка {#установка}

-   Выберите `Start Fedora-Sway-Live 44`.
-   Загрузится графический режим.
-   Если вы запускаете из-под Sway, включите `Passthrough mode`.
-   Установите систему.
-   Выполните следующую команду на хосте, чтобы получить список определённых в данный момент доменов (флаг `--all` перечисляет все домены):
    ```shell
    virsh list --all
    ```
-   После завершения установки выключите домен.


### <span class="section-num">3.4</span> Общая папка {#общая-папка}

-   Будем использовать встроенный метод создания общей папки с помощью _virt-manager_.
-   Делаем, если не настроили при установке.
-   Нажмите на значок с надписью _Показать виртуальное оборудование_ (_Show virtual hardware details_) на панели инструментов.
-   Нажмите _Память_ (_Memory_) на левой панели.
    -   Проверьте, что выбрана опция _Включить общую память_ (_Enable shared memory_).
    -   Нажмите _Применить_.
-   Внизу нажмите _Добавить оборудование_ (_Add hardware_).
    -   Выберите _Файловая система_ (_File system_) на левой панели в окне добавления нового оборудования.
    -   Затем выберите _Driver=virtiofs_ на вкладке Подробности.
    -   Нажмите на _browse &gt; browse local_ и выберите путь к хосту из вашей системы Linux, например `/home`.
    -   В целевом пути укажите любое имя папки, например `hostshare`.
-   Монтироваться будем, например, в `/mnt/hostshare`.

-   Запустите гостя и смонтируйте внутри него:
    ```shell
    sudo mkdir -p /mnt/hostshare
    sudo mount -t virtiofs hostshare /mnt/hostshare
    ```

-   Для автоматического монтирования добавьте запись в /etc/fstab:
    ```conf-unix
    hostshare /mnt/hostshare virtiofs defaults 0 0
    ```


### <span class="section-num">3.5</span> Запуск с virt-manager {#запуск-с-virt-manager}

-   Запустить домен можно с помощью `virt-manager`.


### <span class="section-num">3.6</span> Запуск с virsh {#запуск-с-virsh}

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
