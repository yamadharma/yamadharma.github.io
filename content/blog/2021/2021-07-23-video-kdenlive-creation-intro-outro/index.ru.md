---
title: "Видео. KDEnlive. Создание intro и outro"
author: ["Dmitry S. Kulyabov"]
date: 2021-07-23T19:47:00+03:00
lastmod: 2023-07-11T11:22:00+03:00
tags: ["education"]
categories: ["computer-science"]
draft: false
slug: "video-kdenlive-creation-intro-outro"
---

Создание _intro_ и _outro_ с помощью KDEnlive.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   _intro_ --- заставка в начале видео.
-   _outro_ --- финальная заставка видео.
-   Служат для привлечения внимания и выработки условного рефлекса у зрителя.


## <span class="section-num">2</span> Слияние файлов {#слияние-файлов}

-   После создания заставок их надо добавить к исходному файлу.
-   Предлагается для Этого использовать Avidemux (<http://avidemux.sourceforge.net/>).
-   С помощью командной строки это можно сделать так:
    ```shell
    yes | avidemux3_cli --load intro.mp4 --append input.mkv --append outro.mp4 --output-format mkv --save output.mkv
    ```
-   Поскольку `avidemux3_cli` просит подтверждения действий, я добавил в начало команду `yes` (чтобы не отвечать).
-   Для автоматизации сборки нескольких файлов написал простой скрипт:
    ```shell
    #!/bin/bash

    for i in *.mkv
    do
        yes | avidemux3_cli --load *intro*.mp4 --append "${i}" --append *outro*.mp4 --output-format mkv --save "`basename \"${i}\" .mkv`+intro.mkv"
    done
    ```


## <span class="section-num">3</span> Видео {#видео}

{{< youtube vu7GrfNyT-M >}}
