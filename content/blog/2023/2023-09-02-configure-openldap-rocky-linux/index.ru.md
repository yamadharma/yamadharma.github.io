---
title: "Настройка Openldap"
author: ["Dmitry S. Kulyabov"]
date: 2023-09-02T19:53:00+03:00
lastmod: 2025-02-12T15:57:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "configure-openldap-rocky-linux"
---

Настройка Openldap.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Установка Openldap {#установка-openldap}

-   Установка сервера openldap:
    ```shell
    dnf -y install openldap-servers openldap-clients
    ```
-   Запуск сервера openldap:
    ```shell
    systemctl enable --now slapd
    ```


## <span class="section-num">2</span> Пароль администратора {#пароль-администратора}

-   Для генерации значения пароля пользователя, подходящего для использования с `ldapadd` или `ldapmodify` используется утилита `slappasswd`.
-   Вначале хэша пароля начинающийся алгоритм хэша (например `{SSHA}`).
-   Создайте хеш пароля:
    ```shell
    slappasswd > /etc/openldap/certs/password
    ```


## <span class="section-num">3</span> Обслуживание {#обслуживание}


### <span class="section-num">3.1</span> Удаление устаревших log-файлов базы данных {#удаление-устаревших-log-файлов-базы-данных}

-   log-файлы базы данных занимают всё больше и больше свободного места.
-   В файле `/var/lib/ldap/DB_CONFIG` можно задать:
    ```conf-unix
    set_flags DB_LOG_AUTOREMOVE on
    ```
-   Кажется, эта опция выполнятся выполняется однократно при перезапуске службы и не повторяется периодически.
-   Для удаления ненужных журналов можно запустить в каталоге с базой данных:
    ```shell
    sudo -u ldap db_archive -d
    ```
-   Можно явно указать каталог базы данных:
    ```shell
    sudo -u ldap db_archive -d -h /var/lib/ldap
    ```
-   Можно добавить в `/etc/cron.d/slapd`:
    ```conf-unix
    # LDAP DB maintenance
    0 3 * * * sudo -u ldap /usr/bin/db_archive -d -h /var/lib/ldap
    ```
