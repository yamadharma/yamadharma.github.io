---
title: "kanata. Настройка Caps Word"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-05T15:06:00+03:00
lastmod: 2025-05-06T09:25:00+03:00
tags: ["hard"]
categories: ["computer-science"]
draft: false
slug: "kanata-capsword"
---

kanata. Настройка Caps Word.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Caps Word есть альтернатива классическому Caps Lock.
-   Предназначенная для удобного ввода слов или фрагментов текста в верхнем регистре без необходимости удерживать клавиши.
-   Автоматически активируется и деактивируется, экономя время и снижая нагрузку на руки.


### <span class="section-num">1.1</span> Как работает Caps Word {#как-работает-caps-word}

-   Активация:
    -   Двойной тап на Shift (или другую назначенную клавишу).
    -   Комбинация клавиш (например, Ctrl + Shift).
    -   Однократное нажатие на переназначенный Caps Lock.
-   Деактивация:
    -   При вводе символа, не входящего в разрешённый список (например, пробел, запятая, цифра).
    -   По истечении таймаута.
    -   Явное отключение через повторное нажатие активатора.


### <span class="section-num">1.2</span> Ключевые особенности {#ключевые-особенности}

-   Автоматизация: Не нужно постоянно держать Shift или включать/выключать Caps Lock.
-   Гибкие правила:
    -   Можно разрешить символы вроде `_`, `-`, цифры, чтобы Caps Word не прерывался.
    -   Пример: `API_ENDPOINT_2024` --- все буквы автоматически вводятся в верхнем регистре.
-   Совместимость с модификаторами: Работает вместе с Ctrl, Alt, GUI (например, для горячих клавиш).

---


### <span class="section-num">1.3</span> Примеры использования {#примеры-использования}

-   Программирование:
    -   Ввод констант (`MAX_LENGTH`), макросов (`DEBUG_MODE`), тегов (`<HTML>`) без переключения регистра.
-   Документы:
    -   Заголовки, аббревиатуры (СПб, NASA), акронимы.
-   Гейминг:
    -   Быстрый ввод команд в чате (например, `HELP`).

---


### <span class="section-num">1.4</span> Преимущества перед Caps Lock {#преимущества-перед-caps-lock}

-   Не требует ручного выключения.
-   Не мешает вводу символов в нижнем регистре после завершения слова.
-   Эргономичнее для частого использования (например, в коде).


## <span class="section-num">2</span> Реализация {#реализация}


### <span class="section-num">2.1</span> Формат использования {#формат-использования}

-   `caps-word` приводит kanata в состояние, когда набранные клавиши автоматически предваряются `lsft`.
-   Состояние сохраняется до тех пор, пока не будет прекращено по тайм-ауту или по нажатию клавиши, которая завершает состояние.
    -   Нажатие клавиши, не являющейся завершающей, обновляет длительность тайм-аута.
-   При нажатии клавиша `caps-word-toggle` завершит состояние Caps Word.
-   Синтаксис:
    ```lisp
    (caps-word $timeout)
    (caps-word-toggle $timeout)
    (caps-word-custom $timeout $shifted-list $non-terminal-list)
    (caps-word-custom-toggle $timeout $shifted-list $non-terminal-list)
    ```

-   `$timeout` : количество миллисекунд, по истечении которых состояние заглавных слов заканчивается. Длительность обновляется при вводе не завершающего символа.
-   `$shifted-list` : список клавиш, которые будут использоваться для Caps Word.
-   `$non-terminal-list` : список клавиш, которые не набираются заглавными, но которые не прекращают состояние заглавных слов.


### <span class="section-num">2.2</span> Описание {#описание}

