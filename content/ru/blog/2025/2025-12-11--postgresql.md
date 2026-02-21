---
title: "PostgreSQL"
author: ["Dmitry S. Kulyabov"]
date: 2025-12-11T11:20:00+03:00
lastmod: 2025-12-11T11:39:00+03:00
tags: ["MOC", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "postgresql"
---

PostgreSQL.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   PostgreSQL есть объектно-реляционная система управления базами данных (ORDBMS) с открытым исходным кодом.


## <span class="section-num">2</span> Операции {#операции}

-   [PostgreSQL. Установка]({{< relref "2025-12-11--postgresql-install" >}})


### <span class="section-num">2.1</span> Rocky Linux {#rocky-linux}

-   Обновление пакетов системы:
    ```shell
    sudo dnf update -y
    ```

    -   Открыть терминал и выполнить команду: `sudo dnf update -y`.

-   Установка сервера PostgreSQL:
    -   Выполнить команду для установки PostgreSQL: `sudo dnf install postgresql-server -y`.

-   Инициализация кластера баз данных:
    -   Использовать скрипт для инициализации кластера: `sudo postgresql-setup --initdb`.

-   Запуск и включение службы PostgreSQL:
    -   Запустить службу: `sudo systemctl start postgresql`.
    -   Включить службу для запуска при загрузке системы: `sudo systemctl enable postgresql`.
    -   Проверить статус службы: `sudo systemctl status postgresql`.

-   Обеспечение безопасности пользователя по умолчанию:
    -   Переключиться на учётную запись postgres: `sudo -i -u postgres`.
    -   Войти в интерфейс командной строки PostgreSQL: `psql`.
    -   Установить пароль для пользователя postgres: `\password postgres`.

-   (Опционально) Настройка удалённого доступа:
    -   Настроить правила брандмауэра: `sudo firewall-cmd --add-port=5432/tcp --permanent` и `sudo firewall-cmd --reload`.
    -   Редактировать конфигурационные файлы `postgresql.conf` и `pg_hba.conf`:
        -   В `postgresql.conf` изменить `listen_addresses = 'localhost'` на `listen_addresses = ''`.
        -   В `pg_hba.conf` добавить строку для разрешения подключений: `host all all 0.0.0.0/0 md5`.

-   Перезапуск службы PostgreSQL:
    -   После внесения изменений в конфигурацию перезапустить службу: `sudo systemctl restart postgresql`. Для установки PostgreSQL на Rocky Linux 10 выполните следующие шаги:

-   Проверьте предварительные условия:

-   у вас должен быть установлен Rocky Linux 10;
-   у вас должна быть учётная запись с правами sudo или root;
-   убедитесь в наличии стабильного интернет-соединения.

-   Обновите пакеты системы:

-   откройте терминал и выполните команду:

<!--listend-->

```nil
sudo dnf update -y
```

Это обновит все пакеты системы до последних версий и предотвратит возможные конфликты пакетов.

1.  Установите сервер PostgreSQL:

2.  PostgreSQL включён в репозиторий AppStream по умолчанию, поэтому установка будет простой. Выполните команду:

<!--listend-->

```nil
sudo dnf install postgresql-server -y
```

Эта команда установит основной сервер базы данных, клиентские библиотеки и необходимые инструменты командной строки.

1.  Инициализируйте кластер баз данных:

2.  после установки инициализируйте кластер PostgreSQL с помощью скрипта:

<!--listend-->

```nil
sudo postgresql-setup --initdb
```

После успешного выполнения вы увидите сообщение «Initializing database... OK».

1.  Запустите и включите службу PostgreSQL:

2.  запустите службу:

<!--listend-->

```nil
sudo systemctl start postgresql
```

-   включите автоматический запуск службы при загрузке системы:

<!--listend-->

```nil
sudo systemctl enable postgresql
```

-   проверьте статус службы:

<!--listend-->

```nil
sudo systemctl status postgresql
```

В выводе должно быть указано «active (running)».

1.  Обеспечьте безопасность пользователя по умолчанию:

2.  переключитесь на учётную запись postgres:

<!--listend-->

```nil
sudo -i -u postgres
```

-   войдите в интерфейс командной строки PostgreSQL:

<!--listend-->

```nil
psql
```

-   установите надёжный пароль для пользователя postgres:

<!--listend-->

```nil
\password postgres
```

Введите и подтвердите новый пароль.

-   выйдите из psql и вернитесь к обычной оболочке:

<!--listend-->

```nil
\q
exit
```

1.  (Опционально) Настройте удалённый доступ:

2.  по умолчанию PostgreSQL разрешает подключения только с локального компьютера. Для удалённого доступа нужно настроить брандмауэр и конфигурационные файлы PostgreSQL.

3.  Настройка брандмауэра:

<!--listend-->

```nil
sudo firewall-cmd --add-port=5432/tcp --permanent
sudo firewall-cmd --reload
```

Первая команда добавляет правило для разрешения трафика на порту 5432, вторая --- перезагружает брандмауэр для применения изменений.

-   Редактирование конфигурационных файлов:
    -   откройте файл postgresql.conf:

<!--listend-->

```nil
sudo nano /var/lib/pgsql/data/postgresql.conf
```

Найдите строку `#listen_addresses = 'localhost'`, удалите символ `#` и замените `localhost` на ==, чтобы PostgreSQL слушал все доступные сетевые интерфейсы.

```nil
, откройте файл pg_hba.conf:
```

```nil
sudo nano /var/lib/pgsql/data/pg_hba.conf
```

Добавьте в конец файла строку:

```nil
host all all 0.0.0.0/0 md5
```

Для повышения безопасности в рабочей среде замените `0.0.0.0/0` на конкретный IP-адрес или диапазон CIDR.

-   перезапустите службу PostgreSQL для применения изменений:

<!--listend-->

```nil
sudo systemctl restart postgresql
```

1.  Теперь у вас установлена, защищена и настроена база данных PostgreSQL на Rocky Linux 10.

Вы можете создавать конкретные базы данных, роли и пользователей в соответствии с потребностями вашего приложения.
