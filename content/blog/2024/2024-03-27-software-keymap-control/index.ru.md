---
title: "Программное управление раскладкой клавиатуры"
author: ["Dmitry S. Kulyabov"]
date: 2024-03-27T21:28:00+03:00
lastmod: 2025-05-21T16:04:00+03:00
tags: ["hard"]
categories: ["computer-science"]
draft: false
slug: "software-keymap-control"
---

Программное управление раскладкой клавиатуры.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Программные пакеты {#программные-пакеты}


### <span class="section-num">1.1</span> kanata {#kanata}

-   [Раскладка клавиатуры. kanata]({{< relref "2024-11-13-keymap-control-kanata" >}})
-   Репозиторий: <https://github.com/jtroo/kanata>
-   Поддержка ОС: Linux, Windows, MacOS.
-   Язык реализации: Rust.


### <span class="section-num">1.2</span> kmonad {#kmonad}

-   Репозиторий: <https://github.com/kmonad/kmonad>
-   Поддержка ОС: Linux, Windows, MacOS.
-   Язык реализации: Huskell.


### <span class="section-num">1.3</span> ktrl {#ktrl}

-   Репозиторий: <https://github.com/ItayGarin/ktrl>
-   Поддержка ОС: Linux.
-   Позиционирует себя как реализация QMK под Linux.


### <span class="section-num">1.4</span> kbremap {#kbremap}

-   Репозиторий: <https://github.com/timokroeger/kbremap>
-   Поддержка ОС: Windows.


### <span class="section-num">1.5</span> xcape {#xcape}

-   Репозиторий: <https://github.com/alols/xcape>
-   Поддержка ОС: Linux.
-   Позволяет использовать клавишу-модификатор в при нажатии и отжатии.


### <span class="section-num">1.6</span> karabiner-elements {#karabiner-elements}

-   Сайт: <https://karabiner-elements.pqrs.org/>
-   Репозиторий: <https://github.com/pqrs-org/Karabiner-Elements>
-   Поддержка ОС: MacOS.


### <span class="section-num">1.7</span> capsicain {#capsicain}

-   Репозиторий: <https://github.com/cajhin/capsicain>
-   Поддержка ОС: Windows.
-   Переназначает клавиши и комбинации клавиш-модификаторов на низком уровне.


### <span class="section-num">1.8</span> keyd {#keyd}

-   [Раскладка клавиатуры. keyd]({{< relref "2025-05-21--keyboard-layout-keyd" >}})
-   Репозиторий: <https://github.com/rvaiya/keyd>
-   Поддержка ОС: Linux.
-   Слои: Поддержка слоёв через модификаторы.
-   Tap-hold: Базовая реализация через макросы.
-   Макросы: Только комбинации клавиш.
-   Интегрируется с X11 и Wayland через libinput, но требует настройки для виртуальных машин.


### <span class="section-num">1.9</span> xremap {#xremap}

-   Репозиторий: <https://github.com/xremap/xremap>
-   Поддержка ОС: Linux.
-   Вдохновлена клавиатурными последовательностями Emacs, а не слоями QMK/режимами Vim.


### <span class="section-num">1.10</span> keymapper {#keymapper}

-   Репозиторий: <https://github.com/houmain/keymapper>
-   Поддержка ОС: Linux, Windows, MacOS.


## <span class="section-num">2</span> Firmware {#firmware}


### <span class="section-num">2.1</span> QMK {#qmk}

-   Сайт: <https://qmk.fm/>
-   Документация: <https://docs.qmk.fm/>


### <span class="section-num">2.2</span> keyberon {#keyberon}

-   Репозиторий: <https://github.com/TeXitoi/keyberon>
-   Язык реализации: Rust.


## <span class="section-num">3</span> Логическое управление раскладкой {#логическое-управление-раскладкой}

-   [Клавиатура. xkb]({{< relref "2025-04-22--keyboard-xkb" >}})
