---
title: "Emacs. Работа с библиографией. Org-roam-bibtex"
author: ["Dmitry S. Kulyabov"]
date: 2022-08-30T15:13:00+03:00
lastmod: 2023-10-06T20:39:00+03:00
tags: ["bib", "emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-bibliography-org-roam-bibtex"
---

Пакет для работы с библиографией _org-roam-bibtex_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/org-roam/org-roam-bibtex>
-   Расширение Org Roam, которое интегрирует Org Roam с программным обеспечением для управления библиографией/цитированием: Org Ref, Helm и Ivy BibTeX и Citar.
-   Позволяет пользователям управлять своими библиографическими примечаниями с помощью Org Roam и получать доступ к примечаниям org-roam-directory через
    -   `helm-bibtex`;
    -   `ivy-bibtex`;
    -   `citar-open-notes`.
-   Использует ссылки Org-ref (`cite:`) и ссылки Org-cite.
