---
title: "Hugo. Вкладки bootstrap"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-03T19:23:00+03:00
lastmod: 2025-07-03T20:33:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "hugo-tabbed-view-bootstrap"
---

Hugo. Вкладки bootstrap.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Используем наработки из темы _Hugo Dynamic Tabs_. Реализация на основе _Bootstrap_.


## <span class="section-num">2</span> Тема _Hugo Dynamic Tabs_ {#тема-hugo-dynamic-tabs}

-   Сайт: <https://hugo-dynamic-tabs.netlify.app/>.
-   Репозиторий:
    -   Bootstrap 4: <https://github.com/rvanhorn/hugo-dynamic-tabs>;
    -   Bootstrap 5: <https://github.com/rvanhorn/hugo-dynamic-tabs/tree/bootstrap5>.
-   Тема использует библиотеки _Bootstrap 4_ или _Bootstrap 5_.
-   Темы _Wowchemy_ используют _Bootstrap 4_. Поэтому дополнительных библиотек не нужно.
-   Достаточно поместить файлы `tab.html` и `tabs.html` в каталог сайта `layouts/shortcodes`.


### <span class="section-num">2.1</span> Листинги файлов {#листинги-файлов}

-   Файл `tabs.html` (bootstrap 4):
    ```html
    <nav>
                <div class="nav nav-tabs" id="nav-tab" role="tablist">

                        {{ $tabTotal := .Get "tabTotal" }} {{ $tabRightAlign
                        := .Get "tabRightAlign" }} {{ $tabName := .Scratch.Get
                        "tabName" }} {{ $tabID := .Scratch.Get "tabID" }}

                        {{ range $i, $sequence := (seq $tabTotal) }}

                        <a class="nav-item nav-link {{ if eq $i 0 }} active {{
                           end }}{{ if in $tabRightAlign (add 1 $i) }} ml-auto
                           {{ end }}" id="nav-{{ (index $tabID $i) }}"
                           data-toggle="tab" href="#{{ (index $tabID $i) }}"
                           role="tab" aria-controls="nav-home"
                           aria-selected="true">{{ (replaceRE "(\\s)" ""
                           (index $tabName $i)) }}</a>

                        {{ end }}

                </div>
    </nav>

    <div class="tab-content" id="nav-tab-content">

                {{ .Inner }}

    </div>
    ```

-   Файл `tabs.html` (bootstrap 5):
    ```html
    <nav>
                <div class="nav nav-tabs" id="nav-tab" role="tablist">

                        {{ $tabTotal := .Get "tabTotal" }}
                        {{ $tabRightAlign := .Get "tabRightAlign" }}
                        {{ $tabName := .Scratch.Get "tabName" }}
                        {{ $tabID := .Scratch.Get "tabID" }}

                        {{ range $i, $sequence := (seq $tabTotal) }}

                        <a class="nav-link {{ if eq $i 0 }} active {{ end }}{{ if in $tabRightAlign (add 1 $i) }} ms-auto {{ end }}"
                           id="{{ (index $tabID $i) }}-tab" data-bs-toggle="tab" data-bs-target="#{{ (index $tabID $i) }}"
                           type="button" role="tab" aria-controls="nav-home" aria-selected="true">{{ (replaceRE "(\\s)" "" (index $tabName $i)) }}</a>

                        {{ end }}

                </div>
    </nav>

    <div class="tab-content" id="nav-tab-content">

                {{ .Inner }}

    </div>
    ```

-   Файл `tab.html`:
    ```html
    {{ $tabName := .Get "tabName" }}
    {{ $tabID := delimit (shuffle (slice "a" "b" "c" "d" "e" "f")) "" }}
    {{ .Parent.Scratch.Add "tabName" (slice $tabName) }}
    {{ .Parent.Scratch.Add "tabID" (slice $tabID) }}

    <div class="tab-pane fade show {{ if eq .Ordinal 0 }}active {{ end }}" id="{{ $tabID }}" role="tabpanel" aria-labelledby="nav-1">

            {{ $.Inner | markdownify }}

    </div>
    ```


### <span class="section-num">2.2</span> Использование {#использование}

-   Одна вкладка.
    -   Код:
        ```markdown
        {{</* tabs tabTotal="1" */>}}
        {{</* tab tabName="Tab 1" */>}}

        **Tab 1 Content**

        {{</* /tab */>}}
        {{</* /tabs */>}}
        ```
    -   Отображение:

        {{< tabs tabTotal="1" >}}
        {{< tab tabName="Tab 1" >}}

        **Tab 1 Content**

        {{< /tab >}}
        {{< /tabs >}}
-   Три вкладки. Две из них выровнены направо.
    -   Код:
        ```markdown
        {{</* tabs tabTotal="3" tabRightAlign="2" */>}}
        {{</* tab tabName="Tab 1" */>}}

        **Tab 1 Content**

        {{</* /tab */>}}
        {{</* tab tabName="Tab 2" */>}}

        **Tab 2 Content**

        {{</* /tab */>}}
        {{</* tab tabName="Tab 3" */>}}

        **Tab 3 Content**

        {{</* /tab */>}}
        {{</* /tabs */>}}
        ```
    -   Отображение:

        {{< tabs tabTotal="3" tabRightAlign="2" >}}
        {{< tab tabName="Tab 1" >}}

        **Tab 1 Content**

        {{< /tab >}}
        {{< tab tabName="Tab 2" >}}

        **Tab 2 Content**

        {{< /tab >}}
        {{< tab tabName="Tab 3" >}}

        **Tab 3 Content**

        {{< /tab >}}
        {{< /tabs >}}
