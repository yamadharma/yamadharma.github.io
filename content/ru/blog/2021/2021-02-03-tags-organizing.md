---
title: "Организация меток для записей"
author: ["Dmitry S. Kulyabov"]
date: 2021-02-03T12:21:00+03:00
lastmod: 2025-08-10T15:45:00+03:00
tags: ["MOC", "emacs", "hugo"]
categories: ["computer-science", "self-management"]
draft: false
slug: "tags-organizing"
---

Предлагается следующая структура _категорий_ и _меток_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Обоснование именования меток {#обоснование-именования-меток}

-   Метки и категории задаются для _org-mode todo_, _org-roam_, _hugo_.
-   Метки и категории должны быть согласованы для разных областей применения.
-   Метки и категории должны быть согласованы для разных языков (на данный момент русского и английского).
-   При этом на разных языках они могут звучать по-разному.
-   Предлагается категории предварять символом `@` (см. [Org-mode. Экспорт в Hugo]({{< relref "2020-12-17-org-mode-export-hugo" >}})).


## <span class="section-num">2</span> Категории и метки {#категории-и-метки}

-   `@book`: [Прочитанные книги]({{< relref "2020-12-15-books" >}})
    -   `culture`[^fn:1]: [Книги. Культура]({{< relref "2021-01-10-books-culture" >}})
    -   `fiction`: [Книги. Художественная литература]({{< relref "2023-07-14-books-fiction" >}})
    -   `geometry`: [Книги. Геометрия]({{< relref "2023-08-19-books-geometry" >}})
    -   `history`: [Книги. История]({{< relref "2023-05-06-books-history" >}})
    -   `physics`: [Книги. Физика]({{< relref "2023-07-01-books-physics" >}})
    -   `programming`: [Книги. Программирование]({{< relref "2021-01-10-books-programming" >}})
    -   `science_admin`: [Книги. Научно-административная деятельность]({{< relref "2023-12-07-books-scientific-administrative" >}})
    -   `science_history`: [Книги. История науки]({{< relref "2023-08-20-books-science-history" >}})
    -   `science_people`[^fn:2]: [Книги. Люди науки]({{< relref "2021-02-20-books-science-people" >}})
    -   `science_philosophy`: [Книги. Философия науки]({{< relref "2021-01-06-books-science-philosophy" >}})
    -   `science_writing` : [Книги. Научное письмо]({{< relref "2025-02-04--books-science-writing" >}})
    -   `sysadmin`: [Книги. Системное администрирование]({{< relref "2024-01-24-books-sysadmin" >}})
    -   `modeling`: [Книги. Моделирование]({{< relref "2025-04-11--books-modeling" >}})
    -   `movie`: [Просмотренные фильмы]({{< relref "2025-08-10--movies-watched" >}})

-   `@computer_science`: Компьютерные науки
    -   `cisco`: [Администрирование Cisco]({{< relref "2021-06-16-cisco-administration" >}})
    -   `configuration`: [Конфигурации]({{< relref "2024-06-12-configuration" >}})
    -   `emacs`: [Emacs]({{< relref "2020-12-24-emacs" >}})
    -   `font`: [Шрифты]({{< relref "2024-03-07-font" >}})
    -   `gentoo`[^fn:3]: [Linux. Дистрибутив Gentoo]({{< relref "2022-09-17-linux-gentoo-distribution" >}})
    -   `git`: [Система контроля версий git]({{< relref "2020-12-07-git-cvs" >}})
    -   `hard`:
    -   `hugo`: [Генератор статических сайтов Hugo]({{< relref "2020-12-07-hugo-site-generator" >}})
    -   `ipv6`: [Протокол IPv6]({{< relref "2023-06-26-ipv6-protocol" >}})
    -   `latex3`: [Язык программирования LaTeX3]({{< relref "2024-01-01-latex3" >}})
    -   `latex`: [Система LaTeX]({{< relref "2024-01-01-latex" >}})
    -   `linux`: [Администрирование Linux]({{< relref "2023-06-07-linux-administration" >}})
    -   `network`:
    -   `org_mode`: [Org-mode]({{< relref "2021-10-14-org-mode" >}})
    -   `org_roam`: [Org-roam]({{< relref "2022-11-23-org-roam" >}})
    -   `pandoc`: [Pandoc]({{< relref "2021-08-28-pandoc" >}})
    -   `pdf`: [Формат PDF]({{< relref "2022-06-30-pdf-format" >}})
    -   `programming`: [Программирование]({{< relref "2023-08-05-programming" >}})
    -   `redhat`:
    -   `sysadmin`: [Системное администрирование]({{< relref "2021-04-10-system-administration" >}})
    -   `tex`: [Система TeX]({{< relref "2021-04-23-tex" >}})
    -   `typography`: [Типографика]({{< relref "2024-03-07-typography" >}})
    -   `vim`: [Редактор vim]({{< relref "2023-07-04-vim-editor" >}})
    -   `wayland`: [Wayland]({{< relref "2023-08-14-wayland" >}})
    -   `windows`: [Администрирование Windows]({{< relref "2021-05-01-windows-administration" >}})

-   `@games`: [Компьютерные игры]({{< relref "2022-06-07-computer-games" >}})
    -   `diablo`: [Игры. Diablo]({{< relref "2023-06-16-games-diablo" >}})
    -   `disciples`: [Disciples]({{< relref "2022-06-07-disciples-game" >}})
    -   `homm`: [Heroes of Might and Magic]({{< relref "2022-06-07-homm" >}})
    -   `mm`: [Might And Magic]({{< relref "2023-04-02-might-magic" >}})
-   `@job`: Работа
    -   `rudn`: [РУДН]({{< relref "2023-01-17-rudn" >}})
-   `@life`: [Жизнь]({{< relref "2021-11-26-life" >}})
    -   `apartment`: [Квартира]({{< relref "2022-12-16-apartment" >}})
    -   `appliance` : [Бытовая техника]({{< relref "2023-05-14-household-appliances" >}})
    -   `health`: [Здоровье]({{< relref "2022-10-19-health" >}})
    -   `money`: [Взгляд обывателя на финансы]({{< relref "2023-02-18-philistine-view-finance" >}})
    -   `recreation`: [Отдых]({{< relref "2023-01-17-recreation" >}})
-   `@physics`: [Физика]({{< relref "2024-01-07-physics" >}})
    -   `geometrization`: [Геометризация]({{< relref "2024-01-08-geometrization" >}})
    -   `kinetic`:
    -   `maxwell`: [Электродинамика]({{< relref "2024-01-08-electrodynamics" >}})
    -   `relatyvity`: [Теория относительности]({{< relref "2024-01-07-relativity" >}})

-   `@science`: [Научная деятельность]({{< relref "2021-02-01-scientific-activity" >}})
    -   `education`: [Образование]({{< relref "2024-06-02-education" >}})
    -   `modeling`: [Математическое моделирование]({{< relref "2021-02-21-mathematical-modeling" >}})
    -   `research`: [Научно-исследовательская деятельность]({{< relref "2021-02-01-research" >}})
    -   `science_admin`: [Научно-административная деятельность]({{< relref "2021-02-01-scientific-administrative" >}})
    -   `science_being`: [Бытие науки]({{< relref "2021-02-04-being-science" >}})
    -   `science_people`: [Люди науки]({{< relref "2024-01-12-science-people" >}})
    -   `science_writing`: [Научная писанина]({{< relref "2022-08-25-scientific-writing" >}})
    -   `teaching`: [Преподавание]({{< relref "2021-02-01-teaching" >}})

-   `@self_management`: Информация по самоорганизации, управлением временем, организации дел.
    -   `blog`: [Ведение блога]({{< relref "2023-03-17-blogging" >}})
    -   `gtd`: [Метод GTD]({{< relref "2021-07-12-gtd-method" >}})
    -   `zettelkasten`: [Метод Zettelkasten]({{< relref "2021-02-18-zettelkasten-method" >}})
    -   `read`: [Чтение]({{< relref "2023-12-05-read" >}})

-   `@thinking`: [Мысли]({{< relref "2021-12-14-reflections" >}})
    -   `sociology`: [Социологические заметки]({{< relref "2021-10-23-sociological-notes" >}})

| Уровень  | org-mode todo     | org-roam            | blog (ru)         | blog (en)         |
|----------|-------------------|---------------------|-------------------|-------------------|
| category |                   | `@computer_science` | computer-science  | computer-science  |
| tag      |                   | `hard`              |                   |                   |
| tag      |                   | `soft`              |                   |                   |
| tags     |                   | `gentoo`            |                   |                   |
| category | `@science`        | `@science`          | `сиянс`           | `science`         |
| tag      | `education`       | `education`         | `education`       | `education`       |
| tag      | `research`        | `research`          | `research`        | `research`        |
| tag      | `science_admin`   | `science_admin`     | `science-admin`   | `science-admin`   |
| tag      | `science_being`   | `science_being`     | `science-being`   | `science-being`   |
| tag      | `science_writing` | `science_writing`   | `science-writing` | `science-writing` |
| category |                   | `@book`             | листая-страницы   | through-the-pages |
| tag      |                   | `science_people`    | люди-науки        | science-people    |
| tag      |                   | `culture`           | культура          | culture           |
| category |                   | `@self_management`  | self-management   | self-management   |
| tag      |                   | `gtd`               | gtd               | gtd               |
| category |                   | `@life`             | жизнь             | life              |
| category |                   | `@reflections`      | мысли             | reflections       |
| category |                   | `@games`            | games             | games             |
| tag      |                   | `disciples`         | disciples         | disciples         |
| tag      |                   | `homm`              | homm              | homm              |

[^fn:1]: Всё, что имеет отношение к культуре (культурология, литературоведение).
[^fn:2]: Биографии учёных, мемуары учёных.
[^fn:3]: Это мой основной дистрибутив Linux.
