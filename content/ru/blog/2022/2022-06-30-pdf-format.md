---
title: "Формат PDF"
author: ["Dmitry S. Kulyabov"]
date: 2022-06-30T18:47:00+03:00
lastmod: 2025-04-29T16:32:00+03:00
tags: ["pdf"]
categories: ["computer-science"]
draft: false
slug: "pdf-format"
---

Формат файлов _pdf_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Версии формата PDF {#версии-формата-pdf}

-   PDF 1, PDF 1.1
    -   1993-1994
    -   Работа с потоками данных, защита паролем и цветопередача, независимая от устройства.
-   PDF 1.2
    -   1996
    -   Интерактивные элементы и возможность обрабатывать действия мыши.
-   PDF 1.3
    -   1999
    -   Электронная подпись (ЭП), javaSAFEscript.
-   PDF 1.4
    -   2001
    -   Прозрачность, текстовый слой поверх картинки, метаданные ключ-значение.
-   PDF 1.5
    -   2003
    -   Мультимедиа, объектные и перекрестные потоки, слои.
-   PDF 1.6
    -   2005
    -   XML-формы, AES-шифрование.
-   PDF 1.7, PDF 2.0
    -   2005-2020
    -   AES-шифрование 256-битным ключом, архитектура XML-форм XFA 3.0.


## <span class="section-num">2</span> Стандарты формата PDF {#стандарты-формата-pdf}

-   [Стандарт PDF/A]({{< relref "2021-07-30-pdf-a-standard" >}})


## <span class="section-num">3</span> Обработка PDF {#обработка-pdf}

-   [Pdf. Обработка. pdfcpu]({{< relref "2023-12-02-pdf-processing-pdfcpu" >}})
-   [Конвертация djvu в pdf. dpsprep]({{< relref "2025-04-29--convert-djvu-pdf-dpsprep" >}})
-   [Примеры команд для обработки pdf]({{< relref "2024-04-28-examples-pdf-processing-commands" >}})
-   [Распознавание pdf]({{< relref "2024-08-21-pdf-ocr" >}})


## <span class="section-num">4</span> Оглавление в PDF {#оглавление-в-pdf}

-   [Pdf. Оглавление. pdf-toc]({{< relref "2024-06-21-pdf-toc-pdf-toc" >}})
    -   Позволяет копировать оглавление в текстовый файл и обратно загружать в pdf-файл.
-   [Pdf. Оглавление. pdf.tocgen]({{< relref "2024-06-21-pdf-toc-pdf-tocgen" >}})
    -   Позволяет создавать оглавление на основе шаблона заголовков.


## <span class="section-num">5</span> Просмотр PDF {#просмотр-pdf}

-   [Pdf. Просмотр. Zathura]({{< relref "2023-09-20-pdf-viewer-zathura" >}})
-   [Pdf. Поиск подстроки]({{< relref "2023-06-27-pdf-grep" >}})
-   [Pdf. Просмотр. Sioyek]({{< relref "2024-04-24-pdf-viewer-sioyek" >}})


## <span class="section-num">6</span> Использование в LaTeX {#использование-в-latex}

-   [LaTeX. Пакет pdfx]({{< relref "2021-07-30-latex-packages-pdfx" >}})
