---
title: "Emacs. Org-transclusion"
author: ["Dmitry S. Kulyabov"]
date: 2025-12-30T14:43:00+03:00
lastmod: 2025-12-30T21:40:00+03:00
draft: false
slug: "emacs-org-transclusion"
---

Emacs. Org-transclusion.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Org-transclusion реализует концепцию _трансклюзии_ (англ. _transclusion_) применительно к текстовым файлам.
-   Репозиторий: <https://github.com/nobiot/org-transclusion>
-   Документация: <https://nobiot.github.io/org-transclusion/>
-   Лицензия: GPLv3.


### <span class="section-num">1.1</span> Основная идея {#основная-идея}

-   Трансклюзия в общем смысле (в информатике) есть включение части или всего электронного документа в один или несколько других документов через гипертекстовую ссылку.
-   Это позволяет:
    -   собирать сложные документы из модульных блоков, хранящихся отдельно;
    -   обновлять контент централизованно: изменения в исходном файле автоматически отражаются во всех местах, где он трансклюдирован;
    -   избегать дублирования данных.


### <span class="section-num">1.2</span> Как работает {#как-работает}

-   Пакет позволяет вставлять содержимое из одного файла в другой (через _файловые ссылки_ или _ID-ссылки_ ), сохраняя при этом:
    -   чистоту файловой системы --- в целевом файле хранятся только ссылки, а не копии текста;
    -   актуальность данных --- при изменении исходного файла трансклюдированные копии обновляются (вручную или через «живую синхронизацию»).


### <span class="section-num">1.3</span> Возможности {#возможности}

1.  Вставка контента из любых текстовых файлов (код, Markdown, другие Org-файлы).
2.  Фильтрация элементов : можно выбирать, какие части исходного файла включать (например, исключать блоки свойств).
3.  Управление уровнями заголовков : настройка отображения заголовков из исходного файла.
4.  Трансклюзия диапазонов строк : выбор конкретных строк текста или кода для включения.
5.  Поддержка сетевых протоколов : работа с контентом по HTTP и другим протоколам.
6.  Живая синхронизация (live-sync) : автоматическое обновление трансклюзий при изменении исходного файла.
7.  Интеграция с Org-roam : бесшовная работа с методом ведения заметок Zettelkasten.


### <span class="section-num">1.4</span> Примеры использования {#примеры-использования}

-   Написание книг : сборка черновика из заметок, быстрая переорганизация контента.
-   Академическая работа : включение цитат и заметок из исследовательского хранилища в разные статьи.
-   Техническая документация : вставка фрагментов кода, которые обновляются при изменении исходного файла.
-   Отчётность по проектам : использование общих заметок для отчётов по нескольким проектам.


## <span class="section-num">2</span> Использование {#использование}


### <span class="section-num">2.1</span> Создание трансклюзии {#создание-трансклюзии}


#### <span class="section-num">2.1.1</span> Способ 1: Из существующей ссылки {#способ-1-из-существующей-ссылки}

-   Создайте в файле ссылку (ID или файловую):
    `[[id:20210501T171427.051019][Bertrand Russell]]`
    или
    `[[file:path/to/file.org]]`.
-   Поместите курсор на ссылку.
-   Выполните команду:
    `M-x org-transclusion-make-from-link`
    Это добавит строку вида:
    `#+transclude: [[id:20210501T171427.051019][Bertrand Russell]]`.
-   Поместите курсор на строку `#+transclude:` и выполните:
    `M-x org-transclusion-add`
    -   Содержимое из исходного файла будет вставлено.


#### <span class="section-num">2.1.2</span> Способ 2: Ручное добавление {#способ-2-ручное-добавление}

-   Вставьте строку вручную:

`#+transclude: [[file:path/to/file.org]]`

-   Пакет автоматически обработает её (при активированном режиме).


### <span class="section-num">2.2</span> Управление трансклюзиями {#управление-трансклюзиями}

-   Клавиатурные команды:
    -   `o` : открыть исходный буфер трансклюзии.
    -   `O` : переместиться к исходному буферу.
    -   `g` : обновить трансклюзию (перечитать исходный файл).
    -   `e` : запустить _live-sync_ (редактирование с автоматическим обновлением источника).
    -   `d` : удалить трансклюзию.
    -   `C-c C-c` : завершить _live-sync_ после редактирования.


