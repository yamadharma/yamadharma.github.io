---
title: "Emacs. Работа с библиографией. helm-bibtex"
author: ["Dmitry S. Kulyabov"]
date: 2022-08-30T12:21:00+03:00
lastmod: 2023-07-10T14:31:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-bibliography-helm-bibtex"
---

Пакет для работы с библиографией _helm-bibtex_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Бэкендом является `bibtex-completion`.
-   Фронтенды: `helm-bibtex` и `ivy-bibtex`.
-   Репозиторий: <https://github.com/tmalsburg/helm-bibtex>.


## <span class="section-num">2</span> Форматы цитирования {#форматы-цитирования}


### <span class="section-num">2.1</span> Форматы цитирования по умолчанию {#форматы-цитирования-по-умолчанию}

-   Bibtex-completion создает цитаты на основе основного режима, в котором цитата вставляется.
-   По умолчанию вставляются следующие типы ссылок:
    -   org-mode: ссылка для открытия записи в Ebib;
    -   latex-mode: команда цитирования LaTeX;
    -   markdown-mode: команда цитирования Pandoc;
    -   python-mode: команда цитирования sphinxcontrib-bibtex;
    -   rst-mode: команда цитирования sphinxcontrib-bibtex;
    -   другие режимы: вставка ключа BibTeX.


### <span class="section-num">2.2</span> Изменение формата цитирования {#изменение-формата-цитирования}

-   При использовании org-cite (см. [Emacs. Работа с библиографией. Org-cite]({{< relref "2022-10-10-emacs-bibliography-org-cite" >}})) можно переключиться на соответствующий формат цитирования для org-файлов:
    ```emacs-lisp
    (add-to-list 'bibtex-completion-format-citation-functions
                 '(org-mode . bibtex-completion-format-citation-org-cite))
    ```


## <span class="section-num">3</span> Основные операции {#основные-операции}

-   Пакет позволяет вставлять ссылки в файл.
-   При выборе пункта библиографии есть возможность:
    -   перейти по URL-адресу;
    -   открыть PDF-файл;
    -   вставить запись в качестве цитаты;
    -   вставить запись BibTeX.
-   Вставляет команды цитирования LaTeX, ссылки Ebib или ссылки Pandoc, записи BibTeX или ссылки в виде простого текста в точку, прикрепляйте PDF-файлы к электронным письмам.
-   Поддержка ведения заметок.
-   Быстрый доступ к онлайн-библиографическим базам данных, таким как Pubmed, arXiv, Google Scholar, Библиотека Конгресса и т. д.
-   Импортируйте записи BibTeX из CrossRef и других источников.


## <span class="section-num">4</span> Настройка {#настройка}


### <span class="section-num">4.1</span> Поля, используемые для поиска {#поля-используемые-для-поиска}

-   Поля по умолчанию, используемые для поиска: author, title, year, BibTeX key, entry type.
-   Переменная `bibtex-completion-addition-search-fields` может использоваться для расширения этого списка.
-   Добавим ключевые слова к списку поиска:
    ```emacs-lisp
    (setq bibtex-completion-additional-search-fields '(keywords))
    ```


### <span class="section-num">4.2</span> Настройка результатов поиска {#настройка-результатов-поиска}

-   Настройка представления результатов поиска делается в переменной `bibtex-completion-display-formats`.
-   По умолчанию она имеет вид:
    ```emacs-lisp
    '((t . "${author:36} ${title:*} ${year:4} ${=has-pdf=:1}${=has-note=:1} ${=type=:7}"))
    ```
