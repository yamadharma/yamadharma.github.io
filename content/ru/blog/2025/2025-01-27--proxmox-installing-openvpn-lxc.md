---
title: "Proxmox. Установка OpenVPN в LXC"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-27T19:16:00+03:00
lastmod: 2025-11-19T14:57:00+03:00
draft: false
slug: "proxmox-installing-openvpn-lxc"
---

Proxmox. Установка OpenVPN в LXC.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Информация о дистрибутиве {#информация-о-дистрибутиве}

-   [Linux. Дистрибутив Turnkey]({{< relref "2025-01-26--linux-distro-turnkey" >}})
-   Репозиторий: <https://github.com/turnkeylinux-apps/openvpn>
-   Сайт: <https://www.turnkeylinux.org/openvpn>


## <span class="section-num">2</span> Создание контейнера {#создание-контейнера}

-   Обновим список контейнеров:
    ```shell
    pveam update
    ```
-   Установим дистрибутив Turnkey-OpenVPN (см. [Linux. Дистрибутив Turnkey]({{< relref "2025-01-26--linux-distro-turnkey" >}})):
    ```shell
    pveam available | grep openvpn
    pveam download local debian-12-turnkey-openvpn_18.1-1_amd64.tar.gz
    pveam list local
    ```
-   Создадим контейнер:
    ```shell
    pct create 123 local:vztmpl/debian-12-turnkey-openvpn_18.1-1_amd64.tar.gz --unprivileged 1 -features nesting=1 --net0 name=eth0,bridge=vmbr1,tag=5,firewall=1,ip=12.34.56.78/24,gw=12.34.56.254,type=veth --storage local-lvm --hostname=ovpn
    ```


## <span class="section-num">3</span> Устройство /dev/net/tun {#устройство-dev-net-tun}

-   Поскольку мы использовали непривилегированный контейнер, необходимо прокинуть из контейнера на хост устройство `/dev/net/tun`.
-   В качестве альтернативы можно использовать привилегированный контейнер (но не надо).
-   Посмотрим конфигурацию контейнера:
    ```shell
    pct config 123
    ```
-   Отредактируем файл конфигурации:
    ```shell
    vi /etc/pve/lxc/123.conf
    ```
-   Добавьте следующие строки в конце.
    -   Настроить политики безопасности:
        ```conf-unix
        lxc.apparmor.profile: unconfined
        lxc.cgroup.devices.allow: a
        lxc.cap.drop:
        ```
    -   Чтобы создать устройство:
        ```conf-unix
        lxc.cgroup2.devices.allow: c 10:200 rwm
        lxc.mount.entry: /dev/net/tun dev/net/tun none bind,create=file
        ```
-   Чтобы непривилегированный контейнер мог получить доступ к `/dev/net/tun`, необходимо установить владельца:
    ```shell
    chown 100000:100000 /dev/net/tun
    ```

-   Проверьте, что разрешения устанавливаются правильно:
    ```shell
    ls -l /dev/net/tun
    ```


## <span class="section-num">4</span> Запуск контейнера {#запуск-контейнера}

-   Запустите контейнер:
    ```shell
    pct start 123
    ```
-   Подключитесь к контейнеру:
    ```shell
    pct enter 123
    ```
-   Чтобы сконфигурировать openvpn, надо подключиться к консоли через web-интерфейс.
-   Но грузится долго.
-   Вначале просто чёрный экран.
-   При конфигурировании можно пропустить конфигурацию для Turnkey Hub.
-   После установки можно дополнительно доконфигурить сервер.


## <span class="section-num">5</span> Настройки {#настройки}


### <span class="section-num">5.1</span> HMAC authentication {#hmac-authentication}

-   В утилите `openvpn-addclient` жёстко зашит алгоритм `AES-256-GCM` для HMAC authentication.
-   В конфигурации сервера данная настройка отсутствует.
-   Я добавил в файл `/etc/openvpn/server.conf`:
    ```conf-unix
    # TLS Security
    cipher AES-256-GCM
    tls-version-min 1.2
    tls-cipher TLS-DHE-RSA-WITH-AES-256-GCM-SHA384:TLS-DHE-RSA-WITH-AES-256-CBC-SHA256:TLS-DHE-RSA-WITH-AES-128-GCM-SHA256:TLS-DHE-RSA-WITH-AES-128-CBC-SHA256
    auth SHA512
    auth-nocache
    ```
-   Перестартуйте сервер:
    ```shell
    systemctl restart openvpn@server.service
    ```


### <span class="section-num">5.2</span> Использование одного ключа несколькими клиентами {#использование-одного-ключа-несколькими-клиентами}

-   Удобно использовать один ключ на учебную группу.
-   Я добавил в файл `/etc/openvpn/server.conf`:
    ```conf-unix
    # Enable multiple client to connect with same Certificate key
    duplicate-cn
    ```
-   Перестартуйте сервер:
    ```shell
    systemctl restart openvpn@server.service
    ```


### <span class="section-num">5.3</span> Временная зона {#временная-зона}

-   Некоторые клиенты требуют, чтобы ключи создавались в той же временной зоне, что и на клиенте.
-   Можно изменить временную зону:
    ```shell
    dpkg-reconfigure tzdata
    ```


## <span class="section-num">6</span> Конфигурирование OpenVPN клиента {#конфигурирование-openvpn-клиента}


### <span class="section-num">6.1</span> Добавление конфигурации на сервере {#добавление-конфигурации-на-сервере}

-   Заходим на сервер по SSH.
-   Создаём пользователя VPN:
    ```shell
    openvpn-addclient client-name client-email
    ```

    -   `client-name` : имя пользователя;
    -   `client-email` : почта пользователя.
-   Профиль пользователя будет находиться в файле `/etc/openvpn/easy-rsa/keys/client-name.ovpn`.
-   Если не был сконфигурирован FQDN, а просто добавлен IP-адрес сервера, нужно будет изменить в первой строке конфигурации `vpn.example.com` на IP адрес сервера OpenVPN.


### <span class="section-num">6.2</span> Загрузка конфигурации на клиента {#загрузка-конфигурации-на-клиента}

-   Из консоли SSH выполняем команду:
    ```shell
    /var/www/openvpn/bin/addprofile client-name
    ```
-   С помощью этой команды создайтся ссылка на скачивание файла конфигурации и QR код, считав который с помощью камеры телефона мы автоматически скачиваем и импортируем профиль пользователя в мобильный клиент OpenVPN.
-   Чтобы попасть на URL автоконфигурации клиента, нужно к URL главной страницы добавить часть строки, начинающейся с `/profiles/`, например: `https://IPадрес_сервера/profiles/c87019e41b4ae3dabf94ba86ee126bf35f0f9c01/`.
-   Таким образом мы создаем страничку, откуда будет удобно скачать профиль самостоятельно или импортировать его в телефон с помощью QR кода.


### <span class="section-num">6.3</span> Удаление профиля {#удаление-профиля}

-   Вручную запустить удаление истекших профилей:
    ```shell
    /etc/cron.hourly/openvpn-profiles-delexpired
    ```
-   Отменить сертификат клиента и удалить профиль клиента:
    ```shell
    openvpn-removeclient client-name
    ```
