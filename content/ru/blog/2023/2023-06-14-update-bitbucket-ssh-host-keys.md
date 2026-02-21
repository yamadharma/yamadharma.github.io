---
title: "Обновление хостовых ключей ssh Bitbucket Cloud"
author: ["Dmitry S. Kulyabov"]
date: 2023-06-14T17:45:00+03:00
lastmod: 2023-09-10T20:38:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "update-bitbucket-ssh-host-keys"
---

Обновление хостовых ключей ssh Bitbucket Cloud. Заметка кратковременная, для устранения текущей проблемы.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Информация {#информация}

-   Зашифрованные копии ключей хоста Bitbucket SSH были включены в утечку данных стороннего поставщика управления учётными данными.
-   Bitbucket выпустила два новых ключа хоста SSH, которые заменят текущие ключи хоста 20 июня 2023 года.


## <span class="section-num">2</span> Определите, не сменили ли вы уже ключи {#определите-не-сменили-ли-вы-уже-ключи}

-   Чтобы проверить, какой ключ хоста использует ваш SSH-клиент, можно запустить следующую команду:
    ```shell
    $ ssh git@bitbucket.org host_key_info
    You are using host key with fingerprint:
    ssh-ed25519 SHA256:ybgmFkzwOSotHTHLJgHO0QN8L0xErw6vd0VhFA9m3SM

    See https://bitbucket.org/blog/ssh-host-key-changes for more details.
    ```
-   Если Вы видите новый отпечаток ключа хоста типа `ECDSA` или `Ed25519`, то SSH-клиент переключился на новые ключи.
-   Ничего боле делать не нужно.


## <span class="section-num">3</span> Установите новые ключи {#установите-новые-ключи}

-   Удалите старые и установите новые ключи:
    ```shell
    ssh-keygen -R bitbucket.org && curl https://bitbucket.org/site/ssh >> ~/.ssh/known_hosts
    ```
