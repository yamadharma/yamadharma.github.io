---
title: "Миниатюры видео для youtube"
author: ["Dmitry S. Kulyabov"]
date: 2022-02-05T18:18:00+03:00
lastmod: 2023-06-27T19:09:00+03:00
categories: ["computer-science"]
draft: false
slug: "youtube-video-thumbnail"
---

Каждое видео на YouTube содержит 4 сгенерированных изображения.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Адреса изображений {#адреса-изображений}

-   Полноразмерное изображение
    ```shell
    http://img.youtube.com/vi/<insert-youtube-video-id-here>/0.jpg
    ```

-   Уменьшенные изображения (три изображения по умолчанию)
    ```shell
    http://img.youtube.com/vi/<insert-youtube-video-id-here>/1.jpg
    http://img.youtube.com/vi/<insert-youtube-video-id-here>/2.jpg
    http://img.youtube.com/vi/<insert-youtube-video-id-here>/3.jpg
    ```
-   Миниатюра изображения по умолчанию (т. е. одно из `1.jpg`, `2.jpg`, `3.jpg`):
    ```shell
    http://img.youtube.com/vi/<insert-youtube-video-id-here>/default.jpg
    ```
-   Миниатюра по умолчанию высокого качества:
    ```shell
    http://img.youtube.com/vi/<insert-youtube-video-id-here>/hqdefault.jpg
    ```
-   Миниатюра по умолчанию среднего качества:
    ```shell
    http://img.youtube.com/vi/<insert-youtube-video-id-here>/mqdefault.jpg
    ```
-   Миниатюра по умолчанию стандартного разрешения:
    ```shell
    http://img.youtube.com/vi/<insert-youtube-video-id-here>/sddefault.jpg
    ```
-   Миниатюра по умолчанию максимального разрешения:
    ```shell
    http://img.youtube.com/vi/<insert-youtube-video-id-here>/maxresdefault.jpg
    ```
