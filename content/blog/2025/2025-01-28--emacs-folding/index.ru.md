---
title: "Emacs. Сворачивание (folding)"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-28T11:18:00+03:00
lastmod: 2025-01-28T12:14:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-folding"
---

Emacs. Сворачивание (folding).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Outline {#outline}

-   Моды на основе `outline-mode`.
-   Пытается реализовать аутлайнер, подобный _org-mode_, но для других мод.


### <span class="section-num">1.1</span> Outline-mode {#outline-mode}

-   Входит в состав Emacs.
-   [Emacs. Пакет outline-mode]({{< relref "2025-01-28--emacs-outline-mode" >}})


### <span class="section-num">1.2</span> outli {#outli}

-   Аутлайнинг на базе комментариев.
-   [Emacs. Пакет outli]({{< relref "2025-01-28--emacs-outli" >}})


## <span class="section-num">2</span> Другие пакеты {#другие-пакеты}


### <span class="section-num">2.1</span> yafolding {#yafolding}

-   Репозиторий: <https://github.com/zenozeng/yafolding.el>
-   Не поддерживается.


### <span class="section-num">2.2</span> origami {#origami}

-   Репозиторий: <https://github.com/gregsexton/origami.el>
-   Может работать подобно `folding.el`:
    ```emacs-lisp
    ;; -*- origami-fold-style: triple-braces -*-
    ```


### <span class="section-num">2.3</span> folding.el {#folding-dot-el}

-   Репозиторий: <https://www.emacswiki.org/emacs/folding.el>
-   Использует маркеры в буфере для управления видимостью текста.


### <span class="section-num">2.4</span> hideshow {#hideshow}


### <span class="section-num">2.5</span> ts-fold {#ts-fold}

-   Репозитрий: <https://github.com/emacs-tree-sitter/ts-fold>
-   Основан на tree-sitter.
