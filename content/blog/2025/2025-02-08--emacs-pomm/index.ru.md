---
title: "Emacs. Пакет pomm"
author: ["Dmitry S. Kulyabov"]
date: 2025-02-08T17:30:00+03:00
lastmod: 2025-02-08T18:12:00+03:00
tags: ["emacs"]
categories: ["self-management", "computer-science"]
draft: false
slug: "emacs-pomm"
---

Emacs. Пакет pomm.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Страница: <https://sqrtminusone.xyz/packages/pomm/>
-   Репозиторий: <https://github.com/SqrtMinusOne/pomm.el>
-   Реализация техник _Pomodoro_ (см. [Метод pomodoro]({{< relref "2022-12-18-pomodoro" >}})) и _Third Time_.
-   Управление на основе transient (см.  [Emacs. Пакет transient]({{< relref "2024-10-26-emacs-transient" >}})).


## <span class="section-num">2</span> Использование {#использование}

-   Запустите `M-x pomm`.
-   Откроется transient-буфер.
-   Таймер может иметь 3 состояния.
    -   Выключенный.
        -   Можно запустить с `s` или `M-x pomm-start`.
        -   Запустится таймер.
    -   На паузе.
        -   Можно продолжить с `s` или `M-x pomm-start`.
        -   Можно полностью остановить с `S` или `M-x pomm-stop`.
    -   Работает.
        -   Можно поставить на паузу с `p` или `M-x pomm-pause`.
        -   Можно остановить с `S` или `M-x pomm-stop`.
-   Состояние таймера может быть сброшено с `R` или `M-x pomm-reset`.
-   `U` обновляет transient-буфер.
-   С `r` или `M-x pomm-set-context` можно установить текущий контекст, то есть описание задачи, над которой вы в настоящее время работаете.
-   Это описание будет отображаться в истории и в файле CSV.
-   `M-x pomm-start-with-context` запрашивает контекст, а затем запускает таймер.


## <span class="section-num">3</span> Оповещения {#оповещения}

-   Пакет отправляет оповещения через `alert.el`
-   Стиль оповещения по умолчанию - простой `message`, но если вы хотите графическое уведомление, установите `alert-default-style`:
    ```emacs-lisp
    (setq alert-default-style 'libnotify)
    ```


## <span class="section-num">4</span> Звуки {#звуки}

-   По умолчанию звуки отключены.
-   Установите `pomm-audio-enabled` в `t` для включения.
-   Установите `pomm-audio-tick-enabled` в `t`, если вы хотите тикающий звук во время работы.


## <span class="section-num">5</span> Интерфейс к polybar {#интерфейс-к-polybar}

-   Для отображения состояния Pomodoro в чем-то типа polybar:
    ```emacs-lisp
    (add-hook 'pomm-on-tick-hook 'pomm-update-mode-line-string)
    (add-hook 'pomm-on-status-changed-hook 'pomm-update-mode-line-string)
    ```
-   Для получения информации создайте сценарий:
    ```shell
    if ps -e | grep emacs >> /dev/null
    then
        emacsclient --eval "(if (boundp 'pomm-current-mode-line-string) pomm-current-mode-line-string \"\") " | xargs echo -e
    fi
    ```
-   Добавьте определение модуля polybar:

<!--listend-->

```conf-unix
[module/pomm]
type = custom/script
exec = /home/pavel/bin/polybar/pomm.sh
interval = 1
```


## <span class="section-num">6</span> Расположение файла состояния {#расположение-файла-состояния}

-   Чтобы сохранить состояние между сеансами emacs, пакет хранит своё состояние в следующих файлах:
-   `pomm-state-file-location`, `.emacs.d/pomm`  по умолчанию.
-   `pomm-third-time-state-file-location`, `/.emacs.d/pomm-third-time`  по умолчанию.


## <span class="section-num">7</span> История в формате csv {#история-в-формате-csv}

-   Если вы установите переменную `pomm-csv-history-file`, пакет будет регистрировать свою историю в формате CSV.
-   Файл для техники Pomodoro имеет следующие столбцы:
    -   `timestamp`
    -   `status` ( `stopped`, `paused` или `running`)
    -   `kind` ( `work`, `short-break`, `long-break` или `nil` )
    -   `iteration`
    -   `context`
-   Чтобы настроить временную метку, установите переменную `pomm-csv-history-file-timestamp-format`.
-   Например, для традиционных `YYYY-MM-DD HH:mm:ss`:
    ```emacs-lisp
    (setq pomm-csv-history-file-timestamp-format "%F %T")
    ```
-   Формат такой же, как и в `format-time-string`.


## <span class="section-num">8</span> Использование с `org-clock` {#использование-с-org-clock}

-   Пакет можно интегрировать с org-mode:
    ```emacs-lisp
    (add-hook 'pomm-on-status-changed-hook #'pomm--sync-org-clock)
    (add-hook 'pomm-third-time-on-status-changed-hook #'pomm-third-time--sync-org-clock)
    ```
-   Запустите таймер `pomm` и `org-clock-in`, в любом порядке.
-   Пакет вызовет `org-clock-out`, когда начнётся перерыв.
-   Пакет вызовет `org-clock-in-last`, когда перерыв закончится.
-   Если установить параметр `pomm-org-clock-in-immediately` в `nil`, то вызов `org-clock-in-last` откладывается до тех пор, пока не поступит какая-либо команда от пользователя (через `post-command-hook`).
    -   Это добавлено для того, чтобы при опоздании с перерыва таймер не запускался бы без пользователя.
