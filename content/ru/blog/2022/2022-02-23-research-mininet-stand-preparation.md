---
title: "Исследования. Mininet. Подготовка стенда"
author: ["Dmitry S. Kulyabov"]
date: 2022-02-23T18:33:00+03:00
lastmod: 2023-10-31T12:30:00+03:00
tags: ["modeling", "research", "network"]
categories: ["computer-science", "science"]
draft: false
slug: "research-mininet-stand-preparation"
---

-   Для проведения исследования с использованием _Mininet_ следует подготовить исследовательский стенд.
-   Здесь рассматривается проведение воспроизводимых исследований.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий _Mininet_: <https://github.com/mininet/mininet>
-   Виртуальные машины:
    -   версия 2.2.2: <https://github.com/mininet/mininet/releases/tag/2.2.2>
    -   версия 2.3.0: <https://github.com/mininet/mininet/releases/tag/2.3.0>


## <span class="section-num">2</span> Выбор версии {#выбор-версии}

-   Выбор версии зависит от необходимой версии python:
    -   mininet-2.2.2: python2;
    -   mininet-2.3.0: python3.


## <span class="section-num">3</span> Настройка образа {#настройка-образа}


### <span class="section-num">3.1</span> VirtualBox {#virtualbox}

-   Распакуйте скачанный образ.
-   Импортируйте файл `.ovf`.
-   Перейдите в настройки.
-   Добавьте дополнительный сетевой адаптер _host-only network adapter_, который вы можете использовать для входа в образ виртуальной машины.


## <span class="section-num">4</span> Подключение к виртуальной машине {#подключение-к-виртуальной-машине}

-   Залогиньтесь в виртуальной машине:
    -   login: mininet
    -   password: mininet
-   Посмотрите адрес машины:
    ```shell
    ifconfig
    ```
-   Для активации второго интерфейса наберите:
    ```shell
    sudo dhclient eth1
    ifconfig
    ```
-   Внутренний адрес машины будет иметь вид 192.168.x.y.
-   Подключитесь к виртуальной машине:
    ```shell
    ssh -Y mininet@192.168.x.y
    ```
-   Настройте вход по ключу (см. [Ключи ssh]({{< relref "2022-02-17-ssh-keys" >}})):
    ```shell
    ssh-copy-id mininet@192.168.x.y
    ```


## <span class="section-num">5</span> Видео {#видео}

{{< youtube dDDSaO-j564 >}}
