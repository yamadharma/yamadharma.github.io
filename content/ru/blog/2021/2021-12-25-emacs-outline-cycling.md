---
title: "Emacs. Режим структуры"
author: ["Dmitry S. Kulyabov"]
date: 2021-12-25T19:48:00+03:00
lastmod: 2023-07-08T16:12:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-outline-cycling"
---

-   При использовании _org-mode_ с помощью клавиш _S-tab_ и _C-tab_ можно сворачивать все разделы (_S-tab_) или конкретный раздел (_C-tab_).
-   Данное поведение желательно расширить на все другие моды.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Пакет _bicycle_ {#пакет-bicycle}


### <span class="section-num">1.1</span> Общая информация {#общая-информация}

-   Пакет предоставляет команды для циклического переключения видимости структуры разделов и блоков кода.
-   Репозиторий: <https://github.com/tarsius/bicycle>


### <span class="section-num">1.2</span> Взаимодействие с другими пакетами {#взаимодействие-с-другими-пакетами}

-   Пакет использует `outline-minor-mode-map`. Большая часть работы выполняется с использованием функций пакета _outline_.
-   Кроме того, для работы с блоками кода используется пакет `hideshow`.
    -   Если включена `hs-minor-mode` и курсор находится в начале блока кода, то вместо функций библиотеки _outline_ используется `hs-toggle-hiding`.
    -   При последующем циклическом изменении видимости раздела, содержащего блоки кода, блоки кода, которые были скрыты с помощью `hs-toggle-hiding`, не расширяются.


### <span class="section-num">1.3</span> Настройка {#настройка}

-   Пакет модифицирует настройки _outline-mode_:
    ```emacs-lisp
    (require 'bicycle)

    (define-key outline-minor-mode-map (kbd "<C-tab>") #'bicycle-cycle)
    (define-key outline-minor-mode-map (kbd "<S-tab>") #'bicycle-cycle-global)
    ```
-   Его можно активировать для разных старших мод:
    ```emacs-lisp
    (add-hook 'prog-mode-hook #'outline-minor-mode)
    (add-hook 'markdown-mode-hook #'outline-minor-mode)
    (add-hook 'TeX-mode-hook #'outline-minor-mode)
    (add-hook 'LaTeX-mode-hook #'outline-minor-mode)
    (add-hook 'rst-mode-hook #'outline-minor-mode)
    ```
