---
title: "Emacs. tab-line. Пакет intuitive-tab-line-mode"
author: ["Dmitry S. Kulyabov"]
date: 2025-10-16T09:19:00+03:00
lastmod: 2025-10-16T09:37:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-intuitive-tab-line-mode"
---

Emacs. tab-line. Пакет intuitive-tab-line-mode.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/thread314/intuitive-tab-line-mode>
-   Добавляет более интуитивное управление табами.


## <span class="section-num">2</span> Клавиатурные сочетания {#клавиатурные-сочетания}

| Клавиатурное сочетание | Назначение                  | Функция                              | Примечание                                     |
|------------------------|-----------------------------|--------------------------------------|------------------------------------------------|
| `Ctrl+PgDown`          | Предыдущая вкладка          | `tab-line-switch-to-prev-tab`        | Из `tab-line`                                  |
| `Ctrl+Shift+Tab`       | Предыдущая вкладка          | `tab-line-switch-to-prev-tab`        | Из `tab-line`. Может конфликтовать с `tab-bar` |
| `Ctrl+PgUp`            | Следующая вкладка           | `tab-line-switch-to-next-tab`        | Из `tab-line`.                                 |
| `Ctrl+Tab`             | Следующая вкладка           | `tab-line-switch-to-next-tab`        | Из `tab-line`. Может конфликтовать с `tab-bar` |
| `Ctrl+Shift+PgDown`    | Передвинуть вкладку налево  | `intuitive-tab-line-shift-tab-left`  | Из `intuitive-tab-line-mode`                   |
| `Ctrl+Shift+PgUp`      | Передвинуть вкладку направо | `intuitive-tab-line-shift-tab-right` | Из `intuitive-tab-line-mode`                   |
| `Ctrl+Shift+t`         | Открыть последний файл      | `recentf-open-most-recent-file`      | На основе `recentf-mode`                       |
