---
title: "Использование vagrant. Virtualbox"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-20T18:28:00+03:00
lastmod: 2023-08-20T18:59:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "using-vagrant-virtualbox"
---

Использование vagrant с системой виртуализации Virtual Box.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Запуск Vagrant в текущем каталоге для VirtualBox {#запуск-vagrant-в-текущем-каталоге-для-virtualbox}

-   Если необходимо, чтобы все файлы находились в рабочем каталоге, то следует установить дополнительные переменные среды.


### <span class="section-num">1.1</span> Запуск Vagrant под Windows в текущем каталоге для VirtualBox {#запуск-vagrant-под-windows-в-текущем-каталоге-для-virtualbox}

-   Следует задать переменные окружения
    ```shell
    setx VAGRANT_HOME "X:/your/path/.vagrant.d" /M
    setx VAGRANT_DOTFILE_PATH "X:/your/path/.vagrant" /M
    setx VBOX_USER_HOME "X:/your/path/.vbox" /M
    setx VBOX_INSTALL_PATH "X:/your/path/vm" /M
    ```

    -   Вместо `X:` необходимо записать букву необходимого диска.
    -   Команда `setx` добавляет переменные в постоянный список переменных окружения.
    -   Модификатор `/M` добавляет переменные в системное окружение.
    -   Без этого модификатора переменные будут добавляться в окружение пользователя.


### <span class="section-num">1.2</span> Запуск Vagrant под Linux в текущем каталоге для VirtualBox {#запуск-vagrant-под-linux-в-текущем-каталоге-для-virtualbox}

-   Предлагается вместо явного задания переменных окружения использовать Makefile:

<!--listend-->

```makefile
.PHONY: version

help:
        @echo 'Usage:'
        @echo '  make <target>'
        @echo
        @echo 'Targets:'
        @grep -E '^[a-zA-Z_0-9.-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2}'
        @echo

add:	## Add the built box to Vagrant
        @export VAGRANT_HOME=`pwd`/.vagrant.d; export VAGRANT_DOTFILE_PATH=`pwd`/.vagrant; vagrant box add rocky9 vagrant-virtualbox-rocky-9-x86_64.box

up:     ## Up boxies
        @VBoxManage setproperty machinefolder `pwd`/vm
        -@export VAGRANT_HOME=`pwd`/.vagrant.d; export VAGRANT_DOTFILE_PATH=`pwd`/.vagrant; export VBOX_USER_HOME=`pwd`/.vbox; export VBOX_INSTALL_PATH=`pwd`/vm; vagrant up
        @VBoxManage setproperty machinefolder default

server:	## Up server
        @VBoxManage setproperty machinefolder `pwd`/vm
        -@export VAGRANT_HOME=`pwd`/.vagrant.d; export VAGRANT_DOTFILE_PATH=`pwd`/.vagrant; export VBOX_USER_HOME=`pwd`/.vbox; export VBOX_INSTALL_PATH=`pwd`/vm; vagrant up server
        @VBoxManage setproperty machinefolder default

client:	## Up client
        @VBoxManage setproperty machinefolder `pwd`/vm
        -@export VAGRANT_HOME=`pwd`/.vagrant.d; export VAGRANT_DOTFILE_PATH=`pwd`/.vagrant; export VBOX_USER_HOME=`pwd`/.vbox; export VBOX_INSTALL_PATH=`pwd`/vm; vagrant up client
        @VBoxManage setproperty machinefolder default

server-provision:	## Up and provision server
        @VBoxManage setproperty machinefolder `pwd`/vm
        -@export VAGRANT_HOME=`pwd`/.vagrant.d; export VAGRANT_DOTFILE_PATH=`pwd`/.vagrant; export VBOX_USER_HOME=`pwd`/.vbox; export VBOX_INSTALL_PATH=`pwd`/vm; vagrant up server --provision
        @VBoxManage setproperty machinefolder default

client-provision:	## Up and provision client
        @VBoxManage setproperty machinefolder `pwd`/vm
        -@export VAGRANT_HOME=`pwd`/.vagrant.d; export VAGRANT_DOTFILE_PATH=`pwd`/.vagrant; export VBOX_USER_HOME=`pwd`/.vbox; export VBOX_INSTALL_PATH=`pwd`/vm; vagrant up client --provision
        @VBoxManage setproperty machinefolder default

server-destroy:	## Destroy server
        @VBoxManage setproperty machinefolder `pwd`/vm
        -@export VAGRANT_HOME=`pwd`/.vagrant.d; export VAGRANT_DOTFILE_PATH=`pwd`/.vagrant; export VBOX_USER_HOME=`pwd`/.vbox; export VBOX_INSTALL_PATH=`pwd`/vm; vagrant destroy server
        @VBoxManage setproperty machinefolder default

client-destroy:	## Destroy client
        @VBoxManage setproperty machinefolder `pwd`/vm
        -@export VAGRANT_HOME=`pwd`/.vagrant.d; export VAGRANT_DOTFILE_PATH=`pwd`/.vagrant; export VBOX_USER_HOME=`pwd`/.vbox; export VBOX_INSTALL_PATH=`pwd`/vm; vagrant destroy client
        @VBoxManage setproperty machinefolder default
```


## <span class="section-num">2</span> Используемые расширения для Vagrant {#используемые-расширения-для-vagrant}


### <span class="section-num">2.1</span> vagrant-vbguest {#vagrant-vbguest}

-   Репозиторий: <https://github.com/dotless-de/vagrant-vbguest>
-   Автоматически устанавливает гостевые дополнения VirtualBox хоста в гостевой системе.
-   Установка дополнения:
    ```shell
    vagrant plugin install vagrant-vbguest
    ```
-   Установка дополнения с явно указанным зеркалом для загрузки:
    ```shell
    vagrant plugin install --plugin-clean-sources --plugin-source https://rubygems.org vagrant-vbguest
    ```
