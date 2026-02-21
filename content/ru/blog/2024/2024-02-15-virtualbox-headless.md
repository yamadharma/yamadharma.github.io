---
title: "VirtualBox. Использование без монитора"
author: ["Dmitry S. Kulyabov"]
date: 2024-02-15T20:05:00+03:00
lastmod: 2024-03-06T19:56:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "virtualbox-headless"
---

VirtualBox. Использование без монитора.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Настройка {#настройка}


### <span class="section-num">1.1</span> Папка виртуальных машин {#папка-виртуальных-машин}

-   Установим папку для виртуальных машине в `/var/vm`:
    ```shell
    vboxmanage setproperty machinefolder /var/vm
    ```
-   Можно восстановить значение по умолчанию:
    ```shell
    VBoxManage setproperty machinefolder default
    ```


## <span class="section-num">2</span> Создание виртуальной машины {#создание-виртуальной-машины}

-   Создайте новую виртуальную машину:
    ```shell
    vboxmanage createvm --name "Windows" --ostype Windows10 --register
    ```

    -   Если не указать параметр `--register`, придётся вручную использовать команду `registervm` позже.
-   Список операционных систем можно посмотреть по команде:
    ```shell
    vboxmanage list ostypes
    ```
-   Также нужно установить параметры виртуальной машины:
    ```shell
    vboxmanage modifyvm "Windows" --memory 2048 --acpi on --boot1 dvd --nic1 nat
    ```
-   Создайте виртуальный жесткий диск для виртуальной машины (например, ёмкостью 10 ГБ):
    ```shell
    vboxmanage createhd --filename "win.vdi" --size 10000
    ```
-   Добавьте контроллер IDE в новую виртуальную машину:
    ```shell
    vboxmanage storagectl "Windows" --name "IDE Controller" --add ide --controller PIIX4
    ```
-   Установите созданный вами файл VDI в качестве первого виртуального жесткого диска новой виртуальной машины:
    ```shell
    vboxmanage storageattach "Windows" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium "win.vdi"
    ```
-   Подсоедините к виртуальной машине ISO-файл, содержащий операционную систему, которую вы хотите установить:
    ```shell
    vboxmanage storageattach "Windows" --storagectl "IDE Controller" --port 0 --device 1 --type dvddrive --medium /full/path/to/iso.iso
    ```
-   Включите расширение удаленного рабочего стола VirtualBox (сервер VRDP):
    ```shell
    vboxmanage modifyvm "Windows" --vrde on
    ```
-   Включите поддержку UEFI.
    ```shell
    vboxmanage modifyvm "Windows" --firmware=efi
    ```


## <span class="section-num">3</span> Управление виртуальной машиной {#управление-виртуальной-машиной}

-   Запустите виртуальную машину:
    ```shell
    vboxheadless --startvm "Windows"
    ```
-   Команда запускается и занимает консоль.
-   На клиентском компьютере запустите средство просмотра RDP и подключитесь к серверу.
-   Остановить виртуальную машину можно, запустив на другой консоли:
    ```shell
    vboxmanage controlvm "Windows" poweroff
    ```
