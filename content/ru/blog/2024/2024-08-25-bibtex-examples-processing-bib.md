---
title: "Bibtex. Примеры команд для обработки bib-файлов"
author: ["Dmitry S. Kulyabov"]
date: 2024-08-25T11:23:00+03:00
lastmod: 2024-08-25T13:18:00+03:00
tags: ["tex", "bib"]
categories: ["computer-science"]
draft: false
slug: "bibtex-examples-processing-bib"
---

Bibtex. Примеры команд для обработки bib-файлов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Извлечение записей из bib-файла {#извлечение-записей-из-bib-файла}


### <span class="section-num">1.1</span> bib2bib {#bib2bib}

-   Программа из пакета _bibtex2html_.
-   Сайт: <https://usr.lmf.cnrs.fr/~jcf/bibtex2html/index.en.html>
-   Репозиторий: <https://github.com/backtracking/bibtex2html>


#### <span class="section-num">1.1.1</span> Записи определённого года {#записи-определённого-года}

-   Читает входные файлы `biblio1.bib` и `biblio2.bib`, выбирает только записи, появившиеся в 1999 году:
    ```shell
    bib2bib -oc cite1999 -ob 1999.bib -c 'year=1999' biblio1.bib biblio2.bib
    ```

    -   Полученный файл `cite1999` содержит список выбранных ключей.
    -   Можно создать HTML-файл с помощью:
        ```shell
        bibtex2html -citefile cite1999 1999.bib
        ```
-   Можно выбрать ссылки, появившиеся после заданного года. Например, ссылки после 1997 года:
    ```shell
    bib2bib -oc citeaft1997 -ob aft1997.bib -c 'year>1997' biblio.bib
    ```
-   Можно выбрать ссылки между 1990 и 1995 годами:
    ```shell
    bib2bib -oc cite90-95 -ob 90-95.bib -c 'year>=1990 and year<=1995' biblio.bib
    ```


#### <span class="section-num">1.1.2</span> Ссылки данного автора {#ссылки-данного-автора}

-   Читаем файл `biblio.bib`, выберем только записи, соавтором которых является Дональд Кнут:
    ```shell
    bib2bib -oc knuth-citations -ob knuth.bib -c 'author : "Knuth"' biblio.bib
    ```
-   Выберем только те ссылки, автор которых только Кнут (через регулярные выражения):
    ```shell
    bib2bib -oc knuth-citations -ob knuth.bib -c 'author : "^\(Donald \(E. \)?Knuth\|Knuth, Donald \(E.\)?\)$"' biblio.bib
    ```
-   Почти то же самое (через логические операции):
    ```shell
    bib2bib -oc knuth-citations -ob knuth.bib -c 'author = "Donald Knuth" or author = "Knuth, Donald"' biblio.bib
    ```


## <span class="section-num">2</span> Создание bib-файла с процитированными ссылками {#создание-bib-файла-с-процитированными-ссылками}

-   [Создание bib-файла с процитированными ссылками]({{< relref "2022-11-20-bib-file-cited" >}})
