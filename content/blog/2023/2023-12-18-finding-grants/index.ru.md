---
title: "Поиск грантов"
author: ["Dmitry S. Kulyabov"]
date: 2023-12-18T15:39:00+03:00
lastmod: 2023-12-23T19:03:00+03:00
categories: ["science"]
draft: false
slug: "finding-grants"
---

Поиск грантов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Агрегаторы информации {#агрегаторы-информации}


### <span class="section-num">1.1</span> ГУАП {#гуап}

-   ГУАП (Государственный университет аэрокосмического приборостроения) поддерживает хранилище открытых данных <https://api.guap.ru/data/>.
-   Информация по грантам.
    -   Страница: <https://api.guap.ru/data/NidGrants>
    -   JSON-запрос: `https://api.guap.ru/data/get-nidgrants`:
        ```shell
        curl 'https://api.guap.ru/data/get-nidgrants' -o grants.json
        ```
-   Информация по грантодателям.
    -   Страница: <https://api.guap.ru/data/NidGrantOrgs>
    -   JSON-запрос: `https://api.guap.ru/data/get-nidgrantorgs`:
        ```shell
        curl 'https://api.guap.ru/data/get-nidgrantorgs' -o grantorgs.json
        ```
