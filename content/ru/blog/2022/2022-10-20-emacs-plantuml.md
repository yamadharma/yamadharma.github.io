---
title: "Emacs. Plantuml"
author: ["Dmitry S. Kulyabov"]
date: 2022-10-20T13:07:00+03:00
lastmod: 2023-07-08T16:29:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-plantuml"
---

Поддержка Plantuml (см. [Диаграммы. PlantUML]({{< relref "2022-02-01-diagrams-plantuml" >}})) в Emacs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Поддержка кодового блока Babel {#поддержка-кодового-блока-babel}

-   Пакет `ob-plantuml.el` входит в поставку _org-mode_.
-   Подключение пакета:
    ```emacs-lisp
    (require 'ob-plantuml)
    ```
-   Нужно установить вариант запуска plantuml, например:
    ```emacs-lisp
    (setq org-plantuml-exec-mode 'plantuml)
    ```
-   Варианты следующие:
    -   `jar` : использование jar-архива (установка по умолчанию).
        -   Необходимо ещё установить расположение этого файла в переменной `org-plantuml-jar-path`.
    -   `plantuml` : использование исполняемого файла (по умолчанию `plantuml`).
        -   Исполняемый файл задаётся переменной `org-plantuml-executable-path`.


## <span class="section-num">2</span> Поддержка редактирования кода Plantuml {#поддержка-редактирования-кода-plantuml}

-   Пакет `plantuml-mode`.
-   Репозиторий: <https://github.com/skuro/plantuml-mode>.


### <span class="section-num">2.1</span> Режимы выполнения {#режимы-выполнения}

-   `jar` : (режим по умолчанию) запуск PlantUML с помощью локального jar-файла.
-   `server` : использует `plantuml-server` для отображения предварительного просмотра.
-   `executable` : запуск PlantUML как локального исполняемого файла.


### <span class="section-num">2.2</span> Настройка {#настройка}

-   Пример настройки:
    -   режим `jar`:
        ```emacs-lisp
        ;; Sample jar configuration
        (setq plantuml-jar-path "/path/to/your/copy/of/plantuml.jar")
        (setq plantuml-default-exec-mode 'jar)
        ```
    -   режим `executable`:
        ```emacs-lisp
        ;; Sample executable configuration
        (setq plantuml-executable-path "/path/to/your/copy/of/plantuml.bin")
        (setq plantuml-default-exec-mode 'executable)
        ```
-   Можно  включить `plantuml-mode` для файлов с расширением `plantuml`:
    ```emacs-lisp
    ;; Enable plantuml-mode for PlantUML files
    (add-to-list 'auto-mode-alist '("\\.plantuml\\'" . plantuml-mode))
    ```


### <span class="section-num">2.3</span> Комбинации клавиш {#комбинации-клавиш}

-   `C-c C-c` : предварительный просмотр диаграмм с помощью (`plantuml-preview`).
-   `C-u C-c C-c` : предварительный просмотр в другом окне.
-   `C-u C-u C-c C-c` : предварительный просмотр в другом фрейме.
