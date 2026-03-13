---
title: "Moodle. Администрирование. Moosh"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-21T15:33:00+03:00
lastmod: 2025-08-21T15:50:00+03:00
tags: ["sysadmin", "education"]
categories: ["computer-science"]
draft: false
slug: "moodle-administration-moosh"
---

Moodle. Администрирование. Moosh.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://moosh-online.com/>
-   Репозиторий: <https://github.com/tmuras/moosh>
-   Moosh расшифровывается как MOODLE SHell.
-   Инструмент Командной строки, позволяющий выполнять большинство распространённых задач Moodle.
-   Создан по мотивам Drush --- аналогичного инструмента для Drupal.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Установка из git {#установка-из-git}

-   Установите compose:
    -   RHEL:
        ```shell
        dnf -y install composer
        ```
-   Скачайте репозиторий:
    ```shell
    cd /usr/local/src/
    git clone https://github.com/tmuras/moosh.git
    ```
-   Соберите пакет:
    ```shell
    cd /usr/local/src/mosh
    composer install
    ```
-   Сделайте ссылку на исполняемый файл:
    ```shell
    sudo ln -s /usr/local/src/mosh/moosh.php /usr/local/bin/moosh
    ```
