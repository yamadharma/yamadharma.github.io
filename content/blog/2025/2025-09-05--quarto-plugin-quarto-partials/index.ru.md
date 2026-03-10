---
title: "Quarto. Плагин quarto-partials"
author: ["Dmitry S. Kulyabov"]
date: 2025-09-05T20:35:00+03:00
lastmod: 2025-09-06T13:43:00+03:00
tags: ["markdown"]
categories: ["computer-science"]
draft: false
slug: "quarto-plugin-quarto-partials"
---

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/gadenbuie/quarto-partials>
-   Реализует подстановку mustache (см. [Подстановка Mustache]({{< relref "2025-09-03--mustache-substitution" >}}))


## <span class="section-num">2</span> Установка {#установка}

-   Установить расширение в каталог `_extensions`.

<!--listend-->

```shell
quarto add gadenbuie/quarto-partials
```


## <span class="section-num">3</span> Использование {#использование}

-   Используйте шорткод `{{</* partial file ... */>}}` для включения частичного содержимого из `file`.
-   Можно указать именованные пары «ключ-значение» для создания шаблона данные.


### <span class="section-num">3.1</span> \_hello.md {#hello-dot-md}

-   Пусть `_hello.md` содержит следующее содержание:
    ```markdown
    Hello, {{ name }}!
    ```

-   Укажем наше собственное значение для `{{ name }}`:
    ```markdown
    {{</* partial _hello.md name="weary traveler" */>}}
    ```
-   Результат:
    ```text
    Hello, weary traveler!
    ```

-   Можно включить частичные данные в начало документа, используя ключ `partial-data`:

<!--listend-->

```yaml
partial-data:
  name: "friend"
```

```markdown
{{</* partial _hello.md */>}}

Or used inline: To you I say "{{</* partial _hello.md */>}}"
```

-   Результат:

<!--listend-->

```text
Hello, friend!

Or used inline: To you I say “Hello, friend!”
```

-   В качестве альтернативы второй аргумент шорткода может указывать на пользовательский ключ в вашем YAML-файле, например

<!--listend-->

```yaml
my-data:
  friends:
    name: amigo
```

```markdown
{{</* partial _hello.md my-data.friends */>}}
```

-   Результат:

<!--listend-->

```text
Hello, amigo!
```

-   Другой вариант --- предоставить JSON в данные шорткода.
-   Любая пара «ключ-значение», начинающаяся с `{` или `[`  будет преобразован в объект или массив JSON.


### <span class="section-num">3.2</span> \_hello_first_last.qmd {#hello-first-last-dot-qmd}

-   Содержание файла `_hello_first_last.qmd`:

<!--listend-->

```markdown
::: {.callout-tip title="Hi there!"}
{{#person}}
Hello, {{ honorific }} {{ name.first }} {{ name.last }}!
{{/person}}
:::
```

-   Делаем постановку:

<!--listend-->

```markdown
{{</* partial _hello_first_last.qmd person='{"honorific": "Mr.", "name": {"first": "Garrick", "last": "Aden-Buie"}}' */>}}
```

-   Результат:
    ```text
    Hi there!
    Hello, Mr. Garrick Aden-Buie!
    ```


### <span class="section-num">3.3</span> \_favorite_fruits.md {#favorite-fruits-dot-md}

-   Содержание файла `_favorite_fruits.md`:

<!--listend-->

```markdown
These are a few of my favorite fruits:

{{#fruits}}
- {{.}}
{{/fruits}}
```

-   Сделаем подстановку.

<!--listend-->

```markdown
{{</* partial _favorite_fruits.md fruits='["apple", "banana", "coconut", "mango"]' */>}}
```

-   Результат:
    ```text
    These are a few of my favorite fruits:

     - apple
    ​ - banana
    ​ - coconut
    ​ - mango

    ```
