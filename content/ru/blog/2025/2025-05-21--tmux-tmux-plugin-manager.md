---
title: "tmux. Tmux Plugin Manager"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-21T17:08:00+03:00
lastmod: 2025-05-21T18:01:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "tmux-tmux-plugin-manager"
---

Tmux Plugin Manager.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Tmux Plugin Manager (TPM) --- это менеджер плагинов для терминального мультиплексора Tmux, написанный на Bash.
-   Автоматизирует установку, обновление и удаление плагинов, избавляя от ручного управления.
-   Репозиторий: <https://github.com/tmux-plugins/tpm>
-   Список плагинов: <https://github.com/tmux-plugins/list>


## <span class="section-num">2</span> Установка {#установка}

-   Клонирование репозитория:
    ```shell
    mkdir -p ~/.tmux/plugins
    git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
    ```

-   Добавить в конфигурационный файл (`~/.tmux.conf` или `$XDG_CONFIG_HOME/tmux/tmux.conf`):
    ```shell
    # Список плагинов
    set -g @plugin 'tmux-plugins/tpm'
    set -g @plugin 'tmux-plugins/tmux-sensible'  # пример плагина

    # Инициализация TPM (должна быть в конце файла)
    run '~/.tmux/plugins/tpm/tpm'
    ```

-   После этого выполните (внутри сессии tmux):
    ```shell
    tmux source ~/.tmux.conf
    ```
-   Или:
    ```shell
    tmux source ~/.config/tmux/tmux.conf
    ```

<!--listend-->

-   Автоматическая установка TPM.
-   Добавьте в `~/.tmux.conf`:
    ```shell
    if "test ! -d ~/.tmux/plugins/tpm" \
      "run 'git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm && ~/.tmux/plugins/tpm/bin/install_plugins'"
    ```

    -   Это установит TPM при первом запуске Tmux.


## <span class="section-num">3</span> Основные команды {#основные-команды}

-   Установка плагинов:
    -   Добавьте строку `set -g @plugin 'автор/репозиторий'` в `~/.tmux.conf`.
    -   Нажмите `Prefix + I` (Shift + i), чтобы TPM скачал и подключил плагины:
        ```shell
        set -g @plugin 'tmux-plugins/tmux-resurrect'  # сохранение сессий
        ```

-   Обновление плагинов:
    -   Всех: `Prefix + U` (Shift + u).
    -   Конкретного: `Prefix + Alt + u`, затем введите имя плагина.
-   Удаление плагинов:
    -   Удалите строку плагина из `~/.tmux.conf`.
    -   Нажмите `Prefix + Alt + u` для очистки неиспользуемых плагинов.


## <span class="section-num">4</span> Особенности работы {#особенности-работы}

-   Декларативная конфигурация
    -   Плагины объявляются в `~/.tmux.conf`, а TPM автоматически подгружает их при старте Tmux.
    -   Пример настройки tmux-resurrect:
        ```shell
        set -g @resurrect-capture-pane-contents 'on'  # сохраняет содержимое панелей
        ```

-   Зависимости:
    -   TPM устанавливает зависимости плагинов автоматически.
    -   Например, `tmux-logging` требует `tmux-prefix-highlight`.
-   Обновление самого TPM:
    ```shell
    cd ~/.tmux/plugins/tpm && git pull
    ```


## <span class="section-num">5</span> Популярные плагины {#популярные-плагины}

-   tmux-resurrect : сохранение/восстановление сессий.
-   tmux-yank : копирование в системный буфер.
-   tmux-prefix-highlight : подсветка активного префикса.
-   tmux-battery : отображение заряда батареи в статус-баре.
