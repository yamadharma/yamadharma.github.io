---
title: "Fish. Менеджер плагинов Fisher"
author: ["Dmitry S. Kulyabov"]
date: 2025-02-14T21:10:00+03:00
lastmod: 2025-05-24T13:35:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "fish-plugin-manager-fisher"
---

Fish. Менеджер плагинов Fisher.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Менеджер плагинов.
-   Репозиторий: <https://github.com/jorgebucaran/fisher>


## <span class="section-num">2</span> Установка {#установка}

-   Установить Fisher:
    ```shell
    curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher
    ```
-   Фактически добавляются файлы:
    -   `~/.config/fish/functions/fisher.fish`
    -   `~/.config/fish/completions/fisher.fish`


## <span class="section-num">3</span> Работа с плагинами {#работа-с-плагинами}


### <span class="section-num">3.1</span> Установка плагина {#установка-плагина}

-   Установка плагина из репозитория GitHub:
    ```shell
    fisher install <user_name>/<repo_name>
    ```

-   Установка плагина из локального каталога:
    ```shell
    fisher install ~/path/to/plugin
    ```


### <span class="section-num">3.2</span> Список плагинов {#список-плагинов}

-   Просмотр списка установленных плагинов:
    ```shell
    fisher list
    ```


### <span class="section-num">3.3</span> Обновление плагинов {#обновление-плагинов}

-   Обновление установленного плагина:
    ```shell
    fisher update <user_name>/<repo_name>
    ```


### <span class="section-num">3.4</span> Удаление плагина {#удаление-плагина}

-   Удаления установленного плагина:
    ```shell
    fisher remove <user_name>/<repo_name>
    ```


## <span class="section-num">4</span> Ресурсы {#ресурсы}

-   Fish Awesome: <https://github.com/jorgebucaran/awsm.fish>
