---
title: "Emacs. Markdown в Org с помощью буфера обмена"
author: ["Dmitry S. Kulyabov"]
date: 2026-01-02T20:27:00+03:00
lastmod: 2026-01-02T20:34:00+03:00
tags: ["markdown", "emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-markdown-org-clipboard"
---

Emacs. Markdown в Org с помощью буфера обмена

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   На веб-сайтах и в приложениях преобладает текст в формате Markdown.
-   Преобразование из Markdown в Org есть простая, но лишняя задача.


## <span class="section-num">2</span> Преобразование markdown в org {#преобразование-markdown-в-org}

-   <http://yummymelon.com/devnull/import-markdown-to-org-with-the-clipboard-in-emacs.html>
-   Скопируйте Markdown-код из исходного приложения или веб-сайта в системный буфер обмена. Этот шаг вставит полученный текст в Emacs kill-ring.
-   В Emacs выполните команду, которая преобразует приведенный выше текст Markdown в формат Org, а затем вставит преобразованный текст в нужный файл Org.
    ```emacs-lisp
    (defun yank-markdown-as-org ()
      "Yank Markdown text as Org.

    This command will convert Markdown text in the top of the `kill-ring'
    and convert it to Org using the pandoc utility."
      (interactive)
      (save-excursion
        (with-temp-buffer
          (yank)
          (shell-command-on-region
           (point-min) (point-max)
           "pandoc -f gfm -t org --wrap=preserve" t t)
          (kill-region (point-min) (point-max)))
        (yank)))
    ```
