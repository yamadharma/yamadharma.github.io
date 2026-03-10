---
title: "Pdf. Оглавление. pdf-toc"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-21T20:20:00+03:00
lastmod: 2024-06-21T20:52:00+03:00
tags: ["pdf"]
categories: ["computer-science"]
draft: false
slug: "pdf-toc-pdf-toc"
---

Pdf. Оглавление. pdf-toc.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/HareInWeed/pdf-toc>
-   Позволяет считывать отравление из pdf-файла и записывать оглавление в pdf-файл.


## <span class="section-num">2</span> Форматы файлов оглавления {#форматы-файлов-оглавления}

-   Поддерживаются два типа файлов toc.
-   Формат json, который в основном соответствует спецификации PyMuPDF.
-   Локально определённый формат на основе markdown.


## <span class="section-num">3</span> Установка {#установка}

-   Устанавливается как приложение python:
    ```shell
    pip --user install pdf-toc
    ```


## <span class="section-num">4</span> Примеры применения {#примеры-применения}

-   Показать содержание файла pdf в формате toc:
    ```shell
    pdf-toc --show-toc toc file.pdf
    ```
-   Создайте новый pdf-файл на основе файла `file.pdf` и оглавления toc из toc.txt:
    ```shell
    pdf-toc -t toc.txt -d new-file.pdf file.pdf
    ```
-   Заменить оглавление файла `file.pdf` на содержание из toc.txt:
    ```shell
    pdf-toc -m -t toc.txt file.pdf
    ```
