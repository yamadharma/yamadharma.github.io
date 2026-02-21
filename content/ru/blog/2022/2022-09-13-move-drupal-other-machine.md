---
title: "Перенос Drupal на другую машину"
author: ["Dmitry S. Kulyabov"]
date: 2022-09-13T19:45:00+03:00
lastmod: 2023-09-29T19:52:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "move-drupal-other-machine"
---

Перенос Drupal на другую машину.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Прагматика {#прагматика}

-   При замене операционной системы возникает необходимость переноса сервисов на другую машину.


## <span class="section-num">2</span> Порядок миграции {#порядок-миграции}


### <span class="section-num">2.1</span> Настройка машины {#настройка-машины}

-   Следует установить на машину стек LAMP (см. [Rocky Linux. Установка сервера]({{< relref "2022-08-12-rockylinux-server-installation" >}})).


#### <span class="section-num">2.1.1</span> Необходимое программное обеспечение {#необходимое-программное-обеспечение}

-   Установите необходимое для Drupal программное обеспечение:
    ```shell
    dnf install gd
    dnf install php-gd
    dnf install php-pecl-apcu
    ```


#### <span class="section-num">2.1.2</span> Drush {#drush}

<!--list-separator-->

1.  Drush 8

    -   Загрузите нужную версию `drush` из `https://github.com/drush-ops/drush/releases`:
        ```shell
        cd /usr/local/bin/
        wget https://github.com/drush-ops/drush/releases/download/8.4.8/drush.phar -O drush
        chmod +x drush
        ```


#### <span class="section-num">2.1.3</span> Запуск базы данных {#запуск-базы-данных}

<!--list-separator-->

1.  Mysql

    -   Запустите базу данных:
        ```shell
        systemctl enable --now mariadb.service
        ```
    -   Поправьте уровень безопасности:
        ```shell
        mysql_secure_installation
        ```

        -   Не надо переключаться на сокет и менять пароль пользователя `root`.

<!--list-separator-->

2.  Postgresql

    -   Запустите базу данных:
        ```shell
        systemctl enable --now postgresql.service
        ```


#### <span class="section-num">2.1.4</span> Настройка сети {#настройка-сети}

-   Откройте необходимые порты:
    ```shell
    firewall-cmd --add-service=http --permanent
    firewall-cmd --add-service=https --permanent
    firewall-cmd --reload
    ```


#### <span class="section-num">2.1.5</span> Настройка Selinux {#настройка-selinux}

-   Зададим переключатели для Selinux:
    ```shell
    setsebool -P httpd_can_network_connect 1
    setsebool -P httpd_can_sendmail 1
    ```


### <span class="section-num">2.2</span> Перенос файлов {#перенос-файлов}

-   Перейдите на новой машине в каталог для файлов www-сервера:
    ```shell
    cd /var/www/html
    ```
-   Скопируйте каталог с файлами со старой машины:
    ```shell
    rsync -av -HS -AX root@<oldhost>:/var/www/html/<oldsite> . --delete
    ```
-   Перегенерите метки Selinux:
    ```shell
    restorecon -vR /var/www/
    ```


### <span class="section-num">2.3</span> Перенос базы данных {#перенос-базы-данных}


#### <span class="section-num">2.3.1</span> Создание дампа базы данных {#создание-дампа-базы-данных}

-   На исходной машине необходимо создать дамп базы данных.

<!--list-separator-->

1.  Mysql

    -   Создайте дамп базы:
        ```shell
        mysqldump --quote-names --add-drop-table -u root -p  databasename > mysql-databasename-`date +%Y%m%d-%H%M%S`.sql
        ```

<!--list-separator-->

2.  Postgres

    -   Создайте дамп базы:
        ```shell
        su - postgres -c "pg_dump -U postgres > pg-databasename-`date +%Y%m%d-%H%M%S`.sql
        ```


#### <span class="section-num">2.3.2</span> Создание базы данных на новой машине {#создание-базы-данных-на-новой-машине}

<!--list-separator-->

1.  Mysql

    -   База данных должна быть создана с использованием кодировки UTF-8 (Unicode) (utf8mb4) и параметров сортировки `utf8mb4_unicode_ci` или `utf8mb4_general_ci`.
        -   Разница между двумя сопоставлениями связана с тем, насколько быстро они сравнивают символы и сортируют их.
        -   `utf8mb4_general_ci` немного быстрее, однако `utf8mb4_unicode_ci` более точен для более широкого диапазона символов.
    -   Необходимые значения:
        -   `databasename` --- имя базы данных;
        -   `username` --- имя пользователя базы данных;
        -   `password` --- пароль пользователя базы данных.
    -   Создайте новую базу данных для вашего сайта (измените `username` и `databasename`):
        ```shell
        mysql -u root -p -e "CREATE DATABASE databasename CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        ```
    -   Подключитесь к базе данных:
        ```shell
        mysql -u root -p
        ```

        -   Создайте пользователя и установите разрешения:
            ```sql
            CREATE USER username@localhost IDENTIFIED BY 'password';
            GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES ON `databasename`.* TO 'username'@'localhost' IDENTIFIED BY 'password';
            ```
        -   Сбросьте привилегии:
            ```sql
            FLUSH PRIVILEGES;
            ```
        -   Закройте терминал базы данных, набрав `exit`.

<!--list-separator-->

2.  Postgres

    -   Создайте пользователя базы данных:
        ```shell
        createuser --pwprompt --encrypted --no-adduser --no-createdb username
        ```
    -   Создайте базу данных:
        ```shell
        createdb --encoding=UNICODE --owner=username databasename
        ```


#### <span class="section-num">2.3.3</span> Восстановление дампа базы данных {#восстановление-дампа-базы-данных}

<!--list-separator-->

1.  Mysql

    -   Восстановите базу данных:
        ```shell
        mysql -u root -p databasename < mysql-databasename.sql
        ```

<!--list-separator-->

2.  Postgres

    -   Восстановите базы данных:
        ```shell
        psql -U postgres -d databasename < pg-databasename.sql
        ```
