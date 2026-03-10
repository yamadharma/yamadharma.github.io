---
title: "Конвертация сертификатов PKCS12 в PEM"
author: ["Dmitry S. Kulyabov"]
date: 2024-12-13T20:58:00+03:00
lastmod: 2024-12-13T21:25:00+03:00
tags: ["security", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "convert-pkcs12-pem"
---

Конвертация сертификатов PKCS12 в PEM.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   В Windows обычно используются сертификаты в формате `.pfx` (PKCS12) для хранения закрытого и открытого ключа.
-   В Linux обычно используются сертификаты в формате `.key` и `.crt` (PEM).


## <span class="section-num">2</span> Преобразование pfx в key и crt {#преобразование-pfx-в-key-и-crt}

-   Используем утилиту _openssl_:
    ```shell
    openssl pkcs12 -in certificate.pfx -clcerts -nokeys -out certificate.crt
    ```
-   Нужно будет ввести пароль, который вы указывали при экспорте .pfx-сертификата.
-   Если при создании сертификата в формате `.pfx` были использованы устаревшие алгоритмы, то мы получим ошибки (подобную следующей):
    ```shell
    … error:0308010C:digital envelope routines:inner_evp_generic_fetch:unsupported … Algorithm (RC2-40-CBC : 0) …
    ```
-   Необходимо добавить флаг `-legacy`:
    ```shell
    openssl pkcs12 -in certificate.pfx -clcerts -nokeys -legacy -out certificate.crt
    ```
-   Извлечём закрытую часть сертификата:
    ```shell
    openssl pkcs12 -in certificate.pfx -nocerts -out key-encrypted.key
    ```
-   Необходимо ввести пароль, который использовался для экспорта .pfx-сертификата.
-   Также желательно задать пароль для `.key`-файла.
    -   Второй пароль можете и не вводить, но лучше зашифровать ключ.
    -   Закрытый ключ сертификата с парольной защитой не всегда удобно использовать для запуска демонов.
-   Можно удалить пароль закрытого ключа:
    ```shell
    openssl rsa -in key-encrypted.key -out key-decrypted.key
    ```


## <span class="section-num">3</span> Преобразование key и crt в pfx {#преобразование-key-и-crt-в-pfx}

-   Объединим `crt` и `key` в `pfx`:
    ```shell
    openssl pkcs12 -inkey certificate.key -in certificate.crt -export -out certificate.pfx
    ```
-   Нужно будет ввести пароль от файла закрытого ключа (если этот пароль есть) и пароль для экспорта в pfx.
