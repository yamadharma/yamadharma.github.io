---
title: "Пакетный менеджер для Windows. Chocolatey"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-18T11:23:00+03:00
lastmod: 2025-08-27T18:08:00+03:00
tags: ["windows", "sysadmin", "education"]
categories: ["computer-science"]
draft: false
slug: "package-manager-windows-chocolatey"
---

Наиболее популярным пакетным менеджером для Windows является _Chocolatey_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Ресурсы {#ресурсы}

-   Домашняя страница: <https://chocolatey.org/>
-   Репозиторий: <https://github.com/chocolatey/choco>


## <span class="section-num">2</span> Установка Chocolatey {#установка-chocolatey}

-   Порядок установки описан на странице <https://chocolatey.org/install>.
-   Установка проводится в PowerShell.
    -   PowerShell должен быть запущен с правами администратора.
    -   Проще всего запустить его комбинаций клавиш `Win+X`.
-   Команда установки находится на странице <https://chocolatey.org/install>.

    {{< youtube _1O4vKHhm3I >}}


## <span class="section-num">3</span> Дополнительные настройки {#дополнительные-настройки}

-   Для того, чтобы установка происходила без запроса подтверждения, можно сделать следующую настройку:
    ```shell
    choco feature enable -n=allowGlobalConfirmation
    ```
-   Обратно включить запрос подтверждения можно командой:
    ```shell
    choco feature disable -n=allowGlobalConfirmation
    ```


## <span class="section-num">4</span> Пакеты {#пакеты}

-   Список пакетов находится на странице <https://chocolatey.org/packages>.
-   Список пакетов:
    ```shell
    choco list
    ```


## <span class="section-num">5</span> Работа с программным обеспечением {#работа-с-программным-обеспечением}


### <span class="section-num">5.1</span> Сервисные функции {#сервисные-функции}

-   Информация по ключам командной строки:
    ```shell
    choco --help
    ```
-   Список пакетов в репозитории:
    ```shell
    choco list
    ```
-   Список установленных пакетов:
    ```shell
    choco list --local-only
    ```


### <span class="section-num">5.2</span> Установка пакета {#установка-пакета}

-   Для установки пакета нужно выполнить команду:
    ```shell
    choco install package_name
    ```
-   Чтобы установить без запроса на подтверждение, следует добавить ключ `y`:
    ```shell
    choco install package_name -y
    ```


### <span class="section-num">5.3</span> Удаление пакета {#удаление-пакета}

-   Для удаления пакета нужно выполнить команду:
    ```shell
    choco uninstall package_name
    ```


### <span class="section-num">5.4</span> Обновление пакетов {#обновление-пакетов}

-   Для обновления пакета нужно выполнить команду:
    ```shell
    choco upgrade package_name
    ```
-   Для обновления всех установленных пакетов нужно выполнить команду:
    ```shell
    choco upgrade all -y
    ```


### <span class="section-num">5.5</span> Автоматическое обновление пакетов {#автоматическое-обновление-пакетов}

-   Для автоматического обновления пакетов используется пакет `choco-upgrade-all-at`:
    ```shell
    choco install choco-upgrade-all-at
    ```
-   Обновление можно выполнить командой:
    ```shell
    choco-upgrade-all
    ```
-   Чтобы задать время обновления, нужно устанавливать с определёнными параметрами:
    -   если не указывать никаких параметров, `choco-upgrade-all-at` по умолчанию будет запускаться ежедневно в 2 часа ночи и прерываться в 4 часа ночи;
    -   запуск `choco upgrade all -y` ежедневно (по умолчанию) в 23:00 и прерывание в 1:00 ( по умолчанию `ABORTTIME` равно +2 часа):
        ```shell
        choco install choco-upgrade-all-at --params "'/TIME:23:00'"
        ```
    -   запуск `choco upgrade all -y` ежедневно в 4:00 и прерывание в 8:00:
        ```shell
        choco install choco-upgrade-all-at --params "'/DAILY:yes /TIME:04:00 /ABORTTIME:08:00'"
        ```
    -   запуск `choco upgrade all -y` каждое воскресенье в 1:00 и прерывание в 3:00:
        ```shell
        choco install choco-upgrade-all-at --params "'/WEEKLY:yes /DAY:SUN /TIME:01:00'"
        ```
-   Параметры можно отредактировать, запустив команду:
    ```shell
    choco-upgrade-all -EditConfig
    ```
