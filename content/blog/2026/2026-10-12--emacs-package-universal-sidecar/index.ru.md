---
title: "Emacs. Пакет universal sidecar"
author: ["Dmitry S. Kulyabov"]
date: 2026-10-12T16:20:00+03:00
lastmod: 2026-10-12T17:35:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-package-universal-sidecar"
---

Emacs. Пакет universal sidecar.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий:
    -   <https://git.sr.ht/~swflint/emacs-universal-sidecar>
    -   <https://github.com/emacsmirror/universal-sidecar>
-   Доступен в MELPA.

-   `universal-sidecar` --- это пакет для Emacs, который создаёт боковой буфер (sidecar), показывающий контекстную информацию о текущем активном буфере.
-   Позволяет выводить в отдельной панели различные секции с данными.
-   Пакет требует `magit` (точнее, `magit-section`).


## <span class="section-num">2</span> Загрузка {#загрузка}

```elisp
(require 'universal-sidecar)
```


## <span class="section-num">3</span> Базовая настройка {#базовая-настройка}


### <span class="section-num">3.1</span> Активация и деактивация {#активация-и-деактивация}

-   `M-x universal-sidecar-toggle` : открыть/закрыть sidecar-буфер для текущего фрейма.
-   `M-x universal-sidecar-insinuate` --- автоматически обновлять sidecar.
-   `M-x universal-sidecar-uninsinuate` --- отменить автоматическое обновление.

<!--listend-->

```elisp
(universal-sidecar-insinuate)
```


### <span class="section-num">3.2</span> Имя буфера {#имя-буфера}

-   Формат имени sidecar-буфера задаётся переменной `universal-sidecar-buffer-name-format`, которая должна содержать `%F` --- описание фрейма:

<!--listend-->

```elisp
(setq universal-sidecar-buffer-name-format "*Sidecar: %F*")
```


### <span class="section-num">3.3</span> Таймер обновления {#таймер-обновления}

-   Если `universal-sidecar-enable-timer` не `nil`, sidecar будет обновляться по таймеру простоя.
-   Время настраивается через `universal-sidecar-refresh-time`:

<!--listend-->

```elisp
(setq universal-sidecar-enable-timer t
      universal-sidecar-refresh-time 1.0) ; секунды
```


### <span class="section-num">3.4</span> Игнорирование буферов {#игнорирование-буферов}

-   Буферы можно исключить из отображения в sidecar с помощью регулярного выражения `universal-sidecar-ignore-buffer-regexp` или хука `universal-sidecar-ignore-buffer-functions`:

<!--listend-->

```elisp
(setq universal-sidecar-ignore-buffer-regexp "^ \\*Minibuf")
```


## <span class="section-num">4</span> Настройка секций {#настройка-секций}

-   Секции --- это блоки информации, отображаемые в sidecar.
-   Они задаются переменной `universal-sidecar-sections`.


### <span class="section-num">4.1</span> Добавление секции {#добавление-секции}

```elisp
(add-to-list 'universal-sidecar-sections 'buffer-git-status)
```

-   `add-to-list` добавляет элемент в начало списка.
-   Можно использовать `setq` с явным списком:

<!--listend-->

```elisp
(setq universal-sidecar-sections
      '(buffer-git-status
        buffer-file-name
        buffer-major-mode))
```


### <span class="section-num">4.2</span> Передача аргументов {#передача-аргументов}

-   Некоторые секции принимают ключевые аргументы.
-   Например, `buffer-git-status` поддерживает `:show-renames` (по умолчанию `t`).
-   Чтобы отключить отображение переименований:

<!--listend-->

```elisp
(setq universal-sidecar-sections
      '((buffer-git-status :show-renames nil)
        buffer-file-name))
```


### <span class="section-num">4.3</span> Встроенные секции {#встроенные-секции}

-   Пакет предоставляет несколько готовых секций:
    -   `buffer-git-status` --- статус Git для текущего файла.
    -   `buffer-file-name` --- имя файла.
    -   `buffer-major-mode` --- основной режим.
    -   `buffer-minor-modes` --- активные минорные режимы.
    -   `buffer-position` --- позиция курсора.
    -   `buffer-project` --- информация о проекте (если используется `project.el`).


### <span class="section-num">4.4</span> Создание собственной секции {#создание-собственной-секции}

-   Секция --- это функция, которая принимает буфер и вставляет информацию с помощью `magit-section`:

<!--listend-->

```elisp
(defun my/sidecar-buffer-size (buffer)
  "Показать размер BUFFER в байтах."
  (magit-insert-section (sidecar-buffer-size)
    (magit-insert-heading "Размер буфера:")
    (insert (format "%s байт" (buffer-size buffer)))))

(add-to-list 'universal-sidecar-sections 'my/sidecar-buffer-size)
```


## <span class="section-num">5</span> Настройка отображения {#настройка-отображения}


### <span class="section-num">5.1</span> Формат ID буфера {#формат-id-буфера}

-   Имя sidecar-буфера в списке буферов формируется с помощью `universal-sidecar-buffer-id-format` и `universal-sidecar-buffer-id-formatters`.
-   Последняя --- это alist пар символ/функция, где функция принимает буфер и возвращает строку:

<!--listend-->

```elisp
(setq universal-sidecar-buffer-id-format "%f")
(setq universal-sidecar-buffer-id-formatters
      '((?f . (lambda (buf) (buffer-name buf)))))
```


### <span class="section-num">5.2</span> Шрифтофикация {#шрифтофикация}

-   Для подсветки секций используйте `universal-sidecar-fontify-as`.
-   Макрос позволяет временно установить буфер-локальные переменные перед включением режима:

<!--listend-->

```elisp
(universal-sidecar-fontify-as my-section
  ((my-local-var t))
  (emacs-lisp-mode))
```


## <span class="section-num">6</span> Продвинутая настройка {#продвинутая-настройка}


### <span class="section-num">6.1</span> Автоматическое открытие sidecar {#автоматическое-открытие-sidecar}

-   Можно настроить автоматическое открытие sidecar при входе в определённые режимы:

<!--listend-->

```elisp
(add-hook 'prog-mode-hook
          (lambda ()
            (unless (get-buffer-window universal-sidecar-buffer-name-format)
              (universal-sidecar-toggle))))
```


### <span class="section-num">6.2</span> Интеграция с `project.el` {#интеграция-с-project-dot-el}

-   Если вы используете `project.el`, можно добавить секцию с информацией о проекте:

<!--listend-->

```elisp
(add-to-list 'universal-sidecar-sections 'buffer-project)
```


### <span class="section-num">6.3</span> Настройка `universal-sidecar-advise-commands` {#настройка-universal-sidecar-advise-commands}

-   Переменная `universal-sidecar-advise-commands` содержит список команд, после выполнения которых sidecar должен обновляться.
-   Можно дополнить её своими командами:

<!--listend-->

```elisp
(add-to-list 'universal-sidecar-advise-commands 'my-command)
```
