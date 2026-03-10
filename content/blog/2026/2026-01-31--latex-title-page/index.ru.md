---
title: "LaTeX. Титульная страница"
author: ["Dmitry S. Kulyabov"]
date: 2026-01-31T16:39:00+03:00
lastmod: 2026-01-31T16:48:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex-title-page"
---

LaTeX. Титульная страница.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Встроенное окружение titlepage {#встроенное-окружение-titlepage}

-   Пример:
    ```tex
    \documentclass{scrbook}
    \usepackage[T2A]{fontenc}
    \usepackage[utf8]{inputenc}
    \usepackage[russian]{babel}

    \begin{document}

    \begin{titlepage}
        \centering
        {\Huge\bfseries Название вашей книги\par}
        \vspace{1cm}
        {\Large Подзаголовок или описание\par}
        \vspace{2cm}
        {\Large\textbf{Имя Автора}\par}
        \vspace{3cm}
        {\large Город, Год издания\par}
        \vfill
        {\small Издательство или дополнительная информация\par}
    \end{titlepage}

    % Остальное содержимое книги
    \mainmatter
    \chapter{Первая глава}
    ...

    \end{document}
    ```


## <span class="section-num">2</span> Создание обложек с пакетом bookcover {#создание-обложек-с-пакетом-bookcover}

-   Отдельный класс.
-   CTAN: <https://ctan.org/pkg/bookcover>
-   Верстка книжных обложек и суперобложек.


## <span class="section-num">3</span> Стили uni-titlepage {#стили-uni-titlepage}

-   CTAN: <https://ctan.org/pkg/uni-titlepage>
-   Предоставляет множество предопределенных стилей титульной страницы с несколькими стандартными элементами.
-   Возможность добавления дополнительных элементов.


## <span class="section-num">4</span> titlepages {#titlepages}

-   CTAN: <https://ctan.org/pkg/titlepages>
-   Примеры титульных страниц.
-   Проекты, основанные на ряде опубликованных книг и диссертаций.
