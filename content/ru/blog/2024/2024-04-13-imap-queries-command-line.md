---
title: "Запросы по протоколу imap из командной строки"
date: 2024-04-13T17:27:00+03:00
lastmod: 2024-05-15T17:21:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "imap-queries-command-line"
---

Запросы по протоколу imap из командной строки.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Выполнение запросов imap с использованием curl {#выполнение-запросов-imap-с-использованием-curl}

-   Работа с ящиками imap с помощью curl.


### <span class="section-num">1.1</span> Необходимая информация {#необходимая-информация}

-   Необходимая информация:
    -   адрес почтового сервера;
    -   почтовый логин;
    -   почтовый пароль.
-   В примерах будем подключаться к серверу IMAP `imap.example.com`.
-   URL подключения:
    -   подключение без шифрования: `imap://mail.example.com/`;
    -   подключение по SSL: `imaps://mail.example.com/`;
-   Будем использовать следующие учётные данные:
    -   логин: `user`;
    -   пароль: `password`.
-   Пароли лучше хранить в базе данных паролей или менеджере паролей:
    -   netrc: [Emacs. Почта. Парольная аутентификация]({{< relref "2021-01-22-mail-password-authentication" >}});
    -   pass: [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}}).


### <span class="section-num">1.2</span> Список папок {#список-папок}

-   Выполним запрос к серверу IMAP:
    ```shell
    curl --url "imap://mail.example.com/" --user "user:password"
    ```
-   При запросе через SSL можно дополнительно указать опцию `insecure`:
    ```shell
    curl --insecure --url "imaps://mail.example.com/" --user "user:password"
    ```
-   Если не указать пароль в аргументе `--user`, `curl` запросит пароль перед выполнением запроса.
-   Получим список почтовых ящиков:
    ```shell
    ​* LIST (\HasNoChildren \Unmarked) "|" Archive
    ​* LIST (\HasNoChildren \Unmarked \Drafts) "|" Drafts
    ​* LIST (\HasNoChildren \Unmarked \NoInferiors) "|" INBOX
    ​* LIST (\HasNoChildren \Unmarked \Sent) "|" Sent
    ​* LIST (\HasNoChildren \Unmarked \Junk) "|" Spam
    ​* LIST (\HasNoChildren \Unmarked \Trash) "|" Trash
    ```
-   Если название папки нечитабельно, его можно расшифровать (см. [Почта. Кодировка папок IMAP]({{< relref "2021-07-04-mail-imap-folder-encoding" >}})).


### <span class="section-num">1.3</span> Количество сообщений {#количество-сообщений}

-   Чтобы получить сообщение, нам нужен идентификатор сообщения.
-   Выясним, сколько сообщений в почтовом ящике, поскольку идентификаторы сообщений являются последовательными номерами.
-   Посмотрим, сколько сообщений существует в папке `Archive`:

<!--listend-->

```shell
curl --insecure --url "imaps://mail.example.com/" --request "EXAMINE Archive" --user "user:password"
```

-   Строчка ответа с ключевым словом `EXISTS` укажет количество сообщений в папке.
-   Предположительно, номера сообщений идут от 1 до количества сообщений (не обязательно).


### <span class="section-num">1.4</span> Получение сообщения {#получение-сообщения}

-   Получим сообщение, задав его идентификатор (например, 5):
    ```shell
    curl --insecure --url "imaps://mail.example.com/Archive;UID=5" --user "user:password"
    ```
-   Получение сообщения включает в себя как заголовки, так и тело.
-   Если необходимо получить только заголовки или их подмножество, необходимо закодировать это в запросе.
-   Получим заголовки _Кому_ (`To`), _От_ (`From`), _Дата_ (`Date`), _Тема_ (`Subject`):
    ```shell
    curl --insecure --url "imaps://mail.example.com/Archive;UID=5;SECTION=HEADER.FIELDS%20(DATE%20FROM%20TO%20SUBJECT)" --user "user:password"
    ```
-   Можно отправить запрос отдельно (например, запросив `Subject`):
    ```shell
    curl --insecure --verbose --url "imaps://mail.example.com/Archive" --request "fetch 5 BODY.PEEK[HEADER.FIELDS (Subject)]" --user "user:password"
    ```
-   Однако при программном использовании API-интерфейса curl ответы не декодируются. Поэтому, без флага `--verbose` мы бы получили нулевой вывод.


### <span class="section-num">1.5</span> Простые скрипты {#простые-скрипты}

-   Получить темы первых десяти сообщений в указанном почтовом ящике:
    ```shell
    #!/bin/bash
    # Dump the subject of the first ten messages in the folder

    for id in $(seq 1 10)
    do
        echo "Message ${id}"
        curl --insecure \
             --url "imaps://mail.example.com/Archive;UID=${id};SECTION=HEADER.FIELDS%20(SUBJECT)" \
             --user "user:password"
    done
    ```
-   Получить темы всех сообщений в указанном почтовом ящике:
    ```shell
    #!/bin/bash
    # Dump the subject of all messages in the folder

    while true
    do
        echo "Message ${id}"
        curl --insecure \
             --url "imaps://mail.example.com/Archive;UID=${id};SECTION=HEADER.FIELDS%20(SUBJECT)" \
             --user "user:password" || exit
        id=$(expr $id + 1)
    done
    ```
