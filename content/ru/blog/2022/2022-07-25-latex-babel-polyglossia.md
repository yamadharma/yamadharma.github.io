---
title: "LaTeX. babel vs polyglossia"
author: ["Dmitry S. Kulyabov"]
date: 2022-07-25T17:10:00+03:00
lastmod: 2023-07-10T14:22:00+03:00
tags: ["tex"]
categories: ["computer-science"]
draft: false
slug: "latex-babel-polyglossia"
---

Сравнение _babel_ и _polyglossia_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   _polyglossia_ была создана для замены _babel_ для LuaLaTeX и XeLaTeX, поскольку _babel_ не поддерживал UTF-8.
-   С 2013 года _babel_ поддерживает кодировку UTF-8.
-   Пакеты примерно эквивалентны друг другу.
-   _pandoc_ (см. [Pandoc]({{< relref "2021-08-28-pandoc" >}})) в 2021 году перевёл latex-шаблон с _polyglossia_ на _babel_ (<https://github.com/jgm/pandoc/commit/dd7b83ac9111b63786c1042c4849d7cea79c668b>).


### <span class="section-num">1.1</span> Polyglossia {#polyglossia}

-   Репозиторий: <https://github.com/reutenauer/polyglossia>.


### <span class="section-num">1.2</span> Babel {#babel}

-   Репозиторий: <https://github.com/latex3/babel>.


## <span class="section-num">2</span> Особенности babel и polyglossia {#особенности-babel-и-polyglossia}

-   Поддержка RTL и BiDi в _babel_ теперь хорошо работает для LuaLaTeX. _polyglossia_ ориентирована на поддержку текста RTL с XeLaTeX.
-   Современная ini-система настройки языков _babel_ очень удобна, позволяет настраивать языки по отдельности.
-   Для стандартных европейских языков поддержка _babel_ на высоком уровне.
-   У _polyglossia_ возникают проблемы с поддержкой biblatex, csquotes.
