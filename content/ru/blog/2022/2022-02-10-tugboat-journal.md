---
title: "Журнал TUGboat"
author: ["Dmitry S. Kulyabov"]
date: 2022-02-10T16:49:00+03:00
lastmod: 2023-10-27T15:54:00+03:00
tags: ["tex"]
categories: ["science"]
draft: false
slug: "tugboat-journal"
---

Журнал _TUGboat_ является основным изданием TeX Users Group (TUG).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Журнал TUGboat является основным изданием TeX Users Group (TUG).
-   Страница: <https://www.tug.org/TUGboat/>
-   Список всех выпусков: <https://www.tug.org/TUGboat/contents.html>
-   Существует с 1980 года и в настоящее время выходит три раза в год.
-   Содержит технические статьи, а также отчёты о собраниях и информацию сообщества TeX.
-   Доступ к текущему выпуску ограничен и предоставляется только членам TUG.
    -   Выпуски становятся общедоступными через год после публикации.
-   TUGboat также доступен в печатном виде.
    -   Печатные выпуски рассылаются по почте постоянным членам TUG.


## <span class="section-num">2</span> Скачать все выпуски {#скачать-все-выпуски}

-   Набросал скрипт, чтобы скачать все выпуски _TUGboat_:
    ```shell
    #!/bin/bash

    pass_through_number=01

    for volume in $(seq -w 1 50)
    do
        for number in $(seq 0 5)
        do
            issue=tb${volume}-${number}
            issue2=tb${volume}-${number}-$((number + 1))
            echo ${issue} + ${pass_through_number}
            server_response=$(wget --server-response https://www.tug.org/TUGboat/${issue}/tb${pass_through_number}complete.pdf 2>&1 | awk '/^  HTTP/{print $2}')
            if [[ ${server_response} == 404 ]]
            then
                # Volume 12, number 3-4
                server_response=$(wget --server-response https://www.tug.org/TUGboat/${issue2}/tb${pass_through_number}acomplete.pdf 2>&1 | awk '/^  HTTP/{print $2}')
                server_response=$(wget --server-response https://www.tug.org/TUGboat/${issue2}/tb${pass_through_number}bcomplete.pdf 2>&1 | awk '/^  HTTP/{print $2}')
                if [[ ${server_response} != 404 ]]
                then
                    mkdir -p ${volume}
                    mv tb${pass_through_number}acomplete.pdf ${volume}/"TUGboat - ${volume} - ${number}a (${pass_through_number})".pdf
                    mv tb${pass_through_number}bcomplete.pdf ${volume}/"TUGboat - ${volume} - ${number}b (${pass_through_number})".pdf
                    # Increase `pass_through_number`
                    pass_through_number=$(echo ${pass_through_number} + 1 | bc)
                    if (( ${pass_through_number} < 10 ))
                    then
                        pass_through_number=0${pass_through_number}
                    fi
                fi
                # Volume 22, number 1-2
                server_response=$(wget --server-response https://www.tug.org/TUGboat/${issue2}/tb${pass_through_number}complete.pdf 2>&1 | awk '/^  HTTP/{print $2}')
                if [[ ${server_response} != 404 ]]
                then
                    mkdir -p ${volume}
                    mv tb${pass_through_number}complete.pdf ${volume}/"TUGboat - ${volume} - ${number2} (${pass_through_number})".pdf
                    # Increase `pass_through_number`
                    pass_through_number=$(echo ${pass_through_number} + 1 | bc)
                    if (( ${pass_through_number} < 10 ))
                    then
                        pass_through_number=0${pass_through_number}
                    fi
                fi
                continue
            else
                # Rename file
                mkdir -p ${volume}
                mv tb${pass_through_number}complete.pdf ${volume}/"TUGboat - ${volume} - ${number} (${pass_through_number})".pdf
                # Increase `pass_through_number`
                pass_through_number=$(echo ${pass_through_number} + 1 | bc)
                if (( ${pass_through_number} < 10 ))
                then
                    pass_through_number=0${pass_through_number}
                fi
            fi
        done
    done
    ```
