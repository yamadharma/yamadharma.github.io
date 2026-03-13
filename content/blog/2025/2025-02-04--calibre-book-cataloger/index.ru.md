---
title: "Каталогизатор книг Calibre"
author: ["Dmitry S. Kulyabov"]
date: 2025-02-04T19:09:00+03:00
lastmod: 2025-05-13T14:06:00+03:00
tags: ["book"]
categories: ["self-management", "computer-science"]
draft: false
slug: "calibre-book-cataloger"
---

Каталогизатор книг Calibre.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://calibre-ebook.com/>
-   Репозиторий: <https://github.com/kovidgoyal/calibre>
-   Операционные системы: GNU/Linux, Windows, macOS, BSD.


## <span class="section-num">2</span> Особенности {#особенности}

-   Не поддерживается формат базы пользователя. При импорте книг, все файлы будут скопированы в каталог с базой (автор отказывается менять это решение).
-   Не поддерживаются внешние конвертеры.


## <span class="section-num">3</span> Интерфейс командной строки {#интерфейс-командной-строки}

-   `calibredb` --- инструмент командной строки.
-   Является частью программного обеспечения библиотеки электронных книг Calibre.
-   Возможности calibredb:
    -   Управление базой данных электронных книг  : добавление электронных книг, удаление электронных книг, редактирование метаданных, обновление форматов, управление тегами.
    -   Манипуляции с метаданными : позволяет изменять метаданные: название книги, автор, издатель, дата публикации, изображение обложки, описание.
    -   Преобразование формата.
    -   Импорт и экспорт электронных книг.
    -   Поиск и фильтрация.


### <span class="section-num">3.1</span> Примеры команд calibredb {#примеры-команд-calibredb}

-   Список электронных книг:
    ```shell
    calibredb list
    ```
-   Поиск электронных книг, отображающих дополнительную информацию:
    ```shell
    calibredb list --search search_term
    ```
-   Поиск только идентификаторов электронных книг:
    ```c
    calibredb search search_term
    ```
-   Добавить книгу в библиотеку:
    ```shell
    calibredb add file1 file2 ...
    ```
-   Рекурсивно добавить все электронные книги в каталоге в библиотеку:
    ```shell
    calibredb add -r /path/to/directory
    ```
-   Удалить одну или несколько книг из библиотеки (нужны идентификаторы электронных книг):
    ```shell
    calibredb remove id1 id2 ...
    ```


## <span class="section-num">4</span> Дополнения {#дополнения}


### <span class="section-num">4.1</span> Calibre-web {#calibre-web}

-   Репозиторий: <https://github.com/janeczku/calibre-web>
-   Веб-приложение для просмотра, чтения и загрузки электронных книг, используя базу данных Calibre.


### <span class="section-num">4.2</span> calibre2opds {#calibre2opds}

-   Репозиторий: <https://github.com/calibre2opds/calibre2opds>
-   Java приложение, которое создает web-сайт из вашей Calibre библиотеки.


### <span class="section-num">4.3</span> Calibre2OPDS for Nextcloud {#calibre2opds-for-nextcloud}

-   Репозиторий: <https://gitlab.com/oldnomad/calibre_opds>
-   Предоставляет доступ к Calibre-библиотеке, размещённой в Nextcloud через OPDS.


### <span class="section-num">4.4</span> rdr {#rdr}

-   Репозиторий: <https://github.com/michaelmrose/rdr>
-   Утилита командной строки для поиска и открытия книг из библиотеки Calibre.
-   Написано на Clojure.


## <span class="section-num">5</span> Интерфейс Emacs {#интерфейс-emacs}

-   Информация:
    -   <https://dindi.garjola.net/calibredb-view.html>


### <span class="section-num">5.1</span> calibredb.el {#calibredb-dot-el}

-   [Emacs. calibredb.el]({{< relref "2025-04-09--emacs-calibredbel" >}})
-   Emacs-клиент для  Calibre.
-   Репозиторий: <https://github.com/chenyanming/calibredb.el>


### <span class="section-num">5.2</span> calibre.el {#calibre-dot-el}

-   Emacs-клиент для  Calibre.
-   Репозиторий: <https://git.disroot.org/kjartanoli/calibre.el>
-   ELPA: <https://elpa.gnu.org/packages/calibre.html>


### <span class="section-num">5.3</span> calibre-mode.el {#calibre-mode-dot-el}

-   Поиск по Calibre.
-   Репозиторий: <https://github.com/whacked/calibre-query.el>
