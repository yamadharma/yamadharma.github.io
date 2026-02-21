---
title: "Шаблон конференции для CEUR-WS"
author: ["Dmitry S. Kulyabov"]
date: 2021-09-18T20:06:00+03:00
lastmod: 2023-10-06T17:09:00+03:00
tags: ["tex"]
categories: ["computer-science"]
draft: false
slug: "conference-template-ceur-ws"
---

Подготовка материалов конференции для публикации в репозитории конференций CEUR-WS (см. [Репозиторий конференций CEUR-WS]({{< relref "2021-09-18-ceur-ws-conference-repository" >}})).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


### <span class="section-num">1.1</span> Дополнительные пакеты {#дополнительные-пакеты}


#### <span class="section-num">1.1.1</span> ceur-make {#ceur-make}

-   Для генерации файлов используется проект _ceur-make_.
-   Репозиторий: <https://github.com/ceurws/ceur-make>
-   В исходные файлы _ceur-make_ внесены некоторые изменения.


## <span class="section-num">2</span> Структура каталогов шаблона {#структура-каталогов-шаблона}


## <span class="section-num">3</span> Порядок работы с шаблоном {#порядок-работы-с-шаблоном}


## <span class="section-num">4</span> Компиляция файлов шаблона {#компиляция-файлов-шаблона}


### <span class="section-num">4.1</span> Быстрое действие {#быстрое-действие}

-   Для получения результирующих двух архивов (самого сборника и авторских соглашений) следует выполнить:
    ```shell
    make
    ```


### <span class="section-num">4.2</span> Пояснение работы по шагам {#пояснение-работы-по-шагам}

-   Компиляция всех статей с автоматической расстановкой номеров страниц:
    ```shell
    make compile
    ```
