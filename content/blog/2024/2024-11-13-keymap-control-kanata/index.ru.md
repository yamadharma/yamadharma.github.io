---
title: "Раскладка клавиатуры. kanata"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-13T14:42:00+03:00
lastmod: 2025-07-05T21:09:00+03:00
tags: ["hard"]
categories: ["computer-science"]
draft: false
slug: "keymap-control-kanata"
---

Раскладка клавиатуры. kanata.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/jtroo/kanata>
-   Документация:
    -   <https://github.com/jtroo/kanata/blob/main/docs/config.adoc>
    -   <https://jtroo.github.io/config.html>
-   Поддержка ОС: Linux, Windows, MacOS.
-   Язык реализации: Rust.


### <span class="section-num">1.1</span> Сервисы {#сервисы}

-   Онлайн симулятор kanata: <https://jtroo.github.io/>.
-   Можно загрузить свою конфигурацию и проверить.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   Репозиторий karma (см. [Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
    ```shell
    emerge app-misc/kanata
    ```


## <span class="section-num">3</span> Настройки доступа для Linux {#настройки-доступа-для-linux}

-   В Linux kanata должна иметь доступ к подсистемам `input` и `uinput` для работы с событиями.


### <span class="section-num">3.1</span> Группа uinput {#группа-uinput}

-   Проверьте наличие группы `uinput`:
    ```shell
    getent group | grep uinput
    ```
-   Если группы нет, создайте её:
    ```shell
    sudo groupadd uinput
    ```


### <span class="section-num">3.2</span> Добавьте пользователя в нужные группы {#добавьте-пользователя-в-нужные-группы}

-   Нужно добавить пользователей в группы `input` и `uinput`:
    ```shell
    sudo usermod -aG input $USER
    sudo usermod -aG uinput $USER
    ```
-   Убедитесь, что пользователь добавлен в группы:
    ```shell
    groups
    ```
-   Возможно, вам придётся выйти из системы и залогиниться обратно.


### <span class="section-num">3.3</span> Права доступа к файлу устройства {#права-доступа-к-файлу-устройства}

-   Добавьте правило udev (в `/etc/udev/rules.d` или `/lib/udev/rules.d`):
    ```conf-unix
    KERNEL=="uinput", MODE="0660", GROUP="uinput", OPTIONS+="static_node=uinput"
    ```
-   Перечитайте права доступа:
    ```shell
    sudo udevadm control --reload && udevadm trigger --verbose --sysname-match=uniput
    ```


### <span class="section-num">3.4</span> Загрузите модуль ядра {#загрузите-модуль-ядра}

-   Вручную это можно сделать так:
    ```shell
    sudo modprobe uinput
    ```
-   Для автоматической загрузки добавьте в файл `/etc/modules-load.d/uinput.conf`:
    ```shell
    uinput
    ```


## <span class="section-num">4</span> Отслеживание приложений {#отслеживание-приложений}

-   Можно отслеживать приложения.
-   С помощью дополнительного демона, зависящего от графического окружения.
-   Демон передаёт kanata название слоя, основанное на приложении.
-   Linux
    -   hyprkan: <https://github.com/mdSlash/hyprkan>
    -   nata : <https://github.com/mdSlash/nata>
    -   qanata : <https://github.com/veyxov/qanata>
-   macOS
    -   kanata-vk-agent : <https://github.com/devsunb/kanata-vk-agent>
-   Windows
    -   komokana : <https://github.com/LGUG2Z/komokana>
    -   kanawin : <https://github.com/Aqaao/kanawin>


## <span class="section-num">5</span> Пример разделов файла конфигурации {#пример-разделов-файла-конфигурации}

-   Файла конфигурации по умолчанию `~/.config/kanata/kanata.kbd`


### <span class="section-num">5.1</span> defcfg {#defcfg}

-   В этом разделе хранятся «глобальные» параметры, которые применяются ко всему Kanata.
-   Например, настроим, чтобы обрабатывалась каждая нажатая клавишу, независимо от того, указана ли она в конфигурации явно.
-   Будем отслеживать, на каком слое происходит работа.

<!--listend-->

```lisp
(defcfg
      process-unmapped-keys yes
      log-layer-changes yes
)
```


### <span class="section-num">5.2</span> defsrc {#defsrc}

-   Этот раздел может появляться в конфигурации только один раз.
-   Он сообщает Kanata, какие исходные клавиши следует ожидать для сопоставления.
-   Можно Задавать только интересующие нас клавиши.
    ```lisp
    (defsrc
          esc
          grv
          caps
          a s d f g h j k l scln
          lalt spc ralt
    )
    ```


### <span class="section-num">5.3</span> deflayer {#deflayer}

-   Можно определить много слоёв и активировать их нажатием клавиш.
-   Например, определим два слоя: всегда активный слой, который означает клавиши, которые я хочу постоянно переназначать, чтобы делать что-то другое, и второй слой, который активируется только тогда, когда я удерживаю `caps lock`.
-   Переназначаемые клавиши должны быть в том же порядке, что и исходный слой выше.
-   Символ `_` задаёт прозрачные ключи, их отображение не изменяется и передаётся прозрачно.
-   `@` обозначает псевдоним.
-   В этом примере слой по умолчанию изменяет функциональность всех клавиш, за исключением `g`, `h`, и `spc` потому, что они прозрачны.
-   Левый `alt` меняется на `escape`.
-   Правый `alt` меняется на `backspace`.
-   В слое `cap-Mod` клавиши `h`, `j`, `k`, `l` становятся клавишами со стрелками.
    ```lisp
    (deflayer default
          @esc
          @grv
          @cap
          @a @s @d @f _ _ @j @k @l @scln
          esc _ bspc
    )
    (deflayer cap-mod
          _
          _
          _
          _ _ _ _ _ left down up rght _
          _ _ _
    )
    ```


### <span class="section-num">5.4</span> defvar {#defvar}

-   Kanata позволяет тонко настраивать поведение, указывая такие вещи, как длительность нажатия клавиши, чтобы она считалась «удержанной».
-   Хотя можно вводить эти значения (в миллисекундах) каждый раз, проще определить их как переменную в одном месте и ссылаться на них повсюду.
    ```lisp
    (defvar
          tap-time 200
          hold-time 250
    )
    ```


### <span class="section-num">5.5</span> defalias {#defalias}

-   Здесь определяются все псевдонимы (`@`).
-   Псевдоним принимает форму: `name-of-alias-without-@sign (type-of-functionality options-for-that-function multiple-options-are-space-separated)`.
    ```lisp
    (defalias
          esc (tap-hold-press $tap-time $hold-time esc caps)
          grv (tap-hold-press $tap-time $hold-time S-grv grv)
          capsword (caps-word 2000)
          cap (tap-hold-press $tap-time $hold-time @capsword (layer-toggle cap-mod))
          a (tap-hold $tap-time $hold-time a lmet)
          s (tap-hold $tap-time $hold-time s lalt)
          d (tap-hold $tap-time $hold-time d lsft)
          f (tap-hold $tap-time $hold-time f lctl)
          j (tap-hold $tap-time $hold-time j rctl)
          k (tap-hold $tap-time $hold-time k rsft)
          l (tap-hold $tap-time $hold-time l lalt)
          scln (tap-hold $tap-time $hold-time scln lmet)
    )
    ```
-   `tap-hold` : позволяет нам определить, что происходит, когда мы нажимаем клавишу, а когда удерживаем.
-   `tap-hold` имеет 4 варианта:
    -   `$tap-time` количество миллисекунд, в течение которых клавиша может быть нажата, при этом нажатие будет считаться одним нажатием;
    -   `$hold-time` количество миллисекунд, в течение которых клавиша должна оставаться нажатой, чтобы она считалась удержанием;
    -   код клавиши, который мы хотим, чтобы Каната использовала при нажатии;
    -   код клавиши, который Каната должен использовать при удержании клавиши.
-   `tap-hold-press` похоже на `tap-hold`, но помогает лучше управлять моментами нажатия.
-   `caps-word` : функция, которая позволяет вам вводить CAPITALIZED_WORDS и автоматически отключает CAPS, если это не буква или подчеркивание.


### <span class="section-num">5.6</span> Аккорды (defchords) {#аккорды--defchords}

-   Простые аккорды без гибких таймаутов и release-поведения.
-   Позволяют выполнять различные действия в зависимости от того, какая конкретная комбинация клавиш ввода нажимаются вместе.
-   Такая неупорядоченная комбинация клавиш называется _аккорд_.
-   Входные аккорды настраиваются аналогично `defalias` с двумя дополнительными параметрами в начале каждой группы `defchords`:
    -   название группы;
    -   значение тайм-аута, по истечении которого аккорд срабатывает, если он не был сработан при отпускании клавиши.
-   Пример:
    ```lisp
    (defsrc a b c)
    (deflayer default
      @cha @chb @chc
    )

    (defalias
      cha (chord example a)
      chb (chord example b)
      chc (chord example c)
    )

    (defchords example 500
      (a      ) a
      (   b   ) b
      (a     c) C-v
      (a  b  c) @three
    )
    ```

    -   Первый элемент каждой пары определяет клавиши, составляющие данный аккорд.
    -   Второй элемент каждой пары --— это действие, которое должно быть выполнено.
    -   В отличие от `defseq`, эти ключи не соответствуют напрямую реальным ключам и являются просто произвольными метками, которые имеют смысл в контексте аккорда.


### <span class="section-num">5.7</span> Аккорды (defchordsv2) {#аккорды--defchordsv2}

-   Расширенные настройки, интеграция с макросами, управление слоями.


#### <span class="section-num">5.7.1</span> Синтаксис `defchordsv2` {#синтаксис-defchordsv2}

-   Синтаксис `defchordsv2`
    ```lisp
    (defchordsv2
      (participating-keys1) action1 timeout1 release-behaviour1 (disabled-layers1)
      ...
      (participating-keysN) actionN timeoutN release-behaviourN (disabled-layersN)
    )
    ```

-   Каждый аккорд задаётся 5-кортежем:
    -   `participating-keys` --- список клавиш, участвующих в аккорде (например, `(d a y)`).
    -   `action` --- действие, выполняемое при активации (макрос, переключение слоя и т.д.).
    -   `timeout` --- время (в мс), в течение которого клавиши должны быть нажаты для активации.
    -   `release-behaviour` --- поведение при отпускании клавиш:
        -   `first-release`: аккорд активируется при отпускании любой клавиши.
        -   `last-release`: аккорд активируется при отпускании всех клавиш.
    -   `disabled-layers` --- слои, где аккорд не работает (например, `()` для всех слоёв).


#### <span class="section-num">5.7.2</span> Примеры использования {#примеры-использования}

<!--list-separator-->

1.  1. Простой аккорд для ввода слова

    ```lisp
    (defchordsv2
      (h l o)
      (macro h e l l o spc)
      200
      first-release
      ()
    )
    ```

    -   Клавиши: `h + l + o`.
    -   Действие: вводит "hello " (с пробелом).
    -   Таймаут: 200 мс.
    -   Активация: при отпускании любой клавиши.

<!--list-separator-->

2.  2. Аккорд с управлением регистром

    ```lisp
    (defvirtualkeys rls-sft (multi (release-key lsft) (release-key rsft)))

    (defchordsv2
      (d a y)
      (macro sldr d (t! rls-sft) a y spc nop0)
      200
      first-release
      ()
    )
    ```

    -   Клавиши: `d + a + y`.
    -   Действие:
        -   `(t! rls-sft)` --- отпускает Shift.
        -   Вводит "day " (с пробелом).
        -   `nop0` --- блокирует исходные клавиши.


#### <span class="section-num">5.7.3</span> Особенности {#особенности}

-   Обратное сопоставление
    -   Для работы с текстовыми словарями (как в ZipChord) требуется ручное сопоставление символов с клавишами `defsrc`, что может быть недетерминированным при пересечении слоёв.

-   Интеграция с макросами
    -   Аккорды часто используют `macro` для:
        -   Ввода текста с пробелами: `(macro hello spc)` → "hello ".
        -   Управления модификаторами: `(t! rls-sft)` для сброса Shift.

-   Ограничения
    -   Минимум 2 клавиши в аккорде.
    -   Нет встроенной поддержки автоматического пробела/заглавных букв --- это настраивается вручную через макросы.


## <span class="section-num">6</span> Примеры конфигураций {#примеры-конфигураций}

-   [kanata. Клавиша Caps Lock]({{< relref "2025-05-06--kanata-capslock" >}})
-   [kanata. Русская раскладка]({{< relref "2025-04-21--kanata-russian-layout" >}})
-   [Пример конфигурации раскладки клавиатуры]({{< relref "2025-04-23--kanata-configuration-example" >}})
-   [kanata. Настройка Home Row Mods]({{< relref "2025-05-01--kanata-home-row-mods" >}})
-   [kanata. Настройка Caps Word]({{< relref "2025-05-05--kanata-capsword" >}})
