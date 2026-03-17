---
title: "Hugo. Hugoblox. Слайды"
author: ["Dmitry S. Kulyabov"]
date: 2026-03-17T21:18:00+03:00
lastmod: 2026-03-17T21:36:00+03:00
tags: ["hugo", "markdown"]
categories: ["computer-science"]
draft: false
slug: "hugo-hugoblox-slides"
---

Hugo. Hugoblox. Слайды

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Работает на движке reveal.js.


## <span class="section-num">2</span> Использование {#использование}


### <span class="section-num">2.1</span> Иерархия {#иерархия}

-   `content/slides`.


## <span class="section-num">3</span> Примечания докладчика {#примечания-докладчика}

-   Можно добавить личные заметки, видимые только в режиме докладчика:

<!--listend-->

```markdown
## My Slide

Visible content here

Note:
- This is a speaker note (press S to view)
- Only you see these in presenter mode
- Perfect for talking points and reminders
```

-   Нажмите клавишу `S`  во время презентации, чтобы открыть консоль докладчика.


## <span class="section-num">4</span> Скрытие слайдов {#скрытие-слайдов}

-   Скройте слайды из презентации, сохранив их в исходном коде:

<!--listend-->

```markdown
## Visible Slide

This slide will appear in the presentation.

---
<!-- hide -->
## Hidden Slide

This slide won't appear but stays in source for reference.

Perfect for:
- Backup slides in case of questions
- Speaker-only reference material
- Work-in-progress content
- Alternative explanations

---

## Another Visible Slide

Back to normal presentation flow.
```


### <span class="section-num">4.1</span> Зачем прятать слайды {#зачем-прятать-слайды}

-   Резервный контент : держите дополнительные слайды наготове, не загромождая основной поток информации.
-   Справочная информация о докладчике : личные заметки и подробные сведения.
-   Гибкие возможности для презентаций : один и тот же исходный материал для разных аудиторий или при ограниченном времени.
-   Контроль версий : храните все версии контента в одном файле.


## <span class="section-num">5</span> Брендинг на слайдах {#брендинг-на-слайдах}


### <span class="section-num">5.1</span> Глобальные настройки брендинга {#глобальные-настройки-брендинга}

-   Можно установить глобально для всего сайта:

<!--listend-->

```yaml
slides:
  branding:
    logo:
      filename: "university-logo.svg"
      position: "top-right"
      width: "60px"
    footer:
      text: "© My University"
      position: "bottom-center"
```

-   И изменять для каждой презентации.


### <span class="section-num">5.2</span> Скрытие брендинга на уровне слайда {#скрытие-брендинга-на-уровне-слайда}

-   Иногда нужны чистые слайды --- титульные слайды, изображения на весь экран и т. д.
-   Добавьте HTML-комментарий в **начало**  содержимого слайда:

<!--listend-->

```markdown
---

<!-- no-branding -->
# My Title Slide

This slide has no branding elements.

---

## Regular Slide

This slide shows branding normally.
```


### <span class="section-num">5.3</span> Параметры управления видимостью {#параметры-управления-видимостью}

-   Видимость задаётся комментарием.
-   Комментарий должен располагаться в начале содержимого слайда (сразу после разделителя `---` ).

| Комментарий            | Скрывает                                           |
|------------------------|----------------------------------------------------|
| `<!-- no-branding -->` | Всё (логотип, заголовок, автор, нижний колонтитул) |
| `<!-- no-header -->`   | Логотип + наложение заголовка                      |
| `<!-- no-footer -->`   | Автор + текст нижнего колонтитула                  |
