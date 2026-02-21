---
title: "Wallabag. Консольный склиент. wallabag-client"
author: ["Dmitry S. Kulyabov"]
date: 2025-11-07T12:40:00+03:00
lastmod: 2025-11-10T10:26:00+03:00
tags: ["read", "sysadmin"]
categories: ["self-management", "computer-science"]
draft: false
slug: "wallabag-cli-wallabag-client"
---

Wallabag. Консольный склиент. wallabag-client.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий:
-   Клиент командной строки.
-   Документация: <https://shaik.link/posts/wallabag-client/features/>


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Python {#python}

-   Установка локальная:
    ```shell
    pipx install wallabag-client
    ```


### <span class="section-num">2.2</span> Gentoo {#gentoo}

-   Репозиторий karma ([Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
    ```shell
    emerge dev-python/wallabag-client
    ```


## <span class="section-num">3</span> Конфигурация {#конфигурация}

-   Запустите:
    ```shell
    wallabag config
    ```
-   Введите всю информацию.
