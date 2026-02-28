---
title: "Emacs. Персональная база знаний"
author: ["Dmitry S. Kulyabov"]
date: 2023-11-07T15:54:00+03:00
lastmod: 2026-02-28T20:56:00+03:00
tags: ["org-roam", "emacs", "zettelkasten"]
categories: ["computer-science", "self-management"]
draft: false
slug: "emacs-personal-knowledge-base"
---

-   Организация персональной базы знаний на Emacs.
-   Пакеты можно сгруппировать по сервисам, аналоги которых они хотят реализовать.
-   Или идеям реализации сервиса.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Ориентация на Roam Research {#ориентация-на-roam-research}

-   Roam Research
-   Сайт: <https://roamresearch.com/>
-   Популярный сервис ведения заметок.


### <span class="section-num">1.1</span> Org Roam {#org-roam}

-   [Org-roam]({{< relref "2022-11-23-org-roam" >}})
-   Самый известный проект в области системе типа Zettelkasten на Emacs.
-   Имеет достаточно большое количество сопутствующих пакетов.


#### <span class="section-num">1.1.1</span> Сопутствующие проекты Org-roam {#сопутствующие-проекты-org-roam}

<!--list-separator-->

1.  Визуализация

    <!--list-separator-->

    1.  org-roam-ui

        -   Графический интерфейс, строящий граф для заметок org-roam.
        -   Визуализация связей между заметками.

        <!--list-separator-->

        1.  org-roam/org-roam-ui

            -   Репозиторий: <https://github.com/org-roam/org-roam-ui>.
            -   Подключение: <http://127.0.0.1:35901/>
            -   Давно не обновляется.
            -   У меня перестало показывать что-либо.

        <!--list-separator-->

        2.  lkarp-744/org-roam-ui

            -   Репозиторий: <https://github.com/lkarp-744/org-roam-ui>
            -   Неофициальный форк.
            -   Обновляется.
            -   Подключение: <http://127.0.0.1:35901/>

    <!--list-separator-->

    2.  org-roam-ui-lite

        -   Репозиторий: <https://github.com/tani/org-roam-ui-lite>

    <!--list-separator-->

    3.  roam-viz

        -   Репозиторий: <https://github.com/kkrausse/roam-viz>

<!--list-separator-->

2.  Разные форматы

    <!--list-separator-->

    1.  md-roam

        -   Репозиторий: <https://github.com/nobiot/md-roam>
        -   Поддержка файлов Markdown.
        -   Смешивание файлов Markdown с файлами Org в одной базе данных Org-roam для заметок и обратных ссылок в стиле Zettelkasten.

<!--list-separator-->

3.  BibTeX

    <!--list-separator-->

    1.  org-roam-bibtex

        -   Репозиторий: <https://github.com/org-roam/org-roam-bibtex>.
        -   Интеграция org-roam с программным обеспечением для управления библиографией.

    <!--list-separator-->

    2.  citar-org-roam

        -   Репозиторий: <https://github.com/emacs-citar/citar-org-roam>
        -   Интеграция Citar и Org-Roam.

<!--list-separator-->

4.  Zettelkasten

    -   [Метод Zettelkasten]({{< relref "2021-02-18-zettelkasten-method" >}})

    <!--list-separator-->

    1.  zetteldesk.el

        -   Репозиторий: <https://github.com/Vidianos-Giannitsis/zetteldesk.el>
        -   Навигация по заметкам.

    <!--list-separator-->

    2.  vulpea

        -   Репозиторий: <https://github.com/d12frosted/vulpea>
        -   Библиотека для расширения возможности ведения заметок в org-roam.

    <!--list-separator-->

    3.  org-workbench

        -   Реализует систему цифровых карточек для работы в духе Zettelkasten.
        -   [Emacs. Пакет org-workbench]({{< relref "2026-02-28--emacs-org-workbench" >}})

<!--list-separator-->

5.  Folgezettel

    -   [Нумерация Folgezettel]({{< relref "2025-02-08--folgezettel-numbering" >}})

    <!--list-separator-->

    1.  org-roam-folgezettel

        -   Репозиторий: <https://github.com/krisbalintona/org-roam-folgezettel>

    <!--list-separator-->

    2.  org-roam-fz

        -   Репозиторий: <https://github.com/okomestudio/org-roam-fz>
        -   Репозиторий помечен как read-only <span class="timestamp-wrapper"><span class="timestamp">[2026-02-28 Сб]</span></span>.

<!--list-separator-->

6.  Дневник

    -   [Emacs. Пакет org-daily-reflection]({{< relref "2025-06-06--emacs-org-daily-reflection" >}})
    -   [Org-roam. Daily notes]({{< relref "2025-06-08--org-roam-daily-notes" >}})

<!--list-separator-->

7.  Разные улучшения

    <!--list-separator-->

    1.  org-roam-more

        -   Репозиторий: <https://github.com/gongshangzheng/org-roam-more>
        -   Расширенное управление трансклюзией.
        -   Синхронизация содержимого между узлами.
        -   Утилиты манипулирования содержимым узлов.
        -   Иерархические операции с узлами.

    <!--list-separator-->

    2.  org-roam-download

        -   Репозиторий: <https://github.com/selwynsimsek/org-roam-download>
        -   Используется для загрузки и размещения ссылок на вложения, такие как PDF-файлы или изображения, в узлах org-roam, которые создаются во время веб-серфинга.

    <!--list-separator-->

    3.  org-transclusion-power-pack

        -   Репозиторий: <https://github.com/incandescentman/org-transclusion-power-pack>
        -   Набор улучшений для пакета `org-transclusion` (позволяет динамически отображать содержимое одного org-файла в другом).
        -   Включение и выключение трансклюзии одним нажатием клавиши.
        -   Функция добавления узла org-roam в качестве трансклюзии.
        -   Функция добавления трансклюзии и соответствия текущему уровню org-заголовка.
        -   Более интуитивные названия функций для облегчения навигации.

    <!--list-separator-->

    4.  org-roam-ok

        -   Репозиторий: <https://github.com/okomestudio/org-roam-ok>
        -   Информация в строке мини-буфера.
        -   Автоматическое создание отсутствующих родительских каталогов.
        -   Кэширование в памяти для ускорения поиска узлов.


### <span class="section-num">1.2</span> Gkroam {#gkroam}

-   Репозиторий: <https://github.com/Kinneyzhang/gkroam>
-   Реализация Roam Research для Emacs.
-   Последняя активность в 2022 году.


## <span class="section-num">2</span> Ориентация на TheBraine {#ориентация-на-thebraine}

-   Сайт: <https://www.thebrain.com/>
-   Визуализирование ведение заметок.
-   Похоже на Mindmap или концептуальные карты.


### <span class="section-num">2.1</span> org-brain {#org-brain}

-   Репозиторий: <https://github.com/Kungsgeten/org-brain>


## <span class="section-num">3</span> Ориентация на идею Zettelkasten {#ориентация-на-идею-zettelkasten}

-   [Метод Zettelkasten]({{< relref "2021-02-18-zettelkasten-method" >}})
-   Большое внимание уделяется нумерации Лумана.
-   Реализуются обратные ссылки.


### <span class="section-num">3.1</span> denote {#denote}

-   [Emacs. Пакет denote]({{< relref "2025-01-03--emacs-denote" >}})
-   Репозиторий: <https://github.com/protesilaos/denote>
-   Документация: <https://protesilaos.com/emacs/denote>
-   Большое внимание уделяется схеме именования файлов.
-   Поддерживает реализацию цепочек заметок (Folgezettel, см. [Нумерация Folgezettel]({{< relref "2025-02-08--folgezettel-numbering" >}})) (см. [Denote. Соглашение об именовании]({{< relref "2025-01-03--denote-naming-convention" >}}))
-   Поддерживает любые текстовые форматы файлов.
-   Информация кодируется в названии файла.
-   Название файла следует строгим соглашениям.


### <span class="section-num">3.2</span> ekg {#ekg}

-   ekg (emacs knowledge graph)
-   Репозиторий: <https://github.com/ahyatt/ekg>
-   Данные хранятся в базе данных sqlite.
-   Заметки организованы по тегам.
-   Можете просмотреть множество заметок, просматривая один или несколько тегов.


### <span class="section-num">3.3</span> howm {#howm}

-   Репозиторий: <https://github.com/kaorahi/howm>
-   Сайт: <https://kaorahi.github.io/howm/>


### <span class="section-num">3.4</span> org-zk {#org-zk}

-   Репозиторий: <https://github.com/villarragut/org-zk>
-   Пакет для Zettelcasten в духе Denote.
-   Использует формат org.


### <span class="section-num">3.5</span> phi-notes {#phi-notes}

-   Репозиторий: <https://github.com/brunocbr/phi-notes>
-   Особенности:
    -   Заметки идентифицируются уникальными последовательными номерами или временными метками.
    -   Заметки могут быть связаны с использованием синтаксиса вики-ссылок.
    -   Примечания могут иметь родительские и дочерние примечания.
    -   Библиографические аннотации поддерживаются ссылками BibTeX.
    -   Заметки могут иметь теги.
    -   Для хранения метаданных используется формат YAML.
    -   Заметки могут быть написаны в Markdown.


### <span class="section-num">3.6</span> zetteldeft {#zetteldeft}

-   Репозиторий: <https://github.com/EFLS/zetteldeft>
-   Документация: <https://www.eliasstorms.net/zetteldeft/>
-   Автор перешёл на Denote и забросил пакет.


### <span class="section-num">3.7</span> zk {#zk}

-   Репозиторий: <https://github.com/localauthor/zk>


## <span class="section-num">4</span> Поиск по файлам {#поиск-по-файлам}

-   При работе с большим количеством файлов возникает задача поиска в них.
-   Группа пакетов пытается решить эту проблему.
-   Это, скорее, вспомогательные пакеты.


### <span class="section-num">4.1</span> deft {#deft}

-   [Emacs. Пакет Deft]({{< relref "2024-04-15-emacs-deft" >}})
-   Репозиторий: <https://github.com/jrblevin/deft>
-   Документация: <https://jblevins.org/projects/deft/>
-   Режим для быстрого просмотра, фильтрации и редактирования каталогов заметок.
-   Медленно работает при среднем количестве заметок (несколько тысяч).
-   Можно использовать с другими режимами.


### <span class="section-num">4.2</span> notdeft {#notdeft}

-   Репозиторий: <https://github.com/hasu/notdeft>
-   Документация: <https://tero.hasu.is/notdeft/>
-   Ответвление от Deft.
-   Использует движок Xapian.


## <span class="section-num">5</span> Ссылки {#ссылки}


### <span class="section-num">5.1</span> org-super-links {#org-super-links}

-   Репозиторий: <https://github.com/toshism/org-super-links>
-   Создание ссылок с автоматическими обратными ссылками.
-   Пример:
    ```org
    ​* TODO Test heading target
      :PROPERTIES:
      :ID:       02a5da87-46e5-4ae0-85c1-ee63a570270a
      :END:
      :BACKLINKS:
      [2020-04-11 Sat 00:26] <- [[id:3835d3d0-931a-4a45-a015-a3d6a0baa99a][This has a link]]
      :END:

    This has a backlink as you can see from the BACKLINKS drawer above.

    * TODO This has a link
      :PROPERTIES:
      :ID:       3835d3d0-931a-4a45-a015-a3d6a0baa99a
      :END:

    This has a link pointing to the heading above

    [[id:02a5da87-46e5-4ae0-85c1-ee63a570270a][Test heading target]]
    ```
-   Для поиска использует org-ql.
