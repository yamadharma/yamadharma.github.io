---
title: "Org-mode. Презентации. Beamer"
author: ["Dmitry S. Kulyabov"]
date: 2021-06-16T20:46:00+03:00
lastmod: 2025-07-09T21:08:00+03:00
tags: ["latex", "emacs", "tex", "org-mode"]
categories: ["computer-science"]
draft: false
slug: "org-mode-prezentation-beamer"
---

Создание презентаций Beamer в org-mode.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Конфигурационный файл Emacs {#конфигурационный-файл-emacs}

-   Считаем, что экспорт в LaTeX уже настроен (см. [Org-mode. Экспорт в LaTeX]({{< relref "2020-12-14-org-mode-export-latex" >}})).
-   Подключаем библиотеку экспорта:

<!--listend-->

```elisp
(require 'ox-beamer)
```

-   Задаём уровень заголовка, который будет восприниматься как заголовок слайда:
    ```elisp
    (setq org-beamer-frame-level 3)
    ```
    Этот параметр можно переопределить как на уровне файла:
    ```org
    #+OPTIONS: H:3
    ```
    так и на уровне поддерева:
    ```org
    :EXPORT_OPTIONS: H:3
    ```


## <span class="section-num">2</span> Опции экспорта {#опции-экспорта}

Общие опции экспорта:

-   [Org-mode. Экспорт]({{< relref "2020-12-10-org-mode-export" >}})
-   [Org-mode. Экспорт в LaTeX]({{< relref "2020-12-14-org-mode-export-latex" >}})

<a id="table--Опции экспорта для файла и поддерева"></a>

| Опции экспорта файла | Опции экспорта поддерева  |
|----------------------|---------------------------|
| BEAMER_THEME         | EXPORT_BEAMER_THEME       |
| BEAMER_COLOR_THEME   | EXPORT_BEAMER_COLOR_THEME |
| BEAMER_FONT_THEME    | EXPORT_BEAMER_FONT_THEME  |
| BEAMER_INNER_THEME   | EXPORT_BEAMER_INNER_THEME |
| BEAMER_OUTER_THEME   | EXPORT_BEAMER_OUTER_THEME |
| BEAMER_HEADER        |                           |


## <span class="section-num">3</span> Явный разрыв слайда {#явный-разрыв-слайда}

-   Если текст не умещается на одном слайде, его нужно разбить. Для этого необходимо установить параметр `allowframebreaks` для конкретного слайда:
    ```org
    ** A very long "frame" with breaks
    :PROPERTIES:
    :BEAMER_OPT: allowframebreaks,label=
    :END:
    ```
-   Чтобы добавить явный разрыв страницы:
    ```org
    #+beamer: \framebreak
    ```
-   Можно установить глобально для всех слайдов:
    ```org
    #+BIND: org-beamer-frame-default-options "allowframebreaks"
    ```


## <span class="section-num">4</span> Таблицы {#таблицы}


### <span class="section-num">4.1</span> Управление шириной таблицы {#управление-шириной-таблицы}

Можно задать атрибуты для таблицы:

```org
#+ATTR_LATEX: :align lp{0.4\linewidth}l
```


## <span class="section-num">5</span> Иллюстрации {#иллюстрации}

-   При подготовке иллюстраций можно передать параметры \\(\LaTeX\\):
    ```org
    #+attr_latex: :width 0.8\linewidth
    [[file:../media/image.png]]
    ```
    В результате получим:
