---
title: "Rocky Linux. Установка сервера"
author: ["Dmitry S. Kulyabov"]
date: 2022-08-12T13:57:00+03:00
lastmod: 2025-12-11T10:48:00+03:00
tags: ["redhat", "sysadmin", "linux"]
categories: ["computer-science"]
draft: false
slug: "rockylinux-server-installation"
---

Установка базисного сервера на Rocky Linux.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Rocky Linux --- сборка RedHat Linux, пришедший на смену Centos (см. [Замена Centos]({{< relref "2021-05-25-replacing-centos" >}})).
-   Сайт: <https://rockylinux.org/>.
-   Образы:
    -   <https://rockylinux.org/download>;
    -   <http://dl.rockylinux.org/vault/rocky/>.


### <span class="section-num">1.1</span> Дополнительные стандартные репозитории {#дополнительные-стандартные-репозитории}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Стандартные дополнительные репозитории
</div>

| Repository     | Rocky 8 | Rocky 9 | Включён | Примечание                                                         |
|----------------|---------|---------|---------|--------------------------------------------------------------------|
| Extras         | Yes     | Yes     | Yes     | Дополнительные функции, не нарушающие совместимость исходного кода |
| Plus           | Yes     | Yes     | No      | Либо заменяет стандартный компонент, либо под одну архитектуру     |
| RT (real time) | Yes     | Yes     | No      | Пакеты для                                                         |
| NFV            | Yes     | TBD     | No      |                                                                    |
| SAP / SAP HANA | No      | TBD     | No      |                                                                    |
| Devel / devel  | Yes     | Yes     | No      |                                                                    |


### <span class="section-num">1.2</span> Репозитории сообщества {#репозитории-сообщества}

-   Дополнительные пакеты для Enterprise Linux (EPEL):
    -   документация: <http://fedoraproject.org/wiki/EPEL>;
    -   наиболее часто используемй репозиторий;
    -   сборки пакетов Fedora для каждого поддерживаемого корпоративного Linux;
    -   пакеты не заменяют базовые;
    -   установка:
        ```shell
        dnf config-manager --set-enabled crb
        dnf install epel-release
        ```
-   Репозиторий Community Enterprise Linux (ELRepo):
    -   фокусируется на более новых ядрах и пакетах драйверов kmod для улучшения поддержки оборудования;
    -   репозитории ядра должны быть включены для его использования;
    -   установка:
        ```shell
        dnf install elrepo-release
        ```
-   RPM Fusion:
    -   программное обеспечение, которое Fedora Project или Red Hat не хотят поставлять в Enterprise Linux и Fedora;
    -   базовые пакеты не заменяются;
    -   установка:
        ```shell
        dnf install rpmfusion-free-release
        ```
-   Репозиторий Remi:
    -   сайт: <http://rpms.remirepo.net/>;
    -   поддерживает большую коллекцию RPM, включая, среди прочего, последние версии PHP;
    -   это коллекция репозиториев;
    -   документация: <http://blog.remirepo.net/pages/English-FAQ>;
    -   может конфликтовать с другими сторонними репозиториями.
-   GhettoForge:
    -   документация: <http://ghettoforge.org/index.php/Usage>;
    -   пакеты, которых нет в других сторонних репозиториях;
    -   пакеты, перезаписывающие базу, будут в репозитории `gf-plus`.


## <span class="section-num">2</span> Установка образа {#установка-образа}

-   [Proxmox. Установка Rocky Linux]({{< relref "2025-06-22--proxmox-install-rocky-linux" >}})


## <span class="section-num">3</span> После установки {#после-установки}

-   Здесь даны общие шаги для большей части серверов.


### <span class="section-num">3.1</span> Обновления {#обновления}

-   Обновить все пакеты
    ```shell
    dnf -y update
    ```


### <span class="section-num">3.2</span> Установка локализации {#установка-локализации}

-   Проверьте текущую локализацию:
    ```shell
    localectl status
    ```
-   Посмотрите доступные локализации:
    ```shell
    localectl list-locales
    ```
-   Если нет необходимой, установите её:
    ```shell
    sudo dnf -y install glibc-langpack-ru
    ```
-   Установите нужную локализацию:
    ```shell
    sudo localectl set-locale ru_RU.UTF-8
    ```
-   Проверьте текущую локализацию:
    ```shell
    localectl status
    ```


### <span class="section-num">3.3</span> Дополнительные репозитории {#дополнительные-репозитории}

-   Установим _EPEL_:
    ```shell
    sudo dnf config-manager --set-enabled crb
    sudo dnf -y install epel-release
    ```


