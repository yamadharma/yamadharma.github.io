---
title: "Emacs. Проверка правописания. ispell"
author: ["Dmitry S. Kulyabov"]
date: 2022-08-01T17:31:00+03:00
lastmod: 2023-07-12T18:14:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-spellchecking-ispell"
---

Проверка правописания в Emacs. Ispell.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


## <span class="section-num">2</span> Бекэнд {#бекэнд}


### <span class="section-num">2.1</span> aspell {#aspell}


### <span class="section-num">2.2</span> hunspell {#hunspell}

-   Проверка установленных словарей:
    ```shell
    hunspell -D
    ```
-   Сконфигурируем словари:
    ```emacs-lisp
    with-eval-after-load "ispell"
      ;; Configure `LANG`, otherwise ispell.el cannot find a 'default
      ;; dictionary' even though multiple dictionaries will be configured
      ;; in next line.
      (setenv "LANG" "ru_RU.UTF-8")
      (setq ispell-program-name "hunspell")
      ;; Configure English + Russian.
      (setq ispell-dictionary "en_US,ru_RU")
      ;; ispell-set-spellchecker-params has to be called
      ;; before ispell-hunspell-add-multi-dic will work
      (ispell-set-spellchecker-params)
      (ispell-hunspell-add-multi-dic "en_US,ru_RU")
      ;; For saving words to the personal dictionary, don't infer it from
      ;; the locale, otherwise it would save to ~/.hunspell_de_DE.
      (setq ispell-personal-dictionary "~/.local/hunspell_personal"))

    ;; The personal dictionary file has to exist, otherwise hunspell will
    ;; silently not use it.
    (unless (file-exists-p ispell-personal-dictionary)
      (write-region "" nil ispell-personal-dictionary nil 0))
    ```
