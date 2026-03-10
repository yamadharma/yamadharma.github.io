---
title: "Fish. Полезные плагины"
author: ["Dmitry S. Kulyabov"]
date: 2025-02-14T21:29:00+03:00
lastmod: 2025-02-27T17:33:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "fish-useful-plugins"
---

Fish. Полезные плагины.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Для установки можно использовать Fisher (см. [Fish. Менеджер плагинов Fisher]({{< relref "2025-02-14--fish-plugin-manager-fisher" >}})).


## <span class="section-num">2</span> Поддержка git flow {#поддержка-git-flow}

-   [Рабочий процесс Gitflow]({{< relref "2021-04-18-gitflow-workflow" >}})


### <span class="section-num">2.1</span> plugin-git-flow {#plugin-git-flow}

-   Репозиторий: <https://github.com/oh-my-fish/plugin-git-flow>
-   Поддержка завершения для git flow.
-   Установка (fisher):
    ```shell
    fisher install oh-my-fish/plugin-git-flow
    ```
-   У меня работал с ошибками.


### <span class="section-num">2.2</span> git-flow-completion {#git-flow-completion}

-   Репозиторий: <https://github.com/bobthecow/git-flow-completion>
-   Поддержка bash, zsh, fish.
-   Установка:
    ```shell
    wget https://raw.githubusercontent.com/bobthecow/git-flow-completion/refs/heads/master/git.fish -O ~/.config/fish/completions/git.fish
    ```


## <span class="section-num">3</span> Замена ls на lsd {#замена-ls-на-lsd}


### <span class="section-num">3.1</span> fish-plugin-lsd {#fish-plugin-lsd}

-   Отображает содержание каталога с помощью `lsd` после перехода в него с помощью `cd`.
-   Репозиторий: <https://github.com/tacomilkshake/fish-plugin-lsd>
-   Установка (fisher):
    ```shell
    fisher install jamiesteven/fish-plugin-lsd
    ```


### <span class="section-num">3.2</span> Задание алиаса {#задание-алиаса}

-   Задайте алиас:
    ```shell
    alias --save ls='lsd'
    ```
-   Это создаст файл `~/.config/fish/functions/ls.fish`:
    ```fish
    unction ls --wraps=lsd --description 'alias ls=lsd'
      lsd $argv
    end
    ```


## <span class="section-num">4</span> Поддержка fzf {#поддержка-fzf}


### <span class="section-num">4.1</span> PatrickF1/fzf.fish {#patrickf1-fzf-dot-fish}

-   Репозиторий: <https://github.com/PatrickF1/fzf.fish>
-   [Fish. Плагин PatrickF1/fzf.fish]({{< relref "2025-02-27--fish-plugins-patrickf1-fzf-fish" >}})
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


## <span class="section-num">5</span> Поддержка командного режима VirtualBox {#поддержка-командного-режима-virtualbox}

-   Репозиторий: <https://github.com/jduchateau/fish-virtualbox-completions?tab=readme-ov-file>
-   Установка (fisher):
    ```shell
    fisher install jduchateau/fish-virtualbox-completions
    ```
