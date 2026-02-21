---
title: "Формат Small Form-factor Pluggable (SFP)"
author: ["Dmitry S. Kulyabov"]
date: 2023-03-19T16:38:00+03:00
lastmod: 2023-03-19T17:04:00+03:00
tags: ["sysadmin", "hard"]
categories: ["computer-science"]
draft: false
slug: "small-form-factor-pluggable"
---

Формат сменных модулей для сетевых интерфейсов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> SFP {#sfp}

-   SFP (small form-factor pluggable) заменил модули GBIC (Gigabit interface converter).
-   Размер составляет 1/2 от модуля GBIC.
-   Скорость передачи данных SFP колеблется от 100 Мбит/с до 4 Гбит/с.
-   SFP основан на протоколе SFF-8472.


## <span class="section-num">2</span> SFP+ {#sfp-plus}

-   SFP+ (small form-factor pluggable plus) --- расширенная версия SFP, поддерживающая 8 Гбит/с Fibre Channel, 10 Gigabit Ethernet и стандарт оптической транспортной сети OTU2.
-   SFP+ также предлагает прямое подключение для соединения двух портов SFP+ без дополнительных оптических модулей.
-   SFP и SFP+ модули идентичны по размеру и внешнему виду.
-   SFP+ соответствует протоколам SFF-8431 и SFF-8432.
-   В порт SFP+ можно установить SFP модуль.
-   SFP+ модуль нельзя подключить к порту SFP.


## <span class="section-num">3</span> SFP28 {#sfp28}

-   SFP28 (small form-factor pluggable 28) --- расширенная версия SFP+.
-   SFP28 и SFP+ имеют одинаковый размер, но SFP28 поддерживает 25 Гбит/с на одном канале.
-   Расположение контактов разъёмов SFP28 и SFP+ совместимо.
-   SFP28 будет работать с SFP+ модулями с пониженной скоростью.


## <span class="section-num">4</span> QSFP+ {#qsfp-plus}

-   QSFP+ есть эволюция QSFP (quad small form-factor pluggable).
-   QSFP может поддерживать 4 канала одновременно, и каждый канал может обрабатывать скорость передачи данных 1 Гбит/с, поэтому он называется Quad SFP.
-   QSFP+ поддерживает четыре канала 10 Гбит/с.
-   Эти 4 канала могут быть объединены в один канал.
-   QSFP+ может заменить 4 стандартных SFP+ модулей.


## <span class="section-num">5</span> QSFP28 {#qsfp28}

-   QSFP28 (quad small form-factor pluggable 28) обеспечивает четыре канала высокоскоростных дифференциальных сигналов со скоростями передачи данных от 25 Гбит/с до 40 Гбит/с.


## <span class="section-num">6</span> XFP {#xfp}

-   XFP (10-гигабитный Small Form Factor Pluggable) --- протоколо-независимый оптический трансивер.
-   По размерам XFP больше, чем SFP.
