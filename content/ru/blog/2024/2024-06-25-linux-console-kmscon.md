---
title: "Консоль linux. Kmscon"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-25T12:08:00+03:00
lastmod: 2024-06-25T15:34:00+03:00
tags: ["hard", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "linux-console-kmscon"
---

Консоль linux. Kmscon.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Эмулятор терминала.
-   Основан на kernel mode setting Linux.
-   Попытка заменить реализацию VT в ядре консолью пользовательского пространства.
-   Автор не работает над программой.
-   Стабильного ментейнера нет.
-   Репозиторий текущий: <https://github.com/aetf/kmscon>
-   Репозитории исторические:
    -   <https://cgit.freedesktop.org/~dvdhrm/kmscon/>
    -   <https://github.com/MacSlow/kmscon>


### <span class="section-num">1.1</span> Функции {#функции}

-   Полная реализация vt220–vt510.
-   Полная поддержка интернационализации:
    -   поддерживает Юникод, CJK;
    -   обработка клавиатуры через _libxkbcommon_.
-   Аппаратное ускорение рендеринга.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   В основном репозитории:
    ```shell
    emerge sys-apps/kmscon
    ```


## <span class="section-num">3</span> Включение kmscon {#включение-kmscon}

-   Обычно для tty1 существует специальная конфигурация systemd.
    -   Можно продолжать запускать традиционный agetty на tty1 и запускать kmscon на всех остальных виртуальных терминалах.
    -   Можно запустить kmscon как на tty1, так и на других VT.
-   Чтобы включить kmscon на tty1, отключите `getty@tty1.service` и включить `kmsconvt@tty1.service`.


### <span class="section-num">3.1</span> Включение на всех терминалах {#включение-на-всех-терминалах}

-   Чтобы включить kmscon на всех виртуальных терминалах, выполните:
    ```shell
    ln -s /usr/lib/systemd/system/kmsconvt\@.service /etc/systemd/system/autovt\@.service
    ```
-   Это заставит `systemd-login` использовать `kmsconvt@.service` вместо `getty@.service` для новых VT.
-   Если `kmscon` не может запуститься по какой-либо причине, будет запущен `getty@.service`.


## <span class="section-num">4</span> Файлы настройки {#файлы-настройки}

-   Для настройки используются файлы:
    -   `/etc/kmscon/kmscon.conf`.


## <span class="section-num">5</span> Поддержка HiDPI {#поддержка-hidpi}

-   Можно изменить размер шрифта на лету с помощью `Ctrl++`, `Ctrl+Shift+=`, `Ctrl+-`.
-   Можно установить `font-dpi` и `font-size` в `/etc/kmscon/kmscon.conf`:
    ```conf-unix
    font-dpi=192
    ```
