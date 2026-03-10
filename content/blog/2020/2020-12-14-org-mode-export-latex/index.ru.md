---
title: "Org-mode. Экспорт в LaTeX"
author: ["Dmitry S. Kulyabov"]
date: 2020-12-14T10:35:00+03:00
lastmod: 2023-10-01T14:43:00+03:00
tags: ["org-mode", "emacs", "tex"]
categories: ["computer-science"]
draft: false
slug: "org-mode-export-latex"
---

Экспорт из org-mode в LaTeX.

<!--more-->

{{< toc >}}

Общие настройки экспорта из org-mode описаны в [Org-mode. Экспорт]({{< relref "2020-12-10-org-mode-export" >}}).


## <span class="section-num">1</span> Параметры экспорта {#параметры-экспорта}


### <span class="section-num">1.1</span> Значения параметров экспорта {#значения-параметров-экспорта}


### <span class="section-num">1.2</span> Соответствие параметров экспорта для файла и поддерева {#соответствие-параметров-экспорта-для-файла-и-поддерева}

<a id="table--Опции экспорта для файла и поддерева"></a>

| Опции экспорта файла | Опции экспорта поддерева   |
|----------------------|----------------------------|
| LaTeX_CLASS          | EXPORT_LaTeX_CLASS         |
| LaTeX_CLASS_OPTIONS  | EXPORT_LaTeX_CLASS_OPTIONS |
| LaTeX_HEADER         | EXPORT_LaTeX_HEADER        |


## <span class="section-num">2</span> Специальные варианты экспорта {#специальные-варианты-экспорта}


### <span class="section-num">2.1</span> Экспорт фрагментов математики {#экспорт-фрагментов-математики}

-   Применяется для экспорта в формат `odt`.
-   Можно экспортировать в формат MathML или в виде рисунка


#### <span class="section-num">2.1.1</span> Экспорт в формате MathML {#экспорт-в-формате-mathml}

-   В файле задаётся опция:
    ```org
    #+OPTIONS: tex:t
    ```
-   Можно установить переменную emacs `org-export-with-latex`:
    ```elisp
    (setq org-export-with-latex t)
    ```
-   Устанавливается программа конвертации. Предлагается установить LaTeXML <https://dlmf.nist.gov/LaTeXML/>.
-   В Gentoo _ebuild_ находится в оверлее _flammie_.
    ```shell
    emerge dev-tex/LaTeXML
    ```
-   В конфигурационном файле задаётся переменная `org-latex-to-mathml-convert-command`:
    ```elisp
    (setq org-latex-to-mathml-convert-command
          "latexmlmath \"%i\" --presentationmathml=%o")
    ```


#### <span class="section-num">2.1.2</span> Экспорт в виде рисунка {#экспорт-в-виде-рисунка}

-   В файле устанавливаются опции:
    -   экспорт в `png`:
        ```org
        #+OPTIONS: tex:dvipng
        ```
    -   экспорт в `svg`:
        ```org
        #+OPTIONS: tex:dvisvgm
        ```
    -   экспорт в `png`:
        ```org
        #+OPTIONS: tex:imagemagick
        ```
-   Для генерации изображения запускается соответствующая программа.