### <span class="section-num">3.4</span> Установка часового пояса {#установка-часового-пояса}

-   Просмотрите список всех часовых поясов:
    ```shell
    sudo timedatectl list-timezones
    ```
-   Установите часовой пояс (например, UTC):
    ```shell
    sudo timedatectl set-timezone Etc/UTC
    ```


### <span class="section-num">3.5</span> Синхронизация времени {#синхронизация-времени}

-   Запустите демон:
    ```shell
    sudo systemctl enable --now chronyd
    ```
-   Проверьте работу демона `chronyd`:
    ```shell
    sudo chronyc -a tracking
    ```
-   Включите сетевую синхронизацию времени:
    ```shell
    sudo timedatectl set-ntp true
    ```
-   Проверьте, работает ли он:
    ```shell
    sudo timedatectl status
    ```


### <span class="section-num">3.6</span> Разрешение имён {#разрешение-имён}


#### <span class="section-num">3.6.1</span> systemd-resolved {#systemd-resolved}

-   Можно установить кеширующий локальный name-server `systemd-resolved`:
    ```shell
    dnf -y install systemd-resolved
    ```
-   Файл настройки: `/etc/systemd/resolved.conf`.
-   Можно в нём ничего не менять.
-   Запустим службу:
    ```shell
    systemctl enable --now systemd-resolved.service
    ```
-   Установите резольвер:
    ```shell
    ln -snf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
    ```
-   Проверить работу можно командой:
    ```shell
    resolvectl
    ```


### <span class="section-num">3.7</span> Повышение комфорта работы {#повышение-комфорта-работы}

-   Программы для удобства работы в консоли:
    ```shell
    sudo dnf -y install tmux mc kitty-terminfo
    ```
-   Программы мониторинга:
    ```shell
    sudo dnf -y install htop lsof
    ```
-   Утилита для ssh:
    ```shell
    sudo dnf -y install mosh
    ```
-   Удобство работы с bash:
    ```shell
    sudo dnf -y install bash-completion bash-color-prompt
    ```
-   Разные утилиты:
    ```shell
    sudo dnf -y install wget git tar zstd 7zip
    ```


### <span class="section-num">3.8</span> Отключение графического интерфейса {#отключение-графического-интерфейса}

-   Посмотрите, в каком режиме загружается сервер:
    ```shell
    sudo systemctl get-default
    ```
-   Если результатом является `graphical.target`, то отключите загрузку графического интерфейса.
-   Переключите на загрузку в терминальном многопользовательском режиме:
    ```shell
    sudo systemctl set-default multi-user.target
    ```


### <span class="section-num">3.9</span> Безопасность {#безопасность}


#### <span class="section-num">3.9.1</span> Fail2ban {#fail2ban}

-   Защита от атак:
    ```shell
    dnf -y install fail2ban
    ```

-   Следует сконфигурировать (см. [fail2ban. Основные настройки]({{< relref "2023-10-30-fail2ban-basic-settings" >}})) и запустить:
    ```shell
    systemctl enable --now fail2ban.service
    ```
-   Проверьте работу:
    ```shell
    tail -f /var/log/fail2ban.log
    ```


### <span class="section-num">3.10</span> Администрирование {#администрирование}


#### <span class="section-num">3.10.1</span> Автоматическое обновление {#автоматическое-обновление}

-   При необходимости можно использовать автоматическое обновление (см. [Автообновление систем на базе деривативов RedHat]({{< relref "2022-09-25-redhat-based-systems-auto-update" >}})).
-   Установка программного обеспечения:
    ```shell
    sudo dnf -y install dnf-automatic
    ```
-   Задаёте необходимую конфигурацию в файле `/etc/dnf/automatic.conf`.
-   Запустите таймер:
    ```shell
    sudo systemctl enable --now dnf-automatic.timer
    ```


## <span class="section-num">4</span> Установка дополнительного программного обеспечения {#установка-дополнительного-программного-обеспечения}

-   Описываются дополнительные пакеты для специализированных серверов.


### <span class="section-num">4.1</span> Утилиты {#утилиты}


#### <span class="section-num">4.1.1</span> rsync {#rsync}

-   Установим rsync:
    ```shell
    dnf install rsync
    ```


### <span class="section-num">4.2</span> Безопасность {#безопасность}


#### <span class="section-num">4.2.1</span> Работа с  Let's Encrypt {#работа-с-let-s-encrypt}

-   Установим certbot:
    ```shell
    dnf install certbot
    ```
-   Установим модуль под Apache:
    ```shell
    dnf install python3-certbot-apache
    ```
