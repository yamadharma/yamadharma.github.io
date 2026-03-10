---
title: "Linux. Дистрибутив Proxmox"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-04T10:45:00+03:00
lastmod: 2025-11-20T16:01:00+03:00
tags: ["sysadmin", "linux"]
categories: ["computer-science"]
draft: false
slug: "linux-proxmox-distribution"
---

Дистрибутив Proxmox.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Набор дистрибутивов Linux.
-   Основаны на Debian GNU/Linux.
-   Разрабатывается австрийской фирмой Proxmox Server Solutions GmbH, спонсируемой Internet Foundation Austria.
-   Сайт: <https://www.proxmox.com/>


## <span class="section-num">2</span> Proxmox Virtual Environment (Proxmox VE) {#proxmox-virtual-environment--proxmox-ve}

-   Основной дистрибутив набора.
-   Система виртуализации.
-   В качестве гипервизоров использует KVM и LXC (начиная с версии 4.0, в версиях до 3.4 включительно вместо него использовался OpenVZ).
-   Управление виртуальными машинами и администрирование самого сервера производятся через веб-интерфейс либо через интерфейс командной строки.


### <span class="section-num">2.1</span> Установка и настройка {#установка-и-настройка}

-   [Linux. Установка Proxmox VE]({{< relref "2024-06-04-proxmox-ve-install" >}})
-   [Proxmox. Вспомогательные скрипты]({{< relref "2024-06-04-proxmox-helper-scripts" >}})
-   [Перенос виртуальной машины на Proxmox]({{< relref "2024-09-04-migrating-virtual-machine-proxmox" >}})


### <span class="section-num">2.2</span> Обновление {#обновление}


#### <span class="section-num">2.2.1</span> 8 → 9 {#8-9}

-   Документация: <https://pve.proxmox.com/wiki/Upgrade_from_8_to_9>

<!--list-separator-->

1.  Обновление до последнего релиза

    -   Обновите систему:
        ```shell
        apt update
        apt dist-upgrade
        apt autoremove
        pveversion
        ```

    -   Убедитесь, что в корневой точке монтирования имеется не менее 10 ГБ свободного места на диске:

    <!--listend-->

    ```shell
    df -h /
    ```

<!--list-separator-->

2.  Проверка совместимости

    -   Программа `pve8to9` выводит подсказки и предупреждения о потенциальных проблемах:

    <!--listend-->

    ```shell
    pve8to9
    ```

    -   Чтобы запустить её со всеми включенными проверками, выполните:

    <!--listend-->

    ```shell
    pve8to9 --full
    ```

<!--list-separator-->

3.  Изменения, влияющие на совместимость

    -   Удаление поддержки cgroupv1
        -   Proxmox VE 9 больше не поддерживает legacy cgroupv1. Контейнеры с systemd версии 230 и старше (например, CentOS 7, Ubuntu 16.04) не будут поддерживаться.

    -   Изменения в автоактивации LVM
        -   Для существующих LVM-томов рекомендуется запустить скрипт миграции для отключения автоактивации:

    <!--listend-->

    ```shell
    /usr/share/pve-manager/migrations/pve-lvm-disable-autoactivation
    ```

<!--list-separator-->

4.  Обновление репозиториев Debian

    -   Замените репозитории Bookworm на Trixie:

    <!--listend-->

    ```shell
    sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
    sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
    ```

<!--list-separator-->

5.  Добавление репозитория Proxmox VE 9

    -   Создайте новый файл репозитория:

    <!--listend-->

    ```shell
    cat > /etc/apt/sources.list.d/proxmox.sources << EOF
    Types: deb
    URIs: http://download.proxmox.com/debian/pve
    Suites: trixie
    Components: pve-no-subscription
    Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
    EOF
    ```

    -   Удалите старые репозитории Proxmox VE 8 из соответствующих файлов.

<!--list-separator-->

6.  Обновление репозитория Ceph (при наличии)

    -   Для кластеров:

    <!--listend-->

    ```shell
    cat > /etc/apt/sources.list.d/ceph.sources << EOF
    Types: deb
    URIs: http://download.proxmox.com/debian/ceph-squid
    Suites: trixie
    Components: no-subscription
    Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
    EOF
    ```

    -   Удалите старый файл `/etc/apt/sources.list.d/ceph.list`.

