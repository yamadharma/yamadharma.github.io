---
title: "Emacs. Поддержка LanguageTool"
author: ["Dmitry S. Kulyabov"]
date: 2022-05-19T19:45:00+03:00
lastmod: 2025-07-09T21:08:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-languagetool-support"
---

Реализация для _Emacs_ интерфейса к _LanguageTool_ (см. [LanguageTool]({{< relref "2022-05-19-languagetool" >}})).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> flycheck-languagetool {#flycheck-languagetool}

-   Поддержка LanguageTool на основе Flycheck.
-   Репозиторий: <https://github.com/emacs-languagetool/flycheck-languagetool>.
-   Поддерживает интерфейс http-сервера:
    -   Использует только `languagetool-server.jar`.


## <span class="section-num">2</span> Emacs-langtool {#emacs-langtool}

-   Репозиторий: <https://github.com/mhayashi1120/Emacs-langtool>.
-   Поддерживает следующие интерфейсы.
    -   Интерфейс коммандной строки:
        -   конкретный java-файл: `languagetool-commandline.jar`;
        -   путь, где расположены библиотеки;
        -   скрипт запуска _langtool_ (для Gentoo).
    -   Интерфейс http-сервера:
        -   конкретный java-файл: `languagetool-server.jar`.
    -   Интерфейс http-клиента:
        -   указывается адрес и порт сервера.


## <span class="section-num">3</span> languagetool.el {#languagetool-dot-el}

-   Репозиторий: <https://github.com/PillFall/languagetool.el>.
-   Поддерживает следующие интерфейсы.
    -   Интерфейс коммандной строки:
        -   конкретный java-файл: `languagetool-commandline.jar`;
        -   путь, где расположены библиотеки + имена конкретных классов;
        -   скрипт запуска _langtool_.
    -   Интерфейс http-сервера:
        -   конкретный java-файл: `languagetool-server.jar`.
    -   LanguageTool api (платная подписка).
