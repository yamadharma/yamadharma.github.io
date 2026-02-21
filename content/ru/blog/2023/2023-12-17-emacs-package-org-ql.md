---
title: "Emacs. Пакет org-ql"
author: ["Dmitry S. Kulyabov"]
date: 2023-12-17T19:45:00+03:00
lastmod: 2023-12-17T19:51:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-package-org-ql"
---

Инструмент поиска для org-mode.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/alphapapa/org-ql>
-   Предоставляет язык запросов для файлов `org`.
-   Два стиля синтаксиса:
    -   стиль Лиспа (s-expressions, sexps);
    -   ключевые слова в стиле поисковых систем.
-   Три библиотеки:
    -   `org-ql`: используется в качестве серверной части для других инструментов;
    -   `org-ql-search`: команды интерактивного поиска и сохраненные представления;
    -   `helm-org-ql`: для взаимодействия на основе Helm (см. [Emacs. Автодополнение. Helm]({{< relref "2022-12-14-emacs-completion-helm" >}})).
