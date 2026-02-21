---
title: "Epub. Утилиты"
author: ["Dmitry S. Kulyabov"]
date: 2026-01-09T21:37:00+03:00
lastmod: 2026-01-09T22:05:00+03:00
tags: ["sysadmin", "read"]
categories: ["computer-science"]
draft: false
slug: "epub-utilities"
---

Epub. Утилиты

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Объединение файлов {#объединение-файлов}


### <span class="section-num">1.1</span> 9beach/epub-merge {#9beach-epub-merge}

-   Репозиторий: <https://github.com/9beach/epub-merge>
-   Объединение нескольких файлов ePUB в один.
-   Разделение файла, созданные с помощью epub-merge.
-   Утилиты на bash.


#### <span class="section-num">1.1.1</span> Объединение файлов EPUB {#объединение-файлов-epub}

-   Утилита `epub-merge`:
    ```shell
    # Merge all ePUB files.
    epub-merge *.epub

    # Add prefix and suffix to volume labels
    epub-merge -p "Book " -s " Edition" part1.epub part2.epub

    # Extract a merged ePUB back into original files
    epub-merge -x love.epub

    # Merge files in the order specified with custom volume labels
    epub-merge -O -v "Love//Peace//Hate" a1.epub 02.epub 03.epub

    # Merge with custom title and filename
    epub-merge -t "Arabian Nights: Tales of 1,001 Nights" 1001*.epub
    ```


#### <span class="section-num">1.1.2</span> Работа с метаданными {#работа-с-метаданными}

-   Утилита `epub-meta`:
    ```shell
    # Set title and author
    epub-meta -t "Brave New World Revised" -a "Aldous Huxley" book.epub

    # Multiple authors or translators
    epub-meta -a "Tom Waits--Waits, Tom//Lily Allen--Allen, Lily" book.epub
    epub-meta -r "Deborah Smith//John Doe" book.epub

    # Language, publisher, and dates
    epub-meta -l ko -p "문학동네" -u "2024-08-15" book.epub

    # ISBN and subject
    epub-meta -i "978-89-546-1234-5" -s "Fiction//Classic" book.epub

    # Add a new cover image
    epub-meta -c cover.jpg book.epub

    # Replace an existing cover
    epub-meta -C new-cover.png book.epub

    # Extract current cover to a file (extension auto-added)
    epub-meta -S ./cover-out book.epub

    # Automatically fix invalid cover configurations
    epub-meta -f book.epub
    ```


### <span class="section-num">1.2</span> EpubMerge {#epubmerge}

-   Репозиторий: <https://github.com/JimmXinu/EpubMerge>
-   Плагин для Calibre (см. [Каталогизатор книг Calibre]({{< relref "2025-02-04--calibre-book-cataloger" >}})).
