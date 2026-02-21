---
title: "LaTeX. Греческие буквы в листингах"
author: ["Dmitry S. Kulyabov"]
date: 2022-07-15T16:20:00+03:00
lastmod: 2023-07-22T17:23:00+03:00
tags: ["tex"]
categories: ["computer-science"]
draft: false
slug: "latex-greek-letters-listings"
---

LaTeX. Греческие буквы в листингах.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   В качестве пакета для листингов будем рассматривать `minted`.


## <span class="section-num">2</span> Использование Unicode {#использование-unicode}

-   При использовании Unicode можно в листингах использовать настоящие греческие символы:
    ```latex
    \begin{minted}{python}
      ε = …
      μ = …
      n = …
    \end{minted}
    ```
-   При этом необходимо использовать компиляторы, понимающие Unicode: `xelatex` и `lualatex`.


## <span class="section-num">3</span> Не-unicode компиляторы {#не-unicode-компиляторы}

-   При использовании не-unicode компиляторов (например, `pdflatex`), необходимо обозначать греческие буквы командными последовательностями.
-   Возможно использовать пакет `textgreek`:
    ```latex
    \usepackage{textgreek}
    ```
-   При этом греческие символы в листингах набираются в ограничителях.
-   Ограничители задаются опцией `escapeinside` для _minted_:
    ```latex
    \begin{minted}[escapeinside=||]{python}
      |\textepsilon| = …
      |\textmu| = …
      n = …
    \end{minted}
    ```
-   Ограничители `escapeinside` не срабатывают в комментариях и строках.
-   Можно обойти проблему со строками, задав оператор, заключающий аргумент в кавычки, заданные с помощью внутренних команд _minted_.
-   Зададим оператор:
    ```latex
    \newcommand{\mintescapestring}[1]{\PYG{l+s}{\PYGZsq{}}\PYG{l+s}{#1}\PYG{l+s}{\PYGZsq{}}}
    ```
-   Тогда его можно применять следующим образом:
    ```latex
    \begin{minted}[escapeinside=||]{python}
      |\texttheta| = sp.Symbol(|\mintescapestring{\texttheta}|, real=True)
      (|\texttheta|*i).exp()
    \end{minted}
    ```
-   В кодировке unicode это выглядит следующим образом:
    ```latex
    \begin{minted}{python}
      θ = sp.Symbol('θ', real=True)
      (θ*i).exp()
    \end{minted}
    ```
