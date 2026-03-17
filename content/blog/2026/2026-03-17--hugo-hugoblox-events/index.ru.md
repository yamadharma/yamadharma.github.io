---
title: "Hugo. Hugoblox. Events"
author: ["Dmitry S. Kulyabov"]
date: 2026-03-17T20:48:00+03:00
lastmod: 2026-03-17T21:17:00+03:00
tags: ["markdown", "hugo"]
categories: ["computer-science"]
draft: false
slug: "hugo-hugoblox-events"
---

Hugo. Hugoblox. Events.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Доклады на конференциях, мастер-классы, семинары и вебинары.
-   Можно указывать время начала/окончания, место проведения, тезисы докладов.
-   Можно автоматически встраивать связанные презентации.
-   Автоматически отображает события, отсортированные по дате, со следующими параметрами:
    -   предстоящие события отображаются первыми;
    -   потом прошедшие события.


## <span class="section-num">2</span> Структура {#структура}


### <span class="section-num">2.1</span> Иерархия {#иерархия}

-   `content/events`.


### <span class="section-num">2.2</span> Дата и время {#дата-и-время}

-   Мероприятия предусматривают точное время начала и окончания, а также проведение событий в течение всего дня.
-   Для задания времени используйте формат ISO 8601 с указанием часового пояса.
-   Время отображается в местном часовом поясе посетителя.

<!--listend-->

```yaml
# Specific time range
date: "2024-12-10T14:00:00Z"
date_end: "2024-12-10T15:00:00Z"
all_day: false

# All-day event
date: "2024-12-10"
all_day: true
```


### <span class="section-num">2.3</span> Основные поля {#основные-поля}

| Поле        | Тип        | Описание                                      |
|-------------|------------|-----------------------------------------------|
| `title`     | `string`   | Название доклада/мероприятия (обязательно)    |
| `event`     | `string`   | Название конференции или мероприятия          |
| `event_url` | `string`   | Ссылка на сайт мероприятия                    |
| `location`  | `string`   | Место проведения и город                      |
| `date`      | `datetime` | Дата/время начала (ISO 8601)                  |
| `date_end`  | `datetime` | Дата/время окончания                          |
| `all_day`   | `bool`     | Флаг мероприятия, которое продлится весь день |
| `abstract`  | `string`   | Аннотация доклада                             |
| `slides`    | `string`   | Название папки со слайдами                    |
| `authors`   | `list`     | Выступающие (slug)                            |
| `featured`  | `bool`     | Закрепить вверху списка                       |


## <span class="section-num">3</span> Связывание слайдов с событиями {#связывание-слайдов-с-событиями}

-   Создайте свои слайды в `content/slides/neurips-2024/index.md`
-   Укажите ссылку на слайды, используя поле `slides:`.
-   Слайды автоматически встраиваются на страницу мероприятия с кнопкой переключения в полноэкранный режим.
    ```yaml
    slides: "neurips-2024"   # Matches the folder name
    ```


## <span class="section-num">4</span> Пример {#пример}


### <span class="section-num">4.1</span> Файл события {#файл-события}

```markdown
---
title: "My Conference Talk"

# Event details
event: "NeurIPS 2024"
event_url: "https://neurips.cc"
location: "Vancouver Convention Centre, Vancouver, Canada"

# Talk start and end times (ISO 8601)
date: "2024-12-10T14:00:00Z"
date_end: "2024-12-10T15:00:00Z"
all_day: false

# Abstract
abstract: >
  In this talk, we present our latest findings on scalable
  attention mechanisms for large language models.

# Summary for listing cards
summary: "Presenting our work on scalable attention at NeurIPS 2024."

# Authors / Speakers
authors:
  - jane-doe

# Tags
tags:
  - Machine Learning
  - NeurIPS
  - Attention

# Link to slides (folder name under content/slides/)
slides: "neurips-2024"

# Featured image
image:
  filename: featured.jpg
  caption: "Presenting at NeurIPS"

# Links
links:
  - name: Video Recording
    url: https://youtube.com/...
    icon: video
  - name: Paper
    url: /publication/attention-paper/
    icon: document

# Shorthand link fields
url_pdf: ""
url_slides: ""
url_video: ""
url_code: ""

# Featured
featured: true

# Draft
draft: false
---

## Talk Details

Add any additional context, extended abstract, or notes about the talk.
Include references, acknowledgments, or related work.
```


### <span class="section-num">4.2</span> Соответствующий файл org {#соответствующий-файл-org}

```org
* {{Название выступления}}                                           :event:talk:
:PROPERTIES:
:event:          {{Название конференции/мероприятия}}
:event_url:      {{Ссылка на сайт мероприятия}}
:location:       {{Место проведения}}
:date:           {{Дата и время начала в формате ISO 8601}}
:date_end:       {{Дата и время окончания в формате ISO 8601}}
:all_day:        {{false/true}}
:summary:        {{Краткое описание для карточки (одна строка)}}
:authors:        {{author-id1, author-id2}}   ; разделитель — запятая
:tags:           {{тег1, тег2, тег3}}         ; разделитель — запятая
:slides:         {{идентификатор слайдов (папка в content/slides/)}}
:image_filename: {{имя файла изображения, например featured.jpg}}
:image_caption:  {{Подпись под изображением}}
:links:          {{Name1::url1::icon1
                   Name2::url2::icon2}}       ; каждая ссылка на новой строке
:url_pdf:        {{ссылка на PDF}}
:url_slides:     {{ссылка на слайды (если не используются внутренние)}}
:url_video:      {{ссылка на видео}}
:url_code:       {{ссылка на код}}
:featured:       {{true/false}}
:draft:          {{true/false}}
:END:

#+begin_abstract
{{Текст абстракта. Может занимать несколько абзацев.}}
#+end_abstract

** Talk Details

{{Подробности выступления, благодарности, ссылки на связанные работы и т.д.}}
```


#### <span class="section-num">4.2.1</span> Пояснения к полям {#пояснения-к-полям}

-   Заголовок (`* Название`) : соответствует `title` в front matter.
-   Теги `:event:talk:` можно использовать для удобной фильтрации в org-roam (они не обызательны).
-   Свойства (`:PROPERTIES:`) : почти все поля из front matter перенесены сюда.
    -   `:authors:` : список идентификаторов авторов через запятую. В HugoBlox они обычно ссылаются на файлы в папке `content/authors/`.
    -   `:tags:` : теги через запятую.
    -   `:links:` : многострочное свойство. Каждая строка содержит три части, разделённые `::` : отображаемое имя, URL, имя иконки (из набора Font Awesome или встроенных иконок HugoBlox). При экспорте это преобразуется в список словарей.
    -   Даты (`:date:`, `:date_end:`) обязательно в формате ISO 8601 с часовым поясом (например, `2024-12-10T14:00:00Z`).
-   Блок абстракта (`#+begin_abstract ... #+end_abstract`) : его содержимое пойдёт в поле `abstract`.
-   Секция Talk Details : соответствует основному содержимому страницы после front matter.
