---
title: "LibreNMS. Миграция с Observium"
author: ["Dmitry S. Kulyabov"]
date: 2024-04-26T11:35:00+03:00
lastmod: 2024-04-26T11:37:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "librenms-observium-migration"
---

LibreNMS. Миграция с Observium.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Скрипты миграции {#скрипты-миграции}


### <span class="section-num">1.1</span> Общая информация {#общая-информация}

-   Сценарии миграции доступны в каталоге `/opt/librenms/scripts/Migration`.


### <span class="section-num">1.2</span> Что переносится {#что-переносится}

-   Файлы RRD.
    -   Список хостов.


### <span class="section-num">1.3</span> Типы миграции {#типы-миграции}


#### <span class="section-num">1.3.1</span> Разная архитектура хостов {#разная-архитектура-хостов}

-   RRD файлы преобразуются в XML, а потом обратно в RRD.
-   Скрипты: `/opt/librenms/scripts/Migration/XML_Conversion`.


#### <span class="section-num">1.3.2</span> Одинаковая архитектура хостов {#одинаковая-архитектура-хостов}

-   RRD файлы просто копируются.
-   Скрипты: `/opt/librenms/scripts/Migration/Standard_Conversion`.
-   Скрипты перед использование переименовать:
    ```shell
    mv convert_no_xml.sh convert.sh
    mv destwork_no_xml.sh destwork.sh
    ```
-   Краткий список переменных в скриптах:


### <span class="section-num">1.4</span> Переменные в скриптах {#переменные-в-скриптах}

-   `DEST`: IP-адрес или имя хоста сервера LibreNMS.
-   `L_RRDPATH`: расположение каталога `rrd` LibreNMS. Значение по умолчанию: место установки по умолчанию.
-   `O_RRDPATH`: расположение каталога `rrd` Observium. Значение по умолчанию: место установки по умолчанию.
-   `MKDIR`: расположение скрипта `mkdir.sh`.
-   `DESTSCRIPT`: расположение скрипта `destwork.sh`.
-   `NODELIST`: расположение файла `nodelist.txt`.


### <span class="section-num">1.5</span> Что делают скрипты {#что-делают-скрипты}

-   `convert.sh`: выполняется на Observium. Преобразует файлы RRD в XML и копирует их на LibreNMS, либо просто копирует их на LibreNMS.
-   `destwork.sh`: выполняется на LibreNMS, запускается из `convert.sh`. Преобразует файлы XML в RRD (при необходимости) и добавляет список хостов из `nodelist.txt` в LibreNMS.


### <span class="section-num">1.6</span> Процесс миграциии {#процесс-миграциии}

-   Хосты `observium.example.com` и `librenms.example.com`.
-   Копируем скрипты на `librenms.example.com`:
    ```shell
    root@librenms.example.com# cp destwork.sh mkdir.sh /tmp
    root@librenms.example.com# cd /tmp/
    root@librenms.example.com# chmod +x destwork.sh mkdir.sh
    ```
-   Отредактируйте `SNMPSTRING` в `/tmp/destwork.sh`.
-   Скопируем скрипты с `librenms.example.com` на `observium.example.com`:
    ```shell
    root@librenms.example.com# scp convert.sh mkdir.sh /tmp/destwork.sh observium.example.com:/tmp
    ```
-   Перейдите на `observium.example.com`.
-   Отредактируйте `DEST` в `/etc/convert.sh`.
-   Поменяем права доступа к скрипту:
    ```shell
    root@observium.example.com# chmod +x /tmp/convert.sh /tmp/mkdir.sh /tmp/destwork.sh
    ```
-   Настройте аутентификацию по ключу:
    ```shell
    root@observium.example.com# ssh-copy-id librenms@example.com
    ```
-   Создайте файл `/tmp/nodelist.txt`:
    ```shell
    root@observium.example.com# ls /opt/observium/rrd/ | egrep -v "*.rrd" > /tmp/nodelist.txt
    ```
-   Скопируйте файл `/tmp/nodelist.txt` на `librenms.example.com`:
    ```shell
    root@observium.example.com# scp /tmp/nodelist.txt librenms.example.com:/tmp
    ```
-   Запустите миграцию:
    ```shell
    root@observium.example.com# /tmp/convert.sh
    ```
