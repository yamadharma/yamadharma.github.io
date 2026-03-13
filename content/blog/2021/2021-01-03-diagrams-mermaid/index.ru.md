---
title: "Диаграммы. Mermaid"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-03T14:19:00+03:00
lastmod: 2025-03-24T14:56:00+03:00
tags: ["programming"]
categories: ["computer-science"]
draft: false
slug: "diagrams-mermaid"
---

-   Язык рисования диаграмм Mermaid.
-   Mermaid реализует концепцию _Diagram as Code_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Mermaid --- язык программирования для рисования диаграмм и библиотека для визуализации.
-   Инструментарий написан на javascript.


### <span class="section-num">1.1</span> Ресурсы {#ресурсы}

-   Страница Mermaid: <https://mermaid-js.github.io/>
-   Страница на github: <https://github.com/mermaid-js/mermaid>
-   Утилита командной строки: <https://github.com/mermaid-js/mermaid-cli>
-   HTTP сервер: <https://github.com/TomWright/mermaid-server>
-   Онлайн редактор: <https://mermaid-js.github.io/mermaid-live-editor/>


### <span class="section-num">1.2</span> Интеграция {#интеграция}

-   Интегрирован в системы рендеринга языка Markdown
    -   Pandoc: <https://pandoc.org/>
    -   Hugo: <https://gohugo.io/>
-   Хостинги кода (в файлах `README.md`)
    -   GitHub: <https://github.com/>
    -   GitLab: <https://gitlab.com/>
    -   Gitea: <https://gitea.io/>
-   Приложения работы с текстом (markdown)
    -   Joplin: <https://joplinapp.org/>
    -   Notion: <https://www.notion.so/>


### <span class="section-num">1.3</span> Внедрение _Mermaid_ в _Markdown_ {#внедрение-mermaid-в-markdown}

-   Для блока кода, отмеченного как `mermaid`:
    -   система создаёт новый фрейм `iframe`,
    -   необработанный код из блока передаётся его в _Mermaid.js_,
    -   код преобразуется в диаграмму.
-   Пример входного кода
    ````markdown
    ```mermaid
      graph TD;
          A-->B;
          A-->C;
          B-->D;
          C-->D;
    ```
    ````
-   Результирующее изображение
    ````mermaid
    graph TD;
        A-->B;
        A-->C;
        B-->D;
        C-->D;
    ````


### <span class="section-num">1.4</span> Поддерживаемые типы диаграмм {#поддерживаемые-типы-диаграмм}

-   Блок-схемы (Flowchart)
-   Диаграммы состояния (Sequence diagram)
-   Диаграммы Ганта (Gantt diagram)
-   UML-диаграммы классов (Class diagram)
-   Графы git (Git graph)
-   ER-диаграммы (Entity Relationship Diagram)
-   Диаграммы пользовательского пути (User Journey Diagram)
-   Диаграммы последовательности (Sequence diagrams)
-   Круговые диаграммы (Pie chart)


## <span class="section-num">2</span> Установка {#установка}

-   Необходимо установить программу `mmdc` из проекта <https://github.com/mermaid-js/mermaid-cli>.
-   С помощью yarn:
    ````shell
    yarn global add @mermaid-js/mermaid-cli
    ````
-   С помощью pnpn:
    ````shell
    pnpm install -g @mermaid-js/mermaid-cli
    ````


## <span class="section-num">3</span> Синтаксис {#синтаксис}

-   `%%`: комментарий в коде.


## <span class="section-num">4</span> Типы диаграмм {#типы-диаграмм}


### <span class="section-num">4.1</span> Блок-схемы (Flowchart) {#блок-схемы--flowchart}

-   Один из вариантов представления блок-схем.


#### <span class="section-num">4.1.1</span> Синтаксис {#синтаксис}

-   Ключевое слово: `flowchart` и аббревиатуры для указания направления.
-   `subgraph <имя>`: задаёт поддиаграммы.
    -   `end`: завершает описание поддиаграммы.
-   Основная часть диаграммы --- это узлы.
    -   Текст на диаграмме узла берётся из названия.
    -   Альтернативно можно указать отображаемый текст в квадратных скобках.
    -   Форма узлов задаётся скобочными символами вокруг текста.
    -   Для экранирования используют кавычки.
        -   Всё содержимое в кавычках считается текстом.
-   `click`: задаёт ссылку для узла.
    ````markdown
    click <узел> "<ссылка>" <_blank>
    ````

    -   Ссылка заключается в кавычки.
    -   `_blank`: указывает открыть ссылку в новой вкладке.
-   Направление диаграммы:
    -   `TB`: сверху вниз (top to bottom);
    -   `TD`: сверху вниз (top-down);
    -   `BT`: снизу вверх (bottom to top);
    -   `RL`: справа налево (right to left);
    -   `LR`: слева направо (left to right).
