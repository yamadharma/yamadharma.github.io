---
title: "Emacs. Пакет org-daily-reflection"
author: ["Dmitry S. Kulyabov"]
date: 2025-06-06T20:48:00+03:00
lastmod: 2025-06-08T19:31:00+03:00
tags: ["org-roam", "emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-org-daily-reflection"
---

Emacs. Пакет org-daily-reflection.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/emacsomancer/org-daily-reflection>
-   Можно использовать с Org-roam daily (см. [Org-roam. Daily notes]({{< relref "2025-06-08--org-roam-daily-notes" >}}))


## <span class="section-num">2</span> Ограничения {#ограничения}

-   Одна из проблем заключается в том, что предполагается, что все записи журнала находятся в каталоге, указанном в `org-daily-reflection-dailies-directory` и названы &lt;YYYY-MM-DD&gt;.org (например, 2024-08-01.org).


## <span class="section-num">3</span> Использование {#использование}


### <span class="section-num">3.1</span> Сравнение записей за разные периоды {#сравнение-записей-за-разные-периоды}

-   Команда `org-daily-reflection` запрашивает временной интервал (например, `year`) и целочисленный диапазон (например, `3`).
-   При неинтерактивном вызове: `(org-daily-reflection 'year 3)`.
-   Сравнивается этот день с предыдущими тремя годами.
-   Несколько примеров одноразовых функций с префиксом `org-reflect-on-last-`:
    -   `org-reflect-on-last-five-days` : предыдущие пять дней ежедневных записей.


### <span class="section-num">3.2</span> Интерактивный интерфейс {#интерактивный-интерфейс}

-   `org-daily-reflection-layout-toggle` : восстанавливает макет окна (предназначено для переключения вперед и назад).
-   `org-daily-reflection-restore-prior-windows` : восстанавливает конфигурацию окна.
-   `org-daily-reflection-close-unmodified-newly-opened-buffers` (по умолчанию `nil`) : следует ли закрывать ежедневные журналы, которые ранее не были открыты (и не были изменены) при вызове `org-daily-reflection-restore-prior-windows`.
-   Окна можно закрыть независимо от настроек с помощью интерактивной команды `org-daily-reflection-close-reflection-newly-opened`.
-   `org-daily-reflection--reflect` : выдаёт предыдущее n-ное количество ежедневных записей.
-   `org-daily-reflection` (обёртка вокруг `org-daily-reflection--reflect`) : принимает список точечных пар в форме `(('day . 3) ('month 4) ('year . 2))` (будут показывать 3 дня, предшествующих текущей записи в журнале, с предшествующими ежедневниками за 4 месяца до этого, с предшествующими ежедневниками за 2 года до самого раннего из ежемесячных ежедневников).
