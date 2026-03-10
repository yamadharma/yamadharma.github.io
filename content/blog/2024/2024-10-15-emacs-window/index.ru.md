---
title: "Emacs. Окна"
author: ["Dmitry S. Kulyabov"]
date: 2024-10-15T15:58:00+03:00
lastmod: 2024-10-20T19:18:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-window"
---

Работа с окнами в Emacs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Терминология {#терминология}

-   В Emacs непривычная терминология.
-   То, что обычно мы называем окном, в Emacs называется фреймом (_frame_).
-   Окном (_window_) называется некоторая часть фрейма.
-   Обычно окно занимает весь фрейм, но можно разделить фрейм на несколько окон.


## <span class="section-num">2</span> Основные операции {#основные-операции}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Основные операции с окнами
</div>

| Клавиши   | Функция                   | Действие                              |
|-----------|---------------------------|---------------------------------------|
| `C-x 1`   | delete-other-windows      | Удалить другие окна, оставить текущее |
| `С-x 2`   | split-window-vertically   | Делит по вертикали                    |
| `C-x 3`   | split-window-horizontally | Делит по горизонтали                  |
| `C-x 0`   | delete-window             | Уничтожает текущее окно               |
| `ESC M-d` | dedicated-mode            | Влк/выкл назначенный режим            |
| `C-x o`   | other-window              | Перейти в следующее окно              |


## <span class="section-num">3</span> Режим Windmove {#режим-windmove}

-   [Emacs. Окна. Windmove]({{< relref "2024-10-20-emacs-window-windmove" >}})
