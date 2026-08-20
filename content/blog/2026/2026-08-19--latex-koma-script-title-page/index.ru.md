---
title: "LaTeX. KOMA-Script. Титульные страницы"
author: ["Dmitry S. Kulyabov"]
date: 2026-08-19T21:09:00+03:00
lastmod: 2026-08-19T21:23:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex-koma-script-title-page"
---

LaTeX. KOMA-Script. Титульные страницы.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   В KOMA-Script два способа создать титульную страницу.
    -   С помощью стандартной команды `\maketitle`.
    -   С помощью окружения `titlepage`.


## <span class="section-num">2</span> Команда `\maketitle` {#команда-maketitle}

-   Создаётся комплект титульных страниц: авантитул (полутитул), основной титул, страницу с выходными данными и т.д.


### <span class="section-num">2.1</span> Основные команды {#основные-команды}

-   `\titlehead{...}` : верхний колонтитул титула (занимает всю ширину страницы).
-   `\subject{...}` : тема или рубрика (печатается сразу над заголовком).
-   `\title{...}` : основной заголовок.
-   `\subtitle{...}` : подзаголовок.
-   `\author{...}` : автор; для нескольких авторов используется `\and`.
-   `\date{...}` : дата.
-   `\publishers{...}` : издатель.
-   `\extratitle{...}` : содержимое для авантитула (полутитула), который будет на первой странице перед основным титулом.
-   `\dedication{...}` : страница с посвящением.
-   `\thanks{...}` : сноска для титульной страницы.


### <span class="section-num">2.2</span> Пример {#пример}

```tex
\documentclass{scrbook}

\begin{document}

% --- Данные для титульных страниц ---
\titlehead{Университет имени И.И. Иванова}
\subject{Научное издание}
\title{Название книги}
\subtitle{Подзаголовок}
\author{Иван Иванов}
\date{Москва, 2026}
\publishers{Издательство ``Знание''}

% Создаём титульные страницы
\maketitle

% --- Далее идёт основной текст книги ---
\chapter{Введение}
...
\end{document}
```


## <span class="section-num">3</span> Окружение `titlepage` {#окружение-titlepage}

-   Этот способ даёт полную свободу вёрстки.
-   Внутри можно использовать любые команды LaTeX для форматирования.


### <span class="section-num">3.1</span> Пример {#пример}

```tex
\documentclass{scrbook}

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

\chapter{Первая глава}
...
\end{document}
```


## <span class="section-num">4</span> Опция класса `titlepage` {#опция-класса-titlepage}

-   У класса `scrbook` есть опция `titlepage`, которая управляет тем, как ведёт себя `\maketitle`.

-   `titlepage=true` (по умолчанию): `\maketitle` создаёт титульные страницы.
-   `titlepage=false`: `\maketitle` размещает заголовок в начале первой страницы текста, как в статье.
-   `titlepage=firstiscover`: делает первый титул (авантитул) похожим на обложку, с возможностью настройки полей (`coverpagetopmargin` и др.).
