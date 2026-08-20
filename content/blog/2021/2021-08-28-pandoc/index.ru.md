---
title: "Pandoc"
author: ["Dmitry S. Kulyabov"]
date: 2021-08-28T19:55:00+03:00
lastmod: 2026-07-23T21:05:00+03:00
tags: ["pandoc", "MOC"]
categories: ["computer-science"]
draft: false
slug: "pandoc"
---

Средство конвертации текстовых форматов _Pandoc_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Универсальная утилита конвертирования текстовых форматов.
-   Входные форматы:
    -   markdown;
    -   reStructuredText;
    -   HTML;
    -   LaTeX;
    -   OPML;
    -   Org-mode;
    -   DocBook;
    -   Office Open XML (Microsoft Word .docx).
-   Выходные форматы:
    -   форматы на основе HTML: XHTML, HTML5, HTML-слайды презентаций (S5, Slidy, Slideous, DZSlides);
    -   форматы текстовых процессоров: Microsoft Word docx, OpenOffice/LibreOffice ODT, OpenDocument XML;
    -   электронные книги: EPUB версии 2 или 3, FictionBook2;
    -   форматы технической документации: DocBook, GNU TexInfo, groff[en];
    -   форматы системы ΤΕΧ: LaTeX, ConTeXt, слайды LaTeX Beamer;
    -   PDF (с помощью LaTeX);
    -   текстовые форматы с облегчённой разметкой: Markdown, reStructuredText, AsciiDoc[en], MediaWiki, Emacs Org-Mode, Textile.
-   Основной формат: Markdown.


## <span class="section-num">2</span> Реализации {#реализации}

-   [Система Quarto]({{< relref "2025-03-22--quarto-system" >}})


## <span class="section-num">3</span> Разное {#разное}

-   [Фильтры pandoc]({{< relref "2021-08-28-pandoc-filters" >}})


## <span class="section-num">4</span> Ресурсы {#ресурсы}


### <span class="section-num">4.1</span> gostdown {#gostdown}

-   Репозиторий: <https://gitlab.iaaras.ru/iaaras/gostdown>
-   Набор шаблонов и скриптов для автоматической вёрстки документов по ГОСТ 19.xxx (ЕСПД) и ГОСТ 7.32 (отчёт о научно-исследовательской работе) в форматах docx из файлов текстовой разметки Markdown.
