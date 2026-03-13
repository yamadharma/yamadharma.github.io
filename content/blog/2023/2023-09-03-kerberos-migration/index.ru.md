---
title: "Перенос kerberos на другую машину"
author: ["Dmitry S. Kulyabov"]
date: 2023-09-03T18:13:00+03:00
lastmod: 2023-09-03T20:02:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "kerberos-migration"
---

Перенос службы Kerberos на другую машину.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Исходная машина {#исходная-машина}


## <span class="section-num">2</span> Целевая машина {#целевая-машина}


### <span class="section-num">2.1</span> Установка программного обеспечения {#установка-программного-обеспечения}

-   Установите Kerberos:
    ```shell
    dnf -y install krb5-server krb5-workstation
    ```


### <span class="section-num">2.2</span> Брандмауэр {#брандмауэр}

-   Настройки брандмауэра по умолчанию в RHEL будут блокировать сетевые порты, используемые Kerberos.
-   Необходимо настроить правила брандмауэра на серверах, чтобы разрешить трафик через эти порты.


#### <span class="section-num">2.2.1</span> Сервер Kerberos {#сервер-kerberos}

-   На сервере Kerberos откройте порты udp 88 и 646:
    ```shell
    firewall-cmd --zone=public --add-service=kerberos
    firewall-cmd --zone=public --add-service=kadmin
    firewall-cmd --runtime-to-permanent
    ```


### <span class="section-num">2.3</span> Разрешение имён {#разрешение-имён}

-   Возможно, следует записать адрес сервера в `/etc/hosts`.


### <span class="section-num">2.4</span> Файл конфигурации kerberos {#файл-конфигурации-kerberos}

-   Перенесите конфигурационный файл `/etc/krb5.conf`.
-   Лучше отредактировать новый, установив необходимые _realms_.


### <span class="section-num">2.5</span> База данных {#база-данных}

-   Восстановите базу данных Kerberos:
    ```shell
    kdb5_util load kdb5_dump
    ```


### <span class="section-num">2.6</span> Файл конфигурации сервера kerberos {#файл-конфигурации-сервера-kerberos}

-   Восстановите `/var/kerberos/krb5kdc/kdc.conf` из резервной копии.


### <span class="section-num">2.7</span> Файл прав доступа к серверу администрирования kerberos {#файл-прав-доступа-к-серверу-администрирования-kerberos}

-   Восстановите `/var/kerberos/krb5kdc/kadm5.acl` из резервной копии.


### <span class="section-num">2.8</span> Файл тайника {#файл-тайника}

-   stash-файл позволяет KDC аутентифицировать себя для утилит базы данных, таких как kadmin, kadmind, krb5kdcи kdb5_util.
-   Запустите команду ниже, чтобы сохранить принципал в файле (требуется пароль администратора kdc):
    ```shell
    kdb5_util stash
    ```


### <span class="section-num">2.9</span> Запуск сервера {#запуск-сервера}

-   Запустите сервер:
    ```shell
    systemctl enable --now krb5kdc.service
    ```