<!--list-separator-->

7.  Обновление индекса пакетов

    ```shell
    apt update
    ```

    -   Убедитесь, что команда выполнена без ошибок.

<!--list-separator-->

8.  Выполнение обновления

    ```shell
    apt dist-upgrade
    ```

<!--list-separator-->

9.  Ответы на вопросы конфигурации

    -   Во время обновления система может запросить подтверждение изменений в файлах конфигурации:
        -   `/etc/issue` : выберите «No» (сохранить текущую версию);
        -   `/etc/lvm/lvm.conf` : рекомендуется «Yes» (установить версию дистрибутива);
        -   `/etc/ssh/sshd_config` : если не вносили изменения, выберите «Yes»;
        -   `/etc/default/grub` : будьте осторожны, рекомендуется «No» если есть сомнения.

<!--list-separator-->

10.  Проверка

    -   После успешного завершения обновления:

    <!--listend-->

    ```bash
    pve8to9
    ```

<!--list-separator-->

11.  Возможные проблемы

    <!--list-separator-->

    1.  GRUB может не загрузиться с LVM в режиме UEFI

        -   В PVE 8 и более ранних версиях grub может не загружаться с LVM, выдавая сообщение об ошибке. ``disk `lvmid/...` not found``.
        -   На системах, загружающихся в режиме EFI с правами root на LVM, установите правильный метапакет grub с помощью:

        <!--listend-->

        ```shell
        [ -d /sys/firmware/efi ] && apt install grub-efi-amd64
        ```

    <!--list-separator-->

    2.  Метапакет systemd-boot автоматически изменяет конфигурацию загрузчика и должен быть удален

        -   В Debian Trixie пакет `systemd-boot` был разделен на несколько пакетов.
        -   Proxmox Systems использует `systemd-boot` для загрузки только в некоторых конфигурациях (ZFS на корне и UEFI, загруженный без безопасной загрузки).
        -   Возможно, его стоит удалить:
            ```shell
            apt remove systemd-boot
            ```

<!--list-separator-->

12.  Перезагрузка

    -   Перегрузите:

    <!--listend-->

    ```bash
    reboot
    ```

<!--list-separator-->

13.  Тьюнинг

    -   Перенести существующие источники репозитория в рекомендуемый формат стиля deb822:
        ```shell
        apt modernize-sources
        ```

    -   Запустите скрипт Proxmox VE Post Install (см. [Proxmox. Вспомогательные скрипты]({{< relref "2024-06-04-proxmox-helper-scripts" >}}))

<!--list-separator-->

14.  Проверка после обновления

    -   Очистите кэш браузера (Ctrl + Shift + R).
    -   Проверьте, что все узлы кластера работают корректно.
    -   Убедитесь, что все виртуальные машины и контейнеры функционируют нормально.


## <span class="section-num">3</span> Дистрибутивы для установки {#дистрибутивы-для-установки}

-   [Linux. Дистрибутив Turnkey]({{< relref "2025-01-26--linux-distro-turnkey" >}})


## <span class="section-num">4</span> Установка виртуальных машин {#установка-виртуальных-машин}

-   [Proxmox. Установка OpenVPN в LXC]({{< relref "2025-01-27--proxmox-installing-openvpn-lxc" >}})
-   [Proxmox. Установка Wireguard в LXC]({{< relref "2025-11-19--proxmox-install-wireguard-lxc" >}})
-   [Proxmox. Установка Windows]({{< relref "2025-02-22--proxmox-windows-install" >}})
-   [Proxmox. Сервер Seafile]({{< relref "2025-04-08--proxmox-seafile" >}})
-   [Proxmox. Установка Rocky Linux]({{< relref "2025-06-22--proxmox-install-rocky-linux" >}})


## <span class="section-num">5</span> Дополнительный функционал {#дополнительный-функционал}

-   [Proxmox Backup Server]({{< relref "2025-03-04--proxmox-backup-server" >}})
