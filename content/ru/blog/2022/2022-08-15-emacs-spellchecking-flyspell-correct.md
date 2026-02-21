---
title: "Emacs. Проверка правописания. flyspell-correct"
author: ["Dmitry S. Kulyabov"]
date: 2022-08-15T13:43:00+03:00
lastmod: 2023-07-16T17:21:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-spellchecking-flyspell-correct"
---

Оптимизация исправления слов с помощью flyspell.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/d12frosted/flyspell-correct>.


## <span class="section-num">2</span> Прагматика {#прагматика}

-   Для исправления слов с стандартном интерфейсе _flyspell_ используется мышка.
-   Данный пакет позволяет использовать клавиатурные сочетания в связке с разными пакетами завершения (см. [Emacs. Completion systems]({{< relref "2022-08-15-emacs-completion-systems" >}})).


## <span class="section-num">3</span> Функциональность {#функциональность}

-   Основные функций для запуска процесса коррекции:
    -   `flyspell-correct-wrapper`:
        -   по умолчанию переходит к первому слову с ошибкой перед курсором, предлагает исправить его, возвращает курсор назад.
        -   Вызов с помощью `C-u` даёт возможность исправить несколько слов с ошибками за один прогон.
        -   `C-u C-u` меняет направление.
        -   `C-u C-u C-u` меняет направление и позволяет выполнять несколько исправлений.
        -   В большинстве случаев `flyspell-correct-wrapper` является наиболее удобным вариантом.

    -   `flyspell-correct-at-point`: исправляет слово под курсором.
    -   `flyspell-correct-previous`: исправляет слово перед курсором.
    -   `flyspell-correct-next`: исправляет слово после курсора.
-   Большинство интерфейсов также позволяют сохранить новое слово в словаре, принять это написание в текущем буфере или для всего сеанса или даже пропустить это слово.
-   `flyspell-correct` поставляется с интерфейсом по умолчанию, который использует `completing-read`.
-   Можно использовать другие фреймворки завершения: Ivy, Helm, Ido.
-   Для вызова предлагается использовать сочетание клавиш `C-;`.


## <span class="section-num">4</span> Подключение {#подключение}


### <span class="section-num">4.1</span> Интерфейс `completing-read` {#интерфейс-completing-read}

-   Используется по умолчанию.
-   Подключение:
    ```emacs-lisp
    (require 'flyspell-correct)
    (define-key flyspell-mode-map (kbd "C-;") 'flyspell-correct-wrapper)
    ```


### <span class="section-num">4.2</span> Интерфейс `helm` {#интерфейс-helm}

-   Использует фреймворк _Helm_.
-   Подключение:

<!--listend-->

```emacs-lisp
(require 'flyspell-correct)
(require 'flyspell-correct-helm)
(define-key flyspell-mode-map (kbd "C-;") 'flyspell-correct-wrapper)
```


### <span class="section-num">4.3</span> Интерфейс `ivy` {#интерфейс-ivy}

-   Использует фреймворк _Ivy_.
-   Подключение:

<!--listend-->

```emacs-lisp
(require 'flyspell-correct)
(require 'flyspell-correct-ivy)
(define-key flyspell-mode-map (kbd "C-;") 'flyspell-correct-wrapper)
```


### <span class="section-num">4.4</span> Интерфейс `ido` {#интерфейс-ido}

-   Использует фреймворк _Ido_.
-   Подключение:

<!--listend-->

```emacs-lisp
(require 'flyspell-correct)
(require 'flyspell-correct-ido)
(define-key flyspell-mode-map (kbd "C-;") 'flyspell-correct-wrapper)
```
