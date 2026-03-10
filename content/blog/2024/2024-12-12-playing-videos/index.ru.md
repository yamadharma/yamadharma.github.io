---
title: "Проигрывание видеофайлов"
author: ["Dmitry S. Kulyabov"]
date: 2024-12-12T16:26:00+03:00
lastmod: 2024-12-12T16:53:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "playing-videos"
---

Проигрывание видеофайлов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> mpv {#mpv}


### <span class="section-num">1.1</span> Общая информация {#общая-информация}

-   Мультимедийный плеер, основанный на MPlayer и mplayer2.
-   Сайт: <https://mpv.io>
-   Репозиторий: <https://github.com/mpv-player/mpv>
-   Отличия от предшественников: <https://github.com/mpv-player/mpv/blob/master/DOCS/mplayer-changes.rst>


### <span class="section-num">1.2</span> Установка как приложение по умолчанию {#установка-как-приложение-по-умолчанию}

-   Можно установить mpv как просмотрщик по умолчанию (см. [XDG. Приложения MIME]({{< relref "2023-04-02-xdg-mime-applications" >}})).
-   Проверим, какие ассоциации актуальны:
    ```shell
    cat /usr/share/applications/mpv.desktop | grep -i MimeType | cut -d "=" -f 2 | tr ';' '\n' | xargs -l1 xdg-mime query default
    ```
-   Установим для всех типов ассоциацию с _mpv_:
    ```shell
    cat /usr/share/applications/mpv.desktop | grep -i MimeType | cut -d "=" -f 2 | tr ';' '\n' | xargs -l1 xdg-mime default mpv.desktop
    ```
