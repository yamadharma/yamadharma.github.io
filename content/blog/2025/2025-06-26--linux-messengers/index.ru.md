---
title: "Linux. Использование мессенджеров"
author: ["Dmitry S. Kulyabov"]
date: 2025-06-26T12:36:00+03:00
lastmod: 2025-06-26T13:33:00+03:00
draft: false
slug: "linux-messengers"
---

Linux. Использование мессенджеров.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> WhatsApp {#whatsapp}


### <span class="section-num">1.1</span> WasIstLos {#wasistlos}

-   Репозиторий: <https://github.com/xeco23/WasIstLos>
-   На базе webkit2gtk.
-   Теряет эмодзи.


#### <span class="section-num">1.1.1</span> Установка {#установка}

-   Gentoo (оверлей `guru`):
    ```shell
    emerge net-im/WasIstLos
    ```


## <span class="section-num">2</span> Telegram {#telegram}


### <span class="section-num">2.1</span> Emacs. Telega {#emacs-dot-telega}


## <span class="section-num">3</span> Мультисервисные {#мультисервисные}


### <span class="section-num">3.1</span> Franz {#franz}

-   Сайт: <https://meetfranz.com/>
-   Кроссплатформенное приложение для управления мессенджерами.
-   Позволяет объединить несколько аккаунтов из разных сервисов в одном интерфейсе.
-   Поддерживает более 70 сервисов.
-   Для работы требует учётной записи на сервере <https://meetfranz.com/>.
-   Использование учётной записи --- платное.


#### <span class="section-num">3.1.1</span> Установка {#установка}

-   Gentoo (оверлей `mva`):
    ```shell
    emerge net-im/franz-bin
    ```


### <span class="section-num">3.2</span> Ferdium {#ferdium}

-   Сайт: <https://ferdium.org/>
-   Репозиторий: <https://github.com/ferdium/ferdium-app>
-   Кроссплатформенное приложение для управления мессенджерами.
-   Позволяет объединить несколько аккаунтов из разных сервисов в одном интерфейсе.
-   Форк приложения Franz.
-   Может использовать учётную запись на сервере <https://ferdium.org/>.
-   Учётная запись используется для синхронизации.
-   Использование учётной записи бесплатно.
-   Возможна работа без учётной записи на сервере <https://ferdium.org/>.
-   Также можно использовать свой сервер для учётных записей.


#### <span class="section-num">3.2.1</span> Установка {#установка}

-   Gentoo (оверлей `djs_overlay`):
    ```shell
    emerge net-im/ferdium-bin
    ```
