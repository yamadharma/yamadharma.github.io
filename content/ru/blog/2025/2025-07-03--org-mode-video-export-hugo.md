---
title: "Org-mode. Экспорт ссылок на видео в Hugo"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-03T20:30:00+03:00
lastmod: 2025-07-04T18:06:00+03:00
tags: ["emacs", "org-mode", "hugo"]
categories: ["computer-science"]
draft: false
slug: "org-mode-video-export-hugo"
---

Org-mode. Экспорт ссылок на видео в Hugo

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Прагматика {#прагматика}

-   Нужно экспортировать ссылки на видео не только в Hugo, но и в Markdown.
    -   Неудобно прописывать это дважды.
-   Синтаксис видео во вкладках (см. [Hugo. Видео во вкладках]({{< relref "2022-06-26-hugo-video-tabs" >}})) не зафиксирован.
    -   Пришлось переписывать все низкоуровневые вызовы при смене синтаксиса.
    -   Хотелось бы зафиксировать форму записи.
-   Решение: использование макросов org-mode (см. [Org-mode. Макросы]({{< relref "2025-06-08--org-mode-macro" >}})).
-   Будем использовать синтаксис от вкладок jQuery (см. [Hugo. Вкладки jquery]({{< relref "2025-07-03--hugo-tabbed-view-jquery" >}})).


## <span class="section-num">2</span> Экспорт видео. Решение 1 {#экспорт-видео-dot-решение-1}

-   Нужно экспортировать видео и в hugo, и в markdown.
-   Сделал следующие макросы:
    ```org
    #+macro: youtube @@hugo:{{</* youtube $1 */>}}@@@@md:[![Youtube](http://img.youtube.com/vi/$1/0.jpg){width=560px}](http://www.youtube.com/watch?v=$1)@@
    #+macro: rutube @@hugo:{{</* rutube $1 */>}}@@@@markdown:[![RuTube]($2){width=560px}](https://rutube.ru/video/$1/)@@
    #+macro: plvideo @@hugo:{{</* plvideo $1 */>}}@@@@markdown:[![Платформа]($2){width=560px}](https://plvideo.ru/watch?v=$1)@@
    ```
-   Проблема: в hugo экспортируется и markdown.
-   Получаем излишнюю информацию при экспорте в hugo.


## <span class="section-num">3</span> Экспорт видео. Решение 2 {#экспорт-видео-dot-решение-2}

-   Используем подход с вычислением выражения на elisp:
    ```org
    #+macro: youtube (eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat "@@hugo:{{</* youtube " $1 " */>}}@@")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat "@@html:[![Youtube](http://img.youtube.com/vi/" $1 "/0.jpg){width=560px}](http://www.youtube.com/watch?v=" $1 ")@@"))))
    #+macro: rutube (eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat "@@hugo:{{</* rutube " $1 " */>}}@@")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat "@@html:[![RuTube](" $2 "){width=560px}](https://rutube.ru/video/" $1 "/)@@"))))
    #+macro: plvideo (eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat "@@hugo:{{</* plvideo " $1 " */>}}@@")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat "@@html:[![Платформа](" $2 "){width=560px}](https://plvideo.ru/watch?v=" $1 ")@@"))))
    #+macro: vkvideo (eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat "@@hugo:{{</* vkvideo oid=" $1 " id=" $2 " hd=2 */>}}@@")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat "@@html:[![VKvideo](" $3 "){width=560px}](https://vkvideo.ru/video" $1 "_" $2 ")@@"))))
    ```
-   Здесь используются сокращения для видео:
    -   [Hugo shortcode. Видео на VK Video]({{< relref "2023-08-24-hugo-shortcode-vkvideo" >}})
    -   [Сокращение для видео Rutube для Hugo]({{< relref "2022-04-04-shortcode-video-rutube-hugo" >}})
    -   [Сокращение для видео Платформа для Hugo]({{< relref "2024-11-09-shortcode-video-plvideo-hugo" >}})


## <span class="section-num">4</span> Поддержка вкладок {#поддержка-вкладок}

-   Добавим макросы для поддержки вкладок:
    ```org
    #+macro: begin_tabs @@hugo:{{</* tabs $1 */>}}@@
    #+macro: end_tabs @@hugo:{{</* /tabs */>}}@@
    #+macro: youtube-tab @@hugo:{{</* tab "Youtube" */>}}@@{{{youtube($1)}}}@@hugo:{{</* /tab */>}}@@
    #+macro: rutube-tab @@hugo:{{</* tab "RuTube" */>}}@@{{{rutube($1,$2)}}}@@hugo:{{</* /tab */>}}@@
    #+macro: plvideo-tab @@hugo:{{</* tab "Платформа" */>}}@@{{{plvideo($1,$2)}}}@@hugo:{{</* /tab */>}}@@
    #+macro: vkvideo-tab @@hugo:{{</* tab "VKvideo" */>}}@@{{{vkvideo($1,$2,$3)}}}@@hugo:{{</* /tab */>}}@@
    ```


## <span class="section-num">5</span> Использование {#использование}

-   Предполагается следующий сценарий использования (использовал видео, на которых отлаживал код):
    ```org
    {{{begin_tabs("Создание виртуальной машины с Virtualbox")}}}

    {{{rutube-tab(0a52857a1fb8a79cbf58fcb58d2d8593,https://pic.rutubelist.ru/video/2025-07-02/63/b4/63b485f63c7a400611064eb35be3ffa1.jpg)}}}

    {{{plvideo-tab(Dncja2upfmNQ,https://s-dt-rt1.cloud.edgecore.ru/fp-2025-07-cover/Dncja2upfmNQ/f91849ab-8ad2-4795-9fce-3525054e4bce.jpg)}}}

    {{{vkvideo-tab(-230024722,456239038,https://sun1-18.userapi.com/QhNtwM8UkVfXj44arwC4cvAW9XTPzBQiboJaPA/ZvwM3lG9Da4.jpg)}}}

    {{{youtube-tab(WwYYYIQdUTk)}}}

    {{{end_tabs}}}
    ```

{{< tabs "Создание виртуальной машины с Virtualbox" >}}

{{< tab "RuTube" >}}{{< rutube 0a52857a1fb8a79cbf58fcb58d2d8593 >}}{{< /tab >}}

{{< tab "Платформа" >}}{{< plvideo Dncja2upfmNQ >}}{{< /tab >}}

{{< tab "VKvideo" >}}{{< vkvideo oid=-230024722 id=456239038 hd=2 >}}{{< /tab >}}

{{< tab "Youtube" >}}{{< youtube WwYYYIQdUTk >}}{{< /tab >}}

{{< /tabs >}}


## <span class="section-num">6</span> Загрузка при старте emacs {#загрузка-при-старте-emacs}

-   Будем загружать эти макросы при старте emacs:
    ```emacs-lisp
    (setq org-export-global-macros
          '(
            ("youtube" . "(eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat \"@@hugo:{{</* youtube \" $1 \" */>}}@@\")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat \"@@html:[![Youtube](http://img.youtube.com/vi/\" $1 \"/0.jpg){width=560px}](http://www.youtube.com/watch?v=\" $1 \")@@\"))))")
            ("rutube" . "(eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat \"@@hugo:{{</* rutube \" $1 \" */>}}@@\")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat \"@@html:[![RuTube](\" $2 \"){width=560px}](https://rutube.ru/video/\" $1 \"/)@@\"))))")
            ("plvideo" . "(eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat \"@@hugo:{{</* plvideo \" $1 \" */>}}@@\")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat \"@@html:[![Платформа](\" $2 \"){width=560px}](https://plvideo.ru/watch?v=\" $1 \")@@\"))))")
            ("vkvideo" . "(eval (cond ((org-export-derived-backend-p org-export-current-backend 'hugo) (concat \"@@hugo:{{</* vkvideo oid=\" $1 \" id=\" $2 \" hd=2 */>}}@@\")) ((org-export-derived-backend-p org-export-current-backend (or 'md 'markdown 'gfm)) (concat \"@@html:[![VKvideo](\" $3 \"){width=560px}](https://vkvideo.ru/video\" $1 \"_\" $2 \")@@\"))))")
            ("begin_tabs" . "@@hugo:{{</* tabs $1 */>}}@@")
            ("end_tabs" . "@@hugo:{{</* /tabs */>}}@@")
            ("youtube-tab" . "@@hugo:{{</* tab \"Youtube\" */>}}@@{{{youtube($1)}}}@@hugo:{{</* /tab */>}}@@")
            ("rutube-tab" . "@@hugo:{{</* tab \"RuTube\" */>}}@@{{{rutube($1,$2)}}}@@hugo:{{</* /tab */>}}@@")
            ("plvideo-tab" . "@@hugo:{{</* tab \"Платформа\" */>}}@@{{{plvideo($1,$2)}}}@@hugo:{{</* /tab */>}}@@")
            ("vkvideo-tab" . "@@hugo:{{</* tab \"VKvideo\" */>}}@@{{{vkvideo($1,$2,$3)}}}@@hugo:{{</* /tab */>}}@@")))
    ```
