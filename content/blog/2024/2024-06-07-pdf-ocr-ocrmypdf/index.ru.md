---
title: "Распознавание pdf. OCRmyPDF"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-07T21:07:00+03:00
lastmod: 2025-10-11T16:53:00+03:00
tags: ["pdf", "read"]
categories: ["computer-science"]
draft: false
slug: "pdf-ocr-ocrmypdf"
---

Распознавание pdf. OCRmyPDF

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/ocrmypdf/OCRmyPDF>
-   Сайт: <https://ocrmypdf.readthedocs.io/>


## <span class="section-num">2</span> Примеры использования {#примеры-использования}


### <span class="section-num">2.1</span> Распознавание {#распознавание}

-   Список языков для распознавания:
    ```shell
    tesseract --list-langs
    ```
-   Преобразовать сканированный файл в файл PDF/A с распознаванием русского и английского языков:
    ```shell
    ocrmypdf -l rus+eng input.pdf output.pdf
    ```
-   Заменить отсканированный PDF-файл PDF/A-файлом:
    ```shell
    ocrmypdf input.pdf
    ```
-   Пропустить страницы входного PDF-файла смешанного формата, которые уже содержат текст:
    ```shell
    ocrmypdf --skip-text input.pdf output.pdf
    ```
-   Очистите, исправьте перекос и поверните плохо отсканированные страницы:
    ```shell
    ocrmypdf --clean --deskew --rotate-pages input.pdf output.pdf
    ```
-   Убрать фон:
    ```shell
    ocrmypdf --clean --remove-background input.pdf output.pdf
    ```
-   Разделить сдвоенные страницы:
    ```shell
    ocrmypdf -l rus+eng --clean --clean-final --unpaper-args '--layout double' input.pdf output.pdf
    ```
-   Контролируем оптимизацию:
    ```shell
    ocrmypdf --optimize 3 --jbig2-lossy input.pdf output.pdf
    ```
-   Распознавание с оптимизацией:
    ```shell
    ocrmypdf -l rus+eng --optimize 3 --jbig2-lossy input.pdf output.pdf
    ```
-   Задать метаданные PDF-файла:
    ```shell
    ocrmypdf --skip-text --title "<title>" --author "<author>" --subject "<subject>" --keywords "<keyword; key phrase; ...>" input_file.pdf output.pdf
    ```


### <span class="section-num">2.2</span> Не распознавать pdf-файл {#не-распознавать-pdf-файл}

-   При установке параметра `--tesseract-timeout 0`  OCRmyPDF будет обрабатывать изображения без выполнения OCR.
    ```shell
    ocrmypdf --tesseract-timeout=0 --remove-background input.pdf output.pdf
    ```
-   Удалить весь распознанный текст из pdf-файла:
    ```shell
    ocrmypdf --tesseract-timeout 0 --optimize 3 --force-ocr input.pdf output.pdf
    ```
-   Оптимизация изображений без выполнения распознавания:
    ```shell
    ocrmypdf --tesseract-timeout=0 --optimize 3 --skip-text input.pdf output.pdf
    ```


### <span class="section-num">2.3</span> OCR для больших изображений {#ocr-для-больших-изображений}

-   Иногда не распознаются некоторые страницы.
-   Tesseract имеет внутренние ограничения по размеру изображений, которые он обработает.
-   По умолчанию включён `--tesseract-downsample-large-images`, OCRmyPDF будет понижает разрешение изображений.
-   Эту функцию можно отключить с использованием `--no-tesseract-downsample-large-images`.
-   Необходимо установить `--tesseract-timeout` достаточно большим:

<!--listend-->

```shell
ocrmypdf --tesseract-timeout 600 --tesseract-downsample-large-images bigfile.pdf output.pdf
```

-   Можно установить границу уменьшения в 5000 пикселей:

<!--listend-->

```shell
ocrmypdf --tesseract-timeout 120 --tesseract-downsample-large-images --tesseract-downsample-above 5000 bigfile.pdf output_downsampled_ocr.pdf
```


### <span class="section-num">2.4</span> Используемые мной команды {#используемые-мной-команды}

-   Удалить весь распознанный текст из pdf-файла (если текст кракозябрами):
    ```shell
    ocrmypdf --tesseract-timeout 0 --optimize 3 --force-ocr input.pdf output.pdf
    ```
-   Распознать файл:
    ```shell
    ocrmypdf -l rus+eng --optimize 3 --tesseract-timeout 600 --tesseract-downsample-large-images input.pdf output.pdf
    ```
