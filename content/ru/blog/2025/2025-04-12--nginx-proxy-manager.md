---
title: "Обратный прокси-сервер Nginx Proxy Manager"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-12T13:16:00+03:00
lastmod: 2025-04-12T15:47:00+03:00
tags: ["network"]
categories: ["computer-science"]
draft: false
slug: "nginx-proxy-manager"
---

Обратный прокси-сервер Nginx Proxy Manager.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://nginxproxymanager.com/>
-   Репозиторий: <https://github.com/NginxProxyManager/nginx-proxy-manager>
-   Выполнен как контейнер Docker.
-   Nginx Proxy Manager --- это обратный прокси-сервер (reverse proxy).
-   Настройка выполняется в графическом интерфейсе.
-   Сервис используется для организации доступа к различным веб-приложениям через единую точку входа (в качестве единой точки входа может выступать, например, доменное имя или IP-адрес) с дальнейшей маршрутизацией до конечного приложения.


## <span class="section-num">2</span> Установка для Proxmox {#установка-для-proxmox}

-   Скрипты: <https://community-scripts.github.io/ProxmoxVE/scripts?id=nginxproxymanager>


### <span class="section-num">2.1</span> Установка {#установка}

-   Выполните команду ниже в оболочке Proxmox VE:
    ```shell
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/nginxproxymanager.sh)"
    ```


### <span class="section-num">2.2</span> Учетные данные для входа по умолчанию {#учетные-данные-для-входа-по-умолчанию}

-   Web-интерфейс находится по адресу:
    ```shell
    http://server.ip:81
    ```
-   Начальные учётные данные:
    -   Имя пользователя : admin@example.com
    -   Пароль : changeme
-   Следует изменить после первого подключения.


### <span class="section-num">2.3</span> Настройка certbot {#настройка-certbot}

-   Необходимо установить тот вариант Certbot, который вам нужен.
-   В консоли контейнера запустите:
    ```shell
    /app/scripts/install-certbot-plugins
    ```
-   Будут установлены дополнительные плагины certbot.


## <span class="section-num">3</span> Настройка Nginx Proxy Manager {#настройка-nginx-proxy-manager}

-   После входа в панель управления вы можете перейти к настройке Nginx Proxy Manager.
-   Для добавления новых proxy переходим в раздел _Hosts_ и нажимаем _Add Proxy Host_.
-   В поле _Domain Names_ добавляем доменное имя.
-   В _Scheme_ выбираем протокол по которому будет происходить перенаправление.
-   В _Forward Hostname_ / IP вводим IP адрес или доменное имя на которое будет происходить перенаправление и указываем порт, если он отличный от 80.
-   Дополнительные перенаправления можно сделать на вкладке _Custom locations_
-   Для дополнительной защиты вы можете активировать опцию _Block Common Exploits_.
-   При создании хоста есть возможность выпустить SSL сертификат Let’s Encrypt.
-   Для этого перейдите во вкладку _SSL_.
-   В поле _SSL Certificate_ можно выбрать создание нового сертификата либо использовать ранее созданный сертификат.
