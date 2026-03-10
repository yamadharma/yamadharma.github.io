---
title: "Виртуализация. Virt-manager"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-26T14:08:00+03:00
lastmod: 2024-11-26T14:50:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "virtualization-virt-manager"
---

Виртуализация. Virt-manager.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://virt-manager.org/>
-   Репозиторий: <https://github.com/virt-manager/virt-manager>
-   Графический пользовательский интерфейс для управления виртуальными машинами и контейнерами через библиотеку libvirt.
-   Virt-manager в основном предназначен для работы с виртуальными машинами KVM, но также может работать с Xen и LXC.
-   Встроенные программы просмотра клиентов VNC и SPICE.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   В основном репозитории:
    ```shell
    emerge app-emulation/virt-manager
    ```
