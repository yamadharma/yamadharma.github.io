---
title: "Скачать музыку с VK"
author: ["Dmitry S. Kulyabov"]
date: 2026-09-16T19:54:00+03:00
lastmod: 2026-09-16T20:49:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "download-misic-vk"
---

Скачать музыку с VK.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Скачать через yt-dlp {#скачать-через-yt-dlp}

-   [Закачка с youtube]({{< relref "2022-03-09-download-youtube" >}})
-   Процесс состоит из двух этапов: получение прямой ссылки на аудиофайл и его скачивание.


### <span class="section-num">1.1</span> Получение прямой ссылки на трек {#получение-прямой-ссылки-на-трек}

1.  Откройте VK в броузере и начните воспроизведение нужной песни.
2.  Нажмите `F12`, чтобы открыть инструменты разработчика, и перейдите на вкладку _Сеть_ (Network).
3.  В фильтре введите `m3u8` или `audio`.
4.  Перезагрузите страницу или запустите трек заново.
5.  Найдите запрос, который ведёт на `vkuseraudio.net`. Скопируйте его полный URL. Обычно он выглядит так: `https://cs1-41v4.vkuseraudio.net/s/v1/ac/.../index.m3u8`.


### <span class="section-num">1.2</span> Скачивание через yt-dlp {#скачивание-через-yt-dlp}

-   Откройте терминал и выполните команду, вставив скопированную ссылку:
    ```shell
    yt-dlp -x --audio-format mp3 <url>
    ```

    -   `-x` или `--extract-audio`: извлекает аудиодорожку.
    -   `--audio-format mp3`: конвертирует файл в формат MP3 (можно указать `m4a`, `opus` и др.).

-   VK часто использует HLS-потоки (`.m3u8`).
-   Если скачивание обрывается или файл получается неполным, добавьте флаг `--downloader ffmpeg`:

<!--listend-->

```shell
yt-dlp --downloader ffmpeg -x --audio-format mp3 <url>
```

-   Можно скачивать списком. Создайте текстовый файл `urls.txt`, где каждая строка --- прямая ссылка на трек:
    ```shell
    yt-dlp -x --audio-format mp3 --batch-file urls.txt
    ```


### <span class="section-num">1.3</span> Использование cookies {#использование-cookies}

-   Для доступа к некоторым трекам (ошибка «Sign up to watch...») может потребоваться авторизация.
-   `yt-dlp` поддерживает файлы cookies.
    -   Экспортируйте cookies для `vk.com` из вашего браузера с помощью расширения.
    -   Сохраните файл, например, как `cookies_vk.txt`.
    -   Добавьте флаг `--cookies` в команду:

<!--listend-->

```shell
yt-dlp --cookies cookies_vk.txt -x --audio-format mp3 <url>
```


## <span class="section-num">2</span> Программы для скачивания {#программы-для-скачивания}


### <span class="section-num">2.1</span> yandex-music-downloader {#yandex-music-downloader}

-   Репозиторий: <https://github.com/vladimir120307-droid/yandex-music-downloader>
-   Для скачивания  с Яндекс.Музыки.
-   Автор обещает, что можно скачать с VK тоже.
-   Но у меня не получилось.
