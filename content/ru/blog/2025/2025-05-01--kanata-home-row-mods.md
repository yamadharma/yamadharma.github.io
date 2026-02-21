---
title: "kanata. Настройка Home Row Mods"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-01T20:10:00+03:00
lastmod: 2025-05-05T09:57:00+03:00
tags: ["hard"]
categories: ["computer-science"]
draft: false
slug: "kanata-home-row-mods"
---

kanata. Настройка Home Row Mods (см. [Клавиатура. Раскладка Home Row Mode]({{< relref "2025-04-25--keyboard-home-row-mode" >}})).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Для настройки Home Row Mods в Kanata используйте комбинации `tap-hold`.
-   Для разных пальцев можно задать разные значения, если одни пальцы медленнее других.
-   Если модификаторы срабатывают некорректно, увеличьте `hold-time` или используйте `tap-hold-release-keys` для обработки комбинаций.


### <span class="section-num">1.1</span> Основные функции {#основные-функции}

-   `tap-time` : время, после которого нажатие считается тапом (обычно 100–200 мс).
-   `hold-time` : время, после которого нажатие активирует модификатор (например, 250–300 мс).


### <span class="section-num">1.2</span> Оптимизация для быстрого набора {#оптимизация-для-быстрого-набора}

-   `tap-hold-press` или `tap-hold-release-keys` : активируют модификатор мгновенно, если нажата другая клавиша.
-   Это предотвращает залипание модификаторов при быстрой печати.


## <span class="section-num">2</span> Простая конфигурация {#простая-конфигурация}

-   Простая конфигурация.
-   Используется макет `GACS` / `◆⎇⎈⇧`.
    ```lisp
    ;; Basic home row mods example using QWERTY
    ;; For a more complex but perhaps usable configuration,
    ;; see home-row-mod-advanced.kbd

    (defcfg
      process-unmapped-keys yes
    )
    (defsrc
      a   s   d   f   j   k   l   ;
    )
    (defvar
      ;; Note: consider using different time values for your different fingers.
      ;; For example, your pinkies might be slower to release keys and index
      ;; fingers faster.
      tap-time 200
      hold-time 150
    )
    (defalias
      a (tap-hold $tap-time $hold-time a lmet)
      s (tap-hold $tap-time $hold-time s lalt)
      d (tap-hold $tap-time $hold-time d lctl)
      f (tap-hold $tap-time $hold-time f lsft)
      j (tap-hold $tap-time $hold-time j rsft)
      k (tap-hold $tap-time $hold-time k rctl)
      l (tap-hold $tap-time $hold-time l ralt)
      ; (tap-hold $tap-time $hold-time ; rmet)
    )
    (deflayer base
      @a  @s  @d  @f  @j  @k  @l  @;
    )
    ```
