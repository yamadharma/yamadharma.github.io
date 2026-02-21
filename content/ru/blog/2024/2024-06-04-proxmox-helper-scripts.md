---
title: "Proxmox. Вспомогательные скрипты"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-04T13:34:00+03:00
lastmod: 2025-11-20T16:00:00+03:00
tags: ["sysadmin", "linux"]
categories: ["computer-science"]
draft: false
slug: "proxmox-helper-scripts"
---

Вспомогательные скрипты для Proxmox.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Proxmox VE Helper-Scripts
-   Сайт: <https://community-scripts.github.io/ProxmoxVE/>
-   Репозиторий: <https://github.com/community-scripts/ProxmoxVE>
-   Сборник скриптов для Proxmov VE.


## <span class="section-num">2</span> Настройка сервера {#настройка-сервера}


### <span class="section-num">2.1</span> Proxmox VE Post Install {#proxmox-ve-post-install}

-   Отключение Enterprise Repo.
-   Добавление или исправление источников PVE.
-   Включение No-Subscription Repo.
-   Добавление тестового репозитория.
-   Отключение подписки nag.
-   Обновление Proxmox VE.
-   Github:
    ```shell
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/tools/pve/post-pve-install.sh)"
    ```
-   Gitea:
    ```shell
    bash -c "$(curl -fsSL https://git.community-scripts.org/community-scripts/ProxmoxVE/raw/branch/main/tools/pve/post-pve-install.sh)"
    ```


### <span class="section-num">2.2</span> Proxmox VE Processor Microcode {#proxmox-ve-processor-microcode}

-   Добавление пакета для загрузки микрокода процессора:
    ```shell
    bash -c "$(wget -qLO - https://github.com/community-scripts/ProxmoxVE/raw/main/misc/microcode.sh)"
    ```


### <span class="section-num">2.3</span> Proxmox VE CPU Scaling Governor {#proxmox-ve-cpu-scaling-governor}

-   Частота CPU регулируется в зависимости от рабочей нагрузки.
    ```shell
    bash -c "$(wget -qLO - https://github.com/community-scripts/ProxmoxVE/raw/main/misc/scaling-governor.sh)"
    ```


### <span class="section-num">2.4</span> Proxmox VE Kernel Clean {#proxmox-ve-kernel-clean}

-   Удаление неиспользуемых образов ядра.
    ```shell
    bash -c "$(wget -qLO - https://github.com/community-scripts/ProxmoxVE/raw/main/misc/kernel-clean.sh)"
    ```


### <span class="section-num">2.5</span> Proxmox Update Repositories {#proxmox-update-repositories}

-   Переписать ссылки в контейнерах LXC для нового репозиторий скриптов:
    ```shell
    bash -c "$(wget -qLO - https://github.com/community-scripts/ProxmoxVE/raw/main/misc/update-repo.sh)"
    ```


### <span class="section-num">2.6</span> Proxmox Backup Server Post Install {#proxmox-backup-server-post-install}

-   Отключение Enterprise Repo.
-   Добавление или исправление источников PVE.
-   Включение No-Subscription Repo.
-   Добавление тестового репозитория.
-   Отключение подписки nag.
    ```shell
    bash -c "$(wget -qLO - https://github.com/community-scripts/ProxmoxVE/raw/main/misc/post-pbs-install.sh)"
    ```
