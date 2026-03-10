---
title: "Перенос Openldap на другую машину"
author: ["Dmitry S. Kulyabov"]
date: 2023-09-01T20:12:00+03:00
lastmod: 2023-09-09T18:37:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "openldap-migration"
---

Перенос Openldap на другую машину.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Подготовка {#подготовка}


### <span class="section-num">1.1</span> Установка сервера {#установка-сервера}

-   [Rocky Linux. Установка сервера]({{< relref "2022-08-12-rockylinux-server-installation" >}})


### <span class="section-num">1.2</span> Установка Openldap {#установка-openldap}

-   [Настройка Openldap]({{< relref "2023-09-02-configure-openldap-rocky-linux" >}})


## <span class="section-num">2</span> Дополнительная информация {#дополнительная-информация}


### <span class="section-num">2.1</span> Номер базы данных {#номер-базы-данных}

-   При экспорте ключ `-n` указывает на номер базы openldap. Номер базы виден в конфигурации.
-   База конфигураций всегда является первой, поэтому используется параметр `-n 0`.
-   Обычно пользовательские данные находятся в базе под номером 2 (`-n 2`).
-   Обратите внимание на атрибуты `dn: olcDatabase` в дампе схемы конфигурации.


## <span class="section-num">3</span> Исходная машина {#исходная-машина}

-   1. Остановите службу:
    ```shell
    systemctl stop slapd
    ```
-   Экспортируйте всю схему и `cn=config`:
    ```shell
    slapcat -n 0 -l slapdbackup.conf
    ```
-   Экспортируйте все пользовательские данные, хранящиеся на сервере openldap:
    ```shell
    slapcat -n 2 -l configbackup.ldif
    ```
-   Скопируйте файлы `slapdbackup.conf` и `configbackup.ldif` на новый сервер.


## <span class="section-num">4</span> Целевая машина {#целевая-машина}


### <span class="section-num">4.1</span> Брандмауэр {#брандмауэр}

-   Настройки брандмауэра по умолчанию в RHEL будут блокировать сетевые порты, используемые Kerberos.
-   Необходимо настроить правила брандмауэра на серверах, чтобы разрешить трафик через эти порты.


#### <span class="section-num">4.1.1</span> Сервер ldap {#сервер-ldap}

-   На сервере откройте порты для ldap и ldaps:
    ```shell
    firewall-cmd --zone=public --add-service=ldap
    firewall-cmd --zone=public --add-service=ldap
    firewall-cmd --runtime-to-permanent
    ```


### <span class="section-num">4.2</span> Перенос {#перенос}

-   Сохраните предыдущую конфигурацию:
    ```shell
    cp -R /etc/openldap /etc/openldap.orig
    ```
-   Удалите конфигурацию по умолчанию:
    ```shell
    rm -rf /etc/openldap/slapd.d/*
    ```
-   Восстановите файлы резервной копии:
    ```shell
    slapadd -n 0 -F /etc/openldap/slapd.d -l slapdbackup.conf
    slapadd -n 2 -F /etc/openldap/slapd.d -l configbackup.ldif
    ```
-   Исправьте права доступа к файлам:
    ```shell
    chown -R ldap:ldap /etc/openldap/slapd.d
    ```
-   Восстановите метки SELinux:
    ```shell
    restorecon -vR /etc/openldap
    ```
-   Запустите службу:
    ```shell
    systemctl enable --now slapd
    ```
