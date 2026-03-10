---
title: "Настройка NFS"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-17T20:16:00+03:00
lastmod: 2025-08-17T20:58:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "nfs-setting"
---

Настройка NFS.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Установка {#установка}

-   Debian
    ```shell
    sudo apt install nfs-kernel-server
    ```
-   RHEL
    ```shell
    sudo dnf -y install nfs-utils
    ```


## <span class="section-num">2</span> Настройка NFS-сервера {#настройка-nfs-сервера}

-   Запустите службу `nfs-server`:
    ```shell
    sudo systemctl enable --now nfs-server.service
    sudo systemctl status nfs-server.service
    ```

-   Создайте корневую директорию NFSv4:
    ```shell
    sudo mkdir -p /srv/nfs4
    ```

-   Подготовьте экспортируемые каталоги:
    ```shell
    sudo mkdir /srv/nfs4/data
    sudo chown nobody:nogroup /srv/nfs4/data  # Для безопасности
    ```

-   Настройте привязку каталогов (bind mounts):
    ```shell
    sudo mount --bind /путь/к/вашим/данным /srv/nfs4/data
    ```

-   Для постоянного монтирования добавьте в `/etc/fstab`:
    ```conf-unix
    /путь/к/вашим/данным /srv/nfs4/data none bind 0 0
    ```

-   Настройте экспорт в `/etc/exports`:
    ```conf-unix
    /srv/nfs4        192.168.1.0/24(rw,sync,fsid=0,crossmnt,no_subtree_check)
    /srv/nfs4/data   192.168.1.0/24(rw,sync,no_root_squash,all_squash,anonuid=1000,anongid=1000)
    ```

    -   `fsid=0` : корневая директория NFSv4.
    -   `crossmnt` : разрешает доступ к вложенным каталогам.
    -   `all_squash` : отображает всех пользователей в анонимного (nobody).
    -   `no_all_squash` : отображение всех UID и GID из клиентских запросов на идентичные UID и GID на сервере NFS.
    -   `anonuid`, `anongid` : задают UID/GID для анонимного пользователя.
    -   `no_root_squash` : по умолчанию пользователь `root` на клиентской машине не будет иметь доступа к разделяемой директории сервера. Этой опцией мы снимаем это ограничение.
    -   `sync` : запись данных перед подтверждением.
    -   `sec=krb5` : использовать Kerberos для аутентификации.
    -   `nohide` : NFS автоматически не показывает нелокальные ресурсы (например, примонтированные с помощью `mount –o bind`), эта опция включает отображение таких ресурсов.

<!--listend-->

-   Примените настройки:
    ```shell
    sudo exportfs -arv
    sudo systemctl restart nfs-server
    ```

-   Настройте firewall:
    -   Debian
        ```shell
        sudo ufw allow 2049/tcp
        ```
    -   RHEL
        ```shell
        sudo firewall-cmd --add-service=nfs --permanent
        sudo firewall-cmd --permanent --add-service=rpc-bind
        sudo firewall-cmd --permanent --add-service=mountd
        sudo firewall-cmd --reload
        ```


## <span class="section-num">3</span> Настройка NFS-клиента {#настройка-nfs-клиента}

-   Установите пакеты
    -   Debian
        ```shell
        sudo apt install nfs-common
        ```
    -   RHEL
        ```shell
        sudo dnf install nfs-utils
        ```

-   Создайте точку монтирования:
    ```shell
    sudo mkdir -p /mnt/nfs/data
    ```

-   Смонтируйте NFS-ресурс:
    ```shell
    sudo mount -t nfs4 -o vers=4.2 192.168.1.10:/data /mnt/nfs/data
    ```

    -   `vers=4.2` : явное указание версии NFSv4.2 (не обязательно).

-   Для постоянного монтирования добавьте в `/etc/fstab`:
    ```conf-unix
    192.168.1.10:/data  /mnt/nfs/data  nfs4  vers=4.2,rw,hard,intr,_netdev  0  0
    ```


## <span class="section-num">4</span> Домен {#домен}

-   По умолчанию доменная часть строки представляет собой DNS-имя домена системы.
-   Его также можно указать в файле `/etc/idmapd.conf`, если система многодомная или если DNS-имя домена системы не совпадает с именем области Kerberos системы:
    ```conf-unix
    [General]
    Domain = guestdomain.tld
    ```
-   Если домен не указан в файле `/etc/idmapd.conf`, локальный DNS-сервер будет запрошен на наличие текстовой записи `_nfsv4idmapdomain`.
-   Если запись существует, она будет использована в качестве домена. Если запись отсутствует, будет использована доменная часть DNS-домена.
-   Вывести эффективное доменное имя NFSv4 системы на стандартный вывод:

<!--listend-->

```shell
nfsidmap -d
```


## <span class="section-num">5</span> Проверка работы {#проверка-работы}

-   На сервере: `sudo showmount -e`
-   На клиенте: `df -hT | grep nfs4`
