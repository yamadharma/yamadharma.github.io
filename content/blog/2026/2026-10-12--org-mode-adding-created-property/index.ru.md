---
title: "Org-mode. Добавление свойства CREATED"
author: ["Dmitry S. Kulyabov"]
date: 2026-10-12T11:11:00+03:00
lastmod: 2026-10-12T12:03:00+03:00
tags: ["org-mode"]
categories: ["computer-science"]
draft: false
slug: "org-mode-adding-created-property"
---

Org-mode. Добавление свойства CREATED

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Мы хотим автоматически фиксировать время создания пункта в Org-mode.
-   Будем добавлять свойство `CREATED`.


## <span class="section-num">2</span> Использование `org-capture` {#использование-org-capture}

-   При создании задачи через `org-capture` можно добавить временную метку прямо в шаблон захвата.
-   В шаблоне используйте специальные escape-последовательности:
    -   `%U` : вставит активную временную метку (например, `<2026-10-12 Mon>`).
    -   `%T` : вставит метку с датой и временем.
    -   `%t` : вставит только дату.

-   Пример шаблона:
    ```elisp
    (setq org-capture-templates
          '(("t" "Task" entry (file+headline "inbox.org" "Tasks")
             "* TODO %^{Задача}\n  CREATED: %U\n  %?")))
    ```

-   При создании задачи в свойство `CREATED` автоматически запишется текущая дата и время.


## <span class="section-num">3</span> Автоматизация для ручного ввода {#автоматизация-для-ручного-ввода}

-   Можно добавлять время создания при генерации заголовка вручную (`M-S-RET`).
-   Удобно использовать встроенный модуль `org-expiry` из `org-contrib`.
-   Он позволяет автоматически добавлять свойство `CREATED` при создании нового заголовка:
    ```elisp
    (require 'org-expiry)

    (setopt
      org-expiry-created-property-name "CREATED" ; Name of property when an item is created
      org-expiry-inactive-timestamps   t         ; Don't have everything in the agenda view
    )

    (defun ecf/insert-created-timestamp()
      "Insert a CREATED property using org-expiry.el for TODO entries"
      ;; Org-journal по-своему интерпретирует CREATED
      (unless (derived-mode-p 'org-journal-mode)
        (org-expiry-insert-created)
        (org-back-to-heading)
        (org-end-of-line)
        ;; (insert " ")
        ))

    ;;;; Whenever a TODO entry is created, I want a timestamp
    ;;;; Advice org-insert-todo-heading to insert a created timestamp using org-expiry

    (defadvice org-insert-todo-heading (after ecf/created-timestamp-advice activate)
      "Insert a CREATED property using org-expiry.el for TODO entries"
      (ecf/insert-created-timestamp)
    )

    ;;;; Make it active
    (ad-activate 'org-insert-todo-heading)

    (require 'org-capture)

    (defadvice org-capture (after ecf/created-timestamp-advice activate)
      "Insert a CREATED property using org-expiry.el for TODO entries"
      ;; Test if the captured entry is a TODO, if so insert the created
      ;; timestamp property, otherwise ignore
      (when (member (org-get-todo-state) org-todo-keywords-1)
        (ecf/insert-created-timestamp)))
    (ad-activate 'org-capture)

    ;;;; Add feature to allow easy adding of tags in a capture window
    (defun ecf/add-tags-in-capture()
      (interactive)
      "Insert tags in a capture window without losing the point"
      (save-excursion
        (org-back-to-heading)
        (org-set-tags)))
    ;;;; Bind this to a reasonable key
    (define-key org-capture-mode-map "\C-c\C-t" 'ecf/add-tags-in-capture)
    ```


## <span class="section-num">4</span> Интерактивная команда {#интерактивная-команда}

-   Можно сделать интерактивную команду и повесить её на клавиатурное сочетание.
-   Вызывать её только тогда, когда нужно.
-   Функция вставляет свойство `CREATED` с текущей датой и временем в текущий заголовок и привязывается к клавише.
    ```emacs-lisp
    (defun ecf/org-set-created (&optional force)
      "Set CREATED property in current Org heading.
    With prefix argument FORCE (C-u), overwrite existing value."
      (interactive "P")
      (org-back-to-heading)
      (let ((existing (org-entry-get nil "CREATED")))
        (if (and existing (not force))
            (message "CREATED already set: %s (C-u to overwrite)" existing)
          (org-set-property "CREATED"
                            (format-time-string "[%Y-%m-%d %a %H:%M]"))
          (message "CREATED set"))))

    (with-eval-after-load 'org
      (define-key org-mode-map (kbd "C-c C-.") #'ecf/org-set-created))
    ```
-   `[%Y-%m-%d %a %H:%M]` --- неактивная метка (в квадратных скобках), не попадает в Agenda.
-   `org-set-property` сам создаст блок `:PROPERTIES:`, если его нет.
