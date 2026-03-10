---
title: "Шрифты в Linux"
author: ["Dmitry S. Kulyabov"]
date: 2021-10-27T11:36:00+03:00
lastmod: 2023-07-18T20:08:00+03:00
tags: ["linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "linux-fonts"
---

Работа со шрифтами в Linux.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Установка шрифтов Microsoft {#установка-шрифтов-microsoft}


### <span class="section-num">1.1</span> Основные шрифты Microsoft {#основные-шрифты-microsoft}


#### <span class="section-num">1.1.1</span> Ubuntu {#ubuntu}

-   Шрифты Microsoft не идут под свободной лицензией.
-   Для работы с ними нужно установить соответствующий пакет:
    ```shell
    apt-get install ttf-mscorefonts-installer
    ```
-   Вас попросят принять лицензию (EULA), после этого будут скачаны соответствующие шрифты (в виде архивов), распакованы и установлены в системе.
-   Скачиваются они с проекта _Corefonts_ (<http://corefonts.sourceforge.net/>).
-   Обычно устанавливаются шрифты в каталог `/usr/share/fonts/truetype/msttcorefonts`.


## <span class="section-num">2</span> Шрифты для программирования {#шрифты-для-программирования}

-   [Моноширинные шрифты]({{< relref "2021-05-21-monospace-fonts" >}})
