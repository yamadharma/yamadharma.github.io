---
title: "Распознавание pdf"
author: ["Dmitry S. Kulyabov"]
date: 2024-08-21T20:50:00+03:00
lastmod: 2024-09-29T17:46:00+03:00
tags: ["pdf", "read"]
categories: ["computer-science"]
draft: false
slug: "pdf-ocr"
---

Распознавание pdf.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Решения по распознаванию pdf {#решения-по-распознаванию-pdf}


### <span class="section-num">1.1</span> OCRmyPDF {#ocrmypdf}

-   [Распознавание pdf. OCRmyPDF]({{< relref "2024-06-07-pdf-ocr-ocrmypdf" >}})
-   Репозиторий: <https://github.com/ocrmypdf/OCRmyPDF>
-   Сайт: <https://ocrmypdf.readthedocs.io/>


### <span class="section-num">1.2</span> pdfsandwich {#pdfsandwich}

-   Сайт: <http://www.tobias-elze.de/pdfsandwich/>


## <span class="section-num">2</span> Некоторые типовые задачи {#некоторые-типовые-задачи}


### <span class="section-num">2.1</span> Перенос ocr-слоя из одно файла в другой {#перенос-ocr-слоя-из-одно-файла-в-другой}


#### <span class="section-num">2.1.1</span> Постановка задачи {#постановка-задачи}

-   Есть 2 pdf-файла:
    -   хороший, но без текстового слоя;
    -   плохой, но с правильным текстовым слоем.
-   Оба файла содержат одинаковые изображения.
-   Цель состоит в том, чтобы встроить текстовый слой из второго файла в первый pdf-файл.


#### <span class="section-num">2.1.2</span> Пример задачи {#пример-задачи}

-   Первый файл подготовлен с помощью OCRmyPDF, имеет адекватный размер.
-   Второй файл обработан FineReader, имеет хороший текстовый слой, но очень большой размер.


#### <span class="section-num">2.1.3</span> Варианты решения {#варианты-решения}

-   Удалить изображения из файла `input_ocr.pdf` с помощью Ghostscript:
    ```shell
    gs -o "input_ocr_textonly.pdf" -sDEVICE=pdfwrite -dFILTERIMAGE "input_ocr.pdf"
    ```
-   Объединить его с файлом `input_image.pdf` с помощью `pdftk`:
    ```shell
    pdftk "input_ocr_textonly.pdf" multistamp "input_image.pdf" output "output.pdf"
    ```
-   Или объединить его с файлом `input_image.pdf` с помощью `qpdf`:
    ```shell
    qpdf --empty --pages "input_image.pdf" -- --underlay "input_ocr_textonly.pdf" -- "output.pdf"
    ```


#### <span class="section-num">2.1.4</span> Ресурсы {#ресурсы}

-   <https://superuser.com/questions/679979/copy-pdf-text-layer-to-another-pdf>
