---
title: "Pandoc. Фильтры. Включение файлов"
author: ["Dmitry S. Kulyabov"]
date: 2023-03-23T19:35:00+03:00
lastmod: 2025-11-19T21:28:00+03:00
tags: ["pandoc"]
categories: ["computer-science"]
draft: false
slug: "pandoc-filters-include"
---

Включение файлов в другие файлы.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Включения других файлов в документ {#включения-других-файлов-в-документ}

-   Основные варианты:
    -   рекурсивное включение;
    -   абсолютное включение.
-   Рекурсивное включение:
    -   Пусть файл `a/b.md` подключается из основного документа.
    -   Файл `a/b.md` в свою очередь подключает файл `a/b/c.md`.
    -   В этом случае используется относительный путь `b/c.md`.
    -   То же самое касается путей к изображениям и путей к файлам кодовых блоков с использованием фильтра `include-code-files`.
-   Абсолютное включение:
    -   Как в LaTeX.


### <span class="section-num">1.1</span> include-files {#include-files}

-   Репозиторий: <https://github.com/pandoc/lua-filters>.
-   Язык реализации: Lua.
-   Рекурсивное включение.


#### <span class="section-num">1.1.1</span> Особенности {#особенности}

-   Не запускайте другие фильтры перед выполнением `include-files`.
-   Выполнение большинства фильтров без предварительного использования `include-files` приведёт к тому, что другой фильтр увидит пустой блок кода.


#### <span class="section-num">1.1.2</span> Применение {#применение}

-   Используйте `include` для включения файлов того же формата, что и входные данные.
-   Использование оформляется в виде директивы класса.
-   Каждая строка кода обрабатывается как имя файла, анализируется, и результат добавляется в документ.
-   Метаданные из включенных файлов отбрасываются.
-   Строки комментариев начинаются с символов `//`.


#### <span class="section-num">1.1.3</span> Смена заголовков {#смена-заголовков}

-   По умолчанию вложенные документы включаются без изменений.
-   Иногда удобно изменить уровень заголовков.
-   Ручное переключение: используйте атрибут `shift-heading-level-by` для управления сдвигом заголовка.
-   Автоматическое переключение: добавьте метаданные `-M include-auto`, чтобы включить автоматическое смещение. Не указывайте `shift-heading-level-by`.
-   Пример:
    ````markdown
    # Title f

    This is `file-f.md`.

    ## Subtitle f

    ```{.include} >> equivalent to {.include shift-heading-level-by=2}
    file-a.md
    ```

    ```{.include shift-heading-level-by=1} >> force shift to be 1
    file-a.md
    ```
    ````


#### <span class="section-num">1.1.4</span> Форматы {#форматы}

-   По умолчанию предполагается, что файлы написаны в формате Markdown.
-   При необходимости включить файлы, написанные в другом формате, альтернативный формат может быть указан через атрибут `format`.
-   Принимаются только текстовые форматы.


#### <span class="section-num">1.1.5</span> Пример {#пример}

-   Предположим, мы пишем длинный документ, например диссертацию.
-   Каждая глава и раздел приложения находятся в отдельном файле.
-   Основной файл --- `main.md`:
    ````markdown
    ---
    author: me
    title: Thesis
    ---

    # Frontmatter

    Thanks everyone!

    <!-- actual chapters start here -->

    ``` {.include}
    chapters/introduction.md
    chapters/methods.md
    chapters/results.md
    chapters/discussion.md
    ```

    # Appendix

    More info goes here.

    ``` {.include shift-heading-level-by=1}
    // headings in included documents are shifted down a level,
    // a level 1 heading becomes level 2.
    appendix/questionaire.md
    ```
    ````
-   Например, html можно создать с помощью этой команды:
    ````shell
    pandoc --lua-filter=include-files.lua main.md --output result.html
    ````


### <span class="section-num">1.2</span> panda {#panda}

-   Репозиторий: <https://github.com/CDSoft/panda>.
-   Документация: <http://christophe.delord.free.fr/panda/>.
-   Язык реализации: Lua.
-   Абсолютное включение.


#### <span class="section-num">1.2.1</span> Особенности {#особенности}

-   Включение как блок `div`.
-   Включаемый файл может быть в другом формате.
-   Если блок задаёт входной формат как класс, файл анализируется в соответствии с этим форматом.


#### <span class="section-num">1.2.2</span> Смена заголовков {#смена-заголовков}

-   По умолчанию вложенные документы включаются без изменений.
-   Иногда удобно изменить уровень заголовков.
-   Ручное переключение: используйте атрибут `shift=n` для управления сдвигом заголовка.
-   По умолчанию n = 0.


#### <span class="section-num">1.2.3</span> Пример {#пример}

-   Содержимое файла анализируется в соответствии с его форматом и заменяет содержимое блока `div`:
    ````markdown
    :::{include=file.md shift=n}
    This text is optional and will be replaced by the content of file.md.
    Section title levels are shifted by n (0 if not specified).
    :::
    ````


## <span class="section-num">2</span> Quarto {#quarto}

-   В Quarto можно использовать стандартное сокращение для подключения файлов: [Quarto. Подключение файлов]({{< relref "2025-11-19--quarto-include-file" >}}).
