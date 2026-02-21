---
title: "Emacs. Экспорт в taskjuggler"
author: ["Dmitry S. Kulyabov"]
date: 2025-09-05T13:45:00+03:00
lastmod: 2025-09-05T18:47:00+03:00
tags: ["emacs"]
categories: ["self-management", "computer-science"]
draft: false
slug: "emacs-export-taskjuggler"
---

Emacs. Экспорт в taskjuggler.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/h-oll/ox-taskjuggler>
-   Описание:
    -   <https://orgmode.org/worg/exporters/taskjuggler/ox-taskjuggler.html>
    -   <https://orgmode.org/worg/org-tutorials/org-taskjuggler.html>


## <span class="section-num">2</span> Особенности {#особенности}

-   Входит в состав _org-contrib_.
-   Но этот вариант не работает.
-   Следует брать из репозитория.


## <span class="section-num">3</span> Команды для работы {#команды-для-работы}

| Команда                      | Описание                                                             |
|------------------------------|----------------------------------------------------------------------|
| `C-c C-e j t`                | Экспортировать проект в TaskJuggler и открыть HTML-отчет в браузере. |
| `C-c C-e j p`                | Экспортировать в TaskJuggler и сохранить как `.tjp`-файл.            |
| `M-x org-taskjuggler-export` | Альтернативный способ экспорта.                                      |


## <span class="section-num">4</span> Расширенные настройки {#расширенные-настройки}


### <span class="section-num">4.1</span> Зависимости между задачами {#зависимости-между-задачами}

-   Используйте свойство `:DEPENDS:`:

<!--listend-->

```org
 Тестирование
:PROPERTIES:
:EFFORT:   2d
:DEPENDS:  Разработка_API  ; Зависит от завершения задачи "Разработка API"
:END:
```


### <span class="section-num">4.2</span> Распределение ресурсов {#распределение-ресурсов}

-   Укажите занятость ресурса (в %):

<!--listend-->

```org
 Дизайн логотипа
:PROPERTIES:
:EFFORT:   2d
:RESOURCES: Дизайнер{50%}  ; Дизайнер занят на 50% этой задачей
:END:
```


### <span class="section-num">4.3</span> Milestone {#milestone}

-   Отметьте ключевые точки:

<!--listend-->

```org
 Сдача проекта
:PROPERTIES:
:MILESTONE: t
:PLAN:      2025-09-30
:END:
```


## <span class="section-num">5</span> Пример сложного проекта {#пример-сложного-проекта}

```org
#+TITLE: Запуск приложения
#+TASKJUGGLER_PROJECT: AppLaunch
#+TASKJUGGLER_START: 2025-10-01
#+TASKJUGGLER_RESOURCE: Дизайнер, Backend, Frontend, QA

* Этапы
 Дизайн
* Логотип
:PROPERTIES:
:EFFORT:   2d
:RESOURCES: Дизайнер
:END:
* UI/UX
:PROPERTIES:
:EFFORT:   5d
:RESOURCES: Дизайнер{30%}
:DEPENDS:  Логотип
:END:

 Разработка
* API
:PROPERTIES:
:EFFORT:   10d
:RESOURCES: Backend
:DEPENDS:  UI/UX
:END:
* Интерфейс
:PROPERTIES:
:EFFORT:   8d
:RESOURCES: Frontend
:DEPENDS:  UI/UX
:END:

 Тестирование
:PROPERTIES:
:EFFORT:   3d
:RESOURCES: QA
:DEPENDS:  API, Интерфейс
:END:

 Релиз
:PROPERTIES:
:MILESTONE: t
:PLAN:      2025-11-15
:END:
```
