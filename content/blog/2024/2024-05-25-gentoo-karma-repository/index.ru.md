---
title: "Gentoo. Репозиторий karma"
author: ["Dmitry S. Kulyabov"]
date: 2024-05-25T20:52:00+03:00
lastmod: 2024-05-25T21:07:00+03:00
draft: false
slug: "gentoo-karma-repository"
---

Репозиторий karma.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


### <span class="section-num">1.1</span> Karma {#karma}

-   Репозиторий: <https://github.com/yamadharma/karma>


### <span class="section-num">1.2</span> Karma-profiles {#karma-profiles}


## <span class="section-num">2</span> Установка {#установка}

-   Добавьте репозиторий `karma`:
    ```shell
    eselect repository add karma git https://github.com/yamadharma/karma.git
    emaint sync -r karma
    ```
-   Добавьте репозиторий `karma-profiles`:
    ```shell
    eselect repository add karma-profiles git https://github.com/yamadharma/karma-profiles.git
    emaint sync -r karma-profiles
    ```
