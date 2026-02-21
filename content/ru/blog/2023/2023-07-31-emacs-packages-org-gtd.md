---
title: "Emacs. Пакеты. Org-gtd"
author: ["Dmitry S. Kulyabov"]
date: 2023-07-31T18:24:00+03:00
lastmod: 2026-02-04T14:49:00+03:00
tags: ["emacs", "gtd"]
categories: ["computer-science"]
draft: false
slug: "emacs-packages-org-gtd"
---

Реализация метода GTD на основе Emacs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/Trevoke/org-gtd.el>
-   Пакет пытается максимально точно воспроизвести рабочий процесс GTD (см. [Метод GTD]({{< relref "2021-07-12-gtd-method" >}})).

<!--listend-->

```mermaid
graph TD
    STUFF["STUFF"]
    INBOX[INBOX]
    A{What is it?}
    B{Is it Actionable?}
    Trash[Trash]
    Someday[Someday/Maybe]
    Reference[Reference]
    Projects[Projects]
    Planning[Planning]
    C{What's the NEXT Action?}
    DO[DO IT]
    Waiting[Waiting For]
    NextActions[Next Actions]
    Calendar[Calendar]

    STUFF --> INBOX
    INBOX --> A
    A --> B


    B -- NO --> Trash
    B -- NO --> Someday
    B -- NO --> Reference

    B -- YES --> C

    C -- "Less than 2 minutes" --> DO

    C -- Delegate --> Waiting

    C -- "ASAP" --> NextActions
    C -- "Specific Date or Time" --> Calendar


    B -- "YES (multi-step)" --> Projects
    Projects --> Planning
    Planning --> C

```


## <span class="section-num">2</span> Режимы {#режимы}

-   `org-gtd-mode`: обновляет представления повестки дня, включать все файлы `org-gtd` в `org-agenda-files`.


## <span class="section-num">3</span> Настраиваемые переменные {#настраиваемые-переменные}

-   `org-gtd-directory`: каталог, в котором `org-gtd` будет искать свои файлы.
-   `org-gtd-areas-of-focus`: список строк, представляющих Horizon 3.


## <span class="section-num">4</span> Функции пакета по шагам GTD {#функции-пакета-по-шагам-gtd}


### <span class="section-num">4.1</span> Шаг 1/6: Захват {#шаг-1-6-захват}

-   Функции:
    -   `org-gtd-capture`: обёртка вокруг `org-capture`. Можно использовать для сбора в Inbox.
-   Настраиваемые переменные:
    -   `org-gtd-capture-templates`: шаблоны для `org-gtd-capture`.


### <span class="section-num">4.2</span> Шаг 2/6: Процесс {#шаг-2-6-процесс}

-   Функции:
    -   `org-gtd-process-inbox`: обработать все элементы в Inbox.


### <span class="section-num">4.3</span> Шаг 3/6: Уточнение {#шаг-3-6-уточнение}

-   Функции:
    -   `org-gtd-clarify-item`: определить, для чего элемент из Inbox в рамках `org-gtd`.
    -   `org-gtd-clarify-agenda-item`: организовать пункта повестки дня в рамках `org-gtd`.
    -   `org-gtd-clarify-switch-to-buffer`: вернуться к любому существующему буферу уточнения, используйте вместо переключения обратно в обычный поток.
-   Клавиатура:
    -   `org-gtd-clarify-map`: клавиатурные комбинации в буфере уточнения.


### <span class="section-num">4.4</span> Шаг 4/6: Организуйте {#шаг-4-6-организуйте}

-   Функции:
    -   `org-gtd-organize`: всплывающее меню с вопросом, как организовать (например, отдельное действие, встречу и т. д.) элемент в данный момент.
-   Хуки:
    -   `org-gtd-organize-hooks`: ряд функций, которые вызываются для оформления каждого элемента (например, тегов организации и т. д.).


### <span class="section-num">4.5</span> Шаг 5/6: Ежедневное взаимодействие {#шаг-5-6-ежедневное-взаимодействие}

-   Функции:
    -   `org-gtd-engage`: ежедневный просмотр.
    -   `org-gtd-engage-grouped-by-context`: все действия NEXT, сгруппированные по тегам, начинающимся с @. Это может не сработать, если вы удалите `org-set-tags-command` из `org-gtd-organize-hooks`.


### <span class="section-num">4.6</span> Шаг 6/6: Обзор {#шаг-6-6-обзор}

-   Функции:
    -   `org-gtd-oops`: Показать все пропущенные встречи.
    -   `org-gtd-review-area-of-focus`: показать представление повестки дня, предназначенное для одной из ваших областей деятельности.
    -   `org-gtd-review-stuck-*`: найти любой из типов деятельности, которые остались незамеченными.
