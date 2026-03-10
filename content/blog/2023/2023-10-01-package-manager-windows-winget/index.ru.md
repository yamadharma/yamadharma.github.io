---
title: "Пакетный менеджер для Windows. WinGet"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-01T18:53:00+03:00
lastmod: 2025-07-09T21:09:00+03:00
tags: ["sysadmin", "windows"]
categories: ["computer-science"]
draft: false
slug: "package-manager-windows-winget"
---

Пакетный менеджер для Windows. WinGet.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/microsoft/winget-cli>
-   В WinGet имеется два источника пакетов: магазин Windows и собственный репозиторий, поддерживаемый Microsoft.
-   Репозиторий WinGet является просто каталогом ссылок на скачивание инсталляторов того или иного ПО из различных источников, предлагаемых их разработчиками.
-   Начиная с Windows 10 1709 выпуска он предустановлен по умолчанию.
-   Доступен в Магазине Windows под названием _App Installer_.


## <span class="section-num">2</span> Использование {#использование}


### <span class="section-num">2.1</span> Список пакетов {#список-пакетов}

-   Получение списка уже установленных приложений:
    ```shell
    winget list
    ```
-   Посмотреть список подключённых репозиториев:
    ```shell
    winget source list
    ```

    -   По умолчанию подключено два репозитория: Магазин Windows и WinGet.


### <span class="section-num">2.2</span> Поиск пакета {#поиск-пакета}

-   Найти пакет в репозитории:
    ```shell
    winget search office
    ```
-   Можно искать не по подстроке в названии, а по категории (прозвищу):
    ```shell
    winget search --moniker office
    ```
-   Можно задать репозиторий:
    ```shell
    winget search --moniker office -s winget
    ```
-   Если нужно строгое вхождение, то к строке запроса нужно добавить ключ `-e`, в этом случае будет искаться полное совпадение с учетом регистра:
    ```shell
    winget search --moniker office -s winget -e
    ```
-   Фильтры для запросов:
    -   `--name` : имя пакета;
    -   `--id` : идентификатор пакета;
    -   `--tag` : тег пакета;
    -   `--moniker` : прозвище пакета.

-   Посмотреть информацию о пакете:
    ```shell
    winget show "WPS Office"
    ```
-   Получения списка версий доступных в репозитории:
    ```shell
    winget show Kingsoft.WPSOffice --versions
    ```


### <span class="section-num">2.3</span> Установка пакета {#установка-пакета}

-   Установить пакет:
    ```shell
    winget install Kingsoft.WPSOffice
    ```
-   Приложение будет установлено с параметрами по умолчанию.
-   Ключи:
    -   `-h`, `--silent` :  полностью скрыть процесс установки;
    -   `-i`, `--interactive` : запуск установки в интерактивном режиме;
    -   `-v`, `--version` : установить пакет нужной версии;
    -   `-a`, `--architecture` : явно указать архитектуру (для скачивания), доступными являются значения: `X86` и `X64`;
    -   `--locale` : указать нужный язык.

-   Скачивание пакета в папку _Загрузки_:
    ```shell
    winget download RARLab.WinRAR
    ```
-   Скачать 32-разрядную английскую версию:
    ```shell
    winget download RARLab.WinRAR --locale en-US -a X86
    ```


### <span class="section-num">2.4</span> Обновление пакетов {#обновление-пакетов}

-   Обновить отдельный пакет:
    ```shell
    winget upgrade Microsoft.VCRedist.2015+.x64
    ```
-   Обновить все пакеты:
    ```shell
    winget upgrade --all
    ```
-   Зафиксировать текущую версию пакета и сделать его недоступным для обновления:
    ```shell
    winget pin add RARLab.WinRAR
    ```
-   Пакет может быть обновлён командой обновления пакета или добавлением к `upgrade --all` ключа `--include-pinned`.
-   Полностью заблокировать обновление пакета:
    ```shell
    winget pin add RARLab.WinRAR --blocking
    ```
-   Закрепление пакета в рамках определённой версии:
    ```shell
    winget pin add LibreOffice --version 7.4.*
    ```
-   Просмотр закреплённых пакетов:
    ```shell
    winget pin list
    ```
-   Для удаления закрепления:
    ```shell
    winget pin remove LibreOffice
    ```
-   Удалить установленную программу:
    ```shell
    winget uninstall LibreOffice
    ```


### <span class="section-num">2.5</span> Список программного обеспечения {#список-программного-обеспечения}

-   Экспортировать список установленного программного обеспечения:
    ```shell
    winget export -o C:\ADM\myapp.json
    ```

    -   Если требуется указать конкретные версии, то добавьте ключ `--include-versions`.
-   Автоматической установки программного обеспечения из списка:
    ```shell
    winget import -i C:\ADM\myapp.json
    ```
-   Ключи:
    -   `--accept-source-agreements` : подавляет запрос на принятие исходного лицензионного соглашения на использование источника пакетов;
    -   `--accept-package-agreements` : автоматическое принятие лицензионного соглашения (может потребоваться для некоторых пакетов);
    -   `--ignore-unavailable` : игнорирование ошибок в случае недоступности пакета в источнике;
    -   `--ignore-versions` : игнорировать заданные версии;
    -   `--no-upgrade` : не обновлять существующие.
-   Вариант команды импорта:
    ```shell
    winget import -i C:\ADM\myapp.json --accept-source-agreements --accept-package-agreements --ignore-unavailable --no-upgrade
    ```
