---
title: "Emacs. Управление пакетами"
author: ["Dmitry S. Kulyabov"]
date: 2023-12-18T16:19:00+03:00
lastmod: 2025-01-25T15:03:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-package-management"
---

Управление пакетами в Emacs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Репозитории пакетов {#репозитории-пакетов}


### <span class="section-num">1.1</span> ELPA {#elpa}

-   Сайт: <https://elpa.gnu.org/packages/>
-   Содержит пакеты Emacs, одобренные FSF.


### <span class="section-num">1.2</span> NonGNU ELPA {#nongnu-elpa}

-   Сайт: <https://elpa.nongnu.org/nongnu/>


### <span class="section-num">1.3</span> NonGNU-devel ELPA {#nongnu-devel-elpa}

-   Сайт: <https://elpa.nongnu.org/nongnu-devel/>


### <span class="section-num">1.4</span> MELPA {#melpa}

-   Сайт: <https://melpa.org/>
-   Нет передачи авторских прав.
-   Не нужно размещать свой пакет в git-репозитории ELPA.


### <span class="section-num">1.5</span> Настройка источников пакетов {#настройка-источников-пакетов}

-   Настройка источников пакетов:
    ```emacs-lisp
    (let* ((no-ssl (and (memq system-type '(windows-nt ms-dos))
                            (not (gnutls-available-p))))
               (proto (if no-ssl "http" "https")))
      ;;; Comment/uncomment these two lines to enable/disable MELPA and MELPA Stable as desired
      (add-to-list 'package-archives (cons "melpa" (concat proto "://melpa.org/packages/")) t)
      ;; (add-to-list 'package-archives (cons "melpa-stable" (concat proto "://stable.melpa.org/packages/")) t)
      ;;; Marmalade doesn't work
      ;; (add-to-list 'package-archives '("marmalade" . "http://marmalade-repo.org/packages/") t)
      ;; (add-to-list 'package-archives '("org" . "http://orgmode.org/elpa/") t)
      ;; (add-to-list 'package-archives '("gnu" . (concat proto "://elpa.gnu.org/packages/")) t)
      (when (< emacs-major-version 24)
            ;;; For important compatibility libraries like cl-lib
            (add-to-list 'package-archives '("gnu" . (concat proto "://elpa.gnu.org/packages/")))))
    ```


## <span class="section-num">2</span> Средства управления пакетами {#средства-управления-пакетами}


### <span class="section-num">2.1</span> package {#package}

-   Встроенный пакет Emacs для управления пакетами.
-   [Emacs. Управление пакетами. package]({{< relref "2025-01-25--emacs-package-management-package" >}})


### <span class="section-num">2.2</span> quelpa {#quelpa}

-   Репозиторий: <https://github.com/quelpa/quelpa>
-   Позволяет использовать внешние источники с _package_.


### <span class="section-num">2.3</span> straight {#straight}

-   Репозиторий: <https://github.com/radian-software/straight.el>


### <span class="section-num">2.4</span> Cask {#cask}

-   Репозиторий: <https://github.com/cask/cask>
-   Обёртка для _package_.
