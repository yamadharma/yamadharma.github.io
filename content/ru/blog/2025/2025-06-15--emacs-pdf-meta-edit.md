---
title: "Emacs. Пакет pdf-meta-edit"
author: ["Dmitry S. Kulyabov"]
date: 2025-06-15T19:31:00+03:00
lastmod: 2025-06-22T20:59:00+03:00
draft: false
slug: "emacs-pdf-meta-edit"
---

Emacs. Пакет pdf-meta-edit.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/krisbalintona/pdf-meta-edit>
-   Позволяет редактировать метаданные PDF-файлов: оглавление, нумерацию страниц.
-   Основные функции:
    -   представление текстовой информации о закладках, метках и страницах PDF;
    -   команды для добавления закладок и меток;
    -   базовая блокировка шрифтов.
-   Пакет использует утилиту pdftk для работы с метаданными PDF.


## <span class="section-num">2</span> Использование {#использование}

-   Откройте PDF-файл в любом из основных режимов.
-   Вызовите `M-x pdf-meta-edit-modify`.
    -   Это открывает буфер `pdf-meta-edit-mode`, содержимое которого представляет собой метаданные этого PDF-файла.
-   Перемещайтесь по буферу с помощью `pdf-meta-edit-forward-section`, `pdf-meta-edit-backward-section`, `pdf-meta-edit-forward-subsection` и `pdf-meta-edit-backward-subsection`.
-   Вставьте закладки подразделов (`pdf-meta-edit-bookmark-subsection`) и подразделы меток (`pdf-meta-edit-label-subsection`).
    -   Эти команды используют `completing-read` для запроса значений полей этих подразделов.
-   Редактируйте существующие закладки и подразделы меток.
-   Зафиксируйте содержимое буфера в файле PDF, нажав `C-c C-c`.
