---
title: "Виды комментариев в Emacs Lisp"
author: ["Dmitry S. Kulyabov"]
date: 2022-07-12T18:45:00+03:00
lastmod: 2023-07-08T16:15:00+03:00
tags: ["emacs", "programming"]
categories: ["computer-science"]
draft: false
slug: "emacs-lisp-comments"
---

Виды комментариев в Emacs Lisp.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Есть три типа комментариев:
    -   `;` комментарии в одной строке с кодом;
    -   `;;` комментарии, которые не находятся на одной строке с кодом;
    -   `;;;` Комментарий, используемый в качестве заголовков.
-   Пример использования всех типов комментариев:
    ```emacs-lisp
    ;;; My heading
    ;; A function that greets people
    (defun greet (&optional name)
      "My function"
      (message
       (concat "Hello "
               (if name ; check if nil
                   name
                 "World"))))

    (greet)
    ;; This prints Hello World

    (greet "Gene")
    ;; This prints Hello Gene
    ```
-   Команда `M-;` (`comment-dwim`) автоматически создаёт комментарий соответствующего типа или смещает существующий комментарий в нужное место, в зависимости от количества точек с запятой.

-   Литература
    -   <https://www.gnu.org/software/emacs/manual/html_node/elisp/Comment-Tips.html>;
    -   <https://www.gnu.org/software/emacs/manual/html_node/elisp/Comments.html>.


## <span class="section-num">2</span> Соглашения для комментариев {#соглашения-для-комментариев}


### <span class="section-num">2.1</span> `;` {#09a0a0}

-   Комментарии, начинающиеся с одной точки с запятой `;`, должны быть выровнены по одному и тому же столбцу справа от исходного кода.
-   Такие комментарии обычно объясняют, как код в этой строке выполняет свою работу:
    ```emacs-lisp
    (setq base-version-list                 ; There was a base
          (assoc (substring fn 0 start-vn)  ; version to which
                 file-version-assoc-list))  ; this looks like
                                            ; a subversion.
    ```


### <span class="section-num">2.2</span> `;;` {#189c88}

-   Комментарии, начинающиеся с двух точек с запятой `;;`, должны быть выровнены по тому же уровню отступа, что и код.
-   Такие комментарии обычно описывают назначение следующих строк или состояние программы в этот момент:
    ```emacs-lisp
    (prog1 (setq auto-fill-function
                 …
                 …
      ;; Update mode line.
      (force-mode-line-update)))
    ```
-   Также этот тип комментария используется для комментариев вне функций:
    ```emacs-lisp
    ;; This Lisp code is run in Emacs when it is to operate as
    ;; a server for other processes.
    ```
-   Если у функции нет строки документации, вместо этого она должна иметь комментарий с двумя точками с запятой прямо перед функцией, объясняющий, что делает функция и как ее правильно вызывать.
-   Следует объяснить, что означает каждый аргумент и как функция интерпретирует его возможные значения.


### <span class="section-num">2.3</span> `;;;` {#ec58a0}

-   Комментарии, начинающиеся с трех (или более) точек с запятой `;;;`, должен начинаться с левого края.
-   Используется для комментариев, которые должны считаться заголовком.
-   По умолчанию комментарии, начинающиеся как минимум с трех точек с запятой (за которыми следует один пробел и символ, не являющийся пробелом), считаются заголовками разделов, а комментарии, начинающиеся с двух или менее, --- нет.
-   Три точки с запятой используются для разделов верхнего уровня, четыре для подразделов, пять для подразделов и так далее:
    ```emacs-lisp
    ;;; backquote.el --- implement the ` Lisp construct...
    ;;; Commentary:...
    ;;; Code:...
    ;;; backquote.el ends here
    ```