-   `caps-word` вызывает состояние, в котором в верхнем регистре набирается список активных ключей.
-   Ключи таковы: `a-z` и `-`, которые будут выведены как `A-Z` и `_`  соответственно (при использовании английской раскладки).
-   Это поведение имеет преимущество перед обычным Caps Lock, потому что это автоматически заканчивается.
-   Его не нужно выключать вручную.
-   Также преводит `-` в `_`, чего не делает Caps Lock.
-   Состояние `caps-word` заканчивается, когда клавиатура бездействует определённое время (1-й параметр), или нажата клавиша завершения.
-   Каждый ключ является завершающим ключом за исключением клавиш, которые пишутся с заглавной буквы и дополнительные ключи в этом списке:
    -   `0-9`
    -   `kp0-kp9`
    -   `bspc del`
    -   `up down left rght`
-   Можно использовать `caps-word-custom` вместо `caps-word` если необходимо вручную определить, какие клавиши будут написаны заглавными буквами (2-й параметр) и какими должны быть дополнительные нетерминальные и не заглавные клавиши (3-й параметр).

-   Пример:
    ```lisp
    (defalias
      cw (caps-word 2000)
      ;; This example is similar to the default caps-word behaviour but it moves the
      ;; 0-9 keys to the capitalized key list from the extra non-terminating key list.
      cwc (caps-word-custom
        2000
        (a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9)
        (kp0 kp1 kp2 kp3 kp4 kp5 kp6 kp7 kp8 kp9 bspc del up down left rght)
      )
    )
    ```


### <span class="section-num">2.3</span> caps-word-toggle {#caps-word-toggle}

-   По умолчанию повторное нажатие `caps-word` будет держать `caps-word` активным.
-   `caps-word-toggle` завершит `caps-word`, если он в данный момент активен, в противном случае `caps-word` будет активирован в обычном режиме.
-   Пример:
    ```lisp
    (defalias
      cwt (caps-word-toggle 2000)
      cct (caps-word-custom-toggle
        2000
        (a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9)
        (kp0 kp1 kp2 kp3 kp4 kp5 kp6 kp7 kp8 kp9 bspc del up down left rght)
      )
    )
    ```


## <span class="section-num">3</span> Настройка {#настройка}


### <span class="section-num">3.1</span> Настройка в Kanata/QMK {#настройка-в-kanataqmk}

```lisp
; Kanata-конфиг: Caps Word на двойной тап Shift
(defalias
  capsword (caps-word 2000) ; Таймаут 2000 мс
  shift (tap-hold 200 200 @capsword lsft) ; Двойной тап → активация
)
```

```C
// QMK-реализация (для кастомных клавиатур)
bool process_caps_word(uint16_t keycode) {
  if (is_caps_word_on()) {
    if (keycode == KC_SPC || keycode == KC_ENT) {
      caps_word_off(); // Деактивация на пробел/энтер
      return true;
    }
  }
  return true;
}
```

---


### <span class="section-num">3.2</span> Базовый Caps Word {#базовый-caps-word}

-   Активируется двойным тапом на Shift, автоматически отключается при вводе символа, не являющегося буквой:
    ```lisp
    (defalias
      capsword (caps-word 2000) ; 2000 мс таймаут
      shift (tap-hold 200 200 @capsword lsft) ; Двойной тап на Shift → Caps Word
    )
    ```


### <span class="section-num">3.3</span> Собственные правила {#собственные-правила}

-   Добавьте исключения для символов вроде подчёркивания или цифр, чтобы Caps Word не отключался:
    ```lisp
    (defalias
      capsword (caps-word 2000 (allow-chars "a-zA-Z0-9_")) ; Разрешить цифры и подчёркивание
    )
    ```


### <span class="section-num">3.4</span> Активация через другую клавишу {#активация-через-другую-клавишу}

-   Например, через CapsLock:
    ```lisp
    (defalias
      capsword (caps-word)
      caps (tap-hold 200 200 @capsword caps) ; Тап на CapsLock → Caps Word
    )
    ```


### <span class="section-num">3.5</span> Совмещение с модификаторами {#совмещение-с-модификаторами}

-   Используйте Caps Word вместе с Home Row Mods:
    ```lisp
    (defalias
      capsword (caps-word)
      shift (tap-hold 150 300 @capsword lsft) ; Удержание → Shift, двойной тап → Caps Word
    )
    ```

---
