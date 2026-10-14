---
title: "Gentoo. Portage. Слоты"
author: ["Dmitry S. Kulyabov"]
date: 2026-09-27T13:09:00+03:00
lastmod: 2026-09-27T13:22:00+03:00
tags: ["linux", "gentoo"]
categories: ["computer-science"]
draft: false
slug: "gentoo-portage-slot"
---

Gentoo. Portage. Слоты.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Несколько слотов в системе одновременно {#несколько-слотов-в-системе-одновременно}

-   Чтобы пакеты с разными слотами не удалялись при `emerge --depclean`, нужно явно указать их в world-файле.
-   `depclean` удаляет всё, что не входит в `@world` и не является зависимостью других установленных пакетов.
-   `depclean` не удаляет слот, если он является зависимостью другого установленного пакета.


### <span class="section-num">1.1</span> `emerge --noreplace` {#emerge-noreplace}

-   Чтобы зафиксировать слот пакета, следует добавить нужный слот в `@world` командой `emerge --noreplace`.
-   Она не переустанавливает пакет, а только фиксирует его в world-файле:
    ```shell
    emerge --noreplace <category>/<package>:<slot>
    ```
-   После этого можно проверить, что слот больше не попадает в список на удаление:
    ```shell
    emerge --depclean --pretend
    ```

<!--listend-->

-   Пример: сохранить Python 3.9:
    ```shell
    emerge --noreplace dev-lang/python:3.9
    ```


### <span class="section-num">1.2</span> `emerge --depclean --exclude` {#emerge-depclean-exclude}

-   C помощью `--exclude` можно исключить пакет из `depclean` целиком, но глобально, все слоты сразу:
    ```shell
    emerge --depclean --exclude=sys-kernel/gentoo-sources
    ```


### <span class="section-num">1.3</span> Удалить слот из world-файла {#удалить-слот-из-world-файла}

-   Сделать можно командой `emerge --deselect`:
    ```shell
    emerge --deselect <category>/<package>:<slot>
    ```

-   Пример:
    ```shell
    emerge --deselect dev-lang/python:3.9
    ```
