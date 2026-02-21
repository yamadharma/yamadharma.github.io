---
title: "Gentoo. Создание ebuild для python"
author: ["Dmitry S. Kulyabov"]
date: 2025-11-22T17:53:00+03:00
lastmod: 2025-11-22T18:16:00+03:00
tags: ["gentoo", "linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "gentoo-create-ebuild-python"
---

Gentoo. Создание ebuild для python.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Pyproject2ebuild {#pyproject2ebuild}


### <span class="section-num">1.1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://gitlab.com/oz123/pyproject2ebuild>
-   Инструмент для автоматического преобразования метаданных Python pyproject.toml в файлы ebuild Gentoo.
-   Может открыть локальный файл pyproject.toml или загрузить его автоматически.
-   Анализирует название проекта, версию, описание, лицензию, домашнюю страницу.
-   Преобразует зависимости Python в синтаксис зависимостей Gentoo.
-   Автоматически генерировать metadata.xml.


### <span class="section-num">1.2</span> Установка {#установка}

-   В репозитории guru ([Gentoo. Дополнительные репозитории]({{< relref "2023-10-01-gentoo-additional-repositories" >}})):
    ```shell
    emerge dev-python/pyproject2ebuild
    ```
-   Для работы потребует конфигурационный файл (даже пустой):
    ```shell
    touch ~/.config/pyproject2ebuild.toml
    ```


### <span class="section-num">1.3</span> Использование {#использование}

-   Пример вызова:
    ```shell
    pyproject2ebuild https://raw.githubusercontent.com/pyupio/safety/refs/heads/main/pyproject.toml
    ```
-   Ссылка на исходные коды в ebuild не помещается.
