---
title: "Emacs. Почта. Парольная аутентификация"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-22T15:20:00+03:00
lastmod: 2023-09-16T17:53:00+03:00
tags: ["emacs", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "mail-password-authentication"
---

Конфигурационные файлы для настройки парольной аутентификации для почтовых программ (в частности для Emacs).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Описание {#описание}

-   Библиотека `auth-source` для emacs создавалась для хранения паролей для gnus.
-   Документация: <https://www.gnu.org/software/emacs/manual/html_mono/auth.html>
-   Библиотека `auth-source` поддерживает несколько бэкэнд-хранилищ:
    -   бэкэнд _netrc_,
    -   файлы _json_,
        -   формат файла:
            ```js
            [{ "machine": "SERVER", "port": "PORT", "login": "USER", "password": "PASSWORD" }]
            ```
    -   _Secret Service API_ (<https://www.freedesktop.org/wiki/Specifications/secret-storage-spec/>),
    -   стандартный менеджер паролей Unix _pass_ (см. [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})).


## <span class="section-num">2</span> Настройка Emacs {#настройка-emacs}

-   Переменная `auth-sources`  задаёт источники аутентификации:
    -   устаревшая настройка по умолчанию (для _netrc_):
        ```elisp
        (setq auth-sources '((:source "~/.authinfo.gpg" :host t :port t)))
        ```
    -   то же самое, но короче (для _netrc_):
        ```elisp
        (setq auth-sources '((:source "~/.authinfo.gpg")))
        ```
    -   несколько источников (все варианты для _netrc_) (это является значением по умолчанию):
        ```elisp
        (setq auth-sources '("~/.authinfo.gpg" "~/.authinfo" "~/.netrc"))
        ```
    -   использование _Secrets API_:
        ```elisp
        (setq auth-sources '("secrets:Login"))
        ```
    -   использование _pass_:
        ```elisp
        (setq auth-sources '(password-store))
        ```
    -   использование _json_:
        ```elisp
        (setq auth-sources '("~/.authinfo.json.gpg"))
        ```


## <span class="section-num">3</span> Парольная аутентификация _netrc_ {#парольная-аутентификация-netrc}


### <span class="section-num">3.1</span> Конфигурационные файлы {#конфигурационные-файлы}

-   `~/.authinfo.gpg` - зашифрованный;
-   `~/.authinfo` - не зашифрованный;
-   `~/.netrc` - устаревший вариант.


### <span class="section-num">3.2</span> Разрешения {#разрешения}

Установите права только на чтение и запись для пользователя:

```shell
chmod 600 ~/.authinfo.gpg
```


### <span class="section-num">3.3</span> Формат файла паролей {#формат-файла-паролей}

-   Файл имеет следующий формат:
    ```conf-unix
    machine HOST login NAME password VALUE port NUMBER
    ```

-   Если имеется несколько учётных записей на одном сервере (например, на gmail), вместо имени хоста можно использовать имя профиля:
    ```conf-unix
    machine PROFILE login NAME password VALUE port NUMBER
    ```
-   Учитывая, что с одним логином могут быть почтовые адреса на разных доменах, предлагается в качестве `PROFILE` использовать полный почтовый адрес (такой, как `account@domain`).
-   Также можно использовать этот файл для указания клиентских сертификатов, которые будут использоваться при настройке TLS-соединений:
    ```conf-unix
    machine HOST port PORT key KEY cert CERT
    ```


### <span class="section-num">3.4</span> Шифрование файла паролей {#шифрование-файла-паролей}

Для безопасности следует зашифровать файл паролей (см. [Работа с PGP]({{< relref "2020-12-18-using-pgp" >}})).

-   Зашифровать файл:
    ```shell
    gpg -c .authinfo
    ```
    или
    ```shell
    gpg --symmetric .authinfo
    ```
-   Расшифровать файл:
    ```shell
    gpg --decrypt-files .authinfo.gpg
    ```


### <span class="section-num">3.5</span> Настройка подключения к Google {#настройка-подключения-к-google}

-   [Почта. Подключение к Google]({{< relref "2020-12-25-mail-google-connect" >}})
