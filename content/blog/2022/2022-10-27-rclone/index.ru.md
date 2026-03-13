---
title: "rclone"
author: ["Dmitry S. Kulyabov"]
date: 2022-10-27T14:29:00+03:00
lastmod: 2023-08-26T12:52:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "rclone"
---

Утилита командной строки для синхронизация данных с сетевыми объектными хранилищами.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://rclone.org/>


## <span class="section-num">2</span> Подключение хранилищ {#подключение-хранилищ}


### <span class="section-num">2.1</span> Общая информация {#общая-информация}

-   Для подключения сетевого хранилища следует запустить:
    ```shell
    rclone config
    ```
-   Далее следовать текстовому меню.


### <span class="section-num">2.2</span> Хранилища {#хранилища}


#### <span class="section-num">2.2.1</span> Google Drive {#google-drive}

-   При конфигурировании запускается броузер.
-   Необходимо залогиниться и разрешить доступ.
-   В конфигурационный файл записывается токен для доступа.


#### <span class="section-num">2.2.2</span> Yandex Disk {#yandex-disk}

-   При конфигурировании запускается броузер.
-   Необходимо залогиниться и разрешить доступ.
-   В конфигурационный файл записывается токен для доступа.


#### <span class="section-num">2.2.3</span> Mail.ru Cloud {#mail-dot-ru-cloud}

-   В качестве пароля необходимо использовать пароль для внешнего приложения (см. [Пароли mail.ru]({{< relref "2022-10-27-mail-ru-passwords" >}})).


## <span class="section-num">3</span> Использование {#использование}

-   Пусть название хранилища будет `remote`.
-   Просмотр списка контейнеров в хранилище:
    ```shell
    rclone lsd remote:
    ```
-   Создание нового каталога:
    ```shell
    rclone mkdir remote:/dir
    ```
-   Просмотр списка файлов в каталоге:
    ```shell
    rclone ls remote:/dir
    ```
-   Копирование файлов с локальной машины в хранилище:
    ```shell
    rclone copy /home/local/directory remote:/dir
    ```
-   Синхронизация файлов на локальной машине и в хранилище:
    ```shell
    rclone sync /home/local/directory remote:/dir
    ```
