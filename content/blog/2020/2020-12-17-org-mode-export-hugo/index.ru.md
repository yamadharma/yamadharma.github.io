---
title: "Org-mode. Экспорт в Hugo"
author: ["Dmitry S. Kulyabov"]
date: 2020-12-17T11:01:00+03:00
lastmod: 2023-08-13T13:32:00+03:00
tags: ["hugo", "org-mode", "emacs"]
categories: ["computer-science"]
draft: false
slug: "org-mode-export-hugo"
---

Экспорт org-mode в Hugo является одной из составных частей научного рабочего процесса на основе Emacs и org-mode.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Использование языка Markdown внутри Org {#использование-языка-markdown-внутри-org}

-   При экспорте Org преобразуется в стандартный Markdown. Однако в Hugo используются собственные нестандартные расширения (см. [Синтаксис Markdown для генератора сайтов Hugo]({{< relref "2020-11-26-hugo-markdown" >}})).
-   При необходимости их можно вставлять прямо в текст.


## <span class="section-num">2</span> Соответствие языков разметки {#соответствие-языков-разметки}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Соответствие разметок org и markdown
</div>

| Org                | Markdown                                             | После рендеринга                         |
|--------------------|------------------------------------------------------|------------------------------------------|
| `*bold*`           | `**bold**`                                           | **bold**                                 |
| `/italics/`        | `_italics_`                                          | _italics_                                |
| `=monospace=`      | `` `monospace` ``                                    | `monospace`                              |
| `~key-binding~`    | `` `key-binding` ``  [^fn:1]                         | `key-binding`                            |
| `~key-binding~`    | `<kbd>key-binding</kbd>` [^fn:2]                     |                                          |
| `+strike-through+` | `~~strike-through~~`                                 | ~~strike-through~~                       |
| `_underline_`      | `<span class = "underline">underline</span>` [^fn:3] | <span class="underline">underline</span> |


## <span class="section-num">3</span> Настройка экспорта {#настройка-экспорта}

-   Экспорт производится в рамках общего фреймворка org-mode для экспорта (см. [Org-mode. Экспорт]({{< relref "2020-12-10-org-mode-export" >}})).


### <span class="section-num">3.1</span> Экспорт специфических элементов {#экспорт-специфических-элементов}


#### <span class="section-num">3.1.1</span> Экспорт операторов Hugo {#экспорт-операторов-hugo}

-   Для экспорта конкретных элементов, необходимых только для Hugo, следует использовать блок `export`. Например, оглавление задаётся следующим образом:
    ```org
    #+begin_export hugo
    {{</*/* toc */*/>}}
    #+end_export
    ```
-   Это позволяет задавать оглавление только для Hugo.


#### <span class="section-num">3.1.2</span> Отбивка резюме (Summary Splitter) {#отбивка-резюме--summary-splitter}

-   Отбивка резюме задаётся конструкцией
    ```org
    #+hugo: more
    ```


#### <span class="section-num">3.1.3</span> Резюме и подробная информация {#резюме-и-подробная-информация}

-   Специальный блок «Детали» `#+begin_details … #+end_details`  используется для создания элемента, раскрывающего дополнительные сведения (`<details>` и `<summary>`).
    ```org
    #+begin_details
    #+begin_summary
    Краткая информация
    #+end_summary
    А здесь подробная информация.
    #+end_details
    ```

-   Выглядить это так:

    <details>
    <summary>Краткая информация</summary>
    <div class="details">

    А здесь подробная информация.
    </div>
    </details>

-   Если блок `summary` отсутствует, резюме будет заменено на некоторое значение по умолчанию. Так, блок
    ```org
    #+begin_details
    А здесь подробная информация.
    #+end_details
    ```
    будет иметь следующий вид:

    <details>
    <div class="details">

    А здесь подробная информация.
    </div>
    </details>

-   Можно показывать блок открытым по умолчанию. Для этого следует добавить атрибут HTML `#+attr_html: :open t`:
    ```org
    #+attr_html: :open t
    #+begin_details
    #+begin_summary
    Краткая информация
    #+end_summary
    А здесь подробная информация.
    #+end_details
    ```

    <details open>
    <summary>Краткая информация</summary>
    <div class="details">

    А здесь подробная информация.
    </div>
    </details>


### <span class="section-num">3.2</span> Свойства экспорта {#свойства-экспорта}


#### <span class="section-num">3.2.1</span> Обязательные свойства {#обязательные-свойства}

-   Для экспорта необходимо установить следующие обязательные свойства:
    -   `HUGO_SECTION` - название раздела Hugo по умолчанию для всех сообщений. Обычно это свойство устанавливается для сообщений или блога. Значение по умолчанию устанавливается с помощью `org-hugo-default-section-directory`.
    -   `HUGO_BASE_DIR` - корневой каталог сайта Hugo. Например, если `HUGO_BASE_DIR` установлен на `~/hugo/`, то экспортированные файлы Markdown будут сохранены в каталог `~/hugo/content/<HUGO_SECTION>/`.
-   Данные свойства можно устанавливать как на уровне файла, так и на уровне каталога или проекта.
-   Переменные на уровне каталога задаются в файле `.dir-locals.el`:
    ```elisp
    ((org-mode . ((org-hugo-base-dir . "~/work/blog/git")
             (org-hugo-section . "ru/post"))))
    ```


#### <span class="section-num">3.2.2</span> Формат заголовка {#формат-заголовка}

-   Поддерживаются форматы заголовка TOML (по умолчанию) и YAML.

<!--list-separator-->

1.  Экспорт для всего файла

    ```org
    #+hugo_front_matter_format: yaml
    ```

<!--list-separator-->

2.  Экспорт для поддерева

    ```org
    :PROPERTIES:
    :EXPORT_HUGO_FRONT_MATTER_FORMAT: yaml
    :END:
    ```


#### <span class="section-num">3.2.3</span> Свойства экспорта для заголовка Hugo {#свойства-экспорта-для-заголовка-hugo}

<a id="table--hugo-export-properties-front-matter"></a>
<div class="table-caption">
  <span class="table-number"><a href="#table--hugo-export-properties-front-matter">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 2</a>:</span>
  Сводная таблица свойств экспорта для заголовка Hugo
</div>

| Hugo front-matter (TOML)           | Уровень файла                        | Уровень поддерева                       |
|------------------------------------|--------------------------------------|-----------------------------------------|
| `title = "foo"`                    | `#+title: foo`                       | `* foo`                                 |
| `date = 2017-09-11T14:32:00-04:00` |                                      | `CLOSED: [2017-09-11 Mon 14:32]`        |
| `date = 2017-07-24`                | `#+date: 2017-07-24`                 | `:EXPORT_DATE: 2017-07-24`              |
| `publishDate = 2018-01-26`         | `#+hugo_publishdate: 2018-01-26`     | `SCHEDULED: <2018-01-26 Fri>`           |
| `publishDate = 2018-01-26`         |                                      | `:EXPORT_HUGO_PUBLISHDATE: 2018-01-26:` |
| `expiryDate = 2999-01-01`          | `#+hugo_expirydate: 2999-01-01`      | `DEADLINE: <2999-01-01 Tue>`            |
| `expiryDate = 2999-01-01`          |                                      | `:EXPORT_HUGO_EXPIRYDATE: 2999-01-01:`  |
| `lastmod = <current date>`         | `#+hugo_auto_set_lastmod: t`         | `:EXPORT_HUGO_AUTO_SET_LASTMOD: t`      |
| `lastmod = <current date>`         |                                      | `#+hugo_auto_set_lastmod: t`            |
| `tags = ["toto", "zulu"]`          | `#+hugo_tags: toto zulu`             | `* foo :toto:zulu:`                     |
| `categories = ["x", "y"]`          | `#+hugo_categories: x y`             | `* foo :@x:@y:`                         |
| `draft = true`                     | `#+hugo_draft: true`                 | `* TODO foo`                            |
| `draft = false`                    | `#+hugo_draft: false`                | `* foo` или `* DONE foo`                |
| `weight = 123` (manual)            | `#+hugo_weight: 123`                 | `:EXPORT_HUGO_WEIGHT: 123`              |
| `weight = 123` (auto-calc)         |                                      | `:EXPORT_HUGO_WEIGHT: auto`             |
| `tags_weight = 123` (manual)       | `#+hugo_weight: :tags 123`           | `:EXPORT_HUGO_WEIGHT: :tags 123`        |
| `tags_weight = 123` (auto-calc)    |                                      | `:EXPORT_HUGO_WEIGHT: :tags auto`       |
| `weight = 123` (in [menu.foo])     | `#+hugo_menu: :menu foo :weight 123` | `:EXPORT_HUGO_MENU: :menu foo`          |
| `categories_weight = 123`          | `#+hugo_weight: :categories 123`     |                                         |
|                                    |                                      |                                         |


### <span class="section-num">3.3</span> Особенности экспорта {#особенности-экспорта}

-   [Org-roam. Экспорт в Hugo]({{< relref "2022-11-23-org-roam-hugo-export" >}})


## <span class="section-num">4</span> Сочетания клавиш {#сочетания-клавиш}

-   Экспорт осуществляется через стандартный интерфейс экспорта в org-mode.


### <span class="section-num">4.1</span> Для режимов _один пост на файл_ и _один пост на поддерево_ {#для-режимов-один-пост-на-файл-и-один-пост-на-поддерево}

-   `C-c C-e H H` Экспорт «Что я имею в виду».
    -   Если курсор находится в допустимом поддереве сообщения Hugo,
        экспортирует это поддерево в сообщение Hugo в Markdown. Допустимое
        поддерево сообщений Hugo - это поддерево, для которого установлено
        свойство `EXPORT_FILE_NAME`.
    -   Если файл предназначен для экспорта целиком (т.е. имеет ключевое
        слово `#+title`), экспортирует весь файл Org в сообщение Hugo в
        Markdown.
-   `C-c C-e H A` Экспорт всего «Что я имею в виду».
    -   Если в org-файле есть одно или несколько действительных
        поддеревьев сообщений Hugo, экспортирует их в сообщения Hugo в
        Markdown.
    -   Если файл предназначен для экспорта целиком (т. е. вообще нет
        действительных поддеревьев сообщений Hugo и есть ключевое слово
        `#+title`), экспортирует весь org-файл в сообщение Hugo в
        Markdown.


### <span class="section-num">4.2</span> Для режима _один пост на файл_ {#для-режима-один-пост-на-файл}

-   `C-c C-e H h` Экспорт файла Org в сообщение Hugo в Markdown.


## <span class="section-num">5</span> Теги и категории {#теги-и-категории}


### <span class="section-num">5.1</span> Экспорт уровня файла {#экспорт-уровня-файла}

-   Список тегов:
    ```org
    #+hugo_tags
    ```
-   Список категорий:
    ```org
    #+hugo_categories
    ```


### <span class="section-num">5.2</span> Экспорт уровня поддерева {#экспорт-уровня-поддерева}


#### <span class="section-num">5.2.1</span> Теги {#теги}

Экспортируемые теги Hugo задаются как теги org-mode:

```org
* My post                                                         :tag1:tag2:
```


#### <span class="section-num">5.2.2</span> Категории {#категории}

Экспортируемые категорий Hugo задаются как теги org-mode, для которых установлен префикс @:

```org
* My post                                                       :@cat1:@cat2:
```


#### <span class="section-num">5.2.3</span> Использование filetags {#использование-filetags}

Для экспорта на уровне поддерева можно использовать оператор

```org
#+filetags
```

Например:

```org
#+filetags: :@cat1:tag1:tag2:
```


### <span class="section-num">5.3</span> Дефисы и пробелы в тегах {#дефисы-и-пробелы-в-тегах}

В тегах org-mode нельзя использовать дефисы и пробелы.
Конвертер использует следующие настройки:

-   одиночное подчёркивание переводится в дефис (конфигурационная переменная `org-hugo-prefer-hyphen-in-tags`);
-   двойное подчёркивание переводится в пробел (конфигурационная переменная `org-hugo-allow-spaces-in-tags`).


## <span class="section-num">6</span> Дополнительные поля {#дополнительные-поля}

Нестандартные дополнительные поля в основном используются для
установки пользовательских параметров оформления.

-   Чтобы установить настраиваемый параметр предварительной записи в поддереве, используется свойство `:EXPORT_HUGO_CUSTOM_FRONT_MATTER:`.
-   Чтобы задать настраиваемый параметр внешнего вида глобально или для потока экспорта для каждого файла, используется ключевое слово
    `#+HUGO_CUSTOM_FRONT_MATTER:`.


### <span class="section-num">6.1</span> Синтаксис {#синтаксис}


#### <span class="section-num">6.1.1</span> Пары ключ-значение {#пары-ключ-значение}

-   Можно записывать в одном поле:
    ```org
    :PROPERTIES:
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER: :key1 value1 :key2 value2
    :END:
    ```
-   Можно разбить на несколько полей:
    ```org
    :PROPERTIES:
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER: :key1 value1
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER+: :key2 value2
    :END:
    ```
-   На уровне файла посредством ключевого слова:
    ```org
    #+hugo_custom_front_matter: :key1 value1
    #+hugo_custom_front_matter: :key2 value2
    ```
-   Например, запись
    ```org
    :PROPERTIES:
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER: :feature true
    :END:
    ```
    примет вид (для TOML)
    ```toml
    feature = true
    ```


#### <span class="section-num">6.1.2</span> Списочные значения {#списочные-значения}

-   Запись имеет следующий вид:
    ```org
    :PROPERTIES:
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER: :key1 '(elem11 elem12) :key2 '(elem21 elem22)
    :END:
    ```
-   Например, запись
    ```org
    :PROPERTIES:
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER: :animals '(dog cat "penguin" "mountain gorilla")
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER+: :integers '(123 -5 17 1_234)
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER+: :floats '(12.3 -5.0 -17E-6)
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER+: :booleans '(true false)
    :END:
    ```
    примет вид (для TOML)
    ```toml
    animals = ["dog", "cat", "penguin", "mountain gorilla"]
    integers = [123, -5, 17, 1_234]
    floats = [12.3, -5.0, -1.7e-05]
    booleans = [true, false]
    ```


#### <span class="section-num">6.1.3</span> Многоуровневые значения {#многоуровневые-значения}

-   Запись имеет следующий вид:
    ```org
    :PROPERTIES:
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER: :key1 '((subkey11 . subval11) (subkey12 . (subelem121 subelem122))) :key2 '((subkey21 . subval21))
    :END:
    ```
-   Например, запись
    ```org
    :PROPERTIES:
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER: :versions '((emacs . "27.0.50") (hugo . "0.48"))
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER+: :header '((image . "projects/Readingabook.jpg") (caption . "stay hungry, stay foolish"))
    :EXPORT_HUGO_CUSTOM_FRONT_MATTER+: :collection '((animals . (dog cat "penguin" "mountain gorilla")) (integers . (123 -5 17 1_234)) (floats . (12.3 -5.0 -17E-6)) (booleans . (true false)))
    :END:
    ```
    примет вид (для TOML)
    ```toml
    [versions]
      emacs = "27.0.50"
      hugo = 0.48
    [header]
      image = "projects/Readingabook.jpg"
      caption = "stay hungry, stay foolish"
    [collection]
      animals = ["dog", "cat", "penguin", "mountain gorilla"]
      integers = [123, -5, 17, 1_234]
      floats = [12.3, -5.0, -1.7e-05]
      booleans = [true, false]
    ```


#### <span class="section-num">6.1.4</span> Прямая вставка преамбул {#прямая-вставка-преамбул}

Можно описать преамбулу непосредственно (если невозможно сгенерить средствами экспорта).
Для этого используется аргумент заголовка блока кода `:front_matter_extra t`.

<!--list-separator-->

1.  Преамбула _TOML_

    По умолчанию используется преамбула в формате TOML, поэтому нет необходимости устанавливать ключевое слово `:EXPORT_HUGO_FRONT_MATTER_FORMAT: toml`.

    ```org
    * Post with TOML front-matter (default)
    :PROPERTIES:
    :EXPORT_FILE_NAME: extra-front-matter-toml
    :END:
    The contents of the ~#+begin_src toml :front_matter_extra t~ TOML
    block here will get appended to the TOML front-matter.
    #+begin_src toml :front_matter_extra t
    [[foo]]
      bar = 1
      zoo = "abc"
    [[foo]]
      bar = 2
      zoo = "def"
    #+end_src
    ```

<!--list-separator-->

2.  Преамбула _YAML_

    ```org
    * Post with YAML front-matter
    :PROPERTIES:
    :EXPORT_FILE_NAME: extra-front-matter-yaml
    :EXPORT_HUGO_FRONT_MATTER_FORMAT: yaml
    :END:
    The contents of the ~#+begin_src yaml :front_matter_extra t~ YAML
    block here will get appended to the YAML front-matter.
    #+begin_src yaml :front_matter_extra t
    foo:
      - bar: 1
        zoo: abc
      - bar: 2
        zoo: def
    #+end_src
    ```


## <span class="section-num">7</span> Экспорт элементов {#экспорт-элементов}

-   При экспорте элементов для _Hugo_ используется блок
    ```org
    #+begin_export hugo
    Текст для Hugo
    #+end_export
    ```
-   Возникла коллизия, когда из единого источника необходимо было вывести информацию и в _Hugo_, и в _Markdown_. При экспорте посредством блока
    ```org
    #+begin_export markdown
    Текст для Markdown
    #+end_export
    ```
    этот текст появлялся и в файле для _Hugo_. Для обхода этой ситуации я стал задавать блок для _Markdown_ в следующем виде:
    ```org
    #+begin_src markdown :exports (if (eq org-export-current-backend 'md) "" "none")
    Текст для Markdown
    #+end_src
    ```


## <span class="section-num">8</span> Пакет страниц (page bundle) {#пакет-страниц--page-bundle}


### <span class="section-num">8.1</span> Общая информация {#общая-информация}

-   Для экспорта в пакет (папку) страниц нужно установить для свойства `:EXPORT_HUGO_BUNDLE: (или =#+HUGO_BUNDLE`) имя каталога в качестве значения.
-   Значение `:EXPORT_FILE_NAME:` или `#+EXPORT_FILE_NAME` устанавливается в зависимости от вида пакетов страниц.
-   Пакеты страниц ([Hugo Page Bundle](https://gohugo.io/content-management/page-bundles/)) бывают двух видов:
    -   пакет-страница (Leaf Bundle)
        -   нет подстраниц,
        -   контент и вложения для отдельных страниц,
        -   индексный файл: `index.md`,
        -   пример: `content/posts/my-post/index.md`,
        -   `:EXPORT_FILE_NAME: index`,
        -   `#+EXPORT_FILE_NAME: index`.
    -   пакет веток (Branch Bundle)
        -   содержит подстраницы,
        -   контент и вложения для страниц раздела (домашняя страница, раздел, термины таксономии, список таксономии),
        -   индексный файл: `_index.md`,
        -   пример: `content/posts/_index.md`,
        -   `:EXPORT_FILE_NAME: _index`,
        -   `#+EXPORT_FILE_NAME: _index`.
    -   Пример пакет-страницы (Leaf Bundle):
        -   экспорт в `content/xyz/index.md`
            ```org
            ​* Page title
            :PROPERTIES:
            :EXPORT_HUGO_BUNDLE: xyz
            :EXPORT_FILE_NAME: index
            :END:
            Content
            ```
    -   Пример пакета веток (Branch Bundle)
        -   экспорт в `content/uvw/_index.md`
            ```org
            ​* Page title
            :PROPERTIES:
            :EXPORT_HUGO_BUNDLE: uvw
            :EXPORT_FILE_NAME: _index
            :END:
            Content
            ```


### <span class="section-num">8.2</span> Читаемые курсы {#читаемые-курсы}

Чтобы сделать список и содержание читаемых курсов (или какой-либо документации).

-   Пусть курс называется `mathsec`.
-   Свойства для экспорта:
    ```org
    :PROPERTIES:
    :EXPORT_HUGO_SECTION: ru/course
    :EXPORT_HUGO_BUNDLE: mathsec
    :EXPORT_FILE_NAME: _index
    :END:
    ```


## <span class="section-num">9</span> Автоматический экспорт при сохранении {#автоматический-экспорт-при-сохранении}


### <span class="section-num">9.1</span> Установка на уровне каталога {#установка-на-уровне-каталога}

-   Установка делается в файле `.dir-locals.el` в текущем каталоге:
    ```elisp
    ((org-mode . ((eval . (org-hugo-auto-export-mode)))))
    ```
-   Конфигурация применяется ко всем org-файлам в каталоге.


### <span class="section-num">9.2</span> Установка на уровне проекта {#установка-на-уровне-проекта}

-   Если org-файлы находятся в некотором каталоге, например в `content-org`, то в файле `.dir-locals.el` задаётся конфигурация для этого каталога:
    ```elisp
    (("content-org/"
      . ((org-mode . ((eval . (org-hugo-auto-export-mode)))))))
    ```


### <span class="section-num">9.3</span> Установка для конкретного файла {#установка-для-конкретного-файла}

-   Для каждого файла можно задать локальные переменные:
    ```org
    ​* COMMENT Local Variables                          :ARCHIVE:
    # Local Variables:
    # eval: (org-hugo-auto-export-mode)
    # End:
    ```
-   Рекомендуется добавить заголовок `Footnotes` перед заголовком `Local Variables`, чтобы в случае добавления каких-либо сносок они добавлялись в данный раздел.
-   В противном случае будет автоматически создан новый заголовок `Footnotes` в конце файла, и заголовок `Local Variables` больше не будет последним и не будет обрабатываться.
-   Перечитать локальные переменные можно командой:
    ```elisp
    M-x normal-mode
    ```


### <span class="section-num">9.4</span> Запрет авто сохранения для конкретного файла {#запрет-авто-сохранения-для-конкретного-файла}

-   Для каждого файла можно задать локальные переменные для запрета экспорта:
    ```org
    ​* COMMENT Local Variables                          :ARCHIVE:
    # Local Variables:
    # eval: (org-hugo-auto-export-mode -1)
    # End:
    ```


## <span class="section-num">10</span> Цитирование {#цитирование}


### <span class="section-num">10.1</span> Формат цитирования pandoc {#формат-цитирования-pandoc}

-   Исторический формат цитирования.
-   Рекомендуется перейти на формат цитирования org-cite.


### <span class="section-num">10.2</span> Формат цитирования org-cite {#формат-цитирования-org-cite}

-   Цитирование основано на org-cite (см. [Emacs. Работа с библиографией. Org-cite]({{< relref "2022-10-10-emacs-bibliography-org-cite" >}})).
-   Рекомендуется использовать процессор экспорта _csl_.
-   При задании ключевого слова `#+print_bibliography:` по умолчанию создаётся секция `References.`
-   Можно задать другое название для этой секции:
    ```emacs-lisp
    (with-eval-after-load 'ox-hugo
      (plist-put org-hugo-citations-plist :bibliography-section-heading "Bibliography"))
    ```
-   Если для этого свойства задана пустая строка, этот заголовок не будет вставлен автоматически&nbsp;[^fn:4]:
    ```emacs-lisp
    (with-eval-after-load 'ox-hugo
      (plist-put org-hugo-citations-plist :bibliography-section-heading ""))
    ```

[^fn:1]: Если `org-hugo-use-code-for-kbd` равно `nil` (по умолчанию).
[^fn:2]: Если `org-hugo-use-code-for-kbd` не равно `nil`.  Требует настроек _CSS_ для интерпретации тега `<kbd>`.
[^fn:3]: Требует настроек _CSS_ для интерпретации тега `<underline>`.
[^fn:4]: Так должно быть, но не работает. Вообще литература не печатается.