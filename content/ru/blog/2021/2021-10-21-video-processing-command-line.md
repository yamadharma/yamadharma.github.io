---
title: "Обработка видео. Командная строка"
author: ["Dmitry S. Kulyabov"]
date: 2021-10-21T17:26:00+03:00
lastmod: 2025-07-09T18:15:00+03:00
categories: ["computer-science"]
draft: false
slug: "video-processing-command-line"
---

Обработка видео. Командная строка

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Инструментарий {#инструментарий}


### <span class="section-num">1.1</span> ffmpeg {#ffmpeg}

-   Комплексное решение по обработке видео.
-   Установка
    -   Linux
        -   Gentoo
            ```shell
            emerge media-video/ffmpeg
            ```


### <span class="section-num">1.2</span> mkvtoolnix {#mkvtoolnix}

-   Инструменты для создания, изменения и проверки файлов формата Matroska.
-   Установка
    -   Linux
        -   Gentoo
            ```shell
            emerge media-video/mkvtoolnix
            ```


## <span class="section-num">2</span> Задачи {#задачи}


### <span class="section-num">2.1</span> Перекодирование звуковой дорожки в видеофайле {#перекодирование-звуковой-дорожки-в-видеофайле}

-   Есть видеофайлы (в частности, в формате `mp4`).
-   При проигрывании на телевизоре нет звука.
-   Причина: звуковая дорожка закодирована с частотой дискретизации 48 кГц, а телевизор воспринимает только с частотой дискретизации 44,1 кГц.
-   В видеофайле одна видео-дорожка и одна аудио-дорожка.
-   Для перекодирования сделан командный файл:
    ```shell
    #!/bin/bash
    # recode-48to44.1

    OUTDIR_AUDIO=recoded-audio
    OUTDIR=recoded
    mkdir -p ${OUTDIR}
    mkdir -p ${OUTDIR_AUDIO}

    for i in *.mp4
    do
        NAME=`basename "${i}" .mp4`
        ffmpeg -i "${i}" -vn -ar 44100 -c:a libfdk_aac -b:a 192k "${OUTDIR_AUDIO}"/"${NAME}".aac
        mkvmerge --default-language rus -o "${OUTDIR}"/"${NAME}".mkv --language 1:rus "${i}" --default-track 0:1 "${OUTDIR_AUDIO}"/"${NAME}".aac
    done
    ```
-   Сначала мы с помощью `ffmeg` перекодируем аудио-дорожку:
    -   `-vn` : игнорирование видео-дорожек;
    -   `-ar 44100` : частота дискретизации 44,1 кГц;
    -   `-c:a libfdk_aac` : задаём кодек для формата AAC;
    -   `-b:a 192k` : задаём битрейт.
-   С помощью `mkvmerge` сливаем файлы в новый (формата `mkv`):
    -   `--default-language rus` : задаём язык по умолчанию для дорожек;
    -   `--language 1:rus` : меняем язык аудио-дорожки в исходном файле;
    -   `--default-track 0:1` : ставим новую звуковую дорожку дорожкой по умолчанию.


### <span class="section-num">2.2</span> Объединить несколько файлов `mp4` {#объединить-несколько-файлов-mp4}

-   Дано: набор файлов вида `video1.mp4`, расположенных в алфавитном порядке.
-   Создадим файл `input.txt` с названиями видео-файлов:
    ```shell
    for i in $(ls *.mp4 | sort)
    do
            echo file \'$(readlink -f "${i}")\' >>input.txt
    done
    ```
-   Соединим видеофайлы:
    ```shell
    ffmpeg -f concat -safe 0 -i input.txt -c copy output.mp4
    ```


### <span class="section-num">2.3</span> Объединить несколько файлов `webm` {#объединить-несколько-файлов-webm}

-   Можно объединить несколько файлов:
    ```shell
    mkvmerge -o output.webm -w file1.webm + file2.webm
    ```


### <span class="section-num">2.4</span> Объединить несколько файлов `mkv` {#объединить-несколько-файлов-mkv}

-   Можно объединить несколько файлов:
    ```shell
    mkvmerge --language "1:ru" --title "Title" --generate-chapters when-appending -o output.mkv file1.mkv + file2.mkv
    ```
-   Кроме объединения, мы задали язык звуковой дорожки (русский) и каждый файл обозначили как главу.


### <span class="section-num">2.5</span> Замена аудио-дорожки в видеофайле {#замена-аудио-дорожки-в-видеофайле}

-   Заменит аудио-дорожку в видеофайле:
    ```shell
    ffmpeg -i video.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -shortest output.mp4
    ```

    -   `-map` : выбрать поток;
    -   `-c:v copy` : потоковое копирование видео (не происходит повторного кодирования видео);
        -   если формат входного аудио совместим с выходным, можно изменить `-c:v copy` на `-c copy` для потокового копирования видео и аудио;
    -   `-shortest` : сделать выходной файл такой же продолжительности, как и самый короткий входной.


### <span class="section-num">2.6</span> Добавить аудио к видео {#добавить-аудио-к-видео}

-   Добавим дополнительную аудио-дорожку к видео:
    ```shell
    ffmpeg -i video.mkv -i audio.mp3 -map 0 -map 1:a -c:v copy -shortest output.mkv
    ```

    -   `-map` : выбрать поток;
    -   `-c:v copy` : потоковое копирование видео (не происходит повторного кодирования видео);
        -   если формат входного аудио совместим с выходным, можно изменить `-c:v copy` на `-c copy` для потокового копирования видео и аудио;
    -   `-shortest` : сделать выходной файл такой же продолжительности, как и самый короткий входной.


### <span class="section-num">2.7</span> Добавить беззвучную звуковую дорожку {#добавить-беззвучную-звуковую-дорожку}

-   Можно использовать фильтр `anullsrc` для создания беззвучного аудиопотока.
-   Фильтр позволяет выбрать желаемое расположение каналов (моно, стерео, 5.1 и т. д.) и частоту дискретизации.
    ```shell
    ffmpeg -i video.mp4 -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -c:v copy -shortest output.mp4
    ```


### <span class="section-num">2.8</span> Смикшировать два аудиопотока в один {#смикшировать-два-аудиопотока-в-один}

-   Используем видео из файла video.mkv.
-   Смешаем аудио из файлов video.mkv и audio.m4a с помощью фильтра `amerge`:
    ```shell
    ffmpeg -i video.mkv -i audio.m4a -filter_complex "[0:a][1:a]amerge=inputs=2[a]" -map 0:v -map "[a]" -c:v copy -ac 2 -shortest output.mkv
    ```
