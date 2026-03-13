---
title: "Emacs. Ввод символов unicode"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-29T18:14:00+03:00
lastmod: 2024-10-05T19:14:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-enter-unicode-characters"
---

Emacs. Ввод символов unicode.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> ucs-insert {#ucs-insert}

-   Пакет `ucs-insert` по умолчанию подключён на `C-x 8 RET`.
-   Пример ввода буквы λ:
    -   `C-x 8 RET` `GREEK SMALL LETTER LAMBDA` `RET` → λ;
    -   `C-x 8 RET` `03bb` `RET` → λ.
-   Использование дописывания табуляцией:
    -   `C-x 8 RET`  `* lambda`  `TAB`.
