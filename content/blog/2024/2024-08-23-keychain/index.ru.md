---
title: "Агент для ключей keychain"
author: ["Dmitry S. Kulyabov"]
date: 2024-08-23T17:12:00+03:00
lastmod: 2024-08-23T17:19:00+03:00
tags: ["security", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "keychain"
---

Агент для ключей keychain.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Набор скриптов для управления ssh-agent и gpg-agent.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   Установим пакет:
    ```shell
    emerge net-misc/keychain
    ```


## <span class="section-num">3</span> Интеграция в систему {#интеграция-в-систему}

-   Добавьте в `~/.bashrc`:
    ```shell
    keychain ~/.ssh/id_rsa
    . ~/.keychain/${HOSTNAME}-sh
    . ~/.keychain/${HOSTNAME}-sh-gpg
    ```
-   По желанию можно добавить ещё несколько ключей.
