---
title: "Emacs. Управление пакетами. package"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-25T14:19:00+03:00
lastmod: 2026-06-24T20:28:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-package-management-package"
---

Emacs. Управление пакетами. package.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Документация: <https://www.gnu.org/software/emacs/manual/html_node/emacs/Packages.html>
-   Встроенный пакет Emacs для управления пакетами.


## <span class="section-num">2</span> Основные операции {#основные-операции}

-   Обновить пакеты: `package-upgrade`, `package-upgrade-all`.
-   Удалить пакеты: `package-delete`.


## <span class="section-num">3</span> Установка пакетов репозитория {#установка-пакетов-репозитория}

-   По умолчанию `package-install`  загружает пакет из архива и устанавливает его файлы.
-   Можно установить и напрямую из репозитория.
-   Можно установить, используя `package-vc-install`.
-   Просто клонировать источник пакета, не добавляя его в список пакетов: `package-vc-checkout`.


### <span class="section-num">3.1</span> Указание источников пакетов {#указание-источников-пакетов}

-   Чтобы установить пакет из исходного кода, Emacs должен знать, где взять исходный код пакета (например, репозиторий кода) и основные информация о структуре кода (например, основной файл в многофайловый пакет).
-   Emacs может автоматически загрузить спецификацию пакета из указанного архива, если первый аргумент у `package-vc-install` --- это символьное название пакета:
    ```emacs-lisp
    ;; Emacs will download BBDB's specification from GNU ELPA
    (package-vc-install 'bbdb)
    ```

-   Основные ключи для описания пакета:
    -   `:url` (строка) : URL-адрес, указывающий репозиторий, из которого следует получить исходный код пакета;
    -   `:branch` (строка) : версия кода для установки;
    -   `:lisp-dir` (строка) : относительное имя каталога для репозитория; по умолчанию загружаются файлы, которые находятся в корневом каталоге репозитория;
        -   Поскольку указывается только строка (а не список строк), не понятно, как устанавливать пакеты, файлы которых находятся в нескольких каталогах.
        -   Пока использую _straight_ или _quelpa_.
    -   `:main-file` (строка) : основной файл проекта, из которого можно собрать метаданные пакета; если не указано, по умолчанию используется имя пакета;
    -   `:doc` (строка) : имя документации относительно репозитория;
    -   `:vc-backend` (символ) : бэкэнд для загрузки копии репозитория.
-   Пример:
    ```emacs-lisp
    ;; Specifying information manually:
    (package-vc-install
      '(bbdb :url "https://git.savannah.nongnu.org/git/bbdb.git"
             :lisp-dir "lisp"
             :doc "doc/bbdb.texi"))
    ```


## <span class="section-num">4</span> Зеркала для пакетного менеджера {#зеркала-для-пакетного-менеджера}


### <span class="section-num">4.1</span> Базовые источники {#базовые-источники}

-   Emacs скачивает пакеты из источников, перечисленных в переменной `package-archives`.
-   По умолчанию там только GNU ELPA.
-   Обычно сразу добавляют MELPA.
-   Чтобы использовать зеркала, нужно просто подставить их URL перед вызовом `package-initialize`.
    ```elisp
    ;; ~/.emacs.d/init.el
    (require 'package)

    (setq package-archives
          '(("gnu" . "https://elpa.gnu.org/packages/")
            ("nongnu" . "https://elpa.nongnu.org/nongnu/")
            ("gnu-devel" . "https://elpa.gnu.org/devel/")
            ("melpa" . "https://melpa.org/packages/")
            ("melpa-stable" . "https://stable.melpa.org/packages/")))

    (package-initialize)
    (unless package-archive-contents
      (package-refresh-contents))
    ```

-   Традиционно сложились такие имена:
    -   gnu --- официальный архив GNU ELPA. Исторически он единственный был встроен по умолчанию.
    -   melpa --- самый популярный неофициальный архив со срезом последних коммитов пакетов (сборочная модель «снимки»).
    -   melpa-stable --- архив MELPA, в который попадают только стабильные релизы (теги) пакетов.
-   Emacs из коробки не поддерживает fallback-зеркала.
-   В `package-archives` у каждого имени может быть только один URL. Если добавить две записи с одинаковым именем, последняя просто перезапишет предыдущую.
-   Технически можно добавить несколько архивов, содержащих одно и то же, под разными именами.
-   Тогда в списке пакетов вы увидите одни и те же пакеты дважды, и Emacs может установить пакет из любого архива.
-   Приоритет будет у первого.
-   Если основное зеркало недоступно, то при `package-refresh-contents` вы получите ошибку о недоступности основного репозитория.
-   Однако это порождает путаницу и не гарантирует корректного разрешения зависимостей (версии могут отличаться).
-   Это не рекомендуется.


### <span class="section-num">4.2</span> Зеркала {#зеркала}


#### <span class="section-num">4.2.1</span> Зеркало d12frosted на github {#зеркало-d12frosted-на-github}

-   Автоматически зеркалирует GNU ELPA, MELPA, Org ELPA с помощью GitHub Actions.
-   Репозиторий: <https://github.com/d12frosted/elpa-mirror>:
    ```elisp
    (setq package-archives
          '(("melpa" . "https://raw.githubusercontent.com/d12frosted/elpa-mirror/master/melpa/")
            ("melpa-stable" . "https://raw.githubusercontent.com/d12frosted/elpa-mirror/master/stable-melpa")
            ("gnu" . "https://raw.githubusercontent.com/d12frosted/elpa-mirror/master/gnu/")
            ("nongnu" . "https://raw.githubusercontent.com/d12frosted/elpa-mirror/master/nongnu")))
    ```
-   По ссылке нельзя просмотреть содержимое каталога, поэтому emacs выдаёт ошибку.
-   Я отключил эти зеркала.


#### <span class="section-num">4.2.2</span> Зеркало d12frosted на GitLab {#зеркало-d12frosted-на-gitlab}

-   Автоматически зеркалирует GNU ELPA, MELPA, Org ELPA с помощью GitHub Actions.
-   Репозиторий: <https://gitlab.com/d12frosted/elpa-mirror/>:
    ```elisp
    (setq package-archives
          '(("melpa" . "https://gitlab.com/d12frosted/elpa-mirror/-/tree/master/melpa")
            ("melpa-stable" . "https://gitlab.com/d12frosted/elpa-mirror/-/tree/master/stable-melpa")
            ("gnu" . "https://gitlab.com/d12frosted/elpa-mirror/-/tree/master/gnu")
            ("nongnu" . "https://gitlab.com/d12frosted/elpa-mirror/-/tree/master/nongnu")))
    ```


#### <span class="section-num">4.2.3</span> Проверка зеркала {#проверка-зеркала}

-   Любой URL, добавляемый в `package-archives`, должен отдавать файл `archive-contents`.
-   Просто откройте в браузере `<адрес>/archive-contents`.
-   Если видите текстовые данные с описанием пакетов, зеркало работает.
