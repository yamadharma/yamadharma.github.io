---
title: "Emacs. Автоформатирование. apheleia"
author: ["Dmitry S. Kulyabov"]
date: 2025-11-15T13:54:00+03:00
lastmod: 2025-11-15T17:42:00+03:00
draft: false
slug: "emacs-autoformatting-apheleia"
---

Emacs. Автоформатирование. apheleia.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/radian-software/apheleia>
-   Запускает форматировщик кода для буфера.


## <span class="section-num">2</span> Форматеры {#форматеры}


### <span class="section-num">2.1</span> LaTeX {#latex}


#### <span class="section-num">2.1.1</span> latexindent {#latexindent}

-   Репозиторий: <https://github.com/cmhughes/latexindent.pl>
-   Написан на Perl.
-   Входит в состав TeXLive (см. [Установка TeXlive]({{< relref "2021-04-23-install-texlive" >}})).
-   Установлен как форматер по умолчанию.
-   Широкие возможности настройки через интерфейс конфигурации на основе YAML, позволяющий точно управлять стилями отступов и другими аспектами форматирования.
-   Медленный, особенно при работе с большими файлами LaTeX, благодаря реализации на Perl и обширным возможностям настройки.


### <span class="section-num">2.2</span> tex-fmt {#tex-fmt}

-   [Форматирование. LaTeX. tex-fmt]({{< relref "2025-11-15--formatting-latex-tex-fmt" >}})
-   Ориентирован на скорость и эффективность.
-   Настройки не столь обширны, как у latexindent.
-   Значительно быстрее latexindent на больших файлах.


#### <span class="section-num">2.2.1</span> Замена latexindent {#замена-latexindent}

-   Простая конфигурация для замены latexindent на tex-fmt:
    ```emacs-lisp
    ;;;; Define tex-fmt as an Apheleia formatter
    (add-to-list 'apheleia-formatters '(tex-fmt "tex-fmt" "--stdin"))

    ;;;; Associate tex-fmt with LaTeX modes
    (if (executable-find "tex-fmt")
        (progn
          (setf (alist-get 'latex-mode apheleia-mode-alist) 'tex-fmt)
          (setf (alist-get 'LaTeX-mode apheleia-mode-alist) 'tex-fmt)
             (setf (alist-get 'TeX-latex-mode apheleia-mode-alist) 'tex-fmt)
             (setf (alist-get 'TeX-mode apheleia-mode-alist) 'tex-fmt))
      nil)
    ```
