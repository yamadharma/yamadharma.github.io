---
title: "Система мониторинга Observium"
author: ["Dmitry S. Kulyabov"]
date: 2023-03-02T15:46:00+03:00
lastmod: 2023-09-30T19:45:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "observium-monitoring-system"
---

Система мониторинга Observium.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.observium.org/>.
-   Хорош тем, что практически не требует настройки. Работает из коробки.
-   Observium доступен в двух версиях:
    -   бесплатная _Community_  (выпускается раз в 6 месяцев);
    -   платная _Professional_;
    -   платная _Enterprise_.
-   Observium Community годится только для сервисов не критичных к времени реакции, так как устройства по SNMP опрашиваются раз в 5 минут.
-   В платной версии предусмотрен модуль Alarms.
-   Опрос устройств осуществляется по протоколу SNMP.
-   Наилучшим образом подходит для мониторинга коммутационного оборудования.


## <span class="section-num">2</span> Подключение устройств {#подключение-устройств}

-   Для добавления маршрутизатора Cisco достаточно задать SNMP community:
    ```shell
    snmp-server community public RO
    ```
-   Добавление устройств в Observium осуществляется либо через меню веб интерфейса (Devices-&gt;Add device), либо из командной строки сервера (из каталога _Observium_):
    ```shell
    ./add_device.php hostname
    ```


## <span class="section-num">3</span> Принципы работы {#принципы-работы}

-   Сбор статистики поделен на 2 основных процесса:
    -   `discovery`: выполняется основное обнаружение поддерживаемых на данном устройстве датчиков;
    -   `poller`: опрос устройств каждые 5 минут.
-   В версии для подписчиков есть ещё 2 дополнительных процесса, работающих совместно с процессом `poller`:
    -   `bill`: подсчёт биллинговой информации на отдельных портах для пользователей;
    -   `alert`: генерация уведомлений по собираемым системой параметрам.


## <span class="section-num">4</span> Установка Observium {#установка-observium}

-   Создаем директории, в которых будут располагаться файлы _Observium_:
    ```shell
    sudo mkdir -p /opt/observium
    ```
-   Скачаем версию _Community Edition_:
    ```shell
    cd /opt
    wget http://www.observium.org/observium-community-latest.tar.gz
    tar zxvf observium-community-latest.tar.gz
    ```
-   Переходим в папку с конфигурационными файлами и создаем конфигурационный файл, скопировав файл по умолчанию:
    ```shell
    cd /optobservium
    sudo cp config.php.default config.php
    ```
-   Открываем файл `config.php` и редактируем настройки MySQL: `username`, `password`, `dbname`.
-   Подключаемся к MySQL:
    ```shell
    mysql -u root -p
    ```
-   Создаём базу данных с именем `observium`:
    ```shell
    CREATE DATABASE observium DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    ```
-   Даём полные привилегии пользователю `observium` на одноименную базу данных:
    ```shell
    GRANT ALL PRIVILEGES ON observium.* TO 'observium'@'localhost'IDENTIFIED BY 'PASSWORD';
    ```
-   Выполняем скрипт конфигурации ранее созданной базы данных MySQL:
    ```shell
    /opt/observium/discovery.php -u
    ```
-   Создаем дополнительные служебные каталоги:
    ```shell
    mkdir /opt/observium/logs
    mkdir /opt/observium/rrd
    ```
-   Создайте файл `/etc/httpd/conf.d/observium.conf`:
    ```html
    <VirtualHost *>
       DocumentRoot /opt/observium/html/
       ServerName  observium.domain.com
       CustomLog /opt/observium/logs/access_log combined
       ErrorLog /opt/observium/logs/error_log
       <Directory "/opt/observium/html/">
         AllowOverride All
         Options FollowSymLinks MultiViews
         Require all granted
       </Directory>
    </VirtualHost>
    ```
-   Создайте файл `/etc/cron.d/observium`:
    ```conf-unix
    # Run a complete discovery of all devices once every 6 hours
    33  */6   * * *   root    /opt/observium/discovery.php -h all >> /dev/null 2>&1
    # Run automated discovery of newly added devices every 5 minutes
    */5 *     * * *   root    /opt/observium/discovery.php -h new >> /dev/null 2>&1
    # Run multithreaded poller wrapper every 5 minutes
    */5 *     * * *   root    /opt/observium/poller-wrapper.py >> /dev/null 2>&1
    # Run housekeeping script daily for syslog, eventlog and alert log
    13 5 * * * root /opt/observium/housekeeping.php -ysel
    # Run housekeeping script daily for rrds, ports, orphaned entries in the database and performance data
    47 4 * * * root /opt/observium/housekeeping.php -yrptb
    ```
-   Чтобы форсировать мониторинг устройств, нужно выполнить команды:
    ```shell
    /opt/observium/discovery.php -h all
    /opt/observium/poller.php -h all
    ```


## <span class="section-num">5</span> Обновление Observium {#обновление-observium}

-   Переименуйте старую установку и скачайте и распакуйте новую (всё под пользователем `root`):
    ```shell
    cd /opt
    mv observium observium_old
    wget https://www.observium.org/observium-community-latest.tar.gz
    tar zxvf observium-community-latest.tar.gz
    mv /opt/observium_old/rrd observium/
    mv /opt/observium_old/logs observium/
    mv /opt/observium_old/config.php observium/
    ```
-   Исправьте права доступа:
    ```shell
    chown -R apache:apache /opt/observium
    ```
-   Обновите схему БД:
    ```shell
    /opt/observium/discovery.php -u
    ```
-   Можно принудительно выполнить немедленное повторное обнаружение всех устройств:
    ```shell
    /opt/observium/discovery.php -h all
    ```
-   Можно удалить каталог `observium_old`:
    ```shell
    rm -rf observium_old
    ```
