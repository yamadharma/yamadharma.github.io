---
title: "Octave. Установка пакетов"
author: ["Dmitry S. Kulyabov"]
date: 2021-08-26T16:51:00+03:00
lastmod: 2023-09-09T18:42:00+03:00
tags: ["programming"]
categories: ["сиянс", "computer-science"]
draft: false
slug: "octave-install-packages"
---

Установка пакетов расширения в системе _Octave_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Список пакетов расширения:
    -   <https://gnu-octave.github.io/packages/>
    -   <https://octave.sourceforge.io/packages.php>


## <span class="section-num">2</span> Установка пакета {#установка-пакета}

-   Определим место установки пакета:
    -   глобально на уровне системы:
        ```octave
        pkg prefix -global
        ```
    -   локально в каталоге пользователя:
        ```octave
        pkg prefix -local
        ```
-   Будем устанавливать из центрального репозитория пакетов _Octave Forge_.
-   Просмотрим список пакетов в репозитории:
    ```octave
    pkg list -forge
    ```
-   На всякий случай посмотрим список локальных пакетов:
    ```octave
    pkg list
    ```
-   Установим нужный пакет:
    ```octave
    pkg install <package_name> -forge
    ```


## <span class="section-num">3</span> Видео {#видео}

{{< youtube Xcn3f2bh7mc >}}
