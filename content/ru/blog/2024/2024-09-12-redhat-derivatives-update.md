---
title: "Обновление деривативов RedHat"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-12T12:48:00+03:00
lastmod: 2025-09-10T15:12:00+03:00
tags: ["linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "redhat-derivatives-update"
---

Обновление деривативов RedHat.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


### <span class="section-num">1.1</span> Проект ELevate {#проект-elevate}

-   Сайт: <https://almalinux.org/elevate/>
-   Документация: <https://wiki.almalinux.org/elevate/>
-   Поддерживает следующие пути обновления и миграции:
    -   обновление с CentOS 6 до CentOS 7;
    -   обновление с CentOS 7 до AlmaLinux 8, CentOS Stream 8, Euro Linux 8, Oracle Linux 8 или Rocky Linux 8;
    -   обновление Scientific Linux 7 до AlmaLinux 8;
    -   обновление с 8.x до 9.x в том же дистрибутиве;
    -   миграция на Oracle Linux 9 доступна с утилитой Oracle Leapp.


#### <span class="section-num">1.1.1</span> Scientific Linux 7 {#scientific-linux-7}

-   Scientific Linux 7 была последняя поддерживаемая версия.
-   Они рекомендуют обновляться на AlmaLinux:
    -   <https://listserv.fnal.gov/scripts/wa.exe?A2=ind2212&L=SCIENTIFIC-LINUX-USERS&P=78>
    -   <https://scientificlinux.org/category/uncategorized/fermilab-cern-recommendation-for-linux-distribution/>


### <span class="section-num">1.2</span> Предварительные действия {#предварительные-действия}

-   Определите версию операционной системы:
    ```shell
    cat /etc/os-release
    ```


## <span class="section-num">2</span> 7 → 8 {#7-8}


### <span class="section-num">2.1</span> Обновление Centos 7 до Rocky 8 {#обновление-centos-7-до-rocky-8}


#### <span class="section-num">2.1.1</span> Общая информация {#общая-информация}

-   Будем использовать проект Elevate.


#### <span class="section-num">2.1.2</span> Подготовка к обновлению {#подготовка-к-обновлению}

-   Возможно, придётся заменить репозитории: [CentOS 8. Изменение адресов репозиториев]({{< relref "2022-02-10-centos8-changing-repository-addresses" >}})
-   Удалите внешние репозитории:
    ```shell
    sudo yum -y remove epel-release
    sudo yum -y remove rpmforge-release
    sudo yum -y remove elrepo-release
    ```
-   Обновите систему:
    ```shell
    sudo yum -y upgrade
    ```
-   Перегрузите машину:
    ```shell
    sudo reboot
    ```
-   Установите пакет _elevate-release_:
    ```shell
    sudo yum install -y http://repo.almalinux.org/elevate/elevate-release-latest-el$(rpm --eval %rhel).noarch.rpm
    ```
-   Установите утилиты для миграции:
    ```shell
    sudo yum install -y leapp-upgrade leapp-data-rocky
    ```

    -   Другие варианты установки: `centos`, `almalinux`, `eurolinux`, `oraclelinux`:
        ```shell
        sudo yum install -y leapp-upgrade leapp-data-almalinux
        ```
-   Лучше установить SELinux в `permissive` в файле `/etc/selinux/config`.
-   Перегрузите компьютер.
-   Восстановите метки SELinux:
    ```shell
    sudo restorecon -vR /
    ```
-   Удалите неподдерживаемые модули ядра:
    ```shell
    sudo rmmod pata_acpi
    sudo rmmod floppy
    ```
-   Проверьте возможность обновления:
    ```shell
    sudo leapp preupgrade
    ```
-   Отчёт находится в файле `/var/log/leapp/leapp-report.txt`.
-   Там же находятся и рекомендации по устранению проблем.
-   Тут же будет список неподписанных пакетов, которые, скорее всего, вам придётся установить заново после обновления.
-   Также создаётся файл `/var/log/leapp/answerfile`, где нужно подтвердить действия.
-   Подтвердите удаление модуля PAM PKCS#11:
    ```shell
    sudo leapp answer --section remove_pam_pkcs11_module_check.confirm=True
    ```
-   После исправления запустите утилиту опять. И так до устранения основных недостатков.


#### <span class="section-num">2.1.3</span> Обновление {#обновление}

-   После подготовки сделайте обновление:
    ```shell
    sudo leapp upgrade
    ```
-   После скачивания необходимых пакетов будет предложено перегрузить машину.
-   После перезагрузки начнётся процесс обновления.


#### <span class="section-num">2.1.4</span> После обновления {#после-обновления}

-   Удалите старые пакеты от Centos7:
    ```shell
    rpm -qa | grep -E 'el7[.-]' | xargs rpm -e
    rpm -qa | grep -E 'sl7[.-]' | xargs rpm -e
    ```
-   Выполните последующие действия либо обновляйте до следующей версии.
-   Установите внешние репозитории:
    ```shell
    dnf install epel-release
    ```
-   Обновите необновлённые пакеты:
    ```shell
    dnf -y update
    ```
-   Установите удалённые пакеты, например:
    ```shell
    dnf install fail2ban
    systemctl enable --now fail2ban.service
    ```
-   Если используете LVM, обновите метаданные:
    ```shell
    sudo vgck --updatemetadata <volume_group_name>
    ```

    -   Можно в виде скрипта:
        ```shell
        for i in $(vgdisplay -A -c 2>/dev/null | cut -f1 -d: | xargs ); do sudo vgck --updatemetadata ${i}; done
        ```
-   Установите SELinux в `enforcing` в файле `/etc/selinux/config`.


## <span class="section-num">3</span> 8 → 9 {#8-9}


### <span class="section-num">3.1</span> Обновление Oracle 8 до Oracle 9 {#обновление-oracle-8-до-oracle-9}


#### <span class="section-num">3.1.1</span> Общая информация {#общая-информация}

-   Материалы:
    -   <https://blogs.oracle.com/linux/post/upgrade-oracle-linux-8-to-oracle-linux-9-using-leapp>
    -   <https://docs.oracle.com/en/operating-systems/oracle-linux/9/leapp/leapp-PreparingfortheUpgrade.html#chap-leapp-prep>


#### <span class="section-num">3.1.2</span> Подготовка к обновлению {#подготовка-к-обновлению}

-   Обновите систему:
    ```shell
    sudo dnf update
    ```
-   Установите утилиту _Leapp_:
    ```shell
    sudo dnf install leapp-upgrade --enablerepo=ol8_appstream,ol8_baseos_latest
    ```
-   Лучше установить SELinux в `permissive` в файле `/etc/selinux/config`.
-   Перегрузите компьютер.
-   Восстановите метки SELinux:
    ```shell
    sudo restorecon -vR /
    ```
-   Удалите внешние репозитории:
    ```shell
    dnf remove epel-release
    ```
-   Проверьте возможность обновления:
    ```shell
    sudo leapp preupgrade --oraclelinux
    ```
-   Отчёт находится в файле `/var/log/leapp/leapp-report.txt`.
-   Там же находятся и рекомендации по устранению проблем.
-   Тут же будет список неподписанных пакетов, которые, скорее всего, вам придётся установить заново после обновления.
-   Также создаётся файл `/var/log/leapp/answerfile`, где нужно подтвердить действия.
-   После исправления запустите утилиту опять. И так до устранения основных недостатков.


#### <span class="section-num">3.1.3</span> Обновление {#обновление}

-   После подготовки сделайте обновление:
    ```shell
    sudo leapp upgrade --oraclelinux
    ```
-   После скачивания необходимых пакетов будет предложено перегрузить машину.
-   После перезагрузки начнётся процесс обновления.


#### <span class="section-num">3.1.4</span> После обновления {#после-обновления}

-   Установите внешние репозитории:
    ```shell
    dnf install epel-release
    ```
-   Обновите необновлённые пакеты:
    ```shell
    dnf -y update
    ```
-   Установите удалённые пакеты, например:
    ```shell
    dnf install fail2ban
    systemctl enable --now fail2ban.service
    ```

    -   Установите SELinux в `enforcing` в файле `/etc/selinux/config`.
    -   Установите ядро Unbreakable Enterprise Kernel:
        ```shell
        dnf -y install kernel-uek kernel-uek-modules kernel-uek-modules-extra
        ```


### <span class="section-num">3.2</span> Обновление Rocky 8 до Rocky 9 {#обновление-rocky-8-до-rocky-9}


#### <span class="section-num">3.2.1</span> Общая информация {#общая-информация}

-   Будем использовать проект Elevate.


#### <span class="section-num">3.2.2</span> Подготовка к обновлению {#подготовка-к-обновлению}

-   Возможно, придётся заменить репозитории: [CentOS 8. Изменение адресов репозиториев]({{< relref "2022-02-10-centos8-changing-repository-addresses" >}})
-   Обновите систему:
    ```shell
    sudo dnf -y upgrade
    ```
-   Перегрузите машину:
    ```shell
    sudo reboot
    ```
-   Установите пакет _elevate-release_:
    ```shell
    sudo dnf install -y http://repo.almalinux.org/elevate/elevate-release-latest-el$(rpm --eval %rhel).noarch.rpm
    ```
-   Отменить исключение пакетов, выполненное при предыдущем обновлении:
    ```shell
    sudo dnf config-manager --save --setopt exclude=''
    ```
-   Установите утилиты для миграции:
    ```shell
    sudo dnf install -y leapp-upgrade leapp-data-rocky
    ```

    -   Другие варианты установки: `centos`, `almalinux`:
        ```shell
        sudo yum install -y leapp-upgrade leapp-data-almalinux
        ```
-   Лучше установить SELinux в `permissive` в файле `/etc/selinux/config`.
-   Перегрузите компьютер.
-   Восстановите метки SELinux:
    ```shell
    sudo restorecon -vR /
    ```
-   Удалите внешние репозитории:
    ```shell
    dnf remove epel-release
    ```
-   Проверьте возможность обновления:
    ```shell
    sudo leapp preupgrade
    ```
-   Отчёт находится в файле `/var/log/leapp/leapp-report.txt`.
-   Там же находятся и рекомендации по устранению проблем.
-   Тут же будет список неподписанных пакетов, которые, скорее всего, вам придётся установить заново после обновления.
-   Также создаётся файл `/var/log/leapp/answerfile`, где нужно подтвердить действия.
-   Общие исправления для Rocky Linux 8.
    -   Изменение конфигурации firewalld:
        ```shell
        sudo sed -i "s/^AllowZoneDrifting=.*/AllowZoneDrifting=no/" /etc/firewalld/firewalld.conf
        ```
    -   Удаление файла конфигурации сети для неподдерживаемого типа сетевого устройства:
        ```shell
        rm /etc/sysconfig/network-scripts/ifcfg-[device_name]
        ```
    -   Обход требования проверки устройства VDO в файле ответов:
        ```shell
        sudo leapp answer --section check_vdo.no_vdo_devices=True
        ```
    -   Удалите неподдерживаемые модули ядра:
        ```shell
        sudo rmmod ip_set
        ```
-   После исправления запустите утилиту опять. И так до устранения основных недостатков.


#### <span class="section-num">3.2.3</span> Обновление {#обновление}

-   Обычно пакеты `make-devel` и `rocky-logos` приводят к сбою обновления. Удалите их:
    ```shell
    dnf -y remove make-devel
    dnf -y remove rocky-logos
    ```
-   После подготовки сделайте обновление:
    ```shell
    sudo leapp upgrade
    ```
-   После скачивания необходимых пакетов будет предложено перегрузить машину.
-   После перезагрузки начнётся процесс обновления.


#### <span class="section-num">3.2.4</span> После обновления {#после-обновления}

-   Удалите старые пакеты от Rocky Linux 8:
    ```shell
    sudo rpm -qa | grep -E 'el8[.-]' | xargs rpm -e
    ```
-   Выполните последующие действия либо обновляйте до следующей версии.
-   Установите внешние репозитории:
    ```shell
    sudo dnf config-manager --set-enabled crb
    sudo dnf -y install epel-release
    sudo /usr/bin/crb enable
    ```
-   Обновите необновлённые пакеты:
    ```shell
    sudo dnf -y update
    ```
-   Установите удалённые пакеты, например:
    ```shell
    sudo dnf -y install fail2ban
    sudo systemctl enable --now fail2ban.service
    ```
-   Если используете LVM, обновите метаданные:
    ```shell
    sudo vgck --updatemetadata <volume_group_name>
    ```

    -   Можно в виде скрипта:
        ```shell
        for i in $(vgdisplay -A -c 2>/dev/null | cut -f1 -d: | xargs ); do sudo vgck --updatemetadata ${i}; done
        ```
-   Установите SELinux в `enforcing` в файле `/etc/selinux/config`.


## <span class="section-num">4</span> 9 → 10 {#9-10}
