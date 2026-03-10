---
title: "Подстановка Mustache"
author: ["Dmitry S. Kulyabov"]
date: 2025-09-03T20:24:00+03:00
lastmod: 2025-09-05T20:33:00+03:00
tags: ["markdown"]
categories: ["computer-science"]
draft: false
slug: "mustache-substitution"
---

Подстановка Mustache.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://mustache.github.io/>
-   Mustache является языком шаблонов, который используется для генерации текста на основе данных.
-   Mustache использует синтаксис в виде двойных фигурных скобок `{{ }}` для обозначения мест подстановки данных.
-   Позволяет вставлять переменные и другие данные в шаблоны без необходимости написания сложного кода.
-   Например, если у вас есть шаблон с `{{ name }}`, то при подстановке данных это место будет заменено на значение переменной `name`.


## <span class="section-num">2</span> Особенности {#особенности}

-   Отсутствие логики в шаблонах: Mustache фокусируется только на подстановке данных и не поддерживает условные операторы или циклы непосредственно в шаблонах.
-   Кроссплатформенность: Mustache реализован на множестве языков программирования, включая JavaScript, Python, Ruby и другие.
-   Простота использования: синтаксис Mustache интуитивно понятен и легко осваивается разработчиками.
-   Логика в данных: Вся логика (условия, циклы) выносится в код, а не в шаблон.
-   Экранирование: По умолчанию экранирует HTML-символы (`<`, `>`, `&` и т.д.).
-   Расширяемость: Можно добавлять кастомные хелперы (например, для форматирования дат).


## <span class="section-num">3</span> Пример использования {#пример-использования}

-   Пусть дан html:

<!--listend-->

```html
<h1>Привет, {{ name }}!</h1>
<p>Ты зарегистрировался {{ date }}.</p>
```

-   Данные для подстановки:

<!--listend-->

```js
{
  "name": "Иван",
  "date": "2025-09-03"
}
```

-   Результат:

<!--listend-->

```html
<h1>Привет, Иван!</h1>
<p>Ты зарегистрировался 2025-09-03.</p>
```

-   Пример шаблона с условием и списком:

<!--listend-->

```html
{{#user}}
  <h2>Профиль {{name}}</h2>
  {{#posts}}
    <div class="post">{{title}}</div>
  {{/posts}}
  {{^posts}}
    <p>Нет постов.</p>
  {{/posts}}
{{/user}}
```


## <span class="section-num">4</span> Правила синтаксиса Mustache {#правила-синтаксиса-mustache}


### <span class="section-num">4.1</span> Переменные {#переменные}

Используются двойные фигурные скобки `{{variable}}`. Значение
подставляется с экранированием HTML. Для вывода без экранирования:
`{{{variable}}}` или `{{&variable}}`.
Пример:

```html
<p>{{username}} написал: {{{comment}}}</p>
```


### <span class="section-num">4.2</span> Секции {#секции}

-   Списки: `{{#list}}...{{/list}}` --- повторяет блок для каждого
    элемента массива.
    Пример:
    ```html
    <ul>{{#items}}<li>{{name}}</li>{{/items}}</ul>
    ```

-   Условные блоки:
    -   `{{#condition}}...{{/condition}}` --- отображает блок, если
        `condition` истинно (не пустой массив, не `false`, не `null`).
    -   `{{^condition}}...{{/condition}}` --- отображает блок, если
        `condition` ложно.


### <span class="section-num">4.3</span> Комментарии {#комментарии}

Синтаксис: `{{! Это комментарий}}`. Не отображаются в выходном HTML.


### <span class="section-num">4.4</span> Частичные шаблоны {#частичные-шаблоны}

Подключаются через `{{>partial}}`. Например, `{{>header}}` вставит
содержимое шаблона `header.mustache`.


### <span class="section-num">4.5</span> Изменение разделителей {#изменение-разделителей}

Можно менять `{{ }}` на другие символы через `{{=<% %>`}}=. Возврат к
стандартным: `<%={{ }}=%>`.


### <span class="section-num">4.6</span> Лямбда-функции {#лямбда-функции}

Если переменная является функцией, она вызывается с параметрами
(текст блока, рендеринг). Пример для JS:

```javascript
data.uppercase = () => (text, render) => render(text).toUpperCase();
```

В шаблоне: `{{#uppercase}}Hello{{/uppercase}}` → `HELLO`.


## <span class="section-num">5</span> Поддерживаемые языки и библиотеки {#поддерживаемые-языки-и-библиотеки}


### <span class="section-num">5.1</span> JavaScript {#javascript}

-   Репозиторий: <https://github.com/janl/mustache.js>.
-   Пример:
    ```js
    const html = Mustache.render("Hello {{name}}!", {name: "Алиса"});
    ```


### <span class="section-num">5.2</span> Go {#go}

-   Репозиторий: <https://github.com/hoisie/mustache>.


### <span class="section-num">5.3</span> PHP {#php}

-   Репозиторий: <https://github.com/bobthecow/mustache.php>.


### <span class="section-num">5.4</span> Ruby {#ruby}

-   Репозиторий: <https://github.com/mustache/mustache>.


### <span class="section-num">5.5</span> Python {#python}

-   Репозиторий: <https://github.com/defunkt/pystache>.


### <span class="section-num">5.6</span> Java {#java}

-   Репозиторий: <https://github.com/spullara/mustache.java>.


### <span class="section-num">5.7</span> C++ {#c-plus-plus}

-   Репозиторий: <https://github.com/kainjow/Mustache>.


### <span class="section-num">5.8</span> Swift {#swift}

-   Репозиторий: <https://github.com/groue/GRMustache.swift>.
