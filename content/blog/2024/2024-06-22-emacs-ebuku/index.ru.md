---
title: "Emacs. Пакет ebuku"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-22T21:22:00+03:00
lastmod: 2024-06-22T21:37:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-ebuku"
---

Emacs. Пакет ebuku

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Интерфейс к менеджеру закладок buku (см. [Менеджер закладок buku]({{< relref "2024-06-22-buku-bookmark-manager" >}})).
-   Репозиторий: <https://github.com/flexibeast/ebuku>


## <span class="section-num">2</span> Использование {#использование}

-   Создайте буфер Ebuku с помощью команды `M-x ebuku`.


## <span class="section-num">3</span> Привязки клавиш {#привязки-клавиш}

-   `s` : поиск закладки (`ebuku-search`);
-   `r` : показать недавно добавленные закладки (`ebuku-search-on-recent`);
-   `*` : показать все закладки (`ebuku-show-all`);
-   `-` : переключить лимит результатов (`ebuku-toggle-results-limit`);
-   `g` : обновить результаты поиска на основе последнего поиска (`ebuku-refresh`);
-   `RET` : открыть закладку в браузере (`ebuku-open-url`);
-   `n` : переместить курсор на следующий URL-адрес закладки (`ebuku-next-bookmark`);
-   `p` : переместить курсор на URL-адрес предыдущей закладки (`ebuku-previous-bookmark`);
-   `a` : добавить новую закладку (`ebuku-add-bookmark`);
-   `d` : удалить закладку (`ebuku-delete-bookmark`);
    -   если курсор на закладке, будет предложено удалить эту закладку;  в противном случае будет запрошен индекс закладки, которую нужно удалить;
-   `e` : редактировать закладку (`ebuku-edit-bookmark`);
    -   если курсор находится на закладка, то будет отредактирована эта закладка;  в противном случае будет запрошен индекс закладки для редактирования;
-   `C` : скопировать URL закладки (`ebuku-copy-url`);
-   `T` : скопировать заголовок закладки  (`ebuku-copy-title`);
-   `I` : скопировать индекс закладки в точку списка уничтожений (`ebuku-copy-index`);
-   `q` : выйти из ebuku.