### <span class="section-num">2.3</span> Автоматическое добавление трансклюзий {#автоматическое-добавление-трансклюзий}

-   Включите `org-transclusion-mode` в буфере:

`M-x org-transclusion-mode`

-   При этом (если переменная `org-transclusion-add-all-on-activate` = `t`) все `#+transclude:` строки будут обработаны автоматически.


### <span class="section-num">2.4</span> Фильтрация контента {#фильтрация-контента}

-   Чтобы исключить определённые элементы Org (например, `property-drawer`).
-   Глобально:
    `(setq org-transclusion-exclude-elements '(property-drawer))`
-   Локально для трансклюзии:
    `#+transclude: [[file:path.org]] :exclude property-drawer`


### <span class="section-num">2.5</span> Расширенные возможности {#расширенные-возможности}

-   Включение диапазона строк:
    `#+BEGIN: transclusion :filename "path.org" :min 2 :max 4`
    (вставляет строки 2--4 из файла).
-   Трансклюзия первой секции файла (до первого заголовка):
    настройте `(setq org-transclusion-include-first-section t)`.
-   Интеграция с `org-roam` : трансклюзии работают бесшовно с  заметками в Zettelkasten-методе.


### <span class="section-num">2.6</span> Настройка клавиш {#настройка-клавиш}

-   Если стандартные привязки неудобны, переопределите их в `org-transclusion-map`:

<!--listend-->

```emacs-lisp
(define-key org-transclusion-map (kbd "j") 'org-transclusion-refresh)
```


## <span class="section-num">3</span> Расширения org-transclusion {#расширения-org-transclusion}

-   Пакет `org-transclusion=` поддерживает ряд расширений, расширяющих базовые возможности трансклюзии.


### <span class="section-num">3.1</span> HTML-расширение (`org-transclusion-html`) {#html-расширение--org-transclusion-html}

-   Назначение: позволяет трансклюдировать локальные HTML-файлы, конвертируя их в формат Org с помощью Pandoc.
-   Требования: установленный pandoc (должен быть в `PATH` системы).
-   Как включить:

<!--listend-->

```emacs-lisp
(with-eval-after-load 'org-transclusion
  (add-to-list 'org-transclusion-extensions 'org-transclusion-html)
  (require 'org-transclusion-html))
```

-   Пример использования:

<!--listend-->

```org
#+transclude: [[file:path/to/document.html]]
```

-   Особенности:
    -   Конвертируется весь документ целиком (нельзя выбрать отдельные элементы по ID).
    -   Автоматически распознаёт HTML-файлы без расширения `.html` (по декларации `DOCTYPE`).
    -   Не поддерживает _live-sync_.


### <span class="section-num">3.2</span> HTTP-расширение (`org-transclusion-http`) {#http-расширение--org-transclusion-http}

-   Репозиторий: <https://git.sr.ht/~ushin/org-transclusion-http>
-   Назначение: трансклюдирует контент с удалённых HTTP/HTTPS-источников.
-   Как включить:
    -   Установите пакет `org-transclusion-http`.
    -   Добавьте в конфигурацию:

<!--listend-->

```emacs-lisp
(with-eval-after-load 'org-transclusion
  (add-to-list 'org-transclusion-extensions 'org-transclusion-http)
  (require 'org-transclusion-http))
```

-   Пример:

<!--listend-->

```org
#+transclude: [[http://example.com/page.html]]
```

-   Особенности:
    -   Обрабатывает асинхронные запросы (не блокирует Emacs).
    -   Может извлекать подмножества DOM (например, по ID элемента).
    -   Поддерживает извлечение секций документа по заголовкам.


### <span class="section-num">3.3</span> Расширения для протокола hyperdrive {#расширения-для-протокола-hyperdrive}

-   Репозиторий: <https://git.sr.ht/~ushin/hyperdrive-org-transclusion>
-   Пример включения:

<!--listend-->

