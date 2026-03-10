---
title: "XDG. Каталоги"
author: ["Dmitry S. Kulyabov"]
date: 2024-10-19T18:21:00+03:00
lastmod: 2024-10-19T18:47:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "xdg-directories"
---

XDG. Каталоги

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Спецификация: <https://specifications.freedesktop.org/basedir-spec/>


## <span class="section-num">2</span> Каталоги XDG {#каталоги-xdg}


### <span class="section-num">2.1</span> Каталоги XDG и переменные окружения {#каталоги-xdg-и-переменные-окружения}

-   `$XDG_DATA_DIRS` : `/usr/local/share/:/usr/share/`, упорядоченный по предпочтениям набор каталогов для поиска файлов данных.
-   `$XDG_CONFIG_DIRS` : `/etc/xdg`, упорядоченный по предпочтениям набор каталогов для поиска файлов конфигурации.


### <span class="section-num">2.2</span> Домашние каталоги пользователя и переменные окружения {#домашние-каталоги-пользователя-и-переменные-окружения}

-   `XDG_DATA_HOME` : `$HOME/.local/share`, пользовательские файлы данных.
-   `XDG_CONFIG_HOME` : `$HOME/.config`, пользовательские файлы конфигурации.
-   `XDG_STATE_HOME` : `$HOME/.local/state`, данные о состоянии, которые должны сохраняться между перезапусками (приложения), но не являются важными или переносимыми.
-   `XDG_CACHE_HOME` : `$HOME/.cache`, файлы второстепенных данных, специфичные для пользователя.
-   `XDG_RUNTIME_HOME` : `/run/user/$UID`, несущественные для пользователя файлы времени выполнения и другие файловые объекты (такие как сокеты, именованные каналы и т. д.).
-   `$HOME/.local/bin`, пользовательские исполняемые файлы.


### <span class="section-num">2.3</span> Другие операционные системы {#другие-операционные-системы}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Каталоги XDG для разных операционных систем
</div>

| Переменная окружения XDG | Linux (и BSD)                    | Mac                             | Windows          |
|--------------------------|----------------------------------|---------------------------------|------------------|
| `XDG_DATA_DIRS`          | `/usr/local/share`, `/usr/share` | `/Library/Application Support`  | `%PROGRAMDATA%`  |
| `XDG_DATA_HOME`          | `~/.local/share`                 | `~/Library/Application Support` | `%APPDATA%`      |
| `XDG_CONFIG_DIRS`        | `/etc/xdg`                       | `/Library/Application Support`  | `%PROGRAMDATA%`  |
| `XDG_CONFIG_HOME`        | `~/.config`                      | `~/Library/Application Support` | `%APPDATA%`      |
| `XDG_CACHE_HOME`         | `~/.cache`                       | `~/Library/Caches`              | `%LOCALAPPDATA%` |


## <span class="section-num">3</span> Программные реализации {#программные-реализации}


### <span class="section-num">3.1</span> xdg {#xdg}

-   Кроссплатформенный пакет, реализующий стандарт XDG.
-   Репозиторий: <https://github.com/OpenPeeDeeP/xdg>
