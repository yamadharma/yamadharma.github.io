---
title: "XDG. Приложения MIME"
author: ["Dmitry S. Kulyabov"]
date: 2023-04-02T13:39:00+03:00
lastmod: 2024-07-31T15:59:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "xdg-mime-applications"
---

Настройка вызова приложений с помощью спецификации MIME.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Файлы конфигурации {#файлы-конфигурации}


### <span class="section-num">1.1</span> Общая информация {#общая-информация}

-   Приложения по умолчанию для каждого типа MIME хранятся в файлах `mimeapps.list`, которые могут храниться в нескольких местах.


### <span class="section-num">1.2</span> Расположение файлов конфигурации {#расположение-файлов-конфигурации}

-   Файлы конфигурации проверяются в следующем порядке.
-   Более ранние ассоциации имеют приоритет над более поздними.

| Путь                                          | Применение                                                  |
|-----------------------------------------------|-------------------------------------------------------------|
| `~/.config/mimeapps.list`                     | Пользовательские переопределения                            |
| `/etc/xdg/mimeapps.list`                      | Общесистемные переопределения                               |
| `~/.local/share/applications/mimeapps.list`   | Пользовательские переопределения (устаревшее)               |
| `/usr/local/share/applications/mimeapps.list` | Переопределения, предоставляемые дистрибутивом по умолчанию |
| `/usr/share/applications/mimeapps.list`       | Переопределения, предоставляемые дистрибутивом по умолчанию |

-   Можно определить приложения по умолчанию, специфичные для конкретной среды рабочего стола, с помощью файла вида `desktop-mimeapps.list`, где `desktop` это имя среды рабочего стола (из переменной окружения `XDG_CURRENT_DESKTOP`).
    -   Например, `/etc/xdg/xfce-mimeapps.list` задают общесистемные переопределения приложений по умолчанию для Xfce.
-   Некоторые приложения всё ещё используют файл `~/.local/share/applications/mimeapps.list`.
    -   Для сохранения совместимости можно создать символическую ссылку на `~/.config/mimeapps.list`:
        ```shell
        ln -s ~/.config/mimeapps.list ~/.local/share/applications/mimeapps.list
        ```


### <span class="section-num">1.3</span> Формат файлов конфигурации {#формат-файлов-конфигурации}

-   Файл `mimeapps.list` имеет следующий формат:
    ```conf-unix
    [Added Associations]
    image/jpeg=bar.desktop;baz.desktop
    video/H264=bar.desktop
    [Removed Associations]
    video/H264=baz.desktop
    [Default Applications]
    image/jpeg=foo.desktop
    ```
-   Разделы файла:
    -   _Added Associations_ (Добавленные ассоциации): приложения поддерживают открытие этого типа MIME.
        -   Например, `bar.desktop` и `baz.desktop` могут открывать изображения JPEG.
    -   _Removed Associations_ (Удаленные ассоциации): приложения не поддерживают этот тип MIME.
        -   Например, `baz.desktop` не может открыть видео H.264.
    -   _Default Applications_ (Приложения по умолчанию): приложения должны выбираться по умолчанию для открытия этого типа MIME.
        -   Например, изображения JPEG должны быть открыты с помощью `foo.desktop`.
        -   Если есть несколько приложений, они проверяются по порядку.
-   Каждый раздел является необязательным и может быть опущен, если он не нужен.


### <span class="section-num">1.4</span> Ярлык приложения {#ярлык-приложения}

-   Для связывания приложений с типами MIME требуются ярлык приложения (`desktop`-файл).
-   Если в ярлыке приложения не указан тип MIME под его ключом `MimeType`, он не будет учитываться, когда приложение необходимо для открытия этого типа.
-   Следует изменить `mimeapps.list`, чтобы добавить связь между файлом `.desktop` и типом MIME.


## <span class="section-num">2</span> Утилиты работы со списком приложений {#утилиты-работы-со-списком-приложений}


### <span class="section-num">2.1</span> `xdg-mime` {#xdg-mime}


#### <span class="section-num">2.1.1</span> Общая информация {#общая-информация}

-   `xdg-mime` (1) --- скрипт для прямого запроса и изменения стандартных приложений MIME.


#### <span class="section-num">2.1.2</span> Определение MIME-типа файла {#определение-mime-типа-файла}

-   Определение MIME-типа файла:
    ```shell
    $ xdg-mime query filetype photo.jpeg
    image/jpeg
    ```


#### <span class="section-num">2.1.3</span> Определение приложения по умолчанию для MIME-типа {#определение-приложения-по-умолчанию-для-mime-типа}

-   Определение приложения по умолчанию для MIME-типа:
    ```shell
    $ xdg-mime query default image/jpeg
    gimp.desktop
    ```


#### <span class="section-num">2.1.4</span> Изменение приложения по умолчанию для MIME-типа {#изменение-приложения-по-умолчанию-для-mime-типа}

-   Изменение приложения по умолчанию для MIME-типа:
    ```shell
    xdg-mime default feh.desktop image/jpeg
    ```


#### <span class="section-num">2.1.5</span> Отладка приложения по умолчанию для MIME-типа {#отладка-приложения-по-умолчанию-для-mime-типа}

-   Отладка приложения по умолчанию для MIME-типа:
    ```shell
    env XDG_UTILS_DEBUG_LEVEL=10  xdg-mime query default text/html
    ```
-   В результате получаем список конфигурационных файлов, которые просматриваются для определения приложения по умолчанию.


#### <span class="section-num">2.1.6</span> Обработчики URL схем {#обработчики-url-схем}

-   Для установки приложений по умолчанию для URL схем необходимо определить приложение по умолчанию для `x-scheme-handler/*` MIME-типов:
    ```shell
    xdg-mime default firefox.desktop x-scheme-handler/https x-scheme-handler/http
    ```


### <span class="section-num">2.2</span> `xdg-settings` {#xdg-settings}

-   Установить приложение для открытия всех веб-типов MIME с помощью одного приложения:
    ```shell
    xdg-settings set default-web-browser firefox.desktop
    ```
-   Установить приложение по умолчанию для схемы URL:
    ```shell
    xdg-settings set default-url-scheme-handler irc xchat.desktop
    ```
