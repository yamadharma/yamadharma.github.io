---
title: "Gentoo. Создание ebuild для Rust"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-02T19:06:00+03:00
lastmod: 2024-11-02T19:14:00+03:00
tags: ["linux", "gentoo", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "gentoo-ebuild-rust"
---

Gentoo. Создание ebuild для программ на Rust.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> pycargoebuild {#pycargoebuild}


### <span class="section-num">1.1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/projg2/pycargoebuild/>
-   Генератор ebuild с использованием инфраструктуры Cargo.
-   Установка:
    ```shell
    emerge app-portage/pycargoebuild
    ```


### <span class="section-num">1.2</span> Использование {#использование}

-   Создать новый ebuild:
    ```shell
    pycargoebuild <package-directory>
    ```

    -   _package-directory_ : каталог, содержащий `Cargo.toml`.
    -   Создаётся файл ebuild в текущем каталоге.
-   Обновить существующий ebuild:
    ```shell
    pycargoebuild -i <current-file>.ebuild <package-directory>
    ```
