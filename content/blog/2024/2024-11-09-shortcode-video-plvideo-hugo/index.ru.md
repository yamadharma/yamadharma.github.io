---
title: "Сокращение для видео Платформа для Hugo"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-09T20:13:00+03:00
lastmod: 2024-11-09T20:42:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "shortcode-video-plvideo-hugo"
---

Сокращение для видео Платформа для Hugo.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общее описание {#общее-описание}

-   Видеохостинг _Платформа_: <https://plvideo.ru/>.


## <span class="section-num">2</span> Реализация {#реализация}

-   Добавьте в структуру сайта Hugo файл `layouts/shortcodes/plvideo.html`:
    ```html
    <div class="embed video-player">
      <iframe class="plvideo-player" type="text/html"
              width="720" height="405"
              src="https://plvideo.ru/embed/{{ index .Params 0 }}"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
      </iframe>
    </div>
    ```


## <span class="section-num">3</span> Использование {#использование}

-   Для вставки видео _Платформа_ используется следующая конструкция:
    ```markdown
    {{</* plvideo 1SW2MCtcggzo */>}}
    ```
