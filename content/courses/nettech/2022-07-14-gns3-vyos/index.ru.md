---
title: "GNS3. Образ VyOS"
author: ["Dmitry S. Kulyabov"]
date: 2022-07-14T12:56:00+03:00
lastmod: 2023-07-16T19:16:00+03:00
tags: ["network"]
categories: ["computer-science"]
draft: false
weight: 202
toc: true
type: docs
slug: "gns3-vyos"
summary: "Образ VyOS для GNS3"
menu:
  "gns3-vyos":
    parent: "nettech-gns3-lab"
    weight: 202
    identifier: "gns3-vyos"
---

Установка образа VyOS в GNS3.

<!--more-->


## <span class="section-num">1</span> Цели {#цели}

-   Установить образ VyOS.
-   Сделать первоначальную настройку.
-   Заменить системного пользователя.


## <span class="section-num">2</span> Общая информация {#общая-информация}

-   [Маршрутизация. VyOS]({{< relref "2022-06-03-routing-vyos" >}})
-   [Сборка образа VyOS]({{< relref "2023-07-06-vyos-build" >}})
-   [Сборка образа VyOS. Репозиторий]({{< relref "2023-07-16-vyos-build-repository" >}})
-   Сайты:
    -   Сайт: <https://vyos.net/>.
    -   Снепшоты: <https://vyos.net/get/nightly-builds/>.
    -   Документация: <https://docs.vyos.io/>.
    -   Документация по установке на GNS3: <https://docs.vyos.io/en/equuleus/installation/virtual/gns3.html>
-   Форк проекта _Vyatta_.
-   Реализовано на основе дистрибутива Debian.
-   Система команд похожа на Juniper.


### <span class="section-num">2.1</span> Модель распространения {#модель-распространения}

-   Можно собрать самому из исходного кода.
-   Образы LTS можно скачивать за плату.
    -   Для учебных заведений и некоммерческих организаций предоставляется бесплатный доступ к релизам.
-   Образы для rolling релизов можно скачивать бесплатно.
-   Rolling релизы:
    -   <https://vyos.net/get/?dir=rolling/current/amd64>;
    -   <https://community.vyos.net/get/>.
-   Блокируются российский ip-адреса.


## <span class="section-num">3</span> Настройка образа {#настройка-образа}


### <span class="section-num">3.1</span> Установка образа {#установка-образа}

-   После загрузки установите систему на диск:
    ```shell
    vyos@vyos:~$ install image
    ```


### <span class="section-num">3.2</span> Режим конфигурации {#режим-конфигурации}

-   В рабочем режиме в командной строке отображается символ `$`.
-   В режиме конфигурации в командной строке отображается `#`:
    ```shell
    vyos@vyos$ configure
    vyos@vyos#
    ```


### <span class="section-num">3.3</span> Сохранение {#сохранение}

-   Посмотреть, какие изменения внесены:
    ```shell
    vyos@vyos# compare
    ```
-   После каждого изменения конфигурации необходимо применить изменения:
    ```shell
    vyos@vyos# commit
    ```
-   В конце нужно сохранить конфигурацию:
    ```shell
    vyos@vyos# save
    ```


### <span class="section-num">3.4</span> Имя устройства {#имя-устройства}

-   Имя хоста может содержать до 63 символов. Имя хоста должно начинаться и заканчиваться буквой или цифрой и содержать в качестве внутренних символов только буквы, цифры или дефис:
    ```shell
    set system host-name <hostname>
    ```
-   По умолчанию используется имя хоста _vyos_.
-   Доменное имя должно начинаться и заканчиваться буквой или цифрой и содержать в качестве внутренних символов только буквы, цифры или дефис:
    ```shell
    set system domain-name <domain>
    ```


### <span class="section-num">3.5</span> Конфигурация интерфейсов {#конфигурация-интерфейсов}

-   Интерфейс `eth0`. Использует статический IP-адрес `192.168.0.1/24`.
-   После перехода в режим конфигурации введём следующие команды:
    ```shell
    set interfaces ethernet eth0 address '192.168.0.1/24'
    ```


### <span class="section-num">3.6</span> Замена системного пользователя {#замена-системного-пользователя}

-   Заменим системного пользователя по умолчанию:
    ```shell
    set system login user <myvyosuser> authentication plaintext-password <mysecurepassword>

    commit
    save
    ```
-   Отлогинимся:
    ```shell
    # exit
    $ exit
    ```
-   Залогинимся под новым пользователем.
-   Удалим исходного пользователя `vyos`:
    ```shell
    delete system login user vyos
    ```
-   Зафиксируем изменения, сохраним конфигурацию и выйдем из режима конфигурации:
    ```shell
    # commit
    # save

    # exit
    $
    ```


## <span class="section-num">4</span> Видео: Установка образа VyOS в GNS3 {#видео-установка-образа-vyos-в-gns3}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube e2f3acf0d9b794446eb60983f10b3b1b >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube ovSxPP4XYT0 >}}

{{< /rtab >}}
{{< /tabs >}}


## <span class="section-num">5</span> Видео: Установка образа VyOS в GNS3 на Hyper-V {#видео-установка-образа-vyos-в-gns3-на-hyper-v}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube bafa69237a51444f0d54b2c8af811900 >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube OAckxG6LYtc >}}

{{< /rtab >}}
{{< /tabs >}}
