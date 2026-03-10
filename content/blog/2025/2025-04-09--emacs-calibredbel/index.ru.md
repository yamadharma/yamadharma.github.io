---
title: "Emacs. calibredb.el"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-09T13:53:00+03:00
lastmod: 2025-05-13T14:09:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-calibredbel"
---

Emacs. Пакет calibredb.el.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Emacs-клиент для  Calibre.
-   Репозиторий: <https://github.com/chenyanming/calibredb.el>


## <span class="section-num">2</span> Использование {#использование}


### <span class="section-num">2.1</span> Основные команды {#основные-команды}

-   Интерфейс
    -   `M-x calibredb` : откроет список всех книг в библиотеке.
    -   Для навигации используйте `n` / `p` (вверх/вниз).
    -   `RET` : открыть книгу.
-   Поиск книг
    -   Живой поиск: Нажмите `/` и введите запрос (название, автор, тег).
    -   Фильтрация по формату: `f` → выберите формат (epub, pdf и т.д.).
-   Управление метаданными
    -   `e` : редактировать метаданные (автор, описание, обложка).
    -   `t` : добавить/удалить теги.
    -   Изменения сохраняются в `.metadata.calibre`, требуется обновить метаданные через Calibre.


### <span class="section-num">2.2</span> Работа с файлами {#работа-с-файлами}

-   Добавление книг
    -   Через Calibre: `Connect to folder` → выберите папку с книгами.
    -   Через Dired: `M-x dired` → выделите файлы → `C-c C-a` (добавить в библиотеку).
-   Экспорт/импорт
    -   `E` : экспортировать книгу в выбранный формат (например, epub → mobi).
    -   `C-c C-e` : экспортировать аннотации в отдельный файл.


### <span class="section-num">2.3</span> Дополнительные функции {#дополнительные-функции}

-   Интеграция с Org-mode
    Вставьте ссылку на книгу в Org-файл:
    ```org
    [[calibre:Название_книги][Ссылка на книгу]]
    ```
    Нажмите `C-c C-o` для открытия.
    [geeksrepos.com](https://geeksrepos.com/whacked/calibre-query.el)

-   Автоматизация
    Используйте скрипты для:
    -   Конвертации всех книг в формат EPUB:
        ```elisp
        (calibredb-convert "(format:\"pdf\")" "epub")
        ```

    -   Синхронизации с читалкой:
        ```elisp
        (calibredb-send-to-device "(tag:\"read-later\")" "/path/to/device")
        ```

---


## <span class="section-num">3</span> Ограничения {#ограничения}

-   Обложки могут отображаться как квадраты, если книга не содержит
    встроенного изображения.
-   Добавление книг требует ручного обновления `.metadata.calibre` через
    Calibre.
    [medium.com](https://elecming.medium.com/how-i-manage-documents-if-all-of-them-in-one-flat-folder-using-calibredb-el-3be0e0aeecbe)

---


## <span class="section-num">4</span> Полезные сочетания клавиш {#полезные-сочетания-клавиш}

| Клавиши | Действие                       |
|---------|--------------------------------|
| `g`     | Обновить список                |
| `d`     | Удалить книгу                  |
| `.`     | Открыть папку с книгой (Dired) |
| `s`     | Показать детали книги          |

Документация и примеры:
[Официальный
репозиторий](https://github.com/chenyanming/calibredb.el).
