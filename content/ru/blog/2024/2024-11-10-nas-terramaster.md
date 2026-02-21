---
title: "NAS. TerraMaster"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-10T18:35:00+03:00
lastmod: 2025-08-18T15:59:00+03:00
tags: ["sysadmin", "hard"]
categories: ["computer-science"]
draft: false
slug: "nas-terramaster"
---

NAS. TerraMaster.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.terra-master.com/ru/>
-   AliExpress. TERRAMASTER Store (official): <https://aliexpress.ru/store/910372071>
-   Сопутствующие программы: <https://support.terra-master.com/download>
-   Список совместимости компонентов: <https://www.terra-master.com/ru/compatibility/>
-   Программные пакеты сообщества: <https://tmnascommunity.eu/>
-   4pda: <https://4pda.to/forum/index.php?showtopic=1025592>


## <span class="section-num">2</span> Модели {#модели}


### <span class="section-num">2.1</span> TERRAMASTER F6-424 {#terramaster-f6-424}

-   AliExpress: <https://aliexpress.ru/item/1005007676504890.html>
-   Описание: <https://www.terra-master.com/ru/f6-424.html>
-   Спецификация: <https://www.terra-master.com/ru/f6-424.html?page=menu&mid=1588>
-   Обзоры:
    -   <https://bafista.ru/terramaster-f4-424-max/>
    -   <https://bafista.ru/obzor-i-testirovanie-terramaster-f4-424/>
-   Processor Model: N95 Quad Core CPU
-   System Memory: 8GB DDR5 RAM
-   Корзин для дисков: 6 шт.
-   Диски: 2.5", 3.5".
-   Безвинтовая установка дисков 3.5".
-   Видео-интерфейс: HDMI.
-   54100,00 ₽


## <span class="section-num">3</span> Особые функции {#особые-функции}


### <span class="section-num">3.1</span> TRAID {#traid}

-   Краткое описание: <https://www.terra-master.com/ru/terramaster-traid>
-   Калькулятор дисков: <https://support.terra-master.com/raidcalculation/>


#### <span class="section-num">3.1.1</span> TRAID {#traid}

-   1 диск: JBOD
-   2 диска: RAID1
-   3 и более дисков: RAID5


#### <span class="section-num">3.1.2</span> TRAID+ {#traid-plus}

-   4 и более дисков: RAID6


#### <span class="section-num">3.1.3</span> Переход с TRAID на TRAID+ {#переход-с-traid-на-traid-plus}

-   Переход на TRAID+ возможен, если в массиве уже есть три жестких диска или более.
-   В массив необходимо добавить жесткие диски.
-   Не выключайте TNAS.
-   Вставьте один или несколько новых жёстких дисков.
-   Перейдите в меню «Панель управления &gt; Управление хранилищем &gt; Пул носителей &gt; Изменить»
-   Выберите «Перейти».


### <span class="section-num">3.2</span> Файловая система HyperLock WORM {#файловая-система-hyperlock-worm}

-   Информация: <https://www.terra-master.com/ru/hyperlock-worm/>
-   Файловая система однократной записи.


### <span class="section-num">3.3</span> Hyper Cache {#hyper-cache}

-   Решение по кешированию на основе SSD-дисков.
-   Описание: <https://www.terra-master.com/ru/hyper-cache/>


#### <span class="section-num">3.3.1</span> Рекомендации по настройке Hyper Cache {#рекомендации-по-настройке-hyper-cache}

-   SSD-кэш при работе использует оперативную память.
-   Система не позволит сделать кэш большого объёма при недостатке оперативной памяти.

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Максимальный размер SSD-кэша в зависимости от объёма оперативной памяти
</div>

| RAM, ГБ | Размер SSD-кэша, ГБ |
|---------|---------------------|
| 1 ГБ    | 50                  |
| 2 ГБ    | 160                 |
| 4 ГБ    | 320                 |
| 6 ГБ    | 500                 |
| 8 ГБ    | 800                 |
| 10 ГБ   | 1000                |
| 12 ГБ   | 1280                |
| 16 ГБ   | 1600                |
| 32 ГБ   | 3200                |


