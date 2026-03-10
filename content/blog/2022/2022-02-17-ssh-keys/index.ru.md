---
title: "Ключи ssh"
author: ["Dmitry S. Kulyabov"]
date: 2022-02-17T14:53:00+03:00
lastmod: 2025-04-12T13:07:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "ssh-keys"
---

Создание и работа с ключами ssh.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Алгоритмы шифрования ssh {#алгоритмы-шифрования-ssh}


### <span class="section-num">1.1</span> Аутентификация {#аутентификация}

В SSH поддерживается четыре алгоритма аутентификации по открытым ключам:

-   DSA,
    -   размер ключей DSA не может превышать 1024, его следует отключить
-   RSA
    -   следует создавать ключ большого размера: 4096 бит
-   ECDSA
    -   ECDSA завязан на технологиях NIST, его следует отключить
-   Ed25519
    -   используется пока не везде


#### <span class="section-num">1.1.1</span> Отключение ключей у сервера `sshd` {#отключение-ключей-у-сервера-sshd}

-   Ключи отключаются у сервера.
-   Если просто удалить ключ, он будет повторно создан при перезапуске демона.
    -   Можно воспользоваться обходным путём с создать заведомо нерабочую символическую ссылку, которая помешает создать и использовать ключ:
        ```shell
        cd /etc/ssh
        rm ssh_host_ecdsa_key*
        ln -s ssh_host_ecdsa_key ssh_host_ecdsa_key

        rm ssh_host_dsa_key*
        ln -s ssh_host_dsa_key ssh_host_dsa_key

        rm ssh_host_key*
        ln -s ssh_host_key ssh_host_key
        ```


#### <span class="section-num">1.1.2</span> Создание серверных ключей {#создание-серверных-ключей}

-   Для RSA следует создать ключ большего размера:
    ```shell
    cd /etc/ssh
    rm ssh_host_rsa_key*
    ssh-keygen -t rsa -b 4096 -f ssh_host_rsa_key < /dev/null
    ```


#### <span class="section-num">1.1.3</span> Создание клиентских ключей {#создание-клиентских-ключей}

-   Для создания клиентских ключей лучше использовать команды:
    ```shell
    ssh-keygen -t ed25519
    ssh-keygen -t rsa -b 4096
    ```


### <span class="section-num">1.2</span> Симметричные шифры {#симметричные-шифры}

-   Из 15 поддерживаемых в SSH алгоритмов симметричного шифрования, безопасными можно считать:
    -   `chacha20-poly1305`;
    -   `aes*-ctr`;
    -   `aes*-gcm`.
-   Шифры `3des-cbc` и `arcfour` потенциально уязвимы в силу использования DES и RC4.
-   Шифр `cast128-cbc` применяет слишком короткий размер блока (64 бит).


#### <span class="section-num">1.2.1</span> Конфигурация сервера {#конфигурация-сервера}

-   В `/etc/ssh/sshd_config` рекомендуется добавить:
    ```conf-unix
    Ciphers aes256-gcm@openssh.com,aes128-gcm@openssh.com,chacha20-poly1305@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
    ```


#### <span class="section-num">1.2.2</span> Конфигурация для клиентов {#конфигурация-для-клиентов}

-   В `/etc/ssh/ssh_config` рекомендуется добавить:
    ```conf-unix
    Host *
       Ciphers aes256-gcm@openssh.com,aes128-gcm@openssh.com,chacha20-poly1305@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
    ```


### <span class="section-num">1.3</span> Обмен ключами {#обмен-ключами}

-   Применяемые в SSH методы обмена ключей  DH (Diffie-Hellman) и ECDH (Elliptic Curve Diffie-Hellman) можно считать безопасными.
-   Из 8 поддерживаемых в SSH протоколов обмена ключами вызывают подозрения три,  основанные на рекомендациях NIST:
    -   `ecdh-sha2-nistp256`;
    -   `ecdh-sha2-nistp384`;
    -   `ecdh-sha2-nistp521`.
-   Не стоит использовать протоколы, основанные на _SHA1_.


#### <span class="section-num">1.3.1</span> Настройка сервера {#настройка-сервера}

-   В `/etc/ssh/sshd_config` рекомендуется указать:
    ```conf-unix
    KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-exchange-sha256
    ```


#### <span class="section-num">1.3.2</span> Настройка клиента {#настройка-клиента}

-   В `/etc/ssh/ssh_config` рекомендуется добавить
    ```conf-unix
    Host *
       KexAlgorithms curve25519-sha256@libssh.org,diffie-hellman-group-exchange-sha256
    ```


## <span class="section-num">2</span> Файлы ssh-ключей {#файлы-ssh-ключей}

-   По умолчанию пользовательские ssh-ключи сохраняются в каталоге `~/.ssh` в домашнем каталоге пользователя.
-   Убедитесь, что у вас ещё нет ключа.
-   Файлы закрытых ключей имеют названия типа `id_<алгоритм>` (например, `id_dsa`, `id_rsa`).
    -   По умолчанию закрытые ключи имеют имена:
        ```shell
        id_dsa
        id_ecdsa
        id_ed25519
        id_rsa
        ```

-   Открытые ключи имеют дополнительные расширения `.pub`.
    -   По умолчанию публичные ключи имеют имена:
        ```shell
        id_dsa.pub
        id_ecdsa.pub
        id_ed25519.pub
        id_rsa.pub
        ```


## <span class="section-num">3</span> Создание ключа ssh {#создание-ключа-ssh}

-   Ключ ssh создаётся командой:
    ```shell
    ssh-keygen -t <алгоритм>
    ```
-   Создайте ключи:
    -   по алгоритму _rsa_ с ключём размером 4096 бит:
        ```shell
        ssh-keygen -t rsa -b 4096
        ```
    -   по алгоритму _ed25519_:
        ```shell
        ssh-keygen -t ed25519
        ```
-   При создании ключа команда попросит ввести любую ключевую фразу для более надёжной защиты вашего пароля. Можно пропустить этот этап, нажав `Enter`.
-   Сменить пароль на ключ можно с помощью команды:
    ```shell
    ssh-keygen -p
    ```


## <span class="section-num">4</span> Добавление SSH-ключа в учётную запись GitHub {#добавление-ssh-ключа-в-учётную-запись-github}

-   Скопируйте созданный SSH-ключ в буфер обмена командой:
    ```conf-unix
    xclip -i < ~/.ssh/id_ed25519.pub
    ```
-   Откройте настройки своего аккаунта на GitHub и перейдем в раздел `SSH and GPC keys`.
-   Нажмите кнопку `New SSH key`.
-   Добавьте в поле `Title` название этого ключа, например, `ed25519@<hostname>`.
-   Вставьте из буфера обмена в поле `Key` ключ.
-   Нажмите кнопку `Add SSH key`.


## <span class="section-num">5</span> Аутентификации на базе ключей SSH {#аутентификации-на-базе-ключей-ssh}

-   При аутентификации по ключу можно войти на удалённый хост без пароля учетной записи для удаленного хоста.
-   На удалённом хосте для сервера ssh долен быть настроен вход по ключу:
    ```conf-unix
    # Should we allow Pubkey (SSH version 2) authentication?
    PubkeyAuthentication yes

    # Where do we look for authorized public keys?
    # If it doesn't start with a slash, then it is
    # relative to the user's home directory
    AuthorizedKeysFile    .ssh/authorized_keys
    ```


### <span class="section-num">5.1</span> Копирование открытого ключа на удалённый хост с использованием `ssh-copy-id` {#копирование-открытого-ключа-на-удалённый-хост-с-использованием-ssh-copy-id}

-   Скопируйте на удалённый хост открытый ключ:
    ```shell
    ssh-copy-id username@remote_host
    ```


### <span class="section-num">5.2</span> Копирование открытого ключа с помощью SSH {#копирование-открытого-ключа-с-помощью-ssh}

-   Можно загрузить на удалённый хост ключи с помощью стандартного метода SSH:
    ```shell
    cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
    ```


## <span class="section-num">6</span> Настройка ключей {#настройка-ключей}

-   Для совместимости необходимо настроить разные типы ключей (см. [Тип ключа ssh]({{< relref "2022-02-03-ssh-key-type" >}})).


## <span class="section-num">7</span> Явное указание ключа ssh {#явное-указание-ключа-ssh}


### <span class="section-num">7.1</span> Возможная проблема {#возможная-проблема}

-   При попытке подключения к нужному узлу по SSH в терминал выводится сообщение об ошибке:
    ```shell
    Received disconnect from <HOST> port 22:2: Too many authentication failures
    Disconnected from <HOST> port 22
    ```
-   Это сообщение говорит о том, что вы превысили количество неудачных подключений к узлу.
-   Такое также возможно, когда у вас много ключей ssh:
    -   Если в настройках подключения не указано, какой ключ использовать, агент SSH начинает перебирать все доступные ключи.
    -   Получив отказ при попытке подключения с одним узлом, агент пробует подключиться со следующим.
    -   Примерно после 6 попыток сервер ssh на удалённом узле блокирует подключение.
-   Рекомендуется явное указать ключ ssh.


### <span class="section-num">7.2</span> Командная строка {#командная-строка}

-   В аргументах команды SSH можно явно задать путь к приватному ключу, который нужно использовать при подключении:
    ```shell
    ssh <user>@<host> -i /path/to/private/key
    ```
-   В этом случае перебора не происходит.


### <span class="section-num">7.3</span> Файл настроек {#файл-настроек}

-   Можно задать ключ в файле настроек.
-   Создайте в каталоге `~/.ssh/` файл `config`:
    ```shell
    touch ~/.ssh/config
    ```
-   Добавьте в файл `~/.ssh/config`  настройки подключения к нужным узлам:
    ```shell
    Host <name>
        Hostname       <host>
        IdentityFile   ~/.ssh/<private_key>
        IdentitiesOnly yes
    ```
