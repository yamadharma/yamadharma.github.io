---
title: "Porteus Kiosk"
author: ["Dmitry S. Kulyabov"]
date: 2022-02-15T11:36:00+03:00
lastmod: 2024-03-23T20:49:00+03:00
tags: ["linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "porteus-kiosk"
---

_Porteus Kiosk_ --- дистрибутив Linux, реализующий режим киоска (см. [Режим киоска]({{< relref "2022-02-15-kiosk-mode" >}})).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <http://porteus-kiosk.org/>
-   Есть централизованные платные сервисы.


### <span class="section-num">1.1</span> Поддерживаемые архитектуры {#поддерживаемые-архитектуры}

-   Поддерживается только архитектура _x86_64_.


### <span class="section-num">1.2</span> Ограничения {#ограничения}

-   Заблокирован доступ к скачиванию модулей дистрибутива из России.


## <span class="section-num">2</span> Структура дистрибутива {#структура-дистрибутива}


### <span class="section-num">2.1</span> Модульная структура {#модульная-структура}

-   Часть программного обеспечения реализовано в виде модулей.
-   Можно собирать собственный вариант дистрибутива с необходимыми модулями.
-   Список модулей:
    -   Citrix Receiver.
    -   Дополнительные шрифты.
    -   Поддержка печати для локальных и сетевых принтеров.
    -   Поддержка загрузки по PXE.
    -   Службы SSH и VNC для удалённого управления и мониторинга киоска
    -   Поддержка UEFI.


## <span class="section-num">3</span> Видео {#видео}


### <span class="section-num">3.1</span> Конфигурация на сервере {#конфигурация-на-сервере}

{{< youtube 3FmzjSAVHuc >}}


### <span class="section-num">3.2</span> Установка {#установка}

{{< youtube gWEFRG4mOl4 >}}


### <span class="section-num">3.3</span> Использование после установки {#использование-после-установки}

{{< youtube TCykM713AjA >}}


### <span class="section-num">3.4</span> Удалённый доступ {#удалённый-доступ}

{{< youtube ZAA-ftK5eA0 >}}
