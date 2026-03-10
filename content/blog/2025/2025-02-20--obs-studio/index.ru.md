---
title: "OBS Studio"
author: ["Dmitry S. Kulyabov"]
date: 2025-02-20T11:38:00+03:00
lastmod: 2025-07-08T20:17:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "obs-studio"
---

OBS Studio.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


## <span class="section-num">2</span> Сценарии применения {#сценарии-применения}

-   [OBS Studio. Стриминг]({{< relref "2025-02-16--obs-studio-streaming" >}})


## <span class="section-num">3</span> Плагины {#плагины}


### <span class="section-num">3.1</span> Работа с фоном {#работа-с-фоном}


#### <span class="section-num">3.1.1</span> obs-backgroundremoval {#obs-backgroundremoval}

-   Репозиторий: <https://github.com/locaal-ai/obs-backgroundremoval>
-   Устранение фона (без хромакея).
-   Установка
    -   Gentoo (оверлей `supertux88`):
        ```shell
        emerge media-plugins/obs-backgroundremoval
        ```


#### <span class="section-num">3.1.2</span> obs-composite-blur {#obs-composite-blur}

-   Добавление размытия.
-   Репозиторий: <https://github.com/FiniteSingularity/obs-composite-blur>
-   Установка
    -   Gentoo
        ```shell
        emerge media-plugins/obs-composite-blur
        ```


### <span class="section-num">3.2</span> Стриминг {#стриминг}


#### <span class="section-num">3.2.1</span> obs-multi-rtmp {#obs-multi-rtmp}

-   Репозиторий: <https://github.com/sorayuki/obs-multi-rtmp>
-   Плагин позволяет одновременно стримить на несколько платформ без использования сторонних сервисов рестриминга.
-   Возможности:
    -   Запуск трансляций на несколько RTMP-серверов (зависит от скорости интернет-соединения).
    -   Возможность индивидуальная настройки для каждого потока (выбор кодировщика, разрешения, частоты кадров, битрейт и прочее).
    -   Синхронизация запуска трансляции на несколько платформ по нажатию на одну кнопку.
    -   Выбор аудиодорожек для каждого потока.
-   Установка
    -   Gentoo (оверлей `guru`, см. [Gentoo. Дополнительные репозитории]({{< relref "2023-10-01-gentoo-additional-repositories" >}})):
        ```shell
        emerge media-video/obs-multi-rtmp
        ```


## <span class="section-num">4</span> Управление {#управление}

-   [OBS Studio. Удалённое управление]({{< relref "2025-07-08--obs-studio-remote-control" >}})
