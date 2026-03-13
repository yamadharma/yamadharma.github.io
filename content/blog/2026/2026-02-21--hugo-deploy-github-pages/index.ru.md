---
title: "Hugo. Развёртывание на базе страниц GitHub"
author: ["Dmitry S. Kulyabov"]
date: 2026-02-21T19:35:00+03:00
lastmod: 2026-02-23T18:42:00+03:00
draft: false
slug: "hugo-deploy-github-pages"
---

Hugo. Развёртывание на базе страниц GitHub (github pages).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Хостинги {#хостинги}

-   Публикация типа github pages возможна на нескольких хостингах.
    -   GitHub
    -   GitLab
    -   GitVerse


## <span class="section-num">2</span> Типы страниц GitHub {#типы-страниц-github}

-   Существует два типа страниц GitHub:
    -   Страницы пользователей/организаций: `https://<username|organization>.github.io/`
        -   Необходимо создать отдельный репозиторий `<username|organization>.github.io`.
        -   У пользователя может быть только одна страница подобного типа.
        -   Используется для личной страницы пользователя.
    -   Страницы проекта: `https://<username|organization>.github.io/<project>`
        -   Создаётся как ветка `gh-pages` в рамках существующего репозитория.
        -   Ваши файлы _Hugo_ хранятся в одной ветке, а ваши сгенерированные файлы публикуются в отдельной ветке в рамках одного проекта.


## <span class="section-num">3</span> Подходы к созданию репозитория {#подходы-к-созданию-репозитория}

-   На данный момент существует два метода создания репозитория сайта:
    -   ручной метод (2 репозитория);
    -   метод GitHub Actions (1 репозиторий).
-   Не все шаблоны работают с ручным методом.

| Аспект             | Ручной метод (2 репозитория)                                                        | Метод с GitHub Actions (1 репозиторий)                                                     |
|--------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Каталог `public`   | Вы создаете его локально командой `hugo` и вручную пушите в репозиторий `gh-pages`. | Автоматически создается на серверах GitHub при каждом `push`. В вашем репозитории его нет. |
| Ветки              | `master` для исходного кода, `gh-pages` для файлов сайта из `public`.               | Только ветка `master`. Ветка `gh-pages`  создается и управляется Actions автоматически.    |
| История изменений  | В репозитории `gh-pages`  хранится история сгенерированных файлов.                  | В истории `main` хранятся только изменения исходного кода.                                 |
| Процесс обновления | Два шага: 1) `hugo`, 2) `git push` в репозиторий `gh-pages`.                        | Один шаг: `git push origin mmaster` . Все остальное происходит само.                       |


## <span class="section-num">4</span> Создание репозитория для страницы пользователя на Github {#создание-репозитория-для-страницы-пользователя-на-github}

-   Чтобы опубликовать свой сайт со ссылкой `https://username.github.io`, необходимо создать репозиторий с именем `username.github.io`.
-   Регистр важен, используйте строчные буквы.
-   Видимость: public (бесплатный GitHub Pages работает с публичными репозиториями).
-   При создании не нужно сразу добавлять файлы README, .gitignore или лицензию.
-   Перейдите на свою веб-страницу Github и нажмите «Создать», чтобы создать новый репозиторий.
-   Можно создать с помощью утилиты `gh` (см. [github: утилиты командной строки]({{< relref "2021-08-04-github-command-line-utilities" >}})):
    ```shell
    gh repo create username.github.io --public
    ```


## <span class="section-num">5</span> Изменить `baseURL` в `config.yaml` для Hugo {#изменить-baseurl-в-config-dot-yaml-для-hugo}

-   Не забудьте задать значение для `baseURL` в файле `config.yaml`:
    -   `baseURL: 'https://<username>.github.io'` : для страницы пользователя;
    -   `baseURL: 'https://<username>.github.io/<repository_name>'` : для репозитория проекта.
-   Если это не сделать, то ваш сайт не будет работать.


## <span class="section-num">6</span> Метод GitHub Actions {#метод-github-actions}


### <span class="section-num">6.1</span> Подготовка сайта Hugo на вашем компьютере {#подготовка-сайта-hugo-на-вашем-компьютере}

