---
title: "Emacs. Пакет org-download"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-19T15:49:00+03:00
lastmod: 2025-05-20T14:46:00+03:00
tags: ["markdown", "org-mode", "emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-org-download"
---

Emacs. Пакет org-download.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/abo-abo/org-download>


## <span class="section-num">2</span> Общие настройки {#общие-настройки}

-   Чтобы изображения отображались сразу в буфере, добавьте в настройки:
    ```elisp
    (setq org-startup-with-inline-images t)
    ```


## <span class="section-num">3</span> Методы работы с файлами {#методы-работы-с-файлами}


### <span class="section-num">3.1</span> Копирование файлов {#копирование-файлов}

-   Настройте:
    ```elisp
    (setq org-download-method 'directory)
    ```

-   Файлы копируются напрямую в директорию org-файла.
-   При использовании метода `directory` структура папок будет выглядеть так:
    ```text
    ├── ваш_файл.org
    └── images/
        └── ваш_файл.png
    ```


#### <span class="section-num">3.1.1</span> Своя функция для струтуры {#своя-функция-для-струтуры}

-   Установите `org-download` через `use-package`:
    ```elisp
    (defun my-org-download-set-dir ()
      "Установить путь для сохранения изображений"
      (setq-local org-download-image-dir
                    (concat (file-name-directory (buffer-file-name))
                            "/images/"
                            (file-name-base buffer-file-name)
                            "/")))
    (add-hook 'org-mode-hook 'my-org-download-set-dir)
    ```

-   Структура папок:
    ```text
    ├── ваш_файл.org
    └── images/
        └── ваш_файл/
            ├── Заголовок_1/
            │   └── image1.png
            └── Заголовок_2/
                └── image2.png
    ```


### <span class="section-num">3.2</span> Использование org-attach {#использование-org-attach}

-   Установим метод загрузки:
    ```elisp
    (setq org-download-method 'attach)
    ```

-   Используется механизм org-attach для управления файлами.
    -   Файлы хранятся в специальной директории attachments
    -   Создается символическая ссылка в org-файле
    -   Обеспечивается более структурированное управление файлами

-   Дополнительные настройки для работы с файлами:
    ```elisp
    (setq org-download-image-dir "images/") ; директория для сохранения
    (setq org-download-mkdir-if-not-exist t) ; автоматическое создание директорий
    ```

-   При использовании метода `attach` структура папок будет выглядеть так:
    ```text
    ├── ваш_файл.org
    └── attachments/
        └── unique_id/
            └── ваш_файл.png
    ```
