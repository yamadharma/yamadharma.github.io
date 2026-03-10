---
title: "KVM. QEMU Guest Agent"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-05T16:18:00+03:00
lastmod: 2025-12-11T15:08:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "kvm-qemu-guest-agent"
---

KVM. QEMU Guest Agent.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Программа-демон, которая устанавливается на ВМ.
-   Обеспечивает выполнение команд на ВМ и обмен информацией между ВМ и узлом кластера.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Деривативы Redhat {#деривативы-redhat}

-   Установка:
    ```shell
    sudo dnf -y install qemu-guest-agent
    ```
-   Включите службу:
    ```shell
    sudo systemctl enable --now qemu-guest-agent
    ```


### <span class="section-num">2.2</span> Деривативы Debian {#деривативы-debian}

-   Установка:
    ```shell
    sudo apt install qemu-guest-agent
    ```
-   Включите службу:
    ```shell
    sudo systemctl enable --now qemu-guest-agent
    ```


## <span class="section-num">3</span> Проверка работы {#проверка-работы}


### <span class="section-num">3.1</span> Proxmox {#proxmox}

-   В консоли Proxmox выполните команду:
    ```shell
    qm agent <vmid> ping
    ```
-   В случае, если гостевые средства интеграции доступы эта команда возвращает пустой вывод.
-   Если средства интеграции не доступны, то должна отобразиться ошибка.


### <span class="section-num">3.2</span> libvirt {#libvirt}

-   В консоли выполните команду:
    ```shell
    virsh qemu-agent-command <vm_id>_<vm_name> '{"execute": "guest-info", "arguments": {}}'
    ```
