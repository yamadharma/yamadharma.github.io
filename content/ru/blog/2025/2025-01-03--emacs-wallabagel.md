---
title: "Emacs. Отложенное чтение. wallabag.el"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-03T14:36:00+03:00
lastmod: 2025-01-11T20:42:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-wallabagel"
---

Emacs. Отложенное чтение. wallabag.el.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/chenyanming/wallabag.el>
-   Интерфейс для использование приложения отложенного чтения Wallabag (см. [Отложенное чтение. Wallabag]({{< relref "2024-12-05-read-it-later-wallabag" >}}))


## <span class="section-num">2</span> Установка {#установка}

-   Необходимо задать параметры подключения к сервису:
    ```elisp
    (require 'wallabag)
    (setq wallabag-host "https://xx.xx.xx") ;; wallabag server host name
    (setq wallabag-username "xx") ;; username
    (setq wallabag-password "xx") ;; password
    (setq wallabag-clientid "xx") ;; created with API clients management
    (setq wallabag-secret "xx") ;; created with API clients management
    ```

    -   Запуск с помощью `M-x wallabag`.


### <span class="section-num">2.1</span> Использование `auth-sources` {#использование-auth-sources}

-   Создайте зашифрованный `~/.authinfo.gpg`  файл со строками:
    ```conf-unix
    machine <wallabag-host> login <username> password <password>
    machine <wallabag-client> login <client-id> password <client-secret>

    ```
-   Используйте при настройке пароля Wallabag и секретных переменных:
    ```elisp
    (setq wallabag-password (auth-source-pick-first-password :host "<wallabag-host>")
          wallabag-secret (auth-source-pick-first-password :host "<wallabag-client>"))
    ```


## <span class="section-num">3</span> Привязка клавиш {#привязка-клавиш}


### <span class="section-num">3.1</span> Функции могут использоваться вне режима wallabag {#функции-могут-использоваться-вне-режима-wallabag}

| `wallabag`                                 | Буфер `*wallabag-search*`                                                                             |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `wallabag-find`                            | Выберите записи wallabag из списка с помощью ivy                                                      |
| `wallabag-full-update`                     | Выполните полное обновление базы данных. Он всегда может обновлять локальную базу данных              |
| `wallabag-request-token`                   | Запросить новый токен                                                                                 |
| `wallabag-add-entry`                       | Добавьте одну запись на сервер wallabag с url-адресом и тегами                                        |
| `wallabag-insert-entry`                    | Вставьте запись на сервер wallabag с текущим содержимым буфера                                        |
| `wallabag-request-new-entries`             | Запросить новые записи в фоновом режиме                                                               |
| `wallabag-request-and-synchronize-entries` | Запрашивать и синхронизировать записи, контролируемые `wallabag-number-of-entries-to-be-synchronized` |


### <span class="section-num">3.2</span> wallabag-search-mode {#wallabag-search-mode}

| &lt;RET&gt;           | `wallabag-view`                                | Просмотреть запись                                                                     |
|-----------------------|------------------------------------------------|----------------------------------------------------------------------------------------|
| v                     | `wallabag-view`                                | Просмотреть запись                                                                     |
| V                     | `wallabag-browse-url`                          | Просмотрите url-адрес текущей записи (откроется в браузере)                            |
| o                     | `wallabag-original-entry`                      | Откройте исходную html-запись                                                          |
| s (non-evil), /(evil) | `wallabag-search-live-filter`                  | Фильтровать буфер `*wallabag-search*`                                                  |
| q                     | `wallabag-search-quit`                         | Выйти                                                                                  |
| g (non-evil), r(evil) | `wallabag-search-refresh-and-clear-filter`     | Обновите wallabag и очистить фильтр                                                    |
| G (non-evil), R(evil) | `wallabag-search-clear-filter`                 | Очистить фильтр                                                                        |
| u                     | `wallabag-search-update-and-clear-filter`      | Запросить новые записи, очистить ключевое слово фильтра и обновить `*wallabag-search*` |
| U                     | `wallabag-search-synchronize-and-clear-filter` | Синхронизируйте записи, очистить ключевое слово фильтра и обновить `*wallabag-search*` |
| m                     | `wallabag-mark-and-forward`                    | Отметить запись                                                                        |
| &lt;DEL&gt;           | `wallabag-unmark-and-backward`                 | Снять отметку с записи                                                                 |
| a                     | `wallabag-add-entry`                           | Добавить запись                                                                        |
| d                     | `wallabag-delete-entry`                        | Удалить запись                                                                         |
| n(non-evil), j(evil)  | `wallabag-next-entry`                          | Перейти к следующей записи                                                             |
| p(non-evil), k(evil)  | `wallabag-previous-entry`                      | Перейти к предыдущей записи.                                                           |
| w(non-evil), y(evil)  | `wallabag-org-link-copy`                       | Скопируйте отмеченные записи как ссылки org-mode                                       |
| t                     | `wallabag-add-tags`                            | Добавьте теги (через запятую) к записи                                                 |
| T                     | `wallabag-remove-tag`                          | Удалить один тег из списка                                                             |
| ‘                     | `wallabag-toggle-sidebar`                      | Переключить боковую панель                                                             |
| x                     | `wallabag-update-entry-archive`                | Переключить архивный статус (прочитанный/непрочитанный)                                |
| f                     | `wallabag-update-entry-starred`                | Переключить статус избранного                                                          |
| i                     | `wallabag-update-entry-title`                  | Обновить заголовок                                                                     |
| I                     | `wallabag-update-entry-origin_url`             | Обновите исходный url                                                                  |


### <span class="section-num">3.3</span> wallabag-entry-mode {#wallabag-entry-mode}

| `r`         | `wallabag-view`           | Обновить запись                |
|-------------|---------------------------|--------------------------------|
| `V`         | `wallabag-browse-url`     | Посмотреть url текущей записи  |
| o           | `wallabag-original-entry` | Откройте запись в формате html |
| q           | `wallabag-entry-quit`     | Выход из `*wallabag-entry*`    |
| mouse-1     | `wallabag-mouse-1`        | Посмотреть url                 |
| &lt;RET&gt; | `wallabag-ret`            | Посмотреть url                 |


### <span class="section-num">3.4</span> wallabag-sidebar-mode {#wallabag-sidebar-mode}

| `'`                        | `wallabag-toggle-sidebar`            | Переключить боковую панель      |
|----------------------------|--------------------------------------|---------------------------------|
| &lt;RET&gt;                | `wallabag-sidebar-find-tag`          | Фильтровать по тегу в точке     |
| `g` (non-evil), `r` (evil) | `wallabag-search-clear-filter`       | Очистите ключевое слово фильтра |
| `G` (non-evil), `R` (evil) | `wallabag-search-clear-filter`       | Очистите ключевое слово фильтра |
| `n`                        | `wallabag-sidebar-find-next-tag`     | Фильтровать по следующему тегу  |
| `p`                        | `wallabag-sidebar-find-previous-tag` | Фильтровать по предыдущему тегу |
| `q`                        | `wallabag-sidebar-quit`              | Выйти из режима боковой панели  |
