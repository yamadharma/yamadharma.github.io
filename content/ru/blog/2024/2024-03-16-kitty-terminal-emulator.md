---
title: "Эмулятор терминала kitty"
author: ["Dmitry S. Kulyabov"]
date: 2024-03-16T17:07:00+03:00
lastmod: 2024-10-09T11:00:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "kitty-terminal-emulator"
---

Эмулятор терминала kitty.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://sw.kovidgoyal.net/kitty/>
-   Репозиторий: <https://github.com/kovidgoyal/kitty>
-   Поддерживает мозаичный режим (тайлинг), TrueColor, лигатуры, расширения для работы с клавиатурой и рендеринга изображений.


## <span class="section-num">2</span> Ресурсы {#ресурсы}


### <span class="section-num">2.1</span> Темы {#темы}

-   Основные темы: <https://github.com/kovidgoyal/kitty-themes>
-   Ещё темы: <https://github.com/dexpota/kitty-themes>


### <span class="section-num">2.2</span> Конфигурации {#конфигурации}

-   <https://github.com/ttys3/my-kitty-config>


## <span class="section-num">3</span> Конфигурация {#конфигурация}


### <span class="section-num">3.1</span> Для редакторов {#для-редакторов}

-   Заголовок для редакторов:
    ```conf-unix
    # vim:fileencoding=utf-8:foldmethod=marker
    ```


### <span class="section-num">3.2</span> Структура {#структура}

-   Подключение отдельных конфигурационных файлов:
    ```conf-unix
    # Include *.conf files from all subdirs of kitty.d inside the kitty config dir
    globinclude kitty.d/**/*.conf
    ```
-   Подключим переменные среды:
    ```conf-unix
    # Include the *contents* of all env vars starting with KITTY_CONF_
    envinclude KITTY_CONF_*
    ```


### <span class="section-num">3.3</span> Темы {#темы}


#### <span class="section-num">3.3.1</span> Настройка вручную {#настройка-вручную}

-   Посмотреть все темы:
    ```shell
    kitty +kitten themes
    ```
-   В списке можно выбрать тему.
-   Конфигурация темы будет добавлена в `~/.config/kitty/current-theme.conf`.
-   В свою очередь этот файл будет подключён к конфигурации `kitty.conf`.
-   Можно вручную перегрузить тему во всех терминалах (например, задав тему _Dimmed Monokai_):
    ```shell
    kitten themes --reload-in=all Dimmed Monokai
    ```


#### <span class="section-num">3.3.2</span> Конфигурационный файл {#конфигурационный-файл}

-   Для примера подключим тему _Wryan_.
-   Конфигурация темы (файл `current-theme.conf`):
    ```conf-unix
    background            #101010
    foreground            #999993
    cursor                #9d9eca
    selection_background  #4d4d4d
    color0                #333333
    color8                #3d3d3d
    color1                #8c4665
    color9                #bf4d80
    color2                #287373
    color10               #53a6a6
    color3                #7c7c99
    color11               #9e9ecb
    color4                #395573
    color12               #477ab3
    color5                #5e468c
    color13               #7e62b3
    color6                #31658c
    color14               #6096bf
    color7                #899ca1
    color15               #c0c0c0
    selection_foreground #101010
    ```
-   Подключим файл темы:
    ```conf-unix
    # BEGIN_KITTY_THEME
    # Wryan
    include current-theme.conf
    # END_KITTY_THEME
    ```