### <span class="section-num">3.4</span> TFSS {#tfss}

-   Страница: <https://www.terra-master.com/ru/tfss>
-   Создание снепшотов btrfs.


## <span class="section-num">4</span> Особенности настройки {#особенности-настройки}


### <span class="section-num">4.1</span> sshd {#sshd}

-   По умолчанию предлагается порт 9222.
-   Включается в Терминал и SNMP &gt; Telnet/SSH.


### <span class="section-num">4.2</span> sftpd {#sftpd}

-   По умолчанию предлагается порт 9333.
-   Включается в Файловая служба &gt; FTP.


## <span class="section-num">5</span> Программное обеспечение {#программное-обеспечение}


### <span class="section-num">5.1</span> qBittorrent {#qbittorrent}

-   В стандартном репозитории.
-   Более новые версии в репозитории сообщества: <https://tmnascommunity.eu/download/qbittorrent/>.
-   Учётные данные при запуске:
    -   username: admin
    -   password: adminadmin


### <span class="section-num">5.2</span> Plex Media Server {#plex-media-server}

-   [Plex Media Server]({{< relref "2025-01-27--plex-media-server" >}})
-   В стандартном репозитории.


## <span class="section-num">6</span> Entware {#entware}

-   [Репозиторий программного обеспечения Entware]({{< relref "2024-12-20--entware-software-repository" >}})


### <span class="section-num">6.1</span> Установка {#установка}

-   Подключиться по ssh.
-   Создать каталог для установки:
    ```shell
    mkdir -p /Volume1/@entware/opt
    ```
-   Подключить каталог `/opt`:
    ```shell
    ln -s /Volume1/@entware/opt /opt
    ```
-   Скачать и запустить установщик:
    ```shell
    wget -O - http://bin.entware.net/x64-k3.2/installer/generic.sh | /bin/sh
    ```
-   Сделать ссылку на менеджер пакетов:
    ```shell
    ln -s /opt/bin/opkg /usr/bin/opkg
    ```
-   Отредактировать `/root/.bashrc`, добавив к `PATH` `/opt/bin:/opt/sbin`:
    ```shell
    export PATH=$PATH:/opt/bin:/opt/sbin
    ```
-   Перечитайте `/etc/profile`:
    ```shell
    source /etc/profile
    ```
-   Обновите список пакетов:
    ```shell
    opkg update
    ```
-   Обновите пакеты:
    ```shell
    opkg upgrade
    ```


### <span class="section-num">6.2</span> Программное обеспечение {#программное-обеспечение}


#### <span class="section-num">6.2.1</span> git {#git}

-   Для работы с git:
    ```shell
    opkg install git git-http
    ```


#### <span class="section-num">6.2.2</span> Syncthing {#syncthing}

-   Установить:
    ```shell
    opkg install syncthing
    ```
-   Запустить:
    ```shell
    /opt/etc/init.d/S92syncthing start
    ```
-   Сконфигурируйте через броузер:
    ```shell
    http://<your device ip>:8384/
    ```


## <span class="section-num">7</span> Файловая система {#файловая-система}


### <span class="section-num">7.1</span> data {#data}

-   Всё хранится в `/Volume1/data`.


#### <span class="section-num">7.1.1</span> Видеофайлы для plex {#видеофайлы-для-plex}

-   Создайте необходимые каталоги:
    ```shell
    mkdir -p /Volume1/data/{torent,video,movie,tvshow}
    ```
-   Задайте права:
    ```shell
    setfacl -m u:plex:rwx /Volume1/data
    setfacl -d -m u:plex:rwx /Volume1/data
    setfacl -R -m u:plex:rwx /Volume1/data/{torent,video,movie,tvshow}
    setfacl -R -d -m u:plex:rwx /Volume1/data/{torent,video,movie,tvshow}
    ```


