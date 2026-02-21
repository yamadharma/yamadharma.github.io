---
title: "Emacs. Пакет casual"
author: ["Dmitry S. Kulyabov"]
date: 2024-10-26T17:35:00+03:00
lastmod: 2025-03-24T15:04:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-casual"
---

Emacs. Пакет casual.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/kickingvegas/casual>
-   Коллекция пакетов, реализующих интерфейс с клавиатурным меню наа основе transient (см. [Emacs. Пакет transient]({{< relref "2024-10-26-emacs-transient" >}})).


## <span class="section-num">2</span> Общее управление {#общее-управление}

-   Общие действия меню Casual построен с использованием переходных меню.
-   Каждый пункт меню имеет ключ и метку.
-   Ключ --- это то, что набирает пользователь для выбора пункта меню.
-   Ключ может иметь префикс : Meta (M-) или Control (C-).
-   Transient поддерживает вложенные меню.
-   Выход из меню может быть осуществлен двумя способами:
    -   `C-g` : выход из текущего подменю и возврат в родительское меню;
    -   `C-q` : полный выход из стека меню Transient.
-   Если есть мышь, пункт меню можно выбрать, наведя курсор на его ярлык и нажав кнопку 1.
-   Нажатие клавиш `?` или `C-h` переключает справку по всем пунктам меню.
    -   Нажмите интересующую вас клавишу, чтобы получить справку по ней.
-   При вызове переходного меню перед выбором пункта меню можно ввести префиксный аргумент (`C-u`) и дополнительный аргумент.


## <span class="section-num">3</span> Состав коллекции {#состав-коллекции}


### <span class="section-num">3.1</span> Повестка дня {#повестка-дня}

-   Библиотека elisp: `casual-agenda`
-   Интерфейс для повестки дня org-mode.
-   Подключение:
    ```emacs-lisp
    (require 'casual-agenda)
    ```
-   Клавиатурная комбинация для вызова:
    ```emacs-lisp
    (keymap-set org-agenda-mode-map "C-o" #'casual-agenda-tmenu)
    ```
-   Переключение между агендой и casual:
    ```emacs-lisp
    ;;;; bindings to make jumping consistent between Org Agenda and Casual Agenda
    (keymap-set org-agenda-mode-map "M-j" #'org-agenda-clock-goto) ; optional
    (keymap-set org-agenda-mode-map "J" #'bookmark-jump) ; optional
    ```


### <span class="section-num">3.2</span> Закладки {#закладки}

-   Библиотека elisp: `casual-bookmarks`.
-   Интерфейс для редактирования коллекции закладок.


### <span class="section-num">3.3</span> Калькулятор {#калькулятор}

-   Библиотека elisp: `casual-calc`.
-   Интерфейс для Emacs Calc.


### <span class="section-num">3.4</span> Dired {#dired}

-   Библиотека elisp: `casual-dired`.
-   Интерфейс для файлового менеджера Dired.


### <span class="section-num">3.5</span> EditKit {#editkit}

-   Библиотека elisp: `casual-editkit`.
-   Различные функции редактирования (например, маркировка, копирование, уничтожение, дублирование, преобразование, удаление).


### <span class="section-num">3.6</span> IBuffer {#ibuffer}

-   Библиотека elisp: `casual-ibuffer`.


### <span class="section-num">3.7</span> Image {#image}

-   Библиотека: `casual-image`.


### <span class="section-num">3.8</span> Info {#info}

-   Библиотека elisp: `casual-info`.
-   Интерфейс для системы документации Info.


### <span class="section-num">3.9</span> I-Search {#i-search}

-   Библиотека elisp: `casual-isearch`.
-   Интерфейс для команд I-Search.


### <span class="section-num">3.10</span> Make {#make}

-   Библиотека: `casual-make`.


### <span class="section-num">3.11</span> Re-Builder {#re-builder}

-   Библиотека elisp: `casual-re-builder`.
-   Интерфейс для регулярных выражений Emacs.


## <span class="section-num">4</span> Мотивация {#мотивация}

-   В Emacs имеется множество команд, которые легко забыть, если они не пользоваться ими часто.
-   Transient позволяет создавать пользовательский интерфейс меню, управляемый клавиатурой.
-   Это привлекательно для пользователей, которые предпочитают рабочие процессы, основанные на клавиатуре.
-   Пакет должен предоставить набор инструментов пользовательского интерфейса с клавиатурным меню для распространенных команд Emacs.
