---
title: "CentOS 8. Изменение адресов репозиториев"
author: ["Dmitry S. Kulyabov"]
date: 2022-02-10T14:39:00+03:00
lastmod: 2025-09-10T11:24:00+03:00
tags: ["redhat", "linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "centos8-changing-repository-addresses"
---

С 31 января 2022 года установка пакетов или обновление репозиториев в CentOS8 выдаёт ошибку.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Centos 8 {#centos-8}


### <span class="section-num">1.1</span> Ошибка {#ошибка}

-   При работе с репозиториями в CentOS 8 появилась ошибка:
    ```shell
    Error: Failed to download metadata for repo 'repo_name': Cannot prepare internal mirrorlist: No URLs in mirrorlist
    ```


### <span class="section-num">1.2</span> Причины {#причины}

-   31 января 2022 года удалены все пакеты для _CentOS8_ с официальных зеркал.
-   Вызвано прекращением поддержки _CentOS8_ (см. [Замена Centos]({{< relref "2021-05-25-replacing-centos" >}})).
-   Теперь они перенесены на <https://vault.centos.org>.


### <span class="section-num">1.3</span> Устранение {#устранение}

-   Следует обновить файлы описания репозиториев в `/etc/yum.repos.d`.
-   Следует использовать `vault.centos.org` вместо `mirror.centos.org`.
-   Предлагается выполнить следующие команды:
    ```shell
    sudo sed -i -e "s|mirrorlist=|#mirrorlist=|g" -e "s|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g" -e "s|\$contentdir|centos|g" /etc/yum.repos.d/CentOS-*
    ```


## <span class="section-num">2</span> Scientific Linux 7 {#scientific-linux-7}


### <span class="section-num">2.1</span> Исправление расположения репозиториев {#исправление-расположения-репозиториев}

-   Замените записи о репозиториях:
    ```shell
    sudo sed -i -e "s|scientificlinux.org/linux/scientific/\$slreleasever|scientificlinux.org/linux/scientific/obsolete/\$slreleasever|g" -e "s|scientificlinux.org/linux/scientific/7rolling|scientificlinux.org/linux/scientific/obsolete/7rolling|g" -e "s|scientificlinux.org/linux/scientific/7x|scientificlinux.org/linux/scientific/obsolete/7x|g" /etc/yum.repos.d/sl7* /etc/yum.repos.d/sl-*
    ```
