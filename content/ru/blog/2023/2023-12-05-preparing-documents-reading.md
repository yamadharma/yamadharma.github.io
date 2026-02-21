---
title: "Подготовка документов для чтения"
author: ["Dmitry S. Kulyabov"]
date: 2023-12-05T10:09:00+03:00
lastmod: 2024-09-29T18:12:00+03:00
tags: ["read"]
categories: ["self-management"]
draft: false
slug: "preparing-documents-reading"
---

Подготовка документов для чтения.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Преобразование формата {#преобразование-формата}

-   [Преобразование djvu в pdf]({{< relref "2024-07-26-convert-djvu-pdf" >}})


## <span class="section-num">2</span> Чистка документа {#чистка-документа}


### <span class="section-num">2.1</span> Удалить текстовый слой {#удалить-текстовый-слой}

-   Ghostscript поддерживает параметры, которые позволяют удалить из PDF-файла либо весь текст, либо все изображения, либо все векторные элементы.
-   Удалить весь текст из входного PDF-файла:
    ```shell
    gs -o no-more-texts.pdf -sDEVICE=pdfwrite -dFILTERTEXT input.pdf
    ```
-   Удалить все растровые элементы из входного PDF-файла:
    ```shell
    gs -o no-more-texts.pdf -sDEVICE=pdfwrite -dFILTERIMAGE input.pdf
    ```
-   Удалить все векторные элементы из входного PDF-файла:
    ```shell
    gs -o no-more-texts.pdf -sDEVICE=pdfwrite -dFILTERVECTOR input.pdf
    ```
-   Можно комбинировать любой из двух вышеуказанных параметров (объединение всех трёх приведет к созданию пустых страниц):
    ```shell
    gs -o noIMG.pdf -sDEVICE=pdfwrite -dFILTERIMAGE input.pdf
    gs -o noTXT.pdf -sDEVICE=pdfwrite -dFILTERTEXT input.pdf
    gs -o noVCT.pdf -sDEVICE=pdfwrite -dFILTERVECTOR input.pdf

    gs -o onlyIMG.pdf -sDEVICE=pdfwrite -dFILTERVECTOR -dFILTERTEXT input.pdf
    gs -o onlyTXT.pdf -sDEVICE=pdfwrite -dFILTERVECTOR -dFILTERIMAGE input.pdf
    gs -o onlyVCT.pdf -sDEVICE=pdfwrite -dFILTERIMAGE -dFILTERTEXT input.pdf
    ```


### <span class="section-num">2.2</span> unpaper {#unpaper}

-   Репозиторий: <https://github.com/Flameeyes/unpaper>
-   Сайт: <https://www.flameeyes.com/projects/unpaper>
-   Инструмент постобработки отсканированных изображений.
-   Основная цель --- сделать отсканированные страницы книги более читабельными.


### <span class="section-num">2.3</span> ScanTailor {#scantailor}

-   Сайт: <https://scantailor.org/>
-   Репозиторий: <https://github.com/4lex4/scantailor-advanced>
-   ScanTailor Advanced объединяет функции версий ScanTailor Featured и ScanTailor Enhanced.


## <span class="section-num">3</span> Распознавание документа {#распознавание-документа}

-   [Распознавание pdf]({{< relref "2024-08-21-pdf-ocr" >}})


## <span class="section-num">4</span> Создание оглавления {#создание-оглавления}


### <span class="section-num">4.1</span> Общая информация {#общая-информация}

-   Оглавление упрощает ориентацию в книге.
-   Оглавление позволяет:
    -   всегда иметь под рукой список глав и заголовков книги;
    -   быстро переходить к началу нужной главы или другим важным местам в книге;
    -   структурировать заметки к книге.


### <span class="section-num">4.2</span> Ссылки {#ссылки}

-   <https://commons.wikimedia.org/wiki/Help:Creating_an_outline_for_PDF_and_DjVu/ru>


### <span class="section-num">4.3</span> HandyOutliner for DjVu / PDF {#handyoutliner-for-djvu-pdf}

-   Сайт: <https://handyoutlinerfo.sourceforge.net/index_ru.htm>
-   Sourceforge: <https://sourceforge.net/projects/handyoutlinerfo/>
-   Требует .NET 4.0.
-   Под Linux работает под mono.


### <span class="section-num">4.4</span> Pdf &amp; Djvu Bookmarker {#pdf-and-djvu-bookmarker}

-   Сайт: <https://sourceforge.net/projects/djvubookmarker/>
-   Создание оглавление производится с одновременным просмотром самого документа.


### <span class="section-num">4.5</span> jpdfbookmarks {#jpdfbookmarks}

-   Репозиторий: <https://github.com/SemanticBeeng/jpdfbookmarks>
-   Сайт: <https://sourceforge.net/projects/jpdfbookmarks/>
