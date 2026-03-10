---
title: "Установка сервера afs"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-28T10:22:00+03:00
lastmod: 2025-09-10T17:30:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "afs-server-installation"
---

Установка сервера afs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Первоначальная установка {#первоначальная-установка}

-   [Rocky Linux. Установка сервера]({{< relref "2022-08-12-rockylinux-server-installation" >}})


## <span class="section-num">2</span> Предварительные замечания {#предварительные-замечания}


### <span class="section-num">2.1</span> Минимальная установка {#минимальная-установка}

-   Для простой установки можно использовать один сервер для размещения Kerberos KDC, сервера базы данных OpenAFS и файлового сервера OpenAFS.
-   Для производственной среды рекомендуется развернуть Kerberos KDC на выделенном безопасном сервере, серверы баз данных OpenAFS --- на трех отдельных компьютерах, а при необходимости --- несколько файловых серверов.


### <span class="section-num">2.2</span> Дисковые разделы {#дисковые-разделы}

-   Понадобится хотя бы один раздел на файловом сервере для хранения томов для AFS.
-   Его надо будет примонтировать в `/vicepa`.
-   Если необходимо несколько разделов, их можно смонтировать в `/vicepb`, `/vicepc` и т. д.
-   Файловый сервер использует файловое хранилище (не блочное).
-   Файловые системы: ext3, ext4, xfs.
-   Лучше создать для этого отдельную партицию.


### <span class="section-num">2.3</span> Сеть {#сеть}

-   DNS должен работать правильно при прямом и обратном поиске имён.
-   Серверам необходим хотя бы один интерфейс IPv4, доступный клиентам AFS. Интерфейсы IPv6 пока не поддерживаются.


### <span class="section-num">2.4</span> Синхронизация времени {#синхронизация-времени}

-   Kerberos и, следовательно, OpenAFS требуют хорошей синхронизации часов между клиентами и серверами.


## <span class="section-num">3</span> Брандмауэр {#брандмауэр}

-   Настройки брандмауэра по умолчанию в RHEL будут блокировать сетевые порты, используемые Kerberos и OpenAFS.
-   Необходимо настроить правила брандмауэра на серверах, чтобы разрешить трафик через эти порты.


### <span class="section-num">3.1</span> Сервер Kerberos {#сервер-kerberos}

-   На сервере Kerberos откройте порты udp 88 и 646:
    ```shell
    firewall-cmd --zone=public --add-port=88/udp
    firewall-cmd --zone=public --add-port=646/udp
    firewall-cmd --runtime-to-permanent
    ```


### <span class="section-num">3.2</span> Сервер баз данных OpenAFS {#сервер-баз-данных-openafs}

-   На серверах баз данных OpenAFS откройте udp-порты 7002, 7003 и 7007:
    ```shell
    firewall-cmd --zone=public --add-port=7002/udp
    firewall-cmd --zone=public --add-port=7003/udp
    firewall-cmd --zone=public --add-port=7007/udp
    firewall-cmd --runtime-to-permanent
    ```


### <span class="section-num">3.3</span> Файловый сервер OpenAFS {#файловый-сервер-openafs}

-   На файловых серверах OpenAFS откройте udp-порты 7000, 7005 и 7007:
    ```shell
    firewall-cmd --zone=public --add-port=7000/udp
    firewall-cmd --zone=public --add-port=7005/udp
    firewall-cmd --zone=public --add-port=7007/udp
    firewall-cmd --runtime-to-permanent
    ```


### <span class="section-num">3.4</span> Клиент OpenAFS {#клиент-openafs}

-   Клиенты OpenAFS используют порт udp 7001. Откройте порт udp 7001 в любой системе, в которой установлен клиент OpenAFS:
    ```shell
    firewall-cmd --zone=public --add-port=7001/udp
    firewall-cmd --runtime-to-permanent
    ```


## <span class="section-num">4</span> Установка Kerberos {#установка-kerberos}

-   Установите серверный и клиентский пакеты Kerberos:
    ```shell
    dnf install -y krb5-server krb5-workstation krb5-libs
    ```
-   Замените все примеры имени хоста `kerberos.example.com` фактическим именем вашего сервера Kerberos в файле `/etc/krb5.conf`.


### <span class="section-num">4.1</span> Сервер Kerberos {#сервер-kerberos}

-   На машине сервера Kerberos настройте замените каждый экземпляр `EXAMPLE.COM` именем своей области в следующих файлах конфигурации:
-   `/etc/krb5.conf`
-   `/var/kerberos/krb5kdc/kdc.conf`
-   `/var/kerberos/krb5kdc/kadm5.acl`
-   Замените все примеры имени хоста `kerberos.example.com` фактическим именем вашего сервера Kerberos в файле `/etc/krb5.conf`.
-   Создайте базу данных Kerberos с помощью команды `krb5_util` (вам будет предложено ввести основной пароль):
    ```shell
    /usr/sbin/kdb5_util create -s
    ```
-   Запустите серверы Kerberos:
    ```shell
    systemctl start krb5kdc
    systemctl start kadmin
    systemctl enable krb5kdc
    systemctl enable kadmin
    ```


## <span class="section-num">5</span> Компиляция программного обеспечения {#компиляция-программного-обеспечения}


### <span class="section-num">5.1</span> Компиляция сервера {#компиляция-сервера}

-   Исходные архивы OpenAFS доступны на веб-сайте OpenAFS.
-   Нужно будет собрать собрать RPM-пакеты с помощью команды `rpmbuild`.
-   Установите необходимое программное обеспечение:
    ```shell
    dnf install rpm-build yum-utils make perl libtool bzip2 wget mock elfutils-libelf-devel libtirpc-devel -y
    ```
-   Установите версия ядра для разработчиков:
    ```shell
    dnf install -y "kernel-devel-uname-r = $(uname -r)"
    dnf install -y elfutils-devel
    dnf install -y dkms gcc kernel-devel kernel-headers
    ```


#### <span class="section-num">5.1.1</span> Готовый пакет srpm {#готовый-пакет-srpm}

-   К сожалению, для более новых версий пакетов нет.
-   Скачайте пакет исходных кодов для openafs:
    ```shell
    wget https://www.openafs.org/dl/openafs/<version>/openafs-<version>-1-src.rpm
    ```
-   Здесь `<version>` указывается версия OpenAFS, которую вы хотите установить, например `1.8.10`:
    ```shell
    wget https://www.openafs.org/dl/openafs/1.8.10/openafs-1.8.10-1.src.rpm
    ```


#### <span class="section-num">5.1.2</span> Сделать собственный srpm {#сделать-собственный-srpm}

-   Создайте структуру каталогов для сборки:
    ```shell
    mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
    ```
-   Скачайте исходники OpenAFS:
    ```shell
    cd ~/rpmbuild/SOURCES
    wget https://www.openafs.org/dl/openafs/1.8.13.2/openafs-1.8.13.2-src.tar.bz2
    wget https://www.openafs.org/dl/openafs/1.8.13.2/openafs-1.8.13.2-doc.tar.bz2
    ```
-   Используйте стандартный шаблон из исходников:
    ```shell
    tar xjvf openafs-1.8.13.2-src.tar.bz2
    cd openafs-1.8.13.2/src/packaging/RedHat
    ./makesrpm.pl ~/rpmbuild/SOURCES/openafs-1.8.13.2-src.tar.bz2 /root/rpmbuild/SOURCES/openafs-1.8.13.2-doc.tar.bz2
    mv openafs-1.8.13.2-1.src.rpm ~/rpmbuild/SRPMS
    ```


#### <span class="section-num">5.1.3</span> Компиляция пакета {#компиляция-пакета}

-   Установите необходимы зависимости:
    ```shell
    cd ~/rpmbuild/SRPMS
    dnf builddep openafs-1.8.13.2-1.src.rpm
    ```
-   Откомпилите исходные коды:
    ```shell
    rpmbuild --rebuild --define "build_userspace 1" --define "build_modules 1" --define "kmod_kernel_versions $(uname -r)" openafs-1.8.13.2-1.src.rpm
    ```
-   Опции:
    -   `build_userspace 1` : собирать пользовательские компоненты;
    -   `build_modules 1` : собирать модули ядра;
    -   `kmod_kernel_versions` : версия ядра для модулей.
-   Можно не компилировать модули ядра, соответственно вы не сможете использовать сервер как клиента.
-   Можно откомпилить всё с поддержкой моделей ядра (см. компиляцию для клиентов).
-   Можно собрать и через mock (при желании, тогда ручной сборки не надо):
    ```shell
    mock -r epel-9-x86_64 --rebuild ~/rpmbuild/SRPMS/openafs-*.src.rpm
    ```
-   После успешной сборки пакеты будут в:
    ```shell
    ls ~/rpmbuild/RPMS/x86_64/openafs-*.rpm
    ```


#### <span class="section-num">5.1.4</span> Установка пакетов {#установка-пакетов}

-   Установите пакеты:
    ```shell
    sudo dnf -y install ~/rpmbuild/RPMS/x86_64/openafs-1.8.13.2-*.rpm ~/rpmbuild/RPMS/x86_64/openafs-{client,server,krb5,authlibs,compat,docs}-1.8.13.2-*.rpm ~/rpmbuild/RPMS/x86_64/{dkms,kmod}-openafs-1.8.13.2-*.rpm
    ```


### <span class="section-num">5.2</span> Компиляция клиента {#компиляция-клиента}

-   Модуль ядра OpenAFS должен соответствовать вашей версии ядра.
-   Если вы не поддерживаете локальный репозиторий, который отслеживает каждый выпуск ядра и обновляет его сборки kmod, вам нужно будет использовать механизм DKMS для установки модуля ядра.
-   Установите необходимое программное обеспечение:
    ```shell
    dnf install rpm-build yum-utils make perl libtool bzip2 wget -y
    ```
-   Скачайте пакет исходных кодов для openafs:
    ```shell
    wget https://www.openafs.org/dl/openafs/<version>/openafs-<version>-1-src.rpm
    ```
-   Здесь `<version>` указывается версия OpenAFS, которую вы хотите установить, например `1.8.10`:
    ```shell
    wget https://www.openafs.org/dl/openafs/1.8.10/openafs-1.8.10-1.src.rpm
    ```
-   Установите необходимы зависимости:
    ```shell
    dnf builddep openafs-<version>-1.src.rpm
    ```
-   Установите версия ядра для разработчиков:
    ```shell
    dnf install -y "kernel-devel-uname-r == $(uname -r)"
    dnf install -y elfutils-devel
    dnf install -y dkms gcc kernel-devel kernel-headers
    ```

-   Откомпилите исходные коды:
    ```shell
    rpmbuild --rebuild openafs-<version>-1.src.rpm
    ```


## <span class="section-num">6</span> Установка сервера OpenAFS {#установка-сервера-openafs}


### <span class="section-num">6.1</span> Установка сервера {#установка-сервера}

-   Установите серверные пакеты OpenAFS из каталога RPMS rpmbuild:
    ```shell
    cd ~/rpmbuild/RPMS/x86_64
    dnf install -y openafs-<version>-1.el9.x86_64.rpm openafs-server-<version>-1.el9.x86_64.rpm openafs-docs-<version>-1.el9.x86_64.rpm openafs-krb5-<version>-1.el9.x86_64.rpm
    ```


### <span class="section-num">6.2</span> Установка клиента {#установка-клиента}

-   При установке менеджера кэша на сервере OpenAFS сначала удалите символические ссылки, созданные bosserver. Это будет мешать, если клиент установлен.
    ```shell
    test -h /usr/vice/etc/ThisCell && rm /usr/vice/etc/ThisCell
    test -h /usr/vice/etc/CellServDB && rm /usr/vice/etc/CellServDB
    ```
-   Обязательно перезагрузитесь перед установкой модуля ядра OpenAFS.
-   Установите пакеты OpenAFS из каталога RPMS rpmbuild:
    ```shell
    cd ~/rpmbuild/RPMS/x86_64
    dnf install -y  openafs-<version>-1.el9.x86_64.rpm openafs-client-<version>-1.el9.x86_64.rpm openafs-krb5-<version>-1.el9.x86_64.rpm dkms-openafs-<version>-1.el9.x86_64.rpm
    ```
