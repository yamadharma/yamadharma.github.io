---
title: "Quarto. Титульная страница"
author: ["Dmitry S. Kulyabov"]
date: 2026-08-20T21:15:00+03:00
lastmod: 2026-08-20T21:30:00+03:00
tags: ["markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-title-page"
---

Quarto. Титульная страница

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Расширения {#расширения}


### <span class="section-num">1.1</span> Расширение `quarto_titlepages` {#расширение-quarto-titlepages}

-   Репозиторий: <https://github.com/nmfs-opensci/quarto_titlepages>
-   Документация: <https://nmfs-opensci.github.io/quarto_titlepages/>
-   Добавляет титульные страницы и обложки для pdf.


#### <span class="section-num">1.1.1</span> Установка {#установка}

-   Создание проекта:
    ```shell
    quarto use template nmfs-opensci/quarto_titlepages
    ```

-   Подключение к существующему проекту
    ```shell
    quarto install extension nmfs-opensci/quarto_titlepages
    ```


#### <span class="section-num">1.1.2</span> Подключение {#подключение}

-   Доступны различные темы: `bg-image` (с фоновым изображением), `vline` (с вертикальной линией), `minimal`, `classic` и другие.
-   В `_quarto.yml`:
    ```yaml
    format:
      titlepage-pdf:
        titlepage: bg-image  # или vline, minimal, classic и др.
    ```


#### <span class="section-num">1.1.3</span> Настройка {#настройка}

-   В yaml можно передать параметры:
    -   `titlepage-theme` : тема оформления
    -   `titlepage-font` : шрифт
    -   `titlepage-color` : цвет
    -   `titlepage-geometry` : положение элементов

-   В репозитории есть готовые примеры:
    -   `example_1.qmd`: только титульная страница;
    -   `example_2.qmd`, `example_3.qmd`: обложка, страница копирайта, титульная страница и страница посвящения.


## <span class="section-num">2</span> Частичный LaTeX-шаблоны {#частичный-latex-шаблоны}

-   [LaTeX. Титульная страница]({{< relref "2026-01-31--latex-title-page" >}})
-   Используется частичный шаблон (template partials).


### <span class="section-num">2.1</span> Структура {#структура}

-   Частичный шаблон `before-body.tex` вставляется сразу после `\begin{document}` и заменяет стандартную титульную страницу.

-   Создайте в корне проекта файл c частичным шаблоном.
    ```tex
    \begin{titlepage}
    \centering
    \vspace*{2cm}

    % Логотип
    \includegraphics[width=0.4\textwidth]{logo.png}\\[2cm]

    % Название
    {\Huge\bfseries $title$}\\[0.5cm]
    {\Large $subtitle$}\\[2cm]

    % Автор
    {\large $author$}\\[0.5cm]
    {\large $date$}\\[2cm]

    % Нижняя часть
    \vfill
    {\large Издательство}
    \end{titlepage}

    \clearpage

    % ВТОРАЯ СТРАНИЦА
    \begin{center}
    \vspace*{2cm}
    {\Large\bfseries $title$}\\[1cm]

    \noindent ISBN: 978-5-00000-000-0\\
    \noindent Лицензия: CC BY 4.0\\[0.5cm]

    \noindent \textbf{Аннотация:}\\
    $description$

    \vfill
    \noindent \copyright~Автор, $date$
    \end{center}
    \clearpage
    ```

-   Подключите шаблон в `_quarto.yml`:
    ```yaml
    format:
      pdf:
        template-partials:
    ​      - before-body.tex
    ```

-   По умолчанию Quarto использует KOMA-script (`scrbook`, `scrartcl`).
-   Вместо `\maketitle` можно использовать `\begin{titlepage}...\end{titlepage}` (см. [LaTeX. KOMA-Script. Титульные страницы]({{< relref "2026-08-19--latex-koma-script-title-page" >}})).
-   В шаблонах доступны переменные pandoc: `$title$`, `$author$`, `$date$`, `$subtitle$` и др.
-   Для второй страницы используйте `\clearpage` после титульной.
