---
title: "Pdf. Обработка. pdfcpu"
author: ["Dmitry S. Kulyabov"]
date: 2023-12-02T18:01:00+03:00
lastmod: 2023-12-26T13:34:00+03:00
categories: ["computer-science"]
draft: false
slug: "pdf-processing-pdfcpu"
---

Библиотека и программа pdfcpu для манипуляций с pdf.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Информация {#информация}

-   Сайт: <https://pdfcpu.io/>
-   Репозиторий: <https://github.com/pdfcpu/pdfcpu>


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Linux {#linux}

-   Gentoo (оверлей kermit):
    ```shell
    emerge -v app-text/pdfcpu-bin
    ```


## <span class="section-num">3</span> Использование {#использование}


### <span class="section-num">3.1</span> Примечания {#примечания}

-   При чтении документов в формате pdf можно делать примечания, которые сохраняются как `Annotation`.
-   После работы может возникнуть желание удалить их.
-   Для этого можно использовать команду:
    ```shell
    pdfcpu annotations remove [-p(ages) selectedPages] inFile [outFile] [objNr|annotId|annotType]
    ```
-   Удалить аннотацию с номером объекта 575, взятую из вывода `pdfcpu annotation list`:
    ```shell
    pdfcpu annot remove test.pdf 575
    ```
-   Удалить аннотации для первых 5 страниц:
    ```shell
    pdfcpu annot remove -pages 1-5 test.pdf
    ```
-   Удалить все аннотации:
    ```shell
    pdfcpu annot remove test.pdf
    ```


### <span class="section-num">3.2</span> Водяные знаки {#водяные-знаки}

-   Водяные знаки можно накладывать друг на друга.
-   Это позволяет создавать более сложные штампы страниц --- смесь текста, изображений и стороннего содержимого PDF-страниц.
-   Водяной знак --- это текст или изображение, которое появляется перед или позади существующего содержимого документа.
-   Водяной знак интегрирован в страницу PDF как фиксированный элемент.
-   В `pdfcpu` выделяется два вида водяных знаков:
    -   `stamp`: появляется перед существующим содержимым страницы, располагаясь поверх всего остального на странице в фиксированном положении;
    -   `watermark`: появляется за существующим содержимым страницы и находится на фоне страницы в фиксированном положении.
-   Применение:
    ```shell
    pdfcpu watermark add    [-p(ages) selectedPages] -m(ode) text|image|pdf -- string|file description inFile [outFile]
    pdfcpu watermark update [-p(ages) selectedPages] -m(ode) text|image|pdf -- string|file description inFile [outFile]
    pdfcpu watermark remove [-p(ages) selectedPages] inFile [outFile]
    ```
-   Можно сделать на первой странице пометку как на arxiv.org:
    ```shell
    pdfcpu stamp add -mode text -p 1 -- "Text for mark" 'color:0.4 0.4 0.9, rot:90, pos:l, fontname:Courier, points:13, scalefactor:1 abs, offset:20 0' in.pdf out.pdf
    ```
-   При просмотре информации о файле можно увидеть свойство `Watermarked: Yes`:
    ```shell
    pdfcpu info out.pdf
    ```
