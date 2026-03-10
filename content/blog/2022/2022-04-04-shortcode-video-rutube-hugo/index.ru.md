---
title: "Сокращение для видео Rutube для Hugo"
author: ["Dmitry S. Kulyabov"]
date: 2022-04-04T16:42:00+03:00
lastmod: 2023-07-01T17:34:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "shortcode-video-rutube-hugo"
---

Shortcode для видео _Rutube_ для Hugo.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общее описание {#общее-описание}

-   Видеохостинг _Rutube_: <https://rutube.ru/>.
-   Реализация сделана на скорую руку.


## <span class="section-num">2</span> Реализация {#реализация}

-   Добавьте в структуру сайта Hugo файл `layouts/shortcodes/rutube.html`:
    ```html
    <div class="embed video-player">
      <iframe class="rutube-player" type="text/html"
              width="720" height="405"
              src="https://rutube.ru/play/embed/{{ index .Params 0 }}"
              webkitAllowFullScreen mozallowfullscreen allowFullScreen
              allow="clipboard-write" frameborder="0">
      </iframe>
    </div>
    ```


## <span class="section-num">3</span> Использование {#использование}

-   Для вставки видео _Rutube_ используется следующая конструкция:
    ```markdown
    {{</* rutube e6033653f134bd93e79aa2fe81848f09 */>}}
    ```
