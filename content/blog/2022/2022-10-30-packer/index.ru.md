---
title: "Packer"
author: ["Dmitry S. Kulyabov"]
date: 2022-10-30T19:00:00+03:00
lastmod: 2024-07-19T13:26:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "packer"
---

Утилита для создания образов операционных систем Packer.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.packer.io/>.
-   Репозиторий: <https://github.com/hashicorp/packer>.
-   Бинарные сборки: <https://releases.hashicorp.com/packer> (на данный момент не доступно из России).
-   Зеркало бинарных сборок:
    -   <https://hashicorp-releases.yandexcloud.net/packer/>
    -   <https://hashicorp-releases.mcs.mail.ru/packer/>
    -   <https://sourceforge.net/projects/packer.mirror/files/>


### <span class="section-num">1.1</span> Лицензия {#лицензия}

-   [Смена лицензии HashiCorp]({{< relref "2023-09-21-hashicorp-changes-license" >}})


## <span class="section-num">2</span> Необходимое программное обеспечение {#необходимое-программное-обеспечение}


### <span class="section-num">2.1</span> Virtualbox {#virtualbox}

-   [Система виртуализации VirtualBox]({{< relref "2021-09-17-virtualbox-virtualization-system" >}})
-   Необходимо для создания образов для VirtualBox.
-   Особенности: Использование драйверов под операционную систему (VBoxGuestAdditions)


### <span class="section-num">2.2</span> VmWare {#vmware}

-   Необходимо для создания образов для Vmware.


### <span class="section-num">2.3</span> VMware open-vm-tools {#vmware-open-vm-tools}

-   Необходимо для создания образов для Vmware.
-   Предоставляет набор утилит и драйверов виртуализации с открытым исходным кодом для улучшения функциональности и удобства виртуализации в рамках виртуализации VMware.
-   Репозиторий: <https://github.com/vmware/open-vm-tools>
-   Сайт: <https://sourceforge.net/projects/open-vm-tools/>


## <span class="section-num">3</span> Установка {#установка}


### <span class="section-num">3.1</span> Linux {#linux}

-   Gentoo:
    ```shell
    emerge dev-util/packer
    ```


### <span class="section-num">3.2</span> Windows {#windows}

-   Установка с помощью Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
    ```shell
    choco install packer
    ```


## <span class="section-num">4</span> Скрипты развёртывания {#скрипты-развёртывания}

-   Ранее использовался язык описания JSON.
-   После _Packer-1.5_ используется формат HCL2.


## <span class="section-num">5</span> Плагины {#плагины}

-   Ранее код плагинов был включён в packer.
-   Сейчас их необходимо устанавливать отдельно.


### <span class="section-num">5.1</span> Vagrant {#vagrant}

-   Документация: <https://developer.hashicorp.com/packer/integrations/hashicorp/vagrant>
-   Репозиторий: <https://github.com/hashicorp/packer-plugin-vagrant>


#### <span class="section-num">5.1.1</span> Установка {#установка}

-   Добавьте код в конфигурацию packer
    ```hcl
    packer {
      required_plugins {
        vagrant = {
          version = "~> 1"
          source = "github.com/hashicorp/vagrant"
        }
      }
    }
    ```

    -   Инициализируйте packer:
        ```shell
        packer init
        ```

-   Можно установить из командной строки:
    ```shell
    packer plugins install github.com/hashicorp/vagrant
    ```


### <span class="section-num">5.2</span> Virtualbox {#virtualbox}

-   Репозиторий: <https://github.com/hashicorp/packer-plugin-virtualbox>
-   Документация: <https://developer.hashicorp.com/packer/integrations/hashicorp/virtualbox>


#### <span class="section-num">5.2.1</span> Установка {#установка}

-   Добавьте код в конфигурацию packer
    ```hcl
    packer {
      required_plugins {
        virtualbox = {
          version = "~> 1"
          source  = "github.com/hashicorp/virtualbox"
        }
      }
    }
    ```

    -   Инициализируйте packer:
        ```shell
        packer init
        ```

-   Можно установить из командной строки:
    ```shell
    packer plugins install github.com/hashicorp/virtualbox
    ```


#### <span class="section-num">5.2.2</span> Компоненты {#компоненты}

-   Плагин поставляется с несколькими сборщиками, способными создавать VirtualBox:
    -   `virtualbox-iso`:
        -   запускается с ISO файла,
        -   создаёт новую виртуальную машину VirtualBox,
        -   устанавливает ОС,
        -   подготавливает программное обеспечение в ОС,
        -   экспортирует эту машину для создания образа.
    -   `virtualbox-ovf`:
        -   импортирует существующий файл OVF/OVA;
        -   запускает средства подготовки поверх этой виртуальной машины;
        -   экспортирует машину для создания образа.
    -   `virtualbox-vm`:
        -   использует существующую виртуальную машину для запуска определённых поставщиков поверх этой виртуальной машины;
        -   при необходимости, создает снимок для сохранения изменений, внесенных поставщиками услуг;
        -   может экспортировать эту машину для создания образа.


## <span class="section-num">6</span> Примеры скриптов развёртывания {#примеры-скриптов-развёртывания}


### <span class="section-num">6.1</span> Установка Rocky Linux 9.4 {#установка-rocky-linux-9-dot-4}

