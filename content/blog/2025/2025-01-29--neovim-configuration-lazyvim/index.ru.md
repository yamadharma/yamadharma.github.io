---
title: "NeoVim. Конфигурация LazyVim"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-29T20:35:00+03:00
lastmod: 2025-01-30T13:32:00+03:00
tags: ["vim", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "neovim-configuration-lazyvim"
---

NeoVim. Конфигурация LazyVim.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <http://www.lazyvim.org/>
-   Репозиторий: <https://github.com/LazyVim/LazyVim>
-   Стартовый шаблон: <https://github.com/LazyVim/starter>


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Установка на Linux/macOS {#установка-на-linux-macos}

-   Создание резервной копии текущих файлов Neovim:
    ```shell
    mv ~/.config/nvim{,.bak}
    ## Опционально, но рекомендуется:
    mv ~/.local/share/nvim{,.bak}
    mv ~/.local/state/nvim{,.bak}
    mv ~/.cache/nvim{,.bak}
    ```
-   Клонирование стартового шаблона LazyVim:
    ```shell
    git clone https://github.com/LazyVim/starter ~/.config/nvim
    ```
-   Удаление папки `.git`  для возможности добавления в ваш репозиторий:
    ```shell
    rm -rf ~/.config/nvim/.git
    ```
-   Запуск Neovim:
    ```shell
    nvim
    ```


### <span class="section-num">2.2</span> Установка на Windows {#установка-на-windows}

-   Создание резервной копии текущих файлов Neovim:
    ```shell
    Move-Item $env:LOCALAPPDATA\nvim\{,.bak}
    ## Опционально, но рекомендуется:
    Move-Item $env:LOCALAPPDATA\nvim-data\{,.bak}
    ```
-   Клонирование стартового шаблона LazyVim:
    ```shell
    git clone https://github.com/LazyVim/starter $env:LOCALAPPDATA\nvim
    ```
-   Удаление папки `.git`  для возможности добавления в ваш репозиторий:
    ```shell
    Remove-Item $env:LOCALAPPDATA\nvim\.git -Recurse -Force
    ```
-   Запуск Neovim:
    ```shell
    nvim
    ```


## <span class="section-num">3</span> Структура файлов {#структура-файлов}

-   Структура файлов конфигурации:
    -   Все файлы конфигурации находятся в каталоге `config` . Они будут автоматически загружены в нужное время, поэтому вручную подключать их не нужно.
    -   Пользовательские плагины можно добавлять в `lua/plugins/` . Все файлы оттуда будут автоматически загружаться LazyVim.
-   Цветовая схема и иконки:

    -   Эти параметры можно настроить как опции для плагина LazyVim. Например, в `lua/plugins/core.lua`:

    <!--listend-->

    ```conf-unix
    return {
        { "LazyVim/LazyVim", opts = { colorscheme = "catppuccin" } }
    }
    ```
-   Настройки по умолчанию:

    -   В файле `init.lua`  можно задать параметры по умолчанию:

    <!--listend-->

    ```conf-unix
    defaults = {
        autocmds = true,
        keymaps = true,
        options = {
            colorscheme = function() require("tokyonight").load() end
        }
    }
    ```
-   Автокоманды и раскладки:
    -   Настройки автокоманд и раскладок находятся в файлах `autocmds.lua` и `keymaps.lua` в каталоге `config`.
-   Дополнительные настройки:
    -   Вы можете добавлять пользовательские спецификации плагинов в `lua/plugins/`.
-   Пример структуры каталогов:
    ```shell
    ~/.config/nvim/
    ├── lua/
    │   ├── config/
    │   │   ├── autocmds.lua
    │   │   ├── keymaps.lua
    │   │   ├── lazy.lua
    │   │   └── options.lua
    │   └── plugins/
    │       ├── spec1.lua
    │       └── spec2.lua
    └── init.lua
    ```
