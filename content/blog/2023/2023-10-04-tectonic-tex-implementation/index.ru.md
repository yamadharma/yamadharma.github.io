---
title: "Tectonic Typesetting System как реализация TeX"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-04T12:44:00+03:00
lastmod: 2024-01-13T18:24:00+03:00
tags: ["tex"]
categories: ["computer-science"]
draft: false
slug: "tectonic-tex-implementation"
---

Tectonic Typesetting System как реализация TeX.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://tectonic-typesetting.github.io/>
-   Репозиторий: <https://github.com/tectonic-typesetting/tectonic>
-   Документация: <https://tectonic-typesetting.github.io/book/>
-   Реализована на Rust.
-   За основу взят XeTeX.
-   Пакетная база из TeXLive.
-   Лицензия: MIT License.


## <span class="section-num">2</span> Особенности {#особенности}

-   Автоматически загружает необходимые пакеты.
-   Программа командной строки `tectonic` выполняет полный цикл компиляции, с использованием Bibtex.
-   Предварительно созданные пакеты вспомогательных файлов взяты из TeXLive и размещены на JFrog Bintray.


## <span class="section-num">3</span> Недоработки {#недоработки}

-   Не поддерживается biblatex.
