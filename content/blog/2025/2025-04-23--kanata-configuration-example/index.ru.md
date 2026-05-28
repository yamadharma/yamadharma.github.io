---
title: "Пример конфигурации раскладки клавиатуры"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-23T18:33:00+03:00
lastmod: 2026-05-20T11:14:00+03:00
tags: ["hard"]
categories: ["computer-science"]
draft: false
slug: "kanata-configuration-example"
---

Моя раскладка клавиатуры.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Стандартная клавиатура {#стандартная-клавиатура}

-   Настройка для полной клавиатуры.
-   Сделана на основе Kenkyo (см. [Клавиатура. Раскладка Kenkyo]({{< relref "2025-05-07--keyboard-layout-kenkyo" >}})).


### <span class="section-num">1.1</span> Настройка на основе kanata {#настройка-на-основе-kanata}

-   [Раскладка клавиатуры. kanata]({{< relref "2024-11-13-keymap-control-kanata" >}})


#### <span class="section-num">1.1.1</span> Общие настройки {#общие-настройки}

-   Базовая конфигурация.
-   Разрешаем использование команд оболочки.
    ```lisp
    (defcfg
      danger-enable-cmd yes
      ;; Process keys not explicitly defined in defsrc to ensure consistent state tracking.
      process-unmapped-keys yes
      )
    ```
-   Определяем переменные.
    ```lisp
    (defvar
      ;; Timing variables for home row mods and chords
      streak-count 3      ;; Number of keys to consider a "typing streak"
      streak-time 325     ;; Max time (ms) window to maintain a streak
      tap-timeout 200     ;; Max time (ms) for a tap to be recognized
      hold-timeout 300    ;; Time (ms) to wait before a hold is recognized
      chord-timeout 50    ;; Window (ms) to press keys together for a chord
      tt $tap-timeout
      ht $hold-timeout
      )
    ```


#### <span class="section-num">1.1.2</span> Шаблоны модификаторов {#шаблоны-модификаторов}

<!--list-separator-->

1.  flowtap

    -   Проверка, быстро ли вы печатаете.
    -   Если это так, нажимается клавиша ($flow).
    -   В противном случае выполняется логика нажатия/удержания ($tap).
        ```lisp
        ;; 'flowtap' checks if you are typing fast.
        ;; If so, it immediately taps the key ($flow).
        ;; Otherwise, it executes the tap/hold logic ($tap).
        (deftemplate flowtap (flow tap)
          (switch
            ((key-timing $streak-count less-than $streak-time)) $flow break
            () $tap break
          )
        )
        ```
    -   Параметры:
        -   `key-timing $streak-count less-than $streak-time` — проверяет, нажата ли предыдущая клавиша (3-я по счёту) менее 250 мс назад. Если да, модификатор игнорируется, чтобы избежать ложных срабатываний при быстрой печати.
        -   Проверка `key-timing` снижает ошибки при быстрой печати.

<!--list-separator-->

2.  charmod

    -   Для реализации home row.
        ```lisp
        ;; 'charmod' implements home row modifiers.
        ;; It uses 'flowtap' to avoid mod misfires during fast typing.
        ;; tap-hold-release-timeout resolves as a hold if another key is pressed and released.
        (deftemplate charmod (char mod)
          (t! flowtap
            $char
            (tap-hold-release-timeout $tap-timeout $hold-timeout $char $mod $char reset-timeout-on-press)
          )
        )
        ```
    -   Параметры:
        -   `tap-hold-release-timeout $tap-timeout $hold-timeout`:
            -   `$tap-timeout` : время (мс) удержания для активации модификатора;
            -   `$hold-timeout` : таймаут (мс) для возврата к символу, если модификатор не использован.


#### <span class="section-num">1.1.3</span> Структура раскладки {#структура-раскладки}

-   Структура раскладки:
    ```lisp
    (defsrc
        grv  1    2    3    4    5    6    7    8    9    0    -    =    bspc
        tab  q    w    e    r    t    y    u    i    o    p    [    ]    \
        caps a    s    d    f    g    h    j    k    l    ;    '    ret
        lsft z    x    c    v    b    n    m    ,    .    /    rsft
        lctl lmet lalt           spc            ralt rmet menu rctl
        )
    ```


#### <span class="section-num">1.1.4</span> Слой main {#слой-main}

<!--list-separator-->

1.  Виртуальные клавиши

    -   Зададим виртуальные клавиши.

    <!--listend-->

    ```lisp
    (defvirtualkeys
    ```

    <!--list-separator-->

    1.  Виртуальная клавиша shift

        -   Позволяет временно переключиться на базовый слой и активировать `Shift` для ввода заглавных букв/символов.
        -   `shift` --— аналог включения `Caps Lock`.

        <!--listend-->

        ```lisp
        ;; Virtual keys for managing state when switching layers
        shift (multi (layer-switch main) lsft)
        ```

        -   `(layer-switch main)` : активирует слой main (базовый слой) при нажатии клавиши `shift`.
        -   `lsft` : при удержании даёт левый Shift.

    <!--list-separator-->

    2.  Клавиша сброса

        -   Сбрасывает состояние:
            -   Отключает `shift` (если он активен).
            -   Гарантирует, что после использования `shift`  система вернётся к базовому слою без «залипания» модификаторов.
        -   `clear` --— аналог выключения `Caps Lock`.

        <!--listend-->

        ```lisp
        clear (multi (layer-switch main) (on-press release-virtualkey shift))
        )
        ```

        -   При нажатии клавиши `clear`:
            -   `(layer-switch main)` : возвращает на базовый слой;
        -   `(on-press release-virtualkey shift)` : отпускает виртуальную клавишу `shift` (если она была нажата).

<!--list-separator-->

2.  Аккорды основного слоя

    -   `w` + `e`: `Esc`
        ```lisp
        (defchords mtl $chord-timeout
          (w  ) w
          (  e) e
          (w e) esc
          )
        ```

    -   `i` + `o`: `BackSpace`
        ```lisp
        (defchords mtr $chord-timeout
          (i  ) i
          (  o) o
          (i o) bspc
          )
        ```

    -   `x` + `c`: `Tab`
    -   `x` при удержании : `AltGr`
        ```lisp
        (defchords mbl $chord-timeout
          (x  ) (t! charmod x ralt)
          (  c) c
          (x c) tab
          )
        ```

    -   `,` + `.`: `Enter`
    -   `.` при удержании : `AltGr`
        ```lisp
        (defchords mbr $chord-timeout
          (,  ) ,
          (  .) (t! charmod . ralt)
          (, .) ret
          )
        ```

<!--list-separator-->

3.  Карта слоя

    -   Зададим уровень `main` через `deflayermap`.

    <!--listend-->

    ```lisp
    (deflayermap (main)
    ```

    <!--list-separator-->

    1.  Подключение аккордов

        -   Подключим ранее определённые аккорды:

        <!--listend-->

        ```lisp
        ;; Top row chords
        w (chord mtl w)
        e (chord mtl e)
        i (chord mtr i)
        o (chord mtr o)
        ;; Bottom row modifiers
        x (chord mbl x)
        c (chord mbl c)
        , (chord mbr ,)
        . (chord mbr .)
        ```

    <!--list-separator-->

    2.  Home Row Mods

        -   [kanata. Настройка Home Row Mods]({{< relref "2025-05-01--kanata-home-row-mods" >}})
        -   Используется макет `GACS` / `◆⎇⎈⇧`.
        -   Добавим описание Home Row Mods:

        <!--listend-->

        ```lisp
        ;; Home row modifiers
        a (t! charmod a lmet)
        s (t! charmod s lalt)
        d (t! charmod d lctl)
        f (t! charmod f lsft)
        j (t! charmod j rsft)
        k (t! charmod k rctl)
        l (t! charmod l lalt)
        ; (t! charmod ; rmet)
        ```

    <!--list-separator-->

    3.  Дополнительные управляющие клавиши

        ```lisp
        z (t! charmod z lctl)
        / (t! charmod / rctl)
        ```

    <!--list-separator-->

    4.  Переключение на слой fumbol

        ```lisp
        v (t! charmod v (layer-while-held fumbol))
        m (t! charmod m (layer-while-held fumbol))
        ```

    <!--list-separator-->

    5.  Замена `Caps Lock` на `Ctrl` и `Escape`

        -   [kanata. Клавиша Caps Lock]({{< relref "2025-05-06--kanata-capslock" >}})
        -   Заменим `Caps Lock` на комбинацию:
            -   простое нажатие: `Escape`;
            -   долгое нажатие `Caps Lock` или `Caps Lock` + другая клавиша: `Ctrl`.
                ```lisp
                ;;;; CapsLock -> Esc, Ctrl
                ;; caps (t! charmod esc lctl)
                caps (tap-hold-press $tt $ht esc lctl)
                ```

    <!--list-separator-->

    6.  Использование XKB для переключения раскладок

        -   [kanata. Русская раскладка]({{< relref "2025-04-21--kanata-russian-layout" >}})
        -   Используется XKB для переключения раскладок (см. [Клавиатура. xkb]({{< relref "2025-04-22--keyboard-xkb" >}})).
        -   Несколько команд объединяются с помощью функции `multi`.
        -   Для переключения на английский используем правый `Alt`.
        -   Для переключения на русский язык используется левый `Alt`.
            ```lisp
            ;;; Switch language
            ;;;; ralt -> RU; lalt -> EN
            ```

        <!--list-separator-->

        1.  Переключение путём отправки комбинации клавиш

            -   Установим опцию xkb:
                ```conf-unix
                xkb_layout "us,ru"
                xkb_options "grp:lctrl_lwin_rctrl_menu"
                ```
            -   Комбинация `Ctrl+Left Win` переключает на первую раскладку.
            -   Комбинация `Ctrl+Menu` переключает на вторую раскладку.
            -   Переключаем путём отправки комбинации клавиш:
                ```lisp
                ralt (tap-hold-press $tt $ht (multi rctl menu) ralt)
                lalt (tap-hold-press $tt $ht (multi lctl lmeta) lalt)
                ```

    <!--list-separator-->

    7.  Использование пробела для переключения уровней

        -   Определяем поведение клавиши пробела (`spc`) с использованием Tap-Hold модификатора.

        <!--listend-->

        ```lisp
        ;; Space overloaded to 'extend' layer with state clearing logic
        spc (t! charmod spc (multi (layer-switch extend) (on-release tap-virtualkey clear)))
        ```

        -   `t! charmod` --- Tap-Hold модификатор:
            -   Короткое нажатие (tap) → отправляет `spc` (пробел).
            -   Удержание (hold) → активирует слой `extend`.
        -   `multi` --- выполняет несколько действий последовательно:
            -   `(layer-switch extend)` --- переключает на слой `extend` при удержании.
            -   `(on-release tap-virtualkey clear)` --- при отпускании клавиши отправляет виртуальную клавишу `clear`:
                -   возвращает слой к `main`;
                -   Отпускает все активные модификаторы (например, `Shift`).
        -   Пример:
            -   Удерживаете пробел → попадаете на слой `extend`, где клавиши `HJKL` могут работать как стрелки (←↓↑→).
            -   Отпускаете пробел → автоматически возвращаетесь на базовый слой `main`, и модификаторы (вроде Shift) сбрасываются.
        -   Преимущества:
            -   Пробел становится многофункциональной клавишей:
                -   Не занимает дополнительные клавиши для переключения слоёв.
                -   Избегает залипания слоя `extend` после использования.
            -   Подходит для навигации в тексте/коде без смещения рук с домашнего ряда.

    <!--list-separator-->

    8.  Завершение

        ```lisp
        )
        ```


#### <span class="section-num">1.1.5</span> Слой extend {#слой-extend}

```lisp
(deflayermap (extend)
    ;; Navigation, media, and layer switching
    e (on-press press-virtualkey shift)
    r (layer-switch fumbol)
    y ins
    u home
    i up
    o end
    p pgup

    ;; Modifiers
    a lmet
    s lalt
    d lctl
    f lsft
    g comp

    ;; Navigation & Media
    h esc
    j left
    k down
    l rght
    ; pgdn
    z mute
    x vold
    c volu
    v pp

    ;; Shortcuts
    n tab
    m bspc
    , spc
    . del
    / ret
)
```


#### <span class="section-num">1.1.6</span> Слой fumbol {#слой-fumbol}

<!--list-separator-->

1.  Аккорды слоя

    ```lisp
    ;; Chord definitions for the 'fumbol' layer (Function, Numbers, Symbols)

    (defchords ftl $chord-timeout
      (w  ) f2
      (  e) f3
      (w e) esc
    )

    (defchords ftr $chord-timeout
      (i  ) f8
      (  o) f9
      (i o) bspc
    )

    ;; Chords for numbers and math symbols on the home row
    (defchords fcl $chord-timeout
     (s    ) (t! charmod 2 lalt)
     (  d  ) (t! charmod 3 lctl)
     (    f) (t! charmod 4 lsft)
     (s d  ) kp-
     (  d f) kp+
     (s   f) 🔢₌
    )

    (defchords fcr $chord-timeout
     (j    ) (t! charmod 7 rsft)
     (  k  ) (t! charmod 8 rctl)
     (    l) (t! charmod 9 lalt)
     (j k  ) kp/
     (  k l) kp*
     (j   l) .
    )

    (defchords fbl $chord-timeout
      (x  ) (t! charmod ` ralt)
      (  c) -
      (x c) tab
    )

    (defchords fbr $chord-timeout
      (,  ) [
      (  .) (t! charmod ] ralt)
      (, .) ret
    )
    ```

<!--list-separator-->

2.  Карта слоя

    ```lisp
    (deflayermap (fumbol)
        ;; Top row: Function keys
        q f1
        w (chord ftl w)
        e (chord ftl e)
        r f4
        t f5
        y f6
        u f7
        i (chord ftr i)
        o (chord ftr o)
        p f10

        ;; Home row: Numbers with mods and symbols
        a (t! charmod 1 lmet)
        s (chord fcl s)
        d (chord fcl d)
        f (chord fcl f)
        g 5
        h 6
        j (chord fcr j)
        k (chord fcr k)
        l (chord fcr l)
        ; (t! charmod 0 rmet)

        ;; Bottom row: Symbols
        z (t! charmod lsgt lctl)
        x (chord fbl x)
        c (chord fbl c)
        v =
        b f11
        n f12
        m '
        , (chord fbr ,)
        . (chord fbr .)
        / (t! charmod \ lctl)
    )
    ```
