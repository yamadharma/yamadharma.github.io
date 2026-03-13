---
title: "Преобразование biblatex в bibitem"
author: ["Dmitry S. Kulyabov"]
date: 2023-07-11T19:48:00+03:00
lastmod: 2023-09-15T17:21:00+03:00
tags: ["tex"]
categories: ["computer-science"]
draft: false
slug: "convert-biblatex-bibitem"
---

Преобразование biblatex в bibitem.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Некоторые журналы принимают библиографию только в виде:
    ```bibtex
    \begin{thebibliography}{99}
    \bibitem{name}
    ...
    \end{thebibliography}
    ```
-   Выходной формат _bibtex_ даёт результат, очень похожий на искомый.
-   Но _biblatex_ имеет абсолютно другой формат.
-   Необходимо преобразовать файлы, создаваемые _biblatex_, в искомый вид.


## <span class="section-num">2</span> Пакет `biblatex2bibitem` {#пакет-biblatex2bibitem}

-   Репозиторий: <https://gitlab.com/Nickkolok/biblatex2bibitem>
-   Входит в состав TeXlive.


## <span class="section-num">3</span> Использование {#использование}

-   В преамбуле после загрузки biblatex добавьте:
    ```latex
    \usepackage{biblatex2bibitem}
    ```
-   В конце документа добавьте:
    ```latex
    \printbibitembibliography
    ```
-   Результат в виде `bibitems` будет записан непосредственно в файл pdf.
-   Этот код можно скопировать из файла `.pdf` в файл `.tex`.
-   Скопировать можно мышкой, выделив нужные строки в просмотрщике.
-   Можно скопировать с помощью `pdftotext`.


## <span class="section-num">4</span> Настройка {#настройка}


### <span class="section-num">4.1</span> Разделители bibitem {#разделители-bibitem}

-   По умолчанию полученные `bibitems` разделяются строкой с пустой парой фигурных скобок, чтобы облегчить чтение кода.
-   Можно заменить эти скобки, или просто убрать:
    ```latex
    \renewcommand{\printgeneratedbibitemseparator}{}
    ```


### <span class="section-num">4.2</span> Другие переопределяемые команды {#другие-переопределяемые-команды}

-   `\print@begin@thebibliography`: по умолчанию `\begin{thebibliography}{99}`;
-   `\print@end@thebibliography`: по умолчанию `\end{thebibliography}`;
-   `\print@bibitem@command`: по умолчанию `\bibitem`.


## <span class="section-num">5</span> Пример использования {#пример-использования}

-   Подключите в преамбуле стиль BibLaTex.
    -   Стиль GOST:
        ```latex
        \usepackage[%
        parentracker=true,%
        backend=biber,%
        hyperref=auto,%
        language=auto,
        autolang=other*,%
        langhook=extras,%
        citestyle=gost-numeric,%
        defernumbers=true,%
        bibstyle=gost-footnote,%
        style=gost-numeric,%
        % disable printing the URLs and ISBNs in the bibliography
        url=false,
        isbn=false,
        eprint=true,
        % enables/disables generation of the back references to the citation,
        % which are usually number(s) of the page where citation appears
        %backref=true,
        % Amount of displayed author names
        % limit amount of authors of the cited document to be printed in the
        % document body and in the bibliography, respectively
        maxcitenames=100,
        maxbibnames=100,
        % A threshold affecting all lists of names
        maxnames=100,%
        minnames=1,%
        % This option automatically starts a new reference section at a document division such
        % as a chapter or a section
        %refsection=chapter,%
        % Similar to the refsection option but starts a new reference segment
        %refsegment=chapter,
        % This option automatically executes the \citereset command at a
        % document division such as a chapter or a section.
        %citereset=chapter,%
        % Global cite counter
        %citecounter=false,%
        % sorting=nty,nyt,nyvt,anyt,anyvt,ynt,ydnt,none
        % sorting=nty,
        sorting=none,%
        movenames=false,%
        ]{biblatex}
        ```
-   Подключите bib-файл:
    ```latex
    \addbibresource{bib/cite.bib}
    ```
-   Добавьте вызов пакета для трансляции biblatex в bibitem:
    ```latex
    \usepackage{biblatex2bibitem}
    \renewcommand{\printgeneratedbibitemseparator}{}
    ```
-   В конце документа добавьте:
    -   для контроля вида библиографии:
        ```latex
        \printbibliography
        ```
    -   для вывода библиографии в виде bibitem:
        ```latex
        \printbibitembibliography
        ```