-   Скрипт `vagrant-rocky.pkr.hcl`:
    ```hcl
    packer {
      required_plugins {
        vagrant = {
          source  = "github.com/hashicorp/vagrant"
          version = "~> 1"
        }
        virtualbox = {
          version = "~> 1"
          source  = "github.com/hashicorp/virtualbox"
        }
      }
    }

    variable "artifact_description" {
      type    = string
      default = "Rocky 9.4"
    }

    variable "artifact_version" {
      type    = string
      default = "9.4"
    }

    variable "disk_size" {
      type    = string
      default = "61440"
    }

    variable "iso_checksum" {
      type    = string
      default = "ee3ac97fdffab58652421941599902012179c37535aece76824673105169c4a2"
    }

    variable "iso_checksum_type" {
      type    = string
      default = "sha256"
    }

    variable "iso_url" {
      type    = string
      default = "Rocky-9.4-x86_64-minimal.iso"
    }

    variable "redhat_platform" {
      type    = string
      default = "x86_64"
    }

    variable "redhat_release" {
      type    = string
      default = "9"
    }

    variable "ssh_password" {
      type    = string
      default = "vagrant"
    }

    variable "ssh_username" {
      type    = string
      default = "vagrant"
    }

    source "virtualbox-iso" "virtualbox" {
      boot_command            = [
        "<esc>",
        "<wait><esc><esc>",
        "linux inst.ks=http://{{.HTTPIP}}:{{.HTTPPort}}/ks.cfg biosdevname=0 net.ifnames=0",
        "<enter>"
      ]
      boot_wait               = "30s"
      disk_size               = "${var.disk_size}"
      export_opts             = [
        "--manifest",
        "--vsys", "0",
        "--description", "${var.artifact_description}",
        "--version", "${var.artifact_version}"
      ]
      guest_additions_path    = "VBoxGuestAdditions.iso"
      guest_os_type           = "RedHat_64"
      hard_drive_interface    = "sata"
      http_directory          = "${path.root}/http"
      iso_checksum            = "${var.iso_checksum_type}:${var.iso_checksum}"
      iso_url                 = "${var.iso_url}"
      output_directory        = "builds"
      shutdown_command        = "sudo -S /sbin/halt -h -p"
      shutdown_timeout        = "5m"
      ssh_password            = "${var.ssh_password}"
      ssh_username            = "${var.ssh_username}"
      ssh_port                = 22
      ssh_pty                 = true
      ssh_timeout             = "60m"
      vboxmanage              = [
        ["modifyvm", "{{.Name}}", "--memory", "2048"],
        ["modifyvm", "{{.Name}}", "--cpus", "2"],
        ["modifyvm", "{{.Name}}", "--nat-localhostreachable1", "on"]
      ]
      virtualbox_version_file = ".vbox_version"
      vm_name                 = "packer-rocky-virtualbox-vm"
    }

    build {
      sources = ["source.virtualbox-iso.virtualbox"]

      provisioner "shell" {
        execute_command = "echo 'packer'|{{ .Vars }} sudo -S -E bash '{{ .Path }}'"
        inline          = [
          "sleep 30",
          "sudo dnf -y install epel-release",
          "sudo dnf -y groupinstall 'Development Tools'",
          "sudo dnf -y install kernel-devel",
          "sudo dnf -y install dkms",
          "sudo mkdir /tmp/vboxguest",
          "sudo mount -t iso9660 -o loop /home/vagrant/VBoxGuestAdditions.iso /tmp/vboxguest",
          "cd /tmp/vboxguest",
          "sudo ./VBoxLinuxAdditions.run",
          "cd /tmp",
          "sudo umount /tmp/vboxguest",
          "sudo rmdir /tmp/vboxguest",
          "rm /home/vagrant/VBoxGuestAdditions.iso",
          "sudo systemctl enable --now vboxadd.service",
          "sudo dnf -y install lightdm",
          "sudo dnf -y groupinstall 'Server with GUI'",
          "sudo dnf install -y mc htop tmux",
          "sudo systemctl set-default graphical.target",
          "echo Image Provisioned!"
        ]
      }

      post-processor "vagrant" {
        compression_level = "6"
        output            = "vagrant-virtualbox-rocky-${var.redhat_release}-${var.redhat_platform}.box"
      }
    }


    ```
-   `Makefile` для Virtualbox:
    ```makefile
    .PHONY: version

    all: help

    init: ## Install missing plugins for packer
            @mkdir -p ""`pwd`"/.config/packer/plugins"
            @export PACKER_CONFIG_DIR=""`pwd`"/.config/packer"; export PACKER_PLUGIN_PATH=""`pwd`"/.config/packer/plugins"; packer init vagrant-rocky.pkr.hcl

    box:	init    ## Build box for Rocky Linux
            -@VBoxManage setproperty language C
            @VBoxManage setproperty machinefolder "`pwd`"/vm
            @export TMPDIR=""`pwd`""; export PACKER_CONFIG_DIR=""`pwd`"/.config/packer"; export PACKER_PLUGIN_PATH=""`pwd`"/.config/packer/plugins"; packer build -only=virtualbox-iso.virtualbox vagrant-rocky.pkr.hcl
            @VBoxManage setproperty machinefolder default

    help:
            @echo 'Usage:'
            @echo '  make <target>'
            @echo
            @echo 'Targets:'
            @grep -E '^[a-zA-Z_0-9.-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2}'
            @echo

    ```
-   `Makefile` для Vmware:
    ```makefile
    .PHONY: version

    all: init box

    init: ## Install missing plugins for packer
            @packer init vagrant-rocky.pkr.hcl

    box:    ## Build box for Rocky Linux
            @export TMPDIR=`pwd`; export LANG=C; packer build -only=vmware-iso.vmware vagrant-rocky.pkr.hcl

    help:
            @echo 'Usage:'
            @echo '  make <target>'
            @echo
            @echo 'Targets:'
            @grep -E '^[a-zA-Z_0-9.-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2}'
            @echo
    ```
