---
title: "Emacs. Пакет doc-toc"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-10T14:15:00+03:00
lastmod: 2025-05-10T15:32:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-package-doc-toc"
---

Emacs. Пакет doc-toc.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   ELPA: <https://elpa.gnu.org/packages/doc-toc.html>
-   Репозиторий: <https://github.com/dalanicolai/doc-tools-toc>


### <span class="section-num">1.1</span> Предыдущий вариант пакета {#предыдущий-вариант-пакета}

-   Название:
-   Репозиторий: <https://github.com/dalanicolai/toc-mode>
-   Оставлен для совместимости.
-   Чтобы пакеты, использующие его, не перестали работать.


## <span class="section-num">2</span> Установка {#установка}

-   Зависимости:
    -   `pdftotext` (из пакета `poppler-utils`),
    -   `pdfoutline` (из `fntsample`),
    -   `djvused` (для DjVu),
    -   `tesseract` (для OCR, если документ без текстового слоя);
    -   pdf-tocgen (см. [Pdf. Оглавление. pdf.tocgen]({{< relref "2024-06-21-pdf-toc-pdf-tocgen" >}})).
-   Gentoo:
    -   Основной репозиторий:
        ```shell
        USE=utils emerge app-text/poppler
        emerge app-text/djvu
        emerge app-text/tesseract
        ```
    -   Оверлей: `4nykey` и `karma` (см. [Gentoo. Дополнительные репозитории]({{< relref "2023-10-01-gentoo-additional-repositories" >}})):
        ```shell
        emerge app-text/fntsample
        ```


## <span class="section-num">3</span> Использование {#использование}

-   Извлечение и добавление содержимого в документ выполняется в 4 этапа:
    -   извлечение
    -   очистка
    -   отрегулировать/исправить номера страниц
    -   добавить оглавление в документ


### <span class="section-num">3.1</span> Извлечение оглавления {#извлечение-оглавления}


#### <span class="section-num">3.1.1</span> Для PDF с текстовым слоем {#для-pdf-с-текстовым-слоем}

-   Откройте PDF в Emacs (рекомендуется `pdf-tools`).
-   Выполните `M-x doc-toc-extract-pages`.
-   Укажите начальную и конечную страницы оглавления.
-   Результат появится в буфере `TOC-cleanup`.


#### <span class="section-num">3.1.2</span> Для сканированных PDF/DjVu (через OCR): {#для-сканированных-pdf-djvu--через-ocr}

-   Выполните `M-x doc-toc-extract-pages-ocr`.
-   Укажите диапазон страниц и параметры OCR (например, `psm 1` для двухколоночного текста).


### <span class="section-num">3.2</span> Очистка и настройка структуры {#очистка-и-настройка-структуры}

-   В режиме `TOC-cleanup`:
    -   Объедините строки без номеров: `C-c C-j`.
    -   Преобразуйте римские цифры в арабские: `C-c C-s`.
    -   Используйте `C-c C-c` для перехода к следующему шагу.


### <span class="section-num">3.3</span> Корректировка номеров страниц {#корректировка-номеров-страниц}

-   В режиме `doc-toc-mode`:
    -   Перемещайтесь по записям: `TAB` (предпросмотр страницы).
    -   Изменяйте номера: `S-right` / `S-left` (увеличить/уменьшить).
    -   Прокрутка документа: `C-down` / `C-up`.


### <span class="section-num">3.4</span> Добавление оглавления в документ {#добавление-оглавления-в-документ}

1.  После настройки нажмите `C-c C-c`.
2.  Для PDF:
    -   Оглавление добавится в копию файла (`output.pdf`).
    -   Если `doc-toc-replace-original-file` = `nil`, исходный файл не изменится.


### <span class="section-num">3.5</span> Советы {#советы}

-   Для автоматического определения уровней заголовков:
    1.  Выделите слово в заголовке.
    2.  Выполните `M-x doc-toc-gen-set-level` → укажите уровень (1, 2 и т.д.).
    3.  Запустите `M-x doc-toc-extract-with-pdf-tocgen`.


## <span class="section-num">4</span> Пример конфигурации для двухколоночного TOC {#пример-конфигурации-для-двухколоночного-toc}

```emacs-lisp
;; Настройка языков OCR
(setq doc-toc-ocr-languages '("eng+rus"))
;; Не заменять исходный файл
(setq doc-toc-replace-original-file nil)
```


## <span class="section-num">5</span> Клавиатурные сочетания {#клавиатурные-сочетания}

-   all-modes
    -   `C-c C-c` :  dispatch (next step)
-   doc-toc-cleanup-mode
    -   `C-c C-j` : doc-toc--join-next-unnumbered-lines
    -   `C-c C-s` : doc-toc--roman-to-arabic
-   doc-toc (tablist)
    -   `TAB` : preview/jump-to-page
    -   `right` / `left` :  doc-toc-in/decrease-remaining
    -   `C-right` / `C-left` : doc-toc-in/decrease-remaining and view page
    -   `S-right` / `S-left` : in/decrease pagenumber current entry
    -   `C-down` / `C-up` :  scroll document other window (if document buffer shown)
    -   `S-down` / `S-up` :  full page scroll document other window ( idem )
    -   `C-j` : doc-toc--jump-to-next-entry-by-level
