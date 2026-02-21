---
title: "Emacs. Julia. Julia Snail"
author: ["Dmitry S. Kulyabov"]
date: 2023-11-23T19:50:00+03:00
lastmod: 2023-11-23T20:50:00+03:00
tags: ["emacs", "programming", "julia"]
categories: ["computer-science", "science"]
draft: false
slug: "emacs-julia-julia-snail"
---

Пакет _Julia Snail_ для Emacs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/gcv/julia-snail>
-   Эмуляторы терминала: vterm или Eat для отображения REPL.
-   Обеспечивает связь между кодом Julia и процессом Julia, работающим в REPL.
-   Позволяет загружать целые файлы и отдельные функции в запущенные процессы Julia.
-   Удалённые REPL.
-   Мультимедиа и построение графиков.
-   Использует CSTParser (<https://github.com/julia-vscode/CSTParser.jl>) для определения структуры исходных файлов.


## <span class="section-num">2</span> Основные сочетания клавиш {#основные-сочетания-клавиш}

| Комбинация | Команда                           | Описание                                              |
|------------|-----------------------------------|-------------------------------------------------------|
| `C-c C-z`  | `julia-snail`                     | Запуск REPL; переключение между REPL и исходным кодом |
| `C-c C-a`  | `julia-snail-package-activate`    | Активация проекта, используя `Project.toml`           |
| `C-c C-d`  | `julia-snail-doc-lookup`          | Отображает документацию для идентификатора            |
| `C-c C-l`  | `julia-snail-send-line`           | Скопировать строку в REPL                             |
| `C-c C-r`  | `julia-snail-send-region`         | Скопировать регион в REPL                             |
| `C-c C-e`  | `julia-snail-send-dwim`           | Скопировать в REPL то, что надо                       |
| `C-c C-c`  | `julia-snail-send-top-level-form` | Послать блок                                          |
| `C-M-x`    | `julia-snail-send-top-level-form` | Послать блок                                          |
| `C-c C-k`  | `julia-snail-send-buffer-file`    | Послать файл                                          |
| `C-c C-R`  | `julia-snail-update-module-cache` | Обновить кэш модулей                                  |


## <span class="section-num">3</span> Использование {#использование}

-   Откройте исходный файл Julia.
-   Запустите REPL Julia, используя `M-x julia-snail` или `C-c C-z`.
    -   Это загрузит весь вспомогательный код на стороне Julia, который требуется Snail, и запустит сервер.
    -   Сервер работает через TCP-порт (по умолчанию 10011) на локальном хосте.
    -   Вы увидите `JuliaSnail.start(<port>)` в REPL.
-   Если программа Julia использует `Pkg`, запустите `M-x julia-snail-package-activate` или `C-c C-a` для его включения.
-   Загрузите текущий исходный файл Julia, используя `M-x julia-snail-send-buffer-file` или `C-c C-k`.
    -   REPL не отображает вызов `include()`.
    -   Чтобы прервать задачу Julia, запущенную со стороны Emacs, используйте `julia-snail-interrupt-task`.
