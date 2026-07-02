---
title: "Hugo. Шаблон для научных работников. Подготовка структуры"
author: ["Dmitry S. Kulyabov"]
date: 2026-07-02T16:42:00+03:00
lastmod: 2026-07-02T17:33:00+03:00
tags: ["hugo"]
categories: ["computer-science"]
draft: false
slug: "hugo-hugoblox-preparing-structure"
---

Hugo. Шаблон для научных работников. Подготовка структуры

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Именование каталогов {#именование-каталогов}

-   [Организация рабочего каталога]({{< relref "2021-08-01-organization-working-directory" >}})
-   Использую каталог `~/work/blog` для всего, связанного с моим блогом.
-   Сам блог находится в каталоге `~/work/blog/blog`.


## <span class="section-num">2</span> Скачать шаблон {#скачать-шаблон}

-   Создать каталог:
    ```shell
    mkdir -p ~/work/blog
    ```
-   Скачать и настроить шаблон:
    ```shell
    npx hugoblox create site --template academic-cv
    ```

-   Проект назовём `blog`.
-   Эта команда скачает все необходимые файлы и создаст структуру вашего будущего сайта в новой папке.
-   Также будут скачаны необходимые модули Node.js.
    -   В противном случае их надо будет установить вручную.

-   Перейти в созданную папку:
    ```sh
    cd ~/work/blog/blog
    ```

-   Запустите локальный сервер, чтобы увидеть сайт:
    ```sh
    hugo server
    ```

-   Откройте браузер и перейдите по адресу `http://localhost:1313/`.


### <span class="section-num">2.1</span> Примечание {#примечание}

-   Шаблон по умолчанию содержит ссылки на изображения на `https://images.unsplash.com/`.
-   Этот сайт не доступен.
-   Удалите все ссылки на этот сайт из файлов.


## <span class="section-num">3</span> Скачивание необходимых модулей node.js {#скачивание-необходимых-модулей-node-dot-js}

-   Список необходимых модулей Node.js находится в файле `package.json`.
-   Их нужно установить.


### <span class="section-num">3.1</span> Установка с npm {#установка-с-npm}

-   Установите с помощью `npm`:
    ```shell
    npm install
    ```


### <span class="section-num">3.2</span> Установка с pnpm {#установка-с-pnpm}

-   pnpm создаёт shell-скрипты для вызова программ node.js.
-   `hugo` не поддерживает структуру файлов, создаваемых `pnpm`.
-   Чтобы pnpm создавал символические ссылки (symlinks) вместо shell-скриптов, нужно добавить в файл `.npmrc` в корне вашего проекта следующую строку:
    ```conf-unix
    prefer-symlinked-executables=true
    ```
-   После этого pnpm будет создавать в `node_modules/.bin` прямые ссылки на исполняемые JS-файлы (на POSIX-системах).
-   Эта опция автоматически включается, когда в `.npmrc` установлено `node-linker=hoisted`.
-   В режиме `hoisted` pnpm создаёт более плоскую структуру `node_modules`, похожую на npm.
-   При этом pnpm сам переключится на использование symlinks.
-   Современные версии `pnpm` вместо `.npmrc` читает `pnpm-workspace.yaml`.
-   Добавьте параметры в этот файл:
    ```shell
    pnpm config set node-linker hoisted --location project
    pnpm config set prefer-symlinked-executables true --location project
    ```

<!--listend-->

-   Установите модули с помощью `pnpm`:
    ```shell
    pnpm install
    ```


## <span class="section-num">4</span> Конфигурация языка {#конфигурация-языка}

-   [Hugo. Поддержка многоязычности]({{< relref "2026-03-03--hugo-multilingual-support" >}})
-   Будем делать поддержку языков на основе page-bundle.
-   Добавьте язык в файл `config/_default/languages.yaml`.
-   Здесь вы определяете языки и указываете, в каких папках лежит их контент.
    ```yaml
    # config/_default/languages.yaml

    # Английский язык (по умолчанию)
    en:
      locale: en-us
      title: "My Academic Website"
      params:
        description: "Personal academic website"

    # Русский язык
    ru:
      locale: ru-ru
      title: "Мой академический сайт"
      params:
        description: "Персональный академический сайт"
    ```

-   В файле конфигурации `hugo.yaml` укажите язык по умолчанию:
    ```yaml
    # config/_default/hugo.yaml
    defaultContentLanguage: "en"
    defaultContentLanguageInSubdir: true
    ```

-   Меню тоже можно перевести.
-   В файле `config/_default/languages.yaml` добавьте секцию `menu` для каждого языка.

<!--listend-->

```yaml
# config/_default/languages.yaml

en:
  # ...
  menu:
    main:
      - name: "About"
        url: "#about"
        weight: 1
      - name: "Publications"
        url: "#publications"
        weight: 2

ru:
  # ...
  menu:
    main:
      - name: "Обо мне"
        url: "#about"
        weight: 1
      - name: "Публикации"
        url: "#publications"
        weight: 2
```
