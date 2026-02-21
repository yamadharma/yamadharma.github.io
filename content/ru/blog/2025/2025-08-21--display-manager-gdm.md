---
title: "Дисплейный менеджер gdm"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-21T11:50:00+03:00
lastmod: 2025-08-21T12:14:00+03:00
tags: ["linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "display-manager-gdm"
---

Дисплейный менеджер gdm.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   GDM --- это дисплейный менеджер для GNOME, графическая программа для логина пользователя.
-   Использует Wayland или X Window System.
-   По умолчанию, GDM запускается от лица непривилегированного пользователя и вход от имени root запрещён.
-   Информация:
    -   <https://wiki.archlinux.org/title/GDM>
    -   <https://wiki.debian.org/ru/GDM>


## <span class="section-num">2</span> Настройка {#настройка}


### <span class="section-num">2.1</span> Зеркалирование экрана на HDMI через GDM {#зеркалирование-экрана-на-hdmi-через-gdm}


### <span class="section-num">2.2</span> Настройка зеркалирования в текущей сессии (для пользователя) {#настройка-зеркалирования-в-текущей-сессии--для-пользователя}

-   Откройте `Настройки` → `Дисплеи`.
-   Выберите режим `Зеркальное отображение` (Mirror Displays).
-   Нажмите `Применить` и сохраните изменения.


### <span class="section-num">2.3</span> Настройка GDM для зеркалирования на экране входа {#настройка-gdm-для-зеркалирования-на-экране-входа}

-   GDM использует отдельную конфигурацию.
-   Чтобы применить зеркалирование на экране входа, скопируйте файл настроек мониторов из вашего пользователя в папку GDM:
    ```shell
    sudo cp ~/.config/monitors.xml /var/lib/gdm/.config/
    sudo chown gdm:gdm /var/lib/gdm/.config/monitors.xml
    ```
