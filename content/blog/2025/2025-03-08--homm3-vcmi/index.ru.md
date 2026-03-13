---
title: "Homm3. VCMI"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-08T18:36:00+03:00
lastmod: 2025-03-08T18:53:00+03:00
tags: ["homm"]
categories: ["games"]
draft: false
slug: "homm3-vcmi"
---

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://vcmi.eu/>
-   Репозиторий: <https://github.com/vcmi/vcmi>
-   VK: <https://vk.com/vcmiofficial>
-   Проект по созданию открытого игрового движка для Heroes of Might and Magic III.
-   Важной целью проекта является поддержка модов: возможность добавлять в игру новые города, героев, монстров, артефакты и заклинания без ограничений и конфликтов.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Информация {#информация}

-   <https://vcmi.eu/players/Installation_Linux/>
-   <https://www.gamebuntu.ru/howto/vcmi-geroi-3-ustanovka-i-zapusk-igry/>


### <span class="section-num">2.2</span> Исполняемые файлы {#исполняемые-файлы}

-   Gentoo, репозиторий karma (см. [Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):

<!--listend-->

```shell
emerge vcmi
```


### <span class="section-num">2.3</span> Файлы данных {#файлы-данных}

-   Необходимо скопировать ресурсные файлы от оригинальной игры:
    -   из папки с установленной игрой;
    -   с оригинального компакт-диска игры;
    -   из файла установки HMMiii с сайта GOG.


#### <span class="section-num">2.3.1</span> Из папки с установленной игрой {#из-папки-с-установленной-игрой}

<!--list-separator-->

1.  С помощью утилиты

    -   Можно установить с помощью утилиты:
        ```shell
        vcmibuilder --data /path/to/h3/data
        ```
    -   Для flatpak:
        ```shell
        flatpak run --command=vcmibuilder eu.vcmi.VCMI --data /path/to/h3/data
        ```

<!--list-separator-->

2.  Вручную

    -   Скопируйте папки `Data`, `Maps`, `MP3` в папку `~/.local/share/vcmi/` если вы устанавливали движок из бинарного пакета.
    -   Скопируйте в папку `~/.var/app/eu.vcmi.VCMI/data/vcmi/`, если вы использовали flatpak пакет.


#### <span class="section-num">2.3.2</span> С оригинального компакт-диска игры {#с-оригинального-компакт-диска-игры}

-   Нужны один или два образа CD:
    ```shell
    vcmibuilder --cd1 /path/to/iso/or/cd --cd2 /path/to/second/cd
    ```


#### <span class="section-num">2.3.3</span> Из файла установки с сайта GOG {#из-файла-установки-с-сайта-gog}

-   Нужен автономный установщик загружен с Gog.com (требуются файлы .exe и .bin):
    ```shell
    vcmibuilder --gog /path/to/gog.com/installer.exe
    ```
-   В качестве альтернативы вы можете использовать классический путь:
    ```shell
    innoextract --output-dir=~/Downloads/HoMM3 "setup_heroes_of_might_and_magic_3_complete_4.0_(28740).exe"
    ```
-   Как только InnoExtract завершится, запустите запуск VCMI и выберите размещение существующих файлов.
-   Выберите каталог `~/Downloads/HoMM3`.
-   После завершения размещения вы можете удалить как автономные файлы установщика, так и `~/Downloads/HoMM3`.


### <span class="section-num">2.4</span> Запуск игры {#запуск-игры}

-   Запустите:
    ```shell
    vcmilauncher
    ```
