---
title: "LaTeX. Пакет physics3"
author: ["Dmitry S. Kulyabov"]
date: 2026-07-25T21:24:00+03:00
lastmod: 2026-07-25T21:40:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex-physics3-package"
---

LaTeX. Пакет physics3.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Пакеты `physics`, `physics2` и `physics3` --- это три разных поколения пакетов для LaTeX, созданных для упрощения набора математических и физических формул.


## <span class="section-num">2</span> physics {#physics}

-   CTAN: <https://www.ctan.org/pkg/physics>
-   Оригинальный и самый старый пакет.
-   Он предоставляет множество удобных команд, но имеет ряд серьезных архитектурных проблем:
    -   Существует риск переполнения памяти при использовании более 32767 матричных команд.
    -   Устаревший код. Активно использует `g`-аргумент в `xparse`, что не рекомендуется командой LaTeX.
    -   Заброшен. Для исправления его ошибок существует отдельный пакет-заплатка `physics-patch`.


## <span class="section-num">3</span> physics2 {#physics2}

-   CTAN: <https://www.ctan.org/pkg/physics2>
-   Репозиторий: <https://github.com/AlphaZTX/physics2>

-   Модернизированная модульная версия, пришедшая на смену оригинальному пакету.
-   Ядро (`physics2.sty`) содержит лишь базовые функции, а все остальные возможности подключаются по мере необходимости через отдельные модули.


## <span class="section-num">4</span> physics3 {#physics3}

-   CTAN: <https://www.ctan.org/pkg/physics3>
-   Репозиторий: <https://github.com/myhsia/physics3>
-   Создан как прямая замена `physics` и `physics2`, исправляя их недостатки.
-   Основные улучшения:
    -   Решена проблема с переполнением памяти, которая была в оригинальном `physics`.
    -   Улучшены и оптимизированы команды для работы с матрицами.
    -   Код написан с использованием актуальных и рекомендованных практик LaTeX.
