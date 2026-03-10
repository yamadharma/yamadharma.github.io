---
title: "Использование vagrant. Установка Rocky Linux"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-20T19:00:00+03:00
lastmod: 2024-05-19T18:26:00+03:00
tags: ["sysadmin", "redhat"]
categories: ["computer-science"]
draft: false
slug: "using-vagrant-install-rocky-linux"
---

Установка Rocky Linux из репозитория образов Vagrant.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Будем использовать официальные образы RockyLinux: <https://app.vagrantup.com/rockylinux>
-   Для определённости выберем следующую версию: <https://app.vagrantup.com/rockylinux/boxes/9/versions/3.0.0>
-   Название образа: `rockylinux/9`.


## <span class="section-num">2</span> Установка для Virtualbox {#установка-для-virtualbox}


### <span class="section-num">2.1</span> Скачивание файла {#скачивание-файла}

-   Поскольку в России блокируется автоматическая скачка файла, то необходимо скачать его вручную (скачивается, поскольку этот ссылка на сайт Rocky Linux):
    ```shell
    wget https://app.vagrantup.com/rockylinux/boxes/9/versions/3.0.0/providers/virtualbox.box
    ```
-   Можно скачать и со страницы <https://app.vagrantup.com/rockylinux/boxes/9> непосредственно.
-   Можно скачать с сайта Rocky Linux: <https://dl.rockylinux.org/pub/rocky/9.3/images/x86_64/>.


### <span class="section-num">2.2</span> Установка дополнения для Vagrant {#установка-дополнения-для-vagrant}

-   Дополнение автоматически устанавливает гостевые дополнения VirtualBox хоста в гостевой системе.
-   Установим дополнение, явно указав зеркало для загрузки:
    ```shell
    vagrant plugin install --plugin-clean-sources --plugin-source https://rubygems.org vagrant-vbguest
    ```


### <span class="section-num">2.3</span> Vagrantfile {#vagrantfile}

-   Создадим заготовку файла Vagrantfile:
    ```shell
    vagrant init rockylinux/9 --box-version 3.0.0
    ```


### <span class="section-num">2.4</span> Подключение образа {#подключение-образа}

-   Подключим скачанный файл образа:
    ```shell
    vagrant box add rockylinux/9 virtualbox.box
    ```


### <span class="section-num">2.5</span> Образ Virtualbox {#образ-virtualbox}

-   Создадим образ Virtualbox и запустим его:
    ```shell
    vagrant up
    ```


### <span class="section-num">2.6</span> Подключитесь к системе {#подключитесь-к-системе}

-   Войдём в консоль системы по ssh:
    ```shell
    vagrant ssh
    ```


### <span class="section-num">2.7</span> Обновление системы {#обновление-системы}

-   Перейдём под учётную запись `root`:
    ```shell
    su -
    ```
-   Пароль учётной записи `root`: `vagrant`.
-   Обновим установленную систему:
    ```shell
    dnf update
    ```
-   Установим дополнительное программное обеспечение:
    ```shell
    dnf install tmux
    ```


### <span class="section-num">2.8</span> Перезагрузка виртуальной машины {#перезагрузка-виртуальной-машины}

-   Выйдем из оболочки машины:
    ```shell
    logout
    logout
    ```
-   Перезагрузим виртуальную машину:
    ```shell
    vagrant reload
    ```


### <span class="section-num">2.9</span> Выключение виртуальной машины {#выключение-виртуальной-машины}

-   После работы выключите виртуальную машину:
    ```shell
    vagrant halt
    ```


### <span class="section-num">2.10</span> Видео {#видео}

{{< tabs tabTotal="3" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 7ef1a4fdb0db4b4fd2edcad6bbf46f65 >}}

{{< /rtab >}}
{{< rtab tabName="VKVideo" >}}

{{< vkvideo oid="606414976" id="456239563" hd="2"  >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube vTkYacxvhoc >}}

{{< /rtab >}}
{{< /tabs >}}
