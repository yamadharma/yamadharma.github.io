---
title: "Emacs. Пакет org-appear"
author: ["Dmitry S. Kulyabov"]
date: 2023-01-16T18:37:00+03:00
lastmod: 2025-07-09T21:09:00+03:00
tags: ["emacs", "org-mode"]
categories: ["computer-science"]
draft: false
slug: "emacs-org-appear"
---

Пакет `org-appear`.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/awth13/org-appear>.
-   Org-mode режим позволяет переключать видимость скрытых элементов, таких как маркеры выделения, ссылки и т. д., путём настройки определённых переменных, например `org-hide-emphasis-markers`.
-   Однако время это невозможно сделать интерактивно и поэлементно.
-   Пакет `org-appear` позволяет автоматически переключать видимость в зависимости от положения курсора.
-   Скрытые части элемента появляются, когда курсор находится над элементом, и исчезают, когда курсор передвигается.


## <span class="section-num">2</span> Использование {#использование}

-   Пакет можно активировать интерактивно или автоматически при запуске `org-mode`:
    ```emacs-lisp
    (add-hook 'org-mode-hook 'org-appear-mode)
    ```
-   По умолчанию переключение происходит мгновенно, переключаются только маркеры выделения.


## <span class="section-num">3</span> Переменные настройки {#переменные-настройки}

-   `org-появляются-autoemphasis` : если не `nul` и включён `org-hide-emphasis-markers`, переключаются маркеры выделения.
-   `org-appear-autolinks` : если не `nul` и включён `org-link-descriptive`, переключаются ссылки.
-   `org-appear-autosubmarkers` : если не `nul` и включено `org-pretty-entities`, переключает нижние и верхние индексы.
-   `org-appear-autoentities` : если не `nul` и включено `org-pretty-entities`, переключить структуры org-mode.
-   `org-appear-autokeywords` : если не `nul` и включено `org-hidden-keywords`, переключает ключевые слова в `org-hidden-keywords`.
-   `org-appear-inside-latex` : если не `nul`, переключает сущности и подстрочные/надстрочные индексы во фрагментах LaTeX.
-   `org-appear-delay` : задержка перед переключением (в секундах).
-   `org-appear-trigger` : когда переключать элементы:
    -   `always` : всегда будут переключаться элементы.
    -   `on-change` : элементы будут переключаться только при изменении буфера или щелчке мыши. Эта опция отключает отложенное переключение.
    -   `manual` :  переключение должно быть разрешено вызовом `org-appear-manual-start`. `org-appear-manual-stop` используется для отключения переключения с этой опцией.
