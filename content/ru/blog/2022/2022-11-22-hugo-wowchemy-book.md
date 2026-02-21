---
title: "Hugo. Wowchemy. Book"
author: ["Dmitry S. Kulyabov"]
date: 2022-11-22T16:31:00+03:00
lastmod: 2025-01-06T14:35:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "hugo-wowchemy-book"
---

Использование узла типа _docs_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Тип узла _book_ используется для создания многостраничного контента, такого как онлайн-курсы, документация по программному обеспечению, базы знаний, книги, блокноты, учебные пособия.
-   Другой вариант этого типа узла --- _docs_.
-   При переходе на фреймворк tailwind (2024 год) тип узла _book_ был убран.
-   Рекомендовано вместо него использовать тип узла _docs_.


## <span class="section-num">2</span> Структура {#структура}

-   Предлагается использовать следующую файловую структуру:

<!--listend-->

```shell
content/teaching
├── _index.md         # Overview
└── intro             # Chapter folder
    ├── _index.md     # Chapter metadata including chapter title
    ├── example1.md   # A page
    └── example2.md   # Another page
└── tutorial          # Another chapter
    ├── _index.md
    ├── intro.md
    └── ...
```

-   В именах файлов и папок вместо пробелов следует использовать дефисы.
-   Папка `teaching` может быть переименована.
-   Например, мы можем переименовать её в `book` для написания книги, `docs` для документации по программному обеспечению/проекту, `notes` для создания блокнота или `tutorials` для создания многостраничных руководств.


## <span class="section-num">3</span> Метаданные {#метаданные}

-   Рассмотрим структуру файла `_index.md` (например `content/teaching/example/_index.md`) для книги.
-   Укажем название и краткое содержание книги.
    ```markdown
    # Page title
    title: An Example Course

    # Title for the menu link if you wish to use a shorter link title, otherwise remove this option.
    linktitle: Course

    # Page summary for search engines.
    summary: Blah, blah, blah...

    # Date page published
    date: 2018-09-09

    # Book page type (do not modify).
    type: docs

    # Position of this page in the menu. Remove this option to sort alphabetically.
    weight: 1
    ```


## <span class="section-num">4</span> Меню {#меню}

-   Можете задать меню тремя способами:
    -   по возрастанию названия;
    -   по убыванию названия;
    -   путём ручного упорядочивания с использованием `weight: 10` для первых страниц, где номер определяет порядок.
    -   Рекомендуется использовать веса с шагом 10, чтобы в будущем можно было легко изменить порядок страниц без необходимости изменять вес всех других страниц.


## <span class="section-num">5</span> Страницы {#страницы}

-   Вы можете создать столько страниц, сколько вам нужно. Каждая страница должна иметь поле `title` и тип `type: docs`.
    -   `title` : заголовок страницы (отображается в заголовке страницы);
    -   `linktitle` : метка для ссылки на эту страницу (отображается в меню). Если удалить `linktitle`, ссылка меню не будет отображать заголовок страницы.
-   Чтобы удалить правую боковую панель для оглавления страницы (сгенерированного из заголовков на вашей странице), установите `toc: false`.
-   Чтобы отображать предыдущий/следующий пейджер внизу каждой страницы раздела документов, включите `docs_section_pager` в `params.yaml`, затем установите порядок пейджера, определив `weight` для каждой страницы.
-   Пример страницы выглядит следующим образом:
    ```markdown
    ---
    title: Example Page 1
    date: 2019-05-05
    type: docs
    ---

    Content...
    ```
-   Чтобы перечислить дочерние страницы на страницах глав книги, можно использовать сокращение `{{< list_children >}}`.
    -   При переходе на tailwind данное сокращение было изъято.
    -   Поскольку используется боковой список разделов, данное сокращение выглядит несколько излишним.
