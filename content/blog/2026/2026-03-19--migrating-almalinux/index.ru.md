---
title: "Миграция на AlmaLinux"
author: ["Dmitry S. Kulyabov"]
date: 2026-03-19T14:50:00+03:00
lastmod: 2026-03-19T15:07:00+03:00
tags: ["redhat", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "migrating-almalinux"
---

Миграция на AlmaLinux.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Инструментарий: `almalinux-deploy`.
-   Официальный скрипт от проекта AlmaLinux, предназначенный для автоматической конверсии систем, совместимых с Enterprise Linux (EL), в AlmaLinux.
-   Репозиторий: <https://github.com/AlmaLinux/almalinux-deploy>


### <span class="section-num">1.1</span> Миграция {#миграция}

-   Этапы необходимо выполнять последовательно.


#### <span class="section-num">1.1.1</span> Этап 1. Подготовка системы {#этап-1-dot-подготовка-системы}

-   Полное обновление системы:
    ```shell
    sudo dnf update -y
    sudo reboot
    ```

-   Создание резервной копии.
-   Обеспечение стабильного подключения.
-   Миграция не должна прерываться.
-   Обязательно используйте терминальный мультиплексор, такой как `screen` или `tmux`.


#### <span class="section-num">1.1.2</span> Этап 2. Запуск миграции {#этап-2-dot-запуск-миграции}

-   Скачивание скрипта:
    ```shell
    curl -O https://raw.githubusercontent.com/AlmaLinux/almalinux-deploy/master/almalinux-deploy.sh
    ```

-   Запуск скрипта: Выполните скрипт с правами root.
    ```sh
    sudo bash almalinux-deploy.sh
    ```


#### <span class="section-num">1.1.3</span> Этап 3. Завершение и проверка {#этап-3-dot-завершение-и-проверка}

-   Перезагрузка.
    -   После успешного завершения скрипта (вы увидите сообщение "Migration to AlmaLinux is completed") необходимо перезагрузить систему для загрузки с ядром AlmaLinux.
        ```shell
        sudo reboot
        ```

-   Проверка результата
    -   После перезагрузки убедитесь, что миграция прошла успешно.
    -   Проверьте файл релиза:
        ```shell
        cat /etc/almalinux-release
        # Ожидаемый вывод: AlmaLinux X.Y (дата-версия)
        ```

    -   Проверьте, что загружается ядро AlmaLinux:
        ```shell
        sudo grubby --info DEFAULT | grep AlmaLinux
        # Вывод должен содержать "AlmaLinux" в названии ядра
        ```


### <span class="section-num">1.2</span> Примечания {#примечания}

-   Обработка репозиториев.
    -   Скрипт сопоставляет репозитории для разных дистрибутивов.
-   Логирование и возобновление.
    -   Все действия подробно логируются в файлы `/var/log/almalinux-deploy.log` и `/var/log/almalinux-deploy.debug.log`.
    -   Если миграция прервется, её можно будет возобновить повторным запуском скрипта.
    -   Состояние сохраняется в `/var/run/almalinux-deploy-statuses/`.
-   Пользовательские ядра.
    -   Если установлено нестандартное ядро (например, собственной сборки), оно будет помечено как стороннее, но не удалится автоматически.
    -   В режиме Secure Boot такое ядро загрузиться не сможет, так как оно не подписано AlmaLinux.
