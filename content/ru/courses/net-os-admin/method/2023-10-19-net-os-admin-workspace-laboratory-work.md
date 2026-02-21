---
title: "Рабочее пространство для лабораторной работы"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-19T17:57:00+03:00
lastmod: 2025-07-02T16:43:00+03:00
tags: ["education", "sysadmin"]
categories: ["computer-science"]
draft: false
weight: 810
toc: true
type: "docs"
feedback: false
summary: "Рабочее пространство для лабораторной работы"
linktitle: "Рабочее пространство для лабораторной работы"
menu:
  "net-os-admin-workspace-laboratory-work":
    parent: "net-os-admin-method"
    weight: 810
    identifier: "net-os-admin-workspace-laboratory-work"
---

При выполнении лабораторной работы следует придерживаться структуры рабочего пространства.

<!--more-->


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Описание построено на рекомендациях [Рабочее пространство для лабораторной работы]({{< relref "2021-01-16-workspace-laboratory-work" >}}).
-   Репозиторий: <https://github.com/yamadharma/course-directory-student-template>.
-   Репозиторий с примерами кода: <https://github.com/yamadharma/net-os-admin-lab-code>
-   Аббревиатура курса: `net-os-admin`
-   Учебный год: 2025--2026


## <span class="section-num">2</span> Создание репозитория для курса Администрирование сетевых подсистем {#создание-репозитория-для-курса-администрирование-сетевых-подсистем}

-   Создадим репозиторий с помощью утилит командной строки gh (см. [github: утилиты командной строки]({{< relref "2021-08-04-github-command-line-utilities" >}})):
    ```shell
    mkdir -p ~/work/study/2025-2026/"Администрирование сетевых подсистем"
    cd ~/work/study/2025-2026/"Администрирование сетевых подсистем"
    gh repo create study_2025-2026_net-os-admin --template=yamadharma/course-directory-student-template --public
    git clone --recursive git@github.com:<owner>/study_2025-2026_net-os-admin.git net-os-adminy
    ```


## <span class="section-num">3</span> Настройка каталога курса {#настройка-каталога-курса}

-   При создании структуры название курса берётся из следующих мест:
    -   название курса находится в файле `COURSE`;
    -   каталог курса называется как аббревиатура курса.
-   Перейдите в каталог курса:
    ```shell
    cd ~/work/study/2025-2026/"Администрирование сетевых подсистем"/net-os-admin
    ```
-   Создайте необходимые каталоги:
    ```shell
    make prepare
    ```
-   Отправьте файлы на сервер:
    ```shell
    git add .
    git commit -am 'feat(main): make course structure'
    git push
    ```


## <span class="section-num">4</span> Видео {#видео}

{{< tabs tabTotal="3" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 20ca1a0b52e1e900445be6cab5c5a2ac >}}

{{< /rtab >}}
{{< rtab tabName="VKVideo" >}}

{{< vkvideo oid="606414976" id="456239573" hd="2" >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube CUSA_V8dIrE >}}

{{< /rtab >}}
{{< /tabs >}}
