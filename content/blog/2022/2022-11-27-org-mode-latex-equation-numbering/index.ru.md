---
title: "Org-mode. Нумерация уравнений LaTeX"
author: ["Dmitry S. Kulyabov"]
date: 2022-11-27T19:16:00+03:00
lastmod: 2024-01-14T15:22:00+03:00
tags: ["emacs", "org-mode", "tex"]
categories: ["computer-science"]
draft: false
slug: "org-mode-latex-equation-numbering"
---

Org-mode. Нумерация уравнений LaTeX.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сделано на основе: <https://kitchingroup.cheme.cmu.edu/blog/2016/11/07/Better-equation-numbering-in-LaTeX-fragments-in-org-mode/>.


## <span class="section-num">2</span> Проблема {#проблема}

-   При использовании выключенных уравнений _LaTeX_ в _org-mode_ (см. [Org-mode. Предпросмотр TeX]({{< relref "2024-01-06-org-mode-latex-preview" >}})) каждый фрагмент создаётся изолированно.
-   Каждое пронумерованное уравнение имеет номер `(1)`.


## <span class="section-num">3</span> Предлагаемое решение {#предлагаемое-решение}

-   Для обеспечения правильной нумерации нужно создавать каждый фрагмента не изолированно, a учитывая контекст.
-   Выясняем, какой должна быть нумерация для каждого уравнения, а затем передаём эту информацию для генерации изображения.


## <span class="section-num">4</span> Реализация {#реализация}

-   Предлагается добавить следующий фрагмент в конфигурационные файлы:
    ```emacs-lisp
    (defun ecf/org-renumber-environment (orig-func &rest args)
      (let ((results '())
            (counter -1)
            (numberp))

        (setq results (loop for (begin .  env) in
                            (org-element-map (org-element-parse-buffer) 'latex-environment
                              (lambda (env)
                                (cons
                                 (org-element-property :begin env)
                                 (org-element-property :value env))))
                            collect
                            (cond
                             ((and (string-match "\\\\begin{equation}" env)
                                   (not (string-match "\\\\tag{" env)))
                              (incf counter)
                              (cons begin counter))
                             ((string-match "\\\\begin{align}" env)
                              (prog2
                                  (incf counter)
                                  (cons begin counter)
                                (with-temp-buffer
                                  (insert env)
                                  (goto-char (point-min))
                                  ;; \\ is used for a new line. Each one leads to a number
                                  (incf counter (count-matches "\\\\$"))
                                  ;; unless there are nonumbers.
                                  (goto-char (point-min))
                                  (decf counter (count-matches "\\nonumber")))))
                             (t
                              (cons begin nil)))))

        (when (setq numberp (cdr (assoc (point) results)))
          (setf (car args)
                (concat
                 (format "\\setcounter{equation}{%s}\n" numberp)
                 (car args)))))

      (apply orig-func args))

    (advice-add 'org-create-formula-image :around #'ecf/org-renumber-environment)
    ```
