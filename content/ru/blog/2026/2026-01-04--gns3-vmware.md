---
title: "GNS3 на vmWare"
author: ["Dmitry S. Kulyabov"]
date: 2026-01-04T21:05:00+03:00
lastmod: 2026-01-07T14:22:00+03:00
tags: ["education", "modeling"]
categories: ["science"]
draft: false
slug: "gns3-vmware"
---

GNS3 на vmWare.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Установка на Windows {#установка-на-windows}


### <span class="section-num">1.1</span> Установка программного обеспечения {#установка-программного-обеспечения}


#### <span class="section-num">1.1.1</span> vmWare {#vmware}

-   Будем использовать Chocolatey ([Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})).
-   Установим vmWare (см. [Система виртуализации VMware]({{< relref "2024-05-16-vmware-virtualization-system" >}})):
    ```shell
    choco install vmwareworkstation
    ```
-   Устанавливаются необходимые библиотеки.
-   Скачивание производится по прямой ссылке, поэтому из России скачивание заблокировано.
-   Для скачивания используем сторонний ресурс, например <https://www.comss.ru/list.php?c=vm_apps>.


#### <span class="section-num">1.1.2</span> GNS3 {#gns3}

-   Установим GNS3:
    ```shell
    choco install gns3
    ```
-   Chocolatey автоматически скачает и установит GNS3, включая зависимые компоненты (Wireshark, WinPcap, SuperPutty --- если они не установлены).


#### <span class="section-num">1.1.3</span> Установка образа виртуальной машины {#установка-образа-виртуальной-машины}

-   Установка через Chocolatey не включает GNS3 VM.
-   Его нужно импортировать в VMware отдельно.
-   Скачайте GNS3 VM (`GNS3.VM.VMware.Workstation.3.0.5.zip` для версии 3.0.5) с официального сайта:
    -   <https://www.gns3.com/software/download-vm>;
    -   <https://github.com/GNS3/gns3-gui/releases>
-   Рапакуйте архив.
-   Импортируйте VM в VMware:
    -   В VMware Workstation выберите _File → Open_.
    -   Укажите скачанный файл `.OVA` и завершите импорт.
-   Настройте ресурсы VM (в свойствах VM):
    -   vCPU: 2--4.
    -   ОЗУ: минимум 2 ГБ (оптимально --- половина доступной ОЗУ хоста).
    -   Убедитесь, что включена поддержка виртуализации (Intel VT-x/AMD-V).


### <span class="section-num">1.2</span> Подключение GNS3 к GNS3 VM {#подключение-gns3-к-gns3-vm}

-   Запустите GNS3.
-   Запустите мастер установки: `Help` → `Setup Wizard`.
-   Выберите _Connect to a remote controller_.
