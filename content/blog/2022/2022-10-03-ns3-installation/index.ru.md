---
title: "Установка NS-3"
author: ["Dmitry S. Kulyabov"]
date: 2022-10-03T15:34:00+03:00
lastmod: 2023-07-10T14:33:00+03:00
tags: ["modeling"]
categories: ["science"]
draft: false
slug: "ns3-installation"
---

Установка NS-3.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий кода: <https://gitlab.com/nsnam/ns-3-dev>
-   Репозиторий скриптов для сборки: <https://gitlab.com/nsnam/ns-3-allinone>


## <span class="section-num">2</span> Исходный код {#исходный-код}


### <span class="section-num">2.1</span> Архив исходных кодов релиза {#архив-исходных-кодов-релиза}

-   Последний релиз: <https://www.nsnam.org/releases/latest/>.
-   Адрес архива имеет вид: `https://www.nsnam.org/releases/ns-allinone-3.x.y.tar.bz2`.


### <span class="section-num">2.2</span> Загрузка из репозитория {#загрузка-из-репозитория}

-   Репозиторий скриптов: <https://gitlab.com/nsnam/ns-3-allinone>.
-   Порядок работы.
    -   Скачайте репозиторий скриптов:
        ```shell
        git clone https://gitlab.com/nsnam/ns-3-allinone.git
        ```
    -   Загрузите программный код (текущий снепшот):
        ```shell
        cd ns-3-allinone
        ./download.py
        ```

        -   Загрузка текущего снепшота часто не может определить версии сопутствующего программного обеспечения.
    -   Можно загрузить релиз:
        ```shell
        cd ns-3-allinone
        ./download.py -n ns-3.x.y
        ```


## <span class="section-num">3</span> Необходимые дополнительные пакеты {#необходимые-дополнительные-пакеты}

-   Python API Scanning Support
    -   `pygccxml`
        -   Репозиторий: <https://github.com/CastXML/pygccxml>
    -   `cxxfilt`
        -   Репозиторий: <https://github.com/afq984/python-cxxfilt>


## <span class="section-num">4</span> Опции компиляции {#опции-компиляции}


### <span class="section-num">4.1</span> NetAnim {#netanim}

-   Для компиляции NetAnim нужны библиотеки Qt5 или Qt4.
-   При конфигурировании скрипт ищет утилиты `qmake-qt5` или `qmake-qt4`.
-   Но в _gentoo_ данная утилита называется `qmake5`.
-   Поэтому следует добавить опцию:
    ```shell
    ./build.py --qmake-path=/usr/bin/qmake5
    ```


### <span class="section-num">4.2</span> Опции для компиляции ns3 {#опции-для-компиляции-ns3}

-   Чтобы получить опции компиляции для `ns3`, следует зайти в каталог `ns3-3.x.y` и запустить:
    ```shell
    ./ns3 configure --help
    ```
-   Интеграция с Python:
    ```shell
    ./ns3 configure --enable-python-bindings
    ```
-   Собрать одну большую разделяемую библиотеку:
    ```shell
    ./ns3 configure --enable-monolib
    ```


### <span class="section-num">4.3</span> Итоговые опции компиляции {#итоговые-опции-компиляции}


#### <span class="section-num">4.3.1</span> Gentoo {#gentoo}

<!--list-separator-->

1.  Используя общий скрипт

    -   Основной скрипт скрипт запускается со следующими опциями:
        ```shell
        ./build.py --enable-examples --enable-tests --qmake-path=/usr/bin/qmake5
        ```


#### <span class="section-num">4.3.2</span> Компиляция вручную {#компиляция-вручную}

-   Однако, для более тонкой конфигурации лучше сделать вручную:
    ```shell
    NETANIM_DIR=$(echo netanim-*)
    cd ${NETANIM_DIR}
    qmake5 NetAnim.pro
    cd ..
    NS_DIR=$(echo ns-*)
    cd ${NS_DIR}
    ./ns3 configure --enable-monolib --enable-python-bindings --enable-examples --enable-tests -- -DNS3_SCAN_PYTHON_BINDINGS=ON
    ```
-   Теперь скомпилим код:
    ```shell
    NETANIM_DIR=$(echo netanim-*)
    cd ${NETANIM_DIR}
    make
    cd ..
    NS_DIR=$(echo ns-*)
    cd ${NS_DIR}
    ./ns3 build
    ```
