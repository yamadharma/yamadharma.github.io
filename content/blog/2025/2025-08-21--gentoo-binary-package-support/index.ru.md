---
title: "Gentoo. Поддержка бинарных пакетов"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-21T11:23:00+03:00
lastmod: 2025-08-21T11:49:00+03:00
tags: ["gentoo", "linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "gentoo-binary-package-support"
---

Gentoo. Поддержка бинарных пакетов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Документация:
    -   <https://wiki.gentoo.org/wiki/Binary_package_guide/ru>


## <span class="section-num">2</span> Настройка хоста бинарных пакетов {#настройка-хоста-бинарных-пакетов}

-   Portage поддерживает несколько протоколов для загрузки бинарных пакетов: FTP, FTPS, HTTP, HTTPS и SSH/SFTP.


### <span class="section-num">2.1</span> Хост бинарных пакетов на основе веб {#хост-бинарных-пакетов-на-основе-веб}

-   Основной подход для распространения бинарных пакетов это создать хост бинарных пакетов на основе веб.


#### <span class="section-num">2.1.1</span> Caddy {#caddy}

-   Установка:
    ```shell
    emerge www-servers/caddy
    ```
-   Конфигурация (файл `/etc/caddy/Caddyfile`):

<!--listend-->

```conf-unix
:80 {
    root * /com/lib/portage/packages
    file_server browse
}
```

-   Запустите для проверки:
    ```shell
    caddy run --config /etc/caddy/Caddyfile
    ```
-   Запустите сервис:
    ```shell
    systemctl enable --now caddy.service
    ```

-   На клиентских системах настройте переменную `PORTAGE_BINHOST` в файле `/etc/portage/make.conf`:

<!--listend-->

```conf-unix
PORTAGE_BINHOST="http://binhost.example.com/packages"
```


### <span class="section-num">2.2</span> Экспорт из NFS {#экспорт-из-nfs}

-   В случае использования хоста бинарных пакетов во внутренней сети, может быть проще экспортировать пакеты с помощью NFS, а затем смонтировать их на клиенте.
-   Файл `/etc/exports` может выглядеть так:

<!--listend-->

```conf-unix
/var/cache/binpkgs   2001:db8:81::/48(ro,no_subtree_check,root_squash) 192.168.100.0/24(ro,no_subtree_check,root_squash)
```

-   На клиентах можно смонтировать каталог.
-   Пример записи в файле /etc/fstab:

<!--listend-->

```conf-unix
binhost:/var/cache/binpkgs      /var/cache/binpkgs    nfs    defaults    0 0
```

-   В файле `/etc/portage/make.conf` установите:

<!--listend-->

```bash
PKGDIR="/var/cache/binpkgs"
```

-   Если PKGDIR смонтирован в сети, может быть полезно включить `FEATURES="pkgdir-index-trusted"`.
-   Эта функция отключает проверку всего `PKGDIR` на предмет добавленных или удалённых пакетов и вместо этого доверяет содержимому `Packages`.
