---
title: "Emacs. Пакет tab-line"
author: ["Dmitry S. Kulyabov"]
date: 2024-01-08T20:02:00+03:00
lastmod: 2025-10-16T15:49:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-tab-line"
---

Emacs. Пакет tab-line.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Включено в Emacs 27.
-   Область действия --- в рамках окна, в каждом табе --- буфер.


## <span class="section-num">2</span> Настройка {#настройка}


### <span class="section-num">2.1</span> Включение режима {#включение-режима}

-   Включить режим:
    ```emacs-lisp
    (global-tab-line-mode t)
    ```


### <span class="section-num">2.2</span> Группировка вкладок {#группировка-вкладок}

-   Вкладки группируются согласно функции `tab-line-tabs-function`.


## <span class="section-num">3</span> Навигация {#навигация}

-   Передвижение по вкладкам выполняется с помощью клавиш:
    -   `C-x LEFT` (`previous-buffer`);
    -   `C-x RIGHT` (`next-buffer`).


## <span class="section-num">4</span> Клавиатурные сочетания tab-line {#клавиатурные-сочетания-tab-line}

| Клавиатурное сочетание | Назначение                  | Функция                              | Примечание                                     |
|------------------------|-----------------------------|--------------------------------------|------------------------------------------------|
| `Ct rl+PgDown`         | Предыдущая вкладка          | `tab-line-switch-to-prev-tab`        | Из `tab-line`                                  |
| `Ctrl+Shift+Tab`       | Предыдущая вкладка          | `tab-line-switch-to-prev-tab`        | Из `tab-line`. Может конфликтовать с `tab-bar` |
| `Ctrl+PgUp`            | Следующая вкладка           | `tab-line-switch-to-next-tab`        | Из `tab-line`.                                 |
| `Ctrl+Tab`             | Следующая вкладка           | `tab-line-switch-to-next-tab`        | Из `tab-line`. Может конфликтовать с `tab-bar` |
| `Ctrl+Shift+PgDown`    | Передвинуть вкладку налево  | `intuitive-tab-line-shift-tab-left`  | Из `intuitive-tab-line-mode`                   |
| `Ctrl+Shift+PgUp`      | Передвинуть вкладку направо | `intuitive-tab-line-shift-tab-right` | Из `intuitive-tab-line-mode`                   |
| `Ctrl+Shift+t`         | Открыть последний файл      | `recentf-open-most-recent-file`      | На основе `recentf-mode`                       |


## <span class="section-num">5</span> Пакеты расширения {#пакеты-расширения}


### <span class="section-num">5.1</span> intuitive-tab-line-mode {#intuitive-tab-line-mode}

-   Репозиторий: <https://github.com/thread314/intuitive-tab-line-mode>
-   Добавляет более интуитивное управление табами.
-   [Emacs. tab-line. Пакет intuitive-tab-line-mode]({{< relref "2025-10-16--emacs-intuitive-tab-line-mode" >}})