#### <span class="section-num">7.1.2</span> Торренты (qBittorrent) {#торренты--qbittorrent}

-   Создайте необходимые каталоги:
    ```shell
    mkdir -p /Volume1/data/torent/torrent
    ```
-   Задайте права:
    ```shell
    setfacl -m u:qbittorrent:rwx /Volume1/data
    setfacl -d -m u:qbittorrent:rwx /Volume1/data
    setfacl -R -m u:qbittorrent:rwx /Volume1/data/torent
    setfacl -R -d -m u:qbittorrent:rwx /Volume1/data/torent
    ```


## <span class="section-num">8</span> Администрирование {#администрирование}


### <span class="section-num">8.1</span> btrfs {#btrfs}

-   Обновите утилиты:
    ```shell
    opkg install btrfs-progs
    ```


## <span class="section-num">9</span> Стандартные операции {#стандартные-операции}


### <span class="section-num">9.1</span> Увеличение количества жёстких дисков {#увеличение-количества-жёстких-дисков}

-   Информация: <https://www.terra-master.com/ru/terramaster-traid>
-   Не выключая TNAS, вставьте новый жесткий диск.
-   Перейдите в меню «Панель управления &gt; Диспетчер хранилища &gt; Пул носителей &gt; Редактировать».
-   Выберите _Добавить жёсткие диски в RAID_.


### <span class="section-num">9.2</span> Замена жёсткого диска {#замена-жёсткого-диска}

-   Информация: <https://www.terra-master.com/ru/terramaster-traid>
-   Ёмкость вновь добавленного диска должна быть как минимум такой же, как и диск наименьшей емкости в TRAID.
-   Не выключая TNAS, извлеките один из дисков, а затем вставьте диск большей емкости.
-   Перейдите в меню «Панель управления &gt; Диспетчер хранилища &gt; Пул носителей &gt; Редактировать».
-   Выберите «Восстановить».


### <span class="section-num">9.3</span> Миграция пула носителей {#миграция-пула-носителей}

-   Информация: <https://www.terra-master.com/ru/storage-pool-migration>


## <span class="section-num">10</span> Ресурсы {#ресурсы}

-   Сайт по сравнению NAS: <https://nascompares.com/tag/terramaster-nas/>


## <span class="section-num">11</span> Опыт использования {#опыт-использования}


### <span class="section-num">11.1</span> TerraMaster F6-424 {#terramaster-f6-424}


#### <span class="section-num">11.1.1</span> Установленное программное обеспечение {#установленное-программное-обеспечение}

<!--list-separator-->

1.  Plex Media Server

    -   В стандартном репозитории.

    <!--list-separator-->

    1.  Права на файловую систему

        -   Установим права на файловую систему:
            ```shell
            setfacl -m u:plex:r-x /Volume1/data
            setfacl -d -m u:plex:r-x /Volume1/data
            setfacl -R -m u:plex:rwx /Volume1/data/{tvshow,movie,music}
            setfacl -R -d -m u:plex:rwx /Volume1/data/{tvshow,movie,music}
            ```

<!--list-separator-->

2.  qBittorrent

    -   В стандартном репозитории.
    -   Более новые версии в репозитории сообщества: <https://tmnascommunity.eu/download/qbittorrent/>.
    -   Учётные данные при запуске:
        -   username: admin
        -   password: adminadmin

<!--list-separator-->

3.  Deduplication Manager

    -   В стандартном репозитории.


#### <span class="section-num">11.1.2</span> <span class="timestamp-wrapper"><span class="timestamp">[2024-12-01 Вс] </span></span> Первичное подключение {#первичное-подключение}

