---
title: "Hugo. Видео во вкладках"
author: ["Dmitry S. Kulyabov"]
date: 2022-06-26T18:46:00+03:00
lastmod: 2025-07-03T21:21:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "hugo-video-tabs"
---

Размещение видео во вкладках на сайте.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Прагматика {#прагматика}

-   Из-за проблем с _Youtube_ было принято решение размещать видео параллельно на _RuTube_.
-   Размещение видеофайлов последовательно выглядит несколько громоздко и несколько смущает пользователя.
-   Принято решение размещать видео с разных хостингов на вкладках.
-   Релизация строится на добавлении сокращений для вкладок (см. [Hugo. Вкладки]({{< relref "2022-06-26-hugo-tabbed-view" >}})).


## <span class="section-num">2</span> Вкладки bootstrap {#вкладки-bootstrap}


### <span class="section-num">2.1</span> Реализация {#реализация}

-   Релизация строится на добавлении сокращений для вкладок bootsrap (см. [Hugo. Вкладки bootstrap]({{< relref "2025-07-03--hugo-tabbed-view-bootstrap" >}})).
-   Проблема: При использовании сокращения `tab` отображается не видеоплеер, а код.
-   Причина: Код внутри сокращения обрабатывается как Markdown.
-   Путь решения: Нужно запретить обработку кода внутри сокращения.


#### <span class="section-num">2.1.1</span> Использовать стандартное поведение сокращения {#использовать-стандартное-поведение-сокращения}

-   Если после сокращения идёт непосредственно символ `<` (без пробела), то внутреннее содержание сокращения дальше не обрабатывается.
-   Предполагается, что там может быть html-код.
-   Возникшая проблема: первая вкладка отрабатывает ожидаемым образом, последующие же всё равно обрабатывают содержимое как Markdown.


#### <span class="section-num">2.1.2</span> Создание специального сокращения {#создание-специального-сокращения}

-   Вводится сокращение `rtab` (raw tab):

<!--listend-->

```html
{{ $tabName := .Get "tabName" }}
{{ $tabID := delimit (shuffle (slice "a" "b" "c" "d" "e" "f")) "" }}
{{ .Parent.Scratch.Add "tabName" (slice $tabName) }}
{{ .Parent.Scratch.Add "tabID" (slice $tabID) }}

<div class="tab-pane fade show {{ if eq .Ordinal 0 }}active {{ end }}" id="{{ $tabID }}" role="tabpanel" aria-labelledby="nav-1">

        {{ $.Inner }}

</div>
```

-   Здесь оригинальная конструкция
    ```html
    {{ $.Inner | markdownify }}
    ```
    заменена на
    ```html
    {{ $.Inner }}
    ```
-   Следует разместить этот файл в каталоге `layouts/shortcodes` сайта.


### <span class="section-num">2.2</span> Использование {#использование}

-   Код:
    ```markdown
    {{</* tabs tabTotal="2" */>}}
    {{</* rtab tabName="Rutube" */>}}

    {{</* rutube 1bea1bcf9215678e8ccf797187cc52fd */>}}

    {{</* /rtab */>}}
    {{</* rtab tabName="VKvideo" */>}}

    {{</* vkvideo oid="606414976" id="456239113" hd="2" */>}}

    {{</* /rtab */>}}
    {{</* rtab tabName="Youtube" */>}}

    {{</* youtube ysEdxhyYl8k */>}}

    {{</* /rtab */>}}
    {{</* /tabs */>}}
    ```
-   Отображение:

    {{< tabs tabTotal="3" >}}
    {{< rtab tabName="Rutube" >}}

    {{< rutube 1bea1bcf9215678e8ccf797187cc52fd >}}

    {{< /rtab >}}
    {{< rtab tabName="VKvideo" >}}

    {{< vkvideo oid="606414976" id="456239113" hd="2" >}}

    {{< /rtab >}}
    {{< rtab tabName="Youtube" >}}

    {{< youtube ysEdxhyYl8k >}}

    {{< /rtab >}}
    {{< /tabs >}}


## <span class="section-num">3</span> Вкладки jQuery {#вкладки-jquery}


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   Из-за перехода с Bootstrap на Tailwind пришлось сменить реализацию вкладок.
-   Использовал вкладки jQuery (см. [Hugo. Вкладки jquery]({{< relref "2025-07-03--hugo-tabbed-view-jquery" >}})).


### <span class="section-num">3.2</span> Использование {#использование}

-   Используется следующим образом:
    ```markdown
    {{</* tabs "Создание виртуальной машины с Virtualbox" */>}}

    {{</* tab "RuTube" */>}}
    {{</* rutube 0a52857a1fb8a79cbf58fcb58d2d8593 */>}}
    {{</* /tab */>}}

    {{</* tab "Платформа" */>}}
    {{</* plvideo Dncja2upfmNQ */>}}
    {{</* /tab */>}}

    {{</* tab "VKvideo" */>}}
    {{</* vkvideo oid=-230024722 id=456239038 hd=2 */>}}
    {{</* /tab */>}}

    {{</* tab "Youtube" */>}}
    {{</* youtube WwYYYIQdUTk */>}}
    {{</* /tab */>}}

    {{</* /tabs */>}}
    ```
-   Здесь используются сокращения для видео:
    -   [Hugo shortcode. Видео на VK Video]({{< relref "2023-08-24-hugo-shortcode-vkvideo" >}})
    -   [Сокращение для видео Rutube для Hugo]({{< relref "2022-04-04-shortcode-video-rutube-hugo" >}})
    -   [Сокращение для видео Платформа для Hugo]({{< relref "2024-11-09-shortcode-video-plvideo-hugo" >}})


### <span class="section-num">3.3</span> Оптимизация использования {#оптимизация-использования}

-   [Org-mode. Экспорт ссылок на видео в Hugo]({{< relref "2025-07-03--org-mode-video-export-hugo" >}})
