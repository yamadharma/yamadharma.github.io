---
title: "Emacs. Пакет julia-formatter"
author: ["Dmitry S. Kulyabov"]
date: 2026-03-21T16:43:00+03:00
lastmod: 2026-03-21T17:27:00+03:00
tags: ["emacs", "julia", "programming"]
categories: ["computer-science"]
draft: false
slug: "emacs-julia-formatter"
---

Emacs. Пакет julia-formatter.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://codeberg.org/FelipeLema/julia-formatter.el>
-   Использует JuliaFormatter.jl ([Julia. Форматирование кода]({{< relref "2026-03-21--julia-code-formatting" >}})).


## <span class="section-num">2</span> Базовая настройка {#базовая-настройка}

```elisp
(require 'julia-formatter)
(add-hook 'julia-mode-hook #'julia-formatter-mode)
```

-   При каждом сохранении буфера с расширением `.jl` Emacs будет автоматически форматировать код через `JuliaFormatter.jl`.


### <span class="section-num">2.1</span> Проблема первого запуска {#проблема-первого-запуска}

-   Пакет `julia-formatter` запускает `JuliaFormatter.jl` как фоновый JSON-RPC сервис, чтобы избежать задержек при каждом форматировании.
-   При первом вызове форматирования Emacs может зависнуть на несколько секунд или минут.
    -   Julia компилирует форматтер и сохраняет системный образ.
-   При первой загрузке `julia-formatter-mode` Emacs спросит: _Compile Julia system image?_
    -   Нажмите `y` (Yes).
-   Можно выполнить настройку вручную:
    ```elisp
    ;; Принудительно разрешить компиляцию образа
    (setq julia-formatter-should-compile-julia-image 'always-compile)
    ```


### <span class="section-num">2.2</span> Форматирование при наборе {#форматирование-при-наборе}

-   Чтобы код форматировался не только при сохранении, но и по мере набора текста (например, при нажатии `Enter`), используйте `aggressive-indent-mode`:
    ```elisp
    (require 'julia-formatter)
    (add-hook 'julia-mode-hook #'julia-formatter-mode)
    (add-hook 'julia-formatter-mode-hook #'aggressive-indent)
    ```

-   Предварительно установите пакет `aggressive-indent`.


### <span class="section-num">2.3</span> Проверка работоспособности {#проверка-работоспособности}

-   Откройте любой `.jl` файл.
-   Напишите неотформатированный код (например, `x=1`).
-   Сохраните файл (`C-x C-s`).
-   Код должен превратиться в `x = 1`.

-   Если этого не происходит, проверьте:
    -   Установлен ли JuliaFormatter.jl в вашей системе Julia?
    -   Нет ли синтаксических ошибок в коде (незакрытых `end` или скобок)? Пакет требует, чтобы код был синтаксически завершен для парсинга.
