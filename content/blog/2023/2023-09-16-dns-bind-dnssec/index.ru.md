---
title: "DNS. Bind. DNSSEC"
author: ["Dmitry S. Kulyabov"]
date: 2023-09-16T19:52:00+03:00
lastmod: 2023-12-27T10:11:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "dns-bind-dnssec"
---

Настройка DNSSEC в Bind.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Версия bind выше, чем 9.9:
    ```shell
    named -v
    ```


## <span class="section-num">2</span> Ключи {#ключи}


### <span class="section-num">2.1</span> Каталоги ключей {#каталоги-ключей}

-   Создаём каталог, в котором будем хранить ключи и переходим в него:
    -   Red Hat:
        ```shell
        mkdir /var/named/keys
        cd /var/named/keys
        ```
    -   Debian, Ubuntu:
        ```shell
        mkdir /etc/bind/keys
        cd /etc/bind/keys
        ```


### <span class="section-num">2.2</span> Создание ключей {#создание-ключей}

-   Создаём мастер-ключей (`KSK`):
    ```shell
    dnssec-keygen -f KSK -a ECDSAP256SHA256 -b 4096 -n ZONE example.com
    ```

    -   `-f KSK`: создаётся мастер-ключ;
    -   `-a ECDSAP256SHA256`: используемый алгоритм шифрования;
    -   `-b 2048`: размер ключа в битах (для алгоритма `ECDSAP256SHA256` игнорируется);
    -   `-n ZONE`: для DNS-зоны;
    -   `-r /dev/urandom`: источник случайных данных;
    -   `example.com`: домен, для которого предназначен ключ.

-   Создаём ключ для зоны (`ZSK`):
    ```shell
    dnssec-keygen -a ECDSAP256SHA256 -b 2048 -n ZONE example.com
    ```
-   Задаём владельца для сгенерированных файлов:
    -   Red Hat:
        ```shell
        chown -R named:named /var/named/keys
        ```
    -   Debian, Ubuntu:
        ```shell
        chown -R bind:bind /etc/bind/keys
        ```


### <span class="section-num">2.3</span> Права доступа {#права-доступа}

-   Поправим права доступа:
    ```shell
    chown -R named:named /var/named/keys
    chmod 640 /var/named/keys/*
    ```


## <span class="section-num">3</span> Подпись зоны {#подпись-зоны}

-   Зоны можно подписывать вручную или настроить автоматическую подпись зон.
-   При ручной подписи необходимо переподписывать файл зоны после изменения.


### <span class="section-num">3.1</span> Ручная подпись зоны {#ручная-подпись-зоны}

-   Копируем содержимое ключей в файл зоны:
    ```shell
    cat Kexample.com.*key >> /var/named/master/example.com
    ```
-   Переходим в каталог, где хранится наша зона:
    -   Red Hat:
        ```shell
        cd /var/named/master
        ```
-   Debian, Ubuntu:
    ```shell
    cd /etc/bind/master
    ```
-   Подписываем зону:
    ```shell
    dnssec-signzone -e +3mo -N INCREMENT -K /var/named/keys example.com
    ```

    -   `-e +3mo` : время действия RRSIG (3 месяца);
    -   `-N INCREMENT` : использовать формат серийного номера SOA из файла;
    -   `-K /var/named/keys` : путь хранения сгенерированных ключей;
    -   `example.com` : подписываемый домен.
-   В каталоге хранения зон мы должны увидеть файл подписанной зоны `example.com.signed`.


#### <span class="section-num">3.1.1</span> Настройка BIND {#настройка-bind}

-   Редактируем конфигурационный файл:
    -   Red Hat:
        ```shell
        /etc/named.conf
        ```
    -   Debian, Ubuntu:
        ```shell
        /etc/bind/named.conf.local
        ```
-   Проверяем, чтобы dnssec был включён:
    ```conf-unix
    options {
    ...
    dnssec-enable yes;
    dnssec-validation yes;
    dnssec-lookaside auto;
    }
    ```

    -   `dnssec-enable` : включение или отключение `dnssec` на уровне сервера;
    -   `dnssec-validation` : проверка корректность ответов;
    -   `dnssec-lookaside` : разрешение использовать сторонние корни DNSSEC.

-   В настройке зоны меняем путь к файлу:
    ```conf-unix
    zone "example.com" {
    file "master/example.com.signed";
    };
    ```
-   Перезапускаем bind:
    -   Red Hat:
        ```shell
        systemctl reload named
        ```
    -   Debian, Ubuntu:
        ```shell
        systemctl reload bind
        ```
-   Или перегружаем конфигурацию bind:
    ```shell
    rndc reload
    ```


### <span class="section-num">3.2</span> Автоматическое подписывание зоны {#автоматическое-подписывание-зоны}

-   Для автоматизации процесса в конфигурационном файле bind задаём:
    ```conf-unix
    options {
    ...
    key-directory "/var/named/keys";
    sig-validity-interval 20 10;
    };
    ```

    -   `key-directory` : каталог хранения ключей;
    -   `sig-validity-interval` : период действия ключей: дней (период обновления).
-   Для зоны редактируем:
    ```shell
    zone "example.com" {
    ...
    file "master/example.com";
    inline-signing yes;
    auto-dnssec maintain;
    };
    ```

    -   `inline-signing` : включение или отключение прозрачного формирования подписей (без необходимости менять файл зоны);
    -   `auto-dnssec` : уровень автоматической настройки DNSSEC для зоны.
-   Меняем серийный номер файла зоны.
-   Перезапускаем bind:
    -   Red Hat:
        ```shell
        systemctl reload named
        ```
    -   Debian, Ubuntu:
        ```shell
        systemctl reload bind
        ```
-   Или перегружаем конфигурацию bind:
    ```shell
    rndc reload
    ```
-   В каталоге зоны должны появиться дополнительные 3 файла: `example.com.jbk`, `example.com.signed`, `example.com.signed.jnl`.


## <span class="section-num">4</span> Проверка работы {#проверка-работы}

-   Чтобы проверить, отдаёт ли наш сервер ответы с цифровыми подписями, вводим команду:
    ```shell
    dig example.com +dnssec
    ```
-   Посмотрим подпись зоны:
    ```shell
    dig DNSKEY example.com. @localhost +multiline
    ```
-   Или:
    ```shell
    dig A example.com. @localhost +noadditional +dnssec +multiline
    ```
-   Получить DS записи для реестра доменов и прописать их у регистратора:
    ```shell
    dig @localhost dnskey example.com | dnssec-dsfromkey -f - example.com
    ```
-   После того, как мы добавили DS записи в реестр, спустя какое-то время можно проверять все ли в порядке.
    -   Сайт: <https://dnssec-analyzer.verisignlabs.com>.
