---
title: "Emacs. Темы. Ef-themes"
author: ["Dmitry S. Kulyabov"]
date: 2023-06-13T15:38:00+03:00
lastmod: 2023-09-28T16:16:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-themes-ef-themes"
---

Набор тем _ef-themes_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Руководство: <https://protesilaos.com/emacs/ef-themes>
-   Скриншоты: <https://protesilaos.com/emacs/ef-themes-pictures>
-   Репозитории:
    -   SourceHut: <https://git.sr.ht/~protesilaos/ef-themes>
    -   GitHub: <https://github.com/protesilaos/ef-themes>
    -   GitLab: <https://gitlab.com/protesilaos/ef-themes>
-   Автор: Протесилаос Ставру
-   У автора ещё один набор тем: _modus_ (см. [Emacs. Темы. Modus-themes]({{< relref "2023-02-15-emacs-themes-modus-themes" >}}))


## <span class="section-num">2</span> Пример конфигурации {#пример-конфигурации}

-   Общий пример конфигурации:
    ```emacs-lisp
    ;; Make customisations that affect Emacs faces BEFORE loading a theme
    ;; (any change needs a theme re-load to take effect).
    (require 'ef-themes)

    ;; If you like two specific themes and want to switch between them, you
    ;; can specify them in `ef-themes-to-toggle' and then invoke the command
    ;; `ef-themes-toggle'.  All the themes are included in the variable
    ;; `ef-themes-collection'.
    (setq ef-themes-to-toggle '(ef-summer ef-winter))

    (setq ef-themes-headings ; read the manual's entry or the doc string
          '((0 . (variable-pitch light 1.9))
            (1 . (variable-pitch light 1.8))
            (2 . (variable-pitch regular 1.7))
            (3 . (variable-pitch regular 1.6))
            (4 . (variable-pitch regular 1.5))
            (5 . (variable-pitch 1.4)) ; absence of weight means `bold'
            (6 . (variable-pitch 1.3))
            (7 . (variable-pitch 1.2))
            (t . (variable-pitch 1.1))))

    ;; They are nil by default...
    (setq ef-themes-mixed-fonts t
          ef-themes-variable-pitch-ui t)

    ;; Read the doc string or manual for this one.  The symbols can be
    ;; combined in any order.
    (setq ef-themes-region '(intense no-extend neutral))

    ;; Disable all other themes to avoid awkward blending:
    (mapc #'disable-theme custom-enabled-themes)

    ;; Load the theme of choice:
    (load-theme 'ef-summer :no-confirm)

    ;; OR use this to load the theme which also calls `ef-themes-post-load-hook':
    (ef-themes-select 'ef-summer)

    ;; The themes we provide are recorded in the `ef-themes-dark-themes',
    ;; `ef-themes-light-themes'.

    ;; We also provide these commands, but do not assign them to any key:
    ;;
    ;; - `ef-themes-toggle'
    ;; - `ef-themes-select'
    ;; - `ef-themes-select-dark'
    ;; - `ef-themes-select-light'
    ;; - `ef-themes-load-random'
    ;; - `ef-themes-preview-colors'
    ;; - `ef-themes-preview-colors-current'
    ```


## <span class="section-num">3</span> Настройки {#настройки}


### <span class="section-num">3.1</span> Заголовки {#заголовки}

-   Опция `ef-themes-headings` обеспечивает поддержку стилей заголовков для уровней заголовков от 0 до 8.
-   Это список, который принимает значение `(KEY . LIST-OF-VALUES)`.
    -   `KEY`: либо число, представляющее уровень заголовка (от 0 до 8), либо `t`, относящееся к резервному стилю.
    -   Ключи `agenda-date` и `agenda-structure` применяются к Org-mode Agenda.
-   Уровень `0`: заголовок документа или его эквивалент (например, конструкция `#+title`).
-   Уровни 1--8 являются обычными заголовками.
-   По умолчанию (значение `nil`) все заголовки имеют полужирное моноширинное начертание.
-   Свойство `variable-pitch` изменяет семейство шрифтов заголовка на пропорциональный шрифт.
-   Число, выраженное в виде числа с плавающей запятой (например, `1.5`), увеличивает высоту заголовка во столько же раз.
-   Комбинации любого из этих свойств выражаются в виде списка, как в этих примерах:
    ```emacs-lisp
    (semibold)
    (variable-pitch semibold)
    (variable-pitch semibold 1.3)
    (variable-pitch semibold (height 1.3))   ; same as above
    (variable-pitch semibold (height . 1.3)) ; same as above
    ```
-   В конфигурационных файлах:
    ```emacs-lisp
    (setq ef-themes-headings
          '((1 . (light variable-pitch 1.5))
            (2 . (regular 1.3))
            (3 . (1.1))
            (t . (variable-pitch))))
    ```
-   Для оставления исходного стиля, нужно задать значение не `nil`:
    ```emacs-lisp
    (setq ef-themes-headings
          '((1 . t)           ; keep the default style
            (2 . (variable-pitch 1.2))
            (t . (variable-pitch)))) ; style for all unspecified headings

    (setq ef-themes-headings
          '((1 . (variable-pitch 1.6))
            (2 . (1.3))
            (t . t))) ; default style for all unspecified levels
    ```
