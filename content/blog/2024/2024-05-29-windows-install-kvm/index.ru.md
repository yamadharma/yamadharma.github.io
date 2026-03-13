---
title: "Windows. Установка в kvm"
author: ["Dmitry S. Kulyabov"]
date: 2024-05-29T19:46:00+03:00
lastmod: 2026-02-27T11:52:00+03:00
tags: ["windows", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "windows-install-kvm"
---

Установка Windows на KVM.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Пререквизиты {#пререквизиты}

-   Необходимо иметь установленный libvirt (см. [Виртуализация. Libvirt]({{< relref "2024-11-26-virtualization-libvirt" >}})).
-   Можно устанавливать с помощью какого-либо графического интерфейса управления qemu, например с помощью virt-manager:
-   Gentoo:
    ```shell
    emerge app-emulation/virt-manager
    ```
-   Рекомендуется использовать драйвера Virtio для Windows.
-   Работа через устройства Virtio осуществляется быстрее, чем через эмуляцию SCSI и т.д.
-   Gentoo:
    ```shell
    emerge app-emulation/virtio-win
    ```
-   Можно просто скачать с репозитория:
    -   <https://github.com/virtio-win/virtio-win-pkg-scripts/blob/master/README.md>
-   Скачаем драйвера для qemu:
    ```shell
    cd /var/lib/libvirt/images
    wget https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/latest-virtio/virtio-win.iso
    ```
-   Проще всего использовать образ iso-диска и подмонтировать его как второй cdrom.


## <span class="section-num">2</span> Установка Windows {#установка-windows}

-   При установке следует выбрать пункт о дополнительной конфигурации перед установкой.
-   На этом этапе следует добавить второй виртуальный cdrom с драйверами virtio-win.
-   У жёсткого диска установите шину VirtIO.
-   В разделе _Обзор_ убедитесь, что для чипсета выбрано значение Q35, а для прошивки --- UEFI.
-   Для запуска Windows 11 под QEMU KVM необходимы Secureboot и TPM, в файле конфигураций это выглядит так:
    ```xml
    <os>
      <type arch="x86_64" machine="q35">hvm</type>
      <loader readonly="yes" type="pflash">/usr/share/edk2/ovmf/OVMF_CODE.secboot.fd</loader>
      <nvram template="/usr/share/edk2/ovmf/OVMF_VARS.secboot.fd"/>
      <boot dev="hd"/>
    </os>

    ...

    <tpm model="tpm-tis">
      <backend type="emulator" version="2.0"/>
    </tpm>
    ```


## <span class="section-num">3</span> Использование virt-install {#использование-virt-install}

-   Конфигурацию можно создать с помощью virt-install:
    ```shell
    virt-install \
        --connect qemu:///system \
        --disk /var/lib/libvirt/images/win11.iso,device=cdrom \
        --disk /var/lib/libvirt/images/virtio-win.iso,device=cdrom \
        --disk pool=default,size=120,bus=virtio,format=qcow2 \
        --name windows11 \
        --os-variant=win11 \
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
        --boot cdrom,hd,menu=on
    ```

    -   `--name windows11` : название виртуальной машины;
    -   `--os-type=win11` : тип ОС;
    -   `--cdrom /var/lib/libvirt/images/win11.iso` : путь к ISO-образу установочного диска ОС;
    -   `--graphics spice` : графическая консоль;
    -   `--disk pool=default,size=160,bus=virtio,format=qcow2` : хранилище;
        -   образ виртуальной машины будет создана в пространстве хранения объёмом 160 ГБ, которое автоматически выделяется из пула хранилищ default;
        -   образ диска для этой виртуальной машины будет создан в формате qcow2;
    -   `--ram 4096` : объём оперативной памяти;
    -   `--vcpus=2` : количество процессоров;
    -   `--network network=default` : виртуальная сеть default;
    -   `--hvm` : полностью виртуализированная система;
    -   `--virt-type=kvm` : использовать модуль ядра KVM, который задействует аппаратные возможности виртуализации процессора.
-   В качестве видео-интерфейса ставим QXL.
    -   После установки драйверов следует перевести в Virtio.


## <span class="section-num">4</span> Установка {#установка}

-   Вначале Windows не видит диск.
-   Необходимо установить драйвер диска из папки `e:\amd64\w11`.
-   Далее, для подключения к сети потребуется установить драйвер.
-   Для этого выберите весь диск с драйверами `e:\`.


## <span class="section-num">5</span> После установки {#после-установки}

-   Для загрузки используйте `virt-manager`.
-   Установите сертификат RedHat с CD-диска:
    ```shell
    e:\cert\Virtio_Win_Red_Hat_CA.cer
    ```
-   После загрузки установите необходимые драйвера Virtio:
    ```shell
    e:\wirtio-win-gt-x64.msi
    ```
-   Установите гостевые утилиты:
    ```shell
    e:\virtio-win-guest-tools.exe
    ```
-   Отмонтируйте установочный диск Windows.
-   Поменяйте в настройках virt-manager типы устройств:
    -   видео на Virtio + 3D;
    -   в разделе Spice добавьте OpenGL.
-   Возможно, следует отключить масштабирование экрана в меню (Вид -&gt; Масштабирование экрана -&gt; Никогда) (чтобы шрифты не смазывались).


## <span class="section-num">6</span> Общая папка {#общая-папка}

-   Будем использовать встроенный метод создания общей папки с помощью _virt-manager_.
-   Нажмите на значок с надписью _Показать виртуальное оборудование_ (_Show virtual hardware details_) на панели инструментов.
-   Нажмите _Память_ (_Memory_) на левой панели.
    -   Проверьте, что выбрана опция _Включить общую память_ (_Enable shared memory_).
    -   Нажмите _Применить_.
-   Внизу нажмите _Добавить оборудование_ (_Add hardware_).
    -   Выберите _Файловая система_ (_File system_) на левой панели в окне добавления нового оборудования.
    -   Затем выберите _Driver=virtiofs_ на вкладке Подробности.
    -   Нажмите на _browse &gt; browse local_ и выберите путь к хосту из вашей системы Linux, например `/home`.
    -   В целевом пути укажите любое имя диска, например `h:`.
-   Установите в системе Windows WinFSP (FUSE для Windows).
    -   Можно скачать с сайта <https://github.com/winfsp/winfsp/releases/>.
    -   Можно установить с Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
        ```shell
        choco install winfsp -y
        ```
-   Установите `virtio-win-guest-tools.exe` (уже установили).
    -   Возьмите из комплекта `virtio-win.iso` или скачайте напрямую из <https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/>.
    -   После завершения установки перезагрузите виртуальную машину Windows.
-   Откройте меню "Пуск" и найдите "Службы".
    -   Найдите службу _Служба VirtIO-FS_ (_VirtIO-Sevice-FS_).
    -   Щелкните правой кнопкой мыши и нажмите "Запустить", чтобы запустить службу.
    -   Можно запустить из командной строки:
        ```shell
        sc start VirtioFsSvc
        ```
    -   Установите её на автозапуск (VirtIO-Sevice-FS &gt; Properties &gt; Startup type &gt; Manual to Automatic).
    -   Или из командной строки:
        ```shell
        sc config VirtioFsSvc start= auto
        ```
-   После запуска службы откройте Проводник, и вы должны увидеть метку монтирования, которую вы создали в первом шаге выше, и которая должна быть отображена как диск `H:`.


## <span class="section-num">7</span> Буфер обмена {#буфер-обмена}

-   Должно работать само после установки драйверов virtio.
-   Проверьте, что есть Канал (spice) типа `spicevmc`.
-   Установите в Windows _SPICE Guest Tools_ (возможно установить из следующих источников):
    -   установите `virtio-win-guest-tools.exe` (уже установили).
    -   <https://www.spice-space.org/download/windows/spice-guest-tools/spice-guest-tools-latest.exe>.
    -   Можно установить с помощью Chocolatey:
        ```shell
        choco install spice-agent
        ```


## <span class="section-num">8</span> Видео {#видео}

{{< tabs "Установка Windows на KVM" >}}
{{< tab "RuTube" >}}

{{< rutube 46f95eeb6c0c8e5bbf51b2fe0851e76d >}}

{{< /tab >}}
{{< tab "Платформа" >}}

{{< plvideo coo_ngzPjq8D >}}

{{< /tab >}}
{{< tab "VKvideo" >}}

{{< vkvideo -230024722 456239026 2 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube pZla1y1aPhI >}}

{{< /tab >}}
{{< /tabs >}}
