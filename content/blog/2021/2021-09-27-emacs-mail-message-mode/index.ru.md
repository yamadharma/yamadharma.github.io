---
title: "Emacs. Почта. Message-mode"
author: ["Dmitry S. Kulyabov"]
date: 2021-09-27T19:00:00+03:00
lastmod: 2025-07-09T21:06:00+03:00
tags: ["sysadmin", "emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-mail-message-mode"
---

Режим Emacs для создания писем.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}


## <span class="section-num">2</span> Приёмы работы {#приёмы-работы}


### <span class="section-num">2.1</span> Прикрепить несколько файлов {#прикрепить-несколько-файлов}

-   Откройте каталог в режиме `dired` с помощью `C-x 4 d`.
-   Введите `M-x turn-on-gnus-dired-mode`.
    -   Если у Вас `M-x` привязано к `helm`, то сделать это сразу не получится.
    -   Тогда Вам надо нажать на нужном каталоге `C-RET`, а потом уже ввести `M-x turn-on-gnus-dired-mode`.
-   Отметьте необходимые файлы с помощью `m`.
-   Введите `C-c RET C-a` для вставки в уже открытый буфер сообщений (или назначьте новый).
