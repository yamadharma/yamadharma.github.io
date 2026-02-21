---
title: "Читалка. Foliate"
author: ["Dmitry S. Kulyabov"]
date: 2024-12-30T10:32:00+03:00
lastmod: 2024-12-30T10:46:00+03:00
tags: ["read"]
categories: ["self-management"]
draft: false
slug: "reader-foliate"
---

Читалка. Foliate.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://johnfactotum.github.io/foliate/>
-   Репозиторий: <https://github.com/johnfactotum/foliate/>
-   Лицензия: GPL-3.0
-   Форматы: EPUB, Mobipocket, Kindle, FB2, CBZ, PDF.


## <span class="section-num">2</span> Установка по умолчанию {#установка-по-умолчанию}

-   Можно установить _foliate_ как просмотрщик по умолчанию (см. [XDG. Приложения MIME]({{< relref "2023-04-02-xdg-mime-applications" >}})).
-   Проверим, какие ассоциации актуальны:
    ```shell
    cat /usr/share/applications/com.github.johnfactotum.Foliate.desktop | grep -i MimeType | cut -d "=" -f 2 | tr ';' '\n' | xargs -l1 xdg-mime query default
    ```
-   Установим для всех типов ассоциацию с _foliate_:
    ```shell
    cat /usr/share/applications/com.github.johnfactotum.Foliate.desktop | grep -i MimeType | cut -d "=" -f 2 | tr ';' '\n' | xargs -l1 xdg-mime default com.github.johnfactotum.Foliate.desktop
    ```


## <span class="section-num">3</span> Закладки и аннотации {#закладки-и-аннотации}

-   Запись местоположения базируется на стандартных идентификаторах канонических фрагментов EPUB (CFI) (<https://w3c.github.io/epub-specs/epub33/epubcfi/>).
-   Прогресс чтения, закладки и аннотации сохраняются в `~/.local/share/com.github.johnfactotum.Foliate`.
-   Данные для каждой книги хранятся в файле JSON, названном по идентификатору книги.
