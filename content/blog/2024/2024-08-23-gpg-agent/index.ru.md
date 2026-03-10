---
title: "Агент для ключей gpg-agent"
author: ["Dmitry S. Kulyabov"]
date: 2024-08-23T13:55:00+03:00
lastmod: 2025-09-17T15:33:00+03:00
tags: ["sysadmin", "security"]
categories: ["computer-science"]
draft: false
slug: "gpg-agent"
---

Агент для ключей gpg-agent.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


### <span class="section-num">1.1</span> Отличия gpg-agent от ssh-agent {#отличия-gpg-agent-от-ssh-agent}

-   Можно выбирать, какие конкретно ключи хранить в агенте и они там будут храниться после перезагрузки.
-   Для каждого ключа можно отдельно задать время жизни доступа к нему и дополнительное подтверждение на использование.
-   У gpg-agent есть дополнительный уровень защиты --- пароль на доступ к ключу.
-   Есть GUI для контроля доступа.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   Установим gpg:
    ```shell
    emerge app-crypt/gnupg
    ```
-   Установим приложение для ввода пароля:
    ```shell
    emerge app-crypt/pinentry
    ```


### <span class="section-num">2.2</span> Fedora {#fedora}

-   Установим gpg:
    ```shell
    emerge app-crypt/gnupg
    ```
-   Установим приложение для ввода пароля:
    ```shell
    emerge app-crypt/pinentry
    ```


## <span class="section-num">3</span> Структура {#структура}


### <span class="section-num">3.1</span> Сокеты {#сокеты}

-   gnupg предоставляет пользовательские сокеты systemd, которые включены по умолчанию: gpg-agent.socket, gpg-agent-extra.socket, gpg-agent-browser.socket, gpg-agent-ssh.socket и dirmngr.socket
    -   основной сокет `gpg-agent.socket` используется gpg для подключения к демону `gpg-agent`;
    -   `gpg-agent-extra.socket` --- настройка переадресации Unix-сокета с удалённой системы, что позволяет использовать `gpg` на удалённой системе без передачи на неё закрытых ключей;
    -   `gpg-agent-browser.socket` позволяет веб-браузерам обращаться к демону `gpg-agent`;
    -   `gpg-agent-ssh.socket` может использоваться SSH для кэширования ключей SSH, добавленных программой ssh-add;
    -   `dirmngr.socket` запускает демон GnuPG, обрабатывающий соединения с серверами ключей.


## <span class="section-num">4</span> Основные операции {#основные-операции}


### <span class="section-num">4.1</span> Остановить, запустить, перезапустить агент {#остановить-запустить-перезапустить-агент}

-   gpg-agent работает как демон.
-   Это демон пользовательской сессии, а не системы в целом.
-   Остановить:

<!--listend-->

```shell
gpgconf --kill gpg-agent
```

-   Запустить

<!--listend-->

```shell
/usr/bin/gpg-agent --daemon
```

-   Перезапустить:

<!--listend-->

```shell
gpgconf --kill gpg-agent
/usr/bin/gpg-agent --daemon
```


### <span class="section-num">4.2</span> Просмотр списка ключей в агенте {#просмотр-списка-ключей-в-агенте}

-   Список отпечатков ключей:

<!--listend-->

```shell
ssh-add -l
```

-   Показать публичные ключи:

<!--listend-->

```shell
ssh-add -L
```

-   Можно также пользоваться командой gpg-агента:

<!--listend-->

```shell
gpg-connect-agent 'KEYINFO --ssh-list' /bye
```


### <span class="section-num">4.3</span> Добавление ключа в агент {#добавление-ключа-в-агент}

-   Добавление ключа в агент:

<!--listend-->

```shell
ssh-add ~/.ssh/id_rsa-TEST
```

-   Добавление ключа с TTL=60 секунд:

<!--listend-->

```shell
ssh-add -t 60 ~/.ssh/id_rsa-TEST
```

-   Данный вызов не модифицирует существующий ключ в `~/.gnupg/sshcontrol`.

