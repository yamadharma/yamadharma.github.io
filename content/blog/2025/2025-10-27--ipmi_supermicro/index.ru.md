---
title: "IPMI. Supermicro"
author: ["Dmitry S. Kulyabov"]
date: 2025-10-27T18:42:00+03:00
lastmod: 2025-10-27T19:37:00+03:00
tags: ["sysadmin", "hard"]
categories: ["computer-science"]
draft: false
slug: "ipmi-supermicro"
---

IPMI. Supermicro

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   IPMI (Intelligent Platform Management Interface) --- это стандарт для удалённого мониторинга и управления серверами.
-   Он позволяет системным администраторам контролировать оборудование, даже если операционная система не загружена или сервер выключен.
-   IPMI обеспечивает управление и мониторинг серверных систем с использованием специального интерфейса.
-   IPMI Supermicro --- это реализация стандарта IPMI на серверах компании Supermicro.
-   Она позволяет:
    -   проводить мониторинг физического состояния оборудования (проверять температуру, уровни напряжения, скорость вращения вентиляторов и т. д.);
    -   восстанавливать работоспособность сервера (выполнять удалённую перезагрузку, включать/выключать питание, загружать ISO-образы и обновлять программное обеспечение);
    -   управлять периферийными устройствами;
    -   вести журнал событий;
    -   хранить информацию об используемом оборудовании.


### <span class="section-num">1.1</span> Основные компоненты IPMI на серверах Supermicro {#основные-компоненты-ipmi-на-серверах-supermicro}

-   BMC (Baseboard Management Controller) --- микроконтроллер, который отвечает за удалённое управление сервером. Он работает всегда, вне зависимости от состояния сервера.
-   Возможность подключения дополнительных контроллеров управления (MCs) для расширения функционала.
-   Интерфейс для взаимодействия с сенсорами, хранилищами и другими компонентами сервера.


## <span class="section-num">2</span> Лицензионные ключи {#лицензионные-ключи}

-   Для многих операций с IPMI требуется лицензионный ключ.
-   Можно сгенерить самому.


### <span class="section-num">2.1</span> zsrv/supermicro-product-key {#zsrv-supermicro-product-key}

-   Репозиторий: <https://github.com/zsrv/supermicro-product-key>


#### <span class="section-num">2.1.1</span> Ключ OOB {#ключ-oob}

-   Создаётся на основе mac-адреса BMC:
    ```shell
    supermicro-product-key oob encode <mac-address BMC>
    ```


#### <span class="section-num">2.1.2</span> Ключ SFT-DCMS-SINGLE {#ключ-sft-dcms-single}

-   Создаётся на основе mac-адреса BMC:
    ```shell
    upermicro-product-key nonjson encode --sku SFT-DCMS-SINGLE <mac-address BMC>
    ```
-   Используется с утилитой Supermicro Update Manager (SUM).
-   <https://www.supermicro.com/en/support/resources/downloadcenter/smsdownload>


### <span class="section-num">2.2</span> Прямое создание {#прямое-создание}

-   <https://peterkleissner.com/2018/05/27/reverse-engineering-supermicro-ipmi/>
-   Ключ создаётся как HMAC SHA1 от mac-адреса.
-   Можно сделать командой:
    ```shell
    #!/bin/bash
    read -p "IPMI MAC: " macaddr
    echo -n $macaddr | xxd -r -p | openssl dgst -sha1 -mac HMAC -macopt hexkey:8544E3B47ECA58F9583043F8 | awk '{print $2}' | cut -c 1-24 | sed 's/./&-/4;s/./&-/9;s/./&-/14;s/./&-/19;s/./&-/24;'
    ```
