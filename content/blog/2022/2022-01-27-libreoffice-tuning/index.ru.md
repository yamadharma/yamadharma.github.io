---
title: "Настройка LibreOffice"
author: ["Dmitry S. Kulyabov"]
date: 2022-01-27T14:00:00+03:00
lastmod: 2023-07-11T11:11:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "libreoffice-tuning"
---

Настройка окружения для LibreOffice.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Используемые графические тулкиты {#используемые-графические-тулкиты}

-   LibreOffice попытается автоматически определить наиболее подходящий тулкит для пользовательского интерфейса в зависимости от среды рабочего стола.
-   Чтобы принудительно использовать задать тулкит, надо использовать переменные среды:
    -   `SAL_USE_VCLPLUGIN=gen`: использовать универсальный графический тулкит;
    -   `SAL_USE_VCLPLUGIN=gtk3`: использовать GTK-3;
    -   `SAL_USE_VCLPLUGIN=kf5`: использовать QT5.


## <span class="section-num">2</span> Устранение проблем {#устранение-проблем}


### <span class="section-num">2.1</span> Зависания или аварийное завершение работы {#зависания-или-аварийное-завершение-работы}


#### <span class="section-num">2.1.1</span> Проблемы с OpenCL {#проблемы-с-opencl}

-   Можно отключить OpenCL для LibreOffice, задав переменные среды:
    ```shell
    export SAL_DISABLE_OPENCL=1
    export SAL_DISABLEGL=1
    ```
