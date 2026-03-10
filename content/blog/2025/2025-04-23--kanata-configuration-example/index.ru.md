---
title: "Пример конфигурации раскладки клавиатуры"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-23T18:33:00+03:00
lastmod: 2025-05-21T16:51:00+03:00
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
      )
    ```
-   Определяем переменные.
    ```lisp
    (defvar
      streak-count 3
      streak-time 325
      tap-timeout 200
      hold-timeout 500
      chord-timeout 50
      tt $tap-timeout
      ht $hold-timeout
      )
    ```


#### <span class="section-num">1.1.2</span> Структура раскладки {#структура-раскладки}

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


#### <span class="section-num">1.1.3</span> Шаблон модификаторов {#шаблон-модификаторов}

-   Цель: реализация Tap-Hold модификаторов (клавиша работает как символ при коротком нажатии и как модификатор при удержании).
-   Задаём шаблон:
    ```lisp
    (deftemplate charmod (char mod)
      (switch
        ((key-timing $streak-count less-than $streak-time)) $char break
        () (tap-hold-release-timeout $tap-timeout $hold-timeout $char $mod $char) break
      )
    )
    ```

    -   Параметры:
        -   `key-timing $streak-count less-than $streak-time` — проверяет, нажата ли предыдущая клавиша (3-я по счёту) менее 250 мс назад. Если да, модификатор игнорируется, чтобы избежать ложных срабатываний при быстрой печати.
        -   Проверка `key-timing` снижает ошибки при быстрой печати.
        -   `tap-hold-release-timeout $tap-timeout $hold-timeout`:
            -   `$tap-timeout` : время (мс) удержания для активации модификатора;
            -   `$hold-timeout` : таймаут (мс) для возврата к символу, если модификатор не использован.


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
    -   Подключим ранее определённые аккорды:

    <!--listend-->

    ```lisp
    (deflayermap (main)
        w (chord mtl w)
        e (chord mtl e)
        i (chord mtr i)
        o (chord mtr o)
        x (chord mbl x)
        c (chord mbl c)
        , (chord mbr ,)
        . (chord mbr .)
    ```

    <!--list-separator-->

    1.  Home Row Mods

        -   [kanata. Настройка Home Row Mods]({{< relref "2025-05-01--kanata-home-row-mods" >}})
        -   Используется макет `GACS` / `◆⎇⎈⇧`.
        -   Добавим описание Home Row Mods:

        <!--listend-->

        ```lisp
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

    2.  Дополнительные управляющие клавиши

        ```lisp
        z (t! charmod z lctl)
        / (t! charmod / rctl)
        ```

    <!--list-separator-->

    3.  Переключение на слой fumbol

        ```lisp
        v (t! charmod v (layer-while-held fumbol))
        m (t! charmod m (layer-while-held fumbol))
        ```

    <!--list-separator-->

    4.  Замена `Caps Lock` на `Ctrl` и `Escape`

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

    5.  Использование XKB для переключения раскладок

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

        1.  Переключение с помощью команды оболочки

            -   Переключаем с помощью команд оболочки (для Sway).
                ```lisp
                ;; ralt (tap-hold-press $tt $ht (cmd swaymsg input 'type:keyboard' xkb_layout ru) ralt)
                ;; lalt (tap-hold-press $tt $ht (cmd swaymsg input 'type:keyboard' xkb_layout us) lalt)
                ```
            -   При этом перестаёт работать переключение языка на уровне окна (<https://github.com/artemsen/swaykbdd>).

        <!--list-separator-->

        2.  Переключение путём отправки комбинации клавиш

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

    6.  Использование пробела для переключения уровней

        -   Определяем поведение клавиши пробела (`spc`) с использованием Tap-Hold модификатора.

        <!--listend-->

        ```lisp
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

    7.  Завершение

        ```lisp
        )
        ```


#### <span class="section-num">1.1.5</span> Слой extend {#слой-extend}

```lisp
(deflayermap (extend)
  e (layer-switch fumbol)
  r (on-press press-virtualkey shift)
  y ins
  u home
  i up
  o end
  p pgup
  a lmet
  s lalt
  d lsft
  f lctl
  g comp ;; Enable if not MacOS.
  h esc
  j left
  k down
  l rght
  ; pgdn
  z mute
  x vold
  c volu
  v pp
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
      [ f11
      ] f12
      \ f13
      a (t! charmod 1 lmet)
      s (t! charmod 2 lalt)
      d (t! charmod 3 lsft)
      f (t! charmod 4 lctl)
      g 5
      h 6
      j (t! charmod 7 rctl)
      k (t! charmod 8 rsft)
      l (t! charmod 9 lalt)
      ; (t! charmod 0 rmet)
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
