---
title: "Симулятор трафика Simulation of Urban MObility (SUMO)"
author: ["Dmitry S. Kulyabov"]
date: 2023-03-25T19:53:00+03:00
lastmod: 2023-07-16T17:08:00+03:00
tags: ["modeling"]
categories: ["science"]
draft: false
slug: "simulation-urban-mobility-sumo"
---

Симулятор трафика Simulation of Urban MObility (SUMO).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.eclipse.org/sumo/>.
-   Репозиторий: <https://github.com/eclipse/sumo>.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Зависимости {#зависимости}

-   Для компиляции графического интерфейса нужна библиотека Fox Toolkit (<http://www.fox-toolkit.org/>) версии 1.6.
-   Библиотека Xerces-C (<https://xerces.apache.org/xerces-c/>).
-   Proj (<https://proj.org/>) для поддержки геоконверсии и ссылок.
-   GDAL (<https://gdal.org/>) для импорта из гео-файлов (arcgis).
-   Swig (<http://www.swig.org/>).
-   Java (JDK).
-   Eigen, версия 3 (<https://eigen.tuxfamily.org/index.php?title=Main_Page>).
-   Ffmpeg (<https://ffmpeg.org/>) для вывода видео.
-   OpenSceneGraph (<http://www.openscenegraph.org/>) для 3D GUI.
-   gl2ps (<http://www.geuz.org/gl2ps/>).
-   Python (<https://www.python.org/>).


### <span class="section-num">2.2</span> Ручная установка {#ручная-установка}

-   Можно использовать релиз (например, номер релиза 1.6):
    ```shell
    wget https://github.com/eclipse/sumo/archive/refs/tags/v1_16_0.tar.gz
    ```
-   Можно использовать текущее состояние репозитория:
    ```shell
    git clone --recursive https://github.com/eclipse/sumo
    ```
-   В каталоге проекта выполняем:
    ```shell
    mkdir build/cmake-build && cd build/cmake-build
    cmake ../..
    make -j$(nproc)
    ```


### <span class="section-num">2.3</span> Установка двоичных пакетов {#установка-двоичных-пакетов}

-   Linux
    -   Gentoo:
        ```shell
        emerge sci-misc/sumo
        ```
    -   Fedora (Fedora-37):
        ```shell
        dnf config-manager --add-repo https://download.opensuse.org/repositories/science:/dlr/Fedora_37/
        dnf install -y --nogpgcheck sumo
        ```
    -   Пакет Flatpack: <https://flathub.org/apps/details/org.eclipse.sumo>:
        ```shell
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install flathub org.eclipse.sumo
        ```

        -   Я не знаю, как запускать скрипты с использованием варианта Flatpack.


## <span class="section-num">3</span> Переменные окружения {#переменные-окружения}

-   Скрипты используют переменную окружения `SUMO_HOME`.


### <span class="section-num">3.1</span> Использование из каталога компиляции {#использование-из-каталога-компиляции}

-   Если вы не устанавливаете пакет в системные каталоги, а работаете из каталога компиляции проекта.
-   В каталоге проекта выполняем:
    ```shell
    export SUMO_HOME="$PWD"
    ```
-   После этого можно запускать скрипты.


### <span class="section-num">3.2</span> Установка в системные каталоги {#установка-в-системные-каталоги}

-   Если вы установили пакет в систему, то устанавливается специальная иерархия для скриптов.
-   Если Вы установили в пакет в каталог `/usr`, то задайте переменную окружения:
    ```shell-script
    export SUMO_HOME=/usr/share/sumo
    ```
