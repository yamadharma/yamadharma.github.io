---
title: "Управление файлами конфигурации. Домашний каталог. Репозиторий"
author: ["Dmitry S. Kulyabov"]
date: 2023-07-30T14:24:00+03:00
lastmod: 2024-03-25T15:33:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "configuration-file-management-repo"
---

Репозиторий конфигурационных файлов для домашнего каталога.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Набор конфигурационных файлов.
-   Конфигурационные файлы сделаны в формате Chezmoi (см. [Управление файлами конфигурации. Домашний каталог. Chezmoi]({{< relref "2022-10-28-configuration-file-management-chezmoi" >}})).


## <span class="section-num">2</span> Конфигурация для десктопа {#конфигурация-для-десктопа}

-   Репозиторий: <https://github.com/yamadharma/dotfiles-template>


### <span class="section-num">2.1</span> Содержимое {#содержимое}

-   Bash
-   Tmux
-   i3wm (см. [Window manager i3]({{< relref "2021-05-14-window-manager-i3" >}}))
-   Sway (см. [Переход на Sway]({{< relref "2020-09-10-migration-sway" >}}))


### <span class="section-num">2.2</span> Установка {#установка}


#### <span class="section-num">2.2.1</span> Создание собственного репозитория с помощью утилит {#создание-собственного-репозитория-с-помощью-утилит}

-   Будем использовать утилиты командной строки для работы с github (см. [github: утилиты командной строки]({{< relref "2021-08-04-github-command-line-utilities" >}})).
-   Создадим свой репозиторий для конфигурационных файлов на основе шаблона:
    ```shell
    gh repo create dotfiles --template="yamadharma/dotfiles-template" --private
    ```


#### <span class="section-num">2.2.2</span> Подключение репозитория к своей системе {#подключение-репозитория-к-своей-системе}

-   Инициализируйте `chezmoi` с вашим репозиторием `dotfiles`:
    ```shell
    chezmoi init git@github.com:<username>/dotfiles.git
    ```
-   Проверьте, какие изменения внесёт `chezmoi` в домашний каталог, запустив:
    ```shell
    chezmoi diff
    ```
-   Если вас устраивают изменения, внесённые `chezmoi`, запустите:
    ```shell
    chezmoi apply -v
    ```


## <span class="section-num">3</span> Ресурсы {#ресурсы}

-   Awesome Dotfiles : <https://github.com/webpro/awesome-dotfiles>
-   Your unofficial guide to dotfiles on GitHub : <https://dotfiles.github.io/>
