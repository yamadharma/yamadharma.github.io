---
title: "Работа с PGP"
author: ["Dmitry S. Kulyabov"]
date: 2020-12-18T12:39:00+03:00
lastmod: 2023-07-21T18:05:00+03:00
tags: ["programming", "sysadmin", "education"]
categories: ["computer-science"]
draft: false
slug: "using-pgp"
---

Использование набора программ GPG (GNU ревлизация PGP).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Экспорт ключей PGP {#экспорт-ключей-pgp}

-   Экспорт ключей
    -   Экспорт всех открытых ключей в текстовый файл в кодировке base64:
        ```shell
        gpg -a --export > mypubkeys.asc
        ```
    -   Экспорт всех зашифрованных закрытых ключей (которые также будут включать соответствующие открытые ключи) в текстовый файл:
        ```shell
        gpg -a --export-secret-keys > myprivatekeys.asc
        ```
    -   Опционально экспортируется `trustdb` gpg в текстовый файл:
        ```shell
        gpg --export-ownertrust > otrust.txt
        ```
-   Импорт ключей
    -   Выполните команды `gpg --import` для двух файлов `asc`, а затем проверьте наличие новых ключей с помощью `gpg -k` и `gpg -K`:
        ```shell
        gpg --import myprivatekeys.asc
        gpg --import mypubkeys.asc
        gpg -K
        gpg -k
        ```
    -   При желании также импортируйте файл `trustdb`:
        ```shell
        gpg --import-ownertrust otrust.txt
        ```
    -   Проверьте шифрование и дешифрование с помощью команд `gpg -er USERID` и `gpg -d`.


## <span class="section-num">2</span> `gpg-agent` {#gpg-agent}


### <span class="section-num">2.1</span> Общая информация {#общая-информация}

-   Используется для временного хранения пароля.
-   Предоставляются пользовательские сокеты `systemd`:
    -   основной сокет `gpg-agent.socket` используется _gpg_ для подключения к демону `gpg-agent`;
    -   сокет `gpg-agent-extra.socket` на локальной системе используется для настройки переадресации Unix-сокета с удалённой системы;
    -   `gpg-agent-browser.socket` позволяет веб-браузерам обращаться к демону `gpg-agent`;
    -   `gpg-agent-ssh.socket` может использоваться SSH для кэширования ключей SSH, добавленных программой ssh-add;
    -   `dirmngr.socket` запускает демон GnuPG, обрабатывающий соединения с серверами ключей.


### <span class="section-num">2.2</span> Запуск {#запуск}

-   Активизируются сокеты, а не сам `gpg-agent`.
-   Запуск под управлением `systemd`:
    ```shell
    systemctl --user enable --now gpg-agent.socket
    ```


### <span class="section-num">2.3</span> Перезапуск агента {#перезапуск-агента}

-   После обновления настроек следует перезапустить агента, передав команду `RELOADAGENT` программе `gpg-connect-agent`:
    ```shell
    gpg-connect-agent reloadagent /bye
    ```


### <span class="section-num">2.4</span> Настройка {#настройка}

-   Настраивается в файле `~/.gnupg/gpg-agent.conf`.
-   Время жизни для ключей в кэше с момента последнего использования:
    ```conf-unix
    default-cache-ttl 3600
    ```


### <span class="section-num">2.5</span> pinentry {#pinentry}

-   gpg-agent использует pinentry для отображения диалога запроса пароля.
-   Вариант диалога настраивается в файле настроек `~/.gnupg/gpg-agent.conf`.
-   Чтобы установить конкретный диалог, установите опцию `pinentry-program` в файле `~/.gnupg/gpg-agent.conf`, например:
    ```conf-unix
    pinentry-program /usr/bin/pinentry-curses
    ```
-   Существуют разные реализации pinentry.
-   Просмотр реализаций:
    -   Gentoo:
        ```shell
        eselect pinentry list
        ```


### <span class="section-num">2.6</span> Кэширование паролей {#кэширование-паролей}

-   Время кеширования определяется параметрами `max-cache-ttl` и `default-cache-ttl`.
-   Чтобы вводить пароль всего один раз за сеанс, нужно установить их на очень высокое значение, например:
    ```conf-unix
    ## gpg-agent.conf
    max-cache-ttl 60480000
    default-cache-ttl 60480000
    ```
-   Для кэширования паролей в режиме эмуляции SSH следует установить параметры `default-cache-ttl-ssh` и `max-cache-ttl-ssh`, например:
    ```conf-unix
    ## gpg-agent.conf
    default-cache-ttl-ssh 60480000
    max-cache-ttl-ssh 60480000
    ```


## <span class="section-num">3</span> Шифрование {#шифрование}

-   Шифрование может быть симметричным и ассиметричным.
-   Симметричное шифрование шифруется и расшифровывается приватным ключом или одной и той же парольной фразой.
-   Ассиметричное шифрование шифруется публичным ключом, расшифровывается приватным.


### <span class="section-num">3.1</span> Симметричное шифрование {#симметричное-шифрование}

-   Зашифровать файл:

<!--listend-->

```shell
gpg -c filename
```

или

```shell
gpg --symmetric filename
```

-   Расшифровать файл:
    ```shell
    gpg --decrypt-files filename.gpg
    ```
-   Расшифровать файл с выводом на терминал:
    ```shell
    gpg --decrypt filename.gpg
    ```
