---
title: "Синтаксис языка Markdown"
author: ["Dmitry S. Kulyabov"]
date: 2020-10-22T09:48:00+03:00
lastmod: 2024-02-22T21:59:00+03:00
tags: ["programming", "education"]
categories: ["computer-science"]
draft: false
slug: "markdown-syntax"
---

Общая информация по языку Markdown.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Варианты языка Markdown {#варианты-языка-markdown}

-   Генератор статистических сайтов [Hugo](https://gohugo.io/) (см. [Генератор статических сайтов Hugo]({{< relref "2020-12-07-hugo-site-generator" >}})) использует вариант Markdown на основе библиотеки [Goldmark](https://github.com/yuin/goldmark/) (см. [Синтаксис markdown для генератора сайтов Hugo]({{< relref "2020-11-26-hugo-markdown" >}})).


## <span class="section-num">2</span> Базовый синтаксис Markdown {#базовый-синтаксис-markdown}

-   Чтобы создать заголовок, используйте знак (`#`), например:

<!--listend-->

```markdown
# This is heading 1
## This is heading 2
### This is heading 3
#### This is heading 4
```

---

# This is heading 1
## This is heading 2
### This is heading 3
#### This is heading 4

---

-   Чтобы задать для текста полужирное начертание, заключите его в двойные звездочки:

<!--listend-->

```markdown
This text is **bold**.
```

---

This text is **bold**.

---

-   Чтобы задать для текста курсивное начертание, заключите его в одинарные звездочки:

<!--listend-->

```markdown
This text is *italic*.
```

---

This text is *italic*.

---

-   Чтобы задать для текста полужирное и курсивное начертание, заключите его в тройные звездочки:

<!--listend-->

```markdown
This is text is both ***bold and italic***.
```

---

This is text is both ***bold and italic***.

---

Блоки цитирования создаются с помощью символа &gt;:

```markdown
> The drought had lasted now for ten million years, and the reign of the terrible lizards had long since ended. Here on the Equator, in the continent which would one day be known as Africa, the battle for existence had reached a new climax of ferocity, and the victor was not yet in sight. In this barren and desiccated land, only the small or the swift or the fierce could flourish, or even hope to survive.
```

Неупорядоченный (маркированный) список можно отформатировать с помощью
звездочек или тире:

```markdown
- List item 1
- List item 2
- List item 3
```

Чтобы вложить один список в другой, добавьте отступ для элементов
дочернего списка:

```markdown
- List item 1
  - List item A
  - List item B
- List item 2
```

Упорядоченный список можно отформатировать с помощью соответствующих
цифр:

```markdown
1. First instruction
1. Second instruction
1. Third instruction
```

Чтобы вложить один список в другой, добавьте отступ для элементов
дочернего списка:

```markdown
1. First instruction
   1. Sub-instruction
   1. Sub-instruction
1. Second instruction
```

Синтаксис Markdown для встроенной ссылки состоит из части `[link text]`,
представляющей текст гиперссылки, и части `(file-name.md)` -- URL-адреса
или имени файла, на который дается ссылка:

```markdown
[link text](file-name.md)
```

Markdown поддерживает как встраивание фрагментов кода в предложение, так
и их размещение между предложениями в виде отдельных огражденных блоков.
Огражденные блоки кода --- это простой способ выделить синтаксис для
фрагментов кода. Общий формат огражденных блоков кода:

````md
``` language
your code goes in here
```
````

Верхние и нижние индексы: \\[H\_2\\] записывается как

````markdown
H~2~O
````

\\[2^{10}\\] записывается как

````markdown
2^10^
````

Внутритекстовые формулы делаются аналогично формулам LaTeX. Например,
формула \\(\sin^2 (x) + \cos^2 (x) = 1\\) запишется как

````markdown
$\sin^2 (x) + \cos^2 (x) = 1$
````

Выключные формулы:

\\[\sin^2 (x) + \cos^2 (x) = 1\\] {#eq:eq:sin2+cos2} со ссылкой в тексте
«Смотри формулу ([-@eq:eq:sin2+cos2]).» записывается как

````markdown
$$
\sin^2 (x) + \cos^2 (x) = 1
$$ {#eq:eq:sin2+cos2}

Смотри формулу ([-@eq:eq:sin2+cos2]).
````


## <span class="section-num">3</span> Специальные элементы {#специальные-элементы}


### <span class="section-num">3.1</span> Видео _Youtube_ {#видео-youtube}

-   Видео youtube нельзя добавить напрямую.
-   В некоторых особых случаях можно добавлять непосредственно ссылку (например, в системе Moodle).
-   Можно добавить изображение со ссылкой на видео в виде `html`:
    ````html
    <a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE" target="_blank">
      <img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" alt="alternative text for search engines" width="240" height="180" border="10" />
    </a>
    ````
-   Можно добавить изображение со ссылкой на видео в виде `markdown` (см. [Миниатюры видео для youtube]({{< relref "2022-02-05-youtube-video-thumbnail" >}})):
    ````markdown
    [![alternative text for search engines](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID)
    ````


### <span class="section-num">3.2</span> Видео _Rutube_ {#видео-rutube}

-   Идентификатор видео на _Rutube_ представляет собой шестнадцатеричное число.
-   В адресе для миниатюры используются первые цифры идентификатора.
-   Изображение со ссылкой на видео в виде `markdown`:
    ````markdown
    [![alternative text for search engines](https://pic.rutubelist.ru/video/12/34/RUTUBE_PIC_ID.jpg)](https://rutube.ru/video/RUTUBE_VIDEO_ID/)
    ````

    -   Здесь 12 --- первые 2 цифры `RUTUBE_PIC_ID`; 34 --- 3 и 4 цифры `RUTUBE_PIC_ID`.
-   Связь `RUTUBE_PIC_ID` и `RUTUBE_VIDEO_ID` мне пока не понятна.
