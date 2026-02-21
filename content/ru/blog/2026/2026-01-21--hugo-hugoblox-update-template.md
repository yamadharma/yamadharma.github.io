---
title: "Hugo. HugoBlox. Обновление шаблонов"
author: ["Dmitry S. Kulyabov"]
date: 2026-01-21T21:54:00+03:00
lastmod: 2026-02-21T19:53:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "hugo-hugoblox-update-template"
---

Hugo. HugoBlox. Обновление шаблонов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> До версии 5.3 {#до-версии-5-dot-3}

-   Примечания до версии 5.3 находятся в блоге <https://wowchemy.com/blog/>.
-   В файле `go.mod` установите необходимую версию (например, `5.3`), исправив строку:
    ```conf-unix
    require (
            github.com/wowchemy/wowchemy-hugo-modules/v5 v5.3.0
    )
    ```
-   Обновите пути к модулям в конфигурации в файле `config/_default/config.yaml`:
    ```yaml
    module:
      imports:
    ​    - path: github.com/wowchemy/wowchemy-hugo-modules/wowchemy-cms/v5
    ​    - path: github.com/wowchemy/wowchemy-hugo-modules/wowchemy/v5
    ```
    или `config/_default/config.toml`:
    ```toml
    [module]
      [[module.imports]]
        path = "github.com/wowchemy/wowchemy-hugo-modules/wowchemy-cms/v5"
      [[module.imports]]
        path = "github.com/wowchemy/wowchemy-hugo-modules/wowchemy/v5"
    ```
-   Для использования с _netlify_:
    -   Обновите `HUGO_VERSION` в `netlify.toml` до необходимой версии `0.84.4`.
-   Обновите модуль:
    -   текущий релиз:
        ```shell
        hugo mod get -u
        ```
    -   текущая версия разработчика:
        ```shell
        hugo mod get -u ./...
        ```


## <span class="section-num">2</span> Общие рекомендации {#общие-рекомендации}

-   Текущую версию можно найти:
    -   в файле `themes/academic/data/academic.toml` (если всё делалось очень давно);
    -   в файле `go.mod`:
        -   точная версия (например, `v5.0.0`);
        -   версия сборки в ​​​​форме `v<dummy-version-number>-<date>-<build-number>`.
-   Отредактируйте файл `go.mod`:
    ```conf-unix
    module my_website

    go 1.15

    require (
            github.com/HugoBlox/hugo-blox-builder/modules/blox-bootstrap/v5 v5.9.6
            github.com/HugoBlox/hugo-blox-builder/modules/blox-plugin-netlify v1.1.2-0.20231108141515-0478cf6921f9
            github.com/HugoBlox/hugo-blox-builder/modules/blox-plugin-reveal v1.1.2
    )
    ```

    -   Вы настраиваете версию модуля в операторе `require`.
    -   ~~Вместо версии `main` можно задать конкретную версию модуля (в формате `v5.x.y`).~~
-   Обновите пути модулей в файле `config/_default/module.yaml`:
    ```yaml
    imports:
    ​  - path: github.com/HugoBlox/hugo-blox-builder/modules/blox-plugin-netlify
    ​  - path: github.com/HugoBlox/hugo-blox-builder/modules/blox-plugin-reveal
    ​  - path: github.com/HugoBlox/hugo-blox-builder/modules/blox-bootstrap/v5
    ```
-   Определите необходимую версию `hugo` (`HUGO_VERSION`) (возьмите из примечания к выпуску <https://github.com/HugoBlox/hugo-blox-builder/releases>).
-   Проверьте, что локальная версия _Hugo Extended_ имеет необходимую версию.
-   Последовательно примените любые критические изменения из соответствующих примечаний к выпуску. Если в релизе нет раздела _Breaking Changes_, то никаких изменений не требуется.
-   Обновите модули темы:
    -   до последней официальной версии:
        ```shell
        hugo mod get -u
        ```
    -   до текущей версии в репозитории:
        ```shell
        hugo mod get -u ./...
        ```
-   После этого `main` в `go.mod` будет заменена на конкретную версию.
-   Если Вы обновляете совсем старую версию, Вам может быть проще создать новый сайт и перенести папку `content`.


## <span class="section-num">3</span> Миграция на tailwind {#миграция-на-tailwind}


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   Последний релиз на bootstrap вышел 2023-11-14.
-   Далее релиз стал базироваться на tailwind.
-   Сайт tailwind:
    -   <https://tailwindcss.com/>
    -   <https://tailwindcss.ru/>


### <span class="section-num">3.2</span> Основные изменения {#основные-изменения}


#### <span class="section-num">3.2.1</span> Первая страница {#первая-страница}

-   Вместо отдельных файлов-блоков в каталоге `content/home` осуществлён переход к страницам типа `landing`:
    -   `content/_index.md`;
    -   `content/experience.md`;
    -   `content/projects.md`.


#### <span class="section-num">3.2.2</span> Публикации типа book {#публикации-типа-book}

-   [Hugo. Wowchemy. Book]({{< relref "2022-11-22-hugo-wowchemy-book" >}})
-   Тип публикации `book` отсутствует.
-   Вместо него следует использовать тип `docs`:
    ```yaml
    type: docs
    ```
-   Убран шорткод:
    ```text
    {{</* list_children */>}}
    ```


#### <span class="section-num">3.2.3</span> Поиск {#поиск}

-   Теперь необходимо создать индекс поиска отдельно.
-   Сначала сгенерим страницы сайта, потом создадим индекс поиска, после можно запустить `hugo server` для просмотра:
    ```shell
    hugo && \
    npm_config_yes=true npx pagefind --site "public" --output-subdir ../static/pagefind && \
    hugo server -D
    ```


## <span class="section-num">4</span> Обновление до blox-tailwind/v0.8.0 {#обновление-до-blox-tailwind-v0-dot-8-dot-0}


### <span class="section-num">4.1</span> Общая информация {#общая-информация}

-   Релиз: <https://github.com/HugoBlox/kit/releases/tag/modules%2Fblox-tailwind%2Fv0.8.0>
-   Меняются именования каталогов.
-   Рекомендуется использовать фиксированные названия каталогов.
-   В Hugo Blox стандартизированы типы контента:

| Старый тип контента | Новый тип контента |
|---------------------|--------------------|
| `post`              | `blog`             |
| `publication`       | `publications`     |
| `project`           | `projects`         |
| `event`             | `events`           |
| `teaching`          | `courses`          |

-   Типы коллекций используют имена во множественном числе (`blog` является исключением, но это стандартная практика).

-   Меняются
    -   `page_type:`
-   Перестал работать ручной метод развёртывания (см. [Hugo. Развёртывание на базе страниц GitHub]({{< relref "2026-02-21--hugo-deploy-github-pages" >}})).


### <span class="section-num">4.2</span> Предлагаемые скрипты {#предлагаемые-скрипты}

-   Репозиторий: <https://github.com/HugoBlox/awesome-hugo>
-   Скрипт: `singular2plural`.
-   Документация: <https://github.com/HugoBlox/awesome-hugo/blob/main/singular2plural/README.md>


### <span class="section-num">4.3</span> Вариант 1: Миграция с помощью скрипта {#вариант-1-миграция-с-помощью-скрипта}

-   Два скрипта миграции (выберите тот, который вам больше подходит):
    -   Скрипт на Python (рекомендуется): `migrate-content-types.py`
    -   Скрипт Zsh : `migrate-content-types.sh`

-   Скрипты выполняют операции записи и удаления файлов/папок.
-   Перед запуском обязательно сделайте полную резервную копию своего компьютера и проверьте/адаптируйте код скрипта под свой сайт.
-   Всегда запускайте сначала скрипт с помощью `--dry-run`.


#### <span class="section-num">4.3.1</span> Использование скрипта Python {#использование-скрипта-python}

-   Требования:
    -   Python 3.8+ с `pyyaml` установлены:
        ```bash
        pip3 install pyyaml
        ```

-   Запуск:

<!--listend-->

```bash
# Run the migration script
python migrate-content-types.py /path/to/your/site --dry-run

# Apply changes after reviewing dry-run output
python migrate-content-types.py /path/to/your/site
```


#### <span class="section-num">4.3.2</span> Использование скрипта Zsh {#использование-скрипта-zsh}

-   Требования:
    -   Оболочка macOS/Linux (или Windows через WSL).

-   Запуск:

<!--listend-->

```bash
# Make the script executable (first time only)
chmod +x migrate-content-types.sh

# Preview without making changes
./migrate-content-types.sh /path/to/your/site --dry-run

# Apply changes after reviewing dry-run output
./migrate-content-types.sh /path/to/your/site
```


### <span class="section-num">4.4</span> Вариант 2: Ручная миграция {#вариант-2-ручная-миграция}

Если вы предпочитаете выполнить миграцию вручную, выполните следующие шаги:


#### <span class="section-num">4.4.1</span> Переименовать каталоги с содержимым {#переименовать-каталоги-с-содержимым}

-   Следует заменить:
    -   `post` → `blog`
    -   `publication` → `publications`
    -   `project` → `projects`
    -   `event` → `events`
    -   `teaching` → `courses`
        ```shell
        # For each content type
        mkdir -p content/blog
        mv content/post/* content/blog/
        rmdir content/post

        # Repeat for other types
        mkdir -p content/publications
        mv content/publication/* content/publications/
        rmdir content/publication

        # And so on...
        ```

-   В случае структуры с языком.
-   В каталоге `content`:
    ```shell
    cd content
    grep -r 'page_type:' *
    find . -iname "_index.md" -exec sed -i -e 's/page_type: post/page_type: blog/g' '{}' \;
    find -iname '_index.mde' -delete
    cd ru
    git mv post blog
    cd en
    git mv post blog
    ```


#### <span class="section-num">4.4.2</span> Обновите ссылки на папки в файлах контента {#обновите-ссылки-на-папки-в-файлах-контента}

-   Искать `folders:` разделы в файлах Markdown
-   Обновите ссылки, например: `- post` → `- blog`
-   Обновите ссылки, например: `- publication` → `- publications`
-   Обновите ссылки, например: `- project` → `- projects`
-   Обновите ссылки, например: `- event` → `- events`
-   Обновите ссылки, например: `- teaching` → `- courses`


#### <span class="section-num">4.4.3</span> Обновите ссылки на `page_type` в файлах контента {#обновите-ссылки-на-page-type-в-файлах-контента}

-   Искать `page_type:` в файлах Markdown
-   Обновлять `page_type: post` → `page_type: blog`
-   И так далее для других типов контента.


#### <span class="section-num">4.4.4</span> Удалите переопределения постоянных ссылок в конфигурации Hugo: {#удалите-переопределения-постоянных-ссылок-в-конфигурации-hugo}

-   Отредактируйте свой `hugo.yaml`, `config.yaml`, или `config.toml`.
-   Удалить или обновить любой `permalinks:` разделы, заменив название каталогов.
-   У меня получилось следующее:
    ```yaml
    permalinks:
      blog: "/blog/:year/:month/:day/:slug"
    ```


#### <span class="section-num">4.4.5</span> Добавьте перенаправления в ваш `netlify.toml` для обратной совместимости {#добавьте-перенаправления-в-ваш-netlify-dot-toml-для-обратной-совместимости}

-   Если вы используете netlify.
    ```toml
    [[redirects]]
      from = "/post/*"
      to = "/blog/:splat"
      status = 301
      force = true

    [[redirects]]
      from = "/publication/*"
      to = "/publications/:splat"
      status = 301
      force = true

    # And so on for other content types
    ```


### <span class="section-num">4.5</span> При ведении блога из org-roam {#при-ведении-блога-из-org-roam}

-   Для `post` → `blog`:
    ```shell
    cd ~/work/org
    find . -iname "*.org" -exec sed -i "s:ru/post/:ru/blog/:g" '{}' \;
    find . -iname "*.org" -exec sed -i "s:en/post/:en/blog/:g" '{}' \;
    ```
-   Для `teaching` → `courses`:
    ```shell
    cd ~/work/org
    find . -iname "*.org" -exec sed -i "s:ru/teaching:ru/courses:g" '{}' \;
    find . -iname "*.org" -exec sed -i "s:en/teaching:en/courses:g" '{}' \;
    ```


### <span class="section-num">4.6</span> После миграции {#после-миграции}

-   Запустите свой сайт локально с помощью `hugo server` чтобы проверить изменения.
-   Проверьте все страницы, чтобы убедиться в их корректном отображении.
-   Попробуйте выполнить поиск в папке вашего сайта по таким запросам, как `folders`, `type`, `layout` или старые типы страниц (например, `post` ) чтобы подтвердить, что у вас нет фильтров, ищущих контент в старой структуре.
-   Проверьте корректную работу ссылок и изображений.
-   Зафиксируйте изменения в вашем репозитории.


## <span class="section-num">5</span> Обновление до blox/v0.11.0 {#обновление-до-blox-v0-dot-11-dot-0}


### <span class="section-num">5.1</span> Общая информация {#общая-информация}

-   Релиз: <https://github.com/HugoBlox/kit/releases/tag/modules%2Fblox%2Fv0.11.0>


### <span class="section-num">5.2</span> Основные изменения {#основные-изменения}

-   Пути модулей и репозиториев
    -   Репозиторий и пути всех модулей были переименованы (например, `modules/blox-tailwind` → `modules/blox`).
    -   Сделать: обязательно обновить `go.mod` и `config/_default/modules.yaml` в проекте.                    |
-   Структура конфигурации
    -   Все настройки теперь находятся в едином пространстве `hugoblox:`. Ключевые секции переименованы (например, `branding` → `identity`).
    -   Сделать: перенести старые настройки из `params.yaml` в новую структуру, используя таблицы соответствия.
-   CMS и авторские профили
    -   Устаревший Decap (Netlify) CMS удален. Система авторских профилей стала data-ориентированной.
    -   Сделать: для авторов: перенести файлы из `content/authors/` в `data/authors/`.
-   События (Events)
    -   Логика работы с событиями изменена для совместимости со стандартными датами Hugo.
    -   Сделать: перенести события из `content/event/` в `content/events/` и обновить параметры в front matter.
-   Материалы (логотипы, иконки)
    -   Введена система автоматического определения файлов.
    -   Сделать: Поместить логотип, фавикон и соц. изображение в `assets/media/` с понятными именами.


### <span class="section-num">5.3</span> Рекомендуемый процесс обновления {#рекомендуемый-процесс-обновления}

-   Для максимально гладкого перехода разработчики настоятельно рекомендуют использовать HugoBlox CLI.
-   Этот инструмент автоматизирует большинство задач.


#### <span class="section-num">5.3.1</span> Установите HugoBlox CLI {#установите-hugoblox-cli}

```shell
pnpm install -g hugoblox
```

-   В терминале доступна команда `hbx`.


#### <span class="section-num">5.3.2</span> Автоматическое обновление модулей: {#автоматическое-обновление-модулей}

-   Чтобы обновить пути в `go.mod`, выполните:
    ```shell
    hbx upgrade
    ```


#### <span class="section-num">5.3.3</span> Перенос данных: {#перенос-данных}

-   Перенос авторов:
    ```shell
    hbx migrate v0.11.0-authors
    ```
-   Переноса событий:
    ```shell
    hbx migrate v0.11.0-events
    ```


#### <span class="section-num">5.3.4</span> Настройка конфигурации {#настройка-конфигурации}

-   Вручную обновите ваш `params.yaml`, используя подробные таблицы соответствия из руководства.
-   Скачайте новый шаблон конфига и перенесите в него старые значения.


#### <span class="section-num">5.3.5</span> Проверка {#проверка}

-   Запустите:
    ```shell
    hbx doctor
    ```
-   Запустите `hugo server` и тщательно проверьте все разделы сайта: шапку, подвал, цвета, поиск, аналитику.