```emacs-lisp
(with-eval-after-load 'org-transclusion
  (add-to-list 'org-transclusion-extensions 'hyperdrive-org-transclusion)
  (require 'hyperdrive-org-transclusion))
```

-   Пример использования:

<!--listend-->

```org
#+transclude: [[hyper://aaj45d88g4eenu76rpmwzjiabsof1w8u6fufq6oogyhjk1ubygxy/software.org#::#emacs]]
```


### <span class="section-num">3.4</span> Прочие расширения {#прочие-расширения}

-   Source Lines Extension: управление диапазонами строк (вставка фрагментов кода):
-   Indent and Font-Lock Extensions: настройка отступов и подсветки синтаксиса для трансклюзированного контента.


## <span class="section-num">4</span> Дополнительные пакеты {#дополнительные-пакеты}


### <span class="section-num">4.1</span> org-transclusion-blocks {#org-transclusion-blocks}


#### <span class="section-num">4.1.1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/gggion/org-transclusion-blocks>
-   org-transclusion-blocks реализует трансклюзию на основе заголовков (`header-based transclusion`).
-   Позволяет гибко управлять встраиванием контента из внешних источников в файлы Org Mode, сохраняя структуру и функциональность блоков.


#### <span class="section-num">4.1.2</span> Основная цель {#основная-цель}

-   Решить ограничения базового `org-transclusion`:
    -   Исчезновение ключевых слов.
        -   При стандартной трансклюзии строка `#+transclude:` временно исчезает, нарушая наследование свойств и интеграцию с Babel (например, `:session`, `:results` в src-блоках).
    -   Ограниченная гибкость.
        -   org-transclusion-blocks позволяет определять параметры трансклюзии через явные заголовки, сохраняя структуру блока.


#### <span class="section-num">4.1.3</span> Как работает {#как-работает}

1.  Заголовки для конфигурации. Используются специальные заголовки (`#+HEADER:`) для указания:
    -   источника (`:file-path`);
    -   условий выборки (`:file-search`, `:lines`);
    -   типа трансклюзии (`:transclude-type`).
2.  Построение ссылок. На основе заголовков генерируется строка ссылки, которая передаётся `org-transclusion` для извлечения контента.
3.  Сохранение структуры. Заголовки остаются видимыми, обеспечивая наследование свойств (property drawer) и совместимость с Babel.


#### <span class="section-num">4.1.4</span> Ключевые возможности {#ключевые-возможности}

-   Управление диапазонами строк (`:lines 10-20`).
-   Поиск по заголовкам (`:file-search *Heading`).
-   Типы трансклюзии (например, `file-with-search`).
-   Экранирование синтаксиса для предотвращения конфликтов (автоматическое или ручное через `:transclude-escape-org`).
-   Интеграция с Git (опционально, через `orgit-file` для работы с blob-файлами из репозиториев).


#### <span class="section-num">4.1.5</span> Примеры использования {#примеры-использования}

```org
#+HEADER: :transclude-type file-with-search
#+HEADER: :file-path ~/notes.org
#+HEADER: :file-search *Important Heading
#+HEADER: :transclude-lines 10-20
```

-   Этот блок извлечёт строки 10--20 из раздела «Important Heading» файла `~/notes.org`.


#### <span class="section-num">4.1.6</span> Команды {#команды}

-   `org-transclusion-blocks-add` (рекомендуемая привязка: `C-c n t`) : вставка контента по текущему блоку.
-   `org-transclusion-blocks-describe-type` : показать документацию по типу трансклюзии (например, `M-x org-transclusion-blocks-describe-type RET journal`).
-   `org-transclusion-blocks-list-types` : вывести список зарегистрированных типов.


#### <span class="section-num">4.1.7</span> Переменные {#переменные}

-   `org-transclusion-blocks-escape-org-sources` : автоматическое экранирование синтаксиса Org (по умолчанию `t`).
-   `org-transclusion-blocks-show-interaction-warnings` : показывать предупреждения о конфликтах заголовков (по умолчанию `t`).


#### <span class="section-num">4.1.8</span> Интеграция {#интеграция}

-   Работает поверх `org-transclusion` (требуется его установка).
-   Опционально совместим с `orgit-file` и `org-transclusion-git` для расширенной работы с Git.
