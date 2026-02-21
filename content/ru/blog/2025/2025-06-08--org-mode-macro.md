---
title: "Org-mode. Макросы"
author: ["Dmitry S. Kulyabov"]
date: 2025-06-08T19:38:00+03:00
lastmod: 2025-06-08T19:56:00+03:00
draft: false
slug: "org-mode-macro"
---

Org-mode. Макросы.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Макросы заменяют текстовые фрагменты во время экспорта.
-   Макросы определены глобально в `org-export-global-macros` или в документе.


## <span class="section-num">2</span> Синтаксис {#синтаксис}

-   Определение:
    ```org
    #+MACRO: name   replacement text; $1, $2 are arguments
    ```
-   Можно ссылаться с помощью `{{{name(arg1, arg2)}}}`.
-   Например:
    ```org
    #+MACRO: poem Rose is $1, violet's $2. Life's ordered: Org assists you.
    {{{poem(red,blue)}}}
    ```
-   Результат:
    ```org
    Rose is red, violet's blue.  Life's ordered: Org assists you.
    ```

-   В качестве особого случая Org анализирует любой текст замены, начинающийся с `(eval` как выражение Emacs Lisp.
-   В таких шаблонах аргументы становятся строками.
-   Например:
    ```org
    #+MACRO: gnustamp (eval (concat "GNU/" (capitalize $1)))
    {{{gnustamp(linux)}}}
    ```
-   Результат:
    ```org
    GNU/Linux
    ```

-   Org распознает ссылки на макросы в следующих областях разметки Org:
    -   абзацы,
    -   заголовки,
    -   блоки стихов,
    -   ячейки таблиц,
    -   списки.
-   Org также распознает макросы в ключевых словах:
    -   `CAPTION`,
    -   `TITLE`,
    -   `AUTHOR`,
    -   `DATE`.


## <span class="section-num">3</span> Предопределённые макросы {#предопределённые-макросы}

-   `{{{keyword(NAME)}}}`
-   `{{{title}}}`
-   `{{{author}}}`
-   `{{{email}}}`
    -   макро `keyword` собирает все значения из ключевого слова `NAME` по всему буферу, разделённые пробелами.
    -   `{{{title}}}` соответствует `{{{keyword(TITLE)}}}`.
    -   `{{{author}}}` соответствует `{{{keyword(AUTHOR)}}}`.
    -   `{{{email}}}` соответствует `{{{keyword(EMAIL)}}}`.

-   `{{{date}}}`
-   `{{{date(FORMAT)}}}`
    -   Дата документа.
    -   `FORMAT` должен быть строкой формата `format-time-string`.
-   `{{{time(FORMAT)}}}`
-   `{{{modification-time(FORMAT, VC)}}}`
    -   Эти макросы ссылаются на дату и время экспорта документа и дата и время изменения.
    -   `FORMAT` : строка в форме `format-time-string`.
    -   Если второй аргумент `modification-time` не является `nil`, org-mode использует `vc.el`, чтобы получить время изменения документа из системы контроля версий. В противном случае Org считывает атрибуты файла.
-   `{{{input-file}}}`
    -   Макрос ссылается на имя экспортируемого файла.
-   `{{{property(PROPERTY-NAME)}}}`
-   `{{{property(PROPERTY-NAME, SEARCH OPTION)}}}`
    -   Макрос возвращает значение свойства `PROPERTY-NAME` текущей записи.
-   `{{{n}}}`
-   `{{{n(NAME)}}}`
-   `{{{n(NAME, ACTION)}}}`
    -   Макрос реализует пользовательские счётчики, возвращая, скользко раз макрос был выполнен при экспорте буфера.
