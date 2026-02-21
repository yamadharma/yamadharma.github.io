---
title: "Клиенты ACME. Certbot"
author: ["Dmitry S. Kulyabov"]
date: 2022-05-02T16:54:00+03:00
lastmod: 2024-09-16T13:06:00+03:00
tags: ["sysadmin", "network", "security"]
categories: ["computer-science"]
draft: false
slug: "acme-clients-certbot"
---

Клиент протокола ACME _Certbot_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Бесплатный программный инструмент с открытым исходным кодом для автоматического использования сертификатов Let’s Encrypt.
-   Создан Electronic Frontier Foundation (EFF).
-   Сайт: <https://certbot.eff.org/>


## <span class="section-num">2</span> Получение сертификатов {#получение-сертификатов}


### <span class="section-num">2.1</span> Сертификаты DNS {#сертификаты-dns}


#### <span class="section-num">2.1.1</span> Общая информация {#общая-информация}

-   Для выпуска wildcard-сертификата необходимо выполнить _DNS challenge request_, используя протокол ACMEv2.
-   _DNS challenge_ представляет собой запись TXT, предоставленную клиентом _certbot_, которую необходимо установить вручную в DNS.
-   Нужно будет обновлять DNS при каждом обновлении сертификатов.
    -   Чтобы не делать это вручную, воспользуйтесь _rfc2136_, для которого в Certbot есть плагин `certbot-dns-rfc2136`.
    -   Также необходимо настроить DNS-сервер, чтобы разрешить динамическое обновление TXT-записей.
-   Документация: <https://certbot-dns-rfc2136.readthedocs.io/>


#### <span class="section-num">2.1.2</span> Установка программного обеспечения {#установка-программного-обеспечения}

<!--list-separator-->

1.  Snap

    -   Установка плагина `certbot-dns-rfc2136` для _Snap_:
        ```shell
        snap set certbot trust-plugin-with-root=ok
        sudo snap install certbot-dns-rfc2136
        ```
    -   Сам _Certbot_ может находиться на произвольном сервере.

<!--list-separator-->

2.  Пакетный менеджер

    -   Rocky Linux:
        ```shell
        sudo dnf -y install certbot python3-certbot-dns-rfc2136
        ```


#### <span class="section-num">2.1.3</span> Настройка BIND {#настройка-bind}

-   Сгенерируйте секретный TSIG-ключ:
    ```shell
    tsig-keygen -a HMAC-SHA512 example-key
    ```

    -   Здесь `example-key` --- имя вашего ключа. Выбирается произвольно. Можно назвать по имени домена.
-   Добавьте ключ в файл конфигурации _Bind_ `/etc/named.conf`:
    ```conf-unix
    // /etc/named.conf

    zone "domain.ltd" IN {
            // this is for certbot
            update-policy {
                    grant example-key name _acme-challenge.domain.ltd. txt;
            };
    };

    key "example-key" {
            algorithm hmac-sha512;
            secret "секретный_ключ";
    };
    ```
-   Перезапустите _named_:
    ```shell
    systemctl restart named.service
    ```


#### <span class="section-num">2.1.4</span> Настройка certbot {#настройка-certbot}

-   Сгенерируйте файл конфигурации для плагина _rfc2136_ `/etc/letsencrypt/rfc2136_domain.ltd.ini`:
    ```ini
    # Target DNS server
    dns_rfc2136_server = IP-адрес
    # Target DNS port
    dns_rfc2136_port=53
    # TSIG key name
    dns_rfc2136_name = example-key
    # TSIG key secret
    dns_rfc2136_secret = ключ_без_кавычек
    # TSIG key algorithm
    dns_rfc2136_algorithm = HMAC-SHA512
    ```
-   Поправьте права доступа:
    ```shell
    chmod 600 /etc/letsencrypt/rfc2136_domain.ltd.ini
    ```


#### <span class="section-num">2.1.5</span> Получение сертификата {#получение-сертификата}

-   Выполните команду
    ```shell
    certbot certonly --dns-rfc2136 --force-renewal --dns-rfc2136-credentials /etc/letsencrypt/rfc2136_domain.ltd.ini --server https://acme-v02.api.letsencrypt.org/directory --email admin@domain.ltd --agree-tos --no-eff-email --dns-rfc2136-propagation-seconds 60 -d 'domain.ltd' -d '*.domain.ltd' --non-interactive --quiet
    ```
-   Сертификаты помещаются в каталог `/etc/letsencrypt/live/domain.ltd`.


### <span class="section-num">2.2</span> Сертификаты HTTP {#сертификаты-http}


#### <span class="section-num">2.2.1</span> Сервер _Apache_ {#сервер-apache}

-   Плагин `certbot-apache` предоставляет автоматическую настройку _Apache HTTP Server_.
-   Он пытается найти конфигурацию каждого домена, а также добавляет рекомендованные для безопасности параметры, настройки использования сертификатов и пути к сертификатам Let's Encrypt.
-   Первоначальная настройка виртуальных хостов:
    ```shell
    certbot --apache
    ```
-   Обновление сертификатов:
    ```shell
    certbot renew
    ```
-   Изменение сертификатов без изменения файлов конфигурации _apache_:
    ```shell
    certbot --apache certonly
    ```


#### <span class="section-num">2.2.2</span> Сервер _Nginx_ {#сервер-nginx}

-   Плагин `certbot-nginx` предоставляет автоматическую настройку _Nginx HTTP Server_.
-   Он пытается найти конфигурацию каждого домена, а также добавляет рекомендованные для безопасности параметры, настройки использования сертификатов и пути к сертификатам Let's Encrypt.
-   Первоначальная настройка виртуальных хостов:
    ```shell
    certbot --nginx
    ```
-   Обновление сертификатов:
    ```shell
    certbot renew
    ```
-   Изменение сертификатов без изменения файлов конфигурации _nginx_:
    ```shell
    certbot --nginx certonly
    ```


## <span class="section-num">3</span> Установка {#установка}


### <span class="section-num">3.1</span> Установка _certbot_ {#установка-certbot}

-   Проверьте, что установлен репозитории EPEL:
    ```shell
    dnf -y install epel-release
    ```
-   Установите _certbot_:
    ```shell
    dnf -y install certbot
    ```
-   Для веб-сервера Apache:
    ```shell
    dnf -y install python3-certbot-apache
    ```
-   Для веб-сервера Nginx:
    ```shell
    dnf -y install python3-certbot-nginx
    ```
-   Для сертификата DNS:
    ```shell
    dnf -y install python3-certbot-dns-rfc2136
    ```


### <span class="section-num">3.2</span> Установка реализации _snap certbot_ {#установка-реализации-snap-certbot}

-   Установка _Snap_
    -   Centos
        -   Установите репозиторий _Epel_
            ```shell
            sudo dnf install epel-release
            sudo dnf upgrade
            ```
        -   Установите _Snap_
            ```shell
            sudo dnf -y install snapd
            ```
-   Запустите _Snap_
    ```shell
    sudo systemctl enable --now snapd.socket
    sudo ln -s /var/lib/snapd/snap /snap
    ```
-   Обновите _Snap_ (перед этим необходимо немного подождать, чтобы запустился snapd)
    ```shell
    sudo snap install core
    sudo snap refresh core
    ```
-   Установка _certbot_
    ```shell
    sudo snap install --classic certbot
    ```
-   Сделайте символьную ссылку для запуска:
    ```shell
    sudo ln -s /snap/bin/certbot /usr/local/bin/certbot
    ```
