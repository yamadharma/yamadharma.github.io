---
title: "Система Quarto"
author: ["Dmitry S. Kulyabov"]
date: 2025-03-22T17:37:00+03:00
lastmod: 2026-02-01T18:43:00+03:00
tags: ["science-writing", "markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-system"
---

Система Quarto.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://quarto.org/>
-   Репозиторий: <https://github.com/quarto-dev/quarto-cli>
-   Quarto — это современная система для создания научной, технической и прочей документации.
-   Входной язык: Markdown.
-   Выходные форматы: html, pdf, epub, docx, презентации в формате reveal.js.
-   Интеграция с языками программирования: R, Python, Julia, Observable JS.
    -   Интеграция как в babel (см. [Emacs. Org Babel]({{< relref "2022-10-15-emacs-org-babel" >}})) или julyter.
    -   Позволяет включать в документы интерактивные элементы, такие как виджеты и динамические визуализации.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Windows {#windows}

-   Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):
    ```shell
    choco install quarto
    ```


### <span class="section-num">2.2</span> Linux {#linux}


#### <span class="section-num">2.2.1</span> Linux в общем {#linux-в-общем}

-   Установка с помощью скрипта:
    ```shell
    #!/bin/bash

    ## Система
    TARGET=/opt
    TARGET_BIN=/usr/local/bin
    ## Домашний каталог
    # TARGET=~/opt
    # TARGET_BIN=~/.local/bin


    ## Получить тег
    TAG=`basename $(curl -sL -o /dev/null -w %{url_effective} https://github.com/quarto-dev/quarto-cli/releases/latest)`
    TAG=${TAG/v/}

    ## Скачать
    cd /tmp
    wget https://github.com/quarto-dev/quarto-cli/releases/download/v${TAG}/quarto-${TAG}-linux-amd64.tar.gz

    ## Распаковать
    mkdir -p ${TARGET}
    tar -C ${TARGET} -xvzf /tmp/quarto-${TAG}-linux-amd64.tar.gz
    mv ${TARGET}/quarto-${TAG} ${TARGET}/quarto

    ## Симлинк на исполняемый файл
    mkdir -p ${TARGET_BIN}
    ln -s ${TARGET}/quarto/bin/quarto ${TARGET_BIN}/quarto
    ```


#### <span class="section-num">2.2.2</span> Gentoo {#gentoo}

-   Gentoo, репозиторий karma (см. [Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
    ```shell
    emerge quarto
    ```


#### <span class="section-num">2.2.3</span> Arch {#arch}

-   Arch linux:
    ```shell
    pacman -S quarto-cli-bin
    ```
-   Manjaro linux:
    ```shell
    pamac install quarto-cli-bin
    ```


#### <span class="section-num">2.2.4</span> Fedora {#fedora}

-   Установка из CORP:
    ```shell
    sudo dnf -y copr enable iucar/rstudio
    sudo dnf -y install quarto
    sudo dnf -y install libxcrypt-compat
    ```


## <span class="section-num">3</span> Установка модулей {#установка-модулей}

-   Установка tinytex:
    ```shell
    quarto install tinytex
    ```


## <span class="section-num">4</span> Общий алгоритм работы {#общий-алгоритм-работы}

```mermaid
flowchart LR
  A{Выбираем тип проекта} --> B(Редактируем YAML)
  B --> C(Пишем текст и код)
  B --> D(Добавляем изображения)
  C --> E(Настраиваем отображение)
  D --> E
  E <--> B
  E --> F[Публикация]

  classDef optional stroke-dasharray:10;
  class D optional
  class E optional
```


## <span class="section-num">5</span> Использование {#использование}

-   [Quarto. Язык markdown]({{< relref "2025-03-23--quarto-markdown" >}})
-   [Quarto. Оформление метаданных]({{< relref "2025-03-23--quarto-metadata-formatting" >}})
-   [Quarto. Цитирование]({{< relref "2025-03-23--quarto-citations" >}})
-   [Quarto. Перекрёстные ссылки]({{< relref "2025-03-23--quarto-cross-references" >}})
-   [Quarto. Структура для книги]({{< relref "2025-03-27--quarto-book-structure" >}})
-   [Quarto. Формат pdf]({{< relref "2025-03-27--quarto-pdf-format" >}})
-   [Quarto. Листинги]({{< relref "2025-05-13--quarto-code-listing" >}})
-   [Quarto. Таблицы]({{< relref "2025-05-17--quarto-table" >}})
-   [Quarto. Плагины]({{< relref "2025-09-03--quarto-plugins" >}})
-   [Quarto. Профили]({{< relref "2025-10-08--quarto-profiles" >}})
-   [Quarto. Подключение файлов]({{< relref "2025-11-19--quarto-include-file" >}})
-   [Quarto. Использование переменных]({{< relref "2026-01-31--quarto-variables" >}})
-   [Quarto. Библиография]({{< relref "2026-02-01--quarto-bibliography" >}})
-   [Quarto. subfigures]({{< relref "2026-02-01--quarto-subfigures" >}})


## <span class="section-num">6</span> Ресурсы {#ресурсы}


### <span class="section-num">6.1</span> Шаблоны {#шаблоны}

-   Набор шаблонов для дипломов: <https://github.com/Jupyter4Science/awesome-quarto-thesis>


### <span class="section-num">6.2</span> Рекомендации {#рекомендации}

-   Quarto for Scientists: <https://qmd4sci.njtierney.com>
