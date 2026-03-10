---
title: "Emacs. Работа с библиографией. Org-cite"
author: ["Dmitry S. Kulyabov"]
date: 2022-10-10T12:34:00+03:00
lastmod: 2023-07-18T20:01:00+03:00
tags: ["bib", "emacs", "org-mode"]
categories: ["computer-science"]
draft: false
slug: "emacs-bibliography-org-cite"
---

Библиография в org-mode на основе org-cite.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Выпущена в 2021 году для нативной поддержки ссылок в `org-mode`.
-   Задаёт родной синтаксис для цитирования.


## <span class="section-num">2</span> Цитирование {#цитирование}

-   Прежде чем добавлять цитаты, сначала следует задать один или несколько файлов библиографии:
    -   глобально с помощью `org-cite-global-bibliography`:
        ```emacs-lisp
        (setq org-cite-global-bibliography '("~/work/bib/bib/main.bib"))
        ```
    -   локально с помощью одного или нескольких ключевых слов `bibliography`:
        ```org
        #+bibliography: SomeFile.bib
        #+bibliography: /some/other/file.json
        #+bibliography: "/some/file/with spaces/in its name.bib"
        ```
-   Цитаты можно вставлять и редактировать с помощью `org-cite-insert`, или комбинации `C-c C-x @`.
-   Для цитирования требуется один или несколько ключей цитирования элементов, идентифицирующих ссылку в библиографии:
    ```org
    [cite/style:common prefix ;prefix @key suffix; ... ; common suffix]
    ```

    -   Каждая цитата заключена в квадратные скобки и использует ключевое слово `cite`.
    -   Каждый ключ начинается с символа `@`.
    -   Каждый ключ может быть дополнен префиксом (например, `см.`) и/или суффиксом (например, `стр. 123`), предоставляя информацию, полезную или необходимую для понимания цитаты, но не включенную в ссылку.
    -   Одна цитата может цитировать более одной ссылки; ключи разделены точкой с запятой; форматирование таких групп цитирования определяется стилем.
    -   Можно также указать стилистическую вариацию для цитат, вставив '/' и имя стиля между ключевым словом `cite` и двоеточием.
-   Обязательными элементами являются:
    -   ключевое слово `cite` и двоеточие;
    -   символ `@`, непосредственно предшествующий каждому ключу;
    -   скобки, окружающие цитирование.
-   Чтобы вставить куда-либо библиографию, нужно в этом месте задать ключевое слово `print_bibliography`:
    ```org
    #+print_bibliography:
    ```


## <span class="section-num">3</span> Обработка цитирования {#обработка-цитирования}


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   Важной концепцией `org-cite` являются _экспортные процессоры_.
-   Хотя цитаты всегда будут иметь один и тот же формат, экспортируемый текст будет меняться в зависимости от используемого процессора.
-   Основные функции процессоров:
    -   вставка и редактирование цитат;
    -   связь ссылки и её определения;
    -   выделение цитат в буфере;
    -   экспорт цитат.


### <span class="section-num">3.2</span> Процессоры цитирования {#процессоры-цитирования}


#### <span class="section-num">3.2.1</span> Универсальные {#универсальные}

<!--list-separator-->

1.  basic

    -   Когда обратная совместимость не требуется, а потребности в форматировании минимальны.
    -   Загрузка:
        ```emacs-lisp
        (require 'oc-basic)
        ```

<!--list-separator-->

2.  csl

    -   Используется форматирование на основе Citation Style Language (см. [Citation Style Language (CSL)]({{< relref "2022-10-10-citation-style-language" >}})).
    -   Для этого используется пакет `citeproc-el`.
    -   Конфигурация:
        ```emacs-lisp
        (require 'oc-csl)

        ;;; https://github.com/citation-style-language/styles
        ;;; https://www.zotero.org/styles
        (setq org-cite-csl-styles-dir "~/work/bib/csl")
        ```
    -   `csl` экспортируется в визуализированный текст.
        -   Визуализированный текст --- это текст, вид которого будет совпадать с форматированием в `org-mode`, например, текст, выделенный курсивом `org-mode`, будет обернут в `\emph{}` в LaTeX.
        -   При экспорте `[cite:@bradleyAppearanceRealityMetaphysical2011 82–5;]` в файл LaTeX с помощью csl-процессора, используя файл CSL для стиля цитирования _Modern Language Association (MLA)_, в файле LaTeX будет следующая цитата: `(Bradley 82–85)`.
    -   При экспорте в LaTeX отрендеренного текста зачастую будет недостаточно.
    -   Для получения доступ к более сложным или тонким функциям надо использовать процессор `biblatex`.


