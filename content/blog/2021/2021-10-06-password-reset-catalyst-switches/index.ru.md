---
title: "Сброс пароля на коммутаторах Catalyst"
author: ["Dmitry S. Kulyabov"]
date: 2021-10-06T11:36:00+03:00
lastmod: 2023-10-06T16:59:00+03:00
tags: ["cisco", "sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "password-reset-catalyst-switches"
---

Сброс пароля на коммутаторах Catalyst серий 2900, 2950, 2960, 3500, 3550.

<!--more-->

{{< toc >}}

-   При нажатой кнопке выбора режима (mode) вставить шнур питания (не отпускать кнопку, до тех пор, пока индикатор над портом 1, не будет гореть, как минимум 2 секунды).
-   Ввести команду:
    ```shell
    flash_init
    ```
-   Ввести команду:
    ```shell
    load_helper
    ```
-   Переименовать файл `config.text`:
    ```shell
    rename flash:config.text flash:config.old
    ```
-   Продолжить процесс загрузки:
    ```shell
    boot
    ```
-   Отказаться от входа в режим настройки (набрать `no`).
-   Перейти в пользовательский режим: (`Enter`).
-   Перейти в привилегированный режим:
    ```shell
    enable
    ```
-   Вернуть имя ранее переименованному файлу:
    ```shell
    rename flash:config.old flash:config.text
    ```
-   Загрузить в running-config конфигурационный файл:
    ```shell
    copy startup run
    ```
-   Перейти в конфигурационный режим:
    ```shell
    conf t
    ```
-   Изменить пароль:
    ```shell
    enable password <пароль>
    ```
-   Выйти из режима настройки (`Ctrl+Z`).
-   Сохранить конфигурацию:
    ```shell
    write memory
    ```
