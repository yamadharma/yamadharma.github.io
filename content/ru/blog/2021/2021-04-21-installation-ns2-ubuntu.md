---
title: "Установка NS-2. Ubuntu"
author: ["Dmitry S. Kulyabov"]
date: 2021-04-21T13:31:00+03:00
lastmod: 2023-10-09T09:59:00+03:00
tags: ["modeling"]
categories: ["computer-science"]
draft: false
slug: "installation-ns2-ubuntu"
---

Установка NS-2 на Ubuntu.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Установка операционной системы на виртуальную машину {#установка-операционной-системы-на-виртуальную-машину}

Установка Ubuntu на виртуальную машину не представляет никакого затруднения.


### <span class="section-num">1.1</span> Установка дополнений Virtualbox {#установка-дополнений-virtualbox}

Для установки дополнений _VirtualBox_ необходимо установить компилятор и заголовочные файлы ядра:

```shell
sudo -i
apt-get install build-essential linux-headers-`uname -r`
```

{{< youtube IohW96hlkdE >}}


### <span class="section-num">1.2</span> Настройка общих папок Virtualbox {#настройка-общих-папок-virtualbox}

-   Щёлкните правой кнопкой мыши свою виртуальную машину, затем нажмите «Настройки».
-   Перейти в раздел общих папок.
-   Добавьте новую общую папку.
-   В приглашении «Добавить общий ресурс» выберите путь к папке на вашем хосте, который должен быть доступен внутри вашей виртуальной машины.
-   В поле «Имя папки» введите `shared` (или любое имя, какое желаете).
-   Снимите флажок «Только для чтения» и «Автоматическое монтирование» и установите флажок «Сделать постоянным».
-   Создайте общий каталог в вашем домашнем каталоге:
    ```shell
    mkdir ~/shared
    ```
-   Смонтируйте общую папку с хоста в ваш каталог:
    ```shell
    sudo mount -t vboxsf -o uid=`id -u`,gid=`id -g` shared ~/shared
    ```
-   Можно добавить команду монтирования в файл `/etc/fstab`:
    ```conf-unix
    shared /home/<username>/shared vboxsf defaults,uid=<your_uid>,gid=<your_gid> 0 0
    ```

    {{< youtube TT6FmbqhW-s >}}


## <span class="section-num">2</span> Установка необходимого программного обеспечения {#установка-необходимого-программного-обеспечения}

Для компиляции NS-2 необходимо установить компилятор и библиотеки.

-   Перейдём в режим суперпользователя:
    ```shell
    sudo -i
    ```

-   Установим основные средства разработки:
    ```shell
    apt-get install build-essential
    ```
-   Установим файловый менеджер `mc` (это не обязательно):
    ```shell
    apt-get install mc
    ```
-   Установим `git`:
    ```shell
    apt-get install git
    ```
-   Установим `cmake`:
    ```shell
    apt-get install cmake
    ```
-   Установим `automake`:
    ```shell
    apt-get install automake
    ```
-   Установим файлы для разработки под X11:
    ```shell
    apt-get install xorg-dev
    ```


## <span class="section-num">3</span> Компиляция NS-2 {#компиляция-ns-2}

-   Создадим каталог для компиляции:
    ```shell
    mkdir ~/compile
    ```
-   Скачаем исходники NS-2:
    ```shell
    cd ~/compile
    git clone https://github.com/yamadharma/ns-allinone.git
    ```
-   Откомпилим исходные коды NS-2:
    ```shell
    cd ns-allinone
    ./install
    ```
-   В результате получим исполняемые файлы в каталоге `~/compile/ns-allinone/bin`.

    {{< youtube yG-J5EdZyxU >}}
