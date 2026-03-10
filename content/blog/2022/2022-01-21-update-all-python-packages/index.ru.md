---
title: "Обновление пакетов python"
author: ["Dmitry S. Kulyabov"]
date: 2022-01-21T16:33:00+03:00
lastmod: 2023-09-19T09:30:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "update-all-python-packages"
---

-   Пакеты можно устанавливать с помощью системного менеджера пакетов, и с помощью пакетного менеджера самого _python_, например _pip_.
-   В последнем случае пакеты лучше устанавливать в каталоге пользователя (user-wide).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Список всех устаревших пакетов {#список-всех-устаревших-пакетов}

-   Создать список всех устаревших пакетов:
    ```shell
    pip3 list --outdated
    ```
-   Создать список всех устаревших пакетов, установленных пользователем:
    ```shell
    pip3 list --outdated --user
    ```


## <span class="section-num">2</span> Обновление всех пакетов python в Linux {#обновление-всех-пакетов-python-в-linux}

-   Обновляем пакеты, установленные пользователем (`--user`).
-   С использованием `pip` и `grep`:
    ```shell
    pip3 list --outdated --format=freeze --user | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U --user
    ```
-   С использованием `pip` и `awk`:
    ```shell
    pip3 list --outdated --user | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print)' | cut -d' ' -f1 | xargs -n1 pip3 install -U --user
    ```


## <span class="section-num">3</span> Обновление всех пакетов python в Windows {#обновление-всех-пакетов-python-в-windows}

-   Обновляем пакеты, установленные пользователем (`--user`).
-   Используем _powershell_:
    ```shell
    pip freeze --user | %{$_.split('==')[0]} | %{pip install --upgrade $_ --user}
    ```
