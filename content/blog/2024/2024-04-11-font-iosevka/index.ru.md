---
title: "Шрифт. Iosevka"
author: ["Dmitry S. Kulyabov"]
date: 2024-04-11T19:15:00+03:00
lastmod: 2026-03-09T13:44:00+03:00
tags: ["font"]
categories: ["computer-science"]
draft: false
slug: "font-iosevka"
---

Шрифтовая гарнитура Iosevka.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://typeof.net/Iosevka/>
-   Репозиторий: <https://github.com/be5invis/Iosevka/>
-   Дизайн на основе:
    -   PragmataPro,
    -   PF DIN Mono.
-   Первая версия называлась _codexHW_:
    -   была создана 19 июля 2015 года,
    -   через три дня шрифт был переименован в Iosevka.
    -   Создал китайский типограф Renzhi Li, использующий романизированный псевдоним Belleve Invis.
-   Узкий дизайн.
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: есть
    -   Курсив: есть


## <span class="section-num">2</span> Варианты {#варианты}

-   Для всех вариантов пакеты содержат три варианта интервалов.
    -   _Default_: вариант по умолчанию с лигатурами. Также содержит широкие (2 столбца) символы (например, стрелки).
    -   _Terminal (Term)_: более узкий вариант для терминала. Стрелки и геометрические символы будут узкими.
    -   _Fixed_: моноширинный шрифт без лигатур и широких глифов.
        -   Некоторые среды не воспринимают _Iosevka_ или _Iosevka Term_ как моноширинные шрифты и не могут работать с лигатурами.


## <span class="section-num">3</span> Начертания {#начертания}

-   _Iosevka_: моноширинный.
-   _Iosevka Slab_: моноширинный, Slab-serif.
-   _Iosevka Curly_: моноширинный, Curly Style.
-   _Iosevka Curly Slab_: моноширинный, Curly Style, Slab-serif.
-   _Iosevka Aile_: псевдопропорциональный, Sans-serif.
-   _Iosevka Etoile_: псевдопропорциональный, Slab-serif.


## <span class="section-num">4</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge media-fonts/iosevka
    ```


## <span class="section-num">5</span> Деривативы {#деривативы}


### <span class="section-num">5.1</span> Iosevka Comfy {#iosevka-comfy}

-   Репозиторий:
    -   <https://github.com/protesilaos/iosevka-comfy>
    -   <https://gitlab.com/protesilaos/iosevka-comfy>


### <span class="section-num">5.2</span> Sarasa-Gothic {#sarasa-gothic}

-   На основе шрифтов Inter, Iosevka, Source Han Sans.
-   Основное свойство --- наличие символов CJK.
-   Репозиторий: <https://github.com/be5invis/Sarasa-Gothic>


### <span class="section-num">5.3</span> Настройка {#настройка}


#### <span class="section-num">5.3.1</span> Iosevka-custom-conf {#iosevka-custom-conf}

-   Репозиторий: <https://github.com/v3rmine/Iosevka-custom-conf>
-   Описание возможности настройки шрифта Iosevka.


## <span class="section-num">6</span> Проблемы {#проблемы}


### <span class="section-num">6.1</span> LuaTeX {#luatex}

-   Шрифты для luatex индексируются в базу при помощи программы `luaotfload-tool`.
-   Индексация иногда зависает на некоторых файлах формата `.ttc`.
-   Iosevka распространяется именно в этом формате.
-   И именно на шрифтах Iosevka индексирование виснет на неопределённое время.
-   Следует занести шрифты в блэклист.
-   Создайте файл `luaotfload-blacklist.cnf`:
    ```conf-unix
    Iosevka.ttc
    IosevkaAile.ttc
    IosevkaCurly.ttc
    IosevkaCurlySlab.ttc
    IosevkaEtoile.ttc
    IosevkaSlab.ttc
    ```
-   Разместите его в каталог, доступный для поиска TeX:
    -   `/usr/local/texlive/2026/texmf-dist/tex/luatex/luaotfload/luaotfload-blacklist.cnf`;
    -   `~/texmf/tex/luatex/luaotfload/luaotfload-blacklist.cnf`.
