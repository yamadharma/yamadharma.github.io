---
title: "fail2ban. Основные настройки"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-30T11:01:00+03:00
lastmod: 2024-09-05T20:10:00+03:00
tags: ["sysadmin", "security"]
categories: ["computer-science"]
draft: false
slug: "fail2ban-basic-settings"
---

fail2ban. Основные настройки.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/fail2ban/fail2ban>
-   Fail2Ban сканирует файлы журналов `/var/log/auth.log` и блокирует IP-адреса, совершающие слишком много неудачных попыток входа в систему.
-   Это достигается путем обновления правил системного брандмауэра, запрещающих новые подключения с этих IP-адресов в течение настраиваемого периода времени.


## <span class="section-num">2</span> Настройка {#настройка}


### <span class="section-num">2.1</span> Общие настройки {#общие-настройки}


### <span class="section-num">2.2</span> Время блокирования {#время-блокирования}

-   Создайте файл локальной конфигурации:
    ```shell
    touch /etc/fail2ban/jail.d/50-default.conf
    ```
-   В файле `/etc/fail2ban/jail.d/50-default.conf` задайте время блокирования хостов:
    ```conf-unix
    [DEFAULT]
    bantime = 360000
    ```


### <span class="section-num">2.3</span> Игнорирование избранных ip-адресов {#игнорирование-избранных-ip-адресов}

-   Добавим игнорирование избранных ip-адресов в файле `/etc/fail2ban/jail.d/50-default.conf`:
    ```conf-unix
    # "ignoreself" specifies whether the local resp. own IP addresses should be ignored
    # (default is true). Fail2ban will not ban a host which matches such addresses.
    ignoreself = true

    # "ignoreip" can be a list of IP addresses, CIDR masks or DNS hosts. Fail2ban
    # will not ban a host which matches an address in this list. Several addresses
    # can be defined using space (and/or comma) separator.
    ignoreip = 127.0.0.1/8 ::1 10.0.0.0/8
    ```
-   Диапазон `10.0.0.0/8` добавлен для примера.


### <span class="section-num">2.4</span> Защита ssh {#защита-ssh}

-   Создадим файл для локальной конфигурации ssh:
    ```shell
    touch /etc/fail2ban/jail.d/80-ssh.conf
    ```
-   В файле `/etc/fail2ban/jail.d/80-ssh.conf` активируйте защиту ssh:
    ```conf-unix
    [sshd]
    enabled = true

    # To use more aggressive sshd modes set filter parameter "mode" in jail.local:
    # normal (default), ddos, extra or aggressive (combines all).
    # See "tests/files/logs/sshd" or "filter.d/sshd.conf" for usage example and details.
    #mode   = normal
    port    = ssh
    logpath = %(sshd_log)s
    backend = %(sshd_backend)s


    [selinux-ssh]

    port     = ssh
    logpath  = %(auditd_log)s
    ```


## <span class="section-num">3</span> Настройка для Proxmox {#настройка-для-proxmox}

-   [Linux. Дистрибутив Proxmox]({{< relref "2024-06-04-linux-proxmox-distribution" >}})


### <span class="section-num">3.1</span> Время блокирования {#время-блокирования}

-   Создайте файл локальной конфигурации:
    ```shell
    touch /etc/fail2ban/jail.d/50-default.conf
    ```
-   В файле `/etc/fail2ban/jail.d/50-default.conf` задайте время блокирования хостов:
    ```conf-unix
    [DEFAULT]
    bantime = 360000
    ```


### <span class="section-num">3.2</span> Игнорирование избранных ip-адресов {#игнорирование-избранных-ip-адресов}

-   Добавим игнорирование избранных ip-адресов в файле `/etc/fail2ban/jail.d/50-default.conf`:
    ```conf-unix
    # "ignoreself" specifies whether the local resp. own IP addresses should be ignored
    # (default is true). Fail2ban will not ban a host which matches such addresses.
    ignoreself = true

    # "ignoreip" can be a list of IP addresses, CIDR masks or DNS hosts. Fail2ban
    # will not ban a host which matches an address in this list. Several addresses
    # can be defined using space (and/or comma) separator.
    ignoreip = 127.0.0.1/8 ::1 10.0.0.0/8
    ```
-   Диапазон `10.0.0.0/8` добавлен для примера.


### <span class="section-num">3.3</span> Защита ssh {#защита-ssh}

-   Создадим файл для локальной конфигурации ssh:
    ```shell
    touch /etc/fail2ban/jail.d/80-ssh.conf
    ```
-   В файле `/etc/fail2ban/jail.d/80-ssh.conf` активируйте защиту ssh:
    ```conf-unix
    [sshd]
    enabled = true
    backend = systemd
    ```
-   Удалите файл `/etc/fail2ban/jail.d/defaults-debian.conf`.


### <span class="section-num">3.4</span> Защита proxmox web-интерфейс {#защита-proxmox-web-интерфейс}

-   Создадим файл для локальной конфигурации proxmox:
    ```shell
    touch /etc/fail2ban/jail.d/80-proxmox.conf
    ```
-   В файле `/etc/fail2ban/jail.d/80-proxmox.conf` активируйте защиту web-интерфейса:
    ```conf-unix
    [proxmox]
    enabled = true
    port = https,http,8006
    filter = proxmox
    backend = systemd
    maxretry = 3
    findtime = 2d
    bantime = 1h
    ```
-   Создайте файл фильтра:
    ```shell
    touch /etc/fail2ban/filter.d/proxmox.conf
    ```
-   Настройте фильтр в файле `/etc/fail2ban/filter.d/proxmox.conf`:
    ```shell
    [Definition]
    failregex = pvedaemon\[.*authentication failure; rhost=<HOST> user=.* msg=.*
    ignoreregex =
    journalmatch = _SYSTEMD_UNIT=pvedaemon.service
    ```


## <span class="section-num">4</span> Основные операции {#основные-операции}


### <span class="section-num">4.1</span> Удалить все записи из списков блокировки {#удалить-все-записи-из-списков-блокировки}

-   Для удаления всех записей из списков блокировки выполните скрипт:
    ```shell
    #!/bin/bash

    for JAIL in $(fail2ban-client status | grep 'Jail list:' | awk 'BEGIN {FS="\t"} {print $2}' | sed 's/, / /g')
    do
      for IP in $(fail2ban-client status ${JAIL} | grep 'Banned IP list:' | awk 'BEGIN {FS="\t"} {print $2}' | sed 's/ /\n/g')
      do
        fail2ban-client set ${JAIL} unbanip ${IP}
      done
    done

    unset JAIL IP

    exit 0
    ```
