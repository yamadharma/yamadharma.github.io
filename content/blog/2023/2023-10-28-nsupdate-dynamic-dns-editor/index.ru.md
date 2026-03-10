---
title: "nsupdate: динамический редактор зон DNS"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-28T19:28:00+03:00
lastmod: 2024-01-31T13:42:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "nsupdate-dynamic-dns-editor"
---

nsupdate: динамический редактор зон DNS.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   nsupdate используется для внесения изменений в динамический DNS без необходимости редактирования файлов зоны и перезапуска DNS-сервера.


## <span class="section-num">2</span> Обновление зоны по ключу {#обновление-зоны-по-ключу}


### <span class="section-num">2.1</span> Создание ключа {#создание-ключа}

-   Создадим ключ для зоны `example.com`:
    ```shell
    mkdir -p /etc/named/keys
    tsig-keygen -a HMAC-SHA256 example.com > /etc/named/keys/example.com.key
    ```
-   Файл `/etc/named/keys/example.com.key` будет иметь следующий вид:
    ```conf-unix
    key "example.com" {
        algorithm hmac-sha256;
        secret "KbWuOipDOQ80ZoCiSWxhJmulLmaWSNgw43v9KkUQZBY=";
    };
    ```


### <span class="section-num">2.2</span> Настройка DNS Bind {#настройка-dns-bind}

-   Настройка происходит в файле `/etc/named.conf`.
-   Ключ скопируем на хост с DNS-сервером (если это другой сервер).
-   Поместим его в файл `/etc/named/keys/example.com.key`.
-   Подключим ключ:
    ```conf-unix
    include "/etc/named/keys/example.com.key";
    ```
-   Разрешим обновление зон:
    ```conf-unix
    zone "example.com" IN {
         type master;
         file "local.zone.db";
         allow-update { key "example.com"; };
    };

    zone "0.168.192.in-addr.arpa" IN {
         type master;
         file "192.168.0.db";
         allow-update { key "example.com"; };
    };
    ```
-   Поправим права доступа:
    ```shell
    chown -R named:named /var/named
    chown -R named:named /etc/named
    find /var/named -type d -exec chmod 770 {} \;
    find /var/named -type f -exec chmod 660 {} \;
    ```


## <span class="section-num">3</span> Использование nsupdate {#использование-nsupdate}


### <span class="section-num">3.1</span> Вызов nsupdate {#вызов-nsupdate}

-   При запуске `nsupdate` вы попадете в базовую среду командной строки для отправки команд обновления в DNS.
-   Опции запуска:
    -   `-v` : связь с DNS должна осуществляться по протоколу TCP, а не UDP;
    -   `-k` : указывает на файл ключа.
-   Вызов `nsupdate`:
    ```shell
    nsupdate -v -k /etc/named/keys/example.com.key
    ```
-   Чтобы выйти из сеанса nsupdate, просто нажмите `CTRL-D` или введите `quit` и нажмите `RETURN`.


### <span class="section-num">3.2</span> Удаление записи {#удаление-записи}

-   Безоговорочное удаление записи DNS (например, записи CNAME www.example.com).
-   В командной строке `nsupdate` введите:
    ```shell
    > update delete www.example.com cname
    > send
    ```
-   Когда вы вводите `send` и нажимаете `RETURN`, запрос на обновление создаётся, подписывается и отправляется на соответствующий DNS-сервер.
-   Если ключ был авторизован для выполнения запроса, DNS обновит свою базу данных, обновит файлы журнала, увеличит серийный номер записи SOA и отправит уведомление об изменении всем подчиненным DNS.
-   Подчинённые устройства запустят AXFR (или IXFR) для сбора обновлений с главного DNS.


### <span class="section-num">3.3</span> Несколько обновлений {#несколько-обновлений}

-   Чтобы сэкономить время и уменьшить DNS-трафик, можно одновременно отправить несколько запросов на обновление в одном пакете:
    ```shell
    > update delete www.example.com cname
    > update delete www1.example.com a
    > update delete www2.example.com a
    > update delete www3.example.com a
    > send
    ```
-   Все обновления в одном пакете `send` должны относиться к одной и той же зоне.
-   Особенности реализации: из-за фиксированного входного буфера более 2000 запросов за раз иногда не проходят.


### <span class="section-num">3.4</span> Добавление записей {#добавление-записей}

-   Добавим записи `A`, `CNAME` и `PTR`. При добавлении необходимо указать `TTL` --- время жизни записи в секундах:
    ```shell
    > update add www1.example.com 86400 a 172.16.1.1
    > update add www.example.com 600 cname www1.example.com.
    > send
    > update add 1.1.16.172.in-addr.arpa 86400 ptr www1.example.com.
    > send
    ```


### <span class="section-num">3.5</span> Неинтерактивное использование {#неинтерактивное-использование}

-   Неинтерактивный запуск: можно указать файл, содержащий пакет команд, или просто передать их по STDIN.


#### <span class="section-num">3.5.1</span> С помощью файла {#с-помощью-файла}

-   Например, создадим файл `batch.txt`:
    ```shell
    update delete www.example.com cname
    update delete www1.example.com a
    update delete www2.example.com a
    update delete www3.example.com a
    send
    ```
-   Запустите его, выполнив:
    ```shell
    nsupdate -v -k /etc/named/keys/example.com.key batch.txt
    ```


#### <span class="section-num">3.5.2</span> Удалить все записи A, начинающиеся с www, в зоне example.com {#удалить-все-записи-a-начинающиеся-с-www-в-зоне-example-dot-com}

-   Удалить все записи `A`, начинающиеся с `www`, в зоне `example.com`:
    ```shell
    ( host -t a -l example.com | grep -i '^www' | awk '{ print "update delete "$1" a" }' ; echo send ) | nsupdate -v -k /etc/named/keys/example.com.key
    ```


#### <span class="section-num">3.5.3</span> Добавить хост {#добавить-хост}

-   Добавим хост `www.example.com`:
    ```shell
    echo -e "update add www.example.com 86400 a 192.168.1.1\nshow\nsend" | nsupdate -v -k /etc/named/keys/example.com.key
    ```


## <span class="section-num">4</span> Материалы {#материалы}

-   Скрипт для упрощения использования nsupdate
    -   Репозиторий: <https://github.com/perryflynn/nsupdate-interactive>
