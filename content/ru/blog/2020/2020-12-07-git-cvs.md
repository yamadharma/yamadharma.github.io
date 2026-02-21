---
title: "Система контроля версий git"
author: ["Dmitry S. Kulyabov"]
date: 2020-12-07T15:47:00+03:00
lastmod: 2026-02-17T15:37:00+03:00
tags: ["MOC", "git", "education", "programming"]
categories: ["computer-science"]
draft: false
slug: "git-cvs"
---

Использование системы контроля версий _git_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Использование git {#использование-git}

-   [Верификация коммитов git с помощью GPG]({{< relref "2021-01-28-verifying-git-commits-gpg" >}})
-   [Подпись коммитов git ключом ssh]({{< relref "2024-08-14-verifying-git-commits-ssh" >}})
-   [Варианты Git Workflow]({{< relref "2020-10-30-git-workflow" >}})
-   [Семантическое версионирование]({{< relref "2020-12-11-semantic-versioning" >}})
-   [Общепринятые коммиты]({{< relref "2020-12-11-conventional-commits" >}})
-   [git. Несколько удалённых репозиториев]({{< relref "2021-03-27-git-multiple-remote-repositories" >}})
-   [Практический сценарий использования git]({{< relref "2021-01-17-git-practical-use-case" >}})
-   [git submodules]({{< relref "2022-08-23-git-submodules" >}})
-   [Базовая настройка git]({{< relref "2024-03-16-git-basic-setup" >}})
-   [git. Авторизация по https]({{< relref "2025-08-19--git-authorization-https" >}})


### <span class="section-num">1.1</span> Взаимодествие с репозиториями {#взаимодествие-с-репозиториями}

-   [git. Клиент gcli]({{< relref "2025-01-22--git-gcli-client" >}})
-   [github: утилиты командной строки]({{< relref "2021-08-04-github-command-line-utilities" >}})
-   [Взаимодействие с gitea из командной строки]({{< relref "2023-11-11-interacting-gitea-command-line" >}})


## <span class="section-num">2</span> Хостинги git {#хостинги-git}

-   [Хостинг git. gitea]({{< relref "2023-10-29-git-hosting-gitea" >}})
-   [Хостинги git]({{< relref "2025-02-28--git-hostings" >}})
-   [Хостинги git. Ограничения на имена]({{< relref "2026-02-17--git-hosting-name-restrictions" >}})


## <span class="section-num">3</span> Расширения git {#расширения-git}

-   [Расширение git lfs]({{< relref "2023-11-13-git-lfs" >}})
-   [git. Пакет gir-repair]({{< relref "2025-01-03--git-git-repair" >}})


## <span class="section-num">4</span> Преподавание git {#преподавание-git}

Предполагается вводить git в лабораторные работы начиная с 1 курса.

-   1 курс
    -   Операционные системы (Архитектура ЭВМ)
        -   Работа с git даётся в стиле _monkey see, monkey do_.
        -   Основы работы в git.
        -   Создание учётной записи на Github.
        -   Выкладывание лабораторных работ на Git.
    -   Операционные системы
        -   Основы работы с git
            -   [Лабораторная работа Первоначальна настройка git]({{< relref "2022-04-06-lab-initial-git-setup" >}})
            -   Основы работы в git.
            -   Создание учётной записи на Github.
        -   Сценарии работы с git
            -   [Лабораторная работа Продвинутое использование git]({{< relref "2023-01-07-lab-extended-git-setup" >}})
            -   Формат коммитов и версий. Даётся as is, без особых пояснений.
            -   Выкладывание лабораторных работ на Git.
            -   Использование git-flow.
            -   Семантическое версионирование.
-   Для всех курсов
    -   Рабочее пространство курса располагается в git (см. [Рабочее пространство для лабораторной работы]({{< relref "2021-01-16-workspace-laboratory-work" >}})).
