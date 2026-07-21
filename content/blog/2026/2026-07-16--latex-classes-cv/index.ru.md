---
title: "LaTeX. Классы для резюме"
author: ["Dmitry S. Kulyabov"]
date: 2026-07-16T21:05:00+03:00
lastmod: 2026-07-16T21:58:00+03:00
draft: false
slug: "latex-classes-cv"
---

LaTeX. Классы для резюме

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Список на CTAN: <https://www.ctan.org/topic/cv>


## <span class="section-num">2</span> Основные классы {#основные-классы}


### <span class="section-num">2.1</span> moderncv {#moderncv}

-   CTAN: <https://www.ctan.org/pkg/moderncv>
-   Репозиторий: <https://github.com/moderncv/moderncv>

-   Подходит для большинства профессиональных и академических резюме.
-   Предлагает несколько готовых стилей (`classic`, `casual`, `banking` и др.) и цветовых тем.
-   Не поддерживает BibLaTeX (см. [bibtex vs biblatex]({{< relref "2022-09-11-bibtex-biblatex" >}})).


### <span class="section-num">2.2</span> koma-moderncvclassic {#koma-moderncvclassic}

-   CTAN: <https://www.ctan.org/pkg/koma-moderncvclassic>
-   Не отдельный класс, а пакет (sty), который решает одну конкретную проблему: несовместимость оригинального класса `moderncv` с BibLaTex.
-   В преамбуле вашего документа вы указываете класс KOMA-Script (обычно `scrartcl`), а затем подключаете сам пакет:
    ```tex
    \documentclass{scrartcl}
    \usepackage{koma-moderncvclassic}
    ```

-   После этого становятся доступны все команды `moderncv` для создания резюме (например, `\cventry`, `\cvline` и т.д.).

-   Пакет довольно старый. Его последняя версия датирована 2012 годом.
-   На сайте CTAN он помечен как `obsolete`.


### <span class="section-num">2.3</span> Awesome-CV {#awesome-cv}

-   Репозиторий: <https://github.com/posquit0/Awesome-CV>
-   Очень популярный шаблон с красивой типографикой, поддержкой иконок и цветовых схем. Отлично подходит для исследователей и дизайнеров.


### <span class="section-num">2.4</span> AltaCV {#altacv}

-   Репозиторий: <https://github.com/liantze/AltaCV>
-   Класс, основанный на дизайне резюме Мариссы Майер. Предлагает интересные варианты боковой панели и хорошо подходит для творческих профессий.


### <span class="section-num">2.5</span> Deedy-Resume {#deedy-resume}

-   Репозиторий: <https://github.com/Deedy/Deedy-Resume>
-   Двухколоночный дизайном.
-   Сделан для резюме на одной странице.


### <span class="section-num">2.6</span> Европейское резюме {#европейское-резюме}

-   Оригинальное европейское резюме было запущено в 2002 году и переименовано в Europass CV в 2004 году.
-   В 2013 году был проведен масштабный визуальный редизайн, в результате которого появилась более аккуратная и компактная структура (реализована в пакете europasscv).
-   В 2020 году Европейская комиссия запустила новую онлайн-платформу Europass со встроенным редактором резюме, представив множество новых шаблонов со значительно отличающимся визуальным оформлением.
-   Текущая версия платформы 2025 года предлагает еще более усовершенствованный набор шаблонов (реализована в пакете europasscv2025).


#### <span class="section-num">2.6.1</span> europecv (Europass CV) {#europecv--europass-cv}

-   CTAN: <https://www.ctan.org/pkg/europecv>
-   Репозиторий: <https://github.com/gsilano/EuropeCV>
-   Класс для создания резюме в формате Europass, который часто требуется в Европе.


#### <span class="section-num">2.6.2</span> europasscv (новая версия Europass CV) {#europasscv--новая-версия-europass-cv}

-   CTAN: <https://www.ctan.org/pkg/europasscv>
-   Репозиторий: <https://github.com/gmazzamuto/europasscv>
-   Класс для создания резюме в формате Europass, который часто требуется в Европе.


#### <span class="section-num">2.6.3</span> europasscv2025 {#europasscv2025}

-   CTAN: <https://www.ctan.org/pkg/europasscv2025>
-   Репозиторий: <https://github.com/Supercaly/europasscv2025>


### <span class="section-num">2.7</span> biblatex-cv {#biblatex-cv}

-   CTAN: <https://www.ctan.org/pkg/biblatex-cv>
-   Репозиторий: <https://github.com/danielshub/biblatex-cv>
-   Выглядит заброшенным.
-   Проще просто применить BibLaTeX.

-   Создаёт раздел с академическими публикациями в CV на основе файла BibTeX (`.bib`):
    -   форматирует записи в нужном стиле;
    -   группирует их по годам, типам (статьи, книги, тезисы конференций и т.д.) или другим критериям;
    -   сортирует в заданном порядке.


### <span class="section-num">2.8</span> komacv {#komacv}

-   CTAN: <https://www.ctan.org/pkg/komacv>

-   Пришел на смену устаревшему пакету `koma-moderncvclassic`.
-   Построен на классах KOMA-Script.
-   В комплекте идут три стиля оформления --- `classic`, `casual`, `oldstyle`.
-   Совместим с BibLaTeX.


#### <span class="section-num">2.8.1</span> Экосистема: komacv-rg {#экосистема-komacv-rg}

-   CTAN : <https://www.ctan.org/pkg/komacv-rg>
-   GitHub : <https://github.com/Ri-Ga/komacv-rg/>

-   Для расширения возможностей существует пакет `komacv-rg`.
-   Это набор из трех дополнительных пакетов:
    -   `komacv-addons` : коллекция дополнений и исправлений для основного класса.
    -   `komacv-lco` : позволяет использовать общие файлы настроек (Letter Class Options) между резюме `komacv` и сопроводительными письмами `scrlttr2`.
    -   `komacv-multilang` : упрощает создание и поддержку версий резюме на нескольких языках.


## <span class="section-num">3</span> Какой класс выбрать {#какой-класс-выбрать}

-   Начать проще всего: moderncv даст отличный результат с минимальными усилиями.
-   Для технических специалистов (IT, инженерия): Deedy-Resume или Awesome-CV.
-   Для академической сферы (с публикациями): Awesome-CV. Хорошо подходят для длинных CV с большим списком публикаций.
-   Для работы в Европе: europecv, europasscv, europasscv2025. Это стандартизированный формат, который могут ожидать увидеть работодатели.
