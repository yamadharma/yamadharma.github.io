---
title: "Подготовка скринкаста для занятия"
author: ["Dmitry S. Kulyabov"]
date: 2021-10-09T17:35:00+03:00
lastmod: 2023-10-08T18:43:00+03:00
tags: ["education"]
categories: ["computer-science", "science"]
draft: false
slug: "preparing-screencast-lesson"
---

Подготовка скринкаста для занятия.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Этапы подготовки скринкаста {#этапы-подготовки-скринкаста}


### <span class="section-num">1.1</span> Запись скринкаста {#запись-скринкаста}

-   [Видеозапись самостоятельной работы]({{< relref "2021-01-25-self-work-recording" >}})


### <span class="section-num">1.2</span> Добавление заставки {#добавление-заставки}

-   [Видео. KDEnlive. Создание intro и outro]({{< relref "2021-07-23-video-kdenlive-creation-intro-outro" >}})


### <span class="section-num">1.3</span> Выкладывание в общий доступ {#выкладывание-в-общий-доступ}

-   [Публикация видеофайлов]({{< relref "2021-10-09-publishing-video-files" >}})


### <span class="section-num">1.4</span> Перекодирование {#перекодирование}

-   Для хранения файлы следует перекодировать для уменьшения их размера.
-   Для перекодирования можно использовать любую программу.
    -   Handbrake <https://handbrake.fr/>
        ```shell
        #!/bin/sh

        OUTDIR=encoded

        mkdir -p ${OUTDIR}

        for i in *.mkv
        do
            HandBrakeCLI -Z "H.264 MKV 2160p60 4K" -i "${i}" -o ${OUTDIR}/"${i}"
        done
        ```
-   Естественно, следует перекодировать также intro и outro.
