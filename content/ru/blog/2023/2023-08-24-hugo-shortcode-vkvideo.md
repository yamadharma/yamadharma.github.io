---
title: "Hugo shortcode. Видео на VK Video"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-24T18:35:00+03:00
lastmod: 2025-04-16T21:02:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "hugo-shortcode-vkvideo"
---

Shortcode для видео _VK Video_ для Hugo.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общее описание {#общее-описание}

-   Видеохостинг _VK Video_: <https://vk.com/video>.
-   Реализация сделана на скорую руку.


## <span class="section-num">2</span> Реализация {#реализация}

-   Добавьте в структуру сайта Hugo файл `layouts/shortcodes/vkvideo.html`:
    ```html
    {{ if .IsNamedParams }}
    <div class="embed video-player">
      <iframe class="vkvideo-player" type="text/html"
        src="https://vkvideo.ru/video_ext.php?oid={{ .Get "oid" }}&id={{ .Get "id" }}&hd={{ .Get "hd" }}"
        width="647" height="364" allow="autoplay; encrypted-media; fullscreen; picture-in-picture; screen-wake-lock;" frameborder="0" allowfullscreen>
      </iframe>
    </div>
    {{ else }}
    <div class="embed video-player">
      <iframe class="vkvideo-player" type="text/html"
        src="https://vkvideo.ru/video_ext.php?oid={{ .Get 0 }}&id={{ .Get 1 }}&hd={{ .Get 2 }}"
        width="647" height="364" allow="autoplay; encrypted-media; fullscreen; picture-in-picture; screen-wake-lock;" frameborder="0" allowfullscreen>
      </iframe>
    </div>
    {{ end }}
    ```


## <span class="section-num">3</span> Использование {#использование}


### <span class="section-num">3.1</span> Параметры {#параметры}

-   `oid`: идентификатор владельца;
-   `id`: идентификатор видео;
-   `hd`: хэш (внутренняя функция хостера).


### <span class="section-num">3.2</span> Вставка видео {#вставка-видео}

-   Для вставки видео _VK Video_ используется следующая конструкция (с именованными параметрами):
    ```markdown
    {{</* vkvideo oid="606414976" id="456239563" hd="2" */>}}
    ```
-   Для вставки видео _VK Video_ используется следующая конструкция (с позиционными параметрами):
    ```markdown
    {{</* vkvideo 606414976 456239563 2 */>}}
    ```