-   Если используется Nginx, установим модуль под Nginx:
    ```shell
    install certbot python3-certbot-nginx
    ```


### <span class="section-num">4.3</span> Синхронизация времени {#синхронизация-времени}


#### <span class="section-num">4.3.1</span> systemd-timesyncd {#systemd-timesyncd}

-   Можно использовать альтернативный метод синхронизации времени из пакета systemd.
-   Установите демон синхронизации:
    ```shell
    dnf install systemd-timesyncd
    ```
-   Запустите демон:
    ```shell
    systemctl enable --now systemd-timesyncd
    ```
-   Включите сетевую синхронизацию времени:
    ```shell
    timedatectl set-ntp true
    ```
-   Проверьте, работает ли он:
    ```shell
    timedatectl status
    ```
-   Подробная информация:
    ```shell
    timedatectl timesync-status
    ```


#### <span class="section-num">4.3.2</span> Сервер сетевого времени {#сервер-сетевого-времени}

-   В файле `/etc/chrony.conf` Разрешите подключение клиентов из локальной сети:
    ```conf-unix
    allow 192.168.0.0/16
    ```

-   Запустите сервер сетевого времени:
    ```shell
    systemctl enable --now chronyd
    ```
-   Проверьте пулы NTP:
    ```shell
    chronyc sources
    ```
-   Проверьте состояние синхронизации NTP:
    ```shell
    chronyc tracking
    ```
-   Чтобы принимать входящие запросы клиентов, разрешите службу NTP через брандмауэр:
    ```shell
    firewall-cmd --permanent --add-service=ntp
    ```
-   Перезапустите брандмауэр:
    ```shell
    firewall-cmd --reload
    ```


### <span class="section-num">4.4</span> Вариации на тему стека LAMP (Linux, Apache, MySQL, PHP) {#вариации-на-тему-стека-lamp--linux-apache-mysql-php}

-   Устанавливается, если необходимо поддерживать приложение на PHP.
-   Обычно используются базы данных Mysql или Postgresql.


#### <span class="section-num">4.4.1</span> Apache {#apache}

-   Установка Apache:
    ```shell
    dnf install httpd
    ```
-   Установка поддержки HTTPS:
    ```shell
    dnf install mod_ssl
    ```


#### <span class="section-num">4.4.2</span> PHP {#php}

-   Определим, какие версии php возможно установить:
    ```shell
    sudo dnf module list php
    ```
-   Установим php-8.2:
    ```shell
    sudo dnf module reset php
    sudo dnf module enable php:8.2
    dnf install php
    sudo dnf -y update
    ```


#### <span class="section-num">4.4.3</span> Mysql {#mysql}

-   Установим _mariadb_:
    ```shell
    dnf install mariadb
    dnf install mariadb-server
    ```
-   Установим модуль для php:
    ```shell
    dnf install php-mysqlnd
    ```


### <span class="section-num">4.5</span> Администрирование {#администрирование}


#### <span class="section-num">4.5.1</span> Резервное копирование {#резервное-копирование}

-   Для резервного копирования используется _restic_:
    ```shell
    dnf install restic
    ```


### <span class="section-num">4.6</span> Файловые системы {#файловые-системы}


#### <span class="section-num">4.6.1</span> GlusterFS {#glusterfs}

-   Установите пакет для последнего релиза GlusterFS (см. <https://wiki.centos.org/SpecialInterestGroup/Storage>):
    ```shell
    dnf install centos-release-gluster
    ```
-   Установка клиента GlusterFS:
    ```shell
    dnf install glusterfs
    dnf install glusterfs-fuse
    ```


### <span class="section-num">4.7</span> DNS сервера {#dns-сервера}

-   [DNS. PowerDNS Recursor]({{< relref "2023-05-23-dns-powerdns-recursor" >}})
-   [DNS. Bind]({{< relref "2023-09-19-dns-bind" >}})


### <span class="section-num">4.8</span> Контроль версий {#контроль-версий}


#### <span class="section-num">4.8.1</span> git {#git}

-   Установите `git`:
    ```shell
    dnf -y install git
    ```


#### <span class="section-num">4.8.2</span> cvs {#cvs}

-   Установите `cvs`:
    ```shell
    dnf -y install cvs
    ```


### <span class="section-num">4.9</span> Средства разработки {#средства-разработки}

-   Установим группу средств разработки:
    ```shell
    dnf -y group install "Development Tools"
    ```


### <span class="section-num">4.10</span> Виртуализация и контейнеры {#виртуализация-и-контейнеры}

-   [Контейнеры. podman]({{< relref "2024-12-04-containers-podman" >}})
