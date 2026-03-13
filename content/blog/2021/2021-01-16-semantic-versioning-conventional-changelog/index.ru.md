---
title: "Семантическое версионирование. Conventional Changelog"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-16T17:41:00+03:00
lastmod: 2023-07-19T15:39:00+03:00
tags: ["education", "programming"]
draft: false
slug: "semantic-versioning-conventional-changelog"
---

-   Пакет _Conventional Changelog_ представляет собой набор утилит.
-   Их можно использовать как вместе, так и по отдельности.
-   Также можно задавать свой рабочий процесс.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Репозитории {#репозитории}

-   Основной монорепозиторий: <https://github.com/conventional-changelog/conventional-changelog>


## <span class="section-num">2</span> Список утилит {#список-утилит}


### <span class="section-num">2.1</span> Основные утилиты проекта {#основные-утилиты-проекта}

-   [conventional-changelog-cli](https://github.com/conventional-changelog/conventional-changelog/tree/master/packages/conventional-changelog-cli) --- утилита командной строки.
-   [standard-changelog](https://github.com/conventional-changelog/conventional-changelog/tree/master/packages/standard-changelog) --- утилита командной строки для формата коммитов _angular_.
-   conventional-github-releaser --- создание нового релиза на GitHub из метаданных git.
-   [conventional-recommended-bump](https://github.com/conventional-changelog/conventional-changelog/tree/master/packages/conventional-recommended-bump) --- узнать на основе коммитов, какая версия рекомендуется.
-   [conventional-commits-detector](https://github.com/conventional-changelog/conventional-commits-detector) --- определить, какое соглашение о коммитах использует репозиторий.
-   [commitizen](https://github.com/commitizen/cz-cli) --- утилита, задающая интерфейс к написанию коммитов.
-   commitlint --- проверка правильности текста коммита.


### <span class="section-num">2.2</span> Дополнительные утилиты {#дополнительные-утилиты}

-   [cz-customizable](https://github.com/leoforfree/cz-customizable) --- плагин для `commitizen` для конфигурации формы ввода сообщений.
-   [cz-customizable-ghooks](https://github.com/uglow/cz-customizable-ghooks) --- интеграция `cz-customizable` с `ghooks` или `husky`, чтобы использовать единую конфигурацию для генерации и проверки сообщений коммитов .


## <span class="section-num">3</span> Настройка утилит {#настройка-утилит}


### <span class="section-num">3.1</span> conventional-commits-detector {#conventional-commits-detector}

-   Определить, какое соглашение о коммитах используется в репозитории.


#### <span class="section-num">3.1.1</span> Установка {#установка}

```shell
yarn [global] add [--dev] conventional-commits-detector
```


#### <span class="section-num">3.1.2</span> Использование {#использование}

```shell
npx conventional-commits-detector
```

В результате получим возможный тип коммитов.


### <span class="section-num">3.2</span> conventional-recommended-bump {#conventional-recommended-bump}

узнать на основе коммитов, какая версия рекомендуется.


#### <span class="section-num">3.2.1</span> Установка {#установка}

```shell
yarn [global] add [--dev] conventional-recommended-bump
```


#### <span class="section-num">3.2.2</span> Использование {#использование}

```shell
npx conventional-recommended-bump -p angular
```

Здесь `angular` --- название пресета.

В результате получим уровень, на который изменяется версия.


### <span class="section-num">3.3</span> standard-changelog {#standard-changelog}

Генерация журнала изменений с использованием соглашений о коммитах _angular_.


#### <span class="section-num">3.3.1</span> Установка {#установка}

```shell
yarn [global] add [--dev] standard-changelog
```


#### <span class="section-num">3.3.2</span> Использование {#использование}

Параметры запуска можно посмотреть следующим образом:

```shell
npx standard-changelog --help
```

Генерация файла журнала выполняется следующим образом:

```shell
npx standard-changelog
```

или

```shell
npx standard-changelog -i CHANGELOG.md -s
```


### <span class="section-num">3.4</span> conventional-changelog-cli {#conventional-changelog-cli}

Создаёт журнал изменений из метаданных git (если соглашение о коммитах отлично от _angular_).


#### <span class="section-num">3.4.1</span> Установка {#установка}

```shell
yarn [global] add [--dev] conventional-changelog-cli
```


#### <span class="section-num">3.4.2</span> Использование {#использование}

```shell
cd my-project
npx conventional-changelog -p angular -i CHANGELOG.md -s
```

Если инструмент используется впервые и нужно учесть все предыдущие журналы изменений, можно выполнить команду:

```shell
cd my-project
npx conventional-changelog -p angular -i CHANGELOG.md -s -r 0
```


### <span class="section-num">3.5</span> commitizen {#commitizen}

Утилита, реализующая интерактивный процесс для генерации коммита.


#### <span class="section-num">3.5.1</span> Установка {#установка}

```shell
yarn [global] add [--dev] commitizen
```

При этом устанавливается скрипт `git-cz`, который мы и будем использовать для коммитов.


#### <span class="section-num">3.5.2</span> Использование {#использование}

-   Сконфигурим формат коммитов. Для этого добавим в файл `package.json` команду для формирования коммитов:
    ```js
    "config": {
        "commitizen": {
            "path": "cz-conventional-changelog"
        }
    }
    ```
-   Выполнение коммитов:
    ```shell
    git cz
    ```


### <span class="section-num">3.6</span> cz-customizable {#cz-customizable}

-   Плагин для `commitizen` для конфигурации формы ввода сообщений. Можно задать не только типы коммитов, но и области (scopes) коммитов.


#### <span class="section-num">3.6.1</span> Установка {#установка}

```shell
yarn [global] add [--dev] cz-customizable
```

-   При этом устанавливается скрипт `git-cz`, который мы и будем использовать для коммитов.


#### <span class="section-num">3.6.2</span> Использование {#использование}

-   Сконфигурим формат коммитов. Для этого добавим в файл `package.json` команду для формирования коммитов (заменив стандартный плагин для `commitizen`) и конфигурационный файл для `cz-customizable`:
    ```js
    "config": {
        "commitizen": {
            "path": "cz-customizable"
        },
        "cz-customizable": {
            "config": ".cz-config.js"
        }
    }
    ```
-   Пример конфигурационного файл можно скачать из репозитория _cz-customizable_:
    ```shell
    wget https://raw.githubusercontent.com/leoforfree/cz-customizable/master/cz-config-EXAMPLE.js -O .cz-config.js
    ```
-   Выполнение коммитов:
    ```shell
    git cz
    ```
-   В качестве примера приведу следующий конфигурационный файл (<https://infostart.ru/1c/articles/1016001/>):
    ```js
    "use strict";

    module.exports = {
        // Добавим описание на русском языке ко всем типам
        types: [
            { value: "feature", name: "feature:   Добавление нового функционала" },
            { value: "fix", name: "fix:       Исправление ошибок" },
            { value: "docs", name: "docs:      Обновление документации" },
            { value: "test", name: "test:      Добавление тестов" },
            { value: "refactor",
              name:
              "refactor:  Правки кода без исправления ошибок или добавления новых функций"
            },
            { value: "perf",
              name: "perf:      Изменения направленные на улучшение производительности"
            },
            { value: "style",
              name:
              "style:     Правки по кодстайлу (табы, отступы, точки, запятые и т.д.)"
            },
            { value: "build",
              name: "build:     Сборка проекта или изменения внешних зависимостей"
            },
            { value: "ci", name: "ci:        Настройка CI и работа со скриптами" },
            { value: "revert", name: "revert:    Откат на предыдущие коммиты" }
        ],

        // Область. Она характеризует фрагмент кода, которую затронули изменения
        scopes: [
            { name: "Кэш" },
            { name: "ФормаОсновная" },
            { name: "Валидация" },
            { name: "АвтоматическоеТестирование"},
            { name: "Отчеты" },
            { name: "ПервыйЗапуск" },
            { name: "ЗащитаМодуля" },
            { name: "ТребованияКПроизводительности" },
            { name: "ХранениеДанных" },
            { name: "API" }
        ],

        // Возможность задать спец ОБЛАСТЬ для определенного типа коммита (пример для 'fix')
        /*
          scopeOverrides: {
          fix: [
          {name: 'style'},
          {name: 'e2eTest'},
          {name: 'unitTest'}
          ]
          },
        */

        // Поменяем дефолтные вопросы
        messages: {
            type: "Какие изменения вы вносите?",
            scope: "\nВыберите ОБЛАСТЬ, которую вы изменили (опционально):",
            // Спросим если allowCustomScopes в true
            customScope: "Укажите свою ОБЛАСТЬ:",
            subject: "Напишите КОРОТКОЕ описание:\n",
            body:
            'Напишите ПОДРОБНОЕ описание (опционально). Используйте "|" для новой строки:\n',
            breaking: "Список BREAKING CHANGES (опционально):\n",
            footer:
            "Место для мета данных (тикетов, ссылок и остального). Например: SECRETMRKT-700, SECRETMRKT-800:\n",
            confirmCommit: "Вас устраивает получившийся коммит?"
        },

        // Разрешим собственную ОБЛАСТЬ
        allowCustomScopes: true,

        // allowBreakingChanges: false, // Запрет на Breaking Changes
        // askForBreakingChangeFirst : true, // default is false
        allowBreakingChanges: ['feat', 'fix'],

        // skip any questions you want
        //skipQuestions: ['body'],

        breaklineChar: '|', // It is supported for fields body and footer.

        // Префикс для нижнего колонтитула
        footerPrefix : 'ISSUES CLOSED:',


        // limit subject length
        subjectLimit: 72,
    };
    ```


### <span class="section-num">3.7</span> conventional-github-releaser {#conventional-github-releaser}

-   Утилита, создающая новый выпуск на GitHub на основе метаданных git.


#### <span class="section-num">3.7.1</span> Установка {#установка}

```shell
yarn [global] add [--dev] conventional-github-releaser
```


#### <span class="section-num">3.7.2</span> Использование {#использование}

-   Создайте новый токен для для доступа к github
    -   Токен создаётся по ссылке <https://github.com/settings/tokens/new>.
    -   Права для токена: `public_repo` или `repo`.
    -   Обязательно сразу скопируйте свой новый токен личного доступа. Нет возможности получить доступ к его значению ещё раз.
    -   Установите созданный токен как значение переменной окружения `CONVENTIONAL_GITHUB_RELEASER_TOKEN`.
    -   Также можно указать свой токен аутентификации с помощью флага `-t` или `--token`.
-   Создание релиза с определённым пресетом:
    ```shell
    conventional-github-releaser -p angular
    ```
    Здесь `angular` --- один из пресетов : `angular`, `atom`, `codemirror`, `ember`, `eslint`, `express`, `jquery`, `jscs`, `jshint`.


## <span class="section-num">4</span> Примерный рабочий процесс {#примерный-рабочий-процесс}

-   Внести изменения.
-   Зафиксировать эти изменения.
-   Проверить состояние Travis CI.
-   Изменить версию в `package.json`.
-   Закоммитить файлы: `package.json`.
-   Задать метку (tag).
-   Выложить на удалённый репозиторий (`push`).
-   Сделать релиз (`conventional-github-releaser`)

-   Причина, по которой вы должны зафиксировать изменения и создать метку после выполнения `standard-changelog` заключается в том, что `CHANGELOG.md` должен быть включён в новую версию.
