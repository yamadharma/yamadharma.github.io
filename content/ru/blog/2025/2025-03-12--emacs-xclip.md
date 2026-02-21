---
title: "Emacs. xclip"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-12T14:29:00+03:00
lastmod: 2025-03-12T14:42:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-xclip"
---

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://elpa.gnu.org/packages/xclip.html>
-   Позволяет копировать текст в системный буфер обмена графического интерфейса и вставлять из него при работе в текстовом терминале.
-   Решает проблемы при работе в консоли и при работе в Wayland (при компиляции с pgtk).
-   Может использовать внешние инструменты командной строки, которые необходимо установить, чтобы пакет работал:
    -   X11: `xclip` (<https://xclip.sourceforge.net>) или `xsel` (<https://www.vergenet.net/~conrad/software/xsel/>).
    -   MacOS: `pbpaste`, `pbcopy`.
    -   Cygwin: `getclip`, `putclip`.
    -   Wayland: `wl-clipboard` (<https://github.com/bugaevc/wl-clipboard>).
    -   Termux: `termux-clipboard-get`, `termux-clipboard-set`.
