---
title: "Закачка с youtube"
author: ["Dmitry S. Kulyabov"]
date: 2022-03-09T17:38:00+03:00
lastmod: 2024-01-14T17:35:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "download-youtube"
---

Возникла задача скопировать видео с Youtube. Основная часть содержимого --- это мои видеозаписи для преподавания.
Для этой задачи я использовал `yt-dlp`.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/yt-dlp/yt-dlp>
-   Является продвинутым форком `youtube-dl`.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Linux {#linux}

-   Gentoo
    -   Установка `yt-dlp`:
        ```shell
        emerge net-misc/yt-dlp
        ```
    -   Установка в режиме совместимости с `youtube-dl`:
        ```shell
        USE=yt-dlp emerge net-misc/youtube-dl
        ```


### <span class="section-num">2.2</span> Windows {#windows}

-   C использованием [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})
    ```shell
    choco install yt-dlp
    ```


## <span class="section-num">3</span> Примеры использования {#примеры-использования}


### <span class="section-num">3.1</span> Скачивание видео с Youtube {#скачивание-видео-с-youtube}

-   Просто указывается линк на скачиваемое видео:
    ```shell
    yt-dlp <url>
    ```
-   Загрузите лучшее видео с лучшим кодеком, но не лучше, чем `h264`; разрешение не выше, чем 1080 строк:
    ```shell
    yt-dlp -S "codec:h264,height:1080" <url>
    ```


### <span class="section-num">3.2</span> Скачать только аудио-дорожку {#скачать-только-аудио-дорожку}

-   Опция `-x` используется для загрузки только аудио (требуется _FFmpeg_):
    ```shell
    youtube-dl -x -f bestaudio <url>
    ```


### <span class="section-num">3.3</span> Скачивание своего общедоступного видео с Youtube {#скачивание-своего-общедоступного-видео-с-youtube}


#### <span class="section-num">3.3.1</span> Постановка задачи {#постановка-задачи}

-   Видео добавлены в плейлисты по темам.
-   Есть ссылки на чужие видео.
-   Скачать нужно только своё общедоступное видео.
-   Следует сохранить порядок расположения видео в плейлистах.


#### <span class="section-num">3.3.2</span> Решение {#решение}

-   `%(playlist)s` : будем сортировать виде по плейлистам.
-   `%(playlist_index)s` : будем сохранять номер видео в плейлисте.
-   `%(title)s.%(ext)s` : будем сохранять видео с его названием.
-   `--write-comments` : будем сохранять всю дополнительную информацию в отдельный файл формата `json`.
-   `--match-filter "uploader = 'Dmitry Kulyabov'"` : будем скачивать только те видео, который загрузили мы сами.

<!--list-separator-->

1.  Итоговый скрипт

    -   Итоговый скрипт будет иметь следующий вид:
        ```shell
        yt-dlp -o "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "https://www.youtube.com/user/<youtube user name>/playlists" --write-comments --match-filter "uploader = 'Dmitry Kulyabov'"
        ```


## <span class="section-num">4</span> Конфигурационный файл {#конфигурационный-файл}

-   Конфигурационный файл служит для заданий опций по умолчанию.
-   Конфигурационный файл:
    ```shell
    ~/.config/yt-dlp/config
    ```

-   Пример содержания конфигурационого файла:
    ```conf-unix
    ## Ignore errors
    --ignore-errors

    ## Save in ~/Videos
    -o ~/Videos/%(title)s.%(ext)s

    ## Prefer 1080p or lower resolutions, FPS < 60 Hz
    -f bestvideo[ext=mp4][height<1200][fps<60]+bestaudio[ext=m4a]/bestvideo[height<1200][fps<60]+bestaudio/best[height<1200][fps<60]/best
    ```