<!--listend-->

-   Добавление ключа с включённым подтверждением:

<!--listend-->

```shell
ssh-add -c ~/.ssh/id_rsa-TEST
```

-   Данный вызов не модифицирует существующий ключ в `~/.gnupg/sshcontrol`.


### <span class="section-num">4.4</span> Удаление ключа из агента {#удаление-ключа-из-агента}

-   В ssh-add есть параметр -d, однако для gpg-agent он не сработает (вы можете выполнить команду, но она ничего не сделает).
-   Для полного удаления нужно пользоваться командами агента.
-   Сначала посмотрим список хранимых ключей:

<!--listend-->

```shell
ssh-add -l
```

-   Запоминаем хеш SHA256.
-   В файл `~/.gnupg/sshcontrol` находим этот хеш.:
-   Агент использует `keygrip` ключа для его идентификации.
-   Именно эту строку будем использовать для удаления:

<!--listend-->

```shell
gpg-connect-agent 'DELETE_KEY 3BC01B6F0043256039006294F76C45139B703DBF' /bye
```

-   Проверим:

<!--listend-->

```shell
$ ssh-add -l
```

-   Если ключа в списке нет, то всё нормально.
-   Вручную удалите упоминания ключа из `~/.gnupg/sshcontrol`.


### <span class="section-num">4.5</span> Очистить закешированные пароли {#очистить-закешированные-пароли}

-   Перезагрузите агент:

<!--listend-->

```shell
gpg-connect-agent reloadagent /bye
```


### <span class="section-num">4.6</span> Работа агента ломается после второй одновременной сессии этого же пользователя {#работа-агента-ломается-после-второй-одновременной-сессии-этого-же-пользователя}

-   Если запустить вторую сессию с этим же пользователем (например, через RDP), то старая отваливается.
-   Починить можно так:

<!--listend-->

```shell
pkill -f gpg-agent
gpg-connect-agent /bye
pkill -f gpg-agent
rm -rf $(dirname $SSH_AUTH_SOCK)/*
```


## <span class="section-num">5</span> Работа с ключами ssh {#работа-с-ключами-ssh}

-   gpg-agent поддерживает эмуляцию агента OpenSSH.


### <span class="section-num">5.1</span> Установка SSH_AUTH_SOCK {#установка-ssh-auth-sock}

-   Установите переменные окружения (в `~/.bashrc`):
    ```shell
    unset SSH_AGENT_PID
    if [ "${gnupg_SSH_AUTH_SOCK_by:-0}" -ne $$ ]
    then
      export SSH_AUTH_SOCK="$(gpgconf --list-dirs agent-ssh-socket)"
    fi
    ```


### <span class="section-num">5.2</span> Добавление поддержки в gpg-agent {#добавление-поддержки-в-gpg-agent}

-   Включим поддержку ssh:
    ```shell
    echo enable-ssh-support >> ~/.gnupg/gpg-agent.conf
    ```


### <span class="section-num">5.3</span> Добавление ключей {#добавление-ключей}

-   Идентификаторы одобренных для агента ключей сохраняются в `~/.gnupg/sshcontrol`.
-   Рекомендуется отключить в `/etc/ssh/ssh_config`, `~/.ssh/config` опцию `AddKeysToAgent`, ответственную за автоматическое добавление ключей ssh.
-   Их можно туда добавлять вручную или через `ssh-add`:
    ```shell
    ssh-add ~/.ssh/id_rsa
    ssh-add ~/.ssh/id_ed25519
    ssh-add ~/.ssh/id_ecdsa
    ```
-   Сначала `ssh` спросит парольную фразу для ключа, после чего появится диалог, где нужно выбрать пароль для шифрования ключа в агенте, обычно это простая короткая фраза (не пароль к ключу).


### <span class="section-num">5.4</span> Основные команды {#основные-команды}


#### <span class="section-num">5.4.1</span> Просмотреть список добавленных ключей {#просмотреть-список-добавленных-ключей}

```shell
ssh-add -l
```
