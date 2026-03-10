---
title: "Сборка образа VyOS"
author: ["Dmitry S. Kulyabov"]
date: 2023-07-06T16:38:00+03:00
lastmod: 2023-10-26T17:40:00+03:00
tags: ["network"]
categories: ["computer-science"]
draft: false
slug: "vyos-build"
---

Самостоятельная сборка образа VyOS.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Из-за модели распространения VyOS становится оправданной самостоятельная сборка.
    -   VyOS является проектом с открытым исходным кодом, но ISO-образы могут быть получены только по подписке или путем внесения вклада в сообщество.
-   Текущая стабильная версия: 1.3.4 (<https://blog.vyos.io/vyos-1.3.4-lts-release>).
-   Описание сборки VyOS: <https://docs.vyos.io/en/equuleus/contributing/build-vyos.html>


## <span class="section-num">2</span> Сборка {#сборка}

-   Разработчики рекомендуют использование для сборки окружения в docker.


### <span class="section-num">2.1</span> Установка docker {#установка-docker}


#### <span class="section-num">2.1.1</span> Установка {#установка}

-   Debian:
    ```shell
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install -y docker-ce
    ```
-   Ubuntu:
    ```shell
    sudo apt-get update
    sudo apt-get -y install \
      ca-certificates \
      curl \
      gnupg \
      lsb-release
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    ```
-   Fedora:
    ```shell
    sudo dnf -y install dnf-plugins-core
    sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
    sudo dnf install -y docker-ce docker-ce-cli containerd.io
    ```
-   CentOS:
    ```shell
    sudo yum install -y yum-utils
    sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    sudo yum install -y docker-ce docker-ce-cli containerd.io
    ```
-   Gentoo:
    ```shell
    emerge app-containers/docker app-containers/docker-cli
    ```


#### <span class="section-num">2.1.2</span> Запуск {#запуск}

-   Запустите docker:
    ```shell
    systemctl start docker.service
    ```


#### <span class="section-num">2.1.3</span> Конфигурация {#конфигурация}

-   Текущего пользователя без полномочий `root` необходимо добавить в группу `docker`:
    ```shell
    usermod -aG docker yourusername
    ```


### <span class="section-num">2.2</span> Контейнер со сборочным окружением {#контейнер-со-сборочным-окружением}

-   Контейнер можно создать вручную или загрузить готовый из DockerHub (<https://hub.docker.com/>).


#### <span class="section-num">2.2.1</span> Загрузка контейнера из DockerHub {#загрузка-контейнера-из-dockerhub}

-   Чтобы загрузить контейнер из DockerHub, запустите:
    -   VyOS 1.2
        ```shell
        docker pull vyos/vyos-build:crux
        ```
    -   VyOS 1.3
        ```shell
        docker pull vyos/vyos-build:equuleus
        ```
    -   VyOS 1.4
        ```shell
        docker pull vyos/vyos-build:sagitta
        ```
    -   VyOS 1.5 (rolling release)
        ```shell
        docker pull vyos/vyos-build:current
        ```


### <span class="section-num">2.3</span> Подготовка среды сборки {#подготовка-среды-сборки}

-   Загрузите сборочный код:
    -   VyOS 1.2
        ```shell
        git clone -b crux --single-branch https://github.com/vyos/vyos-build
        ```
    -   VyOS 1.3
        ```shell
        git clone -b equuleus --single-branch https://github.com/vyos/vyos-build
        ```
    -   VyOS 1.4
        ```shell
        git clone -b sagitta --single-branch https://github.com/vyos/vyos-build
        ```
    -   VyOS 1.5 (rolling release)
        ```shell
        git clone -b current --single-branch https://github.com/vyos/vyos-build
        ```
-   Перейдите в сборочный каталог:
    ```shell
    cd vyos-build
    ```
-   Подключите данный каталог к docker:
    -   VyOS 1.2
        ```shell
        docker run --rm -it --privileged -v $(pwd):/vyos -w /vyos vyos/vyos-build:crux bash
        ```
    -   VyOS 1.3
        ```shell
        docker run --rm -it --privileged -v $(pwd):/vyos -w /vyos vyos/vyos-build:equuleus bash
        ```
    -   VyOS 1.4
        ```shell
        docker run --rm -it --privileged -v $(pwd):/vyos -w /vyos vyos/vyos-build:sagitta bash
        ```
    -   VyOS 1.5 (rolling release)
        ```shell
        docker run --rm -it --privileged -v $(pwd):/vyos -w /vyos vyos/vyos-build:current bash
        ```
-   Сконфигурируйте параметры сборки:
    -   Скользящий релиз (rolling release)
        ```shell
        ./configure --architecture amd64 --build-by "your@email"
        ```
    -   Конкретный релиз
        ```shell
        ./configure --architecture amd64 --build-by "your@email" --build-type release --version 1.3.4
        ```


### <span class="section-num">2.4</span> Сборка ISO {#сборка-iso}

-   Запустите сборку:
    ```shell
    sudo make iso
    ```


### <span class="section-num">2.5</span> Образы для платформ виртуализации {#образы-для-платформ-виртуализации}


### <span class="section-num">2.6</span> Конфигурация packer {#конфигурация-packer}

-   В файле `packer.json` заданы достаточно оптимистичные промежутки времени.
-   При компиляции в виртуальной машине их не хватает.
-   Увеличим их:
    ```shell
    sed -ie "s:wait3m:wait10m:g" scripts/packer.json
    ```


#### <span class="section-num">2.6.1</span> QEMU {#qemu}

-   Запустите следующую команду после создания образа `qcow2`:
    ```shell
    make qemu
    ```


#### <span class="section-num">2.6.2</span> Vagrant {#vagrant}

-   Запустите следующую команду после создания образа для vagrant:
    ```shell
    make vagrant-libvirt
    ```
-   Для создания используется образ, созданный для Quemu.
