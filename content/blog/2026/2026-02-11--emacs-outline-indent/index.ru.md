---
title: "Emacs. Пакет outline-indent"
author: ["Dmitry S. Kulyabov"]
date: 2026-02-11T17:35:00+03:00
lastmod: 2026-02-11T18:08:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-outline-indent"
---

Emacs. Пакет outline-indent.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/jamescherti/outline-indent.el>
-   Сворачивание кода на основе отступов.
-   Предоставляет минорный режим `outline-indent-minor-mode`, который превращает каждый уровень отступа в полноценный заголовок (heading) для стандартного `outline-minor-mode`.
-   Основан на нативном коде Emacs.
-   Автоматически определяет `indent-offset` из текущего major mode.


## <span class="section-num">2</span> Включение {#включение}

-   Включается как минорный режим:
    ```elisp
    (outline-indent-minor-mode)
    ```

-   Для конкретных режимов:
    ```elisp
    ;; Python
    (add-hook 'python-mode-hook #'outline-indent-minor-mode)
    (add-hook 'python-ts-mode-hook #'outline-indent-minor-mode)

    ;; YAML
    (add-hook 'yaml-mode-hook #'outline-indent-minor-mode)
    (add-hook 'yaml-ts-mode-hook #'outline-indent-minor-mode)

    ;; Для всех режимов программирования
    (add-hook 'prog-mode-hook #'outline-indent-minor-mode)
    ```


## <span class="section-num">3</span> Настройки {#настройки}

| Переменная                                                                     | Назначение                                                                                        | Значение по умолчанию            |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------|
| `outline-indent-default-offset`                                                | Базовая ширина отступа для расчёта уровня вложенности.                                            | 1                                |
| `outline-indent-shift-width`                                                   | Количество пробелов при повышении/понижении уровня (`promote=/=demote`).                          | nil (наследует `default-offset`) |
| `outline-indent-ellipsis`                                                      | Строка, отображаемая вместо свёрнутого содержимого.                                               | nil                              |
| `outline-indent-advise-outline-functions`                                      | Добавляет обёртки (advice) к стандартным функциям `outline` для совместимости. Рекомендуется `t`. | t                                |
| `outline-indent-insert-heading-add-blank-line`                                 | Вставлять ли пустую строку перед новым заголовком.                                                | nil                              |
| `make-window-start-visible` (ранее `outline-indent-make-window-start-visible`) | Гарантирует, что начало окна не останется скрытым. Устанавливается как `setq-local`.              | t                                |

-   При значении `outline-indent-default-offset = 1` пакет работает с любым языком, так как минимальный отступ в 1 пробел уже считается новым уровнем.
-   Однако для корректной работы команд повышения/понижения уровня рекомендуется явно указывать смещение под конкретный язык.


### <span class="section-num">3.1</span> Пример языко-зависимой настройки {#пример-языко-зависимой-настройки}

```elisp
;; Python: 4 пробела
(add-hook 'python-mode-hook
          (lambda ()
            (setq-local outline-indent-default-offset 4)
            (setq-local outline-indent-shift-width 4)))

;; YAML: 2 пробела
(add-hook 'yaml-mode-hook
          (lambda ()
            (setq-local outline-indent-default-offset 2)
            (setq-local outline-indent-shift-width 2)))
```


## <span class="section-num">4</span> Основные функции {#основные-функции}


### <span class="section-num">4.1</span> Управление сворачиванием {#управление-сворачиванием}

| Функция                                | Действие                                          |
|----------------------------------------|---------------------------------------------------|
| `outline-indent-open-fold`             | Развернуть блок под курсором                      |
| `outline-indent-close-fold`            | Свернуть блок под курсором                        |
| `outline-indent-open-folds`            | Развернуть всё                                    |
| `outline-indent-close-folds`           | Свернуть всё                                      |
| `outline-indent-open-fold-rec`         | Развернуть рекурсивно (все вложенные)             |
| `outline-indent-toggle-fold`           | Переключить состояние блока                       |
| `outline-indent-toggle-level-at-point` | Переключить видимость всех блоков текущего уровня |


### <span class="section-num">4.2</span> Навигация {#compass-навигация}

| Функция                              | Действие                                            |
|--------------------------------------|-----------------------------------------------------|
| `outline-indent-forward-same-level`  | Перейти к следующему блоку такого же уровня отступа |
| `outline-indent-backward-same-level` | Перейти к предыдущему блоку такого же уровня        |

-   Если `outline-indent-advise-outline-functions = t`, работают и стандартные `outline-forward-same-level`, `outline-backward-same-level`.


### <span class="section-num">4.3</span> Редактирование структуры {#редактирование-структуры}

| Функция                            | Действие                                                                    |
|------------------------------------|-----------------------------------------------------------------------------|
| `outline-indent-shift-right`       | Увеличить отступ всего блока (понизить уровень)                             |
| `outline-indent-shift-left`        | Уменьшить отступ всего блока (повысить уровень)                             |
| `outline-indent-move-subtree-up`   | Переместить блок выше                                                       |
| `outline-indent-move-subtree-down` | Переместить блок ниже                                                       |
| `outline-indent-insert-heading`    | Вставить новую строку с таким же отступом (аналог `outline-insert-heading`) |
| `outline-indent-select`            | Выделить весь текущий блок (включая вложения)                               |


## <span class="section-num">5</span> Пример конфигурации {#пример-конфигурации}

```elisp
;;; === outline-indent.el ===
(require 'outline-indent)

;; Внешний вид: треугольник вместо "..."
(setq outline-indent-ellipsis " ▼ ")

;; Языко-зависимые настройки отступов
(defun my/set-outline-indent-offset ()
  "Установить offset и shift-width в зависимости от режима."
  (cond
   ((derived-mode-p 'python-mode)
    (setq-local outline-indent-default-offset 4)
    (setq-local outline-indent-shift-width 4))
   ((derived-mode-p 'yaml-mode)
    (setq-local outline-indent-default-offset 2)
    (setq-local outline-indent-shift-width 2))
   ((derived-mode-p 'js-mode)
    (setq-local outline-indent-default-offset 2)
    (setq-local outline-indent-shift-width 2))))

;; Добавляем во все хуки, где включен outline-indent
(add-hook 'outline-indent-minor-mode-hook #'my/set-outline-indent-offset)

;; Включаем режим для всех режимов программирования
(add-hook 'prog-mode-hook #'outline-indent-minor-mode)

;; Чтобы первая строка всегда была видна
(add-hook 'outline-minor-mode-hook
          (lambda () (setq-local make-window-start-visible t)))

;; Персональные клавиши (если не нравится префикс C-c @)
(define-key outline-indent-minor-mode-map (kbd "C-c f") #'outline-indent-close-fold)
(define-key outline-indent-minor-mode-map (kbd "C-c F") #'outline-indent-open-fold)
(define-key outline-indent-minor-mode-map (kbd "C-c a") #'outline-indent-open-folds)
(define-key outline-indent-minor-mode-map (kbd "C-c C-c") #'outline-indent-close-folds)
(define-key outline-indent-minor-mode-map (kbd "C-c n") #'outline-indent-forward-same-level)
(define-key outline-indent-minor-mode-map (kbd "C-c p") #'outline-indent-backward-same-level)
```
