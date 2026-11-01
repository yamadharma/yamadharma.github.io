---
title: "Org-roam. Пакет folgezett"
author: ["Dmitry S. Kulyabov"]
date: 2026-10-30T16:46:00+03:00
lastmod: 2026-10-30T18:22:00+03:00
draft: false
slug: "org-roam-package-folgezett"
---

Org-roam. Пакет folgezett.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/landerwells/folgezett.el>
-   Утилита для автоматической генерации и управления  лумановскими ID ([Нумерация Folgezettel]({{< relref "2025-02-08--folgezettel-numbering" >}})) во время создания заметок.


## <span class="section-num">2</span> Что делает {#что-делает}

-   Пакет перехватывает процесс `org-roam-capture`.
    -   Когда вы создаете новую заметку, Emacs спрашивает: _Это начало новой цепочки (1), ответвление (branch) или продолжение (continue)_.
-   Записывает идентификатор в свойство `FOLGEZETTEL_ID` .
-   Пакет использует точки для разделения (например, `1.1` → `1.1a` → `1.1a1` ).
-   Луман писал слитно ( `1a1`).
-   Точки добавляются для сортировки.
-   Опционально может переименовывать файл, добавляя ID в начало имени (например, `1.1a-название.org` ).
    -   Для просмотра в Dired.


## <span class="section-num">3</span> Функции {#функции}

-   `folgezett-reparent-subtree`
    -   Если ветка должна быть перенесена под другую заметку-родителя, эта команда автоматически пересчитает ID у всех  дочерних заметок.
-   `folgezett-goto-parent`, `folgezett-list-children`
    -   Быстрое перемещение вверх и вниз по иерархии.


## <span class="section-num">4</span> Настройка пакета {#настройка-пакета}


### <span class="section-num">4.1</span> Чистый emacs {#чистый-emacs}

```elisp
;; Загружаем пакет только после org-roam
(with-eval-after-load 'org-roam

  ;; Подключаем пакет
  (require 'folgezett)

  ;; Добавлять ID в начало имени файла (например: "1.1a Система.org")
  (setq folgezett-include-id-in-filename t)

  ;; "Виртуальные" ссылки на родителя в базе данных.
  ;; Если t, то дочерние заметки будут появляться в буфере Backlinks у родителя,
  ;; хотя в самом тексте файла ссылки на родителя НЕ будет (файл остается чистым).
  ;; Требует выполнения M-x org-roam-db-sync после включения.
  (setq folgezett-db-link-parent t)

  ;; Показывать ID в буфере поиска (M-x org-roam-node-find)
  (setq folgezett-show-id-in-completions t)

  ;; Метка для экспорта (при генерации Hugo/PDF и т.д.)
  ;; Если хотите видеть "Previous: [[...]]" в экспорте, оставьте "Previous"
  ;; Если не нужно — установите в nil
  (setq folgezett-export-parent-label "Previous")

  ;; Активация пакета

  ;; Запускаем режим, который добавляет хуки в org-roam-capture
  (folgezett-setup)

  ;; Настройка клавиш (Keybindings)

  ;; Создаем префиксную карту для Zettelkasten
  (define-prefix-command 'ecf/folgezettel-map)
  (global-set-key (kbd "C-c n z") 'ecf/folgezettel-map)

  ;; Создание и управление ID
  (define-key ecf/folgezettel-map (kbd "a") #'folgezett-assign-id)        ; Назначить ID вручную
  (define-key ecf/folgezettel-map (kbd "d") #'folgezett-remove-id)        ; Удалить ID

  ;; Реструктуризация
  (define-key ecf/folgezettel-map (kbd "r") #'folgezett-reparent)         ; Сменить родителя (только у этой заметки)
  (define-key ecf/folgezettel-map (kbd "R") #'folgezett-reparent-subtree) ; Сменить родителя + пересчитать всю ветку детей

  ;; Навигация
  (define-key ecf/folgezettel-map (kbd "p") #'folgezett-goto-parent)      ; Перейти к родителю (Up)
  (define-key ecf/folgezettel-map (kbd "c") #'folgezett-list-children)    ; Выбрать из списка детей (Children)
  (define-key ecf/folgezettel-map (kbd "t") #'folgezett-show-tree))       ; Показать глобальное дерево (Tree)
```


### <span class="section-num">4.2</span> С использованием general {#с-использованием-general}

```emacs-lisp
(require 'general)

;; ==========================================
;; ЗАГРУЗКА И НАСТРОЙКА FOLGEZETT
;; ==========================================
(with-eval-after-load 'org-roam
  (require 'folgezett)

  ;; Настройка переменных
  (setq folgezett-include-id-in-filename t
        folgezett-db-link-parent t
        folgezett-show-id-in-completions t
        folgezett-export-parent-label "Previous")

  ;; Активация пакета
  (folgezett-setup)

  ;; ==========================================
  ;; КЛАВИАТУРНЫЕ СОЧЕТАНИЯ (префикс C-c n z)
  ;; ==========================================
  (general-define-key
   :prefix "C-c n z"
    ;; --- Создание и управление ID ---
    "a" #'("Assign ID" . folgezett-assign-id)
    "d" #'("Remove ID" . folgezett-remove-id)

    ;; --- Реструктуризация ---
    "r" #'("Reparent" . folgezett-reparent)
    "R" #'("Reparent subtree" . folgezett-reparent-subtree)

    ;; --- Навигация ---
    "p" #'("Goto parent" . folgezett-goto-parent)
    "c" #'("List children" . folgezett-list-children)
    "t" #'("Show tree" . folgezett-show-tree))
```


## <span class="section-num">5</span> Команды {#команды}

-   Все команды доступны через префикс `C-c n z`:

| Клавиша     | Команда                      | Назначение                                                                    |
|-------------|------------------------------|-------------------------------------------------------------------------------|
| `C-c n z a` | `folgezett-assign-id`        | Назначить Folgezettel-ID существующей заметке. Открывает диалог выбора якоря. |
| `C-c n z d` | `folgezett-remove-id`        | Удалить все Folgezettel-свойства из заметки и убрать ID из имени файла.       |
| `C-c n z r` | `folgezett-reparent`         | Перенести текущую заметку под нового родителя. Меняется только её ID.         |
| `C-c n z R` | `folgezett-reparent-subtree` | Перенести заметку и переписать ID у всех её потомков.                         |
| `C-c n z p` | `folgezett-goto-parent`      | Мгновенный переход к родительской заметке.                                    |
| `C-c n z c` | `folgezett-list-children`    | Открыть список всех прямых дочерних заметок для выбора.                       |
| `C-c n z t` | `folgezett-show-tree`        | Открыть специальный буфер `*Folgezettel Tree*` со всей иерархией базы.        |

---


## <span class="section-num">6</span> Workflow {#workflow}

-   Пакет автоматически перехватывает `org-roam-capture`.
-   Вы вызываете `org-roam-capture` (обычно `C-c n i`).
-   В минибуфере появляется диалог: Folgezettel anchor:
-   Выбираете существующую заметку (или `[New chain — top-level note]` для новой темы).
-   Нажимаете одну букву:
    -   `b` --- branch (создать ветку внутри, например `1.1` → `1.1a`)
    -   `c` --- continue (создать сестринскую заметку, например `1.1` → `1.2`)
-   ID автоматически записывается в свойство `:FOLGEZETTEL_ID:`,
-   Если включена опция `folgezett-include-id-in-filename`, файл переименовывается в формат `1.1a Название.org`.
