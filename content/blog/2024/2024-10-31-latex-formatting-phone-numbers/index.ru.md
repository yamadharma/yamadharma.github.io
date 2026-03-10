---
title: "LaTeX. Форматирование телефонных номеров"
author: ["Dmitry S. Kulyabov"]
date: 2024-10-31T15:59:00+03:00
lastmod: 2024-10-31T16:22:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex-formatting-phone-numbers"
---

Форматирование телефонных номеров.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   На данный момент ничего общего для форматирования телефонных номеров нет.
-   Есть несколько пакетов, но применимость их весьма ограничена.
-   Всё необходимо делать вручную.


### <span class="section-num">1.1</span> Стандарты {#стандарты}

-   [E.123 : Notation for national and international telephone numbers, e-mail addresses and web addresses](https://www.itu.int/rec/T-REC-E.123-200102-I/e)


## <span class="section-num">2</span> Пакеты {#пакеты}


### <span class="section-num">2.1</span> telprint {#telprint}

-   CTAN: <http://www.ctan.org/pkg/telprint>
-   Репозиторий: <https://github.com/ho-tex/telprint>
-   Рассчитан на немецкий формат телефонных номеров.
-   Добавляет в телефонный номер правильные шпации.


### <span class="section-num">2.2</span> phonenumbers {#phonenumbers}

-   CTAN: <https://ctan.org/pkg/phonenumbers>
-   Репозиторий: <https://github.com/wehro/phonenumbers>
-   Скорее фреймворк, чем готовый пакет.
-   Позволяет форматировать телефонные номера в соответствии с различными национальными соглашениями.
-   В настоящее время поддерживаются немецкие, французские и североамериканские телефонные номера.
-   Телефонные номера из других стран поддерживаются лишь в элементарном виде.
-   Преобразует номер телефона в гиперссылку.
