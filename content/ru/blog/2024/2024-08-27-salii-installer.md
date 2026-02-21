---
title: "Система установки SALII"
author: ["Dmitry S. Kulyabov"]
date: 2024-08-27T19:25:00+03:00
lastmod: 2025-05-05T11:17:00+03:00
draft: false
slug: "salii-installer"
---

Система установки SALII.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/yamadharma/salii>
-   Форк проекта SALI (см. [Система установки SALI]({{< relref "2024-08-27-sali-automatic-linux-installer" >}}))
-   Вызвано необходимостью настройки и установки не только Linux, но и Windows.
-   Название:

    > Салии (лат. Salii ← salio «прыгаю, пляшу») — в Древнем Риме жреческая коллегия, состоявшая из 12 жрецов бога Марса и 12 жрецов бога Квирина.
    >
    > Своё название салии получили от военной пляски, совершавшейся ими во время ежегодных празднеств в честь Марса. Также существовала версия о происхождении названия от имени Салия, который якобы научил этой пляске. Салии охраняли двенадцать щитов --- анкилов, среди которых один, по легенде, упал с неба, а остальные одиннадцать были точными его копиями. Были также палатинские салии.


## <span class="section-num">2</span> Установка сервера {#установка-сервера}


### <span class="section-num">2.1</span> Дополнительное программное обеспечение {#дополнительное-программное-обеспечение}

-   Установите opentracker.
-   [bittorrent. Трекер opentracker]({{< relref "2024-01-31-bittorrent-opentracker" >}})


### <span class="section-num">2.2</span> Предварительное программное обеспечение {#предварительное-программное-обеспечение}

-   Необходимо
    -   netifaces
    -   paramiko
    -   transmission_rpc
-   Установка:
    ```shell
    dnf install python3-netifaces python3-paramiko python3-pip
    pip install "transmission-rpc<4.0.0"
    dnf install transmission-daemon transmission-cli rsync rsync-daemon
    ```


### <span class="section-num">2.3</span> SELinux {#selinux}

-   Настроим SELinux:
    ```shell
    setsebool rsync_export_all_ro 1
    setsebool rsync_export_all_ro 1 -P
    ```


## <span class="section-num">3</span> Создание загрузочного образа клиента {#создание-загрузочного-образа-клиента}


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   Для загрузочного образа используется buildroot.
-   Сайт buildroot: <https://buildroot.org/>


### <span class="section-num">3.2</span> Создание загрузочного образа {#создание-загрузочного-образа}

-   После сборки образы будут доступны в директории `output/images` в каталоге `buildroot`.


#### <span class="section-num">3.2.1</span> С помощью Makefile {#с-помощью-makefile}

-   Запустите make:
    ```shell
    make
    ```


#### <span class="section-num">3.2.2</span> Вручную {#вручную}

-   Скачайте buildroot и распакуйте его отдельно от этого репозитория, например в `/tmp`:
    ```shell
    cd /tmp && wget https://buildroot.org/downloads/buildroot-2021.02.1.tar.gz
    ```
-   Распакуйте buildroot:
    ```shell
    tar xvf buildroot-2022.11.1.tar.gz
    ```
-   Смените директорию:
    ```shell
    cd buildroot-2022.11.1
    ```
-   Настройте buildroot с помощью `sali_x86_64_defconfig` через метод `BR2_EXTERNAL`:
    ```shell
    make BR2_EXTERNAL=/<salii_dir>/sali/buildroot sali_x86_64_defconfig
    ```
-   Выполните команду:
    ```shell
    make xxhash
    ```
-   Запустите:
    ```shell
    make zstd
    ```
-   Выполните:
    ```shell
    make
    ```


### <span class="section-num">3.3</span> Обновление конфигурации {#обновление-конфигурации}

-   Для разработки или добавления дополнительных свойств.


#### <span class="section-num">3.3.1</span> Обновление конфигурации buildroot {#обновление-конфигурации-buildroot}

-   Выполните:
    ```shell
    make menuconfig
    ```
-   После изменения опций выполните команду:
    ```shell
    make savedefconfig
    ```

-   Может появиться ошибка:

    > Makefile.legacy:9: **\*** "You have legacy configuration in your .config! Please check your configuration.".  Stop.
-   Запустите `make menuconfig`, выберите `Legacy config options`, отключите опцию устаревшей конфигурации.


#### <span class="section-num">3.3.2</span> Обновление конфигурации Linux {#обновление-конфигурации-linux}

-   Выполните:
    ```shell
    make linux-menuconfig
    ```
-   После изменения опций выполните команду:
    ```shell
    make linux-update-defconfig
    ```


#### <span class="section-num">3.3.3</span> Обновление конфигурации Busybox {#обновление-конфигурации-busybox}

-   Выполните:
    ```shell
    make busybox-menuconfig
    ```
-   После изменения опций выполните команду:
    ```shell
    make busybox-update-config
    ```