-   Создайте сайт и инициализируйте Git-репозиторий в его папке:
    ```shell
    # Создайте новый сайт Hugo
    hugo new site username.github.io
    cd username.github.io
    # Инициализируйте локальный Git-репозиторий
    git init
    ```

-   Настройте базовый URL в конфигурационном файле: `baseURL = 'https://username.github.io/'`.
-   Создайте контент, например, пост: `hugo new posts/moy-pervyy-post.md`.
-   Проверьте сайт локально: запустите `hugo server -D` и откройте <http://localhost:1313>.


### <span class="section-num">6.2</span> Настройка автоматической сборки и публикации через GitHub Actions {#настройка-автоматической-сборки-и-публикации-через-github-actions}

-   Создайте файл рабочего процесса по пути `.github/workflows/hugo.yaml` в корне вашего проекта.
-   Можно использовать официальный шаблон от Hugo (его предлагает использовать сам github, он сам же его и создаст).
-   Свяжите локальный проект с GitHub-репозиторием, добавьте файлы и выполните первый коммит:
    ```shell
    # Добавьте удаленный репозиторий
    git remote add origin https://github.com/username/username.github.io.git
    # Добавьте все файлы
    git add .
    # Сделайте коммит
    git commit -m "Первая версия сайта на Hugo"
    git push -u origin master
    ```


### <span class="section-num">6.3</span> Активация GitHub Pages в настройках репозитория {#активация-github-pages-в-настройках-репозитория}

-   После пуша файлов и файла рабочего процесса:
    -   Перейдите в репозиторий на GitHub: `Settings` → `Pages`.
    -   В разделе _Build and deployment_ в качестве _Source_ выберите _GitHub Actions_.
    -   Через несколько минут сайт будет доступен по адресу <https://username.github.io>.
    -   Статус сборки можно проверить на вкладке _Actions_ вашего репозитория.


### <span class="section-num">6.4</span> Примечания {#примечания}

-   Убедитесь, что каталог `public/` добавлен в `.gitignore`.
-   Ваш репозиторий должен содержать только исходники:
    -   конфиг `hugo.toml`;
    -   папки `content/`, `layouts/`;
    -   файл workflow `.github/workflows/hugo.yaml`;
    -   файл `.gitignore`.
-   При выполнении `git push` GitHub Actions считывает инструкции из `hugo.yaml`:
    -   клонирует ваш репозиторий с исходниками;
    -   устанавливает Hugo;
    -   выполняет `hugo --minify`, создавая виртуальный каталог `public` на лету;
    -   берет содержимое этого виртуального каталога и отправляет его на хостинг GitHub Pages.


### <span class="section-num">6.5</span> Шаблон Academic CV {#шаблон-academic-cv}

-   В комплекте идут файлы:
    -   `.github/workflows/build.yml`
    -   `.github/workflows/deploy.yml`
-   В них задано развёртывание сайта для ветки `main`.
-   Если у вас ветка `master`, то замените название в этих файлах.
-   Остальные файлы в этом каталоге можно удалить.


## <span class="section-num">7</span> Ручной метод {#ручной-метод}

-   Считается устаревшим.
-   Не всегда работает.


### <span class="section-num">7.1</span> Подключение репозитория к вложенной папке {#подключение-репозитория-к-вложенной-папке}

-   Создайте отдельный репозиторий для исходных файлов блога.
-   Создайте подмодуль `public` в папке блога:
    ```shell
    cd ~/work/blog/blog
    git submodule add git@github.com:username/username.github.io.git public
    ```


### <span class="section-num">7.2</span> Генерация и развёртывание сайта {#генерация-и-развёртывание-сайта}

-   Сгенерите проект
    ```shell
    cd ~/work/blog/blog
    hugo
    ```
-   Зафиксируйте изменения и отправьте контент на GitHub:
    ```shell
    # Go To Public folder
    cd public

    # Add changes to git.
    git add .

    # Commit changes.
    git commit -am "rebuilding site $(date)"

    # Push source and build repos.
    git push origin master
    ```