-   В консоли не смог залогиниться.
-   Посмотрел ip-адрес (на сервере DHCP, но можно было и в консоли).
-   В web-интерфейсе было только сообщение, что нет дисков. Никаких кнопочек не было.
-   Поставил диск (маленький, на 4 TB).
-   В web-интерфейсе была запрошена инициализация.
-   Включился счётчик на 60 секунд.
-   Появилось предупреждение, что через 60 секунд будут применены настройки по умолчанию.
-   Для своих настроек следовало нажать интерфейсную кнопку `Esc`.
-   Попросил загрузить загрузчик.
-   Попросил выбрать жёсткий диск.
-   Попросил загрузить пакет TOS (операционная система).
-   Проведена была инициализация диска.
-   Было сообщено о перезагрузке (включился счётчик на 5 минут).
-   Принял лицензионное соглашение.
-   Система запросила имя хоста и имя и пароль администратора.
-   Имя `admin` не было принято, поскольку оно зарезервировано.
-   Разные вариации на тему `admin` были отброшены, как небезопасные.
-   Был запрошен почтовый адрес для отправки вспомогательного кода.
-   Но почту система отправить не смогла.
-   Пропустил это шаг.
-   Попал в интерфейс администрирования системы.
-   Было сообщено, что пул не инициализирован.
-   Было предложено настроить пул.
-   Создал на одном диске TRAID.
-   Было запрошено создание тома и файловой системы.
-   От файловой системы _HyperLock WORM_ отказался (не стал включать поддержку).
-   Установил BTRFS (см. [Файловая система btrfs]({{< relref "2021-08-27-btrfs-file-system" >}})).


#### <span class="section-num">11.1.3</span> <span class="timestamp-wrapper"><span class="timestamp">[2024-12-12 Чт] </span></span> Добавление диска {#добавление-диска}

-   Купил 2 жёстких диска.
-   Жесткий диск 18TB SATA 6Gb/s Seagate ST18000NM000J
-   На диске было 2.6GB (фактически, только система).
-   Поскольку на исходном диске ничего, кроме системы, и не было, то можно было бы заменить диски и переинициализировать систему.
-   Но решил попробовать, как будет выполняться штатная замена дисков.
-   Поставил один диск.
-   Добавил его в web-интерфейсе.
-   Запустилась перестройка диска.
-   Сообщило, что на это потребуется больше 5 часов.
-   Размер хранилища остался 3.63TB.


#### <span class="section-num">11.1.4</span> <span class="timestamp-wrapper"><span class="timestamp">[2024-12-13 Пт] </span></span> Замена диска {#замена-диска}

-   Перешёл в меню _Панель управления &gt; Жёсткий диск &gt; Жёсткий диск_.
-   Выбрал диск на 4TB.
-   Диск был помечен как системный.
-   Выбрал операцию _Удалить_.
-   Появилось сообщение, что диск удалять нельзя, поскольку нет дублирования.
-   Извлёк диск.
-   Поставил новый.
-   Перешёл в меню _Панель управления &gt; Диспетчер хранилища &gt; Пул носителей_.
-   Выбрал операцию _Редактировать_.
-   Выбрал пункт _Восстановить RAID_.
-   В интерфейсе пропали все диски.
-   В консоли подключиться стало невозможно.
-   Перегрузил NAS.
-   Система предложила восстановить загрузчик.
-   После перегрузки включилась пищалка.
-   Интерфейсе попросили ввести имя хоста, пользователя, пароль.
-   После этого сообщили о деградированном RAID.
-   Я выбрал опцию в настройках _Быстрое восстановление RAID_.
-   Запустил перестройку RAID.


#### <span class="section-num">11.1.5</span> <span class="timestamp-wrapper"><span class="timestamp">[2024-12-14 Сб] </span></span> Расширение тома {#расширение-тома}

-   Синхронизация RAID закончилась.
-   Перешёл в меню _Панель управления &gt; Том &gt; Том 1_.
-   Выбрал кнопку _Подробнее_.
-   Выбрал подменю _Сжатие файловой системы_.
-   Включил сжатие файловой системы.
-   Выбрал кнопку _Редактировать_.
-   Увеличил файловую систему до максимума.
-   Получилось 16.36TB.
