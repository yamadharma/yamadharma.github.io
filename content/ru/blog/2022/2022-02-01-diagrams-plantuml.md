---
title: "Диаграммы. PlantUML"
author: ["Dmitry S. Kulyabov"]
date: 2022-02-01T19:06:00+03:00
lastmod: 2023-07-20T13:04:00+03:00
tags: ["programming"]
categories: ["computer-science"]
draft: false
slug: "diagrams-plantuml"
---

-   Язык рисования диаграмм PlantUML.
-   PlantUML реализует концепцию _Diagram as Code_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Введение {#введение}

-   Сайт: <https://plantuml.com/>
-   Репозиторий: <https://github.com/plantuml/plantuml>
-   Список официальных тем: <https://the-lum.github.io/puml-themes-gallery/>
-   Язык реализации: Java.
-   В качестве бекэнда использует GraphViz.


## <span class="section-num">2</span> Поддерживаемые типы диаграмм {#поддерживаемые-типы-диаграмм}

-   UML диаграммы
    -   Диаграммы последовательности
    -   Диаграммы использования (прецедентов)
    -   Диаграммы классов
    -   Диаграммы объектов
    -   Диаграммы активности
    -   Диаграммы компонентов
    -   Диаграммы развёртывания
    -   Диаграммы состояний
    -   Диаграммы синхронизации
-   Не-UML диаграммы
    -   JSON данные
    -   Данные в формате YAML
    -   Диаграммы сети (nwdiag)
    -   Каркасный графический интерфейс
    -   Диаграммы ArchiMate
    -   Язык описания и спецификации (SDL)
    -   Диаграммы Ditaa
    -   Диаграммы Gantt
    -   Диаграммы MindMap
    -   Диаграммы иерархической структуры работ (WBS)
    -   Математика в нотации AsciiMath или JLaTeXMath
    -   Диаграммы типа сущность - связь (ER)


## <span class="section-num">3</span> Поддержка редактирования plantuml {#поддержка-редактирования-plantuml}

-   [Emacs. Plantuml]({{< relref "2022-10-20-emacs-plantuml" >}})
