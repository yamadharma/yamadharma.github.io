---
title: "XDG. Пользовательские каталоги"
author: ["Dmitry S. Kulyabov"]
date: 2021-09-16T20:15:00+03:00
lastmod: 2024-10-19T18:22:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "xdg-user-directories"
---

Пользовательские каталоги по стандарту XDG.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Стандарт XDG задаёт стандартные имена для пользовательских каталогов (см. [XDG. Каталоги]({{< relref "2024-10-19-xdg-directories" >}})).


## <span class="section-num">2</span> Программы {#программы}


### <span class="section-num">2.1</span> Создание каталогов {#создание-каталогов}

-   Для создания каталогов стандарта XDG служит программа `xdg-user-dirs-update`.


### <span class="section-num">2.2</span> Запрос имён каталогов {#запрос-имён-каталогов}

-   Программа `xdg-user-dir` служит для запроса имён каталогов, соответствующих стандартным переменным.
-   Например, для получения каталога для переменной `XDG_TEMPLATES_DIR` (это каталог, содержащий шаблоны):
    ```shell
    xdg-user-dir TEMPLATES
    ```


## <span class="section-num">3</span> Конфигурационные файлы {#конфигурационные-файлы}

-   Включение использования каталогов XDG и их кодировка задаются в файлах:
    -   `/etc/xdg/user-dirs.conf`: уровень системы;
    -   `~/.config/user-dirs.conf`: уровень пользователя.
    -   Содержание данного файла имеет вид:
        ```cfg
        enabled=True
        filename_encoding=UTF-8
        ```
-   Имена каталогов по умолчанию (системный уровень) находятся в файле `/etc/xdg/user-dirs.defaults`:
    ```cfg
    # Default settings for user directories
    #
    # The values are relative pathnames from the home directory and
    # will be translated on a per-path-element basis into the users locale
    DESKTOP=Desktop
    DOWNLOAD=Downloads
    TEMPLATES=Templates
    PUBLICSHARE=Public
    DOCUMENTS=Documents
    MUSIC=Music
    PICTURES=Pictures
    VIDEOS=Videos
    # Another alternative is:
    #MUSIC=Documents/Music
    #PICTURES=Documents/Pictures
    #VIDEOS=Documents/Videos
    ```
-   Локальный файл конфигурации `~/.config/user-dirs.dirs` используется для явного задания имён каталогов.
    -   Например, файл `~/.config/user-dirs.dirs` со стандартными английскими названиями:
        ```cfg
        XDG_DESKTOP_DIR="$HOME/Desktop"
        XDG_DOCUMENTS_DIR="$HOME/Documents"
        XDG_DOWNLOAD_DIR="$HOME/Downloads"
        XDG_MUSIC_DIR="$HOME/Music"
        XDG_PICTURES_DIR="$HOME/Pictures"
        XDG_PUBLICSHARE_DIR="$HOME/Public"
        XDG_TEMPLATES_DIR="$HOME/Templates"
        XDG_VIDEOS_DIR="$HOME/Videos"
        ```
    -   Редактировать этот файл можно как непосредственно, так и с помощью утилиты `xdg-user-dirs-update`.
    -   Например, зададим значение `XDG_DOWNLOAD_DIR` как `$HOME/Internet`:
        ```shell
        xdg-user-dirs-update --set DOWNLOAD ~/Internet
        ```
-   Локальный файл конфигурации `~/.config/user-dirs.locale` используется для явной установки локали.


## <span class="section-num">4</span> Локализация названий каталогов {#локализация-названий-каталогов}

-   Иногда русские названия стандартных каталогов не очень удобны. Например, при работе в консоли приходится переключать язык.
-   Для принудительного создания каталогов с английскими именами можно использовать:
    ```shell
    LC_ALL=en_US xdg-user-dirs-update --force
    ```
-   Для фиксации локали для каталогов нужно задать её в файле конфигурации:
    ```shell
    echo 'en_US' > ~/.config/user-dirs.locale
    ```

    -   После этого надо пересоздать каталоги:
        ```shell
        LC_ALL=en_US xdg-user-dirs-update --force
        ```