-   `style`: задаёт оформление диаграммы.
    ````markdown
    style <узел> <style_tag:значение>,<style_tag:значение>
    ````

    -   Теги стилей:
        -   `fill`: заливка;
        -   `stroke`: цвет границы;
        -   `stroke-width`: толщина границы;
        -   `color`: цвет текста;
        -   `stroke-dasharray`: пунктирная граница.
    -   `classDef`: задаёт класс, содержащий набор стилей.
        ````markdown
        classDef <имя_класса> <style_tag:значение>,<style_tag:значение>
        ````

        -   `:::` указывает класс после имени узла.


#### <span class="section-num">4.1.2</span> Примеры {#примеры}

-   Блок

    ```
      flowchart TB
         node
    ```

    ````mermaid
    flowchart TB
       node
    ````
-   Блок с текстом

    ```
      flowchart TB
         node[Текст]
    ```

    ````mermaid
    flowchart TB
       node[Текст]
    ````
-   Формы узлов

    ```
      flowchart TB
        node1[Форма 1]
        node2(Форма 2)
        node3([Форма 3])
        node4[[Форма 4]]
        node5[(Форма 5)]
        node6((Форма 6))
        node7>Форма 7]
        node8{Форма 8}
        node9{{Форма 9}}
        node10[/Форма 10/]
        node11[\Форма 11\]
        node12[/Форма 12\]
        node13[\Форма 13/]
    ```

    ````mermaid
    flowchart TB
      node1[Форма 1]
      node2(Форма 2)
      node3([Форма 3])
      node4[[Форма 4]]
      node5[(Форма 5)]
      node6((Форма 6))
      node7>Форма 7]
      node8{Форма 8}
      node9{{Форма 9}}
      node10[/Форма 10/]
      node11[\Форма 11\]
      node12[/Форма 12\]
      node13[\Форма 13/]
    ````
-   Стрелки

    ```
      flowchart TB
         А --> B
         C --- D
         E -.-> F
         G ==> H
         I --o J
         K --x L
    ```

    ````mermaid
    flowchart TB
       А --> B
       C --- D
       E -.-> F
       G ==> H
       I --o J
       K --x L
    ````

-   Стрелки с текстом

    ```
      flowchart TD
          A -- Text --- B
          C --- |Text| D
          E --> |Text| F
          G -- Text --> H
          I -. Text .-> J
          K == Text ==> L
    ```

    ````mermaid
    flowchart TD
        A -- Text --- B
        C --- |Text| D
        E --> |Text| F
        G -- Text --> H
        I -. Text .-> J
        K == Text ==> L
    ````
-   Поддиаграммы

    ```
      flowchart TB
          c1 --> a2
          subgraph one
              a1 --> a2
          end
          subgraph two
              b1 --> b2
          end
          subgraph three
              c1 --> c2
          end
    ```

    ````mermaid
    flowchart TB
        c1 --> a2
        subgraph one
            a1 --> a2
        end
        subgraph two
            b1 --> b2
        end
        subgraph three
            c1 --> c2
        end
    ````
-   Ссылки

    ```
      flowchart TB
          A --> B
          click A "http://www.github.com" _blank
    ```

    ````mermaid
    flowchart TB
        A --> B
        click A "http://www.github.com" _blank
    ````
-   Стили

    ```
      flowchart LR
          id1(Start)-->id2(Stop)
          style id1 fill:#3f3,stroke:#333,stroke-width:4px
          style id2 fill:#ff2400,stroke:#333,stroke-width:4px,color:#fff,stroke-dasharray: 12 5
    ```

    ````mermaid
    flowchart LR
        id1(Start)-->id2(Stop)
        style id1 fill:#3f3,stroke:#333,stroke-width:4px
        style id2 fill:#ff2400,stroke:#333,stroke-width:4px,color:#fff,stroke-dasharray: 12 5
    ````
-   Классы стилей

    ```
      flowchart LR
          classDef class1 fill:#3f3,stroke:#333,stroke-width:4px
          classDef class2 fill:#ff2400,stroke:#333,stroke-width:4px,color:#fff,stroke-dasharray: 12 5

          A(Start):::class1 --> B(Stop):::class2
    ```

    ````mermaid
    flowchart LR
        classDef class1 fill:#3f3,stroke:#333,stroke-width:4px
        classDef class2 fill:#ff2400,stroke:#333,stroke-width:4px,color:#fff,stroke-dasharray: 12 5

        A(Start):::class1 --> B(Stop):::class2
    ````


### <span class="section-num">4.2</span> Диаграммы состояния (Sequence diagram) {#диаграммы-состояния--sequence-diagram}


#### <span class="section-num">4.2.1</span> Синтаксис {#синтаксис}


#### <span class="section-num">4.2.2</span> Примеры {#примеры}


### <span class="section-num">4.3</span> Диаграммы Ганта (Gantt diagram) {#диаграммы-ганта--gantt-diagram}


#### <span class="section-num">4.3.1</span> Синтаксис {#синтаксис}


