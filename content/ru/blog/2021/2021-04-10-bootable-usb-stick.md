---
title: "Загрузочная флешка"
author: ["Dmitry S. Kulyabov"]
date: 2021-04-10T18:46:00+03:00
lastmod: 2023-07-18T20:07:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "bootable-usb-stick"
---

Задача состояла в том, чтобы сделать загрузочную флешку, способную загружать ISO-образы.

<!--more-->

{{< toc >}}

Несмотря на наличие usb-диска в корпусе Zalman ZM-VE300 (см. [Контейнер для жесткого диска Zalman ZM-VE300]({{< relref "2022-06-06-zalman-zm-ve300" >}})), хотелось также иметь бутовую флешку, загружающую операционные системы из ISO-образов.


## <span class="section-num">1</span> Программный загрузчик {#программный-загрузчик}

-   В качестве программного загрузчика был выбран Ventoy:
    -   <https://www.ventoy.net/>
    -   <https://github.com/ventoy/Ventoy>
-   Основан на загрузчике `grub2` (<https://ru.wikipedia.org/wiki/GNU_GRUB>).


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Установка под Windows {#установка-под-windows}

-   Скачиваем откомпилированный образ для Windows из <https://github.com/ventoy/Ventoy/releases>.
-   Запускаем установщик:
    ```shell
    Ventoy2Disk.exe
    ```


### <span class="section-num">2.2</span> Установка для Linux {#установка-для-linux}

-   Скачиваем откомпилированный образ для Linux из <https://github.com/ventoy/Ventoy/releases>.


#### <span class="section-num">2.2.1</span> Установка из командной строки {#установка-из-командной-строки}

-   Запустить от пользователя `root` установщик:
    ```shell
    Ventoy2Disk.sh { -i | -I | -u } /dev/sdX
    ```
    Здесь

    -   `/dev/sdX` --- usb-диск (флешка);
    -   `-i` --- установить загрузчик;
    -   `-I` --- установить загрузчик принудительно (даже если на флешке был уже установлен этот загрузчик);
    -   `-u` --- обновить загрузчик.


#### <span class="section-num">2.2.2</span> Графическая установка {#графическая-установка}

-   Начиная с версии 1.0.52 поддерживается графическая установка.
-   Исполняемый файл имеет название вида `VentoyGUI.<архитектура>`.
-   Установщик запускается из-под пользователя `root` или из-под обычного пользователя.


### <span class="section-num">2.3</span> Копирование образов систем {#копирование-образов-систем}

-   После завершения установки usb-накопитель будет разделен на 2 раздела.
-   1 раздел форматируется по умолчанию файловой системой exFAT (можно потом переформатировать самому, по желанию в FAT32/NTFS/UDF/XFS/Ext2/Ext3/Ext4).
-   Образы операционных систем копируются на 2 раздел.
-   По умолчанию поиск образов систем ведётся во всех подкаталогах.
-   2 раздел служебный (для UEFI).


## <span class="section-num">3</span> Используемые образы операционных систем {#используемые-образы-операционных-систем}


### <span class="section-num">3.1</span> SystemRescue {#systemrescue}

-   В качестве образа для администрирования системы обычно использую SystemRescue.
    -   <https://www.system-rescue-cd.org/>


### <span class="section-num">3.2</span> Windows {#windows}

-   У нас имеется лицензия на Windows for Education. Поэтому я использую следующий образ:
    -   <https://www.microsoft.com/ru-ru/software-download/vlacademicwindows10iso>


## <span class="section-num">4</span> Видезапись {#видезапись}

Видеозапись процесса создания бутовой флешки.

{{< youtube vHFncWdJCzY >}}
