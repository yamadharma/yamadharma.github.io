---
title: "Org-mode. Предпросмотр TeX"
author: ["Dmitry S. Kulyabov"]
date: 2024-01-06T19:38:00+03:00
lastmod: 2024-11-05T17:59:00+03:00
tags: ["latex", "emacs", "org-mode", "tex"]
categories: ["computer-science"]
draft: false
slug: "org-mode-latex-preview"
---

Предпросмотр TeX в org-mode.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Входит в состав пакета org.


## <span class="section-num">2</span> Использование {#использование}

-   Визуализация запускается командой `C-c C-x C-l` (`org-preview-latex-fragment`).
-   Визуализация поддерева: `C-u C-c C-x C-l`.
-   Визуализация всего буфера: `C-u C-u C-c C-x C-l`.
-   Команда обрабатывает код Latex и создаёт изображение png или svg, которое накладывается на код LaTeX.
-   Просмотр других элементов LaTeX (например, листинг для кода) также работает.


## <span class="section-num">3</span> Реализация {#реализация}

-   Список процедур обработки находятся переменной `org-preview-latex-process-alist`.
-   Используются методы: `dvipng`, `imagemagick`, `dvisvgm`.
-   Фрагмент кода встраивается в полный файл LaTeX, который затем обрабатывается программой LaTeX для создания файла dvi или pdf.
-   Затем результирующий файл преобразуется в формат png или svg.


## <span class="section-num">4</span> Настройка {#настройка}


### <span class="section-num">4.1</span> Метод конвертации {#метод-конвертации}

-   Необходимо выбрать метод конвертации (`dvipng`, `imagemagick`, `dvisvgm`):
    ```emacs-lisp
    ;;; Use svg for rendering
    (setq org-latex-create-formula-image-program 'dvisvgm)
    ```
-   Параметры создаваемых изображений:
    ```emacs-lisp
    (setq org-format-latex-options (plist-put org-format-latex-options :scale 0.8))
    (setq org-format-latex-options (plist-put org-format-latex-options :density 600))
    (setq org-format-latex-options (plist-put org-format-latex-options :background "Transparent"))
    ```


### <span class="section-num">4.2</span> Список методов конвертации {#список-методов-конвертации}

-   Стандартный список методов конвертации задан в файле `org.el`:
    ```emacs-lisp
    (defcustom org-preview-latex-process-alist
      '((dvipng
         :programs ("latex" "dvipng")
         :description "dvi > png"
         :message "you need to install the programs: latex and dvipng."
         :image-input-type "dvi"
         :image-output-type "png"
         :image-size-adjust (1.0 . 1.0)
         :latex-compiler ("latex -interaction nonstopmode -output-directory %o %f")
         :image-converter ("dvipng -D %D -T tight -o %O %f")
         :transparent-image-converter
         ("dvipng -D %D -T tight -bg Transparent -o %O %f"))
        (dvisvgm
         :programs ("latex" "dvisvgm")
         :description "dvi > svg"
         :message "you need to install the programs: latex and dvisvgm."
         :image-input-type "dvi"
         :image-output-type "svg"
         :image-size-adjust (1.7 . 1.5)
         :latex-compiler ("latex -interaction nonstopmode -output-directory %o %f")
         :image-converter ("dvisvgm %f --no-fonts --exact-bbox --scale=%S --output=%O"))
        (imagemagick
         :programs ("latex" "convert")
         :description "pdf > png"
         :message "you need to install the programs: latex and imagemagick."
         :image-input-type "pdf"
         :image-output-type "png"
         :image-size-adjust (1.0 . 1.0)
         :latex-compiler ("pdflatex -interaction nonstopmode -output-directory %o %f")
         :image-converter
         ("convert -density %D -trim -antialias %f -quality 100 %O"))))
    ```
-   При необходимости эту запись можно заменить полностью, либо отредактировать по частям.
-   Например, будем запускать компилятор дважды:
    ```emacs-lisp
    (plist-put
     (cdr (assoc 'dvipng org-preview-latex-process-alist))
     :latex-compiler '("latex -interaction nonstopmode -output-directory %o %f"
                       "latex -interaction nonstopmode -output-directory %o %f"))
    ```


### <span class="section-num">4.3</span> Пакеты {#пакеты}

-   Набор используемых пакетов LaTeX заносятся в переменные:
    -   `org-latex-default-packages-alist` : список пакетов по умолчанию, лучше не изменять;
    -   `org-latex-packages-alist` : пустая по умолчанию переменная, заносите информацию сюда.


### <span class="section-num">4.4</span> Разное {#разное}

-   Созданные изображения лучше поместить в отдельный кэш:
    ```emacs-lisp
    (setq org-preview-latex-image-directory (concat home-cache-path "org-latex/"))
    ```


## <span class="section-num">5</span> Опции в org-файле {#опции-в-org-файле}

-   Вы можете включить предварительный просмотр всех фрагментов LaTeX в файле с помощью опции:
    ```org
    #+STARTUP: latexpreview
    ```
-   Чтобы отключить предпросмотр:
    ```org
    #+STARTUP: nolatexpreview
    ```
