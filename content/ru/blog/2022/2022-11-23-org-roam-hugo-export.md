---
title: "Org-roam. Экспорт в Hugo"
author: ["Dmitry S. Kulyabov"]
date: 2022-11-23T19:40:00+03:00
lastmod: 2023-07-15T20:53:00+03:00
tags: ["hugo", "org-mode", "org-roam"]
categories: ["computer-science"]
draft: false
slug: "org-roam-hugo-export"
---

Экспорт в Hugo из org-roam.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Ошибки при экспорте {#ошибки-при-экспорте}


### <span class="section-num">1.1</span> ox-hugo: broken links {#ox-hugo-broken-links}


#### <span class="section-num">1.1.1</span> Подкаталоги в каталоге org-roam {#подкаталоги-в-каталоге-org-roam}

-   Если каталог для org-roam содержит подкаталоги, то при экспорте теряются ссылки.
-   Для ликвидации этой ошибки следует добавить в настройки:
    ```emacs-lisp
    (require 'org-roam-export)
    ```


#### <span class="section-num">1.1.2</span> Экспорт из поддерева {#экспорт-из-поддерева}

-   ox-hugo предлагает два варианта экспорта:
    -   экспорт всего файла;
    -   экспорт из поддерева.
-   При экспорте из поддерева ссылки типа `id_link` не отображаются.
-   Происходит поиск таких ссылок только в текущем поддереве.
-   Для реализации поиска в других фалах нужно добавить их в переменную `org-id-extra-files`:
    ```emacs-lisp
    (setq org-id-extra-files (directory-files-recursively org-roam-directory ".*\.org$" t))
    ```

    -   Впрочем, у меня это не сработало.
-   Также можно сделать хак для игнорирования ошибок:
    ```emacs-lisp
    (with-eval-after-load 'ox-hugo
      (setq org-hugo--preprocess-buffer nil))
    ```

    -   Вот это у меня сработало.
