---
title: "Лабораторная работа Установка ОС Linux"
author: ["Dmitry S. Kulyabov"]
date: 2022-04-04T13:40:00+03:00
lastmod: 2025-10-28T19:05:00+03:00
tags: ["linux", "education"]
categories: ["computer-science"]
draft: false
weight: 201
toc: true
type: "docs"
feedback: false
slug: "lab-linux-install"
summary: "Установка ОС Linux"
linktitle: "Установка ОС Linux"
menu:
  "lab-linux-install":
    identifier: "лабораторная-работа-установка-ос-linux"
    parent: "os-intro-lab"
    weight: 201
---

Лабораторная работа _Установка ОС Linux_.

<!--more-->


## <span class="section-num">1</span> Цель работы {#цель-работы}

-   Целью данной работы является приобретение практических навыков установки операционной системы на виртуальную машину, настройки минимально необходимых для дальнейшей работы сервисов.


## <span class="section-num">2</span> Указания к работе {#указания-к-работе}


### <span class="section-num">2.1</span> Техническое обеспечение {#техническое-обеспечение}

-   Лабораторная работа подразумевает установку на виртуальную машину VirtualBox (<https://www.virtualbox.org/>) операционной системы Linux (дистрибутив Fedora).
-   Выполнение работы возможно как в дисплейном классе факультета физико-математических и естественных наук РУДН, так и дома. Описание выполнения работы приведено для дисплейного класса со следующими характеристиками техники:
    -   Intel Core i3-550 3.2 GHz, 4 GB оперативной памяти, 80 GB свободного места на жёстком диске;
    -   ОС Linux Gentoo (<http://www.gentoo.ru/>);
    -   VirtualBox версии 7.0 или новее.
-   Для установки в виртуальную машину используется дистрибутив Linux Fedora (<https://getfedora.org>), вариант с менеджером окон _sway_ (<https://fedoraproject.org/spins/sway/>).
-   При выполнении лабораторной работы на своей технике вам необходимо скачать необходимый образ операционной системы (<https://fedoraproject.org/spins/sway/download/index.html>).
-   В дисплейных классах можно воспользоваться образом в каталоге `/afs/dk.sci.pfu.edu.ru/common/files/iso`.
-   Для определённости в описании будем использовать версию `Fedora-Sway-Live-x86_64-43-1.6.iso`.


### <span class="section-num">2.2</span> Соглашения об именовании {#соглашения-об-именовании}

-   При выполнении работ следует придерживаться следующих правил именования:
    -   Пользователь внутри виртуальной машины должен иметь имя, совпадающее с учётной записью студента, выполняющего лабораторную работу.
    -   Имя хоста вашей виртуальной машины должно совпадать с учётной записью студента, выполняющего лабораторную работу.
    -   Имя виртуальной машины должно совпадать с учётной записью студента, выполняющего лабораторную работу.
    -   В дисплейных классах вы можете посмотреть имя вашей учётной записи, набрав в терминале команду:
        ```shell
        id -un
        ```
-   При установке на своей технике необходимо использовать имя вашей учётной записи дисплейных классов. Например, если студента зовут Остап Сулейманович Бендер, то его учётная запись имеет вид `osbender`.


## <span class="section-num">3</span> Последовательность выполнения работы {#последовательность-выполнения-работы}


### <span class="section-num">3.1</span> Варианты создания образа виртуальной машины {#варианты-создания-образа-виртуальной-машины}

-   Предлагается несколько вариантов установки ОС Linux на основе следующих программных эмуляторов:
    -   qemu;
    -   virtualbox.


### <span class="section-num">3.2</span> Установка Linux на qemu {#установка-linux-на-qemu}


#### <span class="section-num">3.2.1</span> Общая информация {#общая-информация}

-   Данный вариант установки возможен, если у Вас установлено программное обеспечение Qemu (<https://www.qemu.org/>).


#### <span class="section-num">3.2.2</span> Выполнение в дисплейном классе {#выполнение-в-дисплейном-классе}

-   Загрузите в дисплейном классе операционную систему Linux. Осуществите вход в систему.

<!--list-separator-->

1.  Настройка каталога для виртуальных машин

    -   Запустите терминал. Перейдите в каталог `/var/tmp`:
        ```shell
        cd /var/tmp
        ```
    -   Создайте каталог с именем пользователя (совпадающий с логином студента в дисплейном классе). Для этого можно использовать команду:
        ```shell
        mkdir /var/tmp/`id -un`
        ```
    -   Дальнейшую работу проводите в этом каталоге.


#### <span class="section-num">3.2.3</span> Создание образа {#создание-образа}

-   Создадим образ виртуального диска: `60GB`, формат `qcow2`:
    ```shell
    qemu-img create -f qcow2 fedora-sway.qcow2 60G
    ```

-   Запустите виртуальную машину:
    ```shell
    qemu-system-x86_64 -boot menu=on -m 2048 -cpu max -smp 4 \
        -cdrom Fedora-Sway-Live-x86_64-43-1.6.iso \
        -drive file=fedora-sway.qcow2,format=qcow2,if=virtio,aio=native,cache=none \
        -bios /usr/share/edk2-ovmf/OVMF_CODE.fd \
        -enable-kvm -machine q35 -device intel-iommu \
        -device virtio-balloon \
        -chardev qemu-vdagent,id=vdagent0,name=vdagent,clipboard=on,mouse=off \
        -display default,show-cursor=on \
        -vga none -device virtio-gpu-pci
    ```

    -   Видео-устройств подключено на видеокарту компьютера.
-   Выберите `Start Fedora-Sway-Live 43`.
-   Загрузится графический режим.
-   Если вы запускаете из-под Sway, включите `Passthrough mode`.
-   Также можно использовать режим захвата, переключая его по комбинации `Ctrl+Alt+g`.
-   Установите систему.


#### <span class="section-num">3.2.4</span> После установки виртуальной машины {#после-установки-виртуальной-машины}

-   Для удобства создайте командный файл `fedora-sway-start.sh`:
    ```shell
    touch fedora-sway-start.sh
    chmod +x fedora-sway-start.sh
    ```
-   В файл запишите команду для запуска:
    ```shell
    #!/bin/bash

    qemu-system-x86_64 -boot menu=on \
       -m 2048 -mem-path /dev/hugepages \
       -cpu max -smp 4 \
        -drive file=fedora-sway.qcow2,format=qcow2,if=virtio,aio=native,cache=none \
        -bios /usr/share/edk2-ovmf/OVMF_CODE.fd \
        -enable-kvm -machine q35 -device intel-iommu \
        -device virtio-balloon \
        -device virtio-serial \
        -chardev spicevmc,id=vdagent,debug=0,name=vdagent \
        -device virtserialport,chardev=vdagent,name=com.redhat.spice.0 \
        -chardev qemu-vdagent,id=vdagent0,name=vdagent,clipboard=on,mouse=on \
        -display default,show-cursor=on \
        -vga none -device virtio-gpu-pci
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      fedora-sway-start.sh
    </div>


#### <span class="section-num">3.2.5</span> Видео: Установка Linux на qemu {#видео-установка-linux-на-qemu}

{{< tabs "Установка Linux на qemu" >}}

{{< tab "RuTube" >}}

{{< rutube 50903a2181f564a0a207ace60067ad3d >}}

{{< /tab >}}

{{< tab "Платформа" >}}

{{< plvideo W5741K4QRBi1 >}}

{{< /tab >}}

{{< tab "VKvideo" >}}

{{< vkvideo 606414976 456239663 2 >}}

{{< /tab >}}

{{< tab "Youtube" >}}

{{< youtube zdGOCVWmnWo >}}

{{< /tab >}}

{{< /tabs >}}


### <span class="section-num">3.3</span> Установка Linux на Virtualbox {#установка-linux-на-virtualbox}


#### <span class="section-num">3.3.1</span> Выполнение в дисплейном классе {#выполнение-в-дисплейном-классе}

-   Загрузите в дисплейном классе операционную систему Linux. Осуществите вход в систему.

<!--list-separator-->

1.  Настройка каталога для виртуальных машин

    <!--list-separator-->

    1.  Создание необходимых каталогов

        -   Запустите терминал. Перейдите в каталог `/var/tmp`:
            ```shell
            cd /var/tmp
            ```
        -   Создайте каталог с именем пользователя (совпадающий с логином студента в дисплейном классе). Для этого можно использовать команду:
            ```shell
            mkdir /var/tmp/`id -un`
            ```
        -   Проверьте в свойствах VirtualBox **месторасположение каталога для виртуальных машин**:
            ```shell
            /var/tmp/имя_пользователя
            ```

            -   Здесь `имя_пользователя` --- логин (учётная запись) студента в дисплейном классе. Если указан другой каталог, то требуется изменить его.

    <!--list-separator-->

    2.  Папка виртуальных машин

        <!--list-separator-->

        1.  Значения по умолчанию

            -   Linux: `$HOME/VirtualBox VMs`.

        <!--list-separator-->

        2.  Графический интерфейс

            -   В меню выберите _Файл_, _Настройки_.
            -   Выберите _Общие_, поле _Папка для машин по умолчанию_.
            -   Установите новое значение, например `/var/tmp/имя_пользователя`.
            -   Нажмите ОК, чтобы сохранить изменения.

        <!--list-separator-->

        3.  Командная строка

            -   Зададим отображение информации о настройках VirtualBox на английском.
            -   Поэтому следует задать кодировку для отображения свойств VirtualBox:
                ```shell
                vboxmanage setproperty language C
                ```
            -   Установим папку для виртуальных машине в `/var/tmp/имя_пользователя`:
                ```shell
                vboxmanage setproperty machinefolder /var/tmp/$(id -un)
                ```
            -   Поверьте, что папка виртуальных машин по умолчанию изменена:
                ```shell
                vboxmanage list systemproperties | grep "Default machine folder:"
                ```
            -   Следующая команда выдаст только каталог:
                ```shell
                vboxmanage list systemproperties | grep "Default machine folder:" | cut -d":" -f2 | tr -d ' '
                ```

        <!--list-separator-->

        4.  Установочный образ

            -   Перенесите установочный образ в папку `/var/tmp/имя_пользователя/iso`:
                ```shell
                mkdir -p "$(vboxmanage list systemproperties | grep 'Default machine folder:' | cut -d':' -f2 | tr -d ' ')/iso"
                mv Fedora-Sway-Live-x86_64-43-1.6.iso "$(vboxmanage list systemproperties | grep 'Default machine folder:' | cut -d':' -f2 | tr -d ' ')/iso"
                ```

<!--list-separator-->

2.  Настройка хост-клавиши

    -   Хост-клавишей по умолчанию является правый `Ctrl`.
    -   По умолчанию в дисплейных классах на клавише правый `Ctrl` находится переключатель языка ввода.
    -   Эти значения могут конфликтовать.

    <!--list-separator-->

    1.  Графический интерфейс

        -   В меню выберите _Файл_, _Настройки_.
        -   Выберите _Ввод_, вкладка _Виртуальная машина_.
        -   Выберите _Сочетание клавиш_ в строке _Хост-комбинация_.
        -   Нажмите новое сочетание клавиш.
        -   Нажмите ОК, чтобы сохранить изменения.

    <!--list-separator-->

    2.  Командная строка

        -   Проверьте текущую комбинацию для хост-клавиши:
            ```shell
            VBoxManage getextradata global GUI/Input/HostKeyCombination
            ```

            -   По умолчанию установлена комбинация `65508`, соответствующая правой клавише `Ctrl`.
        -   Установите нужную клавишу (в примере клавиша _Menu_):
            ```shell
            VBoxManage setextradata global GUI/Input/HostKeyCombination 65383
            ```
        -   Комбинации клавиш можно, например, посмотреть на странице <https://pythonhosted.org/pyglet/api/pyglet.window.key-module.html>.


#### <span class="section-num">3.3.2</span> Создание виртуальной машины {#создание-виртуальной-машины}

-   Для использования графического интерфейса запустите менеджер виртуальных машин, введя в командной строке:
    ```shell
    VirtualBox &
    ```
-   Создайте новую виртуальную машину в графическом интерфейсе или в командной строке.
    -   В командной строке:
        ```shell
        vboxmanage createvm --name "$(id -un)_os-intro" --ostype Fedora_64 --register
        ```
-   Укажите имя виртуальной машины (ваш логин в дисплейном классе), тип операционной системы --- Linux, Fedora.
-   Укажите размер основной памяти виртуальной машины --- от 2048 МБ.
    -   В командной строке:
        ```shell
        vboxmanage modifyvm "$(id -un)_os-intro" --memory 2048 --acpi on --nic1 nat
        ```

-   Задайте конфигурацию жёсткого диска --- загрузочный, VDI (VirtualBox Disk Image), динамический виртуальный диск.
-   Задайте размер диска --- 80 ГБ (или больше), его расположение --- в данном случае `/var/tmp/имя_пользователя/имя_машины/имя_машины.vdi`.
    -   В командной строке:
        ```shell
        vboxmanage createhd --filename "$(vboxmanage list systemproperties | grep 'Default machine folder:' | cut -d':' -f2 | tr -d ' ')/$(id -un)_os-intro/$(id -un)_os-intro.vdi" --size 80000
        ```
-   Выберите в VirtualBox Вашей виртуальной машины. Добавьте новый привод оптических дисков и выберите образ.
    -   В командной строке:
        -   Подключите загрузку с DVD:
            ```shell
            vboxmanage modifyvm "$(id -un)_os-intro" --boot1 dvd
            ```
        -   Добавьте IDE-контроллер:
            ```shell
            vboxmanage storagectl "$(id -un)_os-intro" --name "IDE Controller" --add ide --controller PIIX4
            ```
        -   Установите созданный вами файл VDI в качестве первого виртуального жесткого диска новой виртуальной машины:
            ```shell
            vboxmanage storageattach "$(id -un)_os-intro" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium "$(vboxmanage list systemproperties | grep 'Default machine folder:' | cut -d':' -f2 | tr -d ' ')/$(id -un)_os-intro/$(id -un)_os-intro.vdi"
            ```
        -   Подключите к виртуальной машине ISO-файл:
            ```shell
            vboxmanage storageattach "$(id -un)_os-intro" --storagectl "IDE Controller" --port 0 --device 1 --type dvddrive --medium "$(vboxmanage list systemproperties | grep 'Default machine folder:' | cut -d':' -f2 | tr -d ' ')/iso/Fedora-Sway-Live-x86_64-43-1.6.iso"
            ```
-   При установке на собственной технике используйте скачанный образ операционной системы Fedora.
-   В качестве графического контроллера поставьте VMSVGA.
    -   В командной строке:
        ```shell
        vboxmanage modifyvm "$(id -un)_os-intro" --graphicscontroller=vmsvga
        ```
-   Включите ускорение 3D.
    -   В командной строке:
        ```shell
        vboxmanage modifyvm "$(id -un)_os-intro" --accelerate-3d=on
        ```
-   Если есть проблемы при отображении, загрузитесь в режиме базовой графики.
-   Включите общий буфер обмена и перетаскивание объектов между хостом и гостевой ОС.
    -   В командной строке:
        ```shell
        vboxmanage modifyvm "$(id -un)_os-intro" --clipboard-mode=bidirectional --drag-and-drop=bidirectional
        ```
-   Включите поддержку UEFI.
    -   В командной строке:
        ```shell
        vboxmanage modifyvm "$(id -un)_os-intro" --firmware=efi
        ```


#### <span class="section-num">3.3.3</span> Видео: Создание виртуальной машины {#видео-создание-виртуальной-машины}

{{< tabs "Создание виртуальной машины" >}}

{{< tab "RuTube" >}}

{{< rutube f4e38867368ced9e13556341023c2c03 >}}

{{< /tab >}}

{{< tab "Youtube" >}}

{{< youtube 9_Vt7R57Yw4 >}}

{{< /tab >}}

{{< /tabs >}}


#### <span class="section-num">3.3.4</span> После установки виртуальной машины {#после-установки-виртуальной-машины}

<!--list-separator-->

1.  Установка драйверов для VirtualBox

    -   Войдите в ОС под заданной вами при установке учётной записью.
    -   Нажмите комбинацию _Win+Enter_ для запуска терминала.
    -   Запустите терминальный мультиплексор _tmux_:
        ```shell
        tmux
        ```
    -   Переключитесь на роль супер-пользователя:
        ```shell
        sudo -i
        ```
    -   Установите средства разработки:
        ```shell
        dnf -y group install development-tools
        ```
    -   Установите пакет _DKMS_:
        ```shell
        dnf -y install dkms
        ```
    -   В меню виртуальной машины подключите образ диска дополнений гостевой ОС.
    -   Подмонтируйте диск:
        ```shell
        mount /dev/sr0 /media
        ```
    -   Установите драйвера:
        ```shell
        /media/VBoxLinuxAdditions.run
        ```
    -   Перегрузите виртуальную машину:
        ```shell
        reboot
        ```

<!--list-separator-->

2.  Подключение общей папки

    -   Внутри виртуальной машины добавьте своего пользователя в группу `vboxsf` (вместо `username` укажите ваш логин):
        ```shell
        gpasswd -a username vboxsf
        ```
    -   В хостовой системе подключите разделяемую папку:
        ```shell
        vboxmanage sharedfolder add "$(id -un)_os-intro" --name=work --hostpath=work --automount
        ```
    -   Перегрузите виртуальную машину:
        ```shell
        reboot
        ```
    -   Папка будет монтироваться в `/media/sf_work`.


### <span class="section-num">3.4</span> Установка операционной системы {#установка-операционной-системы}


#### <span class="section-num">3.4.1</span> Запуск приложения для установки системы {#запуск-приложения-для-установки-системы}

-   Загрузите LiveCD.
-   Появится интерфейс начальной конфигурации.
-   Нажмите _Enter_ для создания конфигурации по умолчанию.
-   Нажмите _Enter_, чтобы выбрать в качестве модификатора клавишу _Win_ (она же клавиша _Super_).
-   В файле конфигурации эта клавиша будет обозначена как `$Mod`.
-   Нажмите комбинацию _Win+Enter_ для запуска терминала.
-   В терминале запустите `liveinst`.
-   Для перехода к раскладке окон с табами нажмите _Win+w_.


#### <span class="section-num">3.4.2</span> Установка системы на диск {#установка-системы-на-диск}

-   Выберите язык интерфейса и перейдите к настройкам установки операционной системы.
-   При необходимости скорректируйте часовой пояс, раскладку клавиатуры (рекомендуется в качестве языка по умолчанию указать английский язык).
-   Место установки ОС оставьте без изменения.
-   Установите имя и пароль для пользователя `root`.
-   Установите имя и пароль для Вашего пользователя.
-   Задайте сетевое имя Вашего компьютера.
-   После завершения установки операционной системы корректно перезапустите виртуальную машину.
-   В VirtualBox оптический диск должен отключиться автоматически, но если это не произошло, то необходимо отключить носитель информации с образом.


#### <span class="section-num">3.4.3</span> Видео: Установка операционной системы {#видео-установка-операционной-системы}

{{< tabs "Установка операционной системы" >}}

{{< tab "RuTube" >}}

{{< rutube 603fc8f3cf968d3c4151073aa7a4789f >}}

{{< /tab >}}

{{< tab "Youtube" >}}

{{< youtube XYYbl5ABN9Q >}}

{{< /tab >}}

{{< /tabs >}}


### <span class="section-num">3.5</span> После установки {#после-установки}

-   Войдите в ОС под заданной вами при установке учётной записью.
-   Нажмите комбинацию _Win+Enter_ для запуска терминала.
-   Переключитесь на роль супер-пользователя:
    ```shell
    sudo -i
    ```


#### <span class="section-num">3.5.1</span> Исправления {#исправления}

-   Запретите устанавливать заблокированный openh264:
    ```shell
    sudo dnf config-manager setopt fedora-cisco-openh264.enabled=0
    sudo dnf clean all
    ```


#### <span class="section-num">3.5.2</span> Обновления {#обновления}

-   Установите средства разработки:
    ```shell
    sudo dnf -y group install development-tools
    ```
-   Обновить все пакеты
    ```shell
    sudo dnf -y update
    ```


#### <span class="section-num">3.5.3</span> Повышение комфорта работы {#повышение-комфорта-работы}

-   Программы для удобства работы в консоли:
    ```shell
    sudo dnf -y install tmux mc
    ```
-   Другой вариант консоли:
    ```shell
    sudo dnf -y install kitty
    ```


#### <span class="section-num">3.5.4</span> Автоматическое обновление {#автоматическое-обновление}

-   При необходимости можно использовать автоматическое обновление (см. [Автообновление систем на базе деривативов RedHat]({{< relref "2022-09-25-redhat-based-systems-auto-update" >}})).
-   Установка программного обеспечения:
    ```shell
    sudo dnf -y install dnf-automatic
    ```
-   Задаёте необходимую конфигурацию в файле `/etc/dnf/automatic.conf`.
-   Запустите таймер:
    ```shell
    sudo systemctl enable --now dnf-automatic.timer
    ```


#### <span class="section-num">3.5.5</span> Отключение SELinux {#отключение-selinux}

-   В данном курсе мы не будем рассматривать работу с системой безопасности SELinux.
-   Поэтому отключим его.
-   В файле `/etc/selinux/config` замените значение
    ```conf-unix
    SELINUX=enforcing
    ```
    на значение
    ```conf-unix
    SELINUX=permissive
    ```
-   Перегрузите виртуальную машину:
    ```shell
    sudo systemctl reboot
    ```


### <span class="section-num">3.6</span> Настройка раскладки клавиатуры {#настройка-раскладки-клавиатуры}

-   Войдите в ОС под заданной вами при установке учётной записью.
-   Нажмите комбинацию _Win+Enter_ для запуска терминала.
-   Запустите терминальный мультиплексор _tmux_:
    ```shell
    tmux
    ```
-   Создайте конфигурационный файл `~/.config/sway/config.d/95-system-keyboard-config.conf`:
    ```shell
    mkdir -p ~/.config/sway
    touch ~/.config/sway/config.d/95-system-keyboard-config.conf
    ```
-   Отредактируйте конфигурационный файл `~/.config/sway/config.d/95-system-keyboard-config.conf`:
    ```conf-unix
    exec_always /usr/libexec/sway-systemd/locale1-xkb-config --oneshot
    ```
-   Переключитесь на роль супер-пользователя:
    ```shell
    sudo -i
    ```
-   Отредактируйте конфигурационный файл `/etc/X11/xorg.conf.d/00-keyboard.conf`:
    ```conf-unix
    Section "InputClass"
                Identifier "system-keyboard"
                MatchIsKeyboard "on"
                Option "XkbLayout" "us,ru"
                Option "XkbVariant" ",winkeys"
                Option "XkbOptions" "grp:rctrl_toggle,compose:ralt,terminate:ctrl_alt_bksp"
    EndSection
    ```
-   Для этого можно использовать файловый менеджер `mc` и его встроенный редактор.
-   Перегрузите виртуальную машину:
    ```shell
    sudo systemctl reboot
    ```


#### <span class="section-num">3.6.1</span> Видео: Настройка раскладки клавиатуры {#видео-настройка-раскладки-клавиатуры}

{{< tabs "Настройка раскладки клавиатуры" >}}

{{< tab "RuTube" >}}

{{< rutube f1004d77e929bfb0f856f8aa471aa67c >}}

{{< /tab >}}

{{< tab "Youtube" >}}

{{< youtube ayLha0dDiQw >}}

{{< /tab >}}

{{< /tabs >}}


### <span class="section-num">3.7</span> Установка имени пользователя и названия хоста {#установка-имени-пользователя-и-названия-хоста}

-   Если при установке виртуальной машины вы задали имя пользователя или имя хоста, не удовлетворяющее соглашению об именовании, то вам необходимо исправить это.
-   Запустите виртуальную машину и залогиньтесь.
-   Нажмите комбинацию _Win+Enter_ для запуска терминала.
-   Запустите терминальный мультиплексор _tmux_:
    ```shell
    tmux
    ```
-   Переключитесь на роль супер-пользователя:
    ```shell
    sudo -i
    ```
-   Создайте пользователя (вместо `username` укажите ваш логин в дисплейном классе):
    ```shell
    adduser -G wheel username
    ```
-   Задайте пароль для пользователя (вместо `username` укажите ваш логин в дисплейном классе):
    ```shell
    passwd username
    ```
-   Установите имя хоста (вместо `username` укажите ваш логин в дисплейном классе):
    ```shell
    hostnamectl set-hostname username
    ```
-   Проверьте, что имя хоста установлено верно:
    ```shell
    hostnamectl
    ```


#### <span class="section-num">3.7.1</span> Видео: Имя пользователя и хоста {#видео-имя-пользователя-и-хоста}

{{< tabs "Имя пользователя и хоста" >}}

{{< tab "RuTube" >}}

{{< rutube a1a2bac5dbd805b11d5d5390cdfcee50 >}}

{{< /tab >}}

{{< tab "Youtube" >}}

{{< youtube zU1x8rx4JjA >}}

{{< /tab >}}

{{< /tabs >}}


### <span class="section-num">3.8</span> Установка программного обеспечения для создания документации {#установка-программного-обеспечения-для-создания-документации}

-   Нажмите комбинацию _Win+Enter_ для запуска терминала.
-   Запустите терминальный мультиплексор _tmux_:
    ```shell
    tmux
    ```
-   Переключитесь на роль супер-пользователя:
    ```shell
    sudo -i
    ```


#### <span class="section-num">3.8.1</span> Работа с языком разметки Markdown {#работа-с-языком-разметки-markdown}

-   Средство `pandoc` для работы с языком разметки Markdown.
-   Установка с помощью менеджера пакетов:
    ```shell
    sudo dnf -y install pandoc
    ```
-   Для работы с перекрёстными ссылками мы используем пакет `pandoc-crossref`.
    -   Пакет `pandoc-crossref` в стандартном репозитории отсутствует.
    -   Придётся ставить вручную, скачав с сайта <https://github.com/lierdakil/pandoc-crossref>.
    -   При установке `pandoc-crossref` следует обращать внимание, для какой версии `pandoc` он скомпилён.
-   Лучше установить `pandoc` и `pandoc-crossref` вручную.
    -   Скачайте необходимую версию `pandoc-crossref` (<https://github.com/lierdakil/pandoc-crossref/releases>).
    -   Посмотрите, для какой версии откомпилён `pandoc-crossref`.
    -   Скачайте соответствующую версию `pandoc` (<https://github.com/jgm/pandoc/releases>).
    -   Распакуйте архивы.
    -   Обе программы собраны в виде статически-линкованных бинарных файлов.
    -   Поместите их в каталог `/usr/local/bin`.


#### <span class="section-num">3.8.2</span> texlive {#texlive}

-   Установим дистрибутив TeXlive (см. [Установка TeX Live]({{< relref "2021-04-23-install-texlive" >}})):
    ```shell
    sudo dnf -y install texlive-scheme-full
    ```


#### <span class="section-num">3.8.3</span> Видео: Установка TeX {#видео-установка-tex}

{{< tabs "Установка TeX" >}}
{{< tab "RuTube" >}}

{{< rutube a60d71c8e5644c1fa42b445670fb43c8 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube 65yj0KvKZGM >}}

{{< /tab >}}
{{< /tabs >}}


#### <span class="section-num">3.8.4</span> Видео: После установки Linux {#видео-после-установки-linux}

{{< tabs "После установки Linux" >}}
{{< tab "RuTube" >}}

{{< rutube 4a71b855759392e4135cda667f30e86f >}}

{{< /tab >}}
{{< tab "Платформа" >}}

{{< plvideo SwKzG-swMcwg >}}

{{< /tab >}}
{{< tab "VKvideo" >}}

{{< vkvideo 606414976 456239705 2 >}}

{{< /tab >}}
{{< tab "Youtube" >}}

{{< youtube lhdLoxZ6T9c >}}

{{< /tab >}}
{{< /tabs >}}


## <span class="section-num">4</span> Домашнее задание {#домашнее-задание}

-   Дождитесь загрузки графического окружения и откройте терминал. В окне терминала проанализируйте последовательность загрузки системы, выполнив команду `dmesg`. Можно просто просмотреть вывод этой команды:
    ```shell
    dmesg | less
    ```
-   Можно использовать поиск с помощью `grep`:
    ```shell
    dmesg | grep -i "то, что ищем"
    ```
-   Получите следующую информацию.
    -   Версия ядра Linux (Linux version).
    -   Частота процессора (Detected Mhz processor).
    -   Модель процессора (CPU0).
    -   Объём доступной оперативной памяти (Memory available).
    -   Тип обнаруженного гипервизора (Hypervisor detected).
    -   Тип файловой системы корневого раздела.
    -   Последовательность монтирования файловых систем.


## <span class="section-num">5</span> Содержание отчёта {#содержание-отчёта}

-   Отчёт должен включать:
    -   титульный лист;
    -   формулировку задания работы;
    -   описание результатов выполнения задания:
        -   краткое описание действия;
        -   вводимую команду или команды;
        -   результаты выполнения команд (снимок экрана);
    -   выводы, согласованные с заданием работы;
    -   ответы на контрольные вопросы;
    -   отчёт о выполнении дополнительного задания.


## <span class="section-num">6</span> Контрольные вопросы {#контрольные-вопросы}

1.  Какую информацию содержит учётная запись пользователя?

2.  Укажите команды терминала и приведите примеры:
    -   для получения справки по команде;
    -   для перемещения по файловой системе;
    -   для просмотра содержимого каталога;
    -   для определения объёма каталога;
    -   для создания / удаления каталогов / файлов;
    -   для задания определённых прав на файл / каталог;
    -   для просмотра истории команд.

3.  Что такое файловая система? Приведите примеры с краткой характеристикой.
4.  Как посмотреть, какие файловые системы подмонтированы в ОС?
5.  Как удалить зависший процесс?

При ответах на контрольные вопросы рекомендуется ознакомиться с информацией из  [<a href="#citeproc_bib_item_1">1</a>; <a href="#citeproc_bib_item_1">1</a>–<a href="#citeproc_bib_item_7">7</a>].


## <span class="section-num">7</span> Библиография {#библиография}

## Литература

<div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>1.	Dash, P. Getting Started with Oracle VM VirtualBox / P. Dash. – Packt Publishing Ltd, 2013. – 86 сс.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>2.	Colvin, H. VirtualBox: An Ultimate Guide Book on Virtualization with VirtualBox. VirtualBox / H. Colvin. – CreateSpace Independent Publishing Platform, 2015. – 70 сс.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>3.	Vugt, S. van. Red Hat RHCSA/RHCE 7 cert guide : Red Hat Enterprise Linux 7 (EX200 and EX300) : Certification Guide. Red Hat RHCSA/RHCE 7 cert guide / S. van Vugt. – Pearson IT Certification, 2016. – 1008 сс.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>4.	Робачевский, А. Операционная система UNIX / А. Робачевский, С. Немнюгин, О. Стесик. – 2-е изд. – Санкт-Петербург : БХВ-Петербург, 2010. – 656 сс.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_5"></a>5.	Немет, Э. Unix и Linux: руководство системного администратора. Unix и Linux / Э. Немет, Г. Снайдер, Т.Р. Хейн, Б. Уэйли. – 4-е изд. – Вильямс, 2014. – 1312 сс.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_6"></a>6.	Колисниченко, Д.Н. Самоучитель системного администратора Linux : Системный администратор / Д.Н. Колисниченко. – Санкт-Петербург : БХВ-Петербург, 2011. – 544 сс.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_7"></a>7.	Robbins, A. Bash Pocket Reference / A. Robbins. – O’Reilly Media, 2016. – 156 сс.</div>
</div>
