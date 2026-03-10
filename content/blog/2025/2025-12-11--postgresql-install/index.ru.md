---
title: "PostgreSQL. Установка"
author: ["Dmitry S. Kulyabov"]
date: 2025-12-11T11:38:00+03:00
lastmod: 2025-12-11T11:54:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "postgresql-install"
---

PostgreSQL. Установка.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Rocky Linux {#rocky-linux}


### <span class="section-num">1.1</span> Обновление пакетов системы {#обновление-пакетов-системы}

```shell
sudo dnf update -y
```


### <span class="section-num">1.2</span> Установка сервера PostgreSQL {#установка-сервера-postgresql}

```shell
sudo dnf install postgresql-server -y
```


### <span class="section-num">1.3</span> Инициализируйте кластер баз данных {#инициализируйте-кластер-баз-данных}

-   После установки инициализируйте кластер PostgreSQL с помощью скрипта:

<!--listend-->

```shell
sudo postgresql-setup --initdb
```


### <span class="section-num">1.4</span> Запустите и включите службу PostgreSQL {#запустите-и-включите-службу-postgresql}

-   Запустите службу:

<!--listend-->

```shell
sudo systemctl start postgresql
```

-   Проверьте статус службы:
    ```shell
    sudo systemctl status postgresql
    ```

-   Включите автоматический запуск службы при загрузке системы:
    ```shell
    sudo systemctl enable postgresql
    ```


### <span class="section-num">1.5</span> Обеспечьте безопасность пользователя по умолчанию: {#обеспечьте-безопасность-пользователя-по-умолчанию}

-   Переключитесь на учётную запись postgres:

<!--listend-->

```shell
sudo -i -u postgres
```

-   Войдите в интерфейс командной строки PostgreSQL:

<!--listend-->

```shell
psql
```

-   Установите надёжный пароль для пользователя postgres:

<!--listend-->

```shell
\password postgres
```

-   Выйдите из psql и вернитесь к обычной оболочке:

<!--listend-->

```shell
\q
exit
```


### <span class="section-num">1.6</span> Настройте удалённый доступ {#настройте-удалённый-доступ}

-   Настраиваете только при доступе с внешних хостов.
-   По умолчанию PostgreSQL разрешает подключения только с локального компьютера.
-   Для удалённого доступа нужно настроить брандмауэр и конфигурационные файлы PostgreSQL.

-   Настройка брандмауэра:

<!--listend-->

```shell
sudo firewall-cmd --add-service=postgresq --permanent
sudo firewall-cmd --reload
```

-   Первая команда добавляет правило для разрешения трафика на порту 5432, вторая --- перезагружает брандмауэр для применения изменений.

-   Редактирование конфигурационных файлов.
-   Файл `postgresql.conf` (`/var/lib/pgsql/data/postgresql.conf`).
    -   Найдите строку `#listen_addresses = 'localhost'`, удалите символ `#` и замените `localhost` на `*`, чтобы PostgreSQL слушал все доступные сетевые интерфейсы.
-   Файл `/var/lib/pgsql/data/pg_hba.conf`.
    -   Добавьте в конец файла строку:

<!--listend-->

```conf-unix
host all all 0.0.0.0/0 md5
```

-   Для повышения безопасности в рабочей среде замените `0.0.0.0/0` на конкретный IP-адрес или диапазон CIDR.

-   Перезапустите службу PostgreSQL для применения изменений:

<!--listend-->

```shell
sudo systemctl restart postgresql
```
