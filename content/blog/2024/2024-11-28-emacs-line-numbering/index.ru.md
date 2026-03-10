---
title: "Emacs. Нумерация строк"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-28T19:50:00+03:00
lastmod: 2024-11-28T20:12:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-line-numbering"
---

Emacs. Нумерация строк.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> display-line-numbers-mode {#display-line-numbers-mode}

-   Встроенная библиотека.
-   Более производительна, чем nlinum.
-   Включить глобально:
    ```emacs-lisp
    (global-display-line-numbers-mode 1)
    ```
-   Включить для конкретной моды:
    ```emacs-lisp
    (add-hook 'prog-mode-hook #'display-line-numbers-mode)
    ```


## <span class="section-num">2</span> nlinum {#nlinum}

-   Elpa: <https://elpa.gnu.org/packages/nlinum.html>
-   Включить глобально:
    ```emacs-lisp
    (global-nlinum-mode 1)
    ```
-   Включить для конкретной моды:
    ```emacs-lisp
    (add-hook 'prog-mode-hook #'nlinum-mode)
    ```
