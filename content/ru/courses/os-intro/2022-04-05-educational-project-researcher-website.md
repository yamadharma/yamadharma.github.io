---
title: "Учебный проект Сайт научника"
author: ["Dmitry S. Kulyabov"]
date: 2022-04-05T18:20:00+03:00
lastmod: 2024-02-21T20:54:00+03:00
tags: ["hugo", "education"]
categories: ["computer-science"]
draft: false
weight: 401
toc: true
type: docs
feedback: false
slug: "educational-project-researcher-website"
summary: "Сайт научника"
menu:
  "os-intro-project-personal":
    identifier: "учебный-проект-сайт-научника"
    parent: "os-intro"
    weight: 401
---

Сквозной учебный проект _Персональный сайт научного работника_.

<!--more-->


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Проект является сквозным, так как должен проходить через весь процесс обучения.


## <span class="section-num">2</span> Реализация проекта по курсам {#реализация-проекта-по-курсам}

-   На первом курсе создаётся собственно персональный сайт.
-   На пятом курсе сайт расширяется за счёт добавления собственной библиографии и CV.
-   На этой же основе делаются сайты для групповых проектов.
-   Сайт используется также в активности _Эссе_.


## <span class="section-num">3</span> Этапы реализации проекта {#этапы-реализации-проекта}

1.  Размещение на _Github pages_ заготовки для персонального сайта.
    -   Установить необходимое программное обеспечение.
    -   Скачать шаблон темы сайта.
    -   Разместить его на хостинге git.
    -   Установить параметр для _URLs_ сайта.
    -   Разместить заготовку сайта на _Github pages_.

2.  Добавить к сайту данные о себе.
    -   Список добавляемых данных.
        -   Разместить фотографию владельца сайта.
        -   Разместить краткое описание владельца сайта (Biography).
        -   Добавить информацию об интересах (Interests).
        -   Добавить информацию от образовании (Education).
    -   Сделать пост по прошедшей неделе (см. [Шаблон поста по прошедшей неделе]({{< relref "2022-05-05-template-post-last-week" >}})).
    -   Добавить пост на тему по выбору (см. [Научное эссе]({{< relref "2022-05-05-scientific-essay" >}})):
        -   Управление версиями. Git.
        -   Непрерывная интеграция и непрерывное развертывание (CI/CD).

3.  Добавить к сайту достижения.
    -   Список достижений.
        -   Добавить информацию о навыках (Skills).
        -   Добавить информацию об опыте (Experience).
        -   Добавить информацию о достижениях (Accomplishments).
    -   Сделать пост по прошедшей неделе.
    -   Добавить пост на тему по выбору:
        -   Легковесные языки разметки.
        -   Языки разметки. LaTeX.
        -   Язык разметки Markdown.

4.  Добавить к сайту ссылки на научные и библиометрические ресурсы.
    -   Зарегистрироваться на соответствующих ресурсах и разместить на них ссылки на сайте.
    -   Научные идентификаторы (см. [Научные идентификаторы]({{< relref "2024-02-21-scientific-identifiers" >}})):
        -   ORCID : <https://orcid.org/>;
        -   eLibrary : <https://elibrary.ru/>.
    -   Научные социальные сети:
        -   Google Scholar : <https://scholar.google.com/>;
        -   ResearchGate : <https://www.researchgate.net/>;
        -   Academia.edu : <https://www.academia.edu/>.
    -   Репозитории препринтов и кода:
        -   arXiv : <https://arxiv.org/>;
        -   github : <https://github.com/>.
    -   Сделать пост по прошедшей неделе.
    -   Добавить пост на тему по выбору:
        -   Оформление отчёта.
        -   Создание презентаций.
        -   Работа с библиографией.

5.  Добавить с сайту все остальные элементы.
    -   Сделать записи для персональных проектов.
    -   Сделать пост по прошедшей неделе.
    -   Добавить пост на тему по выбору.
        -   Языки научного программирования.

6.  Размещение двуязычного сайта на Github.
    -   Сделать поддержку английского и русского языков.
    -   Разместить элементы сайта на обоих языках.
    -   Разместить контент на обоих языках.
    -   Сделать пост по прошедшей неделе.
    -   Добавить пост на тему по выбору (на двух языках).


## <span class="section-num">4</span> Техническая реализация проекта {#техническая-реализация-проекта}


### <span class="section-num">4.1</span> Общая информация {#общая-информация}


#### <span class="section-num">4.1.1</span> Генератор статических сайтов {#генератор-статических-сайтов}

-   Для реализации сайта используется генератор статических сайтов _Hugo_.
-   [Генератор статических сайтов Hugo]({{< relref "2020-12-07-hugo-site-generator" >}})
-   Сайт: <https://gohugo.io/>
-   Репозиторий: <https://github.com/gohugoio/hugo>


### <span class="section-num">4.2</span> Шаблон для сайта {#шаблон-для-сайта}

-   [Hugo. Шаблон для научных работников]({{< relref "2021-07-02-hugo-template-for-scientists" >}})
-   Общие файлы для тем _Wowchemy_:
    -   Репозиторий: <https://github.com/wowchemy/wowchemy-hugo-themes>
-   В качестве шаблона индивидуального сайта используется шаблон _Hugo Academic Theme_.
    -   Демо-сайт: <https://academic-demo.netlify.app/>
    -   Репозиторий: <https://github.com/wowchemy/starter-hugo-academic>
-   В качестве шаблона для группового проекта используется шаблон _Hugo Research Group Theme_.
    -   Демо-сайт: <https://research-group.netlify.app/>
    -   Репозиторий: <https://github.com/wowchemy/starter-hugo-research-group>


#### <span class="section-num">4.2.1</span> Видео {#видео}

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


### <span class="section-num">4.3</span> Создание сайта на Hugo {#создание-сайта-на-hugo}

-   [Создание сайта на Hugo]({{< relref "2022-04-12-creating-hugo-site" >}})


### <span class="section-num">4.4</span> Используемый шаблон {#используемый-шаблон}


### <span class="section-num">4.5</span> Markdown для Hugo {#markdown-для-hugo}

-   [Синтаксис Markdown для генератора сайтов Hugo]({{< relref "2020-11-26-hugo-markdown" >}})
-   [Сокращение для видео Rutube для Hugo]({{< relref "2022-04-04-shortcode-video-rutube-hugo" >}})
-   [Hugo shortcode. Видео на VK Video]({{< relref "2023-08-24-hugo-shortcode-vkvideo" >}})


### <span class="section-num">4.6</span> Org-mode для Hugo {#org-mode-для-hugo}

-   [Org-mode. Экспорт в Hugo]({{< relref "2020-12-17-org-mode-export-hugo" >}})
-   [Обратные ссылки в Hugo]({{< relref "2021-06-02-backlinks-hugo" >}})
