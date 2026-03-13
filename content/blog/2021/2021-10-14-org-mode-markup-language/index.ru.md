---
title: "Язык разметки org-mode"
author: ["Dmitry S. Kulyabov"]
date: 2021-10-14T18:49:00+03:00
lastmod: 2023-07-08T16:09:00+03:00
tags: ["emacs", "org-mode"]
categories: ["computer-science"]
draft: false
slug: "org-mode-markup-language"
---

Язык разметки org-mode.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Внешний вид {#внешний-вид}


### <span class="section-num">1.1</span> Изображения {#изображения}

-   Изображение можно вставлять просто в виде имени файла:
    ```org
    ./img/cat.jpg
    ```
-   Можно задать заголовок и метку для изображения. Тогда изображение вставляется в виде ссылки.
    ```org
    #+CAPTION: Заголовок изображения
    #+NAME:   fig:image-a
    [[./img/a.jpg]]
    ```
-   Такие изображения можно отобразить в буфере с помощью команды: `C-c C-x C-v` (`org-toggle-inline-images`).
-   При вызове с префиксом также отображать изображения, у которых есть заголовок: `C-u C-c C-x C-v`.
-   Можно активировать отображение встроенных изображений при запуске:
    -   настроив переменную `org-startup-with-inline-images`;
    -   установив в буфере параметр `STARTUP` в `inlineimages` (или `noinlineimages`).