-   Числа указывают, сколько символов зарезервировано для соответствующего поля.
-   Символ `*` означает, что это поле занимает всё оставшееся место.
-   Можно задать разный формат вывода для разных типов записей:
    ```emacs-lisp
    (setq bibtex-completion-display-formats
          '((article	. "${=has-pdf=:1}${=has-note=:1} ${=type=:7} ${year:4} ${author:36} ${title:*} ${journal:40}")
            (inbook		. "${=has-pdf=:1}${=has-note=:1} ${=type=:7} ${year:4} ${author:36} ${title:*} Chapter ${chapter:32}")
            (incollection	. "${=has-pdf=:1}${=has-note=:1} ${=type=:7} ${year:4} ${author:36} ${title:*} ${booktitle:40}")
            (inproceedings	. "${=has-pdf=:1}${=has-note=:1} ${=type=:7} ${year:4} ${author:36} ${title:*} ${booktitle:40}")
            (book 		. "${=has-pdf=:1}${=has-note=:1} ${=type=:7} ${year:4} ${author:36} ${title:*} ${subtitle:40} ${volume:2}")
            (t		. "${=has-pdf=:1}${=has-note=:1} ${=type=:7} ${year:4} ${author:36} ${title:*}")))
    ```
-   Чтобы это работало, необходимо добавить `journal` и `booktitle` к `bibtex-completion-additional-search-fields`:
    ```emacs-lisp
    (add-to-list 'bibtex-completion-additional-search-fields 'journal)
    (add-to-list 'bibtex-completion-additional-search-fields 'booktitle)
    (add-to-list 'bibtex-completion-additional-search-fields 'subtitle)
    (add-to-list 'bibtex-completion-additional-search-fields 'chapter)
    (add-to-list 'bibtex-completion-additional-search-fields 'volume)
    ```


## <span class="section-num">5</span> Использование {#использование}


### <span class="section-num">5.1</span> Клавиши для поиска {#клавиши-для-поиска}

-   Будем считать, что общий префикс _Helm_ --- `C-c h` (см. [Emacs. Автодополнение. Helm]({{< relref "2022-12-14-emacs-completion-helm" >}})).
-   `C-c h b`: поиск в центральной и в локальной базах bib.
-   `C-c h B`: поиск в локальной базе bib.
-   `C-c h n`: поиска только среди записей, содержащих примечания.
-   Настройка проводится следующим образом:
    ```emacs-lisp
    (define-key helm-command-map "b" 'helm-bibtex)
    (define-key helm-command-map "B" 'helm-bibtex-with-local-bibliography)
    (define-key helm-command-map "n" 'helm-bibtex-with-notes)
    ```


### <span class="section-num">5.2</span> Выбор действия {#выбор-действия}

-   Выделив пункт, необходимо нажать `C-z`.
-   Будет выдан список действий.
-   Первым действием в списке будет действие по умолчанию.
-   При нажатии `<return>` или `<tab>` на записи будет выполнено действие по умолчанию.


### <span class="section-num">5.3</span> Изменить доступные действия {#изменить-доступные-действия}

-   Нажатие `<enter>` на публикации запускает _действие по умолчанию_, которое открывает PDF-файл, связанный с публикацией, если она присутствует, или ее URL-адрес или DOI в противном случае.
-   Нажатие `<tab>` в helm-bibtex или `M-o` в ivy-bibtex вместо этого отображает меню действий со списком доступных действий.
-   Список всех доступных действий вместе с их функциями (это общие функции действий, для `helm-bibtex` имена функций начинаются с `helm-bibtex-` вместо `bibtex-completion-`, а для `ivy-bibtex` они начинаются с `ivy-bibtex-`):
    -   Open PDF, URL or DOI: `bibtex-completion-open-any`
    -   Open PDF file (if present): `bibtex-completion-open-pdf`
    -   Open URL or DOI in browser: `bibtex-completion-open-url-or-doi`
    -   Insert citation: `bibtex-completion-insert-citation`
    -   Insert reference: `bibtex-completion-insert-reference`
    -   Insert BibTeX key: `bibtex-completion-insert-key`
    -   Insert BibTeX entry: `bibtex-completion-insert-bibtex`
    -   Attach PDF to email: `bibtex-completion-add-PDF-attachment`
    -   Edit notes: `bibtex-completion-edit-notes`
    -   Show entry: `bibtex-completion-show-entry`
    -   Add PDF to library: `bibtex-completion-add-pdf-to-library`


#### <span class="section-num">5.3.1</span> Helm-bibtex {#helm-bibtex}

