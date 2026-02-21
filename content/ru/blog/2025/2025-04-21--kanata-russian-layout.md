---
title: "kanata. Русская раскладка"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-21T16:44:00+03:00
lastmod: 2025-04-23T18:31:00+03:00
tags: ["hard"]
categories: ["computer-science"]
draft: false
slug: "kanata-russian-layout"
---

kanata. Русская раскладка

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Варианты {#варианты}


### <span class="section-num">1.1</span> Использование XKB для переключения раскладок {#использование-xkb-для-переключения-раскладок}

-   Один из подходов --- использование XKB для переключения раскладок (см. [Клавиатура. xkb]({{< relref "2025-04-22--keyboard-xkb" >}})).
-   Это не всегда удобно.
-   Примерная конфигурация.

<!--listend-->

```lisp
(defcfg
    danger-enable-cmd yes
  )

(defvar
    tap-timeout   100
  hold-timeout  200
  tt $tap-timeout
  ht $hold-timeout
  )

(defsrc
    grv  1    2    3    4    5    6    7    8    9    0    -    =    bspc
    tab  q    w    e    r    t    y    u    i    o    p    [    ]    \
    caps a    s    d    f    g    h    j    k    l    ;    '    ret
    lsft z    x    c    v    b    n    m    ,    .    /    rsft
    lctl lmet lalt           spc            ralt rmet menu rctl
    )

(deflayer qwerty
    grv  1    2    3    4    5    6    7    8    9    0    -    =    bspc
    tab  q    w    e    r    t    y    u    i    o    p    [    ]    \
    caps  a    s    d    f    g    h    j    k    l    ;    '    ret
    lsft z    x    c    v    b    n    m    ,    .    /    rsft
    lctl lmet lalt           spc            ralt rmet menu @rctl_ext
    )

(deflayer russian
    grv  1    2    3    4    5    6    7    8    9    0    -    =    bspc
    tab  q    w    e    r    t    y    u    i    o    p    [    ]    \
    caps  a    s    d    f    g    h    j    k    l    ;    '    ret
    lsft z    x    c    v    b    n    m    ,    .    /    rsft
    @lctl_ext lmet lalt           spc            ralt rmet menu rctl
    )
```

-   Несколько команд объединяются с помощью функции `multi`.
-   Вариант переключения с помощью команд оболочки.
    ```lisp
    (defalias
        rctl_ext (tap-hold-press $tt $ht (multi (cmd swaymsg input 'type:keyboard' xkb_layout ru) (layer-switch russian)) rctl)
      lctl_ext (tap-hold-press $tt $ht (multi (cmd swaymsg input 'type:keyboard' xkb_layout us) (layer-switch qwerty)) lctl)
      )
    ```
-   В качестве альтернативы можно предложить переключения с помощью клавиатурных сочетаний, используемых операционной системой:
    ```lisp
    (defalias
        rctl_ext (tap-hold-press $tt $ht (multi lsft lalt (layer-switch russian)) rctl)
      lctl_ext (tap-hold-press $tt $ht (multi lsft lalt (layer-switch qwerty)) lctl)
      )
    ```
-   Здесь мы использовали комбинацию `Shift+Alt`.


### <span class="section-num">1.2</span> Использование Unicode {#использование-unicode}

-   Другой вариант — использование Unicode или макросов с Compose-последовательностями.
-   Предлагается использовать слой с латинскими символами, которые преобразуются в русские через XKB или Compose-последовательности.
-   Необходимо настроить XKB для корректной работы.
-   Для примера настроим переключение слоя через CapsLock.
-   Вот пример конфигурации Kanata для поддержки русского языка через отдельный слой с использованием Unicode-символов:
    ```lisp
    (defsrc
      grv  1    2    3    4    5    6    7    8    9    0    -    =    bspc
      tab  q    w    e    r    t    y    u    i    o    p    [    ]    \
      caps a    s    d    f    g    h    j    k    l    ;    '    ret
      lsft z    x    c    v    b    n    m    ,    .    /    rsft
      lctl lmet lalt           spc            ralt rmet rctl
    )

    (deflayer querty
      grv  1    2    3    4    5    6    7    8    9    0    -    =    bspc
      tab  q    w    e    r    t    y    u    i    o    p    [    ]    \
      @ru_switch  a    s    d    f    g    h    j    k    l    ;    '    ret
      lsft z    x    c    v    b    n    m    ,    .    /    rsft
      lctl lmet lalt           spc            ralt rmet rctl
    )

    (deflayer russian
      ё    1    2    3    4    5    6    7    8    9    0    -    =    bspc
      tab  й    ц    у    к    е    н    г    ш    щ    з    х    ъ    \
      @en_switch  ф    ы    в    а    п    р    о    л    д    ж    э    ret
      lsft я    ч    с    м    и    т    ь    б    ю    .    rsft
      lctl lmet lalt           spc            ralt rmet rctl
    )

    (defalias
      ru_switch (layer-switch russian)
      ru_switch (layer-switch english)
      ё (unicode ё)
      ...
    )
    ```
-   В консоли не работает.
-   Отправляет символ как unicode-последовательность. Явно видны задержки.
-   Для работы потребуется:
    -   Установить русскую раскладку в системе
    -   Настроить переключение слоя через сочетание клавиш (в примере CapsLock)
    -   Добавить Unicode-маппинг для всех необходимых символов

-   Особенности реализации:
    -   Использует отдельный слой для русской раскладки
    -   Переключение между слоями через модификатор CapsLock
    -   Прямая отправка Unicode-символов через (unicode xxxx)
