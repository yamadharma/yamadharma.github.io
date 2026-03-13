---
title: "Proxmox Backup Server"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-04T14:02:00+03:00
lastmod: 2025-08-19T20:35:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "proxmox-backup-server"
---

Proxmox Backup Server.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.proxmox.com>


### <span class="section-num">1.1</span> Требования {#требования}

-   Минимальные требования к серверу (предназначены только для тестирования):
    -   CPU: 64bit (x86-64 или AMD64), 2+ Ядра
    -   ОЗУ: 2 ГБ
    -   Диск: от 8 ГБ
    -   Сеть: 1 интерфейс
-   Рекомендуемые требования к серверу:
    -   CPU: 64bit, 4 Ядра
    -   ОЗУ: 4 ГБ (+1 ГБ на каждый ТБ дискового пространства)
    -   Диск: от 32 ГБ + резервное хранилище
    -   Сеть: 1 интерфейс + резервирование


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Отдельный пакет {#отдельный-пакет}

-   Установие сервер PBS:
    ```shell
    apt-get install proxmox-backup-server
    ```
-   Запустите и добавьте в автозагрузку Proxmox Backup API Proxy Server:
    ```shell
    systemctl enable --now proxmox-backup-proxy.service
    ```
-   Служба `proxmox-backup-proxy` предоставляет API Proxmox Backup Server через TCP-порт 8007 с использованием HTTPS. Операции, требующие дополнительных разрешений, перенаправляются в локальную службу `proxmox-backup`.
-   Служба `proxmox-backup` предоставляет API управления Proxmox Backup Server по адресу 127.0.0.1:82. Она имеет разрешение на выполнение всех привилегированных операций.
-   Установите клиент PBS:
    ```shell
    apt-get install proxmox-backup-client
    ```


### <span class="section-num">2.2</span> Контейнер LXC {#контейнер-lxc}

-   Запустите в консоли Proxmox VE:
    ```shell
    bash -c "$(wget -qLO - https://github.com/community-scripts/ProxmoxVE/raw/main/ct/proxmox-backup-server.sh)"
    ```


### <span class="section-num">2.3</span> Виртуальная машина {#виртуальная-машина}

-   Создадим виртуальную машину:
    ```shell
    qm create 150 --name pbs --memory 16000 --cores 4 --sockets 1 --net0 virtio,bridge=vmbr1,firewall=1,mtu=1,tag=12
    ```

    -   `tag` задаёт используемый vlan.
-   Подключим QEMU Guest Agent (см. [KVM. QEMU Guest Agent]({{< relref "2024-09-05-kvm-qemu-guest-agent" >}})):
    ```shell
    qm set 150 --agent enabled=1,fstrim_cloned_disks=1
    ```
-   Создадим диск (80GB):
    ```shell
    pvesm alloc local-lvm 150 vm-150-disk-0 80G
    ```
-   Зададим драйвер диска:
    ```shell
    qm set 150 --scsihw virtio-scsi-single
    ```
-   Подключим диск:
    ```shell
    qm set 150 --virtio0 local-lvm:vm-150-disk-0
    ```
-   Подключим CDROM:
    ```shell
    qm set 150 --ide2 local:iso/proxmox-backup-server_3.3-1.iso,media=cdrom
    ```
-   Зададим порядок загрузки (CD-ROM, затем диск)
    ```shell
    qm set 150 --boot c --bootdisk virtio0
    qm set 150 --boot order='ide2;virtio0'
    ```
-   Зададим тип CPU:
    ```shell
    qm set 150 --cpu cputype=host
    ```
-   Подключим для мышки:
    ```shell
    qm set 150 --tablet 1
    ```
-   Запустите виртуальную машину и установите систему.


## <span class="section-num">3</span> Настройка после установки {#настройка-после-установки}


### <span class="section-num">3.1</span> Повышение комфорта работы {#повышение-комфорта-работы}

-   Обновите список програм:
    ```shell
    apt update
    ```
-   Программы для удобства работы в консоли:
    ```shell
    apt -y install tmux mc
    ```
-   Программы мониторинга:
    ```shell
    apt -y install htop lsof
    ```
-   Утилита для ssh:
    ```shell
    apt -y install mosh
    ```
-   Удобство работы с bash:
    ```shell
    apt -y install bash-completion
    ```
-   Разные утилиты:
    ```shell
    apt -y install p7zip-full git
    ```
-   Для удалённой работы с kitty:
    ```shell
    apt -y install kitty-terminfo kitty-shell-integration
    ```
-   Установите qemu-guest-agent:
    ```shell
    apt -y install qemu-guest-agent
    ```
-   Запустите qemu-guest-agent:
    ```shell
    systemctl enable --now qemu-guest-agent
    ```


### <span class="section-num">3.2</span> Скрипты для тьюнинга (см. [Proxmox. Вспомогательные скрипты]({{< relref "2024-06-04-proxmox-helper-scripts" >}})) {#скрипты-для-тьюнинга--см-dot-proxmox-dot-вспомогательные-скрипты--dot-dot-notes-public-20240604133400-proxmox-вспомогательные-скрипты-dot-md}

-   Proxmox Backup Server Post Install
    ```shell
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/tools/pve/post-pbs-install.sh)"
    ```


### <span class="section-num">3.3</span> Обновление {#обновление}

-   Обновите систему:
    ```shell
    apt update
    apt -y upgrade
    ```


### <span class="section-num">3.4</span> Безопасность {#безопасность}

-   Установите и настройте fail2ban (см. [fail2ban. Основные настройки]({{< relref "2023-10-30-fail2ban-basic-settings" >}})):
    ```shell
    apt install fail2ban
    ```
-   После настройки запустите его:
    ```shell
    systemctl enable --now fail2ban
    ```


## <span class="section-num">4</span> Подключение {#подключение}


### <span class="section-num">4.1</span> Веб-интерфейс {#веб-интерфейс}

-   PBS предлагает интегрированный веб-интерфейс для управления сервером.
-   Веб-интерфейс PBS доступен по адресу <https://<ip-адрес|имя>:8007>.
-   Потребуется пройти аутентификацию (логин по умолчанию: root, пароль указывается в процессе установки).


## <span class="section-num">5</span> Хранилище {#хранилище}


### <span class="section-num">5.1</span> Хранилище данных {#хранилище-данных}

-   Хранилище данных --- это место, где хранятся резервные копии.
-   Текущая реализация PBS использует каталог внутри стандартной файловой системы (ext4, xfs или zfs) для хранения данных резервного копирования.
-   Информация о конфигурации для хранилищ данных хранится в файле `/etc/proxmox-backup/datastore.cfg`.
-   Необходимо настроить как минимум одно хранилище данных.


#### <span class="section-num">5.1.1</span> Добавление диска {#добавление-диска}

-   Если установка выполнялась как виртуальная машина, добавим диск в Proxmox VE:
    ```shell
    pvesm alloc local-lvm 150 vm-150-disk-1 2000G
    ```
-   Подключим диск:
    ```shell
    qm set 150 --virtio1 local-lvm:vm-150-disk-1
    ```


#### <span class="section-num">5.1.2</span> Создание хранилища данных {#создание-хранилища-данных}

-   Увидеть диски, подключенные к системе, можно в веб-интерфейсе «Управление» → «Хранилище/Диски».
-   Просмотр списка дисков в командной строке:
    ```shell
    proxmox-backup-manager disk list
    ```
-   Для создания хранилища в веб-интерфейсе, необходимо нажать кнопку «Добавить хранилище данных» в боковом меню в разделе «Хранилище данных». В открывшемся окне необходимо указать:
    -   «Имя» — название хранилища данных;
    -   «Путь к каталогу хранилища» — путь к каталогу, в котором будет создано хранилище данных;
    -   «Расписание сборщика мусора» — частота, с которой запускается сборка мусора;
    -   «Расписание удаления» — частота, с которой происходит удаление ранее созданных резервных копий;
    -   «Параметры удаления» — количество резервных копий, которые необходимо хранить.

-   Создадим хранилище:
    ```bash
    proxmox-backup-manager disk fs create store1 --disk vdb --filesystem ext4 --add-datastore true
    ```
-   Хранилище данных будет создано по адресу `/mnt/datastore/store1`.

-   После создания хранилища данных по умолчанию появляется следующая структура каталогов:
    ```shell
    # ls -arilh /mnt/datastore/store1
    итого 1,1M
    665243 -rw-r--r-- 1 backup backup    0 мар 31 14:05 .lock
    665242 drwxr-x--- 1 backup backup 1,1M мар 31 14:05 .chunks
    665240 drwxr-xr-x 3 root   root   4,0K мар 31 13:56 ..
    665241 drwxr-xr-x 3 backup backup 4,0K мар 31 14:05
    ```

    -   `.lock` --- пустой файл, используемый для блокировки процесса;
    -   каталог `.chunks` содержит подкаталоги, с именами от 0000 до ffff. В этих каталогах будут храниться фрагментированные данные, после выполнения операции резервного копирования.


#### <span class="section-num">5.1.3</span> Управление хранилищами данных {#управление-хранилищами-данных}

-   Вывести список существующих хранилищ данных:
    ```shell
    proxmox-backup-manager datastore list
    ```
-   Изменить расписание сборки мусора и вывести свойства хранилища данных:
    ```shell
    proxmox-backup-manager datastore update store2 --gc-schedule 'Tue 04:27'
    ```
-   Просмотреть информацию:
    ```shell
    proxmox-backup-manager datastore show store1
    ```
-   Удалить хранилище данных:
    ```shell
    proxmox-backup-manager datastore remove store1
    ```
-   Данная команда удалит только конфигурацию хранилища данных, данные из базового каталога удалены не будут.


#### <span class="section-num">5.1.4</span> Очистка хранилища {#очистка-хранилища}

-   [Ротирование бэкапов]({{< relref "2025-03-11--backup-rotation" >}})
-   _GC Schedule_ --- периодичность выполнения сборки мусора, фактически выполняет задачу дедупликации.
-   Prune Schedule --- периодичность очистки хранилища от устаревших резервных копий.
-   Опции очистки устаревших копий (Prune Options) можно настроить как сразу, так и потом, либо изменить в любое удобное время.
-   Задание очистки обрабатывает опции, в порядке перечисления, уже обработанные копии из дальнейшей обработки исключаются:
    -   _Keep Last &lt;N&gt;_ : хранить последние &lt;N&gt; снимки резервных копий;
    -   _Keep Hourly &lt;N&gt;_ : хранить резервные копии за последние &lt;N&gt; часов (если за один час создаётся более одной резервной копии, сохраняется только последняя);
    -   _Keep Daily &lt;N&gt;_ : хранить резервные копии за последние &lt;N&gt; дней (если за один день создаётся более одной резервной копии, сохраняется только последняя);
    -   _Keep Weekly &lt;N&gt;_ : хранить резервные копии за последние &lt;N&gt; недель (недели начинаются в понедельник и заканчиваются в воскресенье; если за одну неделю создаётся более одной резервной копии, сохраняется только последняя);
    -   _Keep Monthly &lt;N&gt;_ : хранить резервные копии за последние &lt;N&gt; месяцев (если за один месяц создаётся более одной резервной копии, сохраняется только последняя);
    -   _Keep Yearly &lt;N&gt;_ : хранить резервные копии за последние &lt;N&gt; лет (если за один год создаётся более одной резервной копии, сохраняется только самая последняя).
-   Если за один период создаётся более одной резервной копии, сохраняется только последняя.
-   Визуализировать заданное расписание можно с помощью симулятора очистки (<https://pbs.proxmox.com/docs/prune-simulator/>).
-   Безусловное удаление конкретного бэкапа можно осуществить, выполнив:
    ```shell
    proxmox-backup-client forget <snapshot>
    ```

    -   Выполнение команды приведёт к необратимому удалению архивов бэкапа.
-   Условное удаление:
    ```shell
    proxmox-backup-client prune <group> <option1>..<optionN>
    ```

    -   `<group>` : название группы бэкапов;
    -   `<options>` :
        -   `--keep-last <N>` : оставит последние &lt;N&gt; резервных копий;
        -   `--keep-hourly <N>` :  оставит резервные копии за последние &lt;N&gt; часов;
        -   `--keep-daily <N>` : оставит резервные копии за последние &lt;N&gt; дней;
        -   `--keep-weekly <N>` : оставит резервные копии за последние &lt;N&gt; недель;
        -   `--keep-monthly <N>` : оставит резервные копии за последние &lt;N&gt; месяцев;
        -   `--keep-yearly <N>` : оставит резервные копии за последние &lt;N&gt; лет.


## <span class="section-num">6</span> Пользователи {#пользователи}


### <span class="section-num">6.1</span> Управление пользователями {#управление-пользователями}

-   PBS хранит данные пользователей в файле `/etc/proxmox-backup/user.cfg`.
-   Пользователя внутренне идентифицируют по его имени и области аутентификации в форме `<user>@<realm>`.
-   После установки PBS существует один пользователь `root@pam`, который соответствует суперпользователю ОС.
-   Этого пользователя нельзя удалить, все системные письма будут отправляться на адрес электронной почты, назначенный этому пользователю.
-   Суперпользователь имеет неограниченные права, поэтому рекомендуется добавить других пользователей с меньшими правами.


#### <span class="section-num">6.1.1</span> Области аутентификации {#области-аутентификации}

-   PBS поддерживает следующие области (методы) аутентификации:
    -   Стандартная аутентификация Linux PAM (Linux PAM standart authentication) --- пользователь аутентифицируется с помощью своего обычного системного пароля;
    -   Сервер аутентификации Proxmox Backup (Proxmox Backup authentication server) --- аутентификация Proxmox Backup Server. Хэшированные пароли хранятся в файле `/etc/proxmox-backup/shadow.json`;
    -   Сервер LDAP --- позволяет использовать внешний LDAP-сервер для аутентификации пользователей (например, OpenLDAP);
    -   Сервер OpenID Connect --- уровень идентификации поверх протокола OATH 2.0. Позволяет аутентифицировать пользователей на основе аутентификации, выполняемой внешним сервером авторизации.


#### <span class="section-num">6.1.2</span> Стандартная аутентификация Linux PAM {#стандартная-аутентификация-linux-pam}

-   При использовании аутентификации Linux PAM системный пользователь должен существовать (должен быть создан, например, с помощью команды adduser).
-   Область Linux PAM создается по умолчанию и не может быть удалена.


#### <span class="section-num">6.1.3</span> Сервер аутентификации Proxmox Backup {#сервер-аутентификации-proxmox-backup}

-   Область аутентификации PBS представляет собой хранилище паролей в стиле Unix (`/etc/proxmox-backup/shadow.json`). Пароль шифруется с использованием метода хеширования SHA-256.
-   Область создается по умолчанию.
-   Для добавления пользователя в веб-интерфейсе, следует в веб-интерфейсе перейти в раздел «Конфигурация» → «Управление доступом» и на вкладке «Управление пользователями» нажать кнопку «Добавить».
-   Управление пользователями в консоли:
    -   просмотреть список пользователей:
        ```shell
        proxmox-backup-manager user list
        ```
    -   создать пользователя:
        ```shell
        proxmox-backup-manager user create backup_u@pbs --email backup_u@example.com
        ```
    -   обновить или изменить любые свойства пользователя:
        ```shell
        proxmox-backup-manager user update backup_u@pbs --firstname Дмитрий --lastname Иванов
        ```
    -   отключить учетную запись пользователя:
        ```shell
        proxmox-backup-manager user update backup_u@pbs --enable 0
        ```
    -   удалить учетную запись пользователя:
        ```shell
        proxmox-backup-manager user remove backup_u@pbs
        ```


### <span class="section-num">6.2</span> API-токены {#api-токены}

-   Любой аутентифицированный пользователь может генерировать API-токены, которые, в свою очередь, можно использовать для настройки клиентов вместо прямого ввода имени пользователя и пароля.
-   API-токены служат двум целям:
    -   простой отзыв в случае компрометации клиента;
    -   возможность ограничить разрешения для каждого клиента/токена в рамках разрешений пользователей.
-   API-токен состоит из двух частей: идентификатора, состоящего из имени пользователя, области и имени токена (`user@realm!имя токена`), и секретного значения.
-   Можно создать API-токен в веб-интерфейсе.
-   Создание API-токена в консоли:
    ```bash
    proxmox-backup-manager user generate-token backup_u@pbs client1
    ```
-   Отображаемое секретное значение необходимо сохранить, так как после создания токена его нельзя будет отобразить снова.


### <span class="section-num">6.3</span> Контроль доступа {#контроль-доступа}

-   По умолчанию новые пользователи и API-токены не имеют никаких разрешений.
-   Добавить разрешения можно, назначив роли пользователям/токенам на определённых объектах, таких как хранилища данных или удалённые устройства.
-   PBS использует систему управления разрешениями на основе ролей и путей.
-   Запись в таблице разрешений позволяет пользователю играть определённую роль при доступе к объекту или пути.
-   Это означает, что такое правило доступа может быть представлено как тройка (путь, пользователь, роль) или (путь, API-токен, роль), причем роль содержит набор разрешенных действий, а путь представляет цель этих действий.
-   Информация о правах доступа хранится в файле `/etc/proxmox-backup/acl.cfg`.
-   Файл содержит 5 полей, разделенных двоеточием (`:`):
    ```conf-unix
    acl:1:/datastore:backup_u@pbs!client1:DatastoreAdmin
    ```
-   В каждом поле представлены следующие данные:
    -   идентификатор acl;
    -   1 или 0 – включено или отключено;
    -   объект, на который установлено разрешение;
    -   пользователи/токены, для которых установлено разрешение;
    -   устанавливаемая роль.
-   Добавить разрешение можно в веб-интерфейсе («Конфигурация» → «Управление доступом» вкладка «Разрешения»).
-   Добавление разрешения в консоли (добавить пользователя `backup_u@pbs` в качестве администратора хранилища данных для хранилища данных= store1=, расположенного в `/mnt/datastore/store1`):
    ```shell
    proxmox-backup-manager acl update /datastore/store1 DatastoreAdmin --auth-id backup_u@pbs
    ```
-   Вывести список разрешений:
    ```shell
    proxmox-backup-manager acl list
    ```
-   Отобразить действующий набор разрешений пользователя или API-токена:
    ```shell
    proxmox-backup-manager user permissions backup_u@pbs --path /datastore/store1
    ```


## <span class="section-num">7</span> Управление удалёнными PBS {#управление-удалёнными-pbs}

-   Хранилища данных с удалённого сервера можно синхронизировать с локальным хранилищем с помощью задачи синхронизации.
-   Информация о конфигурации удалённых PBS хранится в файле `/etc/proxmox-backup/remote.cfg`.
-   Для добавления удалённого PBS в веб-интерфейсе следует перейти в раздел «Конфигурация» → «Удалённые хранилища» и нажать кнопку «Добавить».
-   Отпечаток TLS-сертификата можно получить на удалённом PBS в веб-интерфейсе.
-   Отпечаток TLS-сертификата можно получить на удалённом PBS в командной строке:
    ```shell
    proxmox-backup-manager cert info | grep Fingerprint
    ```
-   Управление удалёнными PBS в консоли:
    -   добавить удалённый PBS:
        ```shell
        proxmox-backup-manager remote create pbs2 --host pbs2.example.com --userid root@pam --password 'SECRET' --fingerprint 42:5d:ff:3a:50:38:53:5a:9b:f7:50:...:ab:1b
        ```
    -   вывести список удалённых PBS:
        ```shell
        proxmox-backup-manager remote list
        ```
    -   удалить удалённый PBS:
        ```shell
        proxmox-backup-manager remote remove pbs2
        ```

-   Для настройки задачи синхронизации необходимо в разделе «Хранилище данных» перейти на вкладку «Задания синхронизации» и нажать кнопку «Добавить».
-   Управление задачами синхронизации в консоли:
    -   добавить задачу синхронизации:
        ```shell
        proxmox-backup-manager sync-job create test_job --remote pbs2 --remote-store remotestore --store zfs_st --schedule 'Sat 18:15'
        ```
    -   вывести список задач синхронизации:
        ```shell
        proxmox-backup-manager sync-job list
        ```
    -   изменить задачу синхронизации:
        ```shell
        proxmox-backup-manager sync-job  update test_job --comment 'offsite'
        ```
    -   удалить задачу синхронизации:
        ```shell
        proxmox-backup-manager sync-job remove test_job
        ```
-   После создания задания синхронизации оно будет запускаться по заданному расписанию, также его можно запустить вручную из веб-интерфейса (кнопка «Запустить сейчас»).


## <span class="section-num">8</span> Клиент резервного копирования {#клиент-резервного-копирования}

-   Клиент резервного копирования использует следующий формат для указания репозитория хранилища данных на сервере резервного копирования (где имя пользователя указывается в виде user@realm):
    ```shell
    [[username@]server[:port]:]datastore
    ```
-   Значение по умолчанию для имени пользователя: `root@pam`.
-   Если сервер не указан, используется локальный хост: `localhost`.
-   Указать репозиторий можно, передав его в параметре `--repository`, или установив переменную среды `PBS_REPOSITORY`:
    ```shell
    export PBS_REPOSITORY=pbs.example.com:store1
    ```


### <span class="section-num">8.1</span> Создание резервной копии {#создание-резервной-копии}

-   Создать резервную копию домашнего каталога пользователя user (будет создан архив `user.pxar`):
    ```shell
    proxmox-backup-client backup user.pxar:/home/user/ --repository store1
    ```
-   Распространёнными типами архивов являются `.pxar` для файловых архивов и `.img` для образов блочных устройств.
-   Команда создания резервной копии блочного устройства:
    ```shell
    proxmox-backup-client backup mydata.img:/dev/mylvm/mydata
    ```


#### <span class="section-num">8.1.1</span> Шифрование {#шифрование}

-   PBS поддерживает шифрование на стороне клиента с помощью AES-256 в режиме GCM.
-   Создать ключ шифрования:
    ```shell
    proxmox-backup-client key create my-backup.key
    ```
-   Создание зашифрованной резервной копии:
    ```shell
    proxmox-backup-client backup user_s.pxar:/home/user/ --repository pbs.example.com:store1 --keyfile ./my-backup.key
    ```


### <span class="section-num">8.2</span> Восстановление данных {#восстановление-данных}

-   Список всех снимков на сервере:
    ```shell
    proxmox-backup-client snapshot list --repository pbs.example.com:store1
    ```
-   Просмотреть содержимое снимка:
    ```shell
    proxmox-backup-client catalog dump host/pbs/2023-09-15T15:00:37Z --repository pbs.example.com:store1
    ```
-   Команда восстановления позволяет восстановить один архив из резервной копии:
    ```shell
    proxmox-backup-client restore host/pbs/2023-09-15T15:00:37Z user.pxar /target/path/ --repository pbs.example.com:store1

    ```
-   Получить содержимое любого архива можно, восстановив файл `index.json` в репозитории по целевому пути `-`.
-   Это выведет содержимое архива на стандартный вывод:
    ```shell
    proxmox-backup-client restore host/pbs/2023-09-15T15:00:37Z index.json - --repository pbs.example.com:store1
    ```
-   Если необходимо восстановить несколько отдельных файлов, можно использовать интерактивную оболочку восстановления:
    ```shell
    proxmox-backup-client catalog shell host/host-01/2023-09-17T14:17:16Z user.pxar --repository pbs.example.com:store1
    ```


### <span class="section-num">8.3</span> Вход и выход {#вход-и-выход}

-   При первой попытке получить доступ к серверу с использованием команды `proxmox-backup-client` потребуется ввести пароль пользователя.
-   Сервер проверяет учётные данные и отправляет билет, действительный в течение двух часов.
-   Клиент использует этот билет для последующих запросов к этому серверу.
-   Можно вручную инициировать вход/выход.
-   Команда входа:
    ```shell
    proxmox-backup-client login --repository pbs.example.com:store1
    ```
-   Удалить билет:
    ```shell
    proxmox-backup-client logout --repository pbs.example.com:store1
    ```


## <span class="section-num">9</span> Интеграция с PVE {#интеграция-с-pve}

-   Proxmox Backup Server можно интегрировать в автономную или кластерную установку PVE, добавив его в качестве хранилища в PVE.
-   Для создания нового хранилища типа «Proxmox Backup Server» необходимо выбрать «Центр обработки данных» → «Хранилище», нажать кнопку «Добавить» и в выпадающем меню выбрать пункт «Proxmox Backup Server».
-   Отпечаток TLS-сертификата можно получить в веб-интерфейсе сервера резервного копирования.
-   Отпечаток TLS-сертификата можно получить, выполнив следующую команду на сервере резервного копирования:
    ```bash
    proxmox-backup-manager cert info | grep Fingerprint
    ```
-   Добавление хранилища в командной строке:
    ```bash
    pvesm add pbs pbs_backup --server pbs.example.com --datastore store2 --fingerprint  c8:26:af:4a:c3:dc:60:72:...:99:a5 --username root@pam --password
    ```
-   Просмотреть состояние хранилища:
    ```shell
    pvesm status --storage pbs_backup
    ```
-   Добавив хранилище данных типа «Proxmox Backup Server» в PVE, можно создавать резервные копии ВМ и контейнеров в это хранилище, так же как и в любые другие хранилища.


## <span class="section-num">10</span> Обновление {#обновление}


### <span class="section-num">10.1</span> 3 → 4 {#3-4}

-   Документация: <https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4>
-   Проверить версию:
    -   Команда `proxmox-backup-manager versions` выдаст версию 3.4.2 (или выше).
-   Сделайте резервную копию `/etc/proxmox-backup` чтобы гарантировать, что в худшем случае можно будет восстановить любую соответствующую конфигурацию:

<!--listend-->

```shell
tar czf "pbs3-etc-backup-$(date -I).tar.gz" -C "/etc" "proxmox-backup"
```

-   Убедитесь, что в корневой точке монтирования имеется не менее 10 ГБ свободного места на диске:

<!--listend-->

```shell
df -h /
```

-   Программа `pbs3to4` выводит подсказки и предупреждения о потенциальных проблемах:

<!--listend-->

```shell
pbs3to4
```

-   Чтобы запустить её со всеми включенными проверками, выполните:

<!--listend-->

```shell
pbs3to4 --full
```

-   Обновите все записи репозитория для Trixie:

<!--listend-->

```shell
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
```

-   Обновите корпоративный репозиторий до Trixie в новом формате deb822 с помощью следующей команды (не надо делать):
    ```shell
    cat > /etc/apt/sources.list.d/pbs-enterprise.sources << EOF
    Types: deb
    URIs: https://enterprise.proxmox.com/debian/pbs
    Suites: trixie
    Components: pbs-enterprise
    Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
    EOF
    ```
-   Подключите репозиторий:
    ```shell
    cat > /etc/apt/sources.list.d/proxmox.sources << EOF
    Types: deb
    URIs: http://download.proxmox.com/debian/pbs
    Suites: trixie
    Components: pbs-no-subscription
    Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
    EOF
    ```

-   Проверьте, подключились ли репозитории:
    ```shell
    apt update
    apt policy
    ```
-   Обновите систему:
    ```shell
    apt update
    apt dist-upgrade
    ```
-   Перегрузитесь:
    ```shell
    systemctl reboot
    ```
-   Проверьте статус сервиса:
    ```shell
    systemctl status proxmox-backup-proxy.service proxmox-backup.service
    ```
-   Перенести существующие источники репозитория в рекомендуемый формат стиля deb822:
    ```shell
    apt modernize-sources
    ```
