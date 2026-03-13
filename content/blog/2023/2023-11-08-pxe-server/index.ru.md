---
title: "Загрузочный сервер PXE"
author: ["Dmitry S. Kulyabov"]
date: 2023-11-08T14:42:00+03:00
lastmod: 2024-06-18T16:54:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "pxe-server"
---

Установка загрузочного сервера PXE.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая настройка {#общая-настройка}

-   Установите сервер Linux (см. [Rocky Linux. Установка сервера]({{< relref "2022-08-12-rockylinux-server-installation" >}})).


## <span class="section-num">2</span> Сетевые сервисы {#сетевые-сервисы}


### <span class="section-num">2.1</span> tftp {#tftp}

-   Установите сервер tftp:
    ```shell
    dnf -y install tftp-server
    ```
-   Настройте брандмауэр:
    ```shell
    firewall-cmd --add-service=tftp --permanent
    firewall-cmd --reload
    ```
-   Активируйте сервис:
    ```shell
    systemctl enable --now tftp.socket
    ```


### <span class="section-num">2.2</span> web-сервер {#web-сервер}

-   Для снижения нагрузки на tftp будем загружать образы по http.
-   Установим сервер nginx:
    ```shell
    dnf -y install nginx
    ```
-   Настройте брандмауэр:
    ```shell
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    ```


#### <span class="section-num">2.2.1</span> Конфигурация {#конфигурация}

-   Создадим файл конфигурации `/etc/nginx/conf.d/pxe.conf`:
    ```conf-unix
    server {
        listen   80 default_server;
        listen       [::]:80;
        root /var/lib/tftpboot;
        server_name pxe.example.com;

        location / {
        }
        index index.html index.htm;
        autoindex on;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;
    }
    ```


#### <span class="section-num">2.2.2</span> SELinux {#selinux}

-   Зададим переключатели SELinux:
    ```shell
    setsebool -P httpd_serve_cobbler_files 1
    setsebool httpd_serve_cobbler_files 1
    ```
-   Создадим файл с описанием политики `nginx-tftp.te`:
    ```conf-unix
    module nginx-tftp 1.0;

    require {
            type httpd_t;
            type cobbler_var_lib_t;
            type tftpdir_rw_t;
            class dir read;
            class file { getattr open read };
            class lnk_file read;
    }

    #============= httpd_t ==============

    #!!!! This avc is allowed in the current policy
    allow httpd_t cobbler_var_lib_t:dir read;

    #!!!! This avc is allowed in the current policy
    allow httpd_t tftpdir_rw_t:dir read;

    #!!!! This avc is allowed in the current policy
    allow httpd_t tftpdir_rw_t:file { getattr open read };
    allow httpd_t tftpdir_rw_t:lnk_file read;
    ```
-   Применим его:
    ```shell
    semodule -i nginx-tftp.te
    ```


#### <span class="section-num">2.2.3</span> Запуск {#запуск}

-   Запустим nginx:
    ```shell
    systemctl enable --now nginx.service
    ```


### <span class="section-num">2.3</span> Настройки DHCP-сервера {#настройки-dhcp-сервера}


#### <span class="section-num">2.3.1</span> Настройки сервера ISC DHCP {#настройки-сервера-isc-dhcp}

-   Настройки для сервера ISC DHCP.
-   Файл конфигурации `/etc/dhcp/dhcpd.conf`.
-   Настройка основных опций:
    ```conf-unix
    option pxe-system-type code 93 = unsigned integer 16;
    option rfc3442-classless-static-routes code 121 = array of integer 8;
    option ms-classless-static-routes code 249 = array of integer 8;

    option space pxelinux;
    option pxelinux.magic code 208 = string;
    option pxelinux.configfile code 209 = text;
    option pxelinux.pathprefix code 210 = text;
    option pxelinux.reboottime code 211 = unsigned integer 32;
    option architecture-type   code 93 = unsigned integer 16;
    option pxelinux.mtftp-ip    code 1 = ip-address;
    option pxelinux.mtftp-cport code 2 = unsigned integer 16;
    option pxelinux.mtftp-sport code 3 = unsigned integer 16;
    option pxelinux.mtftp-tmout code 4 = unsigned integer 8;
    option pxelinux.mtftp-delay code 5 = unsigned integer 8;
    ```
-   Необходимо также настроить `next_server`, который должен указывать на tftp-сервер:
    ```shell
    next-server     10.100.0.1;
    ```


#### <span class="section-num">2.3.2</span> Настройки сервера ISC Kea DHCP {#настройки-сервера-isc-kea-dhcp}

-   Настройки для сервера ISC Kea DHCP.
-   Файл конфигурации `/etc/kea/kea-dhcp4.conf`.
-   Необходимо также настроить `next_server`, который должен указывать на tftp-сервер:
    ```shell
    {
        "Dhcp4": {
            "next-server": "10.100.0.1",
            ...
        }
    }
    ```


## <span class="section-num">3</span> Сетевые загрузчики {#сетевые-загрузчики}

-   Возможно использовать любой сетевой загрузчик:
    -   pxelinux
    -   ipxe
    -   grub2


### <span class="section-num">3.1</span> pxelinux {#pxelinux}


#### <span class="section-num">3.1.1</span> Общая информация {#общая-информация}

-   Часть загрузчика syslinux.
-   Сайт: <https://wiki.syslinux.org/wiki/index.php?title=PXELINUX>
-   ftp-сайт: <https://mirrors.edge.kernel.org/pub/linux/utils/boot/syslinux/>


#### <span class="section-num">3.1.2</span> Установка {#установка}

-   Скачаем файлы для pxelinux:
    ```shell
    cd /tmp
    wget https://mirrors.edge.kernel.org/pub/linux/utils/boot/syslinux/Testing/6.04/syslinux-6.04-pre1.tar.xz
    tar xJvf syslinux-6.04-pre1.tar.xz
    ```
-   Скопируем файлы в наш корень tftp:
    ```shell
    mkdir -p /var/lib/tftpboot/boot/pxelinux/{bios,efi64,efi32}
    find /tmp/syslinux-6.04-pre1/bios -regex  '.*\(c32\|0\)$' -exec cp '{}' /var/lib/tftpboot/boot/pxelinux/bios/ \;
    find /tmp/syslinux-6.04-pre1/bios -name "memdisk" -type f -exec cp '{}' /var/lib/tftpboot/boot/pxelinux/bios/ \;
    find /tmp/syslinux-6.04-pre1/efi32 -regex  '.*\(c32\|efi\)$' -exec cp '{}' /var/lib/tftpboot/boot/pxelinux/efi32 \;
    find /tmp/syslinux-6.04-pre1/efi64 -regex  '.*\(c32\|efi\|e64\|elf\|lnx\)$' -exec cp '{}' /var/lib/tftpboot/boot/pxelinux/efi64 \;
    ```


#### <span class="section-num">3.1.3</span> Настройки DHCP-сервера {#настройки-dhcp-сервера}

<!--list-separator-->

1.  Настройки сервера ISC DHCP

    -   Настройки для сервера ISC DHCP.
    -   Файл конфигурации `/etc/dhcp/dhcpd.conf`.
    -   Настройка файлов загрузки:
        ```shell
        option architecture-type code 93 = unsigned integer 16;
        class "pxeclients" {
            match if substring (option vendor-class-identifier, 0, 9) = "PXEClient";
            if option architecture-type = 00:00 {
                    filename "/boot/pxelinux/bios/lpxelinux.0";
                } elsif option architecture-type = 00:09 {
                    filename "/boot/pxelinux/efi64/syslinux.efi";
                } elsif option architecture-type = 00:07 {
                    filename "/boot/pxelinux/efi64/syslinux.efi";
                } elsif option architecture-type = 00:06 {
                    filename "/boot/pxelinux/efi32/syslinux.efi";
                } else {
                    filename "/boot/pxelinux/bios/lpxelinux.0";
                }
        }
        ```

<!--list-separator-->

2.  Настройки сервера ISC Kea DHCP

    -   Настройки для сервера ISC Kea DHCP.
    -   Файл конфигурации `/etc/kea/kea-dhcp4.conf`.
    -   Настройка файлов загрузки:
        ```shell
        {
            "Dhcp4": {
                "client-classes": [
                    {
                        "name": "pxe-legacy",
                        "test": "option[93].hex == 0x0000",
                        "boot-file-name": "/boot/pxelinux/bios/lpxelinux.0"
                    },
                    {
                        "name": "pxe-uefi",
                        "test": "option[93].hex == 0x0009 or option[93].hex == 0x0007",
                        "boot-file-name": "/boot/pxelinux/efi64/syslinux.efi"
                    }
                ],
                ...
            }
        }
        ```


#### <span class="section-num">3.1.4</span> Файл конфигурации pxelinux {#файл-конфигурации-pxelinux}

-   Создать каталог `/var/lib/tftpboot/boot/pxelinux/pxelinux.cfg/`:
    ```shell
    mkdir -p /var/lib/tftpboot/boot/pxelinux/pxelinux.cfg
    ```
-   Создадим файл `/var/lib/tftpboot/boot/pxelinux/pxelinux.cfg/default`
    ```conf-unix
    # -*- mode:conf -*-
    default menu.c32
    ontimeout chain.c32 hd0
    timeout 100
    prompt 0
    implicit 1

    NOESCAPE 1
    ALLOWOPTIONS 0

    say Enter command line for bootup:
    menu title Syslinux Bootup
    label disk
    menu label ^Boot from local drive
    menu default
         kernel chain.c32
         append hd0
    ```
-   Создадим символические ссылки для разного типа загрузки:
    ```shell
    ln -s /var/lib/tftpboot/boot/pxelinux/pxelinux.cfg /var/lib/tftpboot/boot/pxelinux/bios/pxelinux.cfg
    ln -s /var/lib/tftpboot/boot/pxelinux/pxelinux.cfg /var/lib/tftpboot/boot/pxelinux/efi64/pxelinux.cfg
    ln -s /var/lib/tftpboot/boot/pxelinux/pxelinux.cfg /var/lib/tftpboot/boot/pxelinux/efi32/pxelinux.cfg
    ```


### <span class="section-num">3.2</span> ipxe {#ipxe}


#### <span class="section-num">3.2.1</span> Настройки DHCP-сервера {#настройки-dhcp-сервера}

-   Настройки для сервера ISC DHCP.
-   Файл конфигурации `/etc/dhcp/dhcpd.conf`.
-   Настройка файлов загрузки:
    ```shell
    option architecture-type code 93 = unsigned integer 16;
    class "pxeclients" {
        match if substring (option vendor-class-identifier, 0, 9) = "PXEClient";
        if option architecture-type != 00:00 {
                filename "/boot/ipxe/ipxe.efi";
            } else {
                filename "/boot/ipxe/undionly.kpxe";
            }
    }
    ```


### <span class="section-num">3.3</span> grub2 {#grub2}


#### <span class="section-num">3.3.1</span> Установка {#установка}

-   Установим необходимые пакеты для grub2:
    ```shell
    dnf -y install grub2-efi-x64-modules grub2-tools-extra grub2-pc-modules
    ```
-   Установим файлы в каталог tftpd:
    ```shell
    grub2-mknetdir --net-directory=/var/lib/tftpboot/
    restorecon -vR /var/lib/tftpboot
    ```
-   Можно также внедрить все модули в загружаемый файл (скорее, для отладки):
    ```conf-unix
    grub2-mkimage -O x86_64-efi -o /var/lib/tftpboot/boot/grub2/x86_64-efi/core.efi --prefix='' /var/lib/tftpboot/boot/grub2/x86_64-efi/*.mod
    ```


#### <span class="section-num">3.3.2</span> Настройки DHCP-сервера {#настройки-dhcp-сервера}

-   Настройки для сервера ISC DHCP.
-   Файл конфигурации `/etc/dhcp/dhcpd.conf`.
-   Настройка файлов загрузки:
    ```shell
    option architecture-type code 93 = unsigned integer 16;
    class "pxeclients" {
        match if substring (option vendor-class-identifier, 0, 9) = "PXEClient";
        if option architecture-type = 00:07 {
                filename "boot/grub2/x86_64-efi/core.efi";
            } else if option architecture-type = 00:08 {
                filename "boot/grub2/x86_64-efi/core.efi";
            } else if option architecture-type = 00:09 {
                filename "boot/grub2/x86_64-efi/core.efi";
            } else if option architecture-type = 00:0a {
                # ArmHFP
                filename "boot/grub2/armv7a-efi/core.efi";
            } else if option architecture-type = 00:0b {
                # aarch64
                filename "boot/grub2/aarch64-efi/core.efi";
            } else {
                # BIOS boot
                filename "boot/grub2/i386-pc/core.0";
            }
    }
    ```


#### <span class="section-num">3.3.3</span> Файл конфигурации grub {#файл-конфигурации-grub}

-   Создадим основной файл конфигурации:
    ```shell
    touch /var/lib/tftpboot/boot/grub2/grub.cfg
    ```
-   Создадим в нём базовую конфигурацию:
    ```conf-unix
    set default=0
    set timeout=60

    menuentry 'Local Boot' {
        exit
    }
    ```
-   Создадим символическую ссылку на этот файл в каждом каталоге, содержащим `core.*`:
    ```shell
    cd /var/lib/tftpboot/boot/grub2/x86_64-efi; ln -snf ../grub.cfg
    cd /var/lib/tftpboot/boot/grub2/i386-pc; ln -snf ../grub.cfg
    ```
-   Можно добавить дополнительные пункты (скорее для забавы):
    ```conf-unix
    menuentry 'EFI Firmware System Setup' $menuentry_id_option 'uefi-firmware' {
      fwsetup
    }

    menuentry 'Reboot' {
      reboot
    }

    menuentry 'Shutdown' {
      halt
    }
    ```


## <span class="section-num">4</span> Приложения {#приложения}


### <span class="section-num">4.1</span> Memtest86+ {#memtest86-plus}

-   Сайт: <https://memtest.org/>
-   Скачайте необходимую версию:
    ```shell
    mkdir -p /var/lib/tftpboot/utils/memtest
    cd /var/lib/tftpboot/utils/memtest
    wget https://memtest.org/download/v6.20/mt86plus_6.20.binaries.zip
    unzip mt86plus_6.20.binaries.zip
    rm mt86plus_6.20.binaries.zip
    ```


#### <span class="section-num">4.1.1</span> pxelinux {#pxelinux}

-   Конфигурация для загрузки memtest86+ будет следующей:
    ```conf-unix
    label memtest
    menu label Memory test
        kernel utils/memtest/memtest64.bin
    ```


#### <span class="section-num">4.1.2</span> grub {#grub}

-   Конфигурация для загрузки memtest86+ будет следующей:
    ```shell
    menuentry "Memory test" --class tools {
        if [ "${grub_platform}" = pc ]; then
            linux (http)/utils/memtest/memtest64.bin
        else
            linuxefi (http)/utils/memtest/memtest64.efi
        fi
    }
    ```


## <span class="section-num">5</span> Дистрибутивы Linux {#дистрибутивы-linux}


### <span class="section-num">5.1</span> Fedora {#fedora}

-   Сайт: <https://fedoraproject.org/>


#### <span class="section-num">5.1.1</span> Grub {#grub}

-   Файл конфигурации будет следующим:
    ```conf-unix
    submenu 'Fedora Linux' --class fedora --class gnu-linux --class gnu --class os {

       menuentry 'Install Fedora Linux (EFI)' --class fedora --class gnu-linux --class gnu --class os {
         linuxefi fedora-x86_64/vmlinuz inst.repo=http://dl.fedoraproject.org/pub/fedora/linux/releases/39/Everything/x86_64/os inst.stage2=http://dl.fedoraproject.org/pub/fedora/linux/releases/39/Everything/x86_64/os ip=dhcp
         initrdefi fedora-x86_64/initrd.img
       }
       menuentry 'Install Fedora Linux (Classic)' --class fedora --class gnu-linux --class gnu --class os {
         linux16 fedora-x86_64/vmlinuz inst.repo=http://dl.fedoraproject.org/pub/fedora/linux/releases/39/Everything/x86_64/os/ inst.stage2=http://dl.fedoraproject.org/pub/fedora/linux/releases/39/Everything/x86_64/os/ ip=dhcp
         initrd16 fedora-x86_64/initrd.img
       }
       menuentry 'Install Fedora Linux (ARM)' --class fedora --class gnu-linux --class gnu --class os {
         linux fedora-aarch64/vmlinuz inst.repo=http://dl.fedoraproject.org/pub/fedora/linux/releases/39/Everything/aarch64/os/ inst.stage2=http://dl.fedoraproject.org/pub/fedora/linux/releases/39/Everything/aarch64/os/ ip=dhcp
         initrd fedora-aarch64/initrd.img
       }
    }
    ```
