---
title: "tmux. Конфигурация Oh My Tmux"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-21T18:07:00+03:00
lastmod: 2025-05-21T18:19:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "tmux-oh-my-tmux"
---

Конфигурация Oh My Tmux.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/gpakosz/.tmux>


## <span class="section-num">2</span> Ключевые функции {#ключевые-функции}

-   Навигация:
    -   Добавляет вторичный префикс `Ctrl + a` (как в Screen).
    -   Удобно при назначении `Ctrl` на `CapsLock` (см. [Клавиатура. Клавиша Caps Lock]({{< relref "2025-05-06--keyboard-capslock" >}})).
    -   Основной префикс ---  `Ctrl + b`.
-   Интеграция с Vim
    -   Переключайтесь между стилями навигации Vim и Tmux без конфликтов.
-   Статус-бар
    -   Отображает SSH-сессии, заряд батареи, uptime и т. д.
-   Копирование в буфер ОС
    -   На Linux требует `xsel`, `xclip`, `wl-copy`.
    -   На macOS требует `reattach-to-user-namespace`.


## <span class="section-num">3</span> Установка {#установка}

-   Установите конфигурацию, клонировав репозиторий и создав симлинки:
    ```sh
    git clone https://github.com/gpakosz/.tmux.git
    ln -s -f .tmux/.tmux.conf ~/
    cp .tmux/.tmux.conf.local ~/
    ```
-   Кастомизируйте настройки через `~/.tmux.conf.local`, не изменяя основной файл.


## <span class="section-num">4</span> Работа с окнами и панелями {#работа-с-окнами-и-панелями}

-   Максимизация панели
    -   `<prefix> +` : разворачивает панель в отдельное окно.
-   Мышь
    -   Включите/выключите режим мыши через `<prefix> m` для изменения размеров панелей и выбора окон.
-   SSH-сессии
    -   При разделении панели Tmux автоматически переподключается к удалённому серверу.


## <span class="section-num">5</span> Tmux plugin manager {#tmux-plugin-manager}

-   Конфигурация интегрирования с TPM (см. [tmux. Tmux Plugin Manager]({{< relref "2025-05-21--tmux-tmux-plugin-manager" >}})).