#### <span class="section-num">3.2.2</span> LaTeX {#latex}

-   Для экспорта в LaTeX.

<!--list-separator-->

1.  natbib

    -   Для экспорта в BibTeX, исторический библиографический процессор, используемый с LaTeX.
    -   Используются команды цитирования из пакета `natbib`.
    -   Загрузка:
        ```emacs-lisp
        (require 'oc-natbib)
        ```

<!--list-separator-->

2.  biblatex

    -   Для экспорта в BibLaTeX, альтернативного библиографического процессора, используемого с LaTeX (см. [bibtex vs biblatex]({{< relref "2022-09-11-bibtex-biblatex" >}})).
    -   Загрузка:
        ```emacs-lisp
        (require 'oc-biblatex)
        ```
    -   Стиль конечного цитирования будет определяться предоставленными параметрами пакета (например, `style=gost`).
    -   Например, `[cite:@bradleyAppearanceRealityMetaphysical2011 82-5;]`  будет экспортироваться в команду LaTeX `\cite[82-5]{bradleyAppearanceRealityMetaphysical2011}`.
    -   Процессору BibLaTeX можно передать параметры команде `\printbibliography`:
        ```org
        #+print_bibliography: :section 2 :heading subbibliography
        #+print_bibliography: :keyword abc,xyz :title "Primary Sources"
        ```


### <span class="section-num">3.3</span> Задание типа экспорта {#задание-типа-экспорта}


#### <span class="section-num">3.3.1</span> Общая информация {#общая-информация}

-   Стиль цитат и библиография зависят от трех вещей:
    -   используемый процессор цитирования;
    -   стиль цитирования;
    -   стиль библиографии.


#### <span class="section-num">3.3.2</span> Задание типа экспорта в файле {#задание-типа-экспорта-в-файле}

-   Ключевое слово `CITE_EXPORT`  указывает процессор экспорта и стили цитирования (и, возможно, ссылки).
-   Зададим процессор экспорта `basic` с цитатами, вставленными как имя автора, и ссылками, проиндексированными по имени автора и году.
    ```org
    #+cite_export: basic author author-year
    ```
-   Зададим процессор `csl` и стиль CSL, который в данном случае определяет числовые цитаты и числовые ссылки в соответствии с ванкуверской спецификацией:
    ```org
    #+cite_export: csl /some/path/to/vancouver-brackets.csl
    ```
-   Зададим процессор `natbib` со стилем цитирования соответствующим гарвардскому стилю и спецификации издателя Wolkers-Kluwer:
    ```org
    #+cite_export: natbib kluwer
    ```


#### <span class="section-num">3.3.3</span> Глобальное задание типа экспорта {#глобальное-задание-типа-экспорта}

-   Необходимо настроить переменную `org-cite-export-processors`:
    ```emacs-lisp
    (org-cite-export-processors
     '((md . (csl "chicago-fullnote-bibliography.csl"))   ; Footnote reliant
       (latex . biblatex)                                 ; For humanities
       (odt . (csl "chicago-fullnote-bibliography.csl"))  ; Footnote reliant
       (t . (csl "modern-language-association.csl"))))      ; Fallback
    ```


## <span class="section-num">4</span> Citeproc.el {#citeproc-dot-el}

-   Используется для процессора csl.
-   В настоящее время он поддерживает экспорт в:
    -   HTML;
    -   LaTeX;
    -   Org;
    -   Plain text.
-   В настоящее время Citeproc может извлекать библиографическую информацию из следующих форматов:
    -   CSL-JSON;
    -   Bib(La)TeX;
    -   org-bibtex (см. <https://gewhere.github.io/org-bibtex>).
-   Поддержка Bib(La)TeX и org-bibtex находится в зачаточном состоянии по сравнению с CSL-JSON .
-   Если не задан стиль в `org-cite-csl--fallback-style-file`, будет использоваться стиль, который по умолчанию соответствует чикагскому стилю _автор-дата_.
