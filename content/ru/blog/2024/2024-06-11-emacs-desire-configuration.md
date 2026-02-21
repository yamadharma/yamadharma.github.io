---
title: "Emacs. Desire. Конфигурация"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-11T18:55:00+03:00
lastmod: 2026-02-20T14:55:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-desire-configuration"
---

Конфигурация для пакета desire.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Каталоги конфигурации {#каталоги-конфигурации}


## <span class="section-num">2</span> Установка переменных {#установка-переменных}


## <span class="section-num">3</span> Конфигурационные файлы {#конфигурационные-файлы}


### <span class="section-num">3.1</span> Верхняя строка {#верхняя-строка}

-   В строке задаём язык программирования, режимы.
    <a id="code-snippet--line-mode"></a>
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ```


### <span class="section-num">3.2</span> Заголовок {#заголовок}

-   В файле `rc.packages.el` находится список используемых пакетов.
-   Заголовок файла:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; rc.packages.el

    ;;; Commentary:

    ;;
    ;;  File id
    ;;
    ;;      Copyright (C)  2002-2025 Dmitry S. Kulyabov
    ;;      Keywords:      rc.packages
    ;;      Author:        Dmitry S. Kulyabov <yamadharma@gmail.com>
    ;;      Maintainer:    Dmitry S. Kulyabov <yamadharma@gmail.com>
    ;;
    ;;      This code is free software in terms of GNU Gen. pub. Lic. v3 or later
    ;;

    ;;;  Description:

    ;;; Change Log:

    ;;; Code:

    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      rc.packages.el
    </div>

-   Файл:

<!--listend-->

```emacs-lisp
;; (desire-conf 'tiny)
(desire-conf 'personal)
;;
;; Mule
;;
(desire-conf 'mule)
;;(desire-conf 'mule-fontset)
;; ----------------------------------------------------------------------
;;
;;{{{ Xemacs

(if (string-match "XEmacs" emacs-version)
    (desired 'xemacs))

;;}}}
```


### <span class="section-num">3.3</span> Управление пакетами {#управление-пакетами}

-   [Emacs. Управление пакетами]({{< relref "2023-12-18-emacs-package-management" >}})

<!--listend-->

```emacs-lisp
;;; Package management
```


#### <span class="section-num">3.3.1</span> Встроенный пакетный менеджер {#встроенный-пакетный-менеджер}

-   [Emacs. Управление пакетами. package]({{< relref "2025-01-25--emacs-package-management-package" >}})

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`

    <!--listend-->

    ```emacs-lisp
    ;;;; Packaging
    (desire 'package)
    ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/package/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Set up the package

        ;;; Code:

        (setopt warning-suppress-log-types '((package reinitialization)))

        (setopt package-enable-at-startup nil
              package-user-dir (concat home-data-path "elpa/")
              package-gnupghome-dir (expand-file-name "gpg" package-user-dir))

        (require 'package)

        ;;;
        ```

<!--list-separator-->

3.  Настройка

    -   Файл: `packages/package/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-

        ;;; Code:

        ;;;
        ```

<!--list-separator-->

4.  Компиляция пакетов

    -   Файл: `packages/package/desire.ecd/native-compile.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Set up the package

        ;;; Code:

        ;;;; Supports ahead-of-time native compilation when installing a package
        (setopt package-native-compile t)

        ;;;
        ```

<!--list-separator-->

5.  Обновлять встроенные пакеты

    -   Файл: `packages/`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Set up the package

        ;;; Code:

        ;;;; Upgrade built-in packages
        (setopt package-install-upgrade-built-in t)

        ;;;
        ```

<!--list-separator-->

6.  Репозитории

    -   Файл: `packages/package/desire.ecd/repos.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Set up repos

        ;;; Code:

        ;;;; Repos
        (let* ((no-ssl (and (memq system-type '(windows-nt ms-dos))
                            (not (gnutls-available-p))))
               (proto (if no-ssl "http://" "https://")))
        ;;;; Comment/uncomment these two lines to enable/disable MELPA and MELPA Stable as desired

          (add-to-list 'package-archives (cons "melpa" (concat proto "melpa.org/packages/")) t)
          (add-to-list 'package-archives (cons "melpa-stable" (concat proto "stable.melpa.org/packages/")) t)
          ;; (add-to-list 'package-archives (cons "org" (concat proto "orgmode.org/elpa/")) t)
          (add-to-list 'package-archives (cons "gnu-devel" (concat proto "elpa.gnu.org/devel/")) t)
          (add-to-list 'package-archives (cons "gnu" (concat proto "elpa.gnu.org/packages/")) t)
          (add-to-list 'package-archives (cons "nongnu" (concat proto "elpa.nongnu.org/nongnu/")) t)

        ;;;; Mirror for some Emacs package archives
        ;; https://github.com/d12frosted/elpa-mirror
          (add-to-list 'package-archives (cons "melpa-github-mirror" "https://raw.githubusercontent.com/d12frosted/elpa-mirror/master/melpa") t)
          (add-to-list 'package-archives (cons "melpa-stable-github-mirror" "https://raw.githubusercontent.com/d12frosted/elpa-mirror/master/stable-melpa") t)
          (add-to-list 'package-archives (cons "gnu-github-mirror" "https://raw.githubusercontent.com/d12frosted/elpa-mirror/master/gnu") t)
          (add-to-list 'package-archives (cons "nongnu-github-mirror" "https://raw.githubusercontent.com/d12frosted/elpa-mirror/master/nongnu") t)

          (add-to-list 'package-archives (cons "melpa-gitlab-mirror" "https://gitlab.com/d12frosted/elpa-mirror/-/tree/master/melpa") t)
          (add-to-list 'package-archives (cons "melpa-stable-gitlab-mirror" "https://gitlab.com/d12frosted/elpa-mirror/-/tree/master/stable-melpa") t)
          (add-to-list 'package-archives (cons "gnu-gitlab-mirror" "https://gitlab.com/d12frosted/elpa-mirror/-/tree/master/gnu") t)
          (add-to-list 'package-archives (cons "nongnu-gitlab-mirror" "https://gitlab.com/d12frosted/elpa-mirror/-/tree/master/nongnu") t)


        ;;;; Marmalade doesn't work
        ;; (add-to-list 'package-archives (cons "marmalade" "http://marmalade-repo.org/packages/") t)

          (when (< emacs-major-version 24)
            ;;; For important compatibility libraries like cl-lib
            (add-to-list 'package-archives (cons "gnu" (concat proto "elpa.gnu.org/packages/")) t)))

        (unless package--initialized
          (package-initialize))

        ;;;; Refreshing the content or the list-packages in case it is empty
        (when (not package-archive-contents)
          (package-refresh-contents))

        ;;;; Dirty hack
        (setopt package-check-signature nil)
        ;;;; Network timeout
        (setopt url-request-timeout 10)  ; 10 секунд

        (desire 'gnu-elpa-keyring-update)

        ;;;
        ```


#### <span class="section-num">3.3.2</span> Пакетный менеджер quelpa {#пакетный-менеджер-quelpa}

-   Необходим для emacs-29 и старше.
-   Начиная с emacs-30 можно использовать `package-vc.`
-   Подключение:
    ```emacs-lisp
    ;;; Build and install your Emacs Lisp packages on-the-fly and directly from source
    ;; (desire 'quelpa)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 2:</span>
      rc.packages.el
    </div>
-   Загружаем:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Build and install your Emacs Lisp packages on-the-fly directly from source
    ;; https://github.com/quelpa/quelpa

    (require 'quelpa)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 3:</span>
      packages/quelpa/loaddefs.ecf
    </div>
-   Асинхронные операции:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Build and install your Emacs Lisp packages on-the-fly directly from source
    ;; https://github.com/quelpa/quelpa

    ;;; If non-nil, quelpa operation will not block Emacs input
    ;; (setopt quelpa-async-p t)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 4:</span>
      packages/quelpa/desire.ecf
    </div>
-   Обновление пакетов:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Build and install your Emacs Lisp packages on-the-fly directly from source
    ;; https://github.com/quelpa/quelpa

    ;;; To run quelpa-upgrade-all at most every 14 days
    ;; (setopt quelpa-upgrade-interval 14)
    ;; (add-hook #'after-init-hook #'quelpa-upgrade-all-maybe)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 5:</span>
      packages/quelpa/personal.ecf
    </div>


#### <span class="section-num">3.3.3</span> Пакетный менеджер straight {#пакетный-менеджер-straight}

```emacs-lisp
;;; A declarative package management system with a command line interface
(desire 'straight)
```


#### <span class="section-num">3.3.4</span> Автообновление пакетов {#автообновление-пакетов}

```emacs-lisp
;;; Auto update packages
(desire 'auto-package-update)

;;;}}}
```


### <span class="section-num">3.4</span> Компиляция файлов {#компиляция-файлов}


#### <span class="section-num">3.4.1</span> compile-angel {#compile-angel}

-   Подключим пакет:
    ```emacs-lisp
    ;;; compile-angel.el
    (desire 'compile-angel)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 6:</span>
      rc.packages.el
    </div>
-   Настроим начальную конфигурацию:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Compile Emacs Lisp libraries automatically.
    ;;; https://github.com/jamescherti/compile-angel.el

    ;; (require 'compile-angel)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 7:</span>
      packages/compile-angel/loaddefs.ecf
    </div>
-   Настроим основные параметры:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Compile Emacs Lisp libraries automatically.
    ;;; https://github.com/jamescherti/compile-angel.el

    ;;; Ensure Emacs loads the most recent byte-compiled files.
    (setopt load-prefer-newer t)

    ;;; Ensure JIT compilation is enabled for improved performance by
    ;;; native-compiling loaded .elc files asynchronously
    (setopt native-comp-jit-compilation t)
    (setopt native-comp-deferred-compilation t) ; Deprecated in Emacs > 29.1

    ;;; Enable/Disable byte compilation and native compilation
    (setopt compile-angel-enable-byte-compile t)
    (setopt compile-angel-enable-native-compile t)

    ;;; Enable verbose (Set it to t while debugging)
    (setopt compile-angel-verbose nil)

    ';; Display the *Compile-Log* buffer (Set it to t while writing elisp)
    (setopt compile-angel-display-buffer nil)

    ;;; Perform byte/native compilation of .el files only once during initial loading
    ;;; (Setting this to nil will try to compile each time an .el file is loaded)
    (setopt compile-angel-on-load-mode-compile-once t)

    ;;; Ignore certain files, for example, for users of the `dir-config` package:
    (setopt compile-angel-excluded-files-regexps '("/\\.dir-config\\.el$"))

    ;;; Function that determines if an .el file should be compiled. It takes one
    ;;; argument (an EL file) and returns t if the file should be compiled,
    ;;; (By default, `compile-angel-predicate-function` is set to nil, which
    ;;; means that the predicate function is not called.)
    (setopt compile-angel-predicate-function
          #'(lambda(el-file)
           ;; Show a message
           (message "PREDICATE: %s" el-file)
           ;; Return t (Compile all)
           t))

    ;; Ensure that quitting only occurs once Emacs finishes native compiling,
    ;; preventing incomplete or leftover compilation files in `/tmp`.
    (setopt native-comp-async-query-on-exit t)
    (setopt confirm-kill-processes t)

    ;;; Show buffer when there is a warning.
    ;;; (NOT RECOMMENDED, except during development).
    ;; (setopt warning-minimum-level :warning)
    ;; (setopt byte-compile-verbose t)
    ;; (setopt byte-compile-warnings t)
    ;; (setopt native-comp-async-report-warnings-errors t)
    ;; (setopt native-comp-warning-on-missing-source t)

    ;;; Non-nil means to natively compile packages as part of their installation.
    (setopt package-native-compile t)

    (add-hook 'emacs-lisp-mode-hook #'compile-angel-on-save-local-mode)

    (compile-angel-on-save-mode)
    (compile-angel-on-load-mode)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 8:</span>
      packages/compile-angel/desire.ecf
    </div>


### <span class="section-num">3.5</span> Системные настройки {#системные-настройки}

```emacs-lisp

;; (desire 'esup)
```


#### <span class="section-num">3.5.1</span> Разные настройки {#разные-настройки}

-   Покидал сюда разные настройки, которые не знаю, куда разместить.
-   Подключение:
    ```emacs-lisp
    (desire-conf 'site-stuff)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 9:</span>
      rc.packages.el
    </div>
-   Подключение:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-

    ;;; Code:
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 10:</span>
      packages/site-stuff.ecf
    </div>
-   Изменение поведения `C-g`:
    ```emacs-lisp
    ;;;; Make C-g a bit more helpful
    ;;;;; https://protesilaos.com/codelog/2024-11-28-basic-emacs-configuration/

    (defun ecf/keyboard-quit-dwim ()
      "Do-What-I-Mean behaviour for a general `keyboard-quit'.

    The generic `keyboard-quit' does not do the expected thing when
    the minibuffer is open.  Whereas we want it to close the
    minibuffer, even without explicitly focusing it.

    The DWIM behaviour of this command is as follows:

    - When the region is active, disable it.
    ​- When a minibuffer is open, but not focused, close the minibuffer.
    ​- When the Completions buffer is selected, close it.
    ​- In every other case use the regular `keyboard-quit'."
      (interactive)
      (cond
       ((region-active-p)
        (keyboard-quit))
       ((derived-mode-p 'completion-list-mode)
        (delete-completion-window))
       ((> (minibuffer-depth) 0)
        (abort-recursive-edit))
       (t
        (keyboard-quit))))

    (define-key global-map (kbd "C-g") #'ecf/keyboard-quit-dwim)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 11:</span>
      packages/site-stuff.ecf
    </div>
-   Оформление интерфейса:
    ```emacs-lisp
    ;;;; Scroll bar mode
    (set-scroll-bar-mode 'left)
    (scroll-bar-mode -1)

    ;;;; Disable the toolbar
    (tool-bar-mode -1)

    ;;;; Menu bar
    (menu-bar-mode 1)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 12:</span>
      packages/site-stuff.ecf
    </div>

<!--listend-->

```emacs-lisp
;;; Automatic decompression, hooks for tar-mode
;;;
;;(require 'jka-compr)
(auto-compression-mode t)

(require 'icomplete) ; Interactive completion in minibuffer.

;; Strip hostname from domain when posting news
                                      ;(setopt gnus-use-generic-from t)

                                      ;(auto-compression-mode t)
;; Time in 24 hour format, plus day and date.
;;
(add-hook 'write-file-hooks 'time-stamp)
                                      ; (require 'mc)


(setopt max-specpdl-size 1000)


;;; Set the fringe a little wider to ensure the text isn’t too close to the window border
;; (fringe-mode 16 . nil)

;; Strip iccc encoding when paste from clipboard
                                      ;(defun fix-rus-letter ()
                                      ;  (interactive)
                                      ;  (goto-char (point-min))
                                      ;  (while (search-forward-regexp ".%/1..koi8-r." nil t)
                                      ;    (replace-match ""))
                                      ;)

;;; Показывает пробелы и табы в конце строк
(setopt show-trailing-whitespace t)

;;; Prevent horizontal window splitting for Emacs 23
;; (setopt split-width-threshold 9999)

(setopt inhibit-startup-message t)

(fset 'yes-or-no-p 'y-or-n-p)

;;; Отключить создание резервных копий
(custom-set-variables '(make-backup-files nil "Отключить создание резервных копий"))

;;; Cursor
(custom-set-variables '(cursor-type 'bar "Внешний вид курсора — вертикальная черта"))
;; Отключить мерцание курсора
(blink-cursor-mode 0)

;;; Highlight Current Line
(global-hl-line-mode 1)

;;; Warnings
;;; Disable report warnings and errors from asynchronous native compilation
(setopt native-comp-async-report-warnings-errors nil)

;;; Not to warn you about anything except problems
;;; :debug | :warning | :error | :emergency
(setopt warning-minimum-level :error)

;;; Don't pop up UI dialogs when prompting
(setopt use-dialog-box nil)

;;; Revert buffers when the underlying file has changed
(global-auto-revert-mode 1)
;;; Revert Dired and other buffers
(setopt global-auto-revert-non-file-buffers t)

;;; Make searches case insensitive
(setopt case-fold-search t)

;;; Tab completion in minibuffer: case insensitive
(setopt completion-ignore-case  t)

;;;
```


#### <span class="section-num">3.5.2</span> Разное {#разное}

```emacs-lisp

;;{{{ Window System

(if (null window-system)
    ()
  (progn
    (desire-conf 'window-system)
                                        ;    (desire-conf  'faces)
                                        ;    (desire-conf  'multi-frame)
    )
  )


;; (if (null window-system)
;;  ()
;;  (desire-conf 'window-system)
;; )

;; (desire-conf 'window-system)
;; (desire-conf 'test)

;; (if (eq window-system 'w32)
;;  (progn
;;    (desired 'window-system)
;;    (desired 'window-system-w32)
;;  )
;; )

;; (if (and window-system
;;	 (member window-system '(x gtk))
;;	 (x-display-color-p)
;;    )
;;    (progn
;;      (desired 'window-system)
;;      (desire-conf  'faces)
;;      (desire-conf  'multi-frame)
;;    )
;; )

;;}}}
;;{{{ Serve

;;; Gnuserv
;;(desire-conf 'gnuserv nil "gnuserv")
;; Rely on dtemacs to do this, otherwise a race condition can cause
;; dtemacs to fail.
;; (gnuserv-start)

;;; Emacs daemon
;; (desire-conf 'emacs-daemon)

;;; Emacs server
(desire 'server)

;;}}}

(desire 'general)

(desire 'exec-path-from-shell)
(desire 'compat)

(desire 'async)
```


#### <span class="section-num">3.5.3</span> Тьюнинг сборщика мусора {#тьюнинг-сборщика-мусора}

-   Подключение:
    ```emacs-lisp
    (desire 'gcmh)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 13:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; The Garbage Collector Magic Hack
    ;; https://gitlab.com/koral/gcmh

    ;;; Code:

    (require 'gcmh)

    ;;; https://github.com/doomemacs/doomemacs/issues/3108
    (setopt gcmh-high-cons-threshold 33554432)  ; 32mb, or 64mb, or *maybe* 128mb, BUT NOT 512mb

    (gcmh-mode 1)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 14:</span>
      packages/gcmh.ecf
    </div>


### <span class="section-num">3.6</span> Общие настройки мод {#общие-настройки-мод}


### <span class="section-num">3.7</span> Поддержка LSP {#поддержка-lsp}

-   [Emacs. Поддержка LSP]({{< relref "2024-01-14-emacs-lsp" >}})


#### <span class="section-num">3.7.1</span> Начало {#начало}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;; LSP mode {{{
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 15:</span>
      rc.packages.el
    </div>


#### <span class="section-num">3.7.2</span> emacs-lsp-booster {#emacs-lsp-booster}

-   Включаем поддержку `emacs-lsp-booster`:
    ```emacs-lisp
    (desired 'emacs-lsp-booster :precondition-system-executable "emacs-lsp-booster")
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 16:</span>
      rc.packages.el
    </div>


#### <span class="section-num">3.7.3</span> Eglog {#eglog}

<!--list-separator-->

1.  Сам Eglot

    -   Файл `rc.packages.el`:
        ```emacs-lisp
        (desire 'eglot)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 17:</span>
          rc.packages.el
        </div>
    -   Начальная загрузка:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A client for Language Server Protocol servers
        ;;; https://github.com/joaotavora/eglot

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 18:</span>
          packages/eglot/loaddefs.ecf
        </div>
    -   Загрузка самого пакета:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A client for Language Server Protocol servers
        ;;; https://github.com/joaotavora/eglot

        (require 'eglot)

        ;;; Control blocking of LSP connection attempts
        (setopt eglot-sync-connect nil)

        (setopt eglot-connect-timeout 10)
        (setopt eglot-autoshutdown t)
        (setopt eglot-send-changes-idle-time 0.5)

        ;;; Disable `eglot-auto-display-help-buffer` because :select t in its popup rule causes eglot to steal focus too often.
        (setopt eglot-auto-display-help-buffer nil)

        ;;; Disable any debug logging and may speed things up
        (setopt eglot-events-buffer-size 0)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 19:</span>
          packages/eglot/desire.ecf
        </div>
    -   Загрузка `emacs-lsp-booster`:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Boost eglot using lsp-booster
        ;;; https://github.com/jdtsmith/eglot-booster

        (desire 'eglot-booster :recipe '(:fetcher github :repo "jdtsmith/eglot-booster" :branch "main" :files ("*.el")))
        (require 'eglot-booster)
        (eglot-booster-mode)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 20:</span>
          packages/eglot/emacs-lsp-booster.ecf
        </div>

<!--list-separator-->

2.  Дополнительные пакеты

    <!--list-separator-->

    1.  LaTeX

        -   Загрузим поддержку LSP для LaTeX:
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; A client for Language Server Protocol servers
            ;;; https://github.com/joaotavora/eglot

            (require 'eglot)

            ;;; Change order
            (let ((item (assoc '(tex-mode context-mode texinfo-mode bibtex-mode) eglot-server-programs)))
              ;; (setf (car item) '(tex-mode context-mode texinfo-mode bibtex-mode))
              (setf (cdr item) '("texlab")))

            (add-hook 'tex-mode-hook #'eglot-ensure)
            (add-hook 'latex-mode-hook #'eglot-ensure)
            (add-hook 'LaTeX-mode-hook #'eglot-ensure)

            ;;;
            ```
            <div class="src-block-caption">
              <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 21:</span>
              packages/auctex/eglot.ecf
            </div>


#### <span class="section-num">3.7.4</span> Lsp-mode {#lsp-mode}

<!--list-separator-->

1.  Собственно lsp-mode

    -   Подключим `lsp-mode`:
        ```emacs-lisp
        ;; (desire 'lsp-mode)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 22:</span>
          rc.packages.el
        </div>
    -   Первоначальная конфигурация:
        ```emacs-lisp
        ;;; Language Server Protocol support for Emacs  -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;; https://emacs-lsp.github.io/
        ;; https://github.com/emacs-lsp/lsp-mode

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 23:</span>
          packages/lsp-mode/loaddefs.ecf
        </div>
    -   Конфигурация:
        ```emacs-lisp
        ;;; Language Server Protocol support for Emacs  -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;; https://emacs-lsp.github.io/
        ;; https://github.com/emacs-lsp/lsp-mode

        (require 'lsp-mode)

        ;;; https://emacs-lsp.github.io/lsp-ui/
        (desire 'lsp-ui)

        ;;; set prefix for lsp-command-keymap (few alternatives - "C-l", "C-c l")
        (setopt lsp-keymap-prefix "C-l")

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 24:</span>
          packages/lsp-mode/desire.ecf
        </div>

<!--list-separator-->

2.  Дополнительные пакеты

    <!--list-separator-->

    1.  LaTeX (texlab)

        -   Загрузим поддержку LSP для LaTeX:
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Emacs lsp-mode client for LaTeX, on texlab
            ;; https://github.com/ROCKTAKEY/lsp-latex

            ;;; Code:

            (require 'lsp-mode)
            (desire 'lsp-latex :precondition-system-executable "texlab")

            ;;;
            ```
            <div class="src-block-caption">
              <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 25:</span>
              packages/auctex/lsp-mode.ecf
            </div>
        -   Загрузка lsp-latex:
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Emacs lsp-mode client for LaTeX, on texlab
            ;; https://github.com/ROCKTAKEY/lsp-latex

            ;;; Code:

            (require 'lsp-latex)

            ;;;; "texlab" executable must be located at a directory contained in `exec-path'.
            ;;;; If you want to put "texlab" somewhere else, you can specify the path to "texlab" as follows:
            ;; (setopt lsp-latex-texlab-executable "/path/to/texlab")

            ;;;
            ```
            <div class="src-block-caption">
              <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 26:</span>
              packages/lsp-latex/loaddefs.ecf
            </div>
        -   Настройка lsp-latex:
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Emacs lsp-mode client for LaTeX, on texlab
            ;;; https://github.com/ROCKTAKEY/lsp-latex

            ;;; Code:

            (add-hook 'tex-mode-hook #'lsp)
            (add-hook 'latex-mode-hook #'lsp)
            (add-hook 'LaTeX-mode-hook #'lsp)
            (add-hook 'LaTeX-mode-hook #'lsp)

            ;;;; For YaTeX
            (with-eval-after-load "yatex"
              (add-hook 'yatex-mode-hook #'lsp))

            ;;;; For bibtex
            (with-eval-after-load "bibtex"
              (add-hook 'bibtex-mode-hook #'lsp))

            ;;;
            ```
            <div class="src-block-caption">
              <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 27:</span>
              packages/lsp-latex/desire.ecf
            </div>

    <!--list-separator-->

    2.  lsp-treemacs

        -   Подключение интеграции treemacs и lsp-mode:
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; lsp-mode ❤️ treemacs
            ;;; https://github.com/emacs-lsp/lsp-treemacs

            ;;; Code:

            (require 'lsp-mode)

            (desire 'lsp-treemacs)
            (require 'lsp-treemacs)

            ;;; Enable bidirectional synchronization of lsp workspace folders and treemacs projects
            (lsp-treemacs-sync-mode 1)

            ;;;
            ```
            <div class="src-block-caption">
              <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 28:</span>
              packages/treemacs/lsp-mode.ecf
            </div>

    <!--list-separator-->

    3.  which-key

        -   Подключение интеграции treemacs и lsp-mode:
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; lsp which-key integration
            ;; https://emacs-lsp.github.io/lsp-mode/page/keybindings/

            ;;; Code:

            (with-eval-after-load 'lsp-mode
              (add-hook 'lsp-mode-hook #'lsp-enable-which-key-integration))

            ;;;
            ```
            <div class="src-block-caption">
              <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 29:</span>
              packages/which-key/lsp-mode.ecf
            </div>


### <span class="section-num">3.8</span> Сессии {#сессии}

```emacs-lisp
;;{{{ Session Management

(desire 'savehist)

;;}}}
```


### <span class="section-num">3.9</span> Утилиты {#утилиты}

```emacs-lisp
(desire 'uniquify)

(desire-conf 'keys)
(desire-conf 'dialog)
(desire-conf 'mouse)
```


#### <span class="section-num">3.9.1</span> xclip {#xclip}

-   [Emacs. xclip]({{< relref "2025-03-12--emacs-xclip" >}})
-   Подключение:
    ```emacs-lisp
    (desire 'xclip)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 30:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Copy&paste GUI clipboard from text terminal
    ;; https://elpa.gnu.org/packages/xclip.html

    ;;; Code:

    (require 'xclip)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 31:</span>
      packages/xclip.ecf
    </div>
-   Какие-то шаманства:
    ```emacs-lisp
    ;; (when (getenv "WAYLAND_DISPLAY")
    ;;   ;; Without this, copy and pasting from other wayland apps into
    ;;   ;; emacs-pgtk doesn't work.
    ;;   ;; https://www.emacswiki.org/emacs/CopyAndPaste#h5o-4
    ;;   (setopt wl-copy-process nil)
    ;;   (defun wl-copy (text)
    ;;     (setopt wl-copy-process (make-process :name "wl-copy"
    ;;                                         :buffer nil
    ;;                                    :command '("wl-copy" "-f" "-n")
    ;;                                    :connection-type 'pipe
    ;;                                    :noquery t))
    ;;     (process-send-string wl-copy-process text)
    ;;     (process-send-eof wl-copy-process))

    ;;   (defun wl-paste ()
    ;;     (if (and wl-copy-process (process-live-p wl-copy-process))
    ;;         nil ; should return nil if we're the current paste owner
    ;;       (shell-command-to-string "wl-paste -n | tr -d \r")))
    ;;   (setopt interprogram-cut-function 'wl-copy)
    ;;   (setopt interprogram-paste-function 'wl-paste))
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 32:</span>
      packages/xclip.ecf
    </div>
-   Явное включение для оконного режима (<https://github.com/doomemacs/doomemacs/issues/5219>):
    ```emacs-lisp
    (add-hook 'window-setup-hook #'xclip-mode)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 33:</span>
      packages/xclip.ecf
    </div>
-   Необходима строчка `'text/plain\;charset=utf-8` в `x-select-request-type` (<https://github.com/doomemacs/doomemacs/issues/5219>):
    ```emacs-lisp
    (setopt x-select-request-type nil)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 34:</span>
      packages/xclip.ecf
    </div>


#### <span class="section-num">3.9.2</span> which-key {#which-key}

-   Подключение:
    ```emacs-lisp
    (desire 'which-key)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 35:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Emacs package that displays available keybindings in popup
    ;;; https://github.com/justbur/emacs-which-key

    (require 'which-key)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 36:</span>
      packages/which-key/loaddefs.ecf
    </div>
-   Конфигурация:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Emacs package that displays available keybindings in popup
    ;; https://github.com/justbur/emacs-which-key

    ;;; Code:

    ;;;; Key-Based replacement
    (which-key-add-key-based-replacements "C-x C-f" "find files")
    (which-key-add-major-mode-key-based-replacements
     'org-mode
     "C-c C-c" "Org C-c C-c"
     "C-c C-a" "Org Attach")

    ;;;; Key and Description replacement
    (add-to-list 'which-key-replacement-alist '(("TAB" . nil) . ("↹" . nil)))
    (add-to-list 'which-key-replacement-alist '(("RET" . nil) . ("⏎" . nil)))
    (add-to-list 'which-key-replacement-alist '(("DEL" . nil) . ("⇤" . nil)))
    (add-to-list 'which-key-replacement-alist '(("SPC" . nil) . ("␣" . nil)))

    ;; Set the special keys. These are automatically truncated to one character and
    ;; have which-key-special-key-face applied. Disabled by default. An example
    ;; setting is
    ;; (setopt which-key-special-keys '("SPC" "TAB" "RET" "ESC" "DEL"))
    (setopt which-key-special-keys nil)


    ;;;; Sorting Options
    ;;;;; Default
    (setopt which-key-sort-order 'which-key-key-order)
    ;;;;; Same as default, except single characters are sorted alphabetically
    ;; (setopt which-key-sort-order 'which-key-key-order-alpha)
    ;;;;; Same as default, except all prefix keys are grouped together at the end
    ;; (setopt which-key-sort-order 'which-key-prefix-then-key-order)
    ;;;;; Same as default, except all keys from local maps shown first
    ;; (setopt which-key-sort-order 'which-key-local-then-key-order)
    ;;;;; Sort based on the key description ignoring case
    ;; (setopt which-key-sort-order 'which-key-description-order)

    ;;;; Popup Type Options
    ;;;; minibuffer | side-window | frame | custom
    (setopt which-key-popup-type 'minibuffer)

    ;;;;; Set the time delay (in seconds) for the which-key popup to appear
    (setopt which-key-idle-delay 1.0)
    (setopt which-key-idle-secondary-delay 0.05)

    ;;;; Set the maximum length (in characters) for key descriptions (commands or prefixes)
    (setopt which-key-max-description-length 27)

    ;;;; Use additional padding between columns of keys
    (setopt which-key-add-column-padding 0)

    ;;;; The maximum number of columns to display in the which-key buffer
    (setopt which-key-max-display-columns nil)


    ;;;; Use unicode
    (setopt which-key-dont-use-unicode nil)

    ;;;; Set the separator used between keys and descriptions
    (setopt which-key-separator " → " )
    (setopt which-key-unicode-correction 3)

    ;;;; Set the prefix string that will be inserted in front of prefix commands
    (setopt which-key-prefix-prefix "+" )

    ;;;; Show the key prefix on the left, top, or bottom (nil means hide the prefix)
    (setopt which-key-show-prefix 'left)

    ;;;; Set to t to show the count of keys shown vs. total keys in the mode line
    (setopt which-key-show-remaining-keys nil)

    ;;;; Show actual combinations
    (setopt which-key-computer-remaps t)

    ;;;; Like [C-h m]
    (setopt which-key-show-major-mode t)

    ;;;; Enable globally
    (which-key-mode)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 37:</span>
      packages/which-key/desire.ecf
    </div>


#### <span class="section-num">3.9.3</span> Разное {#разное}

```emacs-lisp
;; (desire 'keycast)

;; ----------------------------------------------------------------------

(desire 'pcache)
(desire 'persistent-soft)

(desire 'alert)

(desire 'rg :precondition-system-executable "rg")
```

-   В файле используется фолдинг по тройной скобке.


### <span class="section-num">3.10</span> Оформление интерфейса {#оформление-интерфейса}

-   Файл `rc.packages.el`:

<!--listend-->

```emacs-lisp
;;;; User interface
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 38:</span>
  rc.packages.el
</div>


#### <span class="section-num">3.10.1</span> Наборы иконок {#наборы-иконок}

```emacs-lisp
;;;;; Icons
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 39:</span>
  rc.packages.el
</div>

<!--list-separator-->

1.  all-the-icons

    ```emacs-lisp
    ;; (desire 'all-the-icons)
    ```

    <!--list-separator-->

    1.  Интеграция

        <!--list-separator-->

        1.  treemacs

            -   Файл: `packages/treemacs/all-the-icons.ecf`

            <!--listend-->

            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; all-the-icons integration for treemacs

            ;;; Code:

            (desire 'treemacs-all-the-icons)
            (require 'treemacs-all-the-icons)

            ;;;
            ```

<!--list-separator-->

2.  nerd-icons

    -   Загрузка пакета:
        ```emacs-lisp
        (desire 'nerd-icons)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 40:</span>
          rc.packages.el
        </div>

    <!--list-separator-->

    1.  Интеграция

        <!--list-separator-->

        1.  tab-line

            -   [Emacs. Пакет tab-line]({{< relref "2024-01-08-emacs-tab-line" >}})
            -   Поддержка `nerd-icons` в `tab-line`:
                -   <https://github.com/lucius-martius/tab-line-nerd-icons>
            -   Пакет применяет иконки из `nerd-icons` к вкладкам `tab-line`.
            -   Минорный режим `tab-line-nerd-icons-global-mode` добавляет к функции по умолчанию `tab-line-tab-name-format-default` иконки для форматирования имён вкладок.
                ```emacs-lisp
                ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
                ;;; Emacs package that uses the nerd-icons package to apply appropriate icons to tab-line tabs
                ;;;; https://github.com/lucius-martius/tab-line-nerd-icons

                ;;; Code:

                (desire 'tab-line-nerd-icons)
                (require 'tab-line-nerd-icons)

                ;;;; Enable
                (tab-line-nerd-icons-global-mode)

                ;;;
                ```
                <div class="src-block-caption">
                  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 41:</span>
                  packages/tab-line/nerd-icons.ecf
                </div>

        <!--list-separator-->

        2.  corfu

            -   Nerd-icon для corfu
            -   <https://github.com/LuigiPiucco/nerd-icons-corfu>
                ```emacs-lisp
                ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
                ;;; Icons for corfu via nerd-icons
                ;;;; https://github.com/LuigiPiucco/nerd-icons-corfu

                ;;; Code:

                (desire 'nerd-icons-corfu)
                (require 'nerd-icons-corfu)

                (add-to-list 'corfu-margin-formatters #'nerd-icons-corfu-formatter)

                ;;;; Tuning
                (setopt nerd-icons-corfu-mapping
                      '((array :style "cod" :icon "symbol_array" :face font-lock-type-face)
                        (boolean :style "cod" :icon "symbol_boolean" :face font-lock-builtin-face)
                     ;; Remember to add an entry for `t', the library uses that as default.
                        (t :style "cod" :icon "code" :face font-lock-warning-face)))

                ;;;
                ```
                <div class="src-block-caption">
                  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 42:</span>
                  packages/corfu/nerd-icons.ecf
                </div>

        <!--list-separator-->

        3.  marginalia

            -   Nerd-icon для дополнения
            -   <https://github.com/LuigiPiucco/nerd-icons-corfu>
                ```emacs-lisp
                ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
                ;;; Use nerd-icons for completion
                ;;;; https://github.com/rainstormstudio/nerd-icons-completion

                ;;; Code:

                (desire 'nerd-icons-completion)
                (require 'nerd-icons-completion)

                (nerd-icons-completion-mode)
                (add-hook 'marginalia-mode-hook #'nerd-icons-completion-marginalia-setup)

                ;;;
                ```
                <div class="src-block-caption">
                  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 43:</span>
                  packages/marginalia/nerd-icons.ecf
                </div>

        <!--list-separator-->

        4.  dired

            -   Nerd-icon для dired
            -   <https://github.com/rainstormstudio/nerd-icons-dired>
                ```emacs-lisp
                ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
                ;;; Use nerd-icons for Dired
                ;;;; https://github.com/rainstormstudio/nerd-icons-dired

                (desire 'nerd-icons-dired)
                (require 'nerd-icons-dired)

                (add-hook 'dired-mode-hook 'nerd-icons-dired-mode)

                ;;;
                ```
                <div class="src-block-caption">
                  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 44:</span>
                  packages/dired/nerd-icons.ecf
                </div>

        <!--list-separator-->

        5.  treemacs

            -   Файл: `packages/treemacs/nerd-icons.ecf`

            <!--listend-->

            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Nerd-icons theme for treemacs
            ;;; https://github.com/rainstormstudio/treemacs-nerd-icons

            ;;; Code:

            (desire 'treemacs-nerd-icons)
            (require 'treemacs-nerd-icons)
            (treemacs-load-theme "nerd-icons")

            ;;;
            ```


#### <span class="section-num">3.10.2</span> Табы {#табы}

```emacs-lisp
;;; Tabs
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 45:</span>
  rc.packages.el
</div>

<!--list-separator-->

1.  centaur-tabs

    -   [Emacs. Пакет Centaur tabs]({{< relref "2024-01-08-emacs-centaur-tabs" >}})
    -   Подключение:
        ```emacs-lisp
        ;; (desire 'centaur-tabs)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 46:</span>
          rc.packages.el
        </div>

<!--list-separator-->

2.  tab-bar

    -   [Emacs. Пакет tab-bar]({{< relref "2025-07-14--emacs-tab-bar" >}})

    <!--list-separator-->

    1.  Подключение

        -   Файл: `rc.packages.el`
            ```emacs-lisp
            (desire 'tab-bar)
            ```

    <!--list-separator-->

    2.  Загрузка

        -   Файл: `packages/tab-bar/loaddefs.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Emacs Tab Bar

        ;;; Code:

        (require 'tab-bar)

        ;;;
        ```

    <!--list-separator-->

    3.  Настройка

        <!--list-separator-->

        1.  Основная

            -   Файл: `packages/tab-bar/desire.ecf`

            <!--listend-->

            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Emacs Tab Bar

            ;;; Code:

            (tab-bar-mode 1)
            (setopt tab-bar-show 1)

            (setopt tab-bar-new-tab-to 'right)

            ;; (setopt tab-bar-new-tab-choice "*dashboard*")
            ;; (setopt tab-bar-new-tab-choice #'ibuffer)

            (setopt tab-bar-tab-hints t)
            ;; (setq tab-bar-select-tab-modifiers "super") ;; FIXME

            (setopt tab-bar-format '(tab-bar-format-history tab-bar-format-tabs tab-bar-separator))

            ;;;
            ```

        <!--list-separator-->

        2.  Заголовки

            -   Файл: `packages/tab-bar/desire.ecd/title.ecf`

            <!--listend-->

            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Emacs Tab Bar

            ;;; Code:

            (setopt tab-bar-close-button-show t)

            (setopt tab-bar-tab-hints t)

            (defvar ecf/circle-numbers-alist
              '((0 . "⓪")
                (1 . "①")
                (2 . "②")
                (3 . "③")
                (4 . "④")
                (5 . "⑤")
                (6 . "⑥")
                (7 . "⑦")
                (8 . "⑧")
                (9 . "⑨"))
              "Alist of integers to strings of circled unicode numbers.")

            (defun ecf/tab-bar-tab-name-format-default (tab i)
              (let ((current-p (eq (car tab) 'current-tab))
                    (tab-num (if (and tab-bar-tab-hints (< i 10))
                                 (alist-get i ecf/circle-numbers-alist) "")))
                (propertize
                 (concat tab-num
                         " "
                         (alist-get 'name tab)
                         (or (and tab-bar-close-button-show
                                  (not (eq tab-bar-close-button-show
                                           (if current-p 'non-selected 'selected)))
                                  tab-bar-close-button)
                             "")
                         " ")
                 'face (funcall tab-bar-tab-face-function tab))))
            (setopt tab-bar-tab-name-format-function #'ecf/tab-bar-tab-name-format-default)

            ;;;
            ```

    <!--list-separator-->

    4.  Клавиатурные сочетания

        -   Файл: `packages/tab-bar/desire.ecd/keybinding.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Emacs Tab Bar key bindings

        ;;; Code:

        (general-define-key
         ;;;; Select the previous available tab
         ;; "C-{"  'tab-bar-switch-to-prev-tab
         "s-{" 'tab-bar-switch-to-prev-tab
        ;;;; Select the next available tab
         ;; "C-}" 'tab-bar-switch-to-next-tab
         "s-}" 'tab-bar-switch-to-next-tab)

         ;; "s-t" 'tab-bar-new-tab
         ;; "s-w" 'tab-bar-close-tab

        ;;;
        ```

    <!--list-separator-->

    5.  Интеграция

        <!--list-separator-->

        1.  tab-bar-lost-commands

            -   [Emacs. tab-bar. Пакет tab-bar-lost-commands]({{< relref "2025-10-18--emacs-tab-bar-lost-commands" >}})
            -   Файл: `packages/tab-bar/desire.ecd/tab-bar-lost-commands.ecf`
                ```emacs-lisp
                ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
                ;;; The "lost commands" of the tab bar
                ;; https://github.com/fritzgrabo/tab-bar-lost-commands

                ;;; Code:

                (general-define-key
                 "M-s-{" 'tab-bar-lost-commands-switch-to-first-tab
                 "M-s-}" 'tab-bar-lost-commands-switch-to-last-tab
                 "C-s-{" 'tab-bar-lost-commands-move-tab-backward
                 "C-s-}" 'tab-bar-lost-commands-move-tab-forward
                 "C-M-s-{" 'tab-bar-lost-commands-move-tab-first
                 "C-M-s-}" 'tab-bar-lost-commands-move-tab-last)

                (general-define-key
                 :keymaps 'tab-prefix-map
                 "<return>" 'tab-bar-lost-commands-switch-to-or-create-tab)

                ;;;
                ```

        <!--list-separator-->

        2.  vim-tab-bar

            -   Файл: `packages/tab-bar/desire.ecd/vim-tab-bar.ecf`

            <!--listend-->

            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; A Vim-Inspired Tab-Bar That Automatically Adapts to Any Emacs Theme
            ;; https://github.com/jamescherti/vim-tab-bar.el

            ;;; Code

            (desire 'vim-tab-bar)
            (vim-tab-bar-mode)

            ;;;; Show the tab groups
            (setq vim-tab-bar-show-groups t)

            ;;;
            ```

<!--list-separator-->

3.  tab-line

    -   [Emacs. Пакет tab-line]({{< relref "2024-01-08-emacs-tab-line" >}})

    <!--list-separator-->

    1.  Подключение

        -   Файл: `rc.packages.el`
            ```emacs-lisp
            (desire 'tab-line)
            ```

    <!--list-separator-->

    2.  Загрузка

        -   Файл: `packages/tab-line/loaddefs.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Emacs Tab Line

            ;;; Code:

            (require 'tab-line)

            ;;;
            ```

    <!--list-separator-->

    3.  Настройка

        -   Файл: `packages/tab-line/desire.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Emacs Tab Line

            ;;; Code:

            ;;; Show the tabline in the top of the frame
            (global-tab-line-mode t)

            ;;; Do not show add-new button
            (setopt tab-line-new-button-show nil)

            ;;; Do not show close button
            (setopt tab-line-close-button-show nil)

            ;;; Change the separator between tabs
            (setopt tab-line-separator "")

            ;;;
            ```

    <!--list-separator-->

    4.  Клавиатурные сочетания

        -   Файл: `packages/tab-line/desire.ecd/keybinding.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Emacs Tab Line

            ;;; Code

            (general-define-key
             "C-<prior>" 'tab-line-switch-to-prev-tab
             "C-<iso-lefttab>" 'tab-line-switch-to-prev-tab
             "s-[" 'tab-line-switch-to-prev-tab
             "C-<next>" 'tab-line-switch-to-next-tab
             "C-<tab>" 'tab-line-switch-to-next-tab
             "s-]" 'tab-line-switch-to-next-tab)

             ;;;
            ```

    <!--list-separator-->

    5.  Intuitive Tabs in Emacs

        -   [Emacs. tab-line. Пакет intuitive-tab-line-mode]({{< relref "2025-10-16--emacs-intuitive-tab-line-mode" >}})
        -   Файл: `packages/tab-line/desire.ecd/intuitive-tab-line.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Intuitive Tabs in Emacs
            ;; https://github.com/thread314/intuitive-tab-line-mode

            ;;; Code:

            (desire 'intuitive-tab-line :recipe '(:fetcher github :repo "thread314/intuitive-tab-line-mode" :branch "master"))
            (require 'intuitive-tab-line)

            ;;;; Show all user-created buffers as tabs
            ;; (setopt tab-line-tabs-function 'intuitive-tab-line-buffers-list)

            (setopt tab-line-switch-cycling t)

            (general-define-key
             ;; "C-S-<prior>" 'intuitive-tab-line-shift-tab-left
             ;; "C-S-<next>" 'intuitive-tab-line-shift-tab-right
             "C-s-[" 'intuitive-tab-line-shift-tab-left
             "C-s-]" 'intuitive-tab-line-shift-tab-right
             )

            (recentf-mode 1)
            (general-define-key
             "C-S-t" 'recentf-open-most-recent-file)

            ;;;;
            ```


#### <span class="section-num">3.10.3</span> Нумерация строк {#нумерация-строк}

-   [Emacs. Нумерация строк]({{< relref "2024-11-28-emacs-line-numbering" >}})

<!--list-separator-->

1.  display-line-numbers

    -   Подключаем моду:
        ```emacs-lisp
        (desire 'display-line-numbers)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 47:</span>
          rc.packages.el
        </div>
    -   Файл настройки:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Interface for display-line-numbers
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 48:</span>
          packages/display-line-numbers.ecf
        </div>
    -   Глобальная настройка:
        ```emacs-lisp
        ;;; Global
        ;; (global-display-line-numbers-mode 1)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 49:</span>
          packages/display-line-numbers.ecf
        </div>
    -   Глобальная настройка:
        ```emacs-lisp
        ;;; Per mode
        (add-hook 'prog-mode-hook #'display-line-numbers-mode)
        (add-hook 'text-mode-hook #'display-line-numbers-mode)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 50:</span>
          packages/display-line-numbers.ecf
        </div>
    -   Завершение:
        ```emacs-lisp
        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 51:</span>
          packages/display-line-numbers.ecf
        </div>

<!--list-separator-->

2.  nlinum

    -   Подключаем моду:
        ```emacs-lisp
        ;; (desire 'nlinum)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 52:</span>
          rc.packages.el
        </div>
    -   Загрузка пакета:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Show line numbers in the margin
        ;;; https://elpa.gnu.org/packages/nlinum.html

        (require 'nlinum)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 53:</span>
          packages/nlinum.ecf
        </div>
    -   Глобальная настройка:
        ```emacs-lisp
        ;;; Global settings
        ;; (global-nlinum-mode 1)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 54:</span>
          packages/nlinum.ecf
        </div>
    -   Настройка по модам:
        ```emacs-lisp
        ;;; Per mode configuration
        (add-hook 'prog-mode-hook #'nlinum-mode)
        (add-hook 'text-mode-hook #'nlinum-mode)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 55:</span>
          packages/nlinum.ecf
        </div>
    -   Завершение:
        ```emacs-lisp
        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 56:</span>
          packages/nlinum.ecf
        </div>


#### <span class="section-num">3.10.4</span> shr-tag-pre-highlight : раскрашивание eww {#shr-tag-pre-highlight-раскрашивание-eww}

-   Загрузка.
    ```emacs-lisp
    ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Syntax highlighting code block in HTML for shr/eww
    ;; https://github.com/xuchunyang/shr-tag-pre-highlight.el

    ;;; Code:

    (require 'shr-tag-pre-highlight)

    (add-to-list 'shr-external-rendering-functions '(pre . shr-tag-pre-highlight))

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 57:</span>
      packages/shr-tag-pre-highlight.ecf
    </div>


#### <span class="section-num">3.10.5</span> shrface : функциональность Org-mode для eww {#shrface-функциональность-org-mode-для-eww}

-   [Emacs. Пакет shrface]({{< relref "2025-06-05--emacs-shrface" >}})

<!--list-separator-->

1.  Основной пакет : shrface

    -   Подключение.
        ```emacs-lisp
        (desire 'shrface)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 58:</span>
          rc.packages.el
        </div>
    -   Объявления.
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 59:</span>
          packages/shrface/loaddefs.ecf
        </div>
    -   Загрузка.
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        (require 'shrface)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 60:</span>
          packages/shrface/desire.ecf
        </div>
    -   Настройка.
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        (defvar shrface-general-rendering-functions
          (append '((title . eww-tag-title)
                    (form . eww-tag-form)
                    (input . eww-tag-input)
                    (button . eww-form-submit)
                    (textarea . eww-tag-textarea)
                    (select . eww-tag-select)
                    (link . eww-tag-link)
                    (meta . eww-tag-meta)
                    (code . shrface-tag-code)
                    (pre . shrface-shr-tag-pre-highlight))
                  shrface-supported-faces-alist))

        (defvar shrface-nov-rendering-functions
          (append '((img . nov-render-img)
                    (svg . nov-render-svg)
                    (title . nov-render-title)
                    (pre . shrface-shr-tag-pre-highlight)
                    (code . shrface-tag-code)
                    (form . eww-tag-form)
                    (input . eww-tag-input)
                    (button . eww-form-submit)
                    (textarea . eww-tag-textarea)
                    (select . eww-tag-select)
                    (link . eww-tag-link)
                    (meta . eww-tag-meta))
                  shrface-supported-faces-alist))

        (defvar shrface-anki-rendering-functions
          (append '((img . anki-render-img)
                    (pre . shrface-shr-tag-pre-highlight)
                    (code . shrface-tag-code)
                    (form . eww-tag-form)
                    (input . eww-tag-input)
                    (button . eww-form-submit)
                    (textarea . eww-tag-textarea)
                    (select . eww-tag-select)
                    (link . eww-tag-link)
                    (meta . eww-tag-meta))
                  shrface-supported-faces-alist))

        (setq shr-cookie-policy nil)
        (if (string-equal system-type "android")
            (setq shrface-bullets-bullet-list '("▼" "▽" "▿" "▾"))
          (setq shrface-bullets-bullet-list '("▼" "▽" "▿" "▾")))
        (add-hook 'outline-view-change-hook 'shrface-outline-visibility-changed)

        (desire 'shr-tag-pre-highlight)
        (require 'shr-tag-pre-highlight)

        (setq shr-tag-pre-highlight-lang-modes
              '(("ocaml" . tuareg) ("elisp" . emacs-lisp) ("ditaa" . artist)
                ("asymptote" . asy) ("dot" . fundamental) ("sqlite" . sql)
                ("calc" . fundamental) ("C" . c) ("cpp" . c++) ("C++" . c++)
                ("screen" . shell-script) ("shell" . sh) ("bash" . sh)
                ("rust" . rustic)
                ("rust" . rustic)
                ("awk" . bash)
                ("json" . "js")
                ;; Used by language-detection.el
                ("emacslisp" . emacs-lisp)
                ;; Used by Google Code Prettify
                ("el" . emacs-lisp)))

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 61:</span>
          packages/shrface/desire.ecd/config.ecf
        </div>

    -   Функции.
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        (defun shrface-eww-setup ()
          (unless shrface-toggle-bullets
            (shrface-regexp)
            (setq-local imenu-create-index-function #'shrface-imenu-get-tree))
          ;; workaround to show annotations in eww
          (shrface-show-all-annotations))

        (defun shrface-anki-setup ()
          (unless shrface-toggle-bullets
            (shrface-regexp)
            (setq-local imenu-create-index-function #'shrface-imenu-get-tree)))

        (defun shrface-anki-advice (orig-fun &rest args)
          (require 'eww)
          (let ((shrface-org nil)
                (shr-bullet (concat (char-to-string shrface-item-bullet) " "))
                (shr-table-vertical-line "")
                (shr-width 90)
                (shr-indentation 3)
                (anki-shr-rendering-functions shrface-anki-rendering-functions)
                (shrface-toggle-bullets nil)
                (shrface-href-versatile t))
            (apply orig-fun args)))

        (defun shrface-shr-tag-pre-highlight (pre)
          "Highlighting code in PRE."
          (let* ((shr-folding-mode 'none)
                 (shr-current-font 'default)
                 (code (with-temp-buffer
                         (shr-generic pre)
                         ;; (indent-rigidly (point-min) (point-max) 2)
                         (buffer-string)))
                 (lang (or (shr-tag-pre-highlight-guess-language-attr pre)
                           (let ((sym (language-detection-string code)))
                             (and sym (symbol-name sym)))))
                 (mode (and lang
                            (shr-tag-pre-highlight--get-lang-mode lang))))
            (shr-ensure-newline)
            (shr-ensure-newline)
            (setq start (point))
            (insert
             ;; (propertize (concat "#+BEGIN_SRC " lang "\n") 'face 'org-block-begin-line)
             (or (and (fboundp mode)
                      (with-demoted-errors "Error while fontifying: %S"
                        (shr-tag-pre-highlight-fontify code mode)))
                 code)
             ;; (propertize "#+END_SRC" 'face 'org-block-end-line )
             )
            (shr-ensure-newline)
            (setq end (point))
            (pcase (frame-parameter nil 'background-mode)
              ('light
               (add-face-text-property start end '(:background "#D8DEE9" :extend t)))
              ('dark
               (add-face-text-property start end '(:background "#292b2e" :extend t))))
            (shr-ensure-newline)
            (insert "\n")))

        (defun shrface-nov-render-html ()
          (require 'eww)
          (let ((shrface-org nil)
                (shr-bullet (concat (char-to-string shrface-item-bullet) " "))
                (shr-table-vertical-line "|")
                (shr-width 7000) ;; make it large enough, it would not fill the column (use visual-line-mode/writeroom-mode instead)
                (shr-indentation 0) ;; remove all unnecessary indentation
                (tab-width 8)
                (shr-external-rendering-functions shrface-nov-rendering-functions)
                (shrface-toggle-bullets nil)
                (shrface-href-versatile t)
                (shr-use-fonts nil)           ; nil to use default font
                (shr-map nov-mode-map))

            ;; HACK: `shr-external-rendering-functions' doesn't cover
            ;; every usage of `shr-tag-img'
            (cl-letf (((symbol-function 'shr-tag-img) 'nov-render-img))
              (shr-render-region (point-min) (point-max)))
            ;; workaround, need a delay to update the header line
            (run-with-timer 0.01 nil 'shrface-update-header-line)
            ;; workaround, show annotations when document updates
            (shrface-show-all-annotations)))

        (defun shrface-remove-blank-lines-at-the-end (start end)
          "A fix for `shr--remove-blank-lines-at-the-end' which will remove image at the end of the document."
          (save-restriction
            (save-excursion
              (narrow-to-region start end)
              (goto-char end)
              (when (and (re-search-backward "[^ \n]" nil t)
                         (not (eobp)))
                (forward-line 1)
                (delete-region (point) (min (1+ (point)) (point-max)))))))

        (defun shrface-nov-setup ()
          (unless shrface-toggle-bullets
            (shrface-regexp))
          (set-visited-file-name nil t)
          (setq tab-width 8)
          (if (string-equal system-type "android")
              (setq-local touch-screen-enable-hscroll nil)))

        (defun shrface-wallabag-setup ()
          (unless shrface-toggle-bullets
            (shrface-regexp)
            (setq-local imenu-create-index-function #'shrface-imenu-get-tree))
          (if (string-equal system-type "android")
              (setq-local touch-screen-enable-hscroll nil)))

        (defun shrface-wallabag-render-html (beg end)
          ;; workaround, show annotations when document updates
          (shrface-render-region beg end)
          (shrface-update-header-line)
          (paw-annotation-mode 1)
          (visual-line-mode 1))

        (defun shrface-render-region (beg end)
          (require 'eww)
          (let ((shrface-org nil)
                (shr-bullet (concat (char-to-string shrface-item-bullet) " "))
                ;; make it large enough, it would not fill the column
                ;; I uses visual-line-mode, writeroom-mode for improving the reading experience instead
                (shr-width 7000)
                (shr-indentation (if (string-equal system-type "android") 0 0))
                (shr-table-vertical-line "|")
                (shr-external-rendering-functions shrface-general-rendering-functions)
                (shrface-toggle-bullets nil)
                (shrface-href-versatile t)
                (shr-use-fonts nil))
            (shr-render-region beg end)))

        (defun shrface-render-advice (orig-fun &rest args)
          (require 'eww)
          (let ((shrface-org nil)
                (shr-bullet (concat (char-to-string shrface-item-bullet) " "))
                (shr-table-vertical-line "|")
                (shr-width 65)
                (shr-indentation 0)
                (shr-external-rendering-functions shrface-general-rendering-functions)
                (shrface-toggle-bullets nil)
                (shrface-href-versatile t)
                (shr-use-fonts nil))
            ;; workaround, need a delay to update the header line
            (run-with-timer 0.01 nil 'shrface-update-header-line)
            (apply orig-fun args)))

        (defun shrface-elfeed-advice (orig-fun &rest args)
          (require 'eww)
          (let ((shrface-org nil)
                (shr-bullet (concat (char-to-string shrface-item-bullet) " "))
                ;; make it large enough, it would not fill the column
                ;; I uses visual-line-mode, writeroom-mode for improving the reading experience instead
                (shr-width 7000)
                (shr-indentation 0)
                (shr-table-vertical-line "|")
                (shr-external-rendering-functions shrface-general-rendering-functions)
                (shrface-toggle-bullets nil)
                (shrface-href-versatile t)
                (shr-use-fonts nil))
            (apply orig-fun args)
            (with-current-buffer "*elfeed-entry*"
              (shrface-show-all-annotations))))

        (defun shrface-show-all-annotations()
          (when (bound-and-true-p paw-annotation-mode)
            (paw-clear-annotation-overlay)
            (paw-show-all-annotations)
            (if paw-annotation-show-wordlists-words-p
                (paw-focus-find-words :wordlist t))
            (if paw-annotation-show-unknown-words-p
                (paw-focus-find-words))))

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 62:</span>
          packages/shrface/desire.ecd/advice.ecf
        </div>

<!--list-separator-->

2.  Поддержка nov

    -   Настройка:
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        (require 'shrface)

        (add-hook 'nov-mode-hook #'eldoc-mode)
        (add-hook 'nov-mode-hook #'org-indent-mode)
        (add-hook 'nov-mode-hook #'eldoc-box-hover-mode)
        (add-hook 'nov-mode-hook #'shrface-nov-setup)

        (setopt nov-render-html-function #'shrface-nov-render-html)
        (advice-add 'shr--remove-blank-lines-at-the-end :override #'shrface-remove-blank-lines-at-the-end)

        (define-key nov-mode-map (kbd "<tab>") 'shrface-outline-cycle)
        (define-key nov-mode-map (kbd "S-<tab>") 'shrface-outline-cycle-buffer)
        (define-key nov-mode-map (kbd "C-t") 'shrface-toggle-bullets)
        (define-key nov-mode-map (kbd "C-j") 'shrface-next-headline)
        (define-key nov-mode-map (kbd "C-k") 'shrface-previous-headline)
        (define-key nov-mode-map (kbd "M-l") 'shrface-links-consult) ; or 'shrface-links-helm or 'shrface-links-counsel
        (define-key nov-mode-map (kbd "M-h") 'shrface-headline-consult) ; or 'shrface-headline-helm or 'shrface-headline-counsel

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 63:</span>
          packages/nov/shrface.ecf
        </div>

<!--list-separator-->

3.  Поддержка eww

    -   Настройка:
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        (require 'shrface)

        (advice-add 'eww-display-html :around #'shrface-render-advice)
        (add-hook 'eww-after-render-hook #'org-indent-mode)
        (add-hook 'eww-after-render-hook #'eldoc-mode)
        (add-hook 'eww-after-render-hook #'eldoc-box-hover-mode)
        (add-hook 'eww-after-render-hook #'shrface-eww-setup)

        (define-key eww-mode-map (kbd "<tab>") 'shrface-outline-cycle)
        (define-key eww-mode-map (kbd "S-<tab>") 'shrface-outline-cycle-buffer)
        (define-key eww-mode-map (kbd "C-t") 'shrface-toggle-bullets)
        (define-key eww-mode-map (kbd "C-j") 'shrface-next-headline)
        (define-key eww-mode-map (kbd "C-k") 'shrface-previous-headline)
        (define-key eww-mode-map (kbd "M-l") 'shrface-links-consult) ; or 'shrface-links-helm or 'shrface-links-counsel
        (define-key eww-mode-map (kbd "M-h") 'shrface-headline-consult) ; or 'shrface-headline-helm or 'shrface-headline-counsel

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 64:</span>
          packages/eww/shrface.ecf
        </div>

<!--list-separator-->

4.  Поддержка anki

    -   Настройка:
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        (require 'shrface)

        (add-hook 'anki-mode-hook #'org-indent-mode)
        (advice-add 'anki-render-html :around #'shrface-anki-advice)
        (advice-add 'anki-render-region :around #'shrface-anki-advice)
        (add-hook 'anki-mode-hook #'eldoc-mode)
        (add-hook 'anki-mode-hook #'eldoc-box-hover-mode)
        (add-hook 'anki-mode-hook #'shrface-anki-setup)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 65:</span>
          packages/anki/shrface.ecf
        </div>

<!--list-separator-->

5.  Поддержка calibredb

    -   Настройка:
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        (require 'shrface)

        (advice-add 'calibredb-show-entry :around #'shrface-render-advice)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 66:</span>
          packages/calibredb/shrface.ecf
        </div>

<!--list-separator-->

6.  Поддержка wallabag

    -   Настройка:
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        (require 'shrface)

        ;; (add-hook 'wallabag-entry-mode-hook #'org-indent-mode)
        (add-hook 'wallabag-entry-mode-hook #'eldoc-mode)
        (add-hook 'wallabag-entry-mode-hook #'eldoc-box-hover-mode)
        (add-hook 'wallabag-entry-mode-hook #'shrface-wallabag-setup)
        (advice-add 'wallabag-entry-quit :after #'(lambda (&rest args)
                                                    (interactive)
                                                    (if (get-buffer "*Ilist*")
                                                        (kill-buffer "*Ilist*"))))

        (setq wallabag-render-html-function #'shrface-wallabag-render-html)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 67:</span>
          packages/wallabag/shrface.ecf
        </div>

<!--list-separator-->

7.  Поддержка mu4e

    -   Настройка:
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        (require 'shrface)

        (advice-add 'mu4e-shr2text :around #'shrface-render-advice)

        (define-key mu4e-view-mode-map (kbd "<tab>") 'shrface-outline-cycle)
        (define-key mu4e-view-mode-map (kbd "S-<tab>") 'shrface-outline-cycle-buffer)
        (define-key mu4e-view-mode-map (kbd "C-t") 'shrface-toggle-bullets)
        (define-key mu4e-view-mode-map (kbd "C-j") 'shrface-next-headline)
        (define-key mu4e-view-mode-map (kbd "C-k") 'shrface-previous-headline)
        (define-key mu4e-view-mode-map (kbd "M-l") 'shrface-links-consult) ; or 'shrface-links-helm or 'shrface-links-counsel
        (define-key mu4e-view-mode-map (kbd "M-h") 'shrface-headline-consult) ; or 'shrface-headline-helm or 'shrface-headline-counsel

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 68:</span>
          packages/mu4e/shrface.ecf
        </div>

<!--list-separator-->

8.  Поддержка elfeed

    -   Настройка:
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Extend eww/nov with org-mode features, archive web pages to org files with shr
        ;; https://github.com/chenyanming/shrface

        ;;; Code:

        (require 'shrface)

        (add-hook 'elfeed-show-mode-hook #'org-indent-mode)
        (add-hook 'elfeed-show-mode-hook #'eldoc-mode)
        (add-hook 'elfeed-show-mode-hook #'eldoc-box-hover-mode)
        (add-hook 'elfeed-show-mode-hook #'shrface-wallabag-setup)
        (advice-add 'elfeed-insert-html :around #'shrface-elfeed-advice)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 69:</span>
          packages/elfeed/shrface.ecf
        </div>


#### <span class="section-num">3.10.6</span> Universal Sidecar {#universal-sidecar}

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        ;; (desire 'universal-sidecar)
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/universal-sidecar/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A universal "sidecar" buffer for emacs, inspired by the `org-roam-mode` buffer
        ;; https://git.sr.ht/~swflint/emacs-universal-sidecar

        ;;; Code:

        (require 'universal-sidecar)

        ;;;
        ```

<!--list-separator-->

3.  Конфигурация

    -   Файл: `packages/universal-sidecar/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A universal "sidecar" buffer for emacs, inspired by the `org-roam-mode` buffer
        ;; https://git.sr.ht/~swflint/emacs-universal-sidecar

        ;;; Code:

        ;;;; Enable universal-sidecar globally or in specific modes
        ;; (universal-sidecar-global-mode t)

        ;;;; Enable universal-sidecar in specific modes
        (add-hook 'prog-mode-hook #'universal-sidecar-mode)

        ;;;; Configure the sections to display in the sidecar
        (setopt universal-sidecar-sections
              '(
                buffer-git-status ; Shows Git status for the current buffer
                buffer-info-section ; Displays basic buffer information
                ;; Add other sections as needed, e.g.,
                ;; org-cite-overlay-sidecar ; For Org-cite citations if using org-cite-overlay
                ))

        ;;;; Insinuate universal-sidecar to automatically refresh
        ;;;; This advises relevant functions to update the sidecar
         (universal-sidecar-insinuate)

        ;;;; Optionally, configure refresh behavior
        ;; (setopt universal-sidecar-enable-timer t) ; Enable idle timer for refreshing
        ;; (setopt universal-sidecar-refresh-time 5) ; Set refresh time in seconds

        ;;;
        ```


### <span class="section-num">3.11</span> Автодополнение {#автодополнение}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;;; Completion

    ;; (desire 'company)
    (desire 'corfu)
    ```


### <span class="section-num">3.12</span> Автодополнение в минибуфере {#автодополнение-в-минибуфере}


#### <span class="section-num">3.12.1</span> Начало {#начало}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;;; Minibuffer completion
    ```


#### <span class="section-num">3.12.2</span> Ido {#ido}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;; (desire 'ido)
    ```


#### <span class="section-num">3.12.3</span> Helm {#helm}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;; (desire 'helm-posframe)
    ;; (desire 'helm)
    ```


#### <span class="section-num">3.12.4</span> Ivy {#ivy}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;; (desire 'ivy)
    ```


#### <span class="section-num">3.12.5</span> Selectrum {#selectrum}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;; (desire 'selectrum)
    ```


#### <span class="section-num">3.12.6</span> Vertico {#vertico}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    (desire 'vertico)
    ```


### <span class="section-num">3.13</span> Transient {#transient}


#### <span class="section-num">3.13.1</span> transient {#transient}

-   [Emacs. Пакет transient]({{< relref "2024-10-26-emacs-transient" >}})
-   Подключение:
    ```emacs-lisp
    ;;;;; Transient
    (desire 'transient)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 70:</span>
      rc.packages.el
    </div>
-   Дополнительные объявления:
    ```emacs-lisp
    ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Transient command menus
    ;; https://github.com/magit/transient

    ;;; Code:

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 71:</span>
      packages/transient/loaddefs.ecf
    </div>
-   Загрузка:
    ```emacs-lisp
    ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Transient command menus
    ;; https://github.com/magit/transient

    ;;; Code:

    (require 'transient)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 72:</span>
      packages/transient/desire.ecf
    </div>


#### <span class="section-num">3.13.2</span> Casual Suite {#casual-suite}

-   [Emacs. Пакет casual]({{< relref "2024-10-26-emacs-casual" >}})

<!--list-separator-->

1.  Начало

    -   Подключение:
        ```emacs-lisp
        ;;;;; Casual Suite
        (desire 'casual)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 73:</span>
          rc.packages.el
        </div>

<!--list-separator-->

2.  Основная библиотека

    -   Файл `packages/casual/loaddefs.ecf`:
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A collection of opinionated keyboard-driven user interfaces for various built-in Emacs modes
        ;;; https://github.com/kickingvegas/casual

        (require 'casual)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 74:</span>
          packages/casual/loaddefs.ecf
        </div>
    -   Файл `packages/casual/desire.ecf`:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A collection of opinionated keyboard-driven user interfaces for various built-in Emacs modes
        ;; https://github.com/kickingvegas/casual

        ;;; Code:

        (require 'casual-calc)
        (keymap-set calc-mode-map "C-o" #'casual-calc-tmenu)
        (keymap-set calc-alg-map "C-o" #'casual-calc-tmenu)

        (require 'casual-dired)
        (keymap-set dired-mode-map "C-o" #'casual-dired-tmenu)
        (keymap-set dired-mode-map "s" #'casual-dired-sort-by-tmenu) ; optional
        (keymap-set dired-mode-map "/" #'casual-dired-search-replace-tmenu) ; optional

        (require 'casual-isearch)
        (keymap-set isearch-mode-map "C-o" #'casual-isearch-tmenu)

        (require 'casual-ibuffer)
        (keymap-set ibuffer-mode-map "C-o" #'casual-ibuffer-tmenu)
        (keymap-set ibuffer-mode-map "F" #'casual-ibuffer-filter-tmenu)
        (keymap-set ibuffer-mode-map "s" #'casual-ibuffer-sortby-tmenu)

        (require 'casual-image)
        (keymap-set image-mode-map "C-o" #'casual-image-tmenu)

        (require 'casual-info)
        (keymap-set Info-mode-map "C-o" #'casual-info-tmenu)

        (require 'casual-re-builder)
        (keymap-set reb-mode-map "C-o" #'casual-re-builder-tmenu)
        (keymap-set reb-lisp-mode-map "C-o" #'casual-re-builder-tmenu)

        (require 'casual-bookmarks)
        (keymap-set bookmark-bmenu-mode-map "C-o" #'casual-bookmarks-tmenu)

        (require 'casual-editkit)
        (keymap-global-set "C-o" #'casual-editkit-main-tmenu)

        (require 'casual-make)
        (keymap-set makefile-mode-map "M-m" #'casual-make-tmenu)

        ;;;; Use Unicode symbols whenever appropriate for labels
        (setopt casual-lib-use-unicode t)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 75:</span>
          packages/casual/desire.ecf
        </div>
    -   Файл сделан под все элементы пакета.
    -   Необходимо будет разделить всё это по разным пакетам.

<!--list-separator-->

3.  Поддержка Avy

    -   Файл `packages/avy/casual.ecf`:
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; An opinionated Transient menu for Avy.
        ;;; https://github.com/kickingvegas/casual-avy

        (desire 'casual-avy)
        (require 'casual-avy)

        (keymap-global-set "M-g" #'casual-avy-tmenu)

        ;;; Imenu (index) Support
        (add-hook 'markdown-mode-hook #'imenu-add-menubar-index)
        (add-hook 'makefile-mode-hook #'imenu-add-menubar-index)
        (add-hook 'prog-mode-hook #'imenu-add-menubar-index)
        (add-hook 'org-mode-hook #'imenu-add-menubar-index)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 76:</span>
          packages/avy/casual.ecf
        </div>

<!--list-separator-->

4.  Поддержка Symbol Overlay

    -   Файл `packages/casual/symbol-overlay.ecf`:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; An opinionated Transient user interface for the Emacs package Symbol Overlay.
        ;;; https://github.com/kickingvegas/casual-symbol-overlay

        (desire 'casual-symbol-overlay)
        (require 'casual-symbol-overlay)

        (keymap-set symbol-overlay-map "C-o" #'casual-symbol-overlay-tmenu)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 77:</span>
          packages/casual/symbol-overlay.ecf
        </div>

<!--list-separator-->

5.  Поддержка Org-agenda

    -   Файл `packages/org/casual.ecf`:
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A collection of opinionated keyboard-driven user interfaces for various built-in Emacs modes
        ;; https://github.com/kickingvegas/casual

        ;;; Code:

        (require 'casual-agenda)

        ;;;; Load menu
        (keymap-set org-agenda-mode-map "C-o" #'casual-agenda-tmenu)

        ;;;; Configure Org Agenda to be consistent with bindings used by Casual Agenda
        (keymap-set org-agenda-mode-map "M-j" #'org-agenda-clock-goto)
        (keymap-set org-agenda-mode-map "J" #'bookmark-jump)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 78:</span>
          packages/org/casual.ecf
        </div>


### <span class="section-num">3.14</span> Разное {#разное}

-   Файл `rc.packages.el`:

<!--listend-->

```emacs-lisp
;;

(desire 'hydra)

(desire-conf 'show-paren)
;; (desire-conf 'folding)
;;

(desire 'imenu)

(desire 'ace-window)


;; (desire-conf 'toolbar)

;; Parentesis
(desire 'smartparens)
```


### <span class="section-num">3.15</span> Навигация {#навигация}

-   Заголовок:
    ```emacs-lisp
    ;;;; Navigation
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 79:</span>
      rc.packages.el
    </div>


#### <span class="section-num">3.15.1</span> Avy {#avy}

-   Подключение:
    ```emacs-lisp
    (desire 'avy)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 80:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Jump to things in Emacs tree-style
    ;; https://github.com/abo-abo/avy

    ;;; Code:

    (require 'avy)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 81:</span>
      packages/avy/loaddefs.ecf
    </div>
-   Настройка клавиатуры:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Jump to things in Emacs tree-style
    ;; https://github.com/abo-abo/avy

    ;;; Code:


    ;;;; Input one char, jump to it with a tree
    (global-set-key (kbd "C-:") 'avy-goto-char)

    ;;;; Input two consecutive chars, jump to the first one with a tree
    (global-set-key (kbd "C-'") 'avy-goto-char-2)

    ;;;; Input zero chars, jump to a line start with a tree
    (global-set-key (kbd "M-g f") 'avy-goto-line)

    ;;;; Input one char at word start, jump to a word start with a tree
    (global-set-key (kbd "M-g w") 'avy-goto-word-1)

    ;;;; Input zero chars, jump to a word start with a tree
    (global-set-key (kbd "M-g e") 'avy-goto-word-0)

    ;;;; You add this to your config to bind some stuff
    (avy-setup-default)
    (global-set-key (kbd "C-c C-j") 'avy-resume)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 82:</span>
      packages/avy/desire.ecd/keybinding.ecf
    </div>


### <span class="section-num">3.16</span> Навигация по окнам {#навигация-по-окнам}

-   [Emacs. Окна]({{< relref "2024-10-15-emacs-window" >}})


#### <span class="section-num">3.16.1</span> Начало {#начало}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;; Window navigation {{{
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 83:</span>
      rc.packages.el
    </div>


#### <span class="section-num">3.16.2</span> Windmove {#windmove}

-   [Emacs. Окна. Windmove]({{< relref "2024-10-20-emacs-window-windmove" >}})
-   Файл `rc.packages.el`:
    ```emacs-lisp
    (desire 'windmove)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 84:</span>
      rc.packages.el
    </div>
-   Настройка пакета:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Directional window-selection routinesdirectional window-selection routines
    ;;; https://www.emacswiki.org/emacs/WindMove
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 85:</span>
      packages/windmove.ecf
    </div>

-   По умолчанию используется комбинация `Shift` + стрелки. Но это конфликтует с _org-mode_:
    ```emacs-lisp
    ;;; Shifted arrow keys
    ;; (windmove-default-keybindings)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 86:</span>
      packages/windmove.ecf
    </div>
-   Будем использовать  `Ctrl` + стрелки:
    ```emacs-lisp
    ;;; Ctrl + arrow keys
    (windmove-default-keybindings 'ctrl)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 87:</span>
      packages/windmove.ecf
    </div>

-   Что-то делает:
    ```emacs-lisp
    ;;; Wrap around at edges
    (setopt windmove-wrap-around t)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 88:</span>
      packages/windmove.ecf
    </div>

-   Завершим файл:
    ```emacs-lisp
    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 89:</span>
      packages/windmove.ecf
    </div>


#### <span class="section-num">3.16.3</span> Конец {#конец}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;;}}}
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 90:</span>
      rc.packages.el
    </div>


### <span class="section-num">3.17</span> Форматирование {#форматирование}


#### <span class="section-num">3.17.1</span> Apheleia {#apheleia}

-   [Emacs. Автоформатирование. apheleia]({{< relref "2025-11-15--emacs-autoformatting-apheleia" >}})

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        (desire 'apheleia)
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/apheleia/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Run code formatter on buffer contents without moving point
        ;; https://github.com/radian-software/apheleia

        ;;; Code:

        (require 'apheleia)

        ;;;
        ```

<!--list-separator-->

3.  Конфигурация

    -   Файл: `packages/apheleia/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Run code formatter on buffer contents without moving point
        ;; https://github.com/radian-software/apheleia

        ;;; Code:

        (apheleia-global-mode +1)

        ;;;
        ```

<!--list-separator-->

4.  Форматер latex

    -   [Форматирование. LaTeX. tex-fmt]({{< relref "2025-11-15--formatting-latex-tex-fmt" >}})
    -   Файл: `packages/apheleia/desire.ecd/latex.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; An extremely fast LaTeX formatter written in Rust
        ;; https://github.com/WGUNDERWOOD/tex-fmt

        ;;; Code:

        ;;;; Define tex-fmt as an Apheleia formatter
        (add-to-list 'apheleia-formatters '(tex-fmt "tex-fmt" "--stdin"))

        ;;;; Associate tex-fmt with LaTeX modes
        (if (executable-find "tex-fmt")
            (progn
              (setf (alist-get 'latex-mode apheleia-mode-alist) 'tex-fmt)
              (setf (alist-get 'LaTeX-mode apheleia-mode-alist) 'tex-fmt)
                 (setf (alist-get 'TeX-latex-mode apheleia-mode-alist) 'tex-fmt)
                 (setf (alist-get 'TeX-mode apheleia-mode-alist) 'tex-fmt))
          nil)

        ;;;
        ```

<!--list-separator-->

5.  Форматер markdown

    -   Файл: `packages/apheleia/desire.ecd/markdown.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Modern Markdown formatter with smart typography and paragraph wrapping
        ;; https://github.com/jlevy/flowmark

        ;;; Code:

        ;;;; Define flowmark as an Apheleia formatter
        (add-to-list 'apheleia-formatters '(flowmark "flowmark" "--semantic" "--cleanups" "--smartquotes" "--ellipses" "--output" "-" "-"))

        ;;;; Associate flowmark with markdown
        ;; (if (executable-find "flowmark")
        ;;     (setf (alist-get 'markdown-mode apheleia-mode-alist) 'flowmark)
        ;;   nil)

        ;;;
        ```


#### <span class="section-num">3.17.2</span> Tree-sitter {#tree-sitter}

-   [Emacs. Инкрементальный парсер tree-sitter]({{< relref "2025-11-27--emacs-tree-sitter" >}})

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        (desire 'tree-sitter)
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/tree-sitter/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Tree-sitter bindings for Emacs Lisp
        ;; https://github.com/emacs-tree-sitter/elisp-tree-sitter

        (require 'tree-sitter)

        ;;;
        ```

<!--list-separator-->

3.  Конфигурация

    -   Файл: `packages/tree-sitter/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Tree-sitter bindings for Emacs Lisp
        ;; https://github.com/emacs-tree-sitter/elisp-tree-sitter

        (desire 'tree-sitter-langs)
        (require 'tree-sitter-langs)

        (desire 'tree-sitter-hl)
        (require 'tree-sitter-hl)

        (desire 'tree-sitter-debug)
        (require 'tree-sitter-debug)

        (desire 'tree-sitter-query)
        (require 'tree-sitter-query)

        (setopt tree-sitter-syntax-highlight-enable t)
        (setopt tree-sitter-fold-enable t)
        (setopt tree-sitter-fold-indicators-enable t)

        (global-tree-sitter-mode)

        (add-hook 'tree-sitter-after-on-hook #'tree-sitter-hl-mode)

        ;;;
        ```

<!--list-separator-->

4.  treesit-auto

    -   Файл: `packages/tree-sitter/desire.ecd/treesit-auto.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Automatic installation, usage, and fallback for tree-sitter major modes
        ;;; https://github.com/renzmann/treesit-auto

        (desire 'treesit-auto)
        (require 'treesit-auto)

        (setopt treesit-auto-install 'prompt)
        (treesit-auto-add-to-auto-mode-alist 'all)

        (customize-set-variable 'treesit-font-lock-level 3)

        (global-treesit-auto-mode)

        ;;;
        ```


#### <span class="section-num">3.17.3</span> Пробелы {#пробелы}

-   [Emacs. Пробелы]({{< relref "2025-04-11--emacs-space" >}})
-   Секция:
    ```emacs-lisp
    ;;;; Spaces
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 91:</span>
      rc.packages.el
    </div>

<!--list-separator-->

1.  stripspace

    -   Подключение:
        ```emacs-lisp
        (desire 'stripspace)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 92:</span>
          rc.packages.el
        </div>
    -   Подключение:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Automatically removes trailing whitespace before saving a buffer
        ;; https://github.com/jamescherti/stripspace.el

        ;;; Code:

        ;;;; Enable for prog-mode-hook, text-mode-hook, conf-mode-hook
        (add-hook 'prog-mode-hook 'stripspace-local-mode)
        (add-hook 'text-mode-hook 'stripspace-local-mode)
        (add-hook 'conf-mode-hook 'stripspace-local-mode)

        ;;;; The `stripspace-only-if-initially-clean' option:
        ;;;; - nil to always delete trailing whitespace.
        ;;;; - Non-nil to only delete whitespace when the buffer is clean initially.
        ;;;; (The initial cleanliness check is performed when `stripspace-local-mode' is enabled.)
        (custom-set-variables '(stripspace-only-if-initially-clean nil))

        ;;;; Enabling `stripspace-restore-column' preserves the cursor's column position
        ;;;; even after stripping spaces. This is useful in scenarios where you add
        ;;;; extra spaces and then save the file. Although the spaces are removed in the
        ;;;; saved file, the cursor remains in the same position, ensuring a consistent editing experience without affecting cursor placement.
        (custom-set-variables '(stripspace-restore-column t))

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 93:</span>
          packages/stripspace.ecf
        </div>


### <span class="section-num">3.18</span> Сворачивание {#сворачивание}


#### <span class="section-num">3.18.1</span> outline {#outline}

-   [Emacs. Пакет outline-mode]({{< relref "2025-01-28--emacs-outline-mode" >}})

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        ;; (desire 'outline)
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/outline/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Outline mode commands for Emacs

        ;;; Code:

        (require 'outline)

        ;;;
        ```

<!--list-separator-->

3.  Конфигурация

    -   Файл: `packages/outline/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Outline mode commands for Emacs

        ;;; Code:

        ;;;
        ```

<!--list-separator-->

4.  Хуки

    -   Файл: `packages/outline/desire.ecd/hook.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Outline mode commands for Emacs

        ;;; Code:

        ;;;; Автоматическое включение для режимов программирования
        ;; (defun ecf/turn-on-outline-minor-mode ()
        ;;   "Включить outline-minor-mode для режимов программирования."
        ;;   (when (derived-mode-p 'prog-mode)
        ;;     (outline-minor-mode 1)))

        ;; (add-hook 'prog-mode-hook 'ecf/turn-on-outline-minor-mode)

        ;;;; Или для конкретных режимов
        (add-hook 'emacs-lisp-mode-hook 'outline-minor-mode)
        (add-hook 'python-mode-hook 'outline-minor-mode)
        (add-hook 'js-mode-hook 'outline-minor-mode)
        (add-hook 'java-mode-hook 'outline-minor-mode)
        (add-hook 'c-mode-hook 'outline-minor-mode)
        (add-hook 'c++-mode-hook 'outline-minor-mode)
        (add-hook 'web-mode-hook 'outline-minor-mode)

        ;;;
        ```

<!--list-separator-->

5.  Настройка outline-regexp для разных языков

    -   Файл: `packages/outline/desire.ecd/regexp.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Outline mode commands for Emacs

        ;;; Code:

        ;;;; Универсальная настройка outline-regexp
        (defun ecf/set-outline-regexp ()
          "Установить outline-regexp в зависимости от режима."
          (cond
           ;; Emacs Lisp
           ((derived-mode-p 'emacs-lisp-mode 'lisp-mode 'lisp-interaction-mode)
            (setq-local outline-regexp ";;;+ \\|(def\\(un\\|subst\\|macro\\|advice\\|struct\\|class\\|method\\|generic\\)"))

           ;; Python
           ((derived-mode-p 'python-mode)
            (setq-local outline-regexp "def \\|class \\|# "))

           ;; JavaScript/TypeScript
           ((derived-mode-p 'js-mode 'js2-mode 'javascript-mode 'typescript-mode)
            (setq-local outline-regexp "function\\|class\\|const\\|let\\|var\\|// "))

           ;; Java
           ((derived-mode-p 'java-mode)
            (setq-local outline-regexp "class\\|interface\\|enum\\|@interface\\|public\\|protected\\|private\\|// "))

           ;; C/C++
           ((derived-mode-p 'c-mode 'c++-mode)
            (setq-local outline-regexp "^[ \t]*#[ \t]*\\(if\\|else\\|elif\\|endif\\|define\\|include\\)\\|// "))

           ;; Web (HTML/CSS)
           ((derived-mode-p 'web-mode)
            (setq-local outline-regexp "</?[a-z]+\\|^[ \t]*//\\|^[ \t]*/\\*\\|^[ \t]*\\*"))

           ;; Ruby
           ((derived-mode-p 'ruby-mode)
            (setq-local outline-regexp "def \\|class \\|module \\|# "))

           ;; Go
           ((derived-mode-p 'go-mode)
            (setq-local outline-regexp "func \\|type \\|struct \\|interface \\|// "))

           ;; Rust
           ((derived-mode-p 'rust-mode)
            (setq-local outline-regexp "fn \\|struct \\|enum \\|impl \\|trait \\|mod \\|// "))

           ;; PHP
           ((derived-mode-p 'php-mode)
            (setq-local outline-regexp "function\\|class\\|trait\\|interface\\|//\\|/\\*"))

           ;; Shell script
           ((derived-mode-p 'sh-mode 'bash-mode)
            (setq-local outline-regexp "function\\|# "))

           ;; Общий случай для других языков
           (t
            (setq-local outline-regexp "^[ \t]*[A-Za-z0-9]"))))

        ;; Хук для установки regexp при включении outline-minor-mode
        (add-hook 'outline-minor-mode-hook 'ecf/set-outline-regexp)

        ;;;
        ```

<!--list-separator-->

6.  Сочетания клавиш

    -   Файл: `packages/outline/desire.ecd/keybinding.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Outline mode commands for Emacs

        ;;; Code:

        ;;;; Глобальные привязки клавиш
        (global-set-key (kbd "C-c @ C-o") 'outline-minor-mode)
        (global-set-key (kbd "C-c @ C-t") 'outline-toggle-children)

        ;;;; Локальные привязки при включении outline-minor-mode
        (defun ecf/outline-minor-mode-keys ()
          "Установить ключи для outline-minor-mode."
          (when outline-minor-mode
            ;;;; Навигация
            (local-set-key (kbd "C-c @ C-n") 'outline-next-visible-heading)
            (local-set-key (kbd "C-c @ C-p") 'outline-previous-visible-heading)
            (local-set-key (kbd "C-c @ C-f") 'outline-forward-same-level)
            (local-set-key (kbd "C-c @ C-b") 'outline-backward-same-level)
            (local-set-key (kbd "C-c @ C-u") 'outline-up-heading)

            ;;;; Скрытие/показ
            (local-set-key (kbd "C-c @ C-t") 'outline-hide-body)
            (local-set-key (kbd "C-c @ C-a") 'outline-show-all)
            (local-set-key (kbd "C-c @ C-q") 'outline-hide-sublevels)
            (local-set-key (kbd "C-c @ C-e") 'outline-hide-entry)
            (local-set-key (kbd "C-c @ C-i") 'outline-show-entry)
            (local-set-key (kbd "C-c @ C-k") 'outline-show-branches)
            (local-set-key (kbd "C-c @ C-l") 'outline-hide-leaves)
            (local-set-key (kbd "C-c @ C-s") 'outline-show-subtree)
            (local-set-key (kbd "C-c @ C-d") 'outline-hide-subtree)

            ;;;; Использование стандартных Org-mode клавиш (если Org не используется)
            ;; (local-set-key (kbd "TAB") 'outline-cycle)
            ;; (local-set-key (kbd "<S-TAB>") 'outline-cycle-buffer)
            ;; (local-set-key (kbd "C-c C-n") 'outline-next-visible-heading)
            ;; (local-set-key (kbd "C-c C-p") 'outline-previous-visible-heading)
            (local-set-key (kbd "C-c C-f") 'outline-forward-same-level)
            (local-set-key (kbd "C-c C-b") 'outline-backward-same-level)
            (local-set-key (kbd "C-c C-u") 'outline-up-heading)
            (local-set-key (kbd "C-c C-t") 'outline-toggle-children)))

        (add-hook 'outline-minor-mode-hook 'ecf/outline-minor-mode-keys)

        ;;;
        ```

<!--list-separator-->

7.  Настройка outline-level

    -   Файл: `packages/outline/desire.ecd/level.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Outline mode commands for Emacs

        ;;; Code:

        ;;;; Функция для определения уровня заголовка
        (defun ecf/outline-level ()
          "Определить уровень заголовка для текущего режима."
          (save-excursion
            (cond
             ;;;; Для Emacs Lisp: уровень определяется количеством точек ввода
             ((derived-mode-p 'emacs-lisp-mode)
              (let ((count 0))
                (while (re-search-forward "[(]" nil t)
                  (setq count (1+ count)))
                count))

             ;;;; Для языков с отступами (Python)
             ((derived-mode-p 'python-mode)
              (/ (current-indentation) python-indent-offset))

             ;;;; Общий случай: уровень по отступам
             (t
              (1+ (/ (current-indentation) tab-width))))))

        ;; Установка outline-level
        (defun ecf/set-outline-level ()
          "Установить outline-level функцию."
          (setq-local outline-level 'ecf/outline-level))

        (add-hook 'outline-minor-mode-hook 'ecf/set-outline-level)

        ;;;
        ```

<!--list-separator-->

8.  Интеграция с imenu

    -   Файл: `packages/outline/imenu.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Outline mode commands for Emacs

        ;;; Code:

        ;;;; Использовать outline для навигации через imenu
        (defun ecf/outline-imenu-setup ()
          "Настроить imenu для использования outline."
          (when outline-minor-mode
            (setq-local imenu-create-index-function
                        'imenu-default-create-index-function)
            (setq-local imenu-generic-expression
                        (list
                         (list nil outline-regexp 0)))))

        (add-hook 'outline-minor-mode-hook 'ecf/outline-imenu-setup)

        ;;;; Автоматическое обновление imenu при изменениях
        (defadvice outline-minor-mode (after update-imenu activate)
          "Обновить imenu при включении/выключении outline-minor-mode."
          (when (featurep 'imenu)
            (imenu-update-menubar)))

        ;;;
        ```


#### <span class="section-num">3.18.2</span> origami {#origami}

-   [Emacs. Сворачивание (folding)]({{< relref "2025-01-28--emacs-folding" >}})
-   Подключение:
    ```emacs-lisp
    ;; (desire 'origami)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 94:</span>
      rc.packages.el
    </div>
-   Подключение:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; A folding minor mode for Emacs
    ;;; https://github.com/gregsexton/origami.el

    (require 'origami)

    (define-prefix-command 'origami-mode-map)
    (define-key ctl-x-map (kbd "z") 'origami-mode-map)
    (define-key origami-mode-map "o" 'origami-open-node)
    (define-key origami-mode-map "O" 'origami-open-node-recursively)
    (define-key origami-mode-map "c" 'origami-close-node)
    (define-key origami-mode-map "C" 'origami-close-node-recursively)
    (define-key origami-mode-map "a" 'origami-toggle-node)
    (define-key origami-mode-map "A" 'origami-recursively-toggle-node)
    (define-key origami-mode-map "R" 'origami-open-all-nodes)
    (define-key origami-mode-map "M" 'origami-close-all-nodes)
    (define-key origami-mode-map "v" 'origami-show-only-node)
    (define-key origami-mode-map "k" 'origami-previous-fold)
    (define-key origami-mode-map "j" 'origami-forward-fold)
    (define-key origami-mode-map "x" 'origami-reset)

    (global-origami-mode)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 95:</span>
      packages/origami.ecf
    </div>


#### <span class="section-num">3.18.3</span> outli {#outli}

-   [Emacs. Пакет outli]({{< relref "2025-01-28--emacs-outli" >}})
-   Подключение:
    ```emacs-lisp
    (desire 'outli :recipe '(:fetcher github :repo "jdtsmith/outli" :branch "main"))
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 96:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Simple comment-based outline folding for Emacs
    ;;; https://github.com/jdtsmith/outli

    (require 'outli)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 97:</span>
      packages/outli/loaddefs.ecf
    </div>
-   Настройка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Simple comment-based outline folding for Emacs
    ;;; https://github.com/jdtsmith/outli

    (general-define-key
     :keymaps 'outli-mode-map
     ;; convenience key to get back to containing heading
     "C-c C-p"  '(lambda () (interactive) (outline-back-to-heading)))

    (add-hook 'prog-mode-hook #'outli-mode)
    (add-hook 'text-mode-hook #'outli-mode)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 98:</span>
      packages/outli/desire.ecf
    </div>


#### <span class="section-num">3.18.4</span> hideshow {#hideshow}

<!--list-separator-->

1.  Подключение

    ```emacs-lisp
    (desire 'hideshow)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 99:</span>
      rc.packages.el
    </div>

<!--list-separator-->

2.  Загрузка

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Hideshow minor mode
    ;;;; https://www.gnu.org/software/emacs/manual/html_node/emacs/Hideshow.html
    ;;;; https://www.emacswiki.org/emacs/HideShow

    ;;; Code:

    (require 'hideshow)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 100:</span>
      packages/hideshow/loaddefs.ecf
    </div>

<!--list-separator-->

3.  Настройка

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Hideshow minor mode
    ;; https://www.gnu.org/software/emacs/manual/html_node/emacs/Hideshow.html
    ;; https://www.emacswiki.org/emacs/HideShow

    ;;; Code:

    (add-hook 'prog-mode-hook #'hs-minor-mode)
    (add-hook 'c-mode-common-hook #'hs-minor-mode)
    (add-hook 'emacs-lisp-mode-hook #'hs-minor-mode)
    (add-hook 'java-mode-hook #'hs-minor-mode)
    (add-hook 'lisp-mode-hook #'hs-minor-mode)
    (add-hook 'perl-mode-hook #'hs-minor-mode)
    (add-hook 'sh-mode-hook #'hs-minor-mode)

    ;;;; Hide the comments too when you do a 'hs-hide-all'
    (setopt hs-hide-comments nil)
    ;;;; Set whether isearch opens folded comments, code, or both code, comments, t (both), or nil (neither)
    (setopt hs-isearch-open 'code)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 101:</span>
      packages/hideshow/desire.ecf
    </div>

<!--list-separator-->

4.  Интеграция с outline

    -   Файл: `packages/hideshow/outline.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Hideshow minor mode
        ;; https://www.gnu.org/software/emacs/manual/html_node/emacs/Hideshow.html
        ;; https://www.emacswiki.org/emacs/HideShow

        ;;; Code:

        (defun ecf/outline-hideshow-integration ()
          "Интеграция outline-minor-mode и hideshow."
          (when outline-minor-mode
            ;; Использовать outline для навигации, hideshow для сворачивания блоков
            (hs-minor-mode 1)
            (local-set-key (kbd "C-c @ C-h") 'hs-hide-block)
            (local-set-key (kbd "C-c @ C-s") 'hs-show-block)
            (local-set-key (kbd "C-c @ C-c") 'hs-toggle-hiding)))

        (add-hook 'outline-minor-mode-hook 'ecf/outline-hideshow-integration)

        ;;;
        ```


#### <span class="section-num">3.18.5</span> bicycle {#bicycle}

-   Переключение режима структуры.
-   <https://github.com/tarsius/bicycle>
-   Подключение:
    ```emacs-lisp
    (desire 'bicycle)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 102:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Cycle outline and code visibility
    ;;;; https://github.com/tarsius/bicycle

    ;;; Code:

    (require 'bicycle)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 103:</span>
      packages/bicycle/loaddefs.ecf
    </div>
-   Настройка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Cycle outline and code visibility
    ;;;; https://github.com/tarsius/bicycle

    ;;; Code:

    (require 'outline)
    (require 'bicycle)

    (general-define-key
     :keymaps 'outline-minor-mode-map
     [C-tab] 'bicycle-cycle
     [S-tab] 'bicycle-cycle-global)
     ;; (define-key outline-minor-mode-map (kbd "<backtab>") #'bicycle-cycle-global)

    (add-hook 'prog-mode-hook #'outline-minor-mode)
    (add-hook 'markdown-mode-hook #'outline-minor-mode)
    (add-hook 'TeX-mode-hook #'outline-minor-mode)
    (add-hook 'LaTeX-mode-hook #'outline-minor-mode)
    (add-hook 'rst-mode-hook #'outline-minor-mode)
    (add-hook 'prog-mode-hook #'outline-minor-mode)
    (add-hook 'prog-mode-hook #'hs-minor-mode)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 104:</span>
      packages/bicycle/desire.ecf
    </div>


#### <span class="section-num">3.18.6</span> indent-bars {#indent-bars}

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        (desire 'indent-bars)
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/indent-bars/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Fast, configurable indentation guide-bars for Emacs
        ;; https://github.com/jdtsmith/indent-bars

        ;;; Code:

        (require 'indent-bars)

        ;;;
        ```

<!--list-separator-->

3.  Конфигурация

    -   Файл: `packages/indent-bars/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Fast, configurable indentation guide-bars for Emacs
        ;; https://github.com/jdtsmith/indent-bars

        ;;; Code:

        (setq indent-bars-width 1)              ;; Толщина линий
        (setq indent-bars-color "gray50")       ;; Цвет линий
        (setq indent-bars-pad-frac 0.1)         ;; Отступ от текста
        (setq indent-bars-pattern "..")         ;; Паттерн для терминала
        (setq indent-bars-display-on-blank-lines nil)  ;; Не показывать на пустых строках
        (setq indent-bars-zigzag nil)           ;; Без зигзагов
        (setq indent-bars-first-indent t)       ;; Показывать первую линию
        (setq indent-bars-auto-update-delay 0.2) ;; Задержка обновления

        ;;;
        ```

<!--list-separator-->

4.  Хуки

    -   Файл: `packages/indent-bars/desire.ecd/hook.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Fast, configurable indentation guide-bars for Emacs
        ;; https://github.com/jdtsmith/indent-bars

        ;;; Code:

        ;;;; Включить для всех языков программирования
        ;; (add-hook 'prog-mode-hook 'indent-bars-mode)

        ;;;; Черный список режимов
        ;; (defun my-disable-indent-bars ()
        ;;   (indent-bars-mode -1))

        ;; (add-hook 'org-mode-hook 'my-disable-indent-bars)
        ;; (add-hook 'markdown-mode-hook 'my-disable-indent-bars)
        ;; (add-hook 'text-mode-hook 'my-disable-indent-bars)
        ;; (add-hook 'fundamental-mode-hook 'my-disable-indent-bars)

        ;;;; Для конкретных режимов
        (add-hook 'python-mode-hook 'indent-bars-mode)
        (add-hook 'js-mode-hook 'indent-bars-mode)
        (add-hook 'web-mode-hook 'indent-bars-mode)
        (add-hook 'java-mode-hook 'indent-bars-mode)
        (add-hook 'c-mode-hook 'indent-bars-mode)
        (add-hook 'c++-mode-hook 'indent-bars-mode)
        (add-hook 'ruby-mode-hook 'indent-bars-mode)
        (add-hook 'go-mode-hook 'indent-bars-mode)

        ;;;
        ```

<!--list-separator-->

5.  Цвет

    -   Файл: `packages/indent-bars/desire.ecd/color.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Fast, configurable indentation guide-bars for Emacs
        ;; https://github.com/jdtsmith/indent-bars

        ;;; Code:

        ;;;; Автоматический подбор цвета под тему
        ;; (setq indent-bars-color '(highlight :face-bg t :blend 0.2))

        ;;;; Или установить цвета вручную
        ;; (defun my-set-indent-bars-colors ()
        ;;   "Установить цвета indent-bars в зависимости от темы."
        ;;   (cond
        ;;    ((eq (frame-parameter nil 'background-mode) 'dark)
        ;;     (setq indent-bars-color "gray40"))
        ;;    (t
        ;;     (setq indent-bars-color "gray60"))))

        ;; (add-hook 'after-init-hook 'my-set-indent-bars-colors)
        ;; (add-hook 'enable-theme-functions
        ;;           (lambda (_theme) (my-set-indent-bars-colors)))

        ;;;
        ```

<!--list-separator-->

6.  Производительность

    -   Файл: `packages/indent-bars/desire.ecd/performance.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Fast, configurable indentation guide-bars for Emacs
        ;; https://github.com/jdtsmith/indent-bars

        ;;; Code:

        ;;;; Не рисовать внутри строк и комментариев
        ;; (setq indent-bars-no-draw-line-func
        ;;       (lambda (beg end)
        ;;         (or (nth 4 (syntax-ppss))      ;; Внутри строк
        ;;             (nth 3 (syntax-ppss)))))   ;; Внутри комментариев

        ;; ;;;; Отключить для больших файлов
        ;; (defun ecf/indent-bars-maybe ()
        ;;   "Включить indent-bars только для файлов разумного размера."
        ;;   (when (< (buffer-size) 100000)  ;; 100KB
        ;;     (indent-bars-mode 1)))

        ;; (add-hook 'prog-mode-hook 'ecf/indent-bars-maybe)

        ;;;
        ```

<!--list-separator-->

7.  Интеграция с tree-sitter

    -   Файл: `packages/indent-bars/tree-sitter.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Fast, configurable indentation guide-bars for Emacs
        ;; https://github.com/jdtsmith/indent-bars

        ;;; Code:

        ;;;; Для лучшей поддержки tree-sitter
        (when (boundp 'tree-sitter-indent)
          (setq indent-bars-tree-sitter-support t))

        ;;;
        ```


#### <span class="section-num">3.18.7</span> outline-indent {#outline-indent}

-   Сворачивание и разворачивание разделов кода в зависимости от уровня отступа.
-   [Emacs. Пакет outline-indent]({{< relref "2026-02-11--emacs-outline-indent" >}})

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        (desire 'outline-indent)
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/outline-indent/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Folding text based on indentation
        ;; https://github.com/jamescherti/outline-indent.el

        ;;; Code:

        (require 'outline-indent)

        ;;;
        ```

<!--list-separator-->

3.  Конфигурация

    -   Файл: `packages/outline-indent/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Folding text based on indentation
        ;; https://github.com/jamescherti/outline-indent.el

        ;;; Code:

        ;; Основные настройки
        ;; (setopt outline-indent-alist
        ;;       '((emacs-lisp-mode . 2)
        ;;         (lisp-mode . 2)
        ;;         (lisp-interaction-mode . 2)
        ;;         (scheme-mode . 2)
        ;;         (clojure-mode . 2)
        ;;         (common-lisp-mode . 2)
        ;;         (python-mode . 4)
        ;;         (ruby-mode . 2)
        ;;         (js-mode . 2)
        ;;         (js2-mode . 2)
        ;;         (javascript-mode . 2)
        ;;         (typescript-mode . 2)
        ;;         (c-mode . 2)
        ;;         (c++-mode . 2)
        ;;         (java-mode . 4)
        ;;         (php-mode . 4)
        ;;         (perl-mode . 4)
        ;;         (cperl-mode . 4)
        ;;         (tcl-mode . 4)
        ;;         (sh-mode . 2)
        ;;         (bash-mode . 2)
        ;;         (css-mode . 2)
        ;;         (scss-mode . 2)
        ;;         (yaml-mode . 2)
        ;;         (json-mode . 2)
        ;;         (go-mode . 4)
        ;;         (rust-mode . 4)
        ;;         (swift-mode . 4)
        ;;         (kotlin-mode . 4)
        ;;         (scala-mode . 2)
        ;;         (haskell-mode . 2)
        ;;         (ocaml-mode . 2)
        ;;         (erlang-mode . 2)
        ;;         (elixir-mode . 2)))

        (setopt outline-indent-ellipsis " ▼")

        ;;;; Maintaining blank lines between folded sections
        (setopt outline-blank-line t)

        ;;;; Prevent Emacs from Searching Folded Sections
        ;; (setopt search-invisible nil)

        ;;;
        ```

<!--list-separator-->

4.  Хуки

    -   Файл: `packages/outline-indent/desire.ecd/hook.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Folding text based on indentation
        ;; https://github.com/jamescherti/outline-indent.el

        ;;; Code:

        ;;;; Включить для всех режимов программирования
        ;; (defun ecf/turn-on-outline-indent ()
        ;;   "Включить outline-indent для режимов программирования."
        ;;   (when (and (derived-mode-p 'prog-mode)
        ;;              (< (buffer-size) 100000))  ;; 100KB
        ;;     (outline-indent-mode 1)))

        ;; (add-hook 'prog-mode-hook 'ecf/turn-on-outline-indent)

        ;;;; Или для конкретных режимов
        ;; (add-hook 'emacs-lisp-mode-hook 'outline-indent-mode)
        ;; (add-hook 'python-mode-hook 'outline-indent-mode)
        ;; (add-hook 'js-mode-hook 'outline-indent-mode)
        ;; (add-hook 'java-mode-hook 'outline-indent-mode)
        ;; (add-hook 'c-mode-hook 'outline-indent-mode)

        ;;;; Черный список режимов
        ;; (defun ecf/disable-outline-indent ()
        ;;   "Отключить outline-indent для определенных режимов."
        ;;   (when (or (derived-mode-p 'org-mode)
        ;;             (derived-mode-p 'markdown-mode)
        ;;             (derived-mode-p 'text-mode)
        ;;             (derived-mode-p 'fundamental-mode))
        ;;     (outline-indent-mode -1)))

        ;; (add-hook 'outline-indent-mode-hook 'ecf/disable-outline-indent)

        ;;;; Python
        (add-hook 'python-mode-hook #'outline-indent-minor-mode)
        (add-hook 'python-ts-mode-hook #'outline-indent-minor-mode)

        ;;;; YAML
        (add-hook 'yaml-mode-hook #'outline-indent-minor-mode)
        (add-hook 'yaml-ts-mode-hook #'outline-indent-minor-mode)

        ;;;; Automatically Folding All Folds on Mode Activation
        (add-hook 'outline-indent-minor-mode-hook
                  #'(lambda()
                      (outline-indent-close-folds)))

        ;;;
        ```

<!--list-separator-->

5.  Производительность

    -   Файл: `packages/outline-indent/desire.ecd/performance.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Folding text based on indentation
        ;; https://github.com/jamescherti/outline-indent.el

        ;;; Code:

        ;;;; Оптимизация перерисовки
        (setopt outline-indent-delay 0.1)  ;; Задержка перед обновлением

        ;;;; Не показывать на пустых строках
        (setopt outline-indent-blank-lines nil)

        ;;;; Минимальная ширина отступа
        (setopt outline-indent-min-width 2)

        ;;;
        ```

<!--list-separator-->

6.  Сочетания клавиш

    -   Файл: `packages/outline-indent/desire.ecd/keybinding.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Folding text based on indentation
        ;; https://github.com/jamescherti/outline-indent.el

        ;;; Code:

        ;;;; Глобальные клавиши для управления outline-indent
        ;; (global-set-key (kbd "C-c o i") 'outline-indent-mode)
        ;; (global-set-key (kbd "C-c o +") 'outline-indent-increase)
        ;; (global-set-key (kbd "C-c o -") 'outline-indent-decrease)
        ;; (global-set-key (kbd "C-c o r") 'outline-indent-refresh)
        ;; (global-set-key (kbd "C-c o c") 'outline-indent-cycle)

        ;;;; Локальные команды для работы с outline
        ;; (defun ecf/outline-indent-commands ()
        ;;   "Установить локальные команды для outline-indent."
        ;;   (when outline-indent-mode
        ;;     (local-set-key (kbd "TAB") 'outline-indent-cycle)
        ;;     (local-set-key (kbd "<backtab>") 'outline-indent-shift-left)
        ;;     (local-set-key (kbd "C-c TAB") 'outline-indent-refresh)))

        ;; (add-hook 'outline-indent-mode-hook 'ecf/outline-indent-commands)

        ;;;; Fold management
        (define-key outline-indent-minor-mode-map (kbd "C-c o o") 'outline-indent-open-fold)     ; Open fold at point
        (define-key outline-indent-minor-mode-map (kbd "C-c o c") 'outline-indent-close-fold)    ; Close fold at point
        (define-key outline-indent-minor-mode-map (kbd "C-c o m") 'outline-indent-close-folds)   ; Close all folds
        (define-key outline-indent-minor-mode-map (kbd "C-c o r") 'outline-indent-open-folds)    ; Open all folds
        (define-key outline-indent-minor-mode-map (kbd "C-c o O") 'outline-indent-open-fold-rec) ; Open fold recursively
        (define-key outline-indent-minor-mode-map (kbd "C-c o TAB") 'outline-indent-toggle-fold) ; Toggle fold at point
        (define-key outline-indent-minor-mode-map (kbd "C-c o t") 'outline-indent-toggle-level-at-point) ; Toggle level at point

        ;;;; Selection
        (define-key outline-indent-minor-mode-map (kbd "C-c o v") 'outline-indent-select) ; Select current indented block

        ;;;; Navigation at same indentation level
        (define-key outline-indent-minor-mode-map (kbd "C-c o n") 'outline-indent-forward-same-level) ; Next heading at same level
        (define-key outline-indent-minor-mode-map (kbd "C-c o p") 'outline-indent-backward-same-level) ; Previous heading at same level

        ;;;; Shift left or right
        (define-key outline-indent-minor-mode-map (kbd "C-c o <right>") 'outline-indent-shift-right)
        (define-key outline-indent-minor-mode-map (kbd "C-c o <left>") 'outline-indent-shift-left)

        ;;;; Insert heading
        (define-key outline-indent-minor-mode-map (kbd "C-c o i") 'outline-indent-insert-heading)

        ;;;
        ```

<!--list-separator-->

7.  Оформление

    -   Файл: `packages/outline-indent/desire.ecd/decor.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Folding text based on indentation
        ;; https://github.com/jamescherti/outline-indent.el

        ;;; Code:

        ;;;; Символы для разных уровней отступа
        ;; (setopt outline-indent-chars
        ;;       '(?│ ?┃ ?┆ ?┇ ?┊ ?┋ ?╎ ?╏ ?┌ ?┐ ?└ ?┘ ?├ ?┤ ?┬ ?┴ ?┼))

        ;;;; Или простые символы
        ;; (setopt outline-indent-chars '(?| ?| ?| ?| ?|))  ;; Все одинаковые

        ;;;; Специальные символы для терминала
        ;; (setq outline-indent-chars '(?\u2502 ?\u2503 ?\u2506 ?\u2507))

        ;;;; Цвета для разных уровней отступов
        ;; (setq outline-indent-colors
        ;;       '("gray50" "gray55" "gray60" "gray65" "gray70" "gray75"))

        ;;;
        ```

<!--list-separator-->

8.  Интеграция с outline-minor-mode

    -   Файл: `packages/outline-indent/outline.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Folding text based on indentation
        ;; https://github.com/jamescherti/outline-indent.el

        ;;; Code:

        ;;;; Автоматическое включение outline-minor-mode с outline-indent
        (defun my-outline-minor-with-indent ()
          "Включить outline-minor-mode и outline-indent-mode вместе."
          (outline-minor-mode 1)
          (when (derived-mode-p 'prog-mode)
            (outline-indent-mode 1)))

        ;;;; Настройка outline-regexp для разных языков
        (defun ecf/set-outline-regexp ()
          "Установить outline-regexp для текущего режима."
          (cond
           ((derived-mode-p 'emacs-lisp-mode 'lisp-mode)
            (setq-local outline-regexp ";;;+ "))
           ((derived-mode-p 'python-mode)
            (setq-local outline-regexp "def \\|class \\|# "))
           ((derived-mode-p 'js-mode 'typescript-mode)
            (setq-local outline-regexp "function \\|class \\|const \\|let \\|var \\|// "))
           (t
            (setq-local outline-regexp "^[ \t]*[A-Za-z0-9]"))))

        (add-hook 'outline-minor-mode-hook 'ecf/set-outline-regexp)

        ;;;
        ```

<!--list-separator-->

9.  Интеграция с indent-bars

    -   Файл: `packages/outline-indent/indent-bars.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Folding text based on indentation
        ;; https://github.com/jamescherti/outline-indent.el

        ;;; Code:

        (require 'indent-bars)

        ;;;; Setting this to nil is not reliable enough
        ;; https://github.com/jdtsmith/indent-bars?tab=readme-ov-file#stipples
        (setopt indent-bars-prefer-character t)

        ;;;; When `indent-bars-prefer-character' is set to t, displaying indent bars on
        ;;;; blank lines causes cursor movement issues when moving downward, resulting
        ;;;; in abrupt shifts of the window start or cursor position.
        (setopt indent-bars-display-on-blank-lines nil)

        ;;;
        ```


### <span class="section-num">3.19</span> Проверка правописания {#проверка-правописания}

```emacs-lisp
;;; Spell {{{

;; (desire-conf 'spell)
(desire 'ispell)
;; (desire 'flyspell)
;;(desire-conf 'speck)
;;(desire-conf 'wcheck)
```


#### <span class="section-num">3.19.1</span> jinx {#jinx}

-   <https://github.com/minad/jinx>
-   Подключение:
    ```emacs-lisp
    (desire 'jinx)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 105:</span>
      rc.packages.el
    </div>
-   Начальная загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Enchanted Spell Checker
    ;;; https://github.com/minad/jinx

    (require 'jinx)

    ;;; Alternative 1: Enable Jinx globally
    ;; (add-hook 'emacs-startup-hook #'global-jinx-mode)

    ;;; Alternative 2: Enable Jinx per mode
    (dolist (hook '(text-mode-hook prog-mode-hook conf-mode-hook))
      (add-hook hook #'jinx-mode))

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 106:</span>
      packages/jinx/loaddefs.ecf
    </div>
-   Настройки:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Enchanted Spell Checker
    ;;; https://github.com/minad/jinx


    ;;; M-$ triggers correction for the misspelled word before point.
    ;;; C-u M-$ triggers correction for the entire buffer.
    ;;; C-u C-u M-$ forces correction of the word at point, even if it is not misspelled.
    (keymap-global-set "M-$" #'jinx-correct)
    (keymap-global-set "C-M-$" #'jinx-languages)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 107:</span>
      packages/jinx/desire.ecf
    </div>
-   Поддержка vertico:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Enchanted Spell Checker
    ;;; https://github.com/minad/jinx

    (require 'vertico-multiform)
    (add-to-list 'vertico-multiform-categories
                 '(jinx grid (vertico-grid-annotate . 20)))

    (vertico-multiform-mode 1)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 108:</span>
      packages/jinx/vertico.ecf
    </div>


#### <span class="section-num">3.19.2</span> Langtool {#langtool}

```emacs-lisp
;; (desire 'langtool)
;; (desire 'flycheck-languagetool)
;; (desire 'lsp-ltex :recipe '(:fetcher github :repo "emacs-languagetool/lsp-ltex" :branch "master" :files ("*.el")))
;; (desire 'eglot-ltex :recipe '(:fetcher github :repo "emacs-languagetool/eglot-ltex" :branch "master" :files ("*.el")))
```


#### <span class="section-num">3.19.3</span> Завершение {#завершение}

```emacs-lisp
;;;}}}
```


### <span class="section-num">3.20</span> Адресная книга {#адресная-книга}

```emacs-lisp
;;; Adress book {{{

(desired 'vcard)
(desire 'khardel :precondition-system-executable "khard")
(desire 'khalel :precondition-system-executable "khal")
;; (desire 'org-vcard)
;; (desire 'vdirel)
;; (desire 'bbdb)

;;;}}}
```


### <span class="section-num">3.21</span> Библиография {#библиография}


#### <span class="section-num">3.21.1</span> Начало {#начало}

```emacs-lisp
;;; Bibliography {{{
```


#### <span class="section-num">3.21.2</span> Доступ к библиографическим базам данных {#доступ-к-библиографическим-базам-данных}

-   Пакет _biblio_.
-   Подключение:
    ```emacs-lisp
    (desire 'biblio)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 109:</span>
      rc.packages.el
    </div>
-   Настройка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Browse and import bibliographic references from CrossRef, DBLP, HAL, arXiv, Dissemin, and doi.org from Emacs
    ;; https://github.com/cpitclaudel/biblio.el

    (require 'biblio)

    ;;; To get better response times from CrossRef
    ;;; https://github.com/CrossRef/rest-api-doc#etiquette
    (setopt biblio-crossref-user-email-address user-mail-address)

    ;;; Which header to use for BibTeX entries generated from arXiv metadata
    (setopt biblio-arxiv-bibtex-header "misc")

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 110:</span>
      packages/biblio.ecf
    </div>


#### <span class="section-num">3.21.3</span> Настройки bibtex {#настройки-bibtex}

-   Подключение:
    ```emacs-lisp
    (desire 'bibtex)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 111:</span>
      rc.packages.el
    </div>

<!--list-separator-->

1.  Расположение файлов

    -   Персональные настройки расположения файлов.
    -   [Организация рабочего каталога]({{< relref "2021-08-01-organization-working-directory" >}})
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 112:</span>
          packages/bibtex/personal.ecf
        </div>
    -   Основной файл библиографии:
        ```emacs-lisp
        ;;; Where bibliographies can be found
        (setq personal-bibliography '("~/work/bib/bib/main.bib"))
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 113:</span>
          packages/bibtex/personal.ecf
        </div>
    -   Файлы книг и статей:
        ```emacs-lisp
        ;;; Where PDFs can be found
        ;; (setopt bibtex-completion-library-path (directory-files-recursively "~/data/bib/pdf" "\\`[^.]*\\'" 't))
        (setq personal-library-path '("~/work/bib/data/pdf"))
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 114:</span>
          packages/bibtex/personal.ecf
        </div>
    -   Расположение литературных заметок:
        ```emacs-lisp
        ;;; Notes
        ;;; Store all notes in one file
        ;; (setopt personal-notes-path "/path/to/notes.org")
        ;;; Store notes in multiple files, one file per publication
        ;; (setopt personal-notes-path (expand-file-name "~/work/org/notes/literature"))
        (setq personal-notes-path '())
        (add-to-list 'personal-notes-path (expand-file-name "~/work/org/notes/literature"))

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 115:</span>
          packages/bibtex/personal.ecf
        </div>


#### <span class="section-num">3.21.4</span> Завершение {#завершение}

```emacs-lisp
;;;}}}
```


### <span class="section-num">3.22</span> Сниппеты {#сниппеты}

```emacs-lisp

;;(desire-conf 'yasnippet)
```


### <span class="section-num">3.23</span> Текстовые режимы {#текстовые-режимы}

-   Декларация секции:
    ```emacs-lisp
    ;;;; Work with text
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 116:</span>
      rc.packages.el
    </div>


#### <span class="section-num">3.23.1</span> Таблицы {#таблицы}

-   Декларация секции:
    ```emacs-lisp
    ;;;;; Tables
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 117:</span>
      rc.packages.el
    </div>

<!--list-separator-->

1.  lte.el

    -   Large Table Edition in Org and Markdown buffers
    -   <https://github.com/fredericgiquel/lte.el>
    -   Подключение:
        ```emacs-lisp
        (desire 'lte)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 118:</span>
          rc.packages.el
        </div>
    -   Настройка:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Large Table Edition in Org and Markdown buffers for Emacs
        ;;; https://github.com/fredericgiquel/lte.el

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 119:</span>
          packages/lte.ecf
        </div>
    -   Поддержка markdown-mode:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Large Table Edition in Org and Markdown buffers for Emacs
        ;;; https://github.com/fredericgiquel/lte.el

        (require 'lte)
        (add-hook 'markdown-mode-hook #'lte-truncate-table-mode)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 120:</span>
          packages/markdown-mode/lte.ecf
        </div>
    -   Поддержка org-mode:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Large Table Edition in Org and Markdown buffers for Emacs
        ;;; https://github.com/fredericgiquel/lte.el

        (require 'lte)
        (add-hook 'org-mode-hook #'lte-truncate-table-mode)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 121:</span>
          packages/org/lte.ecf
        </div>


#### <span class="section-num">3.23.2</span> Отображение текста {#отображение-текста}

-   Декларация секции:
    ```emacs-lisp
    ;;;;; Text view
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 122:</span>
      rc.packages.el
    </div>

<!--listend-->

```emacs-lisp
(desire 'texfrag)

;; (desire 'adaptive-wrap)
(desired 'visual-line-mode)

;; (desired 'prettify-symbols-mode)
;; (desire 'pretty-mode)
;; (desire 'prettify-math)
;; (desire 'math-preview)
```

```emacs-lisp
(desire-conf 'text)
```


#### <span class="section-num">3.23.3</span> move-text {#move-text}

-   [Emacs. Работа с текстом]({{< relref "2025-01-27--emacs-working-text" >}})
-   Позволяет перемещать строки текста.
-   Подключение:
    ```emacs-lisp
    (desire 'move-text)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 123:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Move current line or region up or down
    ;;; https://github.com/emacsfodder/move-text

    (require 'move-text)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 124:</span>
      packages/move-text/loaddefs.ecf
    </div>
-   Настройка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Move current line or region up or down
    ;;; https://github.com/emacsfodder/move-text

    ;;; Use the default bindings
    (move-text-default-bindings)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 125:</span>
      packages/move-text/desire.ecf
    </div>
-   Перестройка отступов:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Move current line or region up or down
    ;;; https://github.com/emacsfodder/move-text

    ;;; Indent after moving

    (defun indent-region-advice (&rest ignored)
      (let ((deactivate deactivate-mark))
        (if (region-active-p)
            (indent-region (region-beginning) (region-end))
          (indent-region (line-beginning-position) (line-end-position)))
        (setopt deactivate-mark deactivate)))

    (advice-add 'move-text-up :after 'indent-region-advice)
    (advice-add 'move-text-down :after 'indent-region-advice)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 126:</span>
      packages/move-text/desire.ecd/reindent.ecf
    </div>


#### <span class="section-num">3.23.4</span> delsel {#delsel}

-   В дереве emacs.
-   При вставке текста в выделенную область вставленный текст заменяет исходный.
-   Подключение:
    ```emacs-lisp
    (desire 'delsel)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 127:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Delete the selected text upon text insertion

    ;;; Code:

    (require 'delsel)
    (add-hook 'after-init-hook 'delete-selection-mode)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 128:</span>
      packages/delsel.ecf
    </div>


#### <span class="section-num">3.23.5</span> pandoc {#pandoc}

```emacs-lisp
(desire 'pandoc-mode)
```


#### <span class="section-num">3.23.6</span> markdown {#markdown}

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        (desire 'markdown-mode)
        ```

<!--list-separator-->

2.  Интеграция

    <!--list-separator-->

    1.  lsp-mode

        -   [Emacs. LSP для Markdown]({{< relref "2025-08-11--emacs-lsp-markdown" >}})
        -   Файл: `packages/markdown-mode/lsp-mode.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Emacs lsp-mode client for markdown
            ;; https://emacs-lsp.github.io/lsp-mode/page/lsp-marksman/

            ;;; Code:

            (require 'lsp-mode)
            (add-hook 'markdown-mode #'lsp)

            ;;;; Marksman
            (require 'lsp-marksman)

            ;;;
            ```

    <!--list-separator-->

    2.  eglot

        -   [Emacs. LSP для Markdown]({{< relref "2025-08-11--emacs-lsp-markdown" >}})
        -   Файл: `packages/markdown-mode/eglot.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; A client for Language Server Protocol servers
            ;; https://github.com/joaotavora/eglot

            ;;; Code

            (require 'eglot)

            (add-hook 'markdown-mode-hook #'eglot-ensure)

            ;;;
            ```


#### <span class="section-num">3.23.7</span> Форматы документов {#форматы-документов}

<!--list-separator-->

1.  Оглавление pdf

    -   [Emacs. Пакет doc-toc]({{< relref "2025-05-10--emacs-package-doc-toc" >}})
    -   Подключение:
        ```emacs-lisp
        (desire 'doc-toc)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 129:</span>
          rc.packages.el
        </div>
    -   Предварительные настройки:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Create, cleanup, add and manage Table Of Contents (TOC) of pdf and djvu documents with Emacs
        ;; https://github.com/dalanicolai/doc-tools-toc

        ;;; Code:

        (desire 'pdf-tools)
        (desire 'djvu)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 130:</span>
          packages/doc-toc/loaddefs.ecf
        </div>
    -   Загрузка пакета:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Create, cleanup, add and manage Table Of Contents (TOC) of pdf and djvu documents with Emacs
        ;; https://github.com/dalanicolai/doc-tools-toc

        ;;; Code:

        (require 'doc-toc)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 131:</span>
          packages/doc-toc/desire.ecf
        </div>

<!--list-separator-->

2.  Метаданные pdf

    -   [Emacs. Пакет pdf-meta-edit]({{< relref "2025-06-15--emacs-pdf-meta-edit" >}})
    -   Подключение:
        ```emacs-lisp
        (desire 'pdf-meta-edit)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 132:</span>
          rc.packages.el
        </div>
    -   Предварительные настройки:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Emacs code for editing a PDF's metadata, labels, and bookmarks
        ;; https://github.com/krisbalintona/pdf-meta-edit

        ;;; Code:

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 133:</span>
          packages/pdf-meta-edit/loaddefs.ecf
        </div>
    -   Загрузка пакета:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Emacs code for editing a PDF's metadata, labels, and bookmarks
        ;; https://github.com/krisbalintona/pdf-meta-edit

        ;;; Code:

        (require 'pdf-meta-edit)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 134:</span>
          packages/pdf-meta-edit/desire.ecf
        </div>

<!--list-separator-->

3.  Формат pdf

    -   Подключение:
        ```emacs-lisp
        (desire 'pdf-tools)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 135:</span>
          rc.packages.el
        </div>

    -   Подключение doc-toc:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Create, cleanup, add and manage Table Of Contents (TOC) of pdf and djvu documents with Emacs
        ;; https://github.com/dalanicolai/doc-tools-toc

        ;;; Code:

        (require 'doc-toc)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 136:</span>
          packages/pdf-tools/doc-toc.ecf
        </div>

<!--list-separator-->

4.  Формат epub

    ```emacs-lisp
    (desire 'nov)
    ```

<!--list-separator-->

5.  Формат fb2

    ```emacs-lisp
    (desire 'fb2-reader)

    ;; (desire 'valign)
    ```


#### <span class="section-num">3.23.8</span> quarto {#quarto}

-   Поддержка quarto.

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        ;;;; Quarto mode
        (desire 'quarto-mode)
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/quarto-mode/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; An emacs mode for quarto
        ;; https://github.com/quarto-dev/quarto-emacs

        ;;; Code:

        (desire' polymode)
        (desire 'poly-markdown)

        (require 'quarto-mode)

        ;;;
        ```

<!--list-separator-->

3.  Интеграция

    <!--list-separator-->

    1.  lsp-mode

        -   [Emacs. LSP для Markdown]({{< relref "2025-08-11--emacs-lsp-markdown" >}})
        -   Файл: `packages/quarto-mode/lsp-mode.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Emacs lsp-mode client for markdown
            ;; https://emacs-lsp.github.io/lsp-mode/page/lsp-marksman/

            ;;; Code:

            (require 'lsp-mode)
            (add-hook 'quarto-mode #'lsp)

            ;;;; Marksman
            (require 'lsp-marksman)

            ;;;
            ```

    <!--list-separator-->

    2.  eglot

        -   [Emacs. LSP для Markdown]({{< relref "2025-08-11--emacs-lsp-markdown" >}})
        -   Файл: `packages/markdown-mode/eglot.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; A client for Language Server Protocol servers
            ;; https://github.com/joaotavora/eglot

            ;;; Code

            (require 'eglot)

            (add-hook 'quarto-mode-hook #'eglot-ensure)

            ;;;
            ```


#### <span class="section-num">3.23.9</span> calibredb {#calibredb}

-   Клиент для Calibre (см. [Каталогизатор книг Calibre]({{< relref "2025-02-04--calibre-book-cataloger" >}})).
-   <https://github.com/chenyanming/calibredb.el>
-   Подключение:
    ```emacs-lisp
    (desire 'calibredb)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 137:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;; Emacs calibre client - A Document Management Solution in Emacs
    ;; https://github.com/chenyanming/calibredb.el

    ;;; Code:

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 138:</span>
      packages/calibredb/loaddefs.ecf
    </div>
-   Конфигурация:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;; Emacs calibre client - A Document Management Solution in Emacs
    ;; https://github.com/chenyanming/calibredb.el

    ;;; Code:

    (require 'calibredb)

    ;;;; Size indicator
    (setopt calibredb-size-show t)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 139:</span>
      packages/calibredb/desire.ecf
    </div>
-   Персональные настройки:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;; Emacs calibre client - A Document Management Solution in Emacs
    ;; https://github.com/chenyanming/calibredb.el

    ;;; Code:

    (setq calibredb-root-dir "/data/book/calibre")
    ;;;; for folder driver metadata: it should be .metadata.calibre
    (setq calibredb-db-dir (expand-file-name "metadata.db" calibredb-root-dir))
    (setq calibredb-library-alist '(("/data/book/calibre" (name . "Calibre")) ;; with name
                                    ;; ("/Users/damonchan/Documents/Books Library") ;; no name
                                    ;; ("/Users/damonchan/Documents/HELLO")
                                    ;; ("/Users/damonchan/Documents/Books")
                                    ;; ("/Users/damonchan/Documents/World"))
          ))

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 140:</span>
      packages/calibredb/personal.ecf
    </div>
-   Поддержка `nerd-icons`:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;; Emacs calibre client - A Document Management Solution in Emacs
    ;; https://github.com/chenyanming/calibredb.el

    ;;; Code:

    (setopt calibredb-format-nerd-icons t)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 141:</span>
      packages/calibredb/nerd-icons.ecf
    </div>
-   Поддержка `all-the-icons`:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;; Emacs calibre client - A Document Management Solution in Emacs
    ;; https://github.com/chenyanming/calibredb.el

    ;;; Code:

    (setopt calibredb-format-all-the-icons t)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 142:</span>
      packages/calibredb/all-the-icons.ecf
    </div>


### <span class="section-num">3.24</span> Управление временем {#управление-временем}

-   Разделитель:
    ```emacs-lisp
    ;;;; Time management
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 143:</span>
      rc.packages.el
    </div>


#### <span class="section-num">3.24.1</span> pomm {#pomm}

-   [Emacs. Метод pomodoro]({{< relref "2025-01-16--emacs-pomodoro-method" >}})

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        (desire 'pomm)
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/pomm/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Implementation of Pomodoro and Third Time techniques for Emacs
        ;; https://github.com/SqrtMinusOne/pomm.el

        ;;; Code:

        (require 'pomm)

        ;;;
        ```

<!--list-separator-->

3.  Настройка

    -   Файл: `packages/pomm/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Implementation of Pomodoro and Third Time techniques for Emacs
        ;; https://github.com/SqrtMinusOne/pomm.el

        ;;; Code:

        ;;;; If you want an actual notification
        (setopt alert-default-style 'libnotify)

        ;;;; Display in the modeline
        (pomm-mode-line-mode)

        ;;;; By default sounds are disabled
        (setopt pomm-audio-enabled t)

        ;;;; Ticking sound
        ;; (setopt pomm-audio-tick-enabled t)

        ;;;
        ```

<!--list-separator-->

4.  Интерфейс к polybar (разным реализациям)

    -   Файл: `packages/pomm/desire.ecd/polybar.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Implementation of Pomodoro and Third Time techniques for Emacs
        ;; https://github.com/SqrtMinusOne/pomm.el

        ;;; Code:

        (add-hook 'pomm-on-tick-hook 'pomm-update-mode-line-string)
        (add-hook 'pomm-on-status-changed-hook 'pomm-update-mode-line-string)

        ;;;
        ```

<!--list-separator-->

5.  Сохранение истории

    -   Файл: `packages/pomm/desire.ecd/history.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Log history in CSV format
        ;; https://github.com/SqrtMinusOne/pomm.el


        ;;; Code:

        ;;;; Save timer history in a CSV format
        (setopt pomm-csv-history-file (expand-file-name "pomm.csv" user-emacs-directory))

        ;;;; Customize timestamp (for traditional YYYY-MM-DD HH:mm:ss)
        (setopt pomm-csv-history-file-timestamp-format "%F %T")

        ;;;
        ```

<!--list-separator-->

6.  pomm-dwim

    -   <https://github.com/SqrtMinusOne/pomm.el/issues/18>
    -   Файл: `packages/pomm/desire.ecd/pomm-dwim.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; pomm-dwim: Like pomm-start but pauses if running
        ;; https://github.com/SqrtMinusOne/pomm.el/issues/18

        ;;; Code:

        (defun pomm-dwim (arg)
          "Like `pomm-start' but will also pause the timer if it is already running.
        Alternatively if prefixed with \\[universal-argument], the timer state will be reset."
          (interactive "p")
          (if (eq arg 4)
              (pomm--do-reset)
            (if (eq 'running (alist-get 'status pomm--state))
                (pomm-pause)
              (pomm-start))))

        ;;;
        ```

<!--list-separator-->

7.  Интеграция org-mode

    -   Файл: `packages/org/pomm.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Log history in CSV format
        ;; https://github.com/SqrtMinusOne/pomm.el

        ;;; Code:

        (require 'pomm)

        (add-hook 'pomm-on-status-changed-hook #'pomm--sync-org-clock)
        (add-hook 'pomm-third-time-on-status-changed-hook #'pomm-third-time--sync-org-clock)

        ;;;
        ```


#### <span class="section-num">3.24.2</span> org-pomodoro {#org-pomodoro}

```emacs-lisp
(desire 'org-pomodoro)
;; (desire 'hammy)
```


### <span class="section-num">3.25</span> LaTeX {#latex}

```emacs-lisp
;;; LaTeX

(desire 'xenops)

(desire 'cdlatex)

(desire-conf 'xdvi nil "xdvi-search")
(desired 'reftex)
;; (desire-conf 'tex)
(desired 'preview-latex)
```


#### <span class="section-num">3.25.1</span> Auctex {#auctex}

-   Подключение
    ```emacs-lisp
    (desire 'auctex)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 144:</span>
      rc.packages.el
    </div>

<!--list-separator-->

1.  Парсинг файлов TeX

    -   Заголовок:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Automatic Parsing of TeX Files
        ;; http://www.gnu.org/software/auctex/

        ;;; Code:
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 145:</span>
          packages/auctex/desire.ecd/parsing.ecf
        </div>
    -   Автопарсинг:
        ```emacs-lisp
        ;;;; Automatic Parsing of TeX Files
        (setopt TeX-parse-self t)                 ; Enable parse on load
        (setopt TeX-auto-save t)                  ; Enable parse on save
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 146:</span>
          packages/auctex/desire.ecd/parsing.ecf
        </div>
    -   Убрать символы табуляции:
        ```emacs-lisp
        ;;;; Automatically remove all tabs from a file before saving it
        (setopt TeX-auto-untabify t)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 147:</span>
          packages/auctex/desire.ecd/parsing.ecf
        </div>
    -   Финал:
        ```emacs-lisp
        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 148:</span>
          packages/auctex/desire.ecd/parsing.ecf
        </div>


### <span class="section-num">3.26</span> Org-mode {#org-mode}

-   [Org-mode]({{< relref "2021-10-14-org-mode" >}})
-   Конфигурация для `org-mode`:
    ```emacs-lisp
    ;;;; Org-mode
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 149:</span>
      rc.packages.el
    </div>


#### <span class="section-num">3.26.1</span> Babel {#babel}

-   [Emacs. Org Babel]({{< relref "2022-10-15-emacs-org-babel" >}})
-   Общие настройки babel:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Org-Babel

    ;;; Code:
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 150:</span>
      packages/org/desire.ecd/babel.ecf
    </div>
-   Сохраняем отступы:
    ```emacs-lisp
    ;;;; Keep the indentation on org-babel-tangle
    ;; (setopt org-src-preserve-indentation t)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 151:</span>
      packages/org/desire.ecd/babel.ecf
    </div>
-   Отключим подтверждение запутывания:
    ```emacs-lisp
    ;;;; Org-babel confirm before evaluation
    (setopt org-confirm-babel-evaluate nil)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 152:</span>
      packages/org/desire.ecd/babel.ecf
    </div>

<!--list-separator-->

1.  org-auto-tangle

    -   Репозиторий: <https://github.com/yilkalargaw/org-auto-tangle/>
    -   Подключим org-auto-tangle:
        ```emacs-lisp
        ;;;; A simple emacs package to allow org file tangling upon save
        ;;;; https://github.com/yilkalargaw/org-auto-tangle/
        (desire 'org-auto-tangle)
        (require 'org-auto-tangle)
        (add-hook 'org-mode-hook 'org-auto-tangle-mode)

        ;;;; Auto-tangle as the default behavior for all org buffers
        ;; (setopt org-auto-tangle-default t)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 153:</span>
          packages/org/desire.ecd/babel.ecf
        </div>

<!--list-separator-->

2.  Поддержка языков

    -   Включим поддержку разных языков программирования:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-

        ;;; Scripts
        (require 'ob-awk)
        (require 'ob-eshell)
        (require 'ob-sed)
        (require 'ob-shell)

        ;;; Diagrams
        (require 'ob-ditaa)
        (require 'ob-dot)
        (require 'ob-plantuml)

        ;;; Programming languages
        (require 'ob-calc)
        (require 'ob-C)
        (require 'ob-clojure)
        (require 'ob-comint)
        (require 'ob-core)
        (require 'ob-css)
        (require 'ob-emacs-lisp)
        (require 'ob-eval)
        (require 'ob-exp)
        (require 'ob-forth)
        (require 'ob-fortran)
        (require 'ob-gnuplot)
        (require 'ob-groovy)
        (require 'ob-haskell)
        (require 'ob-java)
        (require 'ob-js)
        (require 'ob-julia)
        (require 'ob-latex)
        (require 'ob-lilypond)
        (require 'ob-lisp)
        (require 'ob-lob)
        (require 'ob-lua)
        (require 'ob-makefile)
        (require 'ob-matlab)
        (require 'ob-maxima)
        (require 'ob-ocaml)
        (require 'ob-octave)
        (require 'ob-org)
        (require 'ob-perl)
        (require 'ob-processing)
        (require 'ob-python)
        (require 'ob-ref)
        (require 'ob-R)
        (require 'ob-ruby)
        (require 'ob-sass)
        (require 'ob-scheme)
        (require 'ob-screen)
        (require 'ob-sql)
        (require 'ob-sqlite)
        (require 'ob-table)
        (require 'ob-tangle)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 154:</span>
          packages/org/desire.ecd/ob.ecf
        </div>

<!--list-separator-->

3.  Конец

    ```emacs-lisp
    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 155:</span>
      packages/org/desire.ecd/babel.ecf
    </div>


#### <span class="section-num">3.26.2</span> Оформление {#оформление}

<!--list-separator-->

1.  org-superstar

    <!--list-separator-->

    1.  Подключение

        -   Файл: `rc.packages.el`
            ```emacs-lisp
            ;; (desire 'org-superstar)
            ```

    <!--list-separator-->

    2.  Загрузка

    <!--list-separator-->

    3.  Настройка

    <!--list-separator-->

    4.  Интеграция с org


#### <span class="section-num">3.26.3</span> Разное {#разное}

```emacs-lisp
;; (desire 'org-ql)

(desire 'org-appear)
(desire 'org-fragtog)
(desire 'org-custom-cookies)
;; (desire 'svg-tag-mode)
;; (desire 'org-modern-indent :recipe '(:fetcher github :repo "jdtsmith/org-modern-indent" :branch "main" :files ("*.el")))
(desire 'org-modern)
;; (desire 'org-contacts)
;; (desire 'google-contacts)
(desire 'org-edna)
(desire 'org-ref)
(desire 'org-tree-slide)
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 156:</span>
  rc.packages.el
</div>


#### <span class="section-num">3.26.4</span> org-transclusion {#org-transclusion}

-   [Emacs. Org-transclusion]({{< relref "2025-12-30--emacs-org-transclusion" >}})

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`

    <!--listend-->

    ```emacs-lisp
    (desire 'org-transclusion)
    ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/org-transclusion/loaddefs.ecf`

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Emacs package to enable transclusion with Org Mode
    ;; https://github.com/nobiot/org-transclusion

    ;;; Code:

    ;;;
    ```

<!--list-separator-->

3.  Настройка

    -   Файл: `packages/org-transclusion/desire.ecf`

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Emacs package to enable transclusion with Org Mode
    ;; https://github.com/nobiot/org-transclusion

    ;;; Code:

    (require 'org-transclusion)

    ;; (define-key global-map (kbd "<f12>") #'org-transclusion-add)
    (define-key global-map (kbd "C-c n T") #'org-transclusion-mode)

    ;;; Ignore tags when export
    (with-eval-after-load 'ox-hugo
      (add-to-list 'ecf/tags-categories-to-be-removed "transclude"))

    ;;;
    ```

<!--list-separator-->

4.  org-transclusion-power-pack

    -   Файл: `packages/org-transclusion/desire.ecd/org-transclusion-power-pack.ecf`

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Enhancements for org-transclusion
    ;; https://github.com/incandescentman/org-transclusion-power-pack

    ;;; Code:

    ;; (desire 'org-transclusion-power-pack :recipe '(:fetcher github :repo "incandescentman/org-transclusion-power-pack" :branch "main"))
    ;; (require 'org-transclusion-power-pack)

    ;;;
    ```

<!--list-separator-->

5.  Интеграция

    -   Файл: `packages/org/org-transclusion.ecf`

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Emacs package to enable transclusion with Org Mode
    ;; https://github.com/nobiot/org-transclusion

     (require 'org-transclusion)
    ```


#### <span class="section-num">3.26.5</span> Повестка дня {#повестка-дня}

-   Конфигурация повестки дня:

<!--listend-->

```emacs-lisp
;;; Agenda
(desire 'org-super-agenda)

;;(if (desiredp 'org-ql)
;; (desire 'org-agenda-files-track-ql)
(desire 'org-agenda-files-track)
;;)

;;(if (desiredp 'org-ql)
;; (desire 'org-agenda-files-track-ql :recipe '(:fetcher github :repo "nicolas-graves/org-agenda-files-track" :branch "master" :files ("org-agenda-files-track-ql.el")))
;; (desire 'org-agenda-files-track :recipe '(:fetcher github :repo "nicolas-graves/org-agenda-files-track" :branch "master" :files ("org-agenda-files-track.el")))
;;)

;;; Literate
(desire 'org-tanglesync)

;; (desire 'org-gcal)
(desire 'org-journal)

(desire 'org-noter)
;; (desire 'org-noter :recipe '(:fetcher github :repo "org-noter/org-noter" :branch "feature/org-roam-integration" :files ("*.el" "modules/*.el")))

;; (desire 'org-transclusion)
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 157:</span>
  rc.packages.el
</div>


#### <span class="section-num">3.26.6</span> org-node {#org-node}

-   Подключение:
    ```emacs-lisp
    (desire 'org-node)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 158:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; A notetaking system like Roam using Emacs Org-mode
    ;; https://github.com/meedstrom/org-node

    ;;; Code:

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 159:</span>
      packages/org-node/loaddefs.ecf
    </div>

-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; A notetaking system like Roam using Emacs Org-mode
    ;; https://github.com/meedstrom/org-node

    ;;; Code:

    (desire 'org-mem)

    (require 'org-node)

    (setopt org-mem-do-sync-with-org-id t)
    (setopt org-mem-watch-dirs (list org-roam-directory))
    (org-mem-updater-mode)
    (org-node-cache-mode)
    (org-node-roam-accelerator-mode)

    ;;;; Node seqs
    (require 'org-node-seq)
    (org-node-seq-mode)

    (setopt org-node-creation-fn #'org-node-new-via-roam-capture)
    (setopt org-node-file-slug-fn #'org-node-slugify-like-roam-default)
    (setopt org-node-file-timestamp-format "%Y%m%dT%H%M%S--")

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 160:</span>
      packages/org-node/desire.ecf
    </div>
-   Клавиатурные сочетания:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; A notetaking system like Roam using Emacs Org-mode
    ;; https://github.com/meedstrom/org-node

    ;;; Code:

    (keymap-global-set "C-c N" org-node-global-prefix-map)
    (with-eval-after-load 'org
      (keymap-set org-mode-map "C-c N" org-node-org-prefix-map))

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 161:</span>
      packages/org-node/desire.ecd/key.ecf
    </div>

<!--list-separator-->

1.  Интеграция с org-roam

    -   Используем не отдельно, а как надстройку над org-roam:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A notetaking system like Roam using Emacs Org-mode
        ;; https://github.com/meedstrom/org-node

        ;;; Code:

        (require 'org-node)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 162:</span>
          packages/org-roam/org-node.ecf
        </div>


#### <span class="section-num">3.26.7</span> org-habit-ng {#org-habit-ng}

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        ;; (desire 'org-habit-ng :recipe '(:fetcher codeberg :repo "Trevoke/org-habit-ng" :branch "congruence"))
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/org-habit-ng/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Org-habit-ng lets you schedule habits that org-mode's standard repeaters can't express
        ;; https://codeberg.org/Trevoke/org-habit-ng

        ;;; Code:

        (desire 'transient)

        ;;;
        ```

<!--list-separator-->

3.  Настройка

    -   Файл: `packages/org-habit-ng/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Org-habit-ng lets you schedule habits that org-mode's standard repeaters can't express
        ;; https://codeberg.org/Trevoke/org-habit-ng

        ;;; Code:

        (require 'transient)
        (require 'org-habit-ng)
        (org-habit-ng-mode 1)

        ;;;
        ```


#### <span class="section-num">3.26.8</span> org-gtd {#org-gtd}

-   [Emacs. Пакеты. Org-gtd]({{< relref "2023-07-31-emacs-packages-org-gtd" >}})

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        ;;;; GTD
        (desire 'org-gtd)
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/org-gtd/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A package for using GTD with org-mode
        ;; https://github.com/Trevoke/org-gtd.el

        ;;; Code:

        ;;;; Suppress upgrade warnings (set BEFORE org-gtd loads)
        (setq org-gtd-update-ack "4.0.0")

        ;;;
        ```

<!--list-separator-->

3.  Настройка

    -   Файл: `packages/org-gtd/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A package for using GTD with org-mode
        ;; https://github.com/Trevoke/org-gtd.el

        ;;; Code:

        ;;;; Enable org-edna for project dependencies
        (desire 'org-edna)
        (require 'org-edna)
        (setopt org-edna-use-inheritance t)
        (org-edna-mode 1)

        ;;;; Show properties in the agenda
        ;; (desire 'org-agenda-property)
        ;; (require 'org-agenda-property)

        (setopt org-gtd-agenda-property-list '("LOCATION" "DELEGATED_TO"))
        (setopt org-gtd-agenda-property-position 'where-it-fits)
        (setopt org-gtd-agenda-property-column 60)
        (setopt org-gtd-agenda-property-separator "|")

        ;;;; Load org-gtd
        (require 'org-gtd)

        ;;;; Set GTD directory (defaults to ~/gtd/)
        (setopt org-gtd-directory org-directory-todo)
        ;;;; Add org-gtd files to your agenda
        (add-to-list 'org-agenda-files org-gtd-directory)

        ;;;; Make org-gtd prompt for refile target instead of auto-refiling
        (setopt org-gtd-refile-to-any-target nil)
        ;;;; These types prompt for refile target
        (setopt org-gtd-refile-prompt-for-types
                '(single-action
                  project-heading
                  project-task
                  ;; calendar
                  someday
                  delegated
                  tickler
                  ;; habit
                  knowledge
                  quick-action
                  ;; trash
                  ))

        ;;;
        ```

<!--list-separator-->

4.  Клавиатурные сочетания

    -   Файл: `packages/org-gtd/desire.ecd/keybinding.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A package for using GTD with org-mode
        ;;; Key bindings
        ;; https://github.com/Trevoke/org-gtd.el

        ;;; Code:

        ;;;; Global keybindings (work anywhere in Emacs)
        (general-define-key
         :prefix "C-c d"
         "c" #'("Capture" . org-gtd-capture)
         "e" #'("Engage" . org-gtd-engage)
         "p" #'("Process inbox" . org-gtd-process-inbox)
         "n" #'("Show all next". org-gtd-show-all-next)
         "s" #'("Stuck projects" . org-gtd-reflect-stuck-projects)
         "." #'("Command Center" . org-gtd-command-center))


        ;;;; Keybinding for organizing items (only works in clarify buffers)
        (with-eval-after-load 'org-gtd
          (general-define-key
           :keymaps 'org-gtd-clarify-map
           :prefix "C-c"
           "c" #'("Organize this item" . org-gtd-organize)))

        ;;;; Quick actions on tasks in agenda views (optional but recommended)
        (with-eval-after-load 'org-agenda
          (general-define-key
           :keymaps 'org-agenda-mode-map
           :prefix "C-c"
           "." #'("GTD quick actions" . org-gtd-agenda-transient)))

        ;;;
        ```

<!--list-separator-->

5.  Представления

    -   Файл: `packages/org-gtd/desire.ecd/view.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A package for using GTD with org-mode
        ;;; Views
        ;; https://github.com/Trevoke/org-gtd.el

        ;;; Code:

        (defun org-gtd-engage-view-spec ()
          "Return GTD view specification for the engage view.
        Shows:
        ​- Calendar day view (Calendar + Habit items with timestamps for today)
        ​- Tickler items due today
        ​- Delegated items with check-ins due today
        ​- All next actions
        ​+ Other"
          `((name . "GTD Engage View")
            ;; (prefix . (project area-of-focus "—"))
            (prefix-width . ,org-gtd-prefix-width)
            (blocks . (
                       ((name . "Weekly Agenda")
                        (view-type . agenda)
                        (agenda-span . 1))
                       ;; ((name . "Today's Schedule")
                       ;;  (block-type . calendar-day))
                       ((name . "Overdue events")
                        (type . calendar)
                        (when . past))
                       ((name . "Overdue habits")
                        (type . habit)
                        (when . past))
                       ;; ((name . "Past")
                       ;; 	(type . next-action)
                       ;; 	(scheduled . past)
                       ;; 	(deadline . past))
                       ;; ((name . "Daily Agenda")
                       ;; 	(view-type . agenda)
                       ;; 	(agenda-span . 1))
                       ;; ((name . "Future Habits")
                       ;; 	(type . habit)
                       ;; 	(when . future))
                       ;; ((name . "High Priority")
                       ;; 	(type . next-action)
                       ;; 	(priority . A))
                       ((name . "Important Tasks")
                        (type . next-action)
                        (priority . (>= B)))
                       ((name . "Quick Work")
                        (type . next-action)
                        (effort . (<= "30min")))
                       ((name . "All actions ready to be executed")
                        (type . next-action)
                         (not-habit . t))
                       ((name . "Deep in Progress")
                        (type . next-action)
                        (clocked . (> "1:00")))
                       ((name . "Tickler items ready for today")
                        (type . tickler)
                        (when . today))
                       ((name . "Delegated items to check in on today")
                        (type . delegated)
                        (when . today))
                       ((name . "Missed Delegated")
                        (type . delegated)
                        (when . past))
                       ((name . "Active Projects")
                        (type . project))
                       ((name . "Overdue Projects")
                        (type . project)
                        (deadline . past))
                       ((name . "Incubated Projects")
                        (type . incubated-project))
                       ((name . "Stuck Projects")
                        (type . stuck-project))
                       ((name . "Someday/Maybe")
                        (type . someday))
                       ((name . "Completed This Week")
                        (done . past-week))
                       ((name . "Weekly Agenda")
                        (view-type . agenda)
                        (agenda-span . 7))
                        ))))

        ;;;
        ```

<!--list-separator-->

6.  Хуки

    -   Файл: `packages/org-gtd/desire.ecd/hook.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A package for using GTD with org-mode
        ;;; Custom hooks for org-gtd
        ;; https://github.com/Trevoke/org-gtd.el

        ;;; Code:

        (defun ecf/add-effort ()
          "Prompt for effort on single actions and projects."
          (when (org-gtd-organize-type-member-p '(single-action project-heading))
            (call-interactively #'org-set-effort)))

        (defun ecf/add-priority ()
          "Prompt for priority on single actions."
          (when (org-gtd-organize-type-member-p '(single-action))
            (call-interactively #'org-priority)))

        (defun ecf/auto-tag-contexts ()
          "Automatically suggest context tags based on heading keywords."
          (when (org-gtd-organize-type-member-p '(single-action))
            (let* ((heading (downcase (org-get-heading t t t t)))
                   (suggested-tags '()))
              (when (string-match-p "\\(phone\\|call\\)" heading)
                (push "@phone" suggested-tags))
              (when (string-match-p "\\(computer\\|code\\|write\\)" heading)
                (push "@computer" suggested-tags))
              (when (string-match-p "\\(store\\|buy\\|shop\\)" heading)
                (push "@errands" suggested-tags))
              (when suggested-tags
                (message "Suggested contexts: %s" (string-join suggested-tags ", "))))))

        (defun ecf/track-creation-date ()
          "Add CREATED property with current timestamp."
          (unless (org-gtd-organize-type-member-p '(trash quick-action))
            (org-set-property "CREATED"
                              (format-time-string "[%Y-%m-%d %a %H:%M]"))))

        ;; Install hooks
        (setopt org-gtd-organize-hooks
                '(org-gtd-set-area-of-focus    ;; set area first
                  org-set-tags-command         ;; then tags
                  ecf/auto-tag-contexts        ;; suggest context tags
                  ecf/add-effort               ;; estimate effort
                  ;; ecf/add-priority             ;; set priority if needed
                  ecf/track-creation-date))    ;; track when created

        ;;;
        ```

<!--list-separator-->

7.  Персональные настройки

    -   Файл: `packages/org-gtd/personal.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; A package for using GTD with org-mode
        ;; https://github.com/Trevoke/org-gtd.el

        ;;; Code:

        ;;;; Configure org-mode TODO keywords
        ;; All GTD keywords must be in the same sequence
        ;; Standard options like "TODO(t)" or "DONE(d!)" are fine - org-gtd ignores them
        (setopt org-todo-keywords
              '((sequence "TODO(t)" "NEXT(n)" "WAIT(w)" "|" "DONE(d)" "CNCL(c)")))

        ;;;; Map GTD semantic states to your keywords
        (setopt org-gtd-keyword-mapping
              '((todo . "TODO")      ; tasks not ready to act on
                (next . "NEXT")      ; tasks ready to act on immediately
                (wait . "WAIT")      ; tasks blocked or delegated
                (canceled . "CNCL"))) ; tasks that won't be completed

        ;;;; List of strings representing your areas of focus (horizon 2 in GTD)
        (add-to-list 'org-gtd-areas-of-focus "Science" t)
        (add-to-list 'org-gtd-areas-of-focus "Sciadmin" t)
        (add-to-list 'org-gtd-areas-of-focus "Teaching" t)
        (add-to-list 'org-gtd-areas-of-focus "Study" t)
        (add-to-list 'org-gtd-areas-of-focus "Sysadmin" t)
        (add-to-list 'org-gtd-areas-of-focus "Read" t)

        ;;;
        ```


#### <span class="section-num">3.26.9</span> mobileorg {#mobileorg}

```emacs-lisp
(desired 'mobileorg)
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 163:</span>
  rc.packages.el
</div>


#### <span class="section-num">3.26.10</span> org-download {#org-download}

-   [Emacs. Пакет org-download]({{< relref "2025-05-19--emacs-org-download" >}})
-   Объявление пакета:
    ```emacs-lisp
    (desire 'org-download)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 164:</span>
      rc.packages.el
    </div>
-   Подключение пакета:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Drag and drop images to Emacs org-mode
    ;; https://github.com/abo-abo/org-download

    ;;; Code:

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 165:</span>
      packages/org-download/loaddefs.ecf
    </div>
-   Загрузка пакета:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Drag and drop images to Emacs org-mode
    ;; https://github.com/abo-abo/org-download

    ;;; Code:

    (require 'org-download)

    (setopt org-download-timestamp "%Y%m%dT%H%M%S--")
    (setopt org-download-heading-lvl nil)
    (setopt org-download-link-format "[[download:%s]]\n")
    (setopt org-download-annotate-function (lambda (_link) ""))
    (setopt org-download-image-html-width 500)

    (setopt org-download-abbreviate-filename-function
            (lambda (path)
              (if (file-in-directory-p path org-download-image-dir)
                  (file-relative-name path org-download-image-dir)
                path)))

    (setopt org-download-method 'attach)
    (setopt org-download-link-format-function
            (lambda (filename)
              (if (eq org-download-method 'attach)
                  (format "[[attachment:%s]]\n"
                          (org-link-escape
                           (file-relative-name filename (org-attach-dir))))
                ;; Handle non-image files a little differently. Images should be
                ;; inserted as normal with previews. Other files, like pdfs or zips,
                ;; should be linked to, with an icon indicating the type of file.
                (format (concat (unless (image-type-from-file-name filename)
                                  (concat (+org-attach-icon-for filename)
                                          " "))
                                org-download-link-format)
                        (org-link-escape
                         (funcall org-download-abbreviate-filename-function filename))))))

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 166:</span>
      packages/org-download/desire.ecf
    </div>
-   Настройка для скриншотов:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Drag and drop images to Emacs org-mode
    ;; https://github.com/abo-abo/org-download

    ;;; Code:

    (setopt org-download-screenshot-method
            (cond (IS-MAC "screencapture -i %s")
                  (IS-LINUX
                   (cond ((executable-find "grim") "grim -g \"$(slurp)\" %s")
                         ((executable-find "flameshot") "flameshot gui --raw > %s")
                         ((executable-find "maim") "maim -s %s")
                         ((executable-find "scrot") "scrot -s %s")
                         ((executable-find "gnome-screenshot") "gnome-screenshot -a -f %s")))))

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 167:</span>
      packages/org-download/desire.ecd/screenshot.ecf
    </div>

<!--list-separator-->

1.  Org-mode

    -   Настройки для org-mode:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Drag and drop images to Emacs org-mode
        ;; https://github.com/abo-abo/org-download

        ;;; Code:

        (add-hook 'org-mode-hook 'org-download-enable)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 168:</span>
          packages/org/org-download.ecf
        </div>

<!--list-separator-->

2.  Dired

    -   Настройки для dired:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Drag and drop images to Emacs org-mode
        ;; https://github.com/abo-abo/org-download

        ;;; Code:

        ;;;; Drag-and-drop to `dired`
        (add-hook 'dired-mode-hook 'org-download-enable)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 169:</span>
          packages/dired/org-download.ecf
        </div>


#### <span class="section-num">3.26.11</span> org-mode {#org-mode}

-   Собственно org-mode.
-   [Org-mode]({{< relref "2021-10-14-org-mode" >}})
-   Подключение:
    ```emacs-lisp
    (desire 'org)

    ;;; For messaging
    ;; (desire 'org-msg)

    ;;;}}}
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 170:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Org mode

    ;;; Code:
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 171:</span>
      packages/org/loaddefs.ecf
    </div>

-   Список расширений для моды:
    ```emacs-lisp
    (add-to-list 'auto-mode-alist '("\\.\\(org\\|org_archive\\|txt\\)$" . org-mode))
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 172:</span>
      packages/org/loaddefs.ecf
    </div>

-   Клавиатурные комбинации:
    ```emacs-lisp
    (global-set-key (kbd "C-c a") #'("Agenda" . org-agenda))
    (global-set-key (kbd "C-c d e") #'("Engage" . org-gtd-engage))
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 173:</span>
      packages/org/loaddefs.ecf
    </div>

-   Завершение файла:
    ```emacs-lisp
    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 174:</span>
      packages/org/loaddefs.ecf
    </div>

<!--list-separator-->

1.  Экспорт

    -   Экспорт из org-mode.
    -   Файл: `packages/org/desire.ecd/ox.ecf`

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-


    ;;; Code:

    ;;;; Publishing and Exporting

    (setopt org-alphabetical-lists t)

                                            ; Allow binding variables on export without confirmation
    (setopt org-export-allow-bind t)
    (setopt org-export-allow-bind-keywords t)

    ;;;; Set the default export scope to subtree
    (setf org-export-initial-scope 'subtree)

    ;;;; Toggle TeX-like syntax for sub- and superscripts
    (setopt org-export-with-sub-superscripts '{})

    ;; Explicitly load required exporters

    ;; HTML
    (desire 'htmlize)
    (require 'ox-html)
                                            ; Export HTML without XML header
    (setopt org-html-xml-declaration (quote (("html" . "")
                                             ("was-html" . "<?xml version=\"1.0\" encoding=\"%s\"?>")
                                             ("php" . "<?php echo \"<?xml version=\\\"1.0\\\" encoding=\\\"%s\\\" ?>\"; ?>"))))

    ;;
    (require 'ox)
    (require 'ox-ascii)
    (require 'ox-md)
                                            ;(require 'ox-man)
    (require 'ox-odt)
    (require 'ox-publish)

    ;;;; Allow exporting with 'allegedly' broken links
    (setopt org-export-with-broken-links t)

    ;;(setopt org-export-with-entities nil)


    ;;;; Set export directory
    ;; (setopt exported-org-files-dir (concat org-directory "/export/"))
    ;; (if (not (file-directory-p exported-org-files-dir))
    ;;     (make-directory exported-org-files-dir t))

    ;; (defun org-export-output-file-name-modified (orig-fun extension &optional subtreep pub-dir)
    ;;   (unless pub-dir
    ;;     (setopt pub-dir exported-org-files-dir)
    ;;     (unless (file-directory-p pub-dir)
    ;;       (make-directory pub-dir)))
    ;;   (apply orig-fun extension subtreep pub-dir nil))
    ;; (advice-add 'org-export-output-file-name :around #'org-export-output-file-name-modified)
    ```

    -   [Org-mode. Экспорт ссылок на видео в Hugo]({{< relref "2025-07-03--org-mode-video-export-hugo" >}})

    <!--listend-->

    ```emacs-lisp
    ;;;; Export macros
    (setq org-export-global-macros
          '(
            ("youtube" . "(eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat \"@@hugo:{{</* youtube \" $1 \" */>}}@@\")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat \"@@html:[![Youtube](http://img.youtube.com/vi/\" $1 \"/0.jpg){width=560px}](http://www.youtube.com/watch?v=\" $1 \")@@\"))))")
            ("rutube" . "(eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat \"@@hugo:{{</* rutube \" $1 \" */>}}@@\")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat \"@@html:[![RuTube](\" $2 \"){width=560px}](https://rutube.ru/video/\" $1 \"/)@@\"))))")
            ("plvideo" . "(eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat \"@@hugo:{{</* plvideo \" $1 \" */>}}@@\")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat \"@@html:[![Платформа](\" $2 \"){width=560px}](https://plvideo.ru/watch?v=\" $1 \")@@\"))))")
            ("vkvideo" . "(eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat \"@@hugo:{{</* vkvideo oid=\" $1 \" id=\" $2 \" hd=2 */>}}@@\")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat \"@@html:[![VKvideo](\" $3 \"){width=560px}](https://vkvideo.ru/video\" $1 \"_\" $2 \")@@\"))))")
            ("begin_tabs" . "@@hugo:{{</* tabs $1 */>}}@@")
            ("end_tabs" . "@@hugo:{{</* /tabs */>}}@@")
            ("youtube-tab" . "@@hugo:{{</* tab \"Youtube\" */>}}@@{{{youtube($1)}}}@@hugo:{{</* /tab */>}}@@")
            ("rutube-tab" . "@@hugo:{{</* tab \"RuTube\" */>}}@@{{{rutube($1,$2)}}}@@hugo:{{</* /tab */>}}@@")
            ("plvideo-tab" . "@@hugo:{{</* tab \"Платформа\" */>}}@@{{{plvideo($1,$2)}}}@@hugo:{{</* /tab */>}}@@")
            ("vkvideo-tab" . "@@hugo:{{</* tab \"VKvideo\" */>}}@@{{{vkvideo($1,$2,$3)}}}@@hugo:{{</* /tab */>}}@@")))

    ;;;
    ```

<!--list-separator-->

2.  org-imgtog

    -   <https://github.com/gaoDean/org-imgtog>
    -   Отключение предпромотра избражения.
    -   Файл: `packages/org/desire.ecd/org-imgtog.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Automatic inline image toggling as the cursor enters and exits them
        ;; https://github.com/gaoDean/org-imgtog

        ;;; Code:

        (desire 'org-imgtog :recipe '(:fetcher github :repo "gaoDean/org-imgtog" :branch "main"))

        ;;;; Wait 0.5 seconds before toggling
        (setopt org-imgtog-preview-delay 0.5)
        ;;;; Only delay for remote images
        (setopt org-imgtog-preview-delay-only-remote t)

        (add-hook 'org-mode-hook 'org-imgtog-mode)

        ;;;
        ```

<!--list-separator-->

3.  org-remoteimg

    -   <https://github.com/gaoDean/org-remoteimg>
    -   Отображение удаленных встроенных изображений в org-режиме с автоматическим кэшированием.
    -   Файл: `packages/org/desire.ecd/org-remoteimg.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Display remote inline images in org-mode with automatic caching
        ;; https://github.com/gaoDean/org-remoteimg

        ;;; Code

        (desire 'org-remoteimg :recipe '(:fetcher github :repo "gaoDean/org-remoteimg" :branch "main"))

        ;;;; Enable caching
        (setopt org-display-remote-inline-images 'cache)
        ;;;; or this if you don't want caching
        ;; (setopt org-display-remote-inline-images 'download)
        ;;;; or this if you want to disable this plugin
        ;; (setopt org-display-remote-inline-images 'skip)

        ;;;
        ```

<!--list-separator-->

4.  org-habit-ng

    -   Файл: `packages/org/org-habit-ng.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Org-habit-ng lets you schedule habits that org-mode's standard repeaters can't express
        ;; https://codeberg.org/Trevoke/org-habit-ng

        ;;; Code:

        (require 'transient)
        (require 'org-habit-ng)

        ;;;
        ```


#### <span class="section-num">3.26.12</span> Предпросмотр LaTeX {#предпросмотр-latex}

-   [Org-mode. Предпросмотр TeX]({{< relref "2024-01-06-org-mode-latex-preview" >}})
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Previewing LaTeX fragments
    ;;; https://orgmode.org/manual/Previewing-LaTeX-fragments.html
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 175:</span>
      packages/org/desire.ecd/preview-latex.ecf
    </div>
-   Зададим каталог для создаваемых изображений (по умолчанию они создаются в рабочем каталоге):
    ```emacs-lisp
    ;;; LaTeX image directory
    (setopt org-preview-latex-image-directory (concat home-cache-path "org-latex/"))
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 176:</span>
      packages/org/desire.ecd/preview-latex.ecf
    </div>
-   Зададим опции создания изображений:
    ```emacs-lisp
    ;;; Output format
    (setopt org-format-latex-options (plist-put org-format-latex-options :scale 1.0))
    (setopt org-format-latex-options (plist-put org-format-latex-options :density 600))
    (setopt org-format-latex-options (plist-put org-format-latex-options :background "Transparent"))
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 177:</span>
      packages/org/desire.ecd/preview-latex.ecf
    </div>
-   Зададим формат изображений. В данном случае это формат `svg`:
    ```emacs-lisp
    (setopt org-latex-create-formula-image-program 'dvisvgm)

    (setopt org-preview-latex-process-alist
            '((dvipng :programs ("latex" "dvipng") :description "dvi > png"
                      :message
                      "you need to install the programs: latex and dvipng."
                      :image-input-type "dvi" :image-output-type "png"
                      :image-size-adjust (1.0 . 1.0) :latex-compiler
                      ("latex -interaction nonstopmode -output-directory %o %f")
                      :image-converter ("dvipng -D %D -T tight -o %O %f")
                      :transparent-image-converter
                      ("dvipng -D %D -T tight -bg Transparent -o %O %f"))
              (dvisvgm :programs ("xelatex" "dvisvgm") :description "xdv > svg"
                       :message
                       "you need to install the programs: latex and dvisvgm."
                       :image-input-type "xdv" :image-output-type "svg"
                       :image-size-adjust (1.7 . 1.5) :latex-compiler
                       ("xelatex --no-pdf -interaction nonstopmode -output-directory %o %f")
                       :image-converter
                       ("dvisvgm %f --no-fonts --exact-bbox --scale=%S --output=%O"))
              (imagemagick :programs ("xelatex" "convert") :description "pdf > png"
                           :message
                           "you need to install the programs: latex and imagemagick."
                           :image-input-type "pdf" :image-output-type "png"
                           :image-size-adjust (1.0 . 1.0) :latex-compiler
                           ("xelatex -interaction nonstopmode -output-directory %o %f")
                           :image-converter
                           ("convert -density %D -trim -antialias %f -quality 100 %O"))))
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 178:</span>
      packages/org/desire.ecd/preview-latex.ecf
    </div>
-   Теперь зададим настройки для LaTeX:
    ```emacs-lisp
    ;;; Configure latex
    (setopt org-latex-inputenc-alist '(("utf8" . "utf8x")))
    ;;; Default position for LaTeX figures
    (setopt org-latex-default-figure-position "!htbp")
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 179:</span>
      packages/org/desire.ecd/preview-latex.ecf
    </div>
-   Опишем используемые пакеты:
    ```emacs-lisp
    ;;; Unicode fonts
    (add-to-list 'org-latex-packages-alist '("" "unicode-math") t)
    ;;; Physics2 package
    ;; (add-to-list 'org-latex-packages-alist '("" "physics2") t)
    ;;; Math
    (add-to-list 'org-latex-packages-alist '("" "amsmath") t)
    (add-to-list 'org-latex-packages-alist '("" "mathtools") t)
    ;;; Local definitions
    ;; (add-to-list 'org-latex-packages-alist '("" "local-define") t)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 180:</span>
      packages/org/desire.ecd/preview-latex.ecf
    </div>


#### <span class="section-num">3.26.13</span> Преобразование markdown ←→ org через буфер обмена {#преобразование-markdown-org-через-буфер-обмена}

-   [Emacs. Markdown в Org с помощью буфера обмена]({{< relref "2026-01-02--emacs-markdown-org-clipboard" >}})
-   Файл: `packages/org/desire.ecd/markdown-org-clipboard.ecf`
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Import Markdown to Org with the Clipboard

    ;;; Code:

    (defun ecf/yank-markdown-as-org ()
      "Yank Markdown text as Org.

    This command will convert Markdown text in the top of the `kill-ring'
    and convert it to Org using the pandoc utility."
      (interactive)
      (save-excursion
        (with-temp-buffer
          (yank)
          (shell-command-on-region
           (point-min) (point-max)
           "pandoc -f gfm -t org --wrap=preserve" t t)
          (kill-region (point-min) (point-max)))
        (yank)))

    (defun ecf/org-copy-region-as-markdown ()
      "Copy the region (in Org) to the system clipboard as Markdown."
      (interactive)
      (if (use-region-p)
          (let* ((region
                  (buffer-substring-no-properties
                          (region-beginning)
                          (region-end)))
                 (markdown
                  (org-export-string-as region 'md t '(:with-toc nil))))
            (gui-set-selection 'CLIPBOARD markdown))))

    ;;;
    ```


### <span class="section-num">3.27</span> Заметочники {#заметочники}

-   [Emacs. Персональная база знаний]({{< relref "2023-11-07-emacs-personal-knowledge-base" >}})
-   Разные заметочники:
    ```emacs-lisp
    ;;; Notes
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 181:</span>
      rc.packages.el
    </div>


#### <span class="section-num">3.27.1</span> Инфраструктура Org-roam {#инфраструктура-org-roam}

```emacs-lisp
;;;;; Org-roam

(desire 'emacsql)

;; (desire 'delve :recipe '(:fetcher github :repo "publicimageltd/delve" :branch "main"))
```

<!--list-separator-->

1.  Zetteldesk

    <!--list-separator-->

    1.  Подключение

        -   Файл: `rc.packages.el`

        <!--listend-->

        ```emacs-lisp
        (desire 'zetteldesk)
        ```

    <!--list-separator-->

    2.  Включение

        -   Файл: `packages/zetteldesk/loaddefs.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Zetteldesk.el is an emacs library built on top of org-roam with the purpose of easier revision on various subjects and a better outliner tool for emacs
        ;; https://github.com/Vidianos-Giannitsis/zetteldesk.el

        ;;; Code:

        (desire 'zetteldesk-kb)
        (desire 'zetteldesk-info)
        (desire 'zetteldesk-ref)
        (desire 'zetteldesk-kb)
        (desire 'zetteldesk-remark)

        ;;;
        ```

    <!--list-separator-->

    3.  Загрузка

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Zetteldesk.el is an emacs library built on top of org-roam with the purpose of easier revision on various subjects and a better outliner tool for emacs
        ;; https://github.com/Vidianos-Giannitsis/zetteldesk.el

        ;;; Code:

        (require 'zetteldesk)

        (setopt zetteldesk-kb-hydra-prefix (kbd "C-c z"))

        (zetteldesk-mode 1)

        (require 'zetteldesk-ref)
        (require 'zetteldesk-info)
        (require 'zetteldesk-remark)

        ;;;
        ```

    <!--list-separator-->

    4.  Интеграция с org-roam

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Zetteldesk.el is an emacs library built on top of org-roam with the purpose of easier revision on various subjects and a better outliner tool for emacs
        ;; https://github.com/Vidianos-Giannitsis/zetteldesk.el

        ;;; Code:

        (require 'zetteldesk)

        ;;;
        ```

<!--list-separator-->

2.  Org-roam-ui

    <!--list-separator-->

    1.  Подключение

        -   Файл: `rc.packages.el`

        <!--listend-->

        ```emacs-lisp
        (desire 'org-roam-ui :recipe '(:fetcher github :repo "lkarp-744/org-roam-ui"))
        ;; (desire 'org-roam-ui :recipe '(:fetcher github :repo "lkarp-744/org-roam-ui" :files ("*.el" "public")))
        ;; (desire 'org-roam-ui)
        ```

<!--list-separator-->

3.  Org-roam

    -   Файл: `rc.packages.el`

    <!--listend-->

    ```emacs-lisp
    (desire 'magit-section)
    (desire 'org-roam)
    ```

    <!--list-separator-->

    1.  Дополнительные пакеты

        <!--list-separator-->

        1.  nursery

            -   <https://github.com/chrisbarrett/nursery>
            -   Файл: packages/org-roam/desire.ecd/nursery.ecf
            -   Заголовок:

            <!--listend-->

            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Small org-roam packages
            ;; https://github.com/chrisbarrett/nursery

            ;;; Code:
            ```

            -   org-roam-review

            <!--listend-->

            ```emacs-lisp
            ;;;; Extends org-roam with spaced-repetition review of nodes
            ;; https://github.com/chrisbarrett/nursery/blob/main/lisp/org-roam-review.el

            (desire 'org-drill)

            ;;;;; Provides commands to categorise and review org-roam nodes for Evergreen note-taking
            (desire 'org-roam-review :pkgman 'straight :recipe '(:type git :host github :repo "chrisbarrett/nursery" :branch "main" :files ("lisp/org-roam-review.el" "lisp/org-tags-filter.el" "lisp/plisty.el")))

            (require 'org-roam-review)

            ;;;;; Tag all newly-created notes as seedlings
            ;;;;; https://github.com/chrisbarrett/nursery/issues/7
            (defun ecf/org-roam-review-set-seedling ()
              (with-current-buffer (org-capture-get :buffer)
                (org-roam-review-set-seedling)))
            (add-hook 'org-capture-after-finalize-hook #'ecf/org-roam-review-set-seedling)

            ;;;;; Keybindings for applying Evergreen note properties
            (general-define-key
             :prefix "C-c r"
             "r" #'("accept" . org-roam-review-accept)
             "f" #'("forgot" . org-roam-review-forgot)
             "u" #'("bury" . org-roam-review-bury)
             "m" #'("set memorise" . org-roam-review-set-memorise)
             "x" #'("set excluded" . org-roam-review-set-excluded)
             "b" #'("set budding" . org-roam-review-set-budding)
             "s" #'("set seedling" . org-roam-review-set-seedling)
             "e" #'("set evergreen" . org-roam-review-set-evergreen))

            ;;;;; Ignore tags when export
            (with-eval-after-load 'ox-hugo
              (add-to-list 'ecf/tags-categories-to-be-removed "seedling")
              (add-to-list 'ecf/tags-categories-to-be-removed "evergreen")
              (add-to-list 'ecf/tags-categories-to-be-removed "budding"))
            ```

            -   Разные пакеты:
                ```emacs-lisp
                ;;;;; Renaming nodes, rewriting links and deleting nodes with redirection
                (desire 'org-transclusion)

                (desire 'org-roam-rewrite :pkgman 'straight :recipe '(:type git :host github :repo "chrisbarrett/nursery" :branch "main" :files ("lisp/org-roam-rewrite.el" "lisp/plisty.el")))
                (require 'org-roam-rewrite)

                ;;;; Display a tree of backlinks and forward links up to a configurable depth
                (desire 'org-roam-links :pkgman 'straight :recipe '(:type git :host github :repo "chrisbarrett/nursery" :branch "main" :files ("lisp/org-roam-links.el" "lisp/plisty.el")))
                (require 'org-roam-links)

                ;;;; Make previews in org-roam buffer lazy for better performance
                (desire 'org-roam-lazy-previews :pkgman 'straight :recipe '(:type git :host github :repo "chrisbarrett/nursery" :branch "main" :files ("lisp/org-roam-lazy-previews.el")))
                (require 'org-roam-lazy-previews)

                ;;;; Refill org-roam backlink previews
                (desire 'org-roam-refill-previews :pkgman 'straight :recipe '(:type git :host github :repo "chrisbarrett/nursery" :branch "main" :files ("lisp/org-roam-refill-previews.el")))
                (require 'org-roam-refill-previews)

                (add-hook 'org-roam-preview-postprocess-functions #'org-roam-refill-previews)

                ;;;
                ```

<!--list-separator-->

4.  Org-daily

    -   Загрузка:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Daily-notes

        ;;; Code:

        (require 'org-roam-dailies)

        ;;;; Excluding Nodes and Edges
        (setopt org-roam-graph-exclude-matcher '("private" "dailies"))
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 182:</span>
          packages/org-roam/desire.ecd/dailies.ecf
        </div>
    -   Каталог для записей:
        ```emacs-lisp
        ;;;; Path to daily-notes
        (setopt org-roam-dailies-directory "daily/")
        (unless (file-directory-p (concat org-roam-directory "/" org-roam-dailies-directory))
          (make-directory (concat org-roam-directory "/" org-roam-dailies-directory) t))
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 183:</span>
          packages/org-roam/desire.ecd/dailies.ecf
        </div>
    -   Шаблон записи:
        ```emacs-lisp
        ;;;; Capture templates for daily-notes in Org-roam
        (setopt org-roam-dailies-capture-templates
              '(("d" "default" entry
                 "* %?"
                 :target (file+head "%<%Y-%m-%d>.org"
                                    "#+title: %<%Y-%m-%d>
        :SETUP_LOCAL:
        #+startup: overview num inlineimages latexpreview
        #+options: ^:{} num:t tex:t
        :END:

        "))))
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 184:</span>
          packages/org-roam/desire.ecd/dailies.ecf
        </div>
    -   Сочетания клавиш:
        ```emacs-lisp
        ;;;; Define key bindings

        ;;;;; Capture a note for today (C-c n d n)
        (define-key org-roam-dailies-map (kbd "n") #'org-roam-dailies-capture-today)

        ;;;;; Capture a note for yesterday (C-c n d Y)
        (define-key org-roam-dailies-map (kbd "Y") #'org-roam-dailies-capture-yesterday)

        ;;;;; Capture a note for tomorrow (C-c n d T)
        (define-key org-roam-dailies-map (kbd "T") #'org-roam-dailies-capture-tomorrow)

        ;;;;; Go to the file for yesterday (C-c n d y)
        (define-key org-roam-dailies-map (kbd "y") #'org-roam-dailies-goto-yesterday)

        ;;;;; Go to the file for tomorrow (C-c n d t)
        (define-key org-roam-dailies-map (kbd "t") #'org-roam-dailies-goto-tomorrow)

        ;;;;; Capture a note for a specific date (C-c n d v)
        (define-key org-roam-dailies-map (kbd "v") #'org-roam-dailies-capture-date)

        ;;;;; Go to the file for a specific date (C-c n d c)
        (define-key org-roam-dailies-map (kbd "c") #'org-roam-dailies-goto-date)

        ;;;;; Go back one existing date file (C-c n d b)
        (define-key org-roam-dailies-map (kbd "b") #'org-roam-dailies-goto-next-note)

        ;;;;; Go forward one existing date file (C-c n d f)
        (define-key org-roam-dailies-map (kbd "f") #'org-roam-dailies-goto-previous-note)

        (fset 'org-roam-dailies-map org-roam-dailies-map)
        (global-set-key (kbd "C-c n d") #'org-roam-dailies-map)

        ;; (global-set-key (kbd "C-c n d") #'org-roam-dailies-capture-today)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 185:</span>
          packages/org-roam/desire.ecd/dailies.ecf
        </div>

<!--list-separator-->

5.  org-daily-reflection

    -   [Emacs. Пакет org-daily-reflection]({{< relref "2025-06-06--emacs-org-daily-reflection" >}})
    -   Загрузка.
        ```emacs-lisp
        ;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Reflect on your org-roam daily entries, comparing N org-roam dailies at M intervals
        ;; https://github.com/emacsomancer/org-daily-reflection

        ;;; Code:

        (desire 'org-daily-reflection)
        (require 'org-daily-reflection)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 186:</span>
          packages/org-roam/desire.ecd/org-daily-reflection.ecf
        </div>


#### <span class="section-num">3.27.2</span> Denote {#denote}

```emacs-lisp

;; (desire 'deft)
;; (desire-conf 'zetteldeft nil "zetteldeft" t)

;; (desire 'denote)

;;}}}
```


### <span class="section-num">3.28</span> Диаграммы {#диаграммы}


#### <span class="section-num">3.28.1</span> Диаграммы Ганта {#диаграммы-ганта}

-   [Emacs. Диаграммы Ганта]({{< relref "2024-12-10-emacs-gantt-charts" >}})

<!--list-separator-->

1.  org-gantt-mode

    -   Добавим пакет:
        ```emacs-lisp
        ;; (desire 'org-gantt-mode :recipe '(:fetcher gitlab :repo "joukeHijlkema/org-gantt-mode" :branch "master"))
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 187:</span>
          rc.packages.el
        </div>
    -   Загрузка пакета:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Create SVG gantt charts from an org-mode subtree
        ;;; https://gitlab.com/joukeHijlkema/org-gantt-mode

        (desire 'ts)

        (autoload 'org-gantt-mode "org-gantt-mode" "Create SVG gantt charts" t)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 188:</span>
          packages/org-gantt-mode.ecf
        </div>

<!--list-separator-->

2.  elgantt

    -   Добавим пакет:
        ```emacs-lisp
        (desire 'elgantt :recipe '(:fetcher github :repo "legalnonsense/elgantt" :branch "master"))
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 189:</span>
          rc.packages.el
        </div>
    -   Загрузка пакета:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;;  A Gantt Chart (Calendar) for Org Mode
        ;;; https://github.com/legalnonsense/elgantt

        (require 'elgantt)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 190:</span>
          packages/elgantt/loaddefs.ecf
        </div>

<!--list-separator-->

3.  taskjuggler

    -   Загрузка пакета:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;;  Exporting Gantt charts with Taskjuggler
        ;; https://github.com/h-oll/ox-taskjuggler

        ;;; Code:

        ;; (desire 'ox-taskjuggler :recipe '(:fetcher github :repo "h-oll/ox-taskjuggler" :branch "master"))
        (desire 'ox-taskjuggler :pkgman 'straight :recipe '(:type git :host github :repo "h-oll/ox-taskjuggler" :branch "master" :files ("lisp/*")))
        (require 'ox-taskjuggler)

        ;;;; Report width

        (setopt org-taskjuggler-default-reports
          '("textreport report \"Plan\" {
          formats html
          header '== %title =='

          center -8<-
            [#Plan Plan] | [#Resource_Allocation Resource Allocation]
            ----
            === Plan ===
            <[report id=\"plan\"]>
            ----
            === Resource Allocation ===
            <[report id=\"resourceGraph\"]>
          ->8-
        }

        # A traditional Gantt chart with a project overview.
        taskreport plan \"\" {
          headline \"Project Plan\"
          columns bsi, name, start, end, effort, chart { width 1000 }
          loadunit shortauto
          hideresource 1
        }

        # A graph showing resource allocation. It identifies whether each
        # resource is under- or over-allocated for.
        resourcereport resourceGraph \"\" {
          headline \"Resource Allocation Graph\"
          columns no, name, effort, weekly { width 1000 }
          loadunit shortauto
          hidetask ~(isleaf() & isleaf_())
          sorttasks plan.start.up
        }"))

        ;;;; Some tweaks
        (setopt org-taskjuggler-default-project-duration 999)
        (setopt org-taskjuggler-valid-task-attributes
                '(account start note duration endbuffer endcredit end
                          flags journalentry length limits maxend maxstart minend
                          minstart period reference responsible scheduling
                          startbuffer startcredit statusnote chargeset charge booking))



        ;;;; precedes
        (defun org-taskjuggler-resolve-precedes (task info)
          "Return a list of all tasks TASK precedes on.
        TASK is a headline.  INFO is a plist used as a communication
        channel."
          (let ((precs-ids
                 ;; Get all dependencies specified in BLOCKER and PRECEDES task
                 ;; properties.  Clean options from them.
                 (let ((precs (concat (org-element-property :BLOCKER task)
                                     (org-element-property :PRECEDES task))))
                   (and precs
                        (split-string (replace-regexp-in-string "{.*?}" "" precs)
                                      "[ ,]* +"))))
                precedes)
            (when precs-ids
              ;; Find tasks with :task_id: property matching id in PRECS-IDS.
              ;; Add them to PRECEDES.
              (let* ((project (org-taskjuggler-get-project info))
                     (tasks (if org-taskjuggler-keep-project-as-task project
                              (org-element-contents project))))
                (setq precedes
                      (org-element-map tasks 'headline
                        (lambda (task)
                          (let ((task-id (or (org-element-property :TASK_ID task)
                                             (org-element-property :ID task))))
                            (and task-id (member task-id precs-ids) task)))
                        info)))
              ;; Check BLOCKER and PRECEDES properties.  If "previous-sibling"
              ;; belongs to PRECS-ID, add it to PRECEDES.
              ;; (when (and (member-ignore-case "previous-sibling" precs-ids)
              ;;            (not (org-export-first-sibling-p task info)))
              ;;   (let ((prev (org-export-get-previous-element task info)))
              ;;     (and (not (memq prev precedes)) (push prev precedes))))
              )
            ;; Check ORDERED status of parent.
            ;; (let ((parent (org-export-get-parent task)))
            ;;   (when (and parent
            ;;              (org-element-property :ORDERED parent)
            ;;              (not (org-export-first-sibling-p task info)))
            ;;     (push (org-export-get-previous-element task info) precedes)))
            ;; Return dependencies.
            precedes))

        (defun org-taskjuggler-format-precedes (precedes task info)
          "Format PRECEDES to match TaskJuggler syntax.
        PRECEDES is list of precedes for TASK, as returned by
        `org-taskjuggler-resolve-depedencies'.  TASK is a headline.
        INFO is a plist used as a communication channel.  Return value
        doesn't include leading \"precedes\"."
          (let* ((dep-str (concat (org-element-property :BLOCKER task)
                                  " "
                                  (org-element-property :PRECEDES task)))
                 (get-path
                  (lambda (dep)
                    ;; Return path to DEP relatively to TASK.
                    (let ((parent (org-export-get-parent task))
                          (exclamations 1)
                          (option
                           (let ((id (org-element-property :TASK_ID dep)))
                             (and id
                                  (string-match (concat id " +\\({.*?}\\)") dep-str)
                                  (match-string-no-properties 1 dep-str))))
                          path)
                      ;; Compute number of exclamation marks by looking for the
                      ;; common ancestor between TASK and DEP.
                      (while (not (org-element-map parent 'headline
                                  (lambda (hl) (eq hl dep))))
                        (cl-incf exclamations)
                        (setq parent (org-export-get-parent parent)))
                      ;; Build path from DEP to PARENT.
                      (while (not (eq parent dep))
                        (push (org-taskjuggler-get-id dep info) path)
                        (setq dep (org-export-get-parent dep)))
                      ;; Return full path.  Add dependency options, if any.
                      (concat (make-string exclamations ?!)
                              (mapconcat 'identity path ".")
                              (and option (concat " " option)))))))
            ;; Return precedes string, without the leading "precedes".
            (mapconcat (lambda (dep) (funcall get-path dep)) precedes ", ")))

        (defun org-taskjuggler--build-task (task info)
          "Return a task declaration.

        TASK is a headline.  INFO is a plist used as a communication
        channel.

        All valid attributes from TASK are inserted.  If TASK defines
        a property \"task_id\" it will be used as the id for this task.
        Otherwise it will use the ID property.  If neither is defined
        a unique id will be associated to it."
          (let* ((allocate (org-element-property :ALLOCATE task))
                 (complete
                  (if (eq (org-element-property :todo-type task) 'done) "100"
                    (org-element-property :COMPLETE task)))
                 (depends (org-taskjuggler-resolve-dependencies task info))
                 (precedes (org-taskjuggler-resolve-precedes task info))
                 (effort (let ((property
                                (intern (concat ":" (upcase org-effort-property)))))
                           (org-element-property property task)))
                 (milestone
                  (or (org-element-property :MILESTONE task)
                      (not (or (org-element-map (org-element-contents task) 'headline
                                 'identity info t)  ; Has task any child?
                               effort
                               (org-element-property :LENGTH task)
                               (org-element-property :DURATION task)
                               (and (org-taskjuggler-get-start task)
                                    (org-taskjuggler-get-end task))
                               (org-element-property :PERIOD task)))))
                 (priority
                  (let ((pri (org-element-property :priority task)))
                    (and pri
                         (max 1 (/ (* 1000 (- org-priority-lowest pri))
                                   (- org-priority-lowest org-priority-highest)))))))
            (concat
             ;; Opening task.
             (format "task %s \"%s\" {\n"
                     (org-taskjuggler-get-id task info)
                     (org-taskjuggler-get-name task))
             ;; Add default attributes.
             (and depends
                  (format "  depends %s\n"
                          (org-taskjuggler-format-dependencies depends task info)))
             (and precedes
                  (format "  precedes %s\n"
                          (org-taskjuggler-format-precedes precedes task info)))
             (and allocate
                  (format "  purge %s\n  allocate %s\n"
                          ;; Compatibility for previous TaskJuggler versions.
                          (if (>= org-taskjuggler-target-version 3.0) "allocate"
                            "allocations")
                          allocate))
             (and complete (format "  complete %s\n" complete))
             (and effort (format "  effort %s\n" effort))
             (and priority (format "  priority %s\n" priority))
             (and milestone "  milestone\n")
             ;; Add other valid attributes.
             (org-taskjuggler--indent-string
              (org-taskjuggler--build-attributes
               task org-taskjuggler-valid-task-attributes))
             ;; Add inner tasks.
             (org-taskjuggler--indent-string
              (mapconcat 'identity
                         (org-element-map (org-element-contents task) 'headline
                           (lambda (hl) (org-taskjuggler--build-task hl info))
                           info nil 'headline)
                         ""))
             ;; Closing task.
             "}\n")))

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 191:</span>
          packages/org/desire.ecd/ox-taskjuggler.ecf
        </div>


#### <span class="section-num">3.28.2</span> Mermaid {#mermaid}

```emacs-lisp
(desire' mermaid-mode :precondition-system-executable "mmdc")
```


#### <span class="section-num">3.28.3</span> Plantuml {#plantuml}

```emacs-lisp
(desire 'plantuml-mode)
```


### <span class="section-num">3.29</span> Разное {#разное}

```emacs-lisp
;; XML, XHTML, HTML {{{

;;(desire-conf 'nxml nil "rng-auto")
                                      ; (desire-conf 'psgml)

;;;}}}
;;;{{{ Palm pilot support

                                      ;(desire-conf 'palm)

;;;}}}
```


### <span class="section-num">3.30</span> Управление сессиями {#управление-сессиями}

```emacs-lisp
;;; Desktop {{{
```


### <span class="section-num">3.31</span> Сохранение состояния сессий {#сохранение-состояния-сессий}

```emacs-lisp
;; (desire-conf 'desktop)
(desire-conf 'session nil "session")
(desire-conf 'saveplace nil "saveplace")
```


### <span class="section-num">3.32</span> Организация рабочего пространства {#организация-рабочего-пространства}

-   [Emacs. Управление рабочим пространством]({{< relref "2026-02-20--emacs-managing-workspaces" >}})


#### <span class="section-num">3.32.1</span> one-tab-per-project {#one-tab-per-project}

-   [Emacs. Пакет otpp]({{< relref "2025-02-03--emacs-otpp" >}})
-   Автоматическое создание вкладки для каждого проекта, обеспечивающее управление рабочим пространством на основе панели вкладок для Emacs.
-   <https://github.com/abougouffa/one-tab-per-project>
-   Подключение пакета:
    ```emacs-lisp
    (desire 'otpp)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 192:</span>
      rc.packages.el
    </div>
-   Предварительные настройки:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Automatically create a tab per project, providing a light tab-bar based workspace management for Emacs
    ;;;; https://github.com/abougouffa/one-tab-per-project

    ;;; Code:

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 193:</span>
      packages/otpp/loaddefs.ecf
    </div>
-   Загрузка пакета:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Automatically create a tab per project, providing a light tab-bar based workspace management for Emacs
    ;;;; https://github.com/abougouffa/one-tab-per-project

    ;;; Code:

    (require 'otpp)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 194:</span>
      packages/otpp/desire.ecf
    </div>
-   Задание параметров:
    ```emacs-lisp
    ;;;; If you like to define some aliases for better user experience
    (defalias 'one-tab-per-project-mode 'otpp-mode)
    (defalias 'one-tab-per-project-override-mode 'otpp-override-mode)

    ;;;; Keybindings
    (general-define-key
     :prefix "C-x t"
     "D" 'otpp-detach-buffer-to-tab
     "C" 'otpp-change-tab-root-dir
     "P" 'otpp-prefix)

    ;;;; Enable `otpp-mode` globally
    (otpp-mode 1)

    ;;;; If you want to advice the commands in `otpp-override-commands` to be run in the current's tab (so, current project's) root directory
    (otpp-override-mode 1)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 195:</span>
      packages/otpp/desire.ecf
    </div>
-   Подключение к project.el:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Automatically create a tab per project, providing a light tab-bar based workspace management for Emacs
    ;;; https://github.com/abougouffa/one-tab-per-project

    (require 'otpp)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 196:</span>
      packages/project/otpp.ecf
    </div>


#### <span class="section-num">3.32.2</span> iBuffer {#ibuffer}

```emacs-lisp
(desire 'ibuffer)
;; (desire 'persp-mode)
;; (desire 'perspective)
```


#### <span class="section-num">3.32.3</span> tabspaces {#tabspaces}

-   [Emacs. Пакет Tabspaces]({{< relref "2026-02-20--emacs-tabspaces" >}})

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        (desire 'tabspaces)
        ```

<!--list-separator-->

2.  Загрузка

    -   Файл: `packages/tabspaces/loaddefs.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Create buffer-isolated workspaces
        ;; https://github.com/mclear-tools/tabspaces

        ;;; Code:

        (require 'tabspaces)

        ;;;
        ```

<!--list-separator-->

3.  Настройка

    -   Файл: `packages/tabspaces/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Create buffer-isolated workspaces
        ;; https://github.com/mclear-tools/tabspaces

        ;;; Code


        (setopt tabspaces-use-filtered-buffers-as-default t)
        (setopt tabspaces-default-tab "Default")
        (setopt tabspaces-remove-to-default t)
        (setopt tabspaces-include-buffers '("*scratch*"))
        (setopt tabspaces-initialize-project-with-todo t)
        (setopt tabspaces-todo-file-name "project-todo.org")

        ;;;; Enable automatic session saving on Emacs exit
        (setopt tabspaces-session t)
        ;;;; Auto-restore sessions on startup and when opening projects
        (setopt tabspaces-session-auto-restore t)

        ;;;; Save all project tabs to their individual session files
        ;; (tabspaces-save-all-project-sessions)
        ;;;; Save only non-project tabs to the global session file
        ;; (tabspaces-save-non-project-tabs)

        ;;; Use this only if you want the minor-mode loaded at startup
        (tabspaces-mode)

        ;;;; additional options
        (setopt tabspaces-fully-resolve-paths t)  ; Resolve relative project paths to absolute
        (setopt tabspaces-exclude-buffers '("*Messages*" "*Compile-Log*"))  ; Additional buffers to exclude
        (setopt tab-bar-new-tab-choice "*scratch*")

        ;;;
        ```

<!--list-separator-->

4.  Интеграция с consult

    -   Файл: `packages/tabspaces/consult.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Create buffer-isolated workspaces
        ;; https://github.com/mclear-tools/tabspaces

        ;;; Code:

        ;;;; Filter Buffers for Consult-Buffer

        (with-eval-after-load 'consult
          ;; hide full buffer list (still available with "b" prefix)
          (plist-put consult-source-buffer :hidden t)
          (plist-put consult-source-buffer :default nil)
          ;; set consult-workspace buffer list
          (defvar consult--source-workspace
            (list :name     "Workspace Buffers"
                  :narrow   ?w
                  :history  'buffer-name-history
                  :category 'buffer
                  :state    #'consult--buffer-state
                  :default  t
                  :items    (lambda () (consult--buffer-query
                                   :predicate #'tabspaces--local-buffer-p
                                   :sort 'visibility
                                   :as #'buffer-name)))

            "Set workspace buffer list for consult-buffer.")
          (add-to-list 'consult-buffer-sources 'consult--source-workspace))

        ;;;
        ```


#### <span class="section-num">3.32.4</span> bufler {#bufler}

<!--list-separator-->

1.  Подключение

    -   Файл: `rc.packages.el`
        ```emacs-lisp
        ;; (desire 'bufler)
        ```

<!--list-separator-->

2.  Объявление

    -   Файл: `packages/bufler/loaddefs.ecf`

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Group buffers into workspaces with programmable rules
    ;; https://github.com/alphapapa/bufler.el

    ;;; Code:

    (desire' burly)

    (require 'bufler)

    ;;;
    ```

<!--list-separator-->

3.  Настройка

    <!--list-separator-->

    1.  Основной файл

        -   Файл: `packages/bufler/desire.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Group buffers into workspaces with programmable rules
        ;; https://github.com/alphapapa/bufler.el

        ;;; Code:

        (bufler-mode 1)

        ;;;
        ```

    <!--list-separator-->

    2.  Сочетания клавиш

        -   Файл: `packages/bufler/desire.ecd/keybinding.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Group buffers into workspaces with programmable rules
        ;; https://github.com/alphapapa/bufler.el

        ;;; Code:

        (defun ecf/bufler-one-window (&optional force-refresh)
          (interactive "P")
          (bufler-list)
          (delete-other-windows))

        (global-set-key (kbd "C-x C-b") #'ecf/bufler-one-window)

        ;;;
        ```

    <!--list-separator-->

    3.  Группы буферов

        -   Файл: `packages/bufler/desire.ecd/group.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Group buffers into workspaces with programmable rules
        ;; https://github.com/alphapapa/bufler.el

        ;;; Code:

        ;; (setopt bufler-groups
        ;;       (bufler-defgroups
        ;; 	(group
        ;; 	 ;; Subgroup collecting all named workspaces.
        ;; 	 (auto-workspace))
        ;; 	(group
        ;; 	 ;; Subgroup collecting all `help-mode' and `info-mode' buffers.
        ;; 	 (group-or "*Help/Info*"
        ;; 		   (mode-match "*Help*" (rx bos "help-"))
        ;; 		   (mode-match "*Info*" (rx bos "info-"))))
        ;; 	(group
        ;; 	 ;; Subgroup collecting all special buffers (i.e. ones that are not
        ;; 	 ;; file-backed), except `magit-status-mode' buffers (which are allowed to fall
        ;; 	 ;; through to other groups, so they end up grouped with their project buffers).
        ;; 	 (group-and "*Special*"
        ;; 		    (lambda (buffer)
        ;; 		      (unless (or (funcall (mode-match "Magit" (rx bos "magit-status"))
        ;; 					  buffer)
        ;; 				 (funcall (mode-match "Dired" (rx bos "dired"))
        ;; 					  buffer)
        ;; 				 (funcall (auto-file) buffer))
        ;; 			"*Special*")))
        ;; 	 (group
        ;; 	  ;; Subgroup collecting these "special special" buffers
        ;; 	  ;; separately for convenience.
        ;; 	  (name-match "**Special**"
        ;; 		      (rx bos "*" (or "Messages" "Warnings" "scratch" "Backtrace") "*")))
        ;; 	 (group
        ;; 	  ;; Subgroup collecting all other Magit buffers, grouped by directory.
        ;; 	  (mode-match "*Magit* (non-status)" (rx bos (or "magit" "forge") "-"))
        ;; 	  (auto-directory))
        ;; 	 ;; Subgroup for Helm buffers.
        ;; 	 (mode-match "*Helm*" (rx bos "helm-"))
        ;; 	 ;; Remaining special buffers are grouped automatically by mode.
        ;; 	 (auto-mode))
        ;; 	;; All buffers under "~/.emacs.d" (or wherever it is).
        ;; 	(dir user-emacs-directory)
        ;; 	(group
        ;; 	 ;; Subgroup collecting buffers in `org-directory' (or "~/org" if
        ;; 	 ;; `org-directory' is not yet defined).
        ;; 	 (dir (if (bound-and-true-p org-directory)
        ;; 		  org-directory
        ;; 		"~/org"))
        ;; 	 (group
        ;; 	  ;; Subgroup collecting indirect Org buffers, grouping them by file.
        ;; 	  ;; This is very useful when used with `org-tree-to-indirect-buffer'.
        ;; 	  (auto-indirect)
        ;; 	  (auto-file))
        ;; 	 ;; Group remaining buffers by whether they're file backed, then by mode.
        ;; 	 (group-not "*special*" (auto-file))
        ;; 	 (auto-mode))
        ;; 	(group
        ;; 	 ;; Subgroup collecting buffers in a projectile project.
        ;; 	 (auto-projectile))
        ;; 	(group
        ;; 	 ;; Subgroup collecting buffers in a version-control project,
        ;; 	 ;; grouping them by directory.
        ;; 	 (auto-project))
        ;; 	;; Group remaining buffers by directory, then major mode.
        ;; 	(auto-directory)
        ;; 	(auto-mode))
        ;;       )

        ;;;
        ```

<!--list-separator-->

4.  Интеграция

    <!--list-separator-->

    1.  tab-bar

        -   Файл: `packages/bufler/tab-bar.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Group buffers into workspaces with programmable rules
        ;; https://github.com/alphapapa/bufler.el

        ;;; Code:

        (require 'bufler-workspace-tabs)

        ;;;
        ```

    <!--list-separator-->

    2.  helm

        -   Файл: `packages/bufler/helm.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Group buffers into workspaces with programmable rules
        ;; https://github.com/alphapapa/bufler.el

        ;;; Code

        (desire 'helm-bufler)
        (require 'helm-bufler)

        ;;;
        ```


### <span class="section-num">3.33</span> Проекты {#проекты}


#### <span class="section-num">3.33.1</span> Начало {#начало}

```emacs-lisp
;;; Project management
```


#### <span class="section-num">3.33.2</span> projection {#projection}

-   Projectile-подобная библиотека управления проектами для project.el
-   <https://github.com/mohkale/projection>
-   Подключение:
    ```emacs-lisp
    (desire 'projection)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 197:</span>
      rc.packages.el
    </div>
-   Подготовка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Projectile like project management library built on Emacs project.el
    ;;;; https://github.com/mohkale/projection

    ;;; Code:

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 198:</span>
      packages/projection/loaddefs.ecf
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Projectile like project management library built on Emacs project.el
    ;;;; https://github.com/mohkale/projection

    ;;; Code:

    (require 'projection)

    ;;;; Keymap


    ;;;; Enable `projection-hook', adds the possibility to run functions in per-project basis
    (global-projection-hook-mode 1)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 199:</span>
      packages/projection/desire.ecf
    </div>

<!--list-separator-->

1.  Интеграция

    -   Интеграция с `compile-multi`:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Projectile like project management library built on Emacs project.el
        ;;;; https://github.com/mohkale/projection

        ;;; Code:

        (desire 'projection-multi)
        (require 'projection-multi)

        ;;;; Allow interactively selecting available compilation targets from the current project type
        (general-define-key
         :keymaps 'project-prefix-map
         "RET" 'projection-multi-compile)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 200:</span>
          packages/projection/compile-multi.ecf
        </div>
    -   Интеграция с `ibuffer`:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Projectile like project management library built on Emacs project.el
        ;;;; https://github.com/mohkale/projection

        ;;; Code:

        (add-hook 'ibuffer-hook 'ibuffer-projection-set-filter-groups)
        ;;;; This ensures that `ibuffer-projection-set-filter-groups' takes effect
        (add-hook 'ibuffer-hook (lambda () (run-at-time 0.1 nil (lambda () (call-interactively #'ibuffer-update)))))

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 201:</span>
          packages/projection/ibuffer.ecf
        </div>
    -   Загрузка при использовании `project`:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Projectile like project management library built on Emacs project.el
        ;;;; https://github.com/mohkale/projection

        ;;; Code:

        (require 'projection)

        ;;;; Enable `projection-hook', adds the possibility to run functions in per-project basis
        (global-projection-hook-mode 1)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 202:</span>
          packages/project/projection.ecf
        </div>


#### <span class="section-num">3.33.3</span> project {#project}

-   Подключение:
    ```emacs-lisp
    (desire 'project)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 203:</span>
      rc.packages.el
    </div>


#### <span class="section-num">3.33.4</span> projectile {#projectile}

```emacs-lisp
;; (desire 'projectile)
```


### <span class="section-num">3.34</span> Календарь {#календарь}

```emacs-lisp
;;; Appointments, diary, calendar {{{

;; Use "M-x calendar RET" to display the calendar and start
;; appointment warnings.

;; (desire-conf 'appt)
(desire 'calendar)
;; (desire-conf 'todo-mode)
;; (desire-conf 'diary "diary-lib")

;;;}}}
```


### <span class="section-num">3.35</span> Почта {#почта}


#### <span class="section-num">3.35.1</span> Общие опции {#общие-опции}

```emacs-lisp
;;; These provide options for the various message handling packages {{{

(desire 'browse-url)
;; (desire-conf 'mailcrypt)
;; (desire 'supercite)

;;;}}}
```


#### <span class="section-num">3.35.2</span> Работа с почтой {#работа-с-почтой}

```emacs-lisp
;;; Message {{{

(desire 'smtpmail)
;; (desire 'gnus)
(desire 'message)
;; (desire-conf 'vm)
;; (desire 'wl :ensurename 'wanderlust)
;; (desire-conf 'sendmail)
```


#### <span class="section-num">3.35.3</span> mu4e {#mu4e}

-   Подключение:
    ```emacs-lisp
    ;; (desire 'mu4e-dashboard :recipe '(:fetcher github :repo "rougier/mu4e-dashboard"))
    (desire 'mu4e :precondition-system-executable "mu")
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 204:</span>
      rc.packages.el
    </div>
-   Использование интерфейса transient:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Mu4e mail client, a transient menu
    ;; https://www.djcbsoftware.nl/code/mu/

    ;;; Code:

    (require 'mu4e-transient)
    (global-set-key (kbd "C-c m") #'mu4e-transient-menu)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 205:</span>
      packages/mu4e/transient.ecf
    </div>


### <span class="section-num">3.36</span> Блоги {#блоги}

```emacs-lisp
;;; Blogs {{{

;; (desire-conf 'hexo nil "hexo")
;; (desire-conf 'blog-admin nil "blog-admin") ;; Blog admin for emacs with hexo/org-page supported
(desire-conf 'easy-hugo  nil "easy-hugo" t) ;; Emacs major mode for managing hugo

;;;}}}
;;; Miscellaneous {{{

(desire 'ebuku)
(desire-conf 'graphviz-dot-mode nil "graphviz-dot-mode")
;; (desire-conf 'abbrev)
;; (desire-conf 'bibtex)
;; (desire-conf 'calc)
;; (desire-conf 'eiffel-mode)
;; (desire-conf 'filladapt)
;; (desire-conf 'hugs-mode)
;; (desire-conf 'html-helper-mode)
;; (desire-conf 'lispdir)
;; (desire-conf 'php-mode)
;; (desire-conf 'ps-print)
;; (desire-conf 'sh-script)
;; (desire-conf 'shell)
;; (desire-conf 'sql-mode)
;; (desire-conf 'w3)
(desire 'web-mode)
(desire 'gnuplot)

(desire 'pass)


(desire 'multiple-cursors)
```


### <span class="section-num">3.37</span> Мессенджеры {#мессенджеры}

```emacs-lisp
(desire 'telega)
```


### <span class="section-num">3.38</span> Отложенное чтение {#отложенное-чтение}


#### <span class="section-num">3.38.1</span> Pocket reader {#pocket-reader}

-   [Emacs. Pocket reader]({{< relref "2023-09-06-emacs_pocket_reader" >}})

<!--listend-->

```emacs-lisp
(desire 'pocket-reader)
```


#### <span class="section-num">3.38.2</span> Wallabag {#wallabag}

-   Подключение пакета:
    ```emacs-lisp
    (desire 'wallabag :recipe '(:fetcher github :repo "chenyanming/wallabag.el" :branch "master" :files ("*.el" "*.alist" "*.css")))
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 206:</span>
      rc.packages.el
    </div>
-   Начальные настройки:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Emacs wallabag client - A Read It Later/Web Archiving Solution in Emacs
    ;;; https://github.com/chenyanming/wallabag.el


    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 207:</span>
      packages/wallabag/loaddefs.ecf
    </div>
-   Загрузка пакета:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Emacs wallabag client - A Read It Later/Web Archiving Solution in Emacs
    ;;; https://github.com/chenyanming/wallabag.el

    (require 'wallabag)

    ;;; Retrieve new entries after `M-x wallabag`
    (add-hook 'wallabag-after-render-hook 'wallabag-search-update-and-clear-filter)

    ;;; Image Caching. Setting url-automatic-caching non-nil causes documents to be cached automatically
    (setopt url-automatic-caching t)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 208:</span>
      packages/wallabag/desire.ecf
    </div>
-   Шаблон настройки параметров для пользователя:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Emacs wallabag client - A Read It Later/Web Archiving Solution in Emacs
    ;;; https://github.com/chenyanming/wallabag.el

    ;;; Wallabag server host name
    ;; (setq wallabag-host "https://xx.xx.xx")

    ;;; Username
    ;; (setq wallabag-username "xx")

    ;;; Password
    ;; (setq wallabag-password "xx")

    ;;; Created with API clients management
    ;; (setq wallabag-clientid "xx")

    ;;; Created with API clients management
    ;; (setq wallabag-secret "xx")

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 209:</span>
      packages/wallabag/personal.ecf
    </div>

<!--list-separator-->

1.  Интеграция с elfeed

    -   Подгружаем `wallabag`.

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Emacs wallabag client - A Read It Later/Web Archiving Solution in Emacs
    ;; https://github.com/chenyanming/wallabag.el

    ;;; Code:

    (require 'wallabag)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 210:</span>
      packages/elfeed/wallabag.ecf
    </div>

    -   Клавиша `w` добавляет просматриваемую статью в wallabag.

    <!--listend-->

    ```emacs-lisp
    (general-define-key
     :keymaps 'elfeed-show-mode-map
     "w" #'("Add entry to wallabag" . wallabag-add-entry))

    ;;;
    ```


#### <span class="section-num">3.38.3</span> Elfeed {#elfeed}

-   [Emacs. Чтение rss. Elfeed]({{< relref "2025-06-02--emacs-rss-elfeed" >}})
    Объявление:
    ```emacs-lisp
    (desire 'elfeed)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 211:</span>
      rc.packages.el
    </div>
-   Подключение:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; An Emacs web feeds client
    ;; https://github.com/skeeto/elfeed

    ;;; Code:

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 212:</span>
      packages/elfeed/loaddefs.ecf
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; An Emacs web feeds client
    ;; https://github.com/skeeto/elfeed

    ;;; Code:

    (require 'elfeed)

    ;;;; Elfeed-protocol
    (desire 'elfeed-protocol)
    (require 'elfeed-protocol)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 213:</span>
      packages/elfeed/desire.ecf
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; An Emacs web feeds client
    ;; https://github.com/skeeto/elfeed

    ;;; Code:

    ;;;; Mark all as read
    (defun mark-all-read-and-refresh ()
      (interactive)
      (when (y-or-n-p "Mark all items as read?")
        (elfeed-mark-all-as-read)
        (elfeed-search-fetch nil)))
    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 214:</span>
      packages/elfeed/desire.ecd/utils.ecf
    </div>


#### <span class="section-num">3.38.4</span> Elfeed-protocol {#elfeed-protocol}

-   Поддержка серверов rss:

<!--listend-->

```emacs-lisp
;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
;;; Extra protocols to make like Fever, NewsBlur, Nextcloud/ownCloud News and Tiny Tiny RSS work with elfeed
;; https://github.com/fasheng/elfeed-protocol

;;; Code:

(desire 'elfeed-protocol)
(require 'elfeed-protocol)

;;;; curl recommend
(setopt elfeed-use-curl t)
(elfeed-set-timeout 36000)
;;;;; For https without a trust certificate
(setopt elfeed-curl-extra-arguments '("--insecure"))

;;;; enable elfeed-protocol
(setq elfeed-protocol-enabled-protocols '(fever newsblur owncloud ttrss))
(elfeed-protocol-enable)
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 215:</span>
  packages/elfeed-protocol/desire.ecf
</div>

-   Обновить при поиске:

<!--listend-->

```emacs-lisp
;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
;;; Extra protocols to make like Fever, NewsBlur, Nextcloud/ownCloud News and Tiny Tiny RSS work with elfeed
;; https://github.com/fasheng/elfeed-protocol

;;; Code:

(add-hook 'elfeed-search-mode-hook 'elfeed-update)

;;;
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 216:</span>
  packages/elfeed-protocol/desire.ecd/search.ecf
</div>

<!--list-separator-->

1.  Fever протокол

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Extra protocols to make like Fever, NewsBlur, Nextcloud/ownCloud News and Tiny Tiny RSS work with elfeed
    ;; https://github.com/fasheng/elfeed-protocol

    ;;; Code:
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 217:</span>
      packages/elfeed-protocol/desire.ecd/fever.ecf
    </div>

    -   По умолчанию получайте статьи с ID записи по одной.
    -   Для некоторых сервисов, которые не предоставляют действительный ID записи, например FressRSS, просто установите для `elfeed-protocol-fever-update-unread-only` значение `t` в качестве обходного пути.

    <!--listend-->

    ```emacs-lisp
    (setopt elfeed-protocol-fever-update-unread-only t)
    ```

    -   Получение удаленной категории в качестве тега.

    <!--listend-->

    ```emacs-lisp
    (setopt elfeed-protocol-fever-fetch-category-as-tag t)
    ```

    -   Скачивать только непрочитанные.

    <!--listend-->

    ```emacs-lisp
    (setopt elfeed-protocol-fever-update-unread-only t)
    ```

    -   Перечитать источник.

    <!--listend-->

    ```emacs-lisp
    (general-define-key
     :keymaps 'elfeed-search-mode-map
     "C-c C-u" #'("Retry initial sync operation" . elfeed-protocol-fever-reinit))

      ;;;
    ```

<!--list-separator-->

2.  Персональные настройки

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Extra protocols to make like Fever, NewsBlur, Nextcloud/ownCloud News and Tiny Tiny RSS work with elfeed
    ;; https://github.com/fasheng/elfeed-protocol

    ;;; Code:

    (setopt
     elfeed-protocol-feeds
     '(
    ;;;; same format with elfeed-feeds
       ;; "http://foo/"
       ;; ("http://baz/" comic)

    ;;;; format 1
       ;; "owncloud+https://user:pass@myhost.com"

    ;;;; format 2, for username or password with special characters
       ;; ("owncloud+https://user@domain.com@myhost.com"
       ;;  :password "password/with|special@characters:")

    ;;;; format 3, for password in file
       ;; ("owncloud+https://user@myhost.com"
       ;;  :password-file "~/.password")

    ;;;; format 4, for password in .authinfo,
    ;;;; ensure (auth-source-search :host "myhost.com" :port "443" :user "user4") exists
       ;; ("owncloud+https://user@myhost.com"
       ;;  :use-authinfo t)

    ;;;; format 5, for password in gnome-keyring
       ;; ("owncloud+https://user@myhost.com"
       ;;  :password (shell-command-to-string "echo -n `secret-tool lookup attribute value`"))

    ;;;; format 6, for password in pass(1), using password-store.el
       ;; ("owncloud+https://user@myhost.com"
       ;;  :password (password-store-get "owncloud/app-pass"))

    ;;;; FreshRSS
       ;; ("fever+http://username@mydomain.org"
       ;;  :api-url "http://mydomain.org/api/fever.php"
       ;;  :password "my password")

    ;;;; use autotags
       ;; ("owncloud+https://user@myhost.com"
       ;;  :password "password"
       ;;  :autotags (("example.com" comic)))
       ))

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 218:</span>
      packages/elfeed-protocol/personal.ecf
    </div>


### <span class="section-num">3.39</span> Dashboard {#dashboard}

```emacs-lisp

;;;}}}

;; (desire 'grammarly)

;; (desire 'flycheck-grammarly)

(desire 'dashboard)

;; PERSONAL

;; (require 'chord-mode)  ; edit guitar music.
;; (require 'discography) ; variant of BibTeX mode for discographies.
```


### <span class="section-num">3.40</span> Разные программные режимы {#разные-программные-режимы}


#### <span class="section-num">3.40.1</span> Начало {#начало}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;; Different program modes {{{
    ```


#### <span class="section-num">3.40.2</span> Пакет csv-mode {#пакет-csv-mode}

-   [Emacs. cvs-mode]({{< relref "2024-09-04-emacs-cvs-mode" >}})
-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;; csv-mode
    (desire 'csv-mode)
    ```
-   Установим вызов `cvs-mode` для расширения `.cvs`.
    -   Файл `packages/csv-mode/loaddefs.ecf`:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Major mode for editing comma/char separated values
        ;;; https://elpa.gnu.org/packages/csv-mode.html

        (add-to-list 'auto-mode-alist '("\\.[Cc][Ss][Vv]\\'" . csv-mode))

        ;;;
        ```
-   Загружаем пакет при необходимости.
    -   Файл `packages/csv-mode/desire.ecf`:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Major mode for editing comma/char separated values
        ;;; https://elpa.gnu.org/packages/csv-mode.html

        (require 'csv-mode)
        ```
-   Подключим режим визуального выравнивания полей.
    -   Файл `packages/csv-mode/desire.ecf`:
        ```emacs-lisp
        ;;; Keeps fields visually aligned, on-the-fly
        (add-hook 'csv-mode-hook 'csv-align-mode)
        ```
-   Настроим визуально представление длинных строк.
    -   Файл `packages/csv-mode/desire.ecf`:
        ```emacs-lisp
        (add-hook 'csv-mode-hook '(lambda () (interactive) (toggle-truncate-lines nil)))

        ;;;
        ```


#### <span class="section-num">3.40.3</span> Поддержка ebuild-файлов {#поддержка-ebuild-файлов}

-   Сайт: <https://wiki.gentoo.org/wiki/Project:Emacs>
-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;; Ebuild files
    (desire 'ebuild-mode :recipe '(:fetcher github :repo "emacsmirror/ebuild-mode" :branch "master"))
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 219:</span>
      rc.packages.el
    </div>
-   Настроим загрузку:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Edit ebuild and eclass files
    ;;; https://wiki.gentoo.org/wiki/Project:Emacs
    ;;; https://github.com/emacsmirror/ebuild-mode

    (add-to-list 'load-path "/usr/share/emacs/site-lisp/ebuild-mode")
    (autoload 'ebuild-mode "ebuild-mode"
      "Major mode for Gentoo .ebuild files." t)
    (autoload 'ebuild-eclass-mode "ebuild-mode"
      "Major mode for Gentoo .eclass files." t)
    (autoload 'ebuild-repo-mode "ebuild-mode"
      "Minor mode for files in an ebuild repository." t)
    (autoload 'ebuild-repo-mode-maybe-enable "ebuild-mode")
    (autoload 'devbook-mode "devbook-mode"
      "Major mode for editing the Gentoo Devmanual." t)
    (autoload 'gentoo-newsitem-mode "gentoo-newsitem-mode"
      "Major mode for Gentoo GLEP 42 news items." t)
    (autoload 'glep-mode "glep-mode"
      "Major mode for Gentoo Linux Enhancement Proposals." t)

    (add-to-list 'auto-mode-alist '("\\.ebuild\\'" . ebuild-mode))
    (add-to-list 'auto-mode-alist '("\\.eclass\\'" . ebuild-eclass-mode))
    (add-to-list 'auto-mode-alist '("/devmanual.*\\.xml\\'" . devbook-mode))
    (add-to-list 'auto-mode-alist
             '("/[0-9]\\{4\\}-[01][0-9]-[0-3][0-9]-.+\\.[a-z]\\{2\\}\\.txt\\'"
               . gentoo-newsitem-mode))
    (add-to-list 'auto-mode-alist '("/glep.*\\.rst\\'" . glep-mode))
    (add-to-list 'auto-mode-alist
             '("/\\(package\\.\\(mask\\|unmask\\|use\\|env\
    \\|license\\|properties\\|accept_\\(keywords\\|restrict\\)\\)\
    \\|\\(package\\.\\)?use.\\(stable\\.\\)?\\(force\\|mask\\)\\)\\'"
               . conf-space-mode))
    (add-to-list 'auto-mode-alist
             '("/make\\.\\(conf\\|defaults\\)\\'" . conf-unix-mode))
    (add-to-list 'interpreter-mode-alist '("openrc-run" . sh-mode))
    (add-to-list 'interpreter-mode-alist '("runscript" . sh-mode))
    (add-hook 'find-file-hook #'ebuild-repo-mode-maybe-enable)
    (modify-coding-system-alist 'file "\\.\\(ebuild\\|eclass\\)\\'" 'utf-8)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 220:</span>
      packages/ebuild-mode/loaddefs.ecf
    </div>


#### <span class="section-num">3.40.4</span> Asymptote {#asymptote}

-   <https://asymptote.sourceforge.io/>

<!--list-separator-->

1.  Редактирование файлов Asymptote

    -   Поддержка редактирования файлов Asymptote.
    -   Файл `rc.packages.el`:
        ```emacs-lisp
        ;;; Asymptote
        (desire 'asy-mode :recipe '(:fetcher github :repo "vectorgraphics/asymptote" :branch "master" :files ("base/asy-mode.el")))
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 221:</span>
          rc.packages.el
        </div>
    -   Конфигурационный файл:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; 2D & 3D TeX-Aware Vector Graphics Language
        ;;; https://github.com/vectorgraphics/asymptote

        (autoload 'asy-mode "asy-mode.el" "Asymptote major mode." t)
        (autoload 'lasy-mode "asy-mode.el" "hybrid Asymptote/Latex major mode." t)
        (autoload 'asy-insinuate-latex "asy-mode.el" "Asymptote insinuate LaTeX." t)
        (add-to-list 'auto-mode-alist '("\\.asy$" . asy-mode))

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 222:</span>
          packages/asy-mode.ecf
        </div>

<!--list-separator-->

2.  Поддержка Asymptote в Babel

    -   Репозиторий: <https://github.com/hurrja/ob-asymptote>
    -   Необходимо установить программу Asymptote: <http://asymptote.sourceforge.net/>

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Org-Babel support for evaluating asymptote
    ;;; https://github.com/hurrja/ob-asymptote

    (desire 'ob-asymptote)
    (require 'ob-asymptote)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 223:</span>
      packages/org/desire.ecd/ob-asymptote.ecf
    </div>


#### <span class="section-num">3.40.5</span> kmonad-файлы {#kmonad-файлы}

-   Поддержка синтаксиса конфигурационных файлов kmonad.
-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;; kbd-mode
    ;; (desire 'kbd-mode :recipe '(:fetcher github :repo "kmonad/kbd-mode" :branch "master"))
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 224:</span>
      rc.packages.el
    </div>
-   Конфигурационный файл:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Emacs mode for syntax highlighting kmonad's .kbd files.
    ;;; https://github.com/kmonad/kbd-mode

    (autoload 'kdb-mode "kbd-mode.el" "Kmonad's .kbd files" t)
    (add-to-list 'auto-mode-alist '("\\.kbd$" . kbd-mode))

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 225:</span>
      packages/kbd-mode.ecf
    </div>


#### <span class="section-num">3.40.6</span> Julia {#julia}

```emacs-lisp
;;;;; Julia

(desire 'julia-snail)
;; (desire 'julia-repl)
```

<!--list-separator-->

1.  julia-mode

    <!--list-separator-->

    1.  Подключение

        -   Файл: `rc.packages.el`

        <!--listend-->

        ```emacs-lisp
        (desire 'julia-mode)
        ```

    <!--list-separator-->

    2.  Объявление

        -   Файл: `packages/julia-mode/loaddefs.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Julia support in Emacs
        ;; https://github.com/JuliaEditorSupport/julia-emacs

        ;;; Code:

        (add-to-list 'auto-mode-alist '("\\.jl\\'" . julia-mode))

        ;;;
        ```

    <!--list-separator-->

    3.  Загрузка

        -   Файл: `packages/julia-mode/desire.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Julia support in Emacs
        ;; https://github.com/JuliaEditorSupport/julia-emacs

        ;;; Code:

        (require 'julia-mode)

        ;;;
        ```

    <!--list-separator-->

    4.  Fill docstring

        -   Файл: packages/julia-mode/desire.ecd/fill-docstring.ecf

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Fill docstrings. This is useful if you want to use M-q on docstrings.

        ;;; Code:


        (defun julia-fill-string ()
          "Fill a docstring, preserving newlines before and after triple quotation marks."
          (interactive)
          (if (and transient-mark-mode mark-active)
              (fill-region (region-beginning) (region-end) nil t)
            (cl-flet ((fill-if-string ()
                                      (when (or (looking-at (rx "\"\"\""
                                                                (group
                                                                 (*? (or (not (any "\\"))
                                                                         (seq "\\" anything))))
                                                                "\"\"\""))
                                                (looking-at (rx "\""
                                                                (group
                                                                 (*? (or (not (any "\\"))
                                                                         (seq "\\" anything))))
                                                                "\"")))
                                        (let ((start (match-beginning 1))
                                              (end (match-end 1)))
                                          ;; (ess-blink-region start end)
                                          (fill-region start end nil nil nil)))))
              (save-excursion
                (let ((s (syntax-ppss)))
                  (when (fourth s) (goto-char (ninth s))))
                (fill-if-string)))))

        (local-set-key (kbd "M-q") 'julia-fill-string)
        (set-fill-column 80)

        ;(require 'whitespace)
        ;(setopt whitespace-style '(face empty tabs lines-tail trailing))
        ;(global-whitespace-mode t)
        ;(hungry-delete-mode)

        ;;;
        ```

    <!--list-separator-->

    5.  Фонтификация

        -   Файл: `packages/julia-mode/desire.ecd/fontification.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Borrow matlab.el's fontification of math operators
        ;; https://web.archive.org/web/20170326183805/https://ogbe.net/emacsconfig.html

        ;;; Code:

        (dolist (mode '(julia-mode ess-julia-mode))
          (font-lock-add-keywords
           mode
           `((,(let ((OR "\\|"))
                 (concat "\\("  ; stolen `matlab.el' operators first
                         ;; `:` defines a symbol in Julia and must not be highlighted
                         ;; as an operator. The only operators that start with `:` are
                         ;; `:<` and `::`. This must be defined before `<`.
                         "[:<]:" OR
                         "[<>]=?" OR
                         "\\.[/*^']" OR
                         "===" OR
                         "==" OR
                         "=>" OR
                         "\\<xor\\>" OR
                         "[-+*\\/^&|$]=?" OR  ; this has to come before next (updating operators)
                         "[-^&|*+\\/~]" OR
                         ;; Julia variables and names can have `!`. Thus, `!` must be
                         ;; highlighted as a single operator only in some
                         ;; circumstances. However, full support can only be
                         ;; implemented by a full parser. Thus, here, we will handle
                         ;; only the simple cases.
                         "[[:space:]]!=?=?" OR "^!=?=?" OR
                         ;; The other math operators that starts with `!`.
                         ;; more extra julia operators follow
                         "[%$]" OR
                         ;; bitwise operators
                         ">>>" OR ">>" OR "<<" OR
                         ">>>=" OR ">>" OR "<<" OR
                         "\\)"))
              1 font-lock-type-face))))

        ;;;
        ```

    <!--list-separator-->

    6.  Интеграция

        <!--list-separator-->

        1.  julia-repl

            -   Файл: `packages/julia-mode/julia-repl.ecf`

            <!--listend-->

            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Run an inferior Julia REPL in a terminal inside Emacs
            ;; https://github.com/tpapp/julia-repl

            ;;; Code:

            (require 'julia-repl)
            (add-hook 'julia-mode-hook 'julia-repl-mode)

            ;;;
            ```

        <!--list-separator-->

        2.  julia-snail

            -   Файл: `packages/julia-mode/julia-snail.ecf`

            <!--listend-->

            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; An Emacs development environment for Julia
            ;; https://github.com/gcv/julia-snail

            ;;; Code:

            (require 'julia-snail)
            (add-hook 'julia-mode-hook #'julia-snail-mode)

            ;;;
            ```

        <!--list-separator-->

        3.  lsp-mode

            -   Файл: `packages/julia-mode/lsp-mode.ecf`

            <!--listend-->

            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Julia support for the lsp-mode package using the LanguageServer.jl package
            ;; https://github.com/gdkrmr/lsp-julia

            ;;; Code:

            (require 'lsp-mode)

            (desire 'lsp-julia)
            (require 'lsp-julia)

            ;;;; Linux/macOS
            ;; (setopt lsp-julia-package-dir "/usr/local/bin/julia")

            ;;;; Configure lsp + julia
            (add-hook 'julia-mode-hook #'lsp-mode)
            (add-hook 'julia-mode-hook #'lsp)

            ;;;
            ```


#### <span class="section-num">3.40.7</span> Поддержка командной оболочки fish {#поддержка-командной-оболочки-fish}

-   Загрузка пакета:
    ```emacs-lisp
    ;;; https://github.com/wwwjfy/emacs-fish
    (desire 'fish-mode)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 226:</span>
      rc.packages.el
    </div>
-   Настройка пакета:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; fish-mode for emacs
    ;;; https://github.com/wwwjfy/emacs-fish

    ;;; run fish_indent before save
    (add-hook 'fish-mode-hook (lambda ()
                            (add-hook 'before-save-hook 'fish_indent-before-save)))

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 227:</span>
      packages/fish-mode.ecf
    </div>


#### <span class="section-num">3.40.8</span> Разное {#разное}

```emacs-lisp
(desire 'speedbar)
;; (desire-conf 'semantic nil "semantic")

;; (desire-conf 'cedet nil "cedet")
;; (desire-conf 'ecb nil "ecb")

;; (desire-conf 'php-mode nil "php-mode")
;; (desire-conf 'eiffel-mode nil "eiffel-mode")

(desire 'ebib)

(desire 'lua-mode)
```

```emacs-lisp


(desire 'yaml-mode)
(desire 'ini-mode)
(desire 'hcl-mode)

(desire 'magit-gitflow)
(desire 'magit)
```


#### <span class="section-num">3.40.9</span> Конец {#конец}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;;}}}
    ```


### <span class="section-num">3.41</span> Редактирование текста в броузере {#редактирование-текста-в-броузере}

-   [Emacs. Редактирование текста в броузере]({{< relref "2024-08-28-emacs-edit-text-area-browser" >}})


#### <span class="section-num">3.41.1</span> Начало {#начало}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;; Edit text areas in browsers {{{
    ```


#### <span class="section-num">3.41.2</span> Edit with Emacs {#edit-with-emacs}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    (desire 'edit-server)
    ```
-   Файл `packages/edit-server.ecf`:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; A Chromium/Firefox "clone" of It's All Text for spawning an editor to edit text areas in browsers. Based on David Hilley's original Chromium extension.
    ;;; https://github.com/stsquad/emacs_chrome

    (require 'edit-server)

    (setopt edit-server-new-frame nil)
    (edit-server-start)

    (setopt edit-server-url-major-mode-alist
          '(("github\\.com" . markdown-mode)))

    ;;;
    ```


#### <span class="section-num">3.41.3</span> Ghost Text {#ghost-text}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;; (desire 'atomic-chrome)
    ```
-   Файл `packages/atomic-chrome.ecf`:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Edit text area on Chrome with Emacs using Atomic Chrome
    ;;; https://github.com/alpha22jp/atomic-chrome

    (require 'atomic-chrome)
    (atomic-chrome-start-server)

    ;;; Atomic Chrome for Emacs automatically reflects modifications to the browser by default
    (setopt atomic-chrome-enable-auto-update t)

    ;;; The default major mode of editing buffer is `text-mode`. You can change the major mode manually
    (setopt atomic-chrome-default-major-mode 'markdown-mode)

    ;;; Choose the major mode for a specific website
    (setopt atomic-chrome-url-major-mode-alist
          '(("github\\.com" . gfm-mode)
            ("redmine" . textile-mode)))

    ;;; Select editing buffer style
    ;;; full: Open in the selected window.
    ;;; split: Open in the new window by splitting the selected window (default).
    ;;; frame: Create a new frame and window in it.
    ;; (setopt atomic-chrome-buffer-open-style split)

    ;;;
    ```


#### <span class="section-num">3.41.4</span> Конец {#конец}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;;}}}
    ```


### <span class="section-num">3.42</span> Навигация по файлам {#навигация-по-файлам}

-   [Emacs. Просмотр каталогов]({{< relref "2021-10-03-emacs-directory-browsing" >}})


#### <span class="section-num">3.42.1</span> dired {#dired}

<!--list-separator-->

1.  dired

    -   Файл `rc.packages.el`:
        ```emacs-lisp
        ;;; Dired {{{

        (desire 'mouse3 :recipe '(:fetcher github :repo "emacsmirror/mouse3" :branch "master" :files ("*.el")))

        (desire 'dired)
        (desire 'dired+ :recipe '(:fetcher github :repo "emacsmirror/dired-plus" :branch "master" :files ("*.el")))

        ;; (desire 'ranger)
        ;; (desire 'efar)
        ;; (desire 'sunrise-commander :recipe '(:fetcher github :repo "sunrise-commander/sunrise-commander"))
        (desire 'dirvish)
        ;;;}}}
        ```

<!--list-separator-->

2.  diredc

    -   Репозиторий: <https://github.com/Boruch-Baum/emacs-diredc>
    -   Двупанельный (как в midnight commander) режим.
    -   Подключение:
        ```emacs-lisp
        ;;; Midnight Commander features (plus) for emacs dired-mode
        ;; (desire 'diredc)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 228:</span>
          rc.packages.el
        </div>


#### <span class="section-num">3.42.2</span> Neotree {#neotree}

-   [Emacs. Neotree]({{< relref "2022-03-23-emacs-neotree" >}})
-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;; (desire 'neotree)
    ```


#### <span class="section-num">3.42.3</span> Treemacs {#treemacs}

-   [Emacs. Пакет treemacs]({{< relref "2025-01-20--emacs-treemacs" >}})

<!--list-separator-->

1.  Подключение

    -   Файл `rc.packages.el`
        ```emacs-lisp
        (desire 'treemacs)
        ```

<!--list-separator-->

2.  Объявление

    -   Файл: `packages/treemacs/loaddefs.ecf`

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Treemacs - a tree layout file explorer for Emacs
    ;; https://github.com/Alexander-Miller/treemacs

    ;;; Code:

    (require 'treemacs)

    ;;;
    ```

<!--list-separator-->

3.  Загрузка

    -   Файл: `packages/treemacs/desire.ecf`
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Treemacs - a tree layout file explorer for Emacs
        ;; https://github.com/Alexander-Miller/treemacs

        ;;; Code:

        ;;;; Set the correct python3 executable path. This is needed for treemacs-git-mode extended
        (setopt treemacs-python-executable (executable-find "python"))

        (setopt treemacs-collapse-dirs                 (if treemacs-python-executable 3 0)
                treemacs-deferred-git-apply-delay      0.5
                treemacs-directory-name-transformer    #'identity
                treemacs-display-in-side-window        t
                treemacs-eldoc-display                 'simple
                treemacs-file-event-delay              2000
                treemacs-file-extension-regex          treemacs-last-period-regex-value
                treemacs-file-follow-delay             0.2
                treemacs-file-name-transformer         #'identity
                treemacs-follow-after-init             t
                treemacs-find-workspace-method         'find-for-file-or-pick-first
                treemacs-git-command-pipe              ""
                treemacs-goto-tag-strategy             'refetch-index
                treemacs-header-scroll-indicators      '(nil . "^^^^^^")
                treemacs-hide-dot-git-directory        t
                treemacs-indentation                   2
                treemacs-indentation-string            " "
                treemacs-is-never-other-window         nil
                treemacs-max-git-entries               5000
                treemacs-missing-project-action        'ask
                treemacs-move-forward-on-expand        nil
                treemacs-no-png-images                 nil
                treemacs-no-delete-other-windows       t
                treemacs-project-follow-cleanup        nil
                treemacs-persist-file                  (expand-file-name "treemacs-persist" user-emacs-directory)
                treemacs-position                      'left
                treemacs-recenter-distance             0.1
                treemacs-recenter-after-file-follow    nil
                treemacs-recenter-after-tag-follow     nil
                treemacs-recenter-after-project-jump   'always
                treemacs-recenter-after-project-expand 'on-distance
                treemacs-litter-directories            '("/node_modules" "/.venv" "/.cask")
                treemacs-project-follow-into-home      nil
                treemacs-show-cursor                   nil
                treemacs-show-hidden-files             t
                treemacs-silent-filewatch              nil
                treemacs-silent-refresh                nil
                treemacs-sorting                       'alphabetic-asc
                treemacs-select-when-already-in-treemacs 'move-back
                treemacs-space-between-root-nodes      t
                treemacs-tag-follow-cleanup            t
                treemacs-tag-follow-delay              1.5
                treemacs-user-mode-line-format         nil
                treemacs-user-header-line-format       nil
                treemacs-wide-toggle-width             70
                treemacs-width                         35
                treemacs-width-increment               1
                treemacs-width-is-initially-locked     t
                treemacs-workspace-switch-cleanup      nil)

        ;; The default width and height of the icons is 22 pixels. If you are
        ;; using a Hi-DPI display, uncomment this to double the icon size.
        ;;(treemacs-resize-icons 44)

        (treemacs-follow-mode t)
        (treemacs-filewatch-mode t)
        (treemacs-fringe-indicator-mode 'always)
        (when treemacs-python-executable
           (treemacs-git-commit-diff-mode t))

        (pcase (cons (not (null (executable-find "git")))
                     (not (null treemacs-python-executable)))
          (`(t . t)
           (treemacs-git-mode 'deferred))
          (`(t . _)
           (treemacs-git-mode 'simple)))


        (treemacs-hide-gitignored-files-mode nil)

        ;;; Mouse Interface
        (define-key treemacs-mode-map [mouse-1] #'treemacs-single-click-expand-action)

        ;; (treemacs-start-on-boot)



        ;;;
        ```

<!--list-separator-->

4.  Клавиатурные сочетания

    -   Файл: `packages/treemacs/desire.ecd/key.ecf`

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Treemacs - a tree layout file explorer for Emacs
    ;; https://github.com/Alexander-Miller/treemacs

    ;;; Code:

    (general-define-key
     "M-0" 'treemacs-select-window)

    (general-define-key
     :prefix "C-x t"
     "1" 'treemacs-delete-other-windows
     "t" 'treemacs
     "d" 'treemacs-select-directory
     "B" 'treemacs-bookmark
     "C-t" 'treemacs-find-file
     "M-t" 'treemacs-find-tag)

    ;;;
    ```

<!--list-separator-->

5.  Исправления

    -   Файл: `packages/treemacs/desire.ecd/fix.ecf`

    <!--listend-->

    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Code:

    ;;; Suppress “ad-handle-definition: .. redefined” warnings during Emacs startup
    (custom-set-variables '(ad-redefinition-action (quote accept)))

    ;;;
    ```

<!--list-separator-->

6.  Интеграция

    <!--list-separator-->

    1.  projectile

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Projectile integration for treemacs

        ;;; Code:

        (desire 'treemacs-projectile)
        (require 'treemacs-projectile)

        ;;;
        ```

    <!--list-separator-->

    2.  magit

        -   Файл: `packages/treemacs/magit.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Treemacs - a tree layout file explorer for Emacs
        ;; https://github.com/Alexander-Miller/treemacs

        ;;; Code:

        (desire 'treemacs-magit)
        (require 'treemacs-magit)

        ;;;
        ```

    <!--list-separator-->

    3.  tab-bar

        -   Файл: `packages/treemacs/tab-bar.ecf`

        <!--listend-->

        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Treemacs - a tree layout file explorer for Emacs
        ;; https://github.com/Alexander-Miller/treemacs

        ;;; Code:

        (desire 'treemacs-tab-bar)
        (require 'treemacs-tab-bar)

        (setopt treemacs-set-scope-type 'Tabs)

        ;;;
        ```


### <span class="section-num">3.43</span> Навигация по тексту {#навигация-по-тексту}


#### <span class="section-num">3.43.1</span> Начало {#начало}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;; Text navigation {{{
    ```


#### <span class="section-num">3.43.2</span> line-reminder {#line-reminder}

-   Line annotation for changed and saved lines: <https://github.com/emacs-vs/line-reminder>
-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;; Line annotation for changed and saved lines
    (desire 'line-reminder)
    ```
-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Line annotation for changed and saved lines
    ;;; https://github.com/emacs-vs/line-reminder

    ;;; Enable for all buffers
    (global-line-reminder-mode t)

    ;;; Display Annotation
    ;;; linum | indicators
    (setopt line-reminder-show-option 'linum)

    ;;; Display thumbnail
    (setopt line-reminder-thumbnail t)

    ;;;
    ```


#### <span class="section-num">3.43.3</span> Конец {#конец}

-   Файл `rc.packages.el`:
    ```emacs-lisp
    ;;;}}}
    ```


### <span class="section-num">3.44</span> Перевод {#перевод}


#### <span class="section-num">3.44.1</span> gt {#gt}

-   Подключаем:
    ```emacs-lisp
    ;;; Translator on Emacs
    (desire 'gt)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 229:</span>
      rc.packages.el
    </div>
-   Загрузка:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Translator on Emacs. Supports multiple engines such as Google, Bing, deepL, ChatGPT, StarDict, Youdao and so on
    ;; https://github.com/lorniu/gt.el

    (require 'gt)

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 230:</span>
      packages/go-translate/loaddefs.ecf
    </div>
-   Конфигурация:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Translator on Emacs. Supports multiple engines such as Google, Bing, deepL, ChatGPT, StarDict, Youdao and so on
    ;; https://github.com/lorniu/gt.el


    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 231:</span>
      packages/go-translate/desire.ecf
    </div>
-   Простейшая конфигурация:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Translator on Emacs. Supports multiple engines such as Google, Bing, deepL, ChatGPT, StarDict, Youdao and so on
    ;; https://github.com/lorniu/gt.el

    ;;; Initialize the default translator, let it translate between en and ru via Google Translate, and the result will be displayed in the Echo Area.
    (setopt gt-langs '(en ru))
    (setopt gt-default-translator (gt-translator :engines (gt-google-engine)))

    ;;;
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 232:</span>
      packages/go-translate/desire.ecd/google-simple.ecf
    </div>


### <span class="section-num">3.45</span> UI {#ui}

-   Раздел:
    ```emacs-lisp
    ;;;; UI
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 233:</span>
      rc.packages.el
    </div>


#### <span class="section-num">3.45.1</span> Шрифты {#шрифты}

-   [Emacs. Шрифты]({{< relref "2025-04-01--emacs-fonts" >}})
-   Раздел:
    ```emacs-lisp
    ;;;;; Fonts
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 234:</span>
      rc.packages.el
    </div>

<!--list-separator-->

1.  Выбор шрифта

    Подключение:

    ```emacs-lisp
    (desired 'iosevka)
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 235:</span>
      rc.packages.el
    </div>

<!--list-separator-->

2.  Fontset

    -   Подключение:
        ```emacs-lisp
        (desire 'fontset)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 236:</span>
          rc.packages.el
        </div>
    -   Загрузка:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Set fontset
        ;; https://www.gnu.org/software/emacs/manual/html_node/emacs/Modifying-Fontsets.html

        ;;; Code:

        ;;; Set default font
        ;; (cl-loop for font in '("SF Mono" "Hack" "Source Code Pro" "Fira Code"
        ;; 		       "Menlo" "Monaco" "DejaVu Sans Mono" "Consolas")
        ;; 	 when (font-installed-p font)
        ;; 	 return (set-face-attribute 'default nil
        ;; 				    :font font
        ;; 				    :height (cond (sys/mac-x-p 130)
        ;; 						  (sys/win32p 110)
        ;; 						  (t 100))))

        ;; ;;; Specify font for all unicode characters
        ;; (cl-loop for font in '("Apple Color Emoji" "Segoe UI Symbol" "Symbola" "Symbol")
        ;; 	 when (font-installed-p font)
        ;; 	 return (set-fontset-font t 'unicode font nil 'prepend))

        ;;; Specify font for Chinese characters
        ;; (cl-loop for font in '("WenQuanYi Micro Hei" "Microsoft Yahei")
        ;; 	 when (font-installed-p font)
        ;; 	 return (set-fontset-font t '(#x4e00 . #x9fff) font)))

        ;; (cond
        ;;  ((find-font (font-spec :name "Iosevka"))
        ;;   (add-to-list 'default-frame-alist '(font . "Iosevka-12" ))
        ;;   (set-face-attribute 'default t :font "Iosevka-12" ))
        ;;  ((find-font (font-spec :name "Hack"))
        ;;   (add-to-list 'default-frame-alist '(font . "Hack-12" ))
        ;;   (set-face-attribute 'default t :font "Hack-12" ))
        ;;  ((find-font (font-spec :name "IBM Plex Mono"))
        ;;   (add-to-list 'default-frame-alist '(font . "IBM Plex Mono-12" ))
        ;;   (set-face-attribute 'default t :font "IBM Plex Mono-12" ))
        ;;  ((find-font (font-spec :name "Source Code Pro"))
        ;;   (add-to-list 'default-frame-alist '(font . "Source Code Pro-12" ))
        ;;   (set-face-attribute 'default t :font "Source Code Pro-12" ))
        ;;  ((find-font (font-spec :name "AnonymousPro"))
        ;;   (add-to-list 'default-frame-alist '(font . "AnonymousPro-12" ))
        ;;   (set-face-attribute 'default t :font "AnonymousPro-12" ))
        ;;  ((find-font (font-spec :name "Victor Mono"))
        ;;   (add-to-list 'default-frame-alist '(font . "Victor Mono-12" ))
        ;;   (set-face-attribute 'default t :font "Victor Mono-12" ))
        ;;  ((find-font (font-spec :name "Hermit"))
        ;;   (add-to-list 'default-frame-alist '(font . "Hermit-12" ))
        ;;   (set-face-attribute 'default t :font "Hermit-12" ))
        ;;  ((find-font (font-spec :name "Fira Code"))
        ;;   (add-to-list 'default-frame-alist '(font . "Fira Code-12" ))
        ;;   (set-face-attribute 'default t :font "Fira Code-12" ))
        ;;  ((find-font (font-spec :name "Inconsolata"))
        ;;   (add-to-list 'default-frame-alist '(font . "Inconsolata-12" ))
        ;;   (set-face-attribute 'default t :font "Inconsolata-12" ))
        ;;  ((find-font (font-spec :name "DejaVu Sans Mono"))
        ;;   (add-to-list 'default-frame-alist '(font . "DejaVu Sans Mono-12" ))
        ;;   (set-face-attribute 'default t :font "DejaVu Sans Mono-12" ))
        ;;  ((find-font (font-spec :name "Lucida Console"))
        ;;   (add-to-list 'default-frame-alist '(font . "Lucida Console-12" ))
        ;;   (set-face-attribute 'default t :font "Lucida Console-12" ))
        ;;  ((find-font (font-spec :name "Courier"))
        ;;   (add-to-list 'default-frame-alist '(font . "Courier-12" ))
        ;;   (set-face-attribute 'default t :font "Courier-12" ))
        ;;  )

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 237:</span>
          packages/fontset/loaddefs.ecf
        </div>
    -   Эмодзи:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Set emoji

        ;;; Code:

        ;;;; Use "Noto Color Emoji" for the emoji script (this is the default).
        ;; (set-fontset-font "fontset-default" 'emoji
        ;;                   '("Noto Color Emoji" . "iso10646-1")
        ;;                   nil 'prepend)

        ;;;; Display the "heart" character using a color font.
        ;; (set-fontset-font "fontset-default"
        ;;                   #x2764 "Noto Color Emoji")

        (set-fontset-font
         t
         'emoji
         (cond
          ((member "Apple Color Emoji" (font-family-list)) "Apple Color Emoji")
          ((member "Noto Color Emoji" (font-family-list)) "Noto Color Emoji")
          ((member "Noto Emoji" (font-family-list)) "Noto Emoji")
          ((member "Segoe UI Emoji" (font-family-list)) "Segoe UI Emoji")
          ((member "Symbola" (font-family-list)) "Symbola")))

        (set-fontset-font
         t
         'symbol
         (cond
          ((member "Segoe UI Symbol" (font-family-list)) "Segoe UI Symbol")
          ((member "Apple Symbols" (font-family-list)) "Apple Symbols")
          ((member "Symbola" (font-family-list)) "Symbola")))

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 238:</span>
          packages/fontset/desire.ecd/emoji.ecf
        </div>
    -   Unicode:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Font for all unicode characters

        ;;; Code:

        ;; (set-fontset-font "fontset-default" 'symbol
        ;; 		  (font-spec :family "Symbola")
        ;; 		  nil 'prepend)

        ;; (set-fontset-font "fontset-default" 'unicode
        ;; 		  (font-spec :family "Symbola")
        ;; 		  nil 'prepend)

        ;; set font for cuneiform
        (set-fontset-font
         t
         'cuneiform
         (cond
          ((eq system-type 'windows-nt)
           (cond
            ((member "Segoe UI Historic" (font-family-list)) "Segoe UI Historic")))
          ((eq system-type 'darwin)
           (cond
            ((member "Noto Sans Cuneiform Regular" (font-family-list)) "Noto Sans Cuneiform Regular")))
          ((eq system-type 'gnu/linux)
           (cond
            ((member "Noto Sans Cuneiform Regular" (font-family-list)) "Noto Sans Cuneiform Regular")))))

        (set-fontset-font
         t
         'phoenician
         (cond
          ((eq system-type 'windows-nt)
           (cond
            ((member "Segoe UI Historic" (font-family-list)) "Segoe UI Historic")))
          ((eq system-type 'darwin)
           (cond
            ((member "Noto Sans Phoenician Regular" (font-family-list)) "Noto Sans Phoenician Regular")))
          ((eq system-type 'gnu/linux)
           (cond
            ((member "Noto Sans Phoenician Regular" (font-family-list)) "Noto Sans Phoenician Regular")))))

        (set-fontset-font
         t
         'deseret
         (cond
          ((eq system-type 'windows-nt)
           (cond
            ((member "Segoe UI Symbol" (font-family-list)) "Segoe UI Symbol")))
          ((eq system-type 'darwin)
           (cond
            ((member "Apple Symbols" (font-family-list)) "Apple Symbols")))
          ((eq system-type 'gnu/linux)
           (cond
            ((member "Noto Sans Deseret" (font-family-list)) "Noto Sans Deseret")))))

        (set-fontset-font
         t
         'shavian
         (cond
          ((eq system-type 'windows-nt)
           (cond
            ((member "Segoe UI Historic" (font-family-list)) "Segoe UI Historic")))
          ((eq system-type 'darwin)
           (cond
            ((member "Apple Symbols" (font-family-list)) "Apple Symbols")))
          ((eq system-type 'gnu/linux)
           (cond
            ((member "Noto Sans Shavian Regular" (font-family-list)) "Noto Sans Shavian Regular")))))

        (set-fontset-font
         t
         'egyptian
         (cond
          ((eq system-type 'windows-nt)
           (cond
            ((member "Segoe UI Historic" (font-family-list)) "Segoe UI Historic")))
          ((eq system-type 'darwin)
           (cond
            ((member "Noto Sans Egyptian Hieroglyphs" (font-family-list)) "Noto Sans Egyptian Hieroglyphs")))
          ((eq system-type 'gnu/linux)
           (cond
            ((member "Aegyptus" (font-family-list)) "Aegyptus")))))

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 239:</span>
          packages/fontset/desire.ecd/unicode.ecf
        </div>
    -   Шрифты
        -   Iosevka
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Set Iosevka font
            ;; https://be5invis.github.io/Iosevka/

            ;;; Code:

            ;;;; Set default font

            ;; (add-to-list 'default-frame-alist '(font . "Iosevka Term-12" ))
            ;; (add-to-list 'initial-frame-alist '(font . "Iosevka Term-12" ))
            ;; (set-face-attribute 'default nil :font "Iosevka Term-12" )

            (add-to-list 'default-frame-alist '(font . "Iosevka Nerd Font-12" ))
            (add-to-list 'initial-frame-alist '(font . "Iosevka Nerd Font-12" ))
            (set-face-attribute 'default nil :font "Iosevka Nerd Font-12" )


            ;;;; Set font
            ;; (dolist (charset '(latin cyrillic greek))
            ;;   (set-fontset-font "fontset-default" charset
            ;;                     (font-spec :family "Iosevka Term" :size 12)
            ;;                     nil 'prepend))

            (dolist (charset '(latin cyrillic greek))
              (set-fontset-font "fontset-default" charset
                                (font-spec :family "Iosevka Nerd Font" :size 12)
                                nil 'prepend))

            ;;;
            ```
            <div class="src-block-caption">
              <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 240:</span>
              packages/fontset/iosevka.ecf
            </div>

<!--list-separator-->

3.  Разное

    ```emacs-lisp
    ;; (desire 'mixed-pitch)
    ;; (desire-conf 'font-lock)
    ;; (desire-conf 'font-lock-jit)
    ;; (desire-conf 'font-lock-lazy)
    ;; (desire-conf 'font-lock-fast)
    ;; (desire-conf 'faces)
    ;; (desire-conf 'color-theme nil "color-theme")
    ;; (desire-conf 'fira-code-mode nil "fira-code-mode" t) ;; Simple minor mode for Fira Code ligatures
    ```

<!--list-separator-->

4.  Лигатуры

    ```emacs-lisp
    ;; (desire 'ligature)
    ```

<!--list-separator-->

5.  unicode-fonts

    ```emacs-lisp
    (desire 'unicode-fonts)
    ```

    -   Загрузка:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Configure Unicode fonts for Emacs
        ;; https://github.com/rolandwalker/unicode-fonts

        ;;; Code:

        ;;;; Requires font-utils
        (desire 'font-utils)

        ;;;; Requires ucs-utils
        (desire 'ucs-utils)

        ;;;; Uses if present
        (desire 'persistent-soft)

        ;;;; Load package
        (require 'unicode-fonts)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 241:</span>
          packages/unicode-fonts/loaddefs.ecf
        </div>
    -   Настройка:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Configure Unicode fonts for Emacs
        ;; https://github.com/rolandwalker/unicode-fonts

        ;;; Code:

        ;;; ligature support
        (setopt unicode-fonts-enable-ligatures t)

        ;;; By default ligatures will be enabled in all programing modes.
        (setopt unicode-fonts-ligature-modes '(prog-mode))

        ;;; You can enable ligatures for specific modes.
        ;; (setopt unicode-fonts-ligature-modes '(php-mode js-mode))

        ;;; To enable only for text modes you can use text-mode
        ;; (setopt unicode-fonts-ligature-modes '(text-mode))

        ;;; Configure the ligature set
        (setopt unicode-fonts-ligature-set '("|||>" "<|||" "<==>" "<!--" "####" "~~>" "***" "||=" "||>"
                                           ":::" "::=" "=:=" "===" "==>" "=!=" "=>>" "=<<" "=/=" "!=="
                                           "!!." ">=>" ">>=" ">>>" ">>-" ">->" "->>" "-->" "---" "-<<"
                                           "<~~" "<~>" "<*>" "<||" "<|>" "<$>" "<==" "<=>" "<=<" "<->"
                                           "<--" "<-<" "<<=" "<<-" "<<<" "<+>" "</>" "###" "#_(" "..<"
                                           "..." "+++" "/==" "///" "_|_" "www" "&&" "^=" "~~" "~@" "~="
                                           "~>" "~-" "**" "*>" "*/" "||" "|}" "|]" "|=" "|>" "|-" "{|"
                                           "[|" "]#" "::" ":=" ":>" ":<" "$>" "==" "=>" "!=" "!!" ">:"
                                           ">=" ">>" ">-" "-~" "-|" "->" "-<" "<~" "<*" "<|" "<:" "<$"
                                           "<=" "<>" "<-" "<<" "<+" "</" "#{" "#[" "#:" "#=" "#!" "##"
                                           "#(" "#?" "#_" "%%" ".=" ".-" ".." ".?" "+>" "++" "?:" "?="
                                           "?." "??" ";;" "/*" "/**" "/=" "/>" "__" "~~" "(*" "*)"
                                           "://"))

        (setopt ecf-unicode-font (font-spec :family "Iosevka" :size 12))

        (when ecf-unicode-font
          (let ((ecf-unicode-font-family (plist-get (font-face-attributes ecf-unicode-font) :family)))
            (dolist (unicode-block unicode-fonts-block-font-mapping)
              (push ecf-unicode-font-family (cadr unicode-block)))))

        (unicode-fonts-setup)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 242:</span>
          packages/unicode-fonts/desire.ecf
        </div>


#### <span class="section-num">3.45.2</span> Modeline {#modeline}

<!--list-separator-->

1.  Начало

    -   Файл `rc.packages.el`:
        ```emacs-lisp
        ;;;;; Modeline
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 243:</span>
          rc.packages.el
        </div>

<!--list-separator-->

2.  Общие настройки modeline

    -   Загрузим только конфигурационный файл:
        ```emacs-lisp
        (desire-conf 'modeline)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 244:</span>
          rc.packages.el
        </div>

    -   Заголовок файла:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Configure modeline
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 245:</span>
          packages/modeline.ecf
        </div>
    -   Показывать столбец, в котором находится курсор (<https://www.gnu.org/software/emacs/manual/html_node/efaq/Displaying-the-current-line-or-column.html>):
        ```emacs-lisp
        ;;; Show column number
        (setopt column-number-mode t)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 246:</span>
          packages/modeline.ecf
        </div>
    -   Задаём 24-часовой формат времени:
        ```emacs-lisp
        ;;; Time in 24 hour format, plus day and date.
        (setopt display-time-day-and-date t)
        (setopt display-time-24hr-format t)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 247:</span>
          packages/modeline.ecf
        </div>
    -   Мы можем захотеть видеть и секунды:
        ```emacs-lisp
        ;;; Display time in seconds in the mode line
        ;;; %H is the hour on a 24-hour clock, %I is on a 12-hour clock,
        ;;; %k is like %H only blank-padded, %l is like %I blank-padded.
        ;;; %p is the locale's equivalent of either AM or PM.
        ;;; %M is the minute, %S is the second.
        (setopt display-time-format "%H:%M:%S")
        (setopt display-time-interval 1)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 248:</span>
          packages/modeline.ecf
        </div>

    -   Разрешим показывать время в модлайн:
        ```emacs-lisp
        ;;; Enable the display of time and CPU load average in the modeline
        (display-time-mode 1)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 249:</span>
          packages/modeline.ecf
        </div>


#### <span class="section-num">3.45.3</span> Темы {#темы}

-   Подключаем темы в файле `rc.packages.el`:
    ```emacs-lisp
    ;;;;; Themes

    ;;; Nested menu for minor modes
    (desire 'minions)

    ;;; Tabs and ribbons for the mode-line
    (desire 'moody)

    ;;; Spacemacs theme
    ;; (desire 'spacemacs-theme :precondition-lisp-library "spacemacs-theme-pkg")

    ;;; Doom themes
    ;; (desire 'doom-themes)

    ;; (desire 'zenburn-theme)
    ;; (desire 'lambda-themes :recipe '(:fetcher github :repo "Lambda-Emacs/lambda-themes" :branch "main"))
    ;; (desire 'tao-theme)

    ;;; N Λ N O Theme
    ;; (desire 'nano-theme)

    ;;; Increase the padding/spacing of frames and windows
    ;; (desire 'spacious-padding)

    ```

<!--list-separator-->

1.  Modus-themes

    -   [Emacs. Темы. Modus-themes]({{< relref "2023-02-15-emacs-themes-modus-themes" >}})

    <!--list-separator-->

    1.  Подключение

        -   Подключаем темы в файле `rc.packages.el`:
            ```emacs-lisp
            (desire 'modus-themes)
            ```

    <!--list-separator-->

    2.  Загрузка

        -   Файл: `packages/modus-themes/loaddefs.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Modus Themes
            ;; https://protesilaos.com/modus-themes/
            ;; https://gitlab.com/protesilaos/modus-themes/
            ;; https://github.com/protesilaos/modus-themes/

            ;;; Code:

            (require 'modus-themes)

            ;;;
            ```

    <!--list-separator-->

    3.  Конфигурация

        -   Файл: `packages/modus-themes/desire.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;; Modus Themes
            ;; https://protesilaos.com/modus-themes/
            ;; https://gitlab.com/protesilaos/modus-themes/
            ;; https://github.com/protesilaos/modus-themes/

            ;;; Code:

            (modus-themes-include-derivatives-mode 1)

            ;;;; With a non-nil value (t) display several syntactic constructs in bold weight.
            (setopt modus-themes-bold-constructs t)

            ;;;; With a non-nil value (t) choose to render more faces in slanted text.
            (setopt modus-themes-italic-constructs t)

            ;;;; Toggle the use of monospaced fonts for spacing-sensitive constructs
            (setopt modus-themes-mixed-fonts t)
            (setopt modus-themes-variable-pitch-ui t)
            (setopt modus-themes-custom-auto-reload t)
            (setopt modus-themes-common-palette-overrides nil)
            (setopt modus-themes-to-rotate modus-themes-items)

            (setopt modus-themes-italic-constructs t)
            (setopt modus-themes-bold-constructs t)

            ;;;; Control the style of command prompts
            (setopt modus-themes-prompts '(bold))

            ;;;; Set the overall style of completion framework interfaces
            (setopt modus-themes-completions '((t . (bold))))

            ;;;; Optionally add a key binding for the toggle between the themes:
            ;; (define-key global-map (kbd "<f5>") #'modus-themes-toggle)

            ;;;
            ```

    <!--list-separator-->

    4.  Персональные настройки

        -   Файл: `packages/modus-themes/personal.ecf`
            ```emacs-lisp
            ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
            ;;;; Modus Themes
            ;; https://protesilaos.com/modus-themes/
            ;; https://gitlab.com/protesilaos/modus-themes/
            ;; https://github.com/protesilaos/modus-themes/

            ;;; Main themes
            ;;; modus-operandi is the project's main light theme, while modus-vivendi is its dark counterpart
            ;;; Light theme
            ;; (modus-themes-load-theme 'modus-operandi)
            ;;; Dark theme
            ;; (modus-themes-load-theme 'modus-vivendi)
            ;;; Switch themes
            ;; (setopt modus-themes-to-toggle '(modus-operandi modus-vivendi))

            ;;; Tinted themes
            ;;; modus-operandi-tinted and modus-vivendi-tinted are variants of the two main themes
            ;;; Light theme
            (modus-themes-load-theme 'modus-operandi-tinted)
            ;;; Dark theme
            ;; (modus-themes-load-theme 'modus-vivendi-tinted)
            ;;; Switch themes
            (setopt modus-themes-to-toggle '(modus-operandi-tinted modus-vivendi-tinted))

            ;;; Deuteranopia themes
            ;;; modus-operandi-deuteranopia and its companion modus-vivendi-deuteranopia are optimized for users with red-green color deficiency
            ;;; Light theme
            ;; (modus-themes-load-theme 'modus-operandi-deuteranopia)
            ;;; Dark theme
            ;; (modus-themes-load-theme 'modus-vivendi-deuteranopia)
            ;;; Switch themes
            ;; (setopt modus-themes-to-toggle '(modus-operandi-deuteranopia modus-vivendi-deuteranopia))

            ;;; Tritanopia themes
            ;;; modus-operandi-tritanopia and its companion modus-vivendi-tritanopia are optimized for users with red-green color deficiency
            ;;; Light theme
            ;; (modus-themes-load-theme 'modus-operandi-tritanopia)
            ;;; Dark theme
            ;; (modus-themes-load-theme 'modus-vivendi-tritanopia)
            ;;; Switch themes
            ;; (setopt modus-themes-to-toggle '(modus-operandi-tritanopia modus-vivendi-tritanopia))

            ;;;
            ```

<!--list-separator-->

2.  Ef-themes

    -   [Emacs. Темы. Ef-themes]({{< relref "2023-06-13-emacs-themes-ef-themes" >}})
    -   Подключаем темы в файле `rc.packages.el`:
        ```emacs-lisp
        ;; (desire 'ef-themes)
        ```

<!--list-separator-->

3.  Doric-themes

    -   Подключаем темы в файле `rc.packages.el`:
        ```emacs-lisp
        ;; (desire 'doric-themes)
        ```
    -   Загружаем темы:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Doric themes for GNU Emacs
        ;; https://github.com/protesilaos/doric-themes

        ;;; Code:

        (require 'doric-themes)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 250:</span>
          packages/doric-themes/loaddefs.ecf
        </div>
    -   Конфигурация:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Doric themes for GNU Emacs
        ;; https://github.com/protesilaos/doric-themes

        ;;; Code:

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 251:</span>
          packages/doric-themes/desire.ecf
        </div>
    -   Поддержка Moody:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Tabs and ribbons for the mode-line
        ;; https://github.com/tarsius/moody

        ;;; Code:

        (require 'moody)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 252:</span>
          packages/doric-themes/moody.ecf
        </div>
    -   Выбор темы:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Doric themes for GNU Emacs
        ;; https://github.com/protesilaos/doric-themes

        ;;; Code:

        ;;;; light + dark
        ;; (setopt doric-themes-to-toggle '(doric-light doric-dark))
        ;; (doric-themes-select 'doric-light)

        ;;;; marble + obsidian
        ;; (setopt doric-themes-to-toggle '(doric-marble doric-obsidian))
        ;; (doric-themes-select 'doric-marble)

        ;;;; earth + fire
        ;; (setopt doric-themes-to-toggle '(doric-earth doric-fire))
        ;; (doric-themes-select 'doric-earth)

        ;;;; wind + water
        ;; (setopt doric-themes-to-toggle '(doric-wind doric-water))
        ;; (doric-themes-select 'doric-wind)

        ;;;; cherry + plum
        ;; (setopt doric-themes-to-toggle '(doric-cherry doric-plum))
        ;; (doric-themes-select 'doric-cherry)

        ;;;; oak + pine
        (setopt doric-themes-to-toggle '(doric-oak doric-pine))
        (doric-themes-select 'doric-oak)


        ;;;; Rotate themes
        (setopt doric-themes-to-rotate doric-themes-collection)

        ;;;; To load a random theme instead, use something like one of these:
        ;; (doric-themes-load-random)
        ;; (doric-themes-load-random 'light)
        ;; (doric-themes-load-random 'dark)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 253:</span>
          packages/doric-themes/personal.ecf
        </div>


#### <span class="section-num">3.45.4</span> Внешний вид {#внешний-вид}

<!--list-separator-->

1.  Posframe

    -   Дочерний фрейм в точке.
    -   <https://github.com/tumashu/posframe>
    -   Подключение:
        ```emacs-lisp
        ;; (desire 'posframe)
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 254:</span>
          rc.packages.el
        </div>
    -   Загрузка:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Pop a posframe (just a child-frame) at point
        ;; https://github.com/tumashu/posframe

        ;;; Code:

        (require 'posframe)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 255:</span>
          packages/posframe/loaddefs.ecf
        </div>
    -   Настройка:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Pop a posframe (just a child-frame) at point
        ;; https://github.com/tumashu/posframe

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 256:</span>
          packages/posframe/desire.ecf
        </div>
    -   Поддержка _vertico_:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Vertico-posframe is an vertico extension, which lets vertico use posframe to show its candidate menu
        ;; https://github.com/tumashu/vertico-posframe

        (desire 'vertico-posframe)

        (require 'vertico-posframe)
        ;; (vertico-posframe-mode 1)

        (setopt vertico-multiform-commands
              '((consult-line
                 posframe
                 (vertico-posframe-poshandler . posframe-poshandler-frame-top-center)
                 (vertico-posframe-border-width . 10)
                 ;; NOTE: This is useful when emacs is used in both in X and
                 ;; terminal, for posframe do not work well in terminal, so
                 ;; vertico-buffer-mode will be used as fallback at the
                 ;; moment.
                 (vertico-posframe-fallback-mode . vertico-buffer-mode))
                (t posframe)))
        (vertico-multiform-mode 1)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 257:</span>
          packages/posframe/vertico.ecf
        </div>

<!--list-separator-->

2.  Nova

    -   Репозиторий: <https://github.com/thisisran/nova>
    -   Прорисовка дочерних фреймов с помощью SVG.
    -   Подключение:
        ```emacs-lisp
        (desire 'eldoc-box)
        ;; (desire 'nova :recipe '(:fetcher github :repo "thisisran/nova" :branch "main"))
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 258:</span>
          rc.packages.el
        </div>
    -   Загрузка:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Emacs SVG Child Frames
        ;;;; https://github.com/thisisran/nova

        (require 'nova)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 259:</span>
          packages/nova/loaddefs.ecf
        </div>
    -   Настройка:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Emacs SVG Child Frames
        ;;;; https://github.com/thisisran/nova

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 260:</span>
          packages/nova/desire.ecf
        </div>
    -   Поддержка _vertico_:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Emacs SVG Child Frames
        ;;;; https://github.com/thisisran/nova

        (require 'nova-vertico)
        (nova-vertico-mode 1)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 261:</span>
          packages/nova/vertico.ecf
        </div>
    -   Поддержка _corfu_:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Emacs SVG Child Frames
        ;;;; https://github.com/thisisran/nova

        (require 'nova-corfu)
        (require 'nova-corfu-popupinfo)

        (nova-corfu-mode 1)
        (nova-corfu-popupinfo-mode 1)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 262:</span>
          packages/nova/corfu.ecf
        </div>
    -   Поддержка _eldoc-box_:
        ```emacs-lisp
        ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
        ;;; Emacs SVG Child Frames
        ;;;; https://github.com/thisisran/nova

        ;; (require 'nova-eldoc)
        ;; (nova-eldoc-mode 1)

        ;;;
        ```
        <div class="src-block-caption">
          <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 263:</span>
          packages/nova/eldoc-box.ecf
        </div>

<!--list-separator-->

3.  Zoom

    ```emacs-lisp
    ;; (desire 'zoom)
    ```


### <span class="section-num">3.46</span> Финализирование {#финализирование}

-   Финализируем файл `rc.packages.el`:
    ```emacs-lisp
    ;;; rc.packages.el ends here
    ```
