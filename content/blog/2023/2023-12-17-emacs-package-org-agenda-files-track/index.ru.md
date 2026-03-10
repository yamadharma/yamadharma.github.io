---
title: "Emacs. Пакет org-agenda-files-track"
author: ["Dmitry S. Kulyabov"]
date: 2023-12-17T19:57:00+03:00
lastmod: 2024-01-01T20:41:00+03:00
tags: ["emacs", "org-mode"]
categories: ["computer-science"]
draft: false
slug: "emacs-package-org-agenda-files-track"
---

Пакет для динамической генерации списка файлов для агенды.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/nicolas-graves/org-agenda-files-track>
-   Состоит из двух библиотек:
    -   `org-agenda-files-track`: использует вызовы `org-mode`;
    -   `org-agenda-files-track-ql`: с поддержкой `org-ql` (см. [Emacs. Пакет org-ql]({{< relref "2023-12-17-emacs-package-org-ql" >}})).


## <span class="section-num">2</span> Подключение {#подключение}


### <span class="section-num">2.1</span> org-agenda-files-track {#org-agenda-files-track}

-   Подключается пакет следующим образом:
    ```emacs-lisp
    ;;; Toggle org-agenda-files-track mode on
    (setq org-agenda-files-track-mode t)
    ;;; Load package
    (require 'org-agenda-files-track)
    (add-hook 'org-mode-hook #'org-agenda-files-track-mode)
    ```


### <span class="section-num">2.2</span> org-agenda-files-track-ql {#org-agenda-files-track-ql}

-   Подключается пакет следующим образом:
    ```emacs-lisp
    ;;; Toggle org-agenda-files-track mode on
    (setq org-agenda-files-track-ql-mode t)
    ;;; Load package
    (require 'org-agenda-files-track-ql)
    (add-hook 'org-mode-hook #'org-agenda-files-track-ql-mode)
    ```
