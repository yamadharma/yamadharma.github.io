---
title: "Web-сервер Nginx"
author: ["Dmitry S. Kulyabov"]
date: 2024-12-05T13:36:00+03:00
lastmod: 2024-12-05T14:28:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "web-server-nginx"
---

Web-сервер Nginx.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


## <span class="section-num">2</span> Установка {#установка}

-   Выберем версию сервера:
    ```shell
    dnf module list nginx
    dnf module reset nginx
    dnf module enable nginx:1.24
    dnf module install nginx:1.24
    ```


## <span class="section-num">3</span> Брандмауэр {#брандмауэр}

-   Откроем порты:
    ```shell
    sudo firewall-cmd --permanent --add-service=http
    sudo firewall-cmd --permanent --add-service=https
    sudo firewall-cmd --reload
    ```


## <span class="section-num">4</span> SELinux {#selinux}

-   Разрешить сетевые подключения:
    ```shell
    setsebool -P httpd_can_network_connect 1
    ```
-   Разрешить перенаправление:
    ```shell
    setsebool -P httpd_can_network_relay 1
    ```


## <span class="section-num">5</span> Файлы и каталоги Nginx {#файлы-и-каталоги-nginx}

-   Контент:
    -   `/usr/share/nginx/html`: веб-контент по умолчанию.
-   Конфигурация сервера:
    -   `/etc/nginx`: каталог конфигурации Nginx;
    -   `/etc/nginx/nginx.conf`: основной файл конфигурации Nginx;
    -   `/etc/nginx/conf.d/`: файлы конфигурации блока `server`;
        -   рекомендуется хранить каждый веб-сайт в отдельном файле;
        -   рекомендуется файлы называть доменным именем веб-сайта, например `hostname.domainname.conf`.
-   Журналы:
    -   `/var/log/nginx/access.log`: запросы к веб-серверу;
    -   `/var/log/nginx/error.log`: ошибки Nginx.
