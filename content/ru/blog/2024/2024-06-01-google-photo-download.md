---
title: "Скачать фотографии с google photo"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-01T16:42:00+03:00
lastmod: 2024-06-14T12:01:00+03:00
tags: ["sysadmin", "linux"]
categories: ["computer-science"]
draft: false
slug: "google-photo-download"
---

Скачать фотографии с google photo.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Прагматика {#прагматика}

-   Необходимо было скачать фотографии с сервиса Google Photo.
-   Кроме того, желательно разместить их на другом облачном сервисе.
-   Предполагается разместить на Яндекс с тарифом из группы Яндекс Плюс.
-   На этом тарифе фотографии размещаются без учёта места под них в случае, если загружаются с мобильного телефона.
-   Предполагается следующий алгоритм:
    -   Скачать фотографии на локальный компьютер.
    -   Переименовать фотографии.
    -   Перенести фотографии на телефон.
    -   Скопировать фотографии в локальное хранилище.


## <span class="section-num">2</span> Скачивание фотографий {#скачивание-фотографий}

-   Скачивать будем с помощью rclone (см. [rclone]({{< relref "2022-10-27-rclone" >}})).
-   Запусти команду:
    ```shell
    rclone config
    ```
-   Создадим учётную запись `google-photo` для сервиса `Google Photos`.
-   Проверьте соединение:
    ```shell
    rclone ls google-photo:media
    ```
-   Создадим каталог для скачивания:
    ```shell
    mkdir -p ~/work-local/google-photo/sync
    ```
-   Скачаем фотографии с размещением по месяцам:
    ```shell
    cd ~/work-local/google-photo/sync
    rclone sync google-photo:media/by-month .
    ```
-   Если будет ошибка о превышении квоты на скорость чтения, поставьте ограничение (10 запросов в секунду):
    ```shell
    rclone sync --tpslimit 10 google-photo:media/by-month .
    ```


## <span class="section-num">3</span> Переименование фотографий {#переименование-фотографий}

-   Подготовим каталог, из которого будем переносить фотографии на телефон:
    ```shell
    mkdir -p ~/work-local/google-photo/phone
    ```
-   Сдублируем фотографии:
    ```shell
    cd ~/work-local/google-photo/sync
    find . -type f -exec ln '{}' ../phone/ \;
    ```
-   Переименуем фотографии:
    ```shell
    jhead -n%Y%m%d-%H%M%S *.jpg
    jhead -n%Y%m%d-%H%M%S *.jpeg
    jhead -n%Y%m%d-%H%M%S *.jpe
    exiftool "-filename<createdate" -globaltimeshift "-0:0:1 0:0:0" -d %Y%m%d-%H%M%S.%%e .
    ```
-   Также можно переименовать файлы на основе времени создания:
    ```shell
    for i in *.png; do mv -n "$i" "$(date -r "$i" +"%Y%m%d-%H%M%S").png"; done
    for i in *.gif; do mv -n "$i" "$(date -r "$i" +"%Y%m%d-%H%M%S").gif"; done
    for i in *.mp4; do mv -n "$i" "$(date -r "$i" +"%Y%m%d-%H%M%S").mp4"; done
    for i in *.avi; do mv -n "$i" "$(date -r "$i" +"%Y%m%d-%H%M%S").avi"; done
    ```


## <span class="section-num">4</span> Копируем фотографии на телефон {#копируем-фотографии-на-телефон}

-   Подключим телефон.
-   Посмотрим список подключённых устройств:
    ```shell
    simple-mtpfs -l
    ```
-   Подмонтируем телефон (от был под номером `1` в списке устройств):
    ```shell
    mkdir -p ~/n/mtp/
    simple-mtpfs --device 1 ~/n/mtp/
    ```

    -   Создадим каталог на телефоне для фотографий:
        ```shell
        mkdir -p ~/n/mtp/google-photo
        ```
    -   Скопируем (или перенесём) файлы на телефон:
        ```shell
        rsync -aiv ~/work-local/google-photo/phone/* ~/n/mtp/google-photo/
        ```
    -   Можно удалять файлы по мере копирования:
        ```shell
        rsync -aiv --remove-source-files ~/work-local/google-photo/phone/* ~/n/mtp/google-photo/
        ```
    -   Вы можете потом поправить время создания файлов:
        ```shell
        jhead -ft *.jpg
        ```