-   Список действий можно изменить с помощью команд `helm-add-action-to-source` и `helm-delete-action-from-source`.
-   Добавим новое действие `helm-bibtex-open-annotated-pdf` сразу после первого элемента в списке:
    ```emacs-lisp
    (helm-add-action-to-source
     "Open annotated PDF (if present)" 'helm-bibtex-open-annotated-pdf
     helm-source-bibtex 1)
    ```
-   Если последний числовой аргумент в `helm-add-action-to-source` опущен, новое действие добавляется в конец списка.
-   Поскольку действие по умолчанию --- это просто первая запись в списке действий, действие по умолчанию можно изменить, удалив действие и повторно вставив его вверху списка.
-   Сделаем _Вставить ключ BibTeX_ действием по умолчанию:
    ```emacs-lisp
    (helm-delete-action-from-source "Insert BibTeX key" helm-source-bibtex)
    (helm-add-action-to-source "Insert BibTeX key" 'helm-bibtex-insert-key helm-source-bibtex 0)
    ```


#### <span class="section-num">5.3.2</span> Ivy-bibtex {#ivy-bibtex}

-   Действие по умолчанию и дополнительные доступные действия задаются отдельно.
-   Действие по умолчанию управляется переменными `ivy-bibtex-default-action` и `ivy-bibtex-default-multi-action`, причем последние предназначены для списков отмеченных записей.
-   Изменим действие по умолчанию на _Вставить ключ BibTeX_:
    ```emacs-lisp
    (setq ivy-bibtex-default-action 'ivy-bibtex-insert-key)
    ```
-   Установим действие по умолчанию для списков отмеченных записей на _Вставить ключ BibTeX_:
    ```emacs-lisp
    (setq ivy-bibtex-default-multi-action 'ivy-bibtex-insert-key)
    ```
-   Дополнительные действия задаются передачей в команду нужного списка действий `ivy-set-actions`.
-   Сохраним только два доступных действия в дополнение к одному по умолчанию:
    ```emacs-lisp
    (ivy-set-actions
     'ivy-bibtex
     '(("p" ivy-bibtex-open-any "Open PDF, URL, or DOI" ivy-bibtex-open-any)
       ("e" ivy-bibtex-edit-notes "Edit notes" ivy-bibtex-edit-notes)))
    ```
-   Буквы `p` и `e` являются привязками клавиш для двух действий в меню действий.
-   Привязка клавиши `o` зарезервирована для действия по умолчанию.
-   Если вы хотите добавить новые действия только в конец списка действий, вы также можете использовать команду `ivy-add-actions`.
-   Добавим новое действие `ivy-bibtex-open-annotated-pdf` в конец списка действий:
    ```emacs-lisp
    (ivy-add-actions
       'ivy-bibtex
       '(("P" ivy-bibtex-open-annotated-pdf "Open annotated PDF (if present)" ivy-bibtex-open-annotated-pdf)))
    ```


### <span class="section-num">5.4</span> Выбор нескольких записей {#выбор-нескольких-записей}


#### <span class="section-num">5.4.1</span> Helm-bibtex {#helm-bibtex}

-   Запустите helm-bibtex.
-   Введите поисковое выражение.
-   Переместите курсор на соответствующую запись и введите `C-<space>`, чтобы отметить эту запись.
-   При желании измените свое поисковое выражение, отметьте другие записи.
-   Нажмите `<return>` или `<tab>`, чтобы выполнить действие для всех выбранных записей одновременно и выйти из helm-bibtex.


#### <span class="section-num">5.4.2</span> Ivy-bibtex {#ivy-bibtex}

-   Запустите ivy-bibtex.
-   Введите поисковое выражение.
-   Переместите курсор на соответствующую запись и введите `C-<space>`, чтобы отметить эту запись.
-   При желании измените свое поисковое выражение, отметьте больше записей.
-   Нажмите `<return>` чтобы выполнить действие по умолчанию со всеми выбранными записями или `M-o` чтобы выбрать другое действие.
-   Нажмите `S-<space>`, чтобы снять пометку с отмеченной записи.
