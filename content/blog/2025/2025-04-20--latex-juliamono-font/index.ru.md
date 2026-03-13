---
title: "LaTeX. Шрифт JuliaMono"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-20T17:08:00+03:00
lastmod: 2025-04-20T17:46:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex-juliamono-font"
---

LaTeX. Шрифт JuliaMono.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Достаточно полный набор математических символов:
    -   <https://mono-math.netlify.app/#JuliaMono>
    -   <https://coding-fonts.css-tricks.com/fonts/juliamono/?language=charmap>
-   Сайт: <https://juliamono.netlify.app/>
-   Репозиторий: <https://github.com/cormullion/juliamono>
-   Свойства
    -   Лицензия: SIL Open Font licence
    -   Лигатуры: есть
    -   Курсив: нет


## <span class="section-num">2</span> LaTeX {#latex}


### <span class="section-num">2.1</span> Использование в LuaLaTeX и XeLaTeX для отдельного проекта {#использование-в-lualatex-и-xelatex-для-отдельного-проекта}

-   Скачайте шрифт и расположите в подкаталоге `fonts` рабочего каталога:
    ```shell
    mkdir -p fonts
    cd fonts
    wget https://github.com/cormullion/juliamono/releases/latest/download/JuliaMono-ttf.tar.gz
    tar xzvf JuliaMono-ttf.tar.gz
    rm -f JuliaMono-ttf.tar.gz
    ```
-   Использование в LuaLaTeX и XeLaTeX:

-   Здесь шрифты расположены в локальном каталоге `./fonts`.
-   В зависимости от гарнитуры основного текста для кода можно использовать вместо гарнитуры `JuliaMono-Medium` гарнитуру `JuliaMono-Light` или `JuliaMono-Black`.


### <span class="section-num">2.2</span> Настройки стилей {#настройки-стилей}

-   Стиль для `listings`:
    -   <https://github.com/mossr/julia-mono-listings>
