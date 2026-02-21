---
title: "BibLaTeX. Отображение кода EDN"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-18T16:16:00+03:00
lastmod: 2023-10-19T19:45:00+03:00
tags: ["tex", "bib"]
categories: ["computer-science"]
draft: false
slug: "biblatex-edn-implementation"
---

BibLaTeX. Отображение кода EDN.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Реализуется отображение кода eLibrary EDN (см. [EDN - идентификатор eLibrary.ru]({{< relref "2023-10-18-edn-elibrary-ru-identifier" >}})).


## <span class="section-num">2</span> Реализация {#реализация}


### <span class="section-num">2.1</span> Расширение модели данных {#расширение-модели-данных}

-   Создаётся файл описания модели данных `edn.dbx`:
    ```latex
    \ProvidesFile{edn.dbx}[2023/10/18 add EDN field to biblatex]

    \DeclareDatamodelFields[type=field,datatype=verbatim]{edn}
    \DeclareDatamodelEntryfields{edn}

    \endinput
    ```
-   Модель данных подключается следующим образом:
    ```latex
    \usepackage[style=gost-numeric,datamodel=edn]{biblatex}
    ```


## <span class="section-num">3</span> Задание нового поля {#задание-нового-поля}

-   Задаётся новая запись для поля:
    ```latex
    \newtoggle{bbx:edn}
    \newtoggle{cbx:edn}

    \DeclareBibliographyOption{edn}[true]{%
      \global\settoggle{bbx:edn}{#1}%
      \global\settoggle{cbx:edn}{#1}}
    \ExecuteBibliographyOptions{edn}

    \DeclareFieldFormat{edn}{%
      \mkbibacro{EDN}\addcolon\space
      \ifhyperref{
        \lowercase{\href{https://elibrary.ru/#1}}{\nolinkurl{#1}}
      }{\nolinkurl{#1}}
    }
    ```


## <span class="section-num">4</span> Изменение макросов для отображения {#изменение-макросов-для-отображения}

-   Подключаем пакет для исправления макросов:
    ```latex
    \usepackage{xpatch}
    ```
-   Исправляем стандартный макрос:
    ```latex
    \xapptobibmacro{doi+eprint+url}{
      \ifcitation{
        \iftoggle{cbx:edn}
        {\printfield{edn}}
        {}
      }{
        \iftoggle{bbx:edn}
        {\printfield{edn}}
        {}
      }%
    }{}{}
    ```
-   В стиле `biblatex-gost` используется другой макрос. Исправляем и его:
    ```latex
    \xapptobibmacro{doi+eprint+url+note}{
      \newunit\newblock
      \ifcitation{
        \iftoggle{cbx:edn}
        {\printfield{edn}}
        {}
      }{
        \iftoggle{bbx:edn}
        {\printfield{edn}}
        {}
      }%
    }{}{}
    ```
