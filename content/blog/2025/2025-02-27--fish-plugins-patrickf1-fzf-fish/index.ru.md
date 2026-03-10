---
title: "Fish. Плагин PatrickF1/fzf.fish"
author: ["Dmitry S. Kulyabov"]
date: 2025-02-27T15:56:00+03:00
lastmod: 2025-02-27T17:33:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "fish-plugins-patrickf1-fzf-fish"
---

Fish. Плагин PatrickF1/fzf.fish.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/PatrickF1/fzf.fish>


## <span class="section-num">2</span> Установка {#установка}

-   Установка пререквизитов:
    ```shell
    emerge app-shells/fish
    emerge app-shells/fzf
    emerge sys-apps/bat
    emerge sys-apps/fd
    ```
-   Установка (системный пакет, репозиторий `guru`, см. [Gentoo. Дополнительные репозитории]({{< relref "2023-10-01-gentoo-additional-repositories" >}})):
    ```shell
    fisher install PatrickF1/fzf.fish
    ```
-   Установка (fisher):
    ```shell
    fisher install PatrickF1/fzf.fish
    ```


## <span class="section-num">3</span> Сочетания клавиш {#сочетания-клавиш}


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   Табуляция используется для выбора нескольких записей.
-   Если вы запустите поиск, когда ваш курсор находится на слове, это слово будет использовано для запроса fzf и будет заменено выбранным вами.
-   Все поисковые запросы включают предварительный просмотр объекта, на который наведён курсор.
-   Для ручной привязки используйте `fzf_configure_bindings`:
    ```shell
    fzf_configure_bindings --help
    ```


### <span class="section-num">3.2</span> Поиск по каталогу {#поиск-по-каталогу}

-   Сочетание клавиш: `Ctrl+Alt+F`
-   Мнемоника: `F` for _file_
-   Ввод FZF: рекурсивный список не скрытых файлов текущего каталога
-   Вывод:  относительные пути выбранных файлов
-   Окно предварительного просмотра: файл с выделением синтаксиса, содержанием каталога или типом файла


### <span class="section-num">3.3</span> Поиск по журналу GIT {#поиск-по-журналу-git}

-   Сочетание клавиш: `Ctrl+Alt+L`
-   Мнемоника: `L` for _log_
-   Вход FZF: отформатированный `git log` текущего репозитория
-   Вывод: хэши выбранных коммитов
-   Окно предварительного просмотра: Сообщение и различие


### <span class="section-num">3.4</span> Поиск по статусу GIT {#поиск-по-статусу-git}

-   Сочетание клавиш: `Ctrl+Alt+S`
-   Мнемоника: `S` for _status_
-   Вход: `git status` текущего репозитория
-   Вывод: относительные пути
-   Окно предварительного просмотра: `git diff` файла


### <span class="section-num">3.5</span> Поиск по истории командной оболочки {#поиск-по-истории-командной-оболочки}

-   Сочетание клавиш: `Ctrl+R`
-   Мнемоника: `R` for _reverse-i-search_
-   Вход:  история команд
-   Вывод:  выбранные команды
-   Окно предварительного просмотра: вся команды


### <span class="section-num">3.6</span> Поиск по процессам {#поиск-по-процессам}

-   Сочетание клавиш: `Ctrl+Alt+P`
-   Мнемоника: `P` for _process_
-   Вход: вывод `ps`
-   Вывод: pid процесса
-   Окно предварительного просмотра: использование ЦП, использование памяти, время запуска и т.д.


### <span class="section-num">3.7</span> Поиск по переменным {#поиск-по-переменным}

-   Сочетание клавиш: `Ctrl+V`
-   Мнемоника: `V` for _variable_
-   Вход: все переменные оболочки
-   Вывод:  выбранные переменные оболочки
-   Окно предварительного просмотра:  информация и значения переменной


## <span class="section-num">4</span> Настройка поведения {#настройка-поведения}


### <span class="section-num">4.1</span> Просмотр каталогов и обычных файлов {#просмотр-каталогов-и-обычных-файлов}

-   Поиск по каталогу по умолчанию:
    -   `ls` для просмотра каталогов;
    -   `bat` для просмотра обычных файлов.
-   Чтобы использовать свою собственную команду предварительного просмотра каталога, установите её в `fzf_preview_dir_cmd`:
    ```shell
    set fzf_preview_dir_cmd eza --all --color=always
    ```
-   Можно использовать свою собственную команду предварительного просмотра файлов в переменной `fzf_preview_file_cmd`:
    ```shell
    set fzf_preview_file_cmd cat -n
    ```


### <span class="section-num">4.2</span> Файлы при поиске {#файлы-при-поиске}

-   Чтобы передать пользовательские параметры `fd` установите их в `fzf_fd_opts`:
    ```bash
    set fzf_fd_opts --hidden --max-depth 5
    ```
-   По умолчанию, `fd` скрывает файлы, перечисленные в `.gitignore`.
-   Можно отключить это поведение, добавив флаг `--no-ignore` в `fzf_fd_opts`.


### <span class="section-num">4.3</span> Изменить форматирование поиска в журнале GIT {#изменить-форматирование-поиска-в-журнале-git}

-   Поиск в журнале GIT выполняет командой `git log --format`.
-   Чтобы использовать свой собственный формат, установите его в `fzf_git_log_format`, например, показывать хэш и субъект для каждого коммита:
    ```shell
    set fzf_git_log_format "%H %s"
    ```


### <span class="section-num">4.4</span> Декорирование вывода diff {#декорирование-вывода-diff}

-   Установите команду вызыва highligher в `fzf_diff_highlighter`:
    ```shell
    # width=20 so delta decorations don't wrap around small fzf preview pane
    set fzf_diff_highlighter delta --paging=never --width=20
    # Or, if using DFS
    set fzf_diff_highlighter diff-so-fancy
    ```


### <span class="section-num">4.5</span> Формат времени для поиска {#формат-времени-для-поиска}

-   Измените `fzf_history_time_format`, например, форматируем время даты как `dd-mm-yy`:
    ```shell
    set fzf_history_time_format %d-%m-%y
    ```
