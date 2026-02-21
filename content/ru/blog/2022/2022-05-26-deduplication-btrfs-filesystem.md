---
title: "Дедупликация файловой системы btrfs"
author: ["Dmitry S. Kulyabov"]
date: 2022-05-26T14:29:00+03:00
lastmod: 2023-07-13T12:09:00+03:00
tags: ["sysadmin", "btrfs"]
categories: ["computer-science"]
draft: false
slug: "deduplication-btrfs-filesystem"
---

Дедупликация файловой системы btrfs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   При дедупликации идентифицируются блоки данных, которые имеют общие последовательности.
-   Они объединяются в один экстент с семантикой копирования при записи.


## <span class="section-num">2</span> Реализация {#реализация}


### <span class="section-num">2.1</span> duperemove {#duperemove}


### <span class="section-num">2.2</span> bees {#bees}

-   [Дедупликация btrfs. Bees]({{< relref "2022-05-28-deduplication-btrfs-filesystem-bees" >}})
-   Уровень дедупликации: блочный.
-   Работает как демон.
-   Использую для дедупликации файловой системы.


### <span class="section-num">2.3</span> bedup {#bedup}


### <span class="section-num">2.4</span> btrfs-dedup {#btrfs-dedup}


## <span class="section-num">3</span> Дедупликация на уровне файлов {#дедупликация-на-уровне-файлов}

-   Некоторые утилиты для дедупликации на уровне файлов поддерживают файловую систему _btrfs_.
-   [Дедупликация файлов в Linux]({{< relref "2022-05-26-file-deduplication-linux" >}})
