---
title: "Emacs. Окна. Windmove"
author: ["Dmitry S. Kulyabov"]
date: 2024-10-20T19:08:00+03:00
lastmod: 2024-10-20T19:11:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-window-windmove"
---

Перемещение между окнами Windmove.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общее описание {#общее-описание}

-   В режиме Windmove можно задать перемещение по окнам с помощью стрелок.


## <span class="section-num">2</span> Настройка {#настройка}

-   Активируем режим:
    ```emacs-lisp
    (windmove-default-keybindings)
    ```
