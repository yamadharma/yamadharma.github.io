---
title: "BibTeX entry types"
author: ["Dmitry S. Kulyabov"]
date: 2023-07-11T17:53:00+03:00
lastmod: 2023-07-11T18:23:00+03:00
tags: ["tex"]
categories: ["computer-science"]
draft: false
slug: "bibtex-entry-type"
---

BibTeX entry types.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> General information {#general-information}

-   A BibTeX entry start with the `@` sign followed by the entry type name.
-   Everything that belongs to the entry is enclosed in curly brackets.
    ```bibtex
    % Basic structure of a BibTeX entry
    @book{ ... }
    ```


## <span class="section-num">2</span> Entry types {#entry-types}

-   In its current version BibTeX features 14 entry types.
-   Here is a complete list of the BibTeX entry types:
    -   `article`: any article published in a periodical like a journal article or magazine article;
    -   `book`: a book;
    -   `booklet`: like a book but without a designated publisher;
    -   `conference`: a conference paper;
    -   `inbook`: a section or chapter in a book;
    -   `incollection`: an article in a collection;
    -   `inproceedings`: a conference paper (same as the `conference` entry type);
    -   `manual`: a technical manual;
    -   `masterthesis`: a Masters thesis;
    -   `misc`: used if nothing else fits;
    -   `phdthesis`: a PhD thesis;
    -   `proceedings`: the whole conference proceedings;
    -   `techreport`: a technical report, government report or white paper;
    -   `unpublished`: a work that has not yet been officially published.
