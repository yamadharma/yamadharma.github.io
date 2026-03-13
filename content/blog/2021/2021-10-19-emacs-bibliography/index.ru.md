---
title: "Emacs. Работа с библиографией"
author: ["Dmitry S. Kulyabov"]
date: 2021-10-19T14:21:00+03:00
lastmod: 2023-07-18T19:57:00+03:00
tags: ["bib", "emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-bibliography"
---

Работа с библиографией в Emacs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Основные пакеты для работы с библиографическими данными {#основные-пакеты-для-работы-с-библиографическими-данными}


### <span class="section-num">1.1</span> Управление библиографической базой {#управление-библиографической-базой}


#### <span class="section-num">1.1.1</span> Ebib {#ebib}

-   `ebib`: предоставляет инструмент для редактирования самих файлов `.bib`.
-   [Emacs. Менеджер библиографической информации Ebib]({{< relref "2021-09-14-emacs-ebib-bibliography-manager" >}})


### <span class="section-num">1.2</span> Управление ссылками {#управление-ссылками}


#### <span class="section-num">1.2.1</span> Helm-bibtex {#helm-bibtex}

-   `helm-bibtex`: инструмент для просмотра и манипуляции записями в файлах `.bib`.
-   [Emacs. Работа с библиографией. helm-bibtex]({{< relref "2022-08-30-emacs-bibliography-helm-bibtex" >}})
-   Позволяет вставлять ссылки в файл.
-   Используется чаще всего как фронтенд для вставки ссылок.
-   Можно управлять базой библиографических данных, выполняя с ней разные действия.


#### <span class="section-num">1.2.2</span> Org-ref {#org-ref}

-   `org-ref`: система управления ссылками, тесно интегрированная с `org-mode`.
-   [Emacs. Работа с библиографией. org-ref]({{< relref "2022-08-30-emacs-bibliography-org-ref" >}})
-   Можно:
    -   редактировать файлы `bibtex`;
    -   вставлять цитаты;
    -   искать и загружать PDF-файлы для ссылок;
    -   вставлять библиографические данные.


#### <span class="section-num">1.2.3</span> Org Roam BibTeX {#org-roam-bibtex}

-   Расширение Org Roam, которое интегрирует Org Roam с программным обеспечением для управления библиографией/цитированием: Org Ref, Helm и Ivy BibTeX и Citar.
-   [Emacs. Работа с библиографией. Org-roam-bibtex]({{< relref "2022-08-30-emacs-bibliography-org-roam-bibtex" >}})


#### <span class="section-num">1.2.4</span> Org-cite {#org-cite}

-   [Emacs. Работа с библиографией. Org-cite]({{< relref "2022-10-10-emacs-bibliography-org-cite" >}})
-   Для цитирования в org-mode.
-   Задаёт формат ссылок.
-   Лучше использовать как бэкенд.
