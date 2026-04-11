---
title: "Тегированный pdf. Реализации"
author: ["Dmitry S. Kulyabov"]
date: 2026-04-11T15:54:00+03:00
lastmod: 2026-04-11T16:05:00+03:00
tags: ["pdf"]
categories: ["computer-science"]
draft: false
slug: "tagged-pdf-implementations"
---

Тегированный pdf. Реализации.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Реализации {#реализации}

-   Quarto. Тегированный pdf


## <span class="section-num">2</span> Quarto {#quarto}

-   [Система Quarto]({{< relref "2025-03-22--quarto-system" >}})


### <span class="section-num">2.1</span> Общая информация {#общая-информация}

-   Необходимо для проверки установить VeraPDF:
    ```shell
    quarto install verapdf
    ```


### <span class="section-num">2.2</span> Настройка {#настройка}


#### <span class="section-num">2.2.1</span> PDF (LaTeX) {#pdf--latex}

```yaml
format:
  pdf:
    pdf-standard: ua-2
```


#### <span class="section-num">2.2.2</span> Typst {#typst}

```yaml
format:
  typst:
    pdf-standard: ua-1
```


### <span class="section-num">2.3</span> Если документ не прошел проверку {#если-документ-не-прошел-проверку}


#### <span class="section-num">2.3.1</span> LaTeX {#latex}

-   LaTeX не выполняет проверку данных во время генерации PDF-файлов.
-   Если проверка veraPDF не пройдена, то будет предупреждение, и вы все равно получите частично доступный PDF-файл.


#### <span class="section-num">2.3.2</span> Typst {#typst}

-   Typst выдает ошибку и не создает PDF-файл, если встроенная проверка не проходит во время генерации PDF.


### <span class="section-num">2.4</span> Особенности {#особенности}

Требования доступности:

-   Метаданные документа (заголовок, автор, дата, язык) передаются во встроенные поля метаданных PDF-файла.
-   Семантическая структура Markdown удовлетворяет требованиям к тегированию PDF-файлов. Для Typst эта функция всегда включена; для LaTeX она включается, когда вы указываете стандарт, который этого требует.
-   Альтернативный текст для изображений переносится в PDF-файл для программ чтения с экрана.

Но вам необходимо убедиться, что ваш документ содержит:

-   Заголовок **.**  во вводной части YAML-файла
-   **Альтернативный текст для каждого изображения** , указанный с помощью =fig-alt=Подробности см. [на рисунках](https://quarto.org/docs/authoring/figures.html#alt-text) .
