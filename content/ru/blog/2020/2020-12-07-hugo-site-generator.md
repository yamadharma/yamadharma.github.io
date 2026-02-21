---
title: "Генератор статических сайтов Hugo"
author: ["Dmitry S. Kulyabov"]
date: 2020-12-07T14:06:00+03:00
lastmod: 2025-08-11T21:13:00+03:00
tags: ["hugo", "MOC", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "hugo-site-generator"
---

Особенности генератора статических сайтов Hugo.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Темы {#темы}

-   В рамах Hugo создан набор разнообразных тем.
-   Для сайта научного работника или научной группы можно рекомендовать набор тем Wowchemy (см. [Hugo. Шаблон для научных работников]({{< relref "2021-07-02-hugo-template-for-scientists" >}})).


## <span class="section-num">2</span> Язык описания страниц {#язык-описания-страниц}

-   В качестве языка описания страниц используется Markdown. Сам Hugo использует библиотеку [Goldmark](https://github.com/yuin/goldmark/). Этот диалект полностью соответствует спецификации [CommonMark](https://commonmark.org/).
-   Язык расширен в основном за счёт операторов (shortcodes) и поддержки расширений для диаграмм, LaTeX и др. ( см. [Синтаксис Markdown для генератора сайтов Hugo]({{< relref "2020-11-26-hugo-markdown" >}})).
-   Кроме того, возможно использование и других диалектов Markdown.
-   Также возможно использование других легковесных языков разметки (см. [Легковесные языки разметки]({{< relref "2021-08-28-lightweight-markup-languages" >}})): [Emacs Org-mode](https://github.com/niklasfasching/go-org), [AsciiDoc](https://asciidoctor.org/), [RST](http://docutils.sourceforge.net/rst.html) через внешние программы.


## <span class="section-num">3</span> Собственная favicon для сайта {#собственная-favicon-для-сайта}

-   Собственная иконка для сайта делается в виде файла `icon.png`, размеры 512x512 пикселей.
-   Иконка располагается в каталоге `assets/media/`.


## <span class="section-num">4</span> Взаимодействие с внешними сервисами {#взаимодействие-с-внешними-сервисами}

-   Для комментариев используются сервисы [Disqus](https://disqus.com/) и [Commento](https://commento.io/) (см. [Комментирование для статических сайтов]({{< relref "2021-05-25-commenting-static-sites" >}})).


## <span class="section-num">5</span> Процесс создания блога {#процесс-создания-блога}

-   Предлагается не писать заметки непосредственно для сайта, а использовать систему генерации статических сайтов как бэкенд для систем ведения заметок.
-   Предлагается использовать режим _org-roam_ (см. [Org-roam. Экспорт в Hugo]({{< relref "2022-11-23-org-roam-hugo-export" >}})) редактора _emacs_ как реализации _Zettelkasten_ (см. [Метод Zettelkasten]({{< relref "2021-02-18-zettelkasten-method" >}})).
-   Для реализации методики _Zettelkasten_ на сайте необходима реализация обратных ссылок (см. [Обратные ссылки в Hugo]({{< relref "2021-06-02-backlinks-hugo" >}})).


## <span class="section-num">6</span> Создание статического сайта {#создание-статического-сайта}

-   [Создание сайта на Hugo]({{< relref "2022-04-12-creating-hugo-site" >}})
-   [Hugo. Система шаблонов]({{< relref "2025-08-11--hugo-template-system" >}})


## <span class="section-num">7</span> Варианты программы {#варианты-программы}


### <span class="section-num">7.1</span> deploy {#deploy}

-   Свойство `deploy` в Hugo --- это команда CLI, позволяющая напрямую развертывать статический сайт в облачных хранилищах: Amazon S3, Azure Blob Storage или Google Cloud Storage.
-   Требуется расширенная версия Hugo (Hugo extended/deploy edition).
-   Основные особенности:
    -   Конфигурация целей развёртывания
        -   В файле конфигурации сайта (например, `hugo.yaml`) указываются параметры цели: имя и URL бакета с регионом (например, `s3://my_bucket?region=us-west-1`).
    -   Синхронизация файлов
        -   Команда `hugo deploy` синхронизирует содержимое локальной папки `public` с удалённым бакетом, сравнивая имена файлов, их размеры и MD5-хеши.
        -   Изменённые или отсутствующие файлы перезаписываются, а лишние удаляются (с ограничением на удаление не более 256 файлов по умолчанию).
    -   Дополнительные флаги
        -   `--force` : принудительная перезапись всех файлов;
        -   `--dryRun` : предпросмотр изменений без применения;
        -   `--maxDeletes` : изменение лимита на удаление файлов.

-   Перед использованием необходимо:
    -   Настроить аутентификацию через CLI выбранного облачного провайдера (AWS, Azure, Google Cloud);
    -   Создать бакет с публичным доступом для статического сайта.
-   Документация: <https://gohugo.io/host-and-deploy/deploy-with-hugo-deploy/>


## <span class="section-num">8</span> Ресурсы {#ресурсы}


### <span class="section-num">8.1</span> Учебные материалы {#учебные-материалы}

-   Учебные материалы:
    -   <https://hugo-mini-course.netlify.app/ru/>


### <span class="section-num">8.2</span> Модули {#модули}


#### <span class="section-num">8.2.1</span> hugo-modules {#hugo-modules}

-   Репозиторий: <https://github.com/gethugothemes/hugo-modules>
-   Сайт: <https://gethugothemes.com/hugo-modules>


### <span class="section-num">8.3</span> Списки тем {#списки-тем}


#### <span class="section-num">8.3.1</span> Hugo themes {#hugo-themes}

-   Сайт: <https://themes.gohugo.io/>


#### <span class="section-num">8.3.2</span> awesome-hugo-themes {#awesome-hugo-themes}

-   Репозиторий: <https://github.com/QIN2DIM/awesome-hugo-themes>


### <span class="section-num">8.4</span> Темы {#темы}


#### <span class="section-num">8.4.1</span> hugobricks {#hugobricks}

-   Сайт: <https://www.hugobricks.preview.usecue.com>
-   Репозитоирий: <https://github.com/jhvanderschee/hugobricks>


#### <span class="section-num">8.4.2</span> Dot Org Theme {#dot-org-theme}

-   Репозиторий: <https://github.com/cncf/dot-org-hugo-theme>
-   Сайт: <https://dot-org-hugo-theme-demo.netlify.app/>


#### <span class="section-num">8.4.3</span> hugo-theme-tailwind {#hugo-theme-tailwind}

-   Репозиторий: <https://github.com/tomowang/hugo-theme-tailwind>


#### <span class="section-num">8.4.4</span> hextra {#hextra}

-   Сайт: <https://imfing.github.io/hextra/>
-   Шаблон: <https://github.com/imfing/hextra-starter-template>
-   Репозиторий: <https://github.com/imfing/hextra>
