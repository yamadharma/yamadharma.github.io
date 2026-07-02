---
title: "Emacs. Поддержка броузеров"
author: ["Dmitry S. Kulyabov"]
date: 2026-05-15T17:22:00+03:00
lastmod: 2026-05-15T17:32:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-browser-support"
---

Emacs. Поддержка броузеров.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   За открытие ссылок и html-файлов отвечает встроенный пакет `browse-url`.


## <span class="section-num">2</span> Базовые команды {#базовые-команды}

-   Явные команды:

-   `M-x browse-url` : запросит URL и откроет его в броузере.
-   `M-x browse-url-at-point` : откроет URL, на который указывает курсор.
-   `M-x browse-url-of-file` : позволит выбрать локальный HTML-файл и откроет его.
-   `M-x browse-url-of-buffer` : создаст временный файл из текущего буфера и откроет его в броузере.


## <span class="section-num">3</span> Броузер по умолчанию {#броузер-по-умолчанию}

-   Нужно явно указать нужную программу через переменную `browse-url-browser-function`.


### <span class="section-num">3.1</span> Системный броузер по умолчанию {#системный-броузер-по-умолчанию}

```elisp
(setq browse-url-browser-function 'browse-url-default-browser)
```


### <span class="section-num">3.2</span> Напрямую указать броузер {#напрямую-указать-броузер}

-   Google Chrome:
    ```elisp
    (setq browse-url-browser-function 'browse-url-chrome)
    ```

-   Firefox:
    ```elisp
    (setq browse-url-browser-function 'browse-url-firefox)
    ```

-   Через `xdg-open`
    ```elisp
    (setq browse-url-browser-function 'browse-url-generic)
    (setq browse-url-generic-program "xdg-open")
    ```


## <span class="section-num">4</span> Разные броузеры для разных URL {#разные-броузеры-для-разных-url}

-   Иногда удобно открывать разные типы ссылок в разных броузерах.
-   Например, рабочие сайты --- в Chrome, а всё остальное --- в Firefox.
-   Для этого можно настроить список правил `browse-url-handlers`.

<!--listend-->

```elisp
(setq browse-url-handlers
      '(("docs.google.com" . browse-url-firefox)        ;; Google Docs в Firefox
        ("github.com" . browse-url-chrome)              ;; GitHub в Chrome
        ("." . browse-url-default-browser)))            ;; Все остальное в системный броузер
```
