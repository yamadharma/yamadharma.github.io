---
title: "Установка TeXlive"
author: ["Dmitry S. Kulyabov"]
date: 2021-04-23T18:09:00+03:00
lastmod: 2025-08-15T15:43:00+03:00
tags: ["latex", "tex"]
categories: ["computer-science"]
draft: false
slug: "install-texlive"
---

Установка дистрибутива _TeXlive_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   TeX Live --- наиболее полный дистрибутив LaTeX, поддерживаемый TeX-сообществом.
-   Поддерживает большое количество операционных систем.
-   Разрабатывается начиная с 1996 года.
-   Был основан на дистрибутиве teTeX.
-   MacTeX --- вариант для MacOS.
-   Основная страница: <https://www.tug.org/texlive/>.
-   TeX Live --- это дистрибутив с непрерывным обновлением в рамках ежегодной версии дистрибутива.


## <span class="section-num">2</span> Установка из пакетов дистрибутива {#установка-из-пакетов-дистрибутива}

-   Ubuntu:
    ```shell
    apt install texlive-full
    ```


## <span class="section-num">3</span> Сетевая установка на один компьютер {#сетевая-установка-на-один-компьютер}


### <span class="section-num">3.1</span> Установка с помощью дистрибутивных скриптов {#установка-с-помощью-дистрибутивных-скриптов}

-   Ссылки на сайте даны на зеркала. Зеркало выбирается автоматически.
    -   Скачивается инсталлятор:
        -   Unix: <https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz>
            ```shell
            cd /tmp/
            wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
            ```
        -   Windows: <https://mirror.ctan.org/systems/texlive/tlnet/install-tl-windows.exe>
    -   Для Windows: запускаете исполняемый файл и устанавливаете.
    -   Для Linux
        -   Распаковываете скачанный файл:
            ```shell
            tar xzvf install-tl-unx.tar.gz
            ```
        -   Заходите в распакованный каталог и запускаете установщик:
            ```shell
            cd install-tl-[0-9]*
            sudo ./install-tl
            ```

            -   Рекомендуется создать ссылки на исполняемые файлы в каталоге `/usr/local/bin`. Для этого в консольном варианте утилиты выберите опцию `O`, а затем `L`. Для возврата в предыдущее меню используйте `R`.


### <span class="section-num">3.2</span> Установка с помощью менеджера пакетов {#установка-с-помощью-менеджера-пакетов}

-   Windows. Используйте пакетный менеджер Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})).
    ```shell
    choco install texlive
    ```


## <span class="section-num">4</span> Поддержка сетевой установки на нескольких компьютерах {#поддержка-сетевой-установки-на-нескольких-компьютерах}


### <span class="section-num">4.1</span> Файл-сервер {#файл-сервер}

-   На файл-сервере хранится копия архива TeX Live.
-   Храним её в каталоге `/com/lib/portage/extras/texlive` (естественно, можно выбрать любой).
-   Данный каталог расшариваем по NFS (например).
-   Сделаем скрипт для ежедневного скачивания:
    ```shell
    #!/bin/bash
    # /etc/cron.daily/texlive-rsync-tree

    RSYNC_MIRROR=rsync://mirrors.mi.ras.ru/CTAN/

    mkdir -p /com/lib/portage/extras/texlive
    rsync -rltpD -v -HS --delete ${RSYNC_MIRROR}/systems/texlive/tlnet/ /com/lib/portage/extras/texlive
    ```


### <span class="section-num">4.2</span> Клиенты {#клиенты}


#### <span class="section-num">4.2.1</span> Установка {#установка}

-   На клиентах вначале устанавливаем вручную. Для этого на клиенте запускаем:
    ```shell
    /com/lib/portage/extras/texlive/install-tl --repository=/com/lib/portage/extras/texlive
    ```


### <span class="section-num">4.3</span> Обновление {#обновление}

-   Для обновления используем на клиенте скрипт:
    ```shell
    #!/bin/bash

    if [[ -d /com/lib/portage/extras/texlive ]]
    then
            tlmgr update --repository=/com/lib/portage/extras/texlive --self
            tlmgr update --repository=/com/lib/portage/extras/texlive --all
    else
            tlmgr update --self
            tlmgr update --all
    fi
    tlmgr path add
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      /etc/cron.weekly/texlive-update
    </div>


## <span class="section-num">5</span> Обновление до следующей версии TeXlive {#обновление-до-следующей-версии-texlive}

-   Рекомендуется установить новую версию TeXlive отдельно.
-   Но можно сделать ручное обновление, используя уже существующую установку.
-   Будем считать, что у нас архитектура `x86_64-linux`.
-   Если вы установили символические ссылки в системные каталоги (через опцию установщика или `tlmgr path add`), удалите их:
    ```shell
    tlmgr path remove
    ```
-   Перенесите весь каталог TeXlive так, чтобы он соответствовал новой версии, например:
    ```shell
    mv /usr/local/texlive/2024/ /usr/local/texlive/2025
    ```
-   Удалите бекапы пакетов:
    ```shell
    rm /usr/local/texlive/2025/tlpkg/backups/*
    ```
-   Создайте ссылки на исполняемые файлы:
    ```shell
    /usr/local/texlive/2025/bin/x86_64-linux/tlmgr path add
    ```
-   Загрузите последнюю версию скрипта `update-tlmgr-latest.sh`:
    ```shell
    wget https://mirror.ctan.org/systems/texlive/tlnet/update-tlmgr-latest.sh -O /tmp/update-tlmgr-latest.sh
    ```
-   Запустите скрипт:
    ```shell
    sh /tmp/update-tlmgr-latest.sh -- upgrade
    ```
-   Если вы не хотите использовать репозиторий по умолчанию для загрузки новых файлов, то замените его:
    ```shell
    tlmgr option repository <reponame>
    ```
-   Обновите менеджер пакетов TeXlive:
    ```shell
    tlmgr update --self
    ```
-   Обновите пакеты TeXlive:
    ```shell
    tlmgr update --all
    ```
-   Установите символические ссылки на исполняемые файлы в системные каталоги (`/usr/local/bin`):
    ```shell
    tlmgr path add
    ```
-   Можно пересоздать кэш _lualatex_ под пользователем:
    ```shell
    mv ~/.texlive2024 ~/.texlive2025
    luaotfload-tool -fu
    ```

    -   Если этого не сделать, то кэш будет пересоздан при первом запуске `lualatex`.
