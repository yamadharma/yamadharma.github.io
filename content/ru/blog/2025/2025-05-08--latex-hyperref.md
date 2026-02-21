---
title: "LaTeX. Гиперссылки"
author: ["Dmitry S. Kulyabov"]
date: 2025-05-08T20:22:00+03:00
lastmod: 2025-05-08T20:36:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex-hyperref"
---

LaTeX. Гиперссылки.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Ошибки {#ошибки}


### <span class="section-num">1.1</span> Ошибка Improper alphabetic constant {#ошибка-improper-alphabetic-constant}

-   Ошибка `Improper alphabetic constant` при использовании hyperref возникает, когда пакет пытается обработать специальные символы или команды в закладках PDF (например, в секциях или ссылках).
-   Возникает в частности при использовании совместно с пакетом `unicode-math`.
-   Ссылки:
    -   <https://tex.stackexchange.com/questions/570000/improper-alphabetic-constant-error-in-title-with-greek-bug-with-unicode-math-an>
    -   <https://tex.stackexchange.com/questions/79131/improper-alphabetic-constant-with-hyperref-and-bidi-packages>


#### <span class="section-num">1.1.1</span> Используйте `\texorpdfstring` {#используйте-texorpdfstring}

-   Если в заголовках (например, `\section{}`) есть команды, которые нельзя преобразовать в текст (математические символы, RTL-текст и т.д.), оберните их в `\texorpdfstring`:
    ```tex
    \section{\texorpdfstring{$\alpha$}{$\symit{alpha}$}}
    ```
-   Первый аргумент --- текст для документа, _второй_ --- упрощённая версия для PDF.


#### <span class="section-num">1.1.2</span> Прямые Unicode-символы вместо команд {#прямые-unicode-символы-вместо-команд}

-   Альтернативный вариант.
-   Если вы используете `unicode-math`, заменяйте команды вроде `\euro` на прямые Unicode-символы (€ вместо `\euro`):
    ```tex
    \renewcommand{\euro}{€} % После загрузки hyperref
    ```


#### <span class="section-num">1.1.3</span> Отключите проблемные команды для закладок {#отключите-проблемные-команды-для-закладок}

-   Если ошибка вызвана командами вроде `\RL{}` (из пакета `bidi`) или символами Unicode, добавьте в преамбулу:
    ```tex
    \pdfstringdefDisableCommands{%
      \let\RL\@firstofone % Отключает обработку \RL{} в закладках
    }
    ```

-   Это заменит команду `\RL` на ее содержимое без форматирования.


#### <span class="section-num">1.1.4</span> Порядок загрузки пакетов {#порядок-загрузки-пакетов}

-   Некоторые пакеты (например, `bidi`, `polyglossia`) должны загружаться после `hyperref`.
