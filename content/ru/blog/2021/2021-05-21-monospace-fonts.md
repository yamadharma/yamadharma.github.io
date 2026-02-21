---
title: "Моноширинные шрифты"
author: ["Dmitry S. Kulyabov"]
date: 2021-05-21T13:25:00+03:00
lastmod: 2025-04-20T17:11:00+03:00
tags: ["programming"]
categories: ["computer-science"]
draft: false
slug: "monospace-fonts"
---

-   Для программирования и описания программ в статьях необходим шрифт с большим количеством символов.
-   Стандартный буквенный набор поддерживает большинство шрифтов (но не все поддерживают кириллицу), но с дополнительными символами могут возникнуть проблемы.
-   Особенно часто дополнительные символы используются в программах на языке _Julia_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Основные определения {#основные-определения}

-   Моноширинный (непропорциональный) шрифт --- это шрифт, в котором все знаки (кегельные площадки знаков) имеют одинаковую ширину.


## <span class="section-num">2</span> Сравнение шрифтов {#сравнение-шрифтов}

-   Есть несколько сайтов, на которых сравниваются шрифты для программирования на предмет широты охвата разных символов.
    -   <https://mono-math.netlify.app/> --- математические символы в моноширинных шрифтах.
    -   <https://devfonts.gafi.dev/> --- шрифты для программирования.
    -   <https://www.programmingfonts.org/> --- шрифты для программирования.
    -   <https://coding-fonts.css-tricks.com/> --- шрифты для программирования.
-   На данный момент наибольшее количество математических символов содержит шрифт _JuliaMono_.


## <span class="section-num">3</span> Применимость {#применимость}

-   Шрифт для редактора (например, emacs) желательно выбирать с курсивом. Иначе, теряется определённый набор выделений текста.
-   Также для семантического выделения курсив используют разные программы с текстовым интерфейсам (например, эмулятор терминала _kitty_).
-   Если шрифт имеет переменную ширину знаков, то едут таблицы.


## <span class="section-num">4</span> Активация лигатур в шрифтах {#активация-лигатур-в-шрифтах}


### <span class="section-num">4.1</span> LaTeX {#latex}

-   При использовании LuaTeX и XeTeX лигатуры включаются опцией `Contextuals=Alternate` пакета `fontspec`:


## <span class="section-num">5</span> Шрифты с лигатурами {#шрифты-с-лигатурами}

-   Часть шрифтов для программирования содержит лигатуры.


### <span class="section-num">5.1</span> Fira Code {#fira-code}

-   Шрифт сделан на базе Fira Mono.
-   Репозиторий: <https://github.com/tonsky/FiraCode>
-   Автор: Никита Прокопов
    -   Блог в livejournal (на русском): <https://tonsky.livejournal.com/>
    -   Блог на английском: <https://tonsky.me/>
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: есть
    -   Курсив: нет
-   Установка.
    -   Gentoo:
        ```shell
        emerge media-fonts/fira-code
        ```


### <span class="section-num">5.2</span> Iosevka {#iosevka}

-   [Шрифт. Iosevka]({{< relref "2024-04-11-font-iosevka" >}})
-   Сайт: <https://typeof.net/Iosevka/>
-   Репозиторий: <https://github.com/be5invis/Iosevka/>
-   Дизайн на основе:
    -   PragmataPro,
    -   PF DIN Mono.
-   Узкий дизайн.
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: есть
    -   Курсив: есть


### <span class="section-num">5.3</span> JetBrains Mono {#jetbrains-mono}

-   Сайт: <https://www.jetbrains.com/lp/mono/>
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: есть
    -   Курсив: есть
-   Установка.
    -   Gentoo:
        ```shell
        emerge media-fonts/jetbrains-mono
        ```


### <span class="section-num">5.4</span> JuliaMono {#juliamono}

-   [LaTeX. Шрифт JuliaMono]({{< relref "2025-04-20--latex-juliamono-font" >}})
-   Достаточно полный набор математических символов:
    -   <https://mono-math.netlify.app/#JuliaMono>
    -   <https://coding-fonts.css-tricks.com/fonts/juliamono/?language=charmap>
-   Сайт: <https://juliamono.netlify.app/>
-   Репозиторий: <https://github.com/cormullion/juliamono>
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: есть
    -   Курсив: нет


### <span class="section-num">5.5</span> Hasklig {#hasklig}

-   Сделан на основе Source Code Pro с добавлением лигатур.
-   Репозиторий: <https://github.com/i-tu/Hasklig>
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: есть
    -   Курсив: нет


### <span class="section-num">5.6</span> Cascadia Code {#cascadia-code}

-   Разработан для Windows Terminal.
-   Репозиторий: <https://github.com/microsoft/cascadia-code>
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: есть
    -   Курсив: нет
-   Установка.
    -   Gentoo:
        ```shell
        emerge media-fonts/cascadia-code
        ```


### <span class="section-num">5.7</span> Victor Mono {#victor-mono}

-   Сайт: <https://rubjo.github.io/victor-mono/>
-   Репозиторий: <https://github.com/rubjo/victor-mono>
-   Таблицы, оформленные этим шрифтом, разъезжаются.
-   Имеет узкий дизайн.
-   Свойства
    -   Лицензия: MIT
    -   Лигатуры: есть
    -   Курсив: есть
-   Установка.
    -   Gentoo:
        -   Можно найти в оверлее:
            -   _4nykey_: <https://gpo.zugaina.org/Overlays/4nykey>
            -   karma: <https://github.com/yamadharma/gentoo-portage-local>
        -   Установка
            ```shell
            emerge media-fonts/victor-mono
            ```


## <span class="section-num">6</span> Шрифты с иконками {#шрифты-с-иконками}


### <span class="section-num">6.1</span> Font Awesome {#font-awesome}

-   Наиболее известный шрифт с иконками.
-   <https://fontawesome.com/>
-   Font Awesome Pro
    -   <https://fontawesome.com/pro>
    -   Распространяется по платной подписке.
-   Font Awesome Free
    -   <https://github.com/FortAwesome/Font-Awesome>
    -   Лицензия:
        -   Иконки: CC BY 4.0
        -   Шрифты: SIL Open Font licence
        -   Программный код: MIT
    -   Для использования шрифта можно использовать список кодов для иконок <https://fontawesome.com/cheatsheet>.
-   Установка
    -   Gentoo
        ```shell
        emerge media-fonts/fontawesome
        ```


### <span class="section-num">6.2</span> Nerd fonts {#nerd-fonts}

-   Проект по добавлению ы разные шрифты дополнительных глифов (в основном иконок).
-   Сайт: <https://www.nerdfonts.com/>
-   Репозиторий: <https://github.com/ryanoasis/nerd-fonts/>
-   Поиск глифа: <https://www.nerdfonts.com/cheat-sheet>
-   Установка
    -   Gentoo
        ```shell
        USE="iosevka" emerge nerd-fonts
        ```

        -   При установке следует указать, какой конкретно шрифт следует устанавливать.
        -   Ebuild находится не в основном репозитории.


## <span class="section-num">7</span> Шрифты {#шрифты}


### <span class="section-num">7.1</span> Source Code Pro {#source-code-pro}

-   Часть набора Source Pro.
-   Сайт: <http://adobe-fonts.github.io/source-code-pro/>
-   Репозиторий: <https://github.com/adobe-fonts/source-code-pro>
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: нет
    -   Курсив: есть
-   Установка.
    -   Gentoo:
        ```shell
        emerge media-fonts/source-pro
        ```


### <span class="section-num">7.2</span> Anonymous Pro {#anonymous-pro}

-   Сайт: <https://www.marksimonson.com/fonts/view/anonymous-pro>
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: нет
    -   Курсив: есть
-   Установка.
    -   Gentoo:
        ```shell
        emerge media-fonts/anonymous-pro
        ```


### <span class="section-num">7.3</span> Hack {#hack}

-   Репозиторий: <https://github.com/source-foundry/Hack>
-   Свойства
    -   Лицензия: MIT
    -   Лигатуры: нет
    -   Курсив: есть
-   Установка.
    -   Gentoo:
        ```shell
        emerge media-fonts/hack
        ```


### <span class="section-num">7.4</span> Hermit {#hermit}

-   Сайт: <https://pcaro.es/p/hermit/>
-   Репозиторий: <https://github.com/pcaro90/hermit>
-   Таблицы, оформленные им, разъезжаются.
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: нет
    -   Курсив: есть
-   Установка.
    -   Gentoo:
        ```shell
        emerge media-fonts/hermit
        ```


### <span class="section-num">7.5</span> IBM Plex Mono {#ibm-plex-mono}

-   Сайт: <https://www.ibm.com/plex/>
-   Репозиторий: <https://github.com/IBM/plex>
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: нет
    -   Курсив: есть
-   Установка.
    -   Gentoo:
        ```shell
        emerge media-fonts/ibm-plex
        ```
