---
title: "Виртуализация. Libvirt"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-26T13:39:00+03:00
lastmod: 2025-03-07T10:26:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "virtualization-libvirt"
---

Виртуализация. Libvirt.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.libvirt.org/>
-   Репозиторий: <https://gitlab.com/libvirt/libvirt>
-   Набор инструментов для управления виртуализацией.
-   Может взаимодействовать с другим программным обеспечением для виртуализации: QEMU, LXC, VMware, VirtualBox, Xen.


### <span class="section-num">1.1</span> Обзор Libvirt {#обзор-libvirt}

-   libvirt хранит свою конфигурацию для каждой виртуальной машины и контейнера внутри каталогов, используя формат XML в `/etc/libvirt`.
    -   Конфигурация QEMU находится в каталоге `/etc/libvirt/qemu`.
    -   Конфигурация LXC находится в каталоге `/etc/libvirt/lxc`.
-   libvirt можно использовать для работы с виртуальными машинами и экземплярами контейнеров.
-   libvirt можно использовать для создания моментального снимка экземпляра виртуальной машины.
-   libvirt может монтировать ISO-образы компакт-дисков.
-   libvirt можно использовать для создания различных сетевых подключений для гостевой ОС в виртуальной машине или контейнере.
-   libvirt может создавать мосты, MACVLAN, статический netdev и IP-интерфейс с NAT.
-   libvirt можно использовать для работы с пулами хранения данных: прямой общий доступ к каталогу, блочному устройству, gluster, iSCSI, LVM, netfs, SCSI, RADOS/Ceph.


### <span class="section-num">1.2</span> Фронтенды {#фронтенды}

-   virsh (командная строка)
-   virt-manager (графический) (см. [Виртуализация. Virt-manager]({{< relref "2024-11-26-virtualization-virt-manager" >}}))


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   В основном репозитории:
    ```shell
    emerge app-emulation/libvirt
    ```


## <span class="section-num">3</span> Разрешения пользователя {#разрешения-пользователя}

-   Чтобы запустить virt-manager от имени обычного пользователя, убедитесь, что пользователь добавлен в группу `libvirt`:
    ```shell
    sudo usermod -a -G kvm,libvirt <user>
    ```
-   Необходимы следующие права доступа к файлу устройства:
    ```shell
    sudo chown root:kvm /dev/kvm
    sudo chmod 660 /dev/kvm
    ```
-   Раскомментируйте следующие строки из файла конфигурации `/etc/libvirt/libvirtd.conf`:
    ```conf-unix
    auth_unix_ro = "none"
    auth_unix_rw = "none"
    unix_sock_group = "libvirt"
    unix_sock_ro_perms = "0777"
    unix_sock_rw_perms = "0770"
    ```


## <span class="section-num">4</span> Запуск {#запуск}

-   Запустите драйвер для гипервизора:
    -   qemu:
        ```shell
        systemctl enable --now virtqemud.service
        ```
    -   lxc:
        ```shell
        systemctl enable --now virtlxcd.service
        ```
-   Запустите демон управления хранилищем:
    ```shell
    systemctl enable --now virtstoraged.socket
    ```
-   Запустите демон управления сетью:
    ```shell
    systemctl enable --now virtnetworkd.service
    ```
-   Запустите сам демон libvirtd:
    ```shell
    systemctl enable --now libvirtd.service
    ```
