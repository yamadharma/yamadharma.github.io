---
title: "Linux. Подсистема Live Update Orchestrator"
author: ["Dmitry S. Kulyabov"]
date: 2026-02-15T20:29:00+03:00
lastmod: 2026-02-19T11:06:00+03:00
tags: ["sysadmin", "linux"]
categories: ["computer-science"]
draft: false
slug: "linux-live-update-orchestrator"
---

Linux. Подсистема Live Update Orchestrator

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Live Update Orchestrator (LUO) позволяет заменять ядро без перегрузки.


## <span class="section-num">2</span> Настройка конфигурации ядра {#настройка-конфигурации-ядра}

-   Используйте конфигурацию текущего ядра как основу:
    ```shell
    cd /usr/src/linux
    # Если есть работающая конфигурация
    zcat /proc/config.gz > .config 2>/dev/null || cp /boot/config-* .config
    ```

-   Теперь включите необходимые параметры:
    ```shell
    make menuconfig
    ```

-   Включите следующие опции (их можно найти через поиск `/`):
    -   CONFIG_LIVEUPDATE --- основная поддержка LUO (находится в разделе «General setup» → «Live Update Orchestrator»)
    -   CONFIG_KEXEC_HANDOVER --- фреймворк передачи состояния (KHO), необходимый для LUO
    -   CONFIG_KEXEC_HANDOVER_DEBUG (опционально, для отладки)
    -   Также убедитесь, что включены CONFIG_KEXEC и CONFIG_KEXEC_FILE (обычно включены по умолчанию)

-   Можно добавить вручную в файл `.config`:
    ```shell
    echo "CONFIG_LIVEUPDATE=y" >> .config
    echo "CONFIG_KEXEC_HANDOVER=y" >> .config
    make olddefconfig   # чтобы обновить конфигурацию и разрешить зависимости
    ```
