---
title: "Проверка документов в CEURART"
author: ["Dmitry S. Kulyabov"]
date: 2024-10-27T19:39:00+03:00
lastmod: 2026-02-19T16:28:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "ceurart-check"
---

Проверка документов перед отправкой в депозитарий CEUR-WS.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Основные проблемы {#основные-проблемы}

-   Возможные проблемы с pdf-файлами.
-   Pdf-документы не используют шрифты Libertinus.
    -   Необходимо запрашивать исправления у организаторов семинаров, если многие документы не используют Libertinus.
    -   Если документов всего 1-2, то можно на это закрыть глаза.
-   Растровые документы pdf.
    -   Нет возможности выделения текста.
    -   Поисковые системы, такие как Google Scholar, не смогут правильно проиндексировать эти статьи.


## <span class="section-num">2</span> Утилиты {#утилиты}

-   Утилиты для проверки документов для CEUR-WS находятся в репозитории: <https://github.com/yamadharma/ceurart-check>


### <span class="section-num">2.1</span> `check-pdf-errors` {#check-pdf-errors}

-   Источник: <https://ceur-ws.org/check-pdf-errors>
-   Проверяет pdf-файлы.
-   Проверка наличия фразы 'Creative Commons' в pdf-файлах.
    -   Это делается чтобы проверить, можно ли выделить текст (не является ли документ картинкой).
-   Проверка использования шрифтов Libertinus.
-   Проверка дублирования pdf-файлов.


### <span class="section-num">2.2</span> `check-index-errors` {#check-index-errors}

-   Источник: <https://ceur-ws.org/check-index-errors>
-   Проверяет файл `index.html`.
-   Правила:
    -   документы в формате `pdf`, которые есть в каталоге, но не перечислены в `index.html`;
    -   документы, на которые даны ссылки в `index.html`, но которые отсутствуют;
    -   проверка количества статей, опубликованных в рамках программы `CEURVOLEDITOR`, что помогает проверить часть правила разнообразия.


### <span class="section-num">2.3</span> `ceur-add-pagenum` {#ceur-add-pagenum}

-   Репозиторий: <https://github.com/amato-gianluca/ceur-add-pagenum>
-   Скрипт на Python для подсчёта количества страниц в PDF-файлах, связанных с документом index.html (подготовленным для отправки в CEUR-WS), и обновления полей CEURPAGES.
-   Скрипт не изменяет PDF-файлы, а только `index.html`.
-   Скрипт зависит от пакетов `lxml` и `PyPDF2`.


## <span class="section-num">3</span> Пререквизиты {#пререквизиты}


### <span class="section-num">3.1</span> Official W3C HTML validation check {#official-w3c-html-validation-check}

-   Download vnu.jar from <https://github.com/validator/validator/releases/download/latest/vnu.jar> into `$HOME/bin` for a full check.


## <span class="section-num">4</span> Проверка {#проверка}

-   Проверьте pdf-файлы:
    ```shell
    check-pdf-errors
    ```
-   Проверьте `index.html`:
    ```shell
    check-index-errors
    ```
