---
title: "kanata. Клавиша Caps Lock"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-06T10:39:00+03:00
lastmod: 2025-05-06T10:46:00+03:00
tags: ["hard"]
categories: ["computer-science"]
draft: false
slug: "kanata-capslock"
---

kanata. Клавиша Caps Lock.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   [Клавиатура. Клавиша Caps Lock]({{< relref "2025-05-06--keyboard-capslock" >}})


## <span class="section-num">2</span> Замена `Caps Lock` на `Escape` {#замена-caps-lock-на-escape}

-   Заменим `Caps Lock` на `Escape`:
    ```kbd
    (defcfg)
    (defsrc)
    (deflayermap (base-layer)
      caps esc
    )
    ```


## <span class="section-num">3</span> Замена `Caps Lock` на `Ctrl` и `Escape` {#замена-caps-lock-на-ctrl-и-escape}

-   Заменим `Caps Lock` на комбинацию:
    -   простое нажатие: `Escape`;
    -   долгое нажатие `Caps Lock` или `Caps Lock` + другая клавиша: `Ctrl`.


### <span class="section-num">3.1</span> Сопоставлением {#сопоставлением}

-   Сделаем на основе `deflayermap`:
    ```lisp
    (defcfg)
    (defsrc)
    (deflayermap (base-layer)
      caps (tap-hold-press 200 200 esc lctl)
    )
    ```

**\***

-   Сделаем с помощью карты клавиатуры:
    ```lisp
    (deflayer base
        grv  1    2    3    4    5    6    7    8    9    0    -    =    bspc
        tab  q    w    e    r    t    y    u    i    o    p    [    ]    \
        @cap a    s    d    f    g    h    j    k    l    ;    '    ret
        lsft z    x    c    v    b    n    m    ,    .    /    rsft
        lctl lmet lalt           spc            ralt rmet menu rctl
        )

    (defalias
        cap (tap-hold-press $tt $ht esc lctl)
      )
    ```
