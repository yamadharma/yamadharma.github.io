---
title: "Почта. Удаление дубликатов сообщений из локальных почтовых ящиков"
author: ["Dmitry S. Kulyabov"]
date: 2021-09-09T19:47:00+03:00
lastmod: 2023-09-14T16:36:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "removing-duplicate-messages"
---

Удаление дубликатов сообщений из почтового хранилища типа _Maildir_. Для _mbox_ тоже можно.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Программные средства {#программные-средства}


### <span class="section-num">1.1</span> mail-deduplicate {#mail-deduplicate}

-   Репозиторий: <https://github.com/kdeldycke/mail-deduplicate>
-   Сайт: <https://mail-deduplicate.readthedocs.io/en/latest/>
-   При первом поиске нашёл данную утилиту.
-   К сожалению, собственно функционал по удалению дубликатов писем продекларирован, но пока не реализован.


## <span class="section-num">2</span> Реализация средствами командной строки {#реализация-средствами-командной-строки}

-   Принято решение реализовать на коленке.


### <span class="section-num">2.1</span> Используемое программное обеспечение {#используемое-программное-обеспечение}

-   Функционалом удаления почтовых дубликатов обладает утилита `reformail`.
-   Утилита является частью пакета _maildrop_, которая в свою очередь является частью почтового сервера [Courier](http://www.courier-mta.org/).
-   Сайт: <https://www.courier-mta.org/maildrop/>
-   Установка:
    -   Linux
        -   Gentoo
            ```shell
            emerge maildrop
            ```


### <span class="section-num">2.2</span> Предварительные сведения {#предварительные-сведения}

-   Почтовый ящик `maildir` представляет собой дерево каталогов:
    ```shell
    Maildir/cur
    Maildir/new
    Maildir/tmp
    ```
-   Программа `reformail` считывает сообщение со стандартного входа, обрабатывает его и записывает результат на стандартный вывод.
-   Извлечение и печать содержимого заголовка:
    ```shell
    reformail -x
    ```
-   Обнаружение повторяющихся сообщений
    ```shell
    reformail -D len filename
    ```

    -   Параметр `-D` реализует удаления повторяющихся сообщений во входящей почте.
    -   `filename` --- файл кэша длиной примерно `len` байт.
    -   Если сообщение имеет заголовок `Message-ID:`, который уже находится в файле кэша, повторное сообщение завершается с кодом выхода, равным 0.
    -   В противном случае повторное сообщение завершается с кодом выхода, установленным на 1.
    -   Например:
        ```shell
        formail -D $((1024*1024*10)) /tmp/idcache
        ```

        -   Кэш установлен в 10 мегабайт.
-   Для работы с форматом `mbox` используют параметр `-s`.
    -   Файл почтового ящика в формате `mbox` разбивается на отдельные сообщения.
    -   Для каждого сообщения выполняется внешняя программа.
    -   Содержание каждого отдельного сообщения будет предоставлено внешней программе на стандартном вводе.


### <span class="section-num">2.3</span> Реализация для Maildir {#реализация-для-maildir}


#### <span class="section-num">2.3.1</span> Удаление дубликатов {#удаление-дубликатов}

-   Простейший однострочник:
    ```shell
    rm -f /tmp/idcache; for i in cur/*; do reformail -D $((1024*1024*10)) /tmp/idcache <$i && rm $i; done
    ```
-   Скрипт, удаляющий дубликаты во всех ящиках, синхронизируемых с помощью _mbsync_ (см. [Почта. Синхронизация. mbsync]({{< relref "2021-01-22-mail-synchronization-mbsync" >}}))
    ```shell
    #!/bin/bash
    # NAME: dedup-mailbox

    MAILDIR=~/Maildir

    list_imap=$(grep -e "^IMAPAccount" ~/.mbsyncrc | cut -d" " -f2 | xargs -I {} -n 1 echo {}" ")

    for i in ${list_imap}
    do
        list_imapdir=`ls ${MAILDIR}/${i}`

        for j in $list_imapdir
        do
            cd "${MAILDIR}/${i}/${j}"

            messages_before=`for k in cur/*; do [[ -f $k ]] && reformail -x Message-ID: <$k; done | wc -l`
            messages_unique_before=`for k in cur/*; do [[ -f $k ]] && reformail -x Message-ID: <$k; done | sort -u | wc -l`

            rm -f /tmp/idcache
            for k in cur/*
            do
                [[ -f $k ]] && reformail -D $((1024*1024*10)) /tmp/idcache <$k && rm $k
            done

            messages_after=`for k in cur/*; do [[ -f $k ]] && reformail -x Message-ID: <$k; done | wc -l`
            messages_unique_after=`for k in cur/*; do [[ -f $k ]] && reformail -x Message-ID: <$k; done | sort -u | wc -l`

            echo "Number of messages in ${MAILDIR}/${i}/${j}"
            echo -e "\t" "Total" "\t" "Unique"
            echo -e "Before:\t" $messages_before "\t" $messages_unique_before
            echo -e "After:\t"  $messages_after  "\t" $messages_unique_after
        done

    done
    ```


#### <span class="section-num">2.3.2</span> Необязательные проверки {#необязательные-проверки}

-   Перед и после удаления проверьте полное количество сообщений:
    ```shell
    for i in cur/*; do reformail -x Message-ID: <$i; done | wc -l
    ```
-   Также проверьте количество уникальных сообщений:
    ```shell
    for i in cur/*; do reformail -x Message-ID: <$i; done | sort -u | wc -l
    ```


### <span class="section-num">2.4</span> Реализация для mbox {#реализация-для-mbox}


#### <span class="section-num">2.4.1</span> Удаление дубликатов {#удаление-дубликатов}

-   Скрипт, вызывающий программу обработки для каждого сообщения из _mbox_:
    ```shell
    #!/bin/sh
    # NAME: dedup-mbox
    # INPUT: $1 = mbox
    # OUTPUT: nmbox (файл с удалёнными дубликатами сообщений)

    # Delete temporary files
    rm -f /tmp/tmpmail /tmp/idcache nmbox

    # reformail-mbox.sh is called for each mail
    cat $1 | reformail -s ./reformail-mbox.sh
    ```
-   Основной скрипт для дедупликации:
    ```shell
    #!/bin/bash
    # NAME: reformail-mbox.sh
    # INPUT: stdin: a email
    # called by dedup-mbox

    TM=/tmp/tmpmail
    if [ -f $TM ]
    then
        echo error!
        exit 1
    fi
    cat > $TM

    # mbox format, each mail end with a blank line
    echo "" >> $TM

    cat $TM | reformail -D $((1024*1024*10)) /tmp/idcache

    # if this mail isn't a dup (reformail return 1 if message-id is not found)
    if [ $? != 0 ]
    then
        # each mail shall have a message-id
        if grep -q -i '^message-id:' $TM
        then
            cat $TM >> nmbox
        fi
    fi

    rm $TM
    ```