#### <span class="section-num">4.3.2</span> Примеры {#примеры}


### <span class="section-num">4.4</span> UML-диаграммы классов (Class diagram) {#uml-диаграммы-классов--class-diagram}


#### <span class="section-num">4.4.1</span> Синтаксис {#синтаксис}


#### <span class="section-num">4.4.2</span> Примеры {#примеры}


### <span class="section-num">4.5</span> Графы git (Git graph) {#графы-git--git-graph}

-   Описание стратегии ветвления _git_.


#### <span class="section-num">4.5.1</span> Синтаксис {#синтаксис}

-   Ключевое слово: `gitGraph`.
-   `options`: задаёт параметры отображения.
-   `commit`: отображается кружочком с хешем.
    -   Хеш коммита генерится автоматически.
-   `checkout <branch>`: переключает на новую ветку.
-   `merge <branch>`: сливает ветки.


#### <span class="section-num">4.5.2</span> Примеры {#примеры}

-   Простое ветвление

    ```
      gitGraph:
      options
      {
          "nodeSpacing": 100,
          "nodeRadius": 10
      }
      end
      commit
      branch newbranch
      checkout newbranch
      commit
      commit
      checkout master
      commit
      commit
      merge newbranch
    ```

    ````mermaid
    gitGraph:
    options
    {
        "nodeSpacing": 100,
        "nodeRadius": 10
    }
    end
    commit
    branch newbranch
    checkout newbranch
    commit
    commit
    checkout master
    commit
    commit
    merge newbranch
    ````


### <span class="section-num">4.6</span> ER-диаграммы (Entity Relationship Diagram) {#er-диаграммы--entity-relationship-diagram}


#### <span class="section-num">4.6.1</span> Синтаксис {#синтаксис}


#### <span class="section-num">4.6.2</span> Примеры {#примеры}


### <span class="section-num">4.7</span> Диаграммы пользовательского пути (User Journey Diagram) {#диаграммы-пользовательского-пути--user-journey-diagram}

-   С помощью диаграммы пользовательского пути можно продемонстрировать процесс использования или реализации чего-либо.
-   Указывается набор пользователей и их удовлетворение процессом.


#### <span class="section-num">4.7.1</span> Синтаксис {#синтаксис}

-   `journey`: начинает диаграмму.
-   `title`: название диаграммы.
-   `section`: раздел диаграммы.
    -   В каждом разделе указываются конкретные шаги с оценкой по десятибалльной шкале и закреплённое за действием лицо.
    -   `:` разделитель полей.


#### <span class="section-num">4.7.2</span> Примеры {#примеры}

-   Простая диаграмма пользовательского пути

    ```
      journey
          title Процесс написания статьи
          section Поиск / изучение
            Поиск информации: 5: Я
            Структурирование: 5: Я
          section Пишем
            Пишем черновик: 5: Я
            Готовим картинки: 4: Я
          section Редактируем
              Проверяем: 3: Я, Соавтор
              Финальные правки: 2: Я
          section Публикация
              Публикуем: 5: Я
              Радуемся: 8: Я, Соавтор
    ```

    ````mermaid
    journey
        title Процесс написания статьи
        section Поиск / изучение
          Поиск информации: 5: Я
          Структурирование: 5: Я
        section Пишем
          Пишем черновик: 5: Я
          Готовим картинки: 4: Я
        section Редактируем
            Проверяем: 3: Я, Соавтор
            Финальные правки: 2: Я
        section Публикация
            Публикуем: 5: Я
            Радуемся: 8: Я, Соавтор
    ````


### <span class="section-num">4.8</span> Диаграммы последовательности (Sequence diagrams) {#диаграммы-последовательности--sequence-diagrams}


#### <span class="section-num">4.8.1</span> Синтаксис {#синтаксис}


#### <span class="section-num">4.8.2</span> Примеры {#примеры}


### <span class="section-num">4.9</span> Круговые диаграммы (Pie chart) {#круговые-диаграммы--pie-chart}

-   Показывает, какую часть от общего числа занимает отдельные части.


#### <span class="section-num">4.9.1</span> Синтаксис {#синтаксис}

-   Ключевое слово: `pie`.
-   Оператор `title` позволяет задать название диаграммы.
    -   `title` можно опустить, тогда диаграмма будет безымянной.
-   Строки с названиями элементов.
    -   Данные записываются построчно следующим образом:
        -   название в кавычках;
        -   разделитель в виде двоеточия;
        -   положительное числовое значение (поддерживается до двух знаков после запятой).


#### <span class="section-num">4.9.2</span> Примеры {#примеры}

-   Домашние животные

    ```
      pie title Домашние животные
          "Собаки" : 386
          "Кошки" : 85
          "Хомячки" : 15
    ```

    ````mermaid
    pie title Домашние животные
        "Собаки" : 386
        "Кошки" : 85
        "Хомячки" : 15
    ````
