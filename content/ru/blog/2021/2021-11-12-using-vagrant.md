---
title: "Использование vagrant"
author: ["Dmitry S. Kulyabov"]
date: 2021-11-12T12:11:00+03:00
lastmod: 2023-10-11T16:21:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "using-vagrant"
---

Использование vagrant.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.vagrantup.com/>
-   Репозиторий: <https://github.com/hashicorp/vagrant>
-   Бинарные сборки: <https://releases.hashicorp.com/vagrant> (на данный момент не доступно из России).
-   Зеркало бинарных сборок:
    -   <https://hashicorp-releases.yandexcloud.net/vagrant/>
    -   <https://hashicorp-releases.mcs.mail.ru/vagrant/>
-   Зеркало сборок из репозитория:
    -   <https://sourceforge.net/projects/vagrant.mirror/files/>
-   Репозиторий образов для Vagrant: <https://app.vagrantup.com/>


### <span class="section-num">1.1</span> Лицензия {#лицензия}

-   [Смена лицензии HashiCorp]({{< relref "2023-09-21-hashicorp-changes-license" >}})


### <span class="section-num">1.2</span> Ответвления {#ответвления}

-   Смена лицензии привела к возникновению форка под лицензией MPL.
-   Репозиторий: <https://github.com/viagrunts/viagrunts>


### <span class="section-num">1.3</span> Основные понятия Vagrant {#основные-понятия-vagrant}

-   провайдер (provider) --- система виртуализации, с которой работает Vagrant (например, VirtualBox, VMWare и т.п.);
-   box-файл (или Vagrant Box) --- сохранённый образ виртуальной машины с развёрнутой в ней операционной системой; по сути, box-файл используется как основа для клонирования виртуальных машин с теми или иными настройками;
-   Vagrantfile --- конфигурационный файл, написанный на языке Ruby, в котором указаны настройки запуска виртуальной машины.


### <span class="section-num">1.4</span> Основные команды Vagrant {#основные-команды-vagrant}

-   С Vagrant можно работать, используя следующие основные команды:
    -   `vagrant help` --- вызов справки по командам Vagrant;
    -   `vagrant box list` --- список подключённых к Vagrant box-файлов;
    -   `vagrant box add` --- подключение box-файла к Vagrant;
    -   `vagrant destroy` --- отключение box-файла от Vagrant и удаление его из виртуального окружения;
    -   `vagrant init` --- создание <span class="org-target" id="org-target-----------"></span> конфигурационного файла `Vagrantfile` для его последующего изменения;
    -   `vagrant up` --- запуск виртуальной машины с использованием инструкций по запуску из конфигурационного файла `Vagrantfile`;
    -   `vagrant reload` --- перезагрузка виртуальной машины;
    -   `vagrant halt` --- остановка и выключение виртуальной машины;
    -   `vagrant provision` --- настройка внутреннего окружения имеющейся виртуальной машины (например, добавление новых инструкций (скриптов) в ранее созданную виртуальную машину);
    -   `vagrant ssh` --- подключение к виртуальной машине через ssh.


### <span class="section-num">1.5</span> Пример конфигурации Vagrantfile {#пример-конфигурации-vagrantfile}

-   Пример содержимого файла `Vagrantfile` для понимания принципов его синтаксиса.

<!--listend-->

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
  config.vm.box = "BOX_NAME"
  config.vm.hostname = "HOST_NAME"
  config.vm.network "private_network", ip: "192.168.1.1"
  config.vm.define "VM_NAME"
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end
end
```

-   Первые две строки указывают на режим работы с `Vagrantfile` и использование языка Ruby.
-   Затем идёт цикл `do`, заменяющий конструкцию `Vagrant.configure` далее по тексту на `config`.
-   Строка `config.vm.box = "BOX_NAME"` задаёт название образа (box-файла) виртуальной машины (обычно выбирается из официального репозитория).
-   Строка `config.vm.hostname = "HOST_NAME"` задаёт имя виртуальной машины.
-   Конструкция `config.vm.network` задаёт тип сетевого соединения и может иметь следующие назначения:
    -   `config.vm.network "private_network", ip: "xxx.xxx.xxx.xxx"` --- адрес из внутренней сети;
    -   `config.vm.network "public_network", ip: "xxx.xxx.xxx.xxx"` --- публичный адрес, по которому виртуальная машина будет доступна;
    -   `config.vm.network "private_network", type: "dhcp"` --- адрес, назначаемый по протоколу DHCP.
-   Строка `config.vm.define "VM_NAME"` задаёт название виртуальной машины, по которому можно обращаться к ней из Vagrant и VirtualBox.
-   В конце идёт конструкция, определяющая параметры провайдера, а именно запуск виртуальной машины без графического интерфейса и с выделением 1 ГБ памяти.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Linux {#linux}

-   Gentoo:
    ```shell
    emerge app-emulation/vagrant
    ```


### <span class="section-num">2.2</span> Windows {#windows}

-   Установка с помощью Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
    ```shell
    choco install vagrant
    ```


## <span class="section-num">3</span> Принципы работы {#принципы-работы}

-   [Сеть в vagrant]({{< relref "2023-10-11-vagrant-network" >}})


## <span class="section-num">4</span> Подготовка образа {#подготовка-образа}


### <span class="section-num">4.1</span> Общая информация {#общая-информация}

-   Подготовка образа проводится с помощью _Packer_ (см. [Packer]({{< relref "2022-10-30-packer" >}})).
-   Сайт: <https://www.packer.io/>


### <span class="section-num">4.2</span> Описание установки {#описание-установки}

-   Ранее использовался язык описания JSON.
-   После _Packer-1.5_ используется формат HCL2.


## <span class="section-num">5</span> Установка дополнений {#установка-дополнений}

-   Список дополнений: <https://github.com/hashicorp/vagrant/wiki/Available-Vagrant-Plugins>
-   Установка дополнения:
    ```shell
    vagrant plugin install <plugin-name>
    ```
-   Дополнение скачивается с сайта .
-   Поскольку доступ из России блокируется, следует явно указать зеркало для загрузки дополнений:
    ```shell
    vagrant plugin install --plugin-clean-sources --plugin-source https://rubygems.org <plugin-name>
    ```


## <span class="section-num">6</span> Разные системы виртуализации {#разные-системы-виртуализации}

-   [Использование vagrant. Virtualbox]({{< relref "2023-08-20-using-vagrant-virtualbox" >}})


## <span class="section-num">7</span> Конкретные примеры {#конкретные-примеры}

-   [Использование vagrant. Установка Rocky Linux]({{< relref "2023-08-20-using-vagrant-install-rocky-linux" >}})
