---
title: "Plex Media Server. Соглашения об именовании"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-27T12:16:00+03:00
lastmod: 2025-04-12T20:08:00+03:00
tags: ["appliance"]
categories: ["computer-science"]
draft: false
slug: "plex-media-server-naming-convention"
---

Plex Media Server. Соглашения об именовании.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Организация каталогов {#организация-каталогов}

-   Сканеры и агенты метаданных, используемые Plex, будут работать лучше, когда основные типы контента отделены друг от друга.
-   Рекомендуется разделить кино и телевизионный контент (сериалы) на отдельные основные каталоги.
-   Например:
    ```shell
    data/
    ├── home-video/
    ├── movie/
    ├── music/
    ├── photo/
    ├── tvshow/
    └── video/
    ```
-   Или, другой вариант (из документации):
    ```shell
    /Media
       /Movies
          movie content
       /Music
          music content
       /TV Shows
          television content
    ```


## <span class="section-num">2</span> Организация файлов фильмов {#организация-файлов-фильмов}


### <span class="section-num">2.1</span> Фильмы в своих папках {#фильмы-в-своих-папках}

-   Файлы фильмов можно размещать в отдельных папках (это рекомендуемый метод).
-   Назовите папку так же, как название фильма:

    > /Movies/MovieName (release year)/MovieName (release year).ext
-   Развёрнутый вид:
    ```shell
    /Movies
       /Avatar (2009)
          Avatar (2009).mkv
       /Batman Begins (2005)
          Batman Begins (2005).mp4
          Batman Begins (2005).en.srt
          poster.jpg

    ```
-   Если вы используете текущий агент метаданных «Plex Movie» для библиотеки, вы также можете включить идентификационный номер IMDb или TheMovieDB в фигурные скобки, чтобы облегчить сопоставление фильма.
-   Он должен соответствовать форме `{[source]-[id]}`:
    ```shell
    /Movies
       /Batman Begins (2005) {imdb-tt0372784}
          Batman Begins (2005) {imdb-tt0372784}.mp4
    ```
-   Или:
    ```shell
    /Movies
       /Batman Begins (2005) {tmdb-272}
          Batman Begins (2005) {tmdb-272}.mp4
    ```


### <span class="section-num">2.2</span> Автономные файлы фильмов {#автономные-файлы-фильмов}

-   При желании вы также можете поместить файлы фильмов рядом друг с другом в основной папке.
-   Хотя это поддерживается, всё же рекомендуется хранить фильмы в отдельных папках
-   Пример названия файла фильма:

    > MovieName (release year).ext
-   Например:
    ```shell
    /Movies
       Avatar (2009).mkv
       Batman Begins (2005).mp4
    ```


### <span class="section-num">2.3</span> Несколько редакций {#несколько-редакций}

-   Для возможности указывать разные редакции для фильма, требуется подписка Plex Pass для учетной записи администратора Plex Media Server.
-   В тех случаях, когда у вас есть конкретное издание фильма (театральный релиз, режиссерский релиз, расширенное издание и т. д.) или несколько изданий, вы можете указать информацию об этом издании, надлежащим образом назвав файл или папку.
-   Для этого вы добавляете информацию об издании в фигурных скобках в форме `{edition-[Edition Name]}`.
-   Можно указать любой текст для названия редакции (максимально 32 символа):
    ```shell
    /Movies
       Avatar (2009).mkv
       Blade Runner (1982).mp4
       Blade Runner (1982) {edition-Director's Cut}.mp4
       Blade Runner (1982) {edition-Final Cut}.mkv
       Top Gun (1986).mkv
    ```
-   При использовании отдельные папки для каждого фильма, можно добавить имя редакции к названиям папки и файла:
    ```shell
    /Movies
       /Blade Runner (1982)
          Blade Runner (1982).mp4
       /Blade Runner (1982) {edition-Director's Cut}
          Blade Runner (1982) {edition-Director's Cut}.mp4
       /Blade Runner (1982) {edition-Final Cut}
          Blade Runner (1982) {edition-Final Cut}.mkv
    ```
-   Можно использовать редакции и версии одновременно:
    ```shell
    /Media
       /Movies
          /Blade Runner (1982)
             Blade Runner (1982).mp4
          /Blade Runner (1982) {edition-Director's Cut}
             Blade Runner (1982).1080p.h264 {edition-Director's Cut}.mp4
             Blade Runner (1982).1080p.hevc {edition-Director's Cut}.mkv
             Blade Runner (1982).4k.h264 {edition-Director's Cut}.mp4
             Blade Runner (1982).4k.hevc {edition-Director's Cut}.mkv
    ```
-   Здесь представлены два разных издания _Blade Runner_, оригинальный релиз и режиссёрский релиз. Режиссёрский релиз имеет четыре различных версии: кодировки H.264 и HEVC в разрешениях 1080p и 4K.


### <span class="section-num">2.4</span> Фильмы разделены на несколько файлов {#фильмы-разделены-на-несколько-файлов}

-   Фильмы, разделённые на несколько файлов (например, pt1, pt2), могут воспроизводиться как один элемент.
-   Разделённые части должны быть помещены в отдельную папку с обычным именем для фильма:

    > /Movies/MovieName (release year)/MovieName (release year) – Split_Name.ext

-   Здесь `Split_Name` есть одно из следующего:
    -   cdX
    -   discX
    -   diskX
    -   dvdX
    -   partX
    -   ptX
-   Замените `X` с соответствующим номером (CD1, CD2 и т. д.):
    ```shell
    /Movies
       /The Dark Knight (2008)
          The Dark Knight (2008) - pt1.mp4
          The Dark Knight (2008) - pt2.mp4
    ```
