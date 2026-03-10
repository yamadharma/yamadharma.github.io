---
title: "Сайт The Movie Database"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-14T18:56:00+03:00
lastmod: 2024-11-14T20:04:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "the-movie-database"
---

Сайт The Movie Database.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.themoviedb.org/>
-   Предоставляет обложки, описание для фильмов и сериалов.
-   Используют медиаплееры: Plex, Kodi.
-   Они загружают оттуда обложки.
-   В 2022 году этот ресурс заблокировал доступ из РФ.


## <span class="section-num">2</span> Блокировка доступа {#блокировка-доступа}

-   Блокировка осуществляется по GeoDNS.
-   Отдаются разные ответы для разных регионов.
-   Для российских адресов они отдают IP-адрес 127.0.0.1 (localhost):
    ```shell
    dig www.themoviedb.org
    ;; ANSWER SECTION:
    www.themoviedb.org.	300	IN	A	127.0.0.1
    ```


### <span class="section-num">2.1</span> Решение этой проблемы {#решение-этой-проблемы}


#### <span class="section-num">2.1.1</span> Добавить IP-адреса themoviedb.org в файл `/etc/hosts` {#добавить-ip-адреса-themoviedb-dot-org-в-файл-etc-hosts}

-   Нужно настроить адреса для следующих хостов:
    -   themoviedb.org
    -   tmdb.org
    -   tmdb-image-prod.b-cdn.net
-   Можно получить через внешний DNS-сервер.
    ```bash
    dig @9.9.9.9 themoviedb.org
    dig @9.9.9.9 tmdb.org
    dig @9.9.9.9 tmdb-image-prod.b-cdn.net
    ```


#### <span class="section-num">2.1.2</span> Настроить 9.9.9.9 как DNS-сервер на компьютере с медиаплеером {#настроить-9-dot-9-dot-9-dot-9-как-dns-сервер-на-компьютере-с-медиаплеером}
