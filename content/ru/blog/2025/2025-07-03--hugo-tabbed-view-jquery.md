---
title: "Hugo. Вкладки jquery"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-03T19:47:00+03:00
lastmod: 2025-07-03T20:32:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "hugo-tabbed-view-jquery"
---

Hugo. Вкладки jquery.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сделал на основе сокращения <https://yairgadelov.me/simple-tab-widget-for-hugo-blog/>.
-   Сокращение базируется на JQuery Tab widget (<https://www.tutorialspoint.com/jquery/widget-tab.htm>)


## <span class="section-num">2</span> Код {#код}


### <span class="section-num">2.1</span> `tabs` {#tabs}

```html
{{ $title := "tabe widget" }}
{{ if .IsNamedParams }}
  {{ with .Get "title" }}
    {{ $title = . }}
  {{ end }}
{{ else }}
  {{ with .Get 0 }}
    {{ $title = . }}
  {{ end }}
{{ end }}

<!-- <link rel = "stylesheet" -->
<!--       href = "https://code.jquery.com/ui/1.14.1/themes/flick/jquery-ui.css"> -->

{{ $css := resources.Get "css/flick/jquery-ui.css" }}
{{ $styles := $css | toCSS | minify | fingerprint }}
<link rel="stylesheet" href="{{ $styles.RelPermalink }}" integrity="{{ $styles.Data.Integrity }}">

<script type = "text/javascript" src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js">
</script>

<script type = "text/javascript" src = "https://ajax.googleapis.com/ajax/libs/jqueryui/1.14.1/jquery-ui.min.js">
</script>

<!-- {{ $js := resources.Get "js/jquery.min.js" | js.Build | minify | fingerprint }} -->
<!-- <script -->
<!--   src="{{ $js.RelPermalink }}" -->
<!--   integrity="{{ $js.Data.Integrity }}" -->
<!--   defer -->
<!-- ></script> -->

<!-- {{ $js := resources.Get "js/jquery-ui.min.js" | js.Build | minify | fingerprint }} -->
<!-- <script -->
<!--   src="{{ $js.RelPermalink }}" -->
<!--   integrity="{{ $js.Data.Integrity }}" -->
<!--   defer -->
<!-- ></script> -->

<!-- {{ $js := resources.Get "js/jquery.min.js" | js.Build }} -->
<!-- <script -->
<!--   src="{{ $js.RelPermalink }}" -->
<!--   defer -->
<!-- ></script> -->

<!-- {{ $js := resources.Get "js/jquery-ui.min.js" | js.Build }} -->
<!-- <script -->
<!--   src="{{ $js.RelPermalink }}" -->
<!--   defer -->
<!-- ></script> -->

<!-- <script type = "text/javascript" -->
<!--   src="/js/jquery.min.js" -->
<!-- ></script> -->

<!-- <script type = "text/javascript" src="/js/jquery-ui.min.js"> -->
<!-- </script> -->

<script>
    $(function() {
        $( "#tabs, #tabs1, #tabs2, #tabs3, #tabs4, #tabs5, #tabs6, #tabs7, #tabs8" ).tabs();
    });
</script>

<div id = "tabs">
{{ $ss:=split .Inner "---" }}
    <ul>
    {{ range $idx, $el :=$ss }}
      {{ if ne $idx 0 }}
        {{ $content:=split $el "$$$" }}
        <li><a href = "#{{  (printf ("tab-%d") $idx)  }}"> {{index $content 0}}</a></li>
      {{ end }}
    {{ end }}
    </ul>

    {{ range $idx, $el :=$ss }}
        {{ $content:=split $el "$$$" }}
        {{ $tab := index $content 1 }}
        <div id ="{{  (printf ("tab-%d") $idx)  }}">
             {{ $tab | markdownify }}
        </div>

    {{ end }}

</div>
{{ $title}}
```


### <span class="section-num">2.2</span> `tab` {#tab}

```html
{{ $name := trim (.Get 0) " " }}
---
{{ $name }}
$$$
{{ $.Inner }}
```


## <span class="section-num">3</span> Использование {#использование}

-   Использовать можно следующим образом:

<!--listend-->

```markdown
{{</* tabs "Общее название" */>}}

{{</* tab "Первый" */>}}

Содержание 1

{{</* /tab */>}}

{{</* tab "Второй" */>}}

Содержание 2

{{</* /tab */>}}

{{</* tab "Третий" */>}}

Содержание 3

{{</* /tab */>}}

{{</* /tabs */>}}
```
