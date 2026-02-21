---
title: "Базовая настройка git"
author: ["Dmitry S. Kulyabov"]
date: 2024-03-16T17:34:00+03:00
lastmod: 2025-03-01T16:29:00+03:00
tags: ["sysadmin", "git"]
categories: ["computer-science"]
draft: false
slug: "git-basic-setup"
---

Базовая настройка git.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Первичная настройка параметров git {#первичная-настройка-параметров-git}

-   Зададим имя и email владельца репозитория:
    ```shell
    git config --global user.name "Name Surname"
    git config --global user.email "work@mail"
    ```
-   Настроим utf-8 в выводе сообщений git:
    ```shell
    git config --global core.quotepath false
    ```
-   Зададим имя начальной ветки (будем называть её `master`):
    ```shell
    git config --global init.defaultBranch master
    ```


## <span class="section-num">2</span> Верификация коммитов {#верификация-коммитов}

-   Настройте верификацию и подписание коммитов git (см. [Подпись коммитов git]({{< relref "2024-08-22-verifying-git-commits" >}})).


## <span class="section-num">3</span> Учёт переносов строк {#учёт-переносов-строк}

-   В разных операционных системах приняты разные символы для перевода строк:
    -   Windows: `\r\n` (`CR` и `LF`);
    -   Unix: `\n` (`LF`);
    -   Mac: `\r` (`CR`).
-   Посмотреть значения переносов строк в репозитории можно командой:
    ```shell
    git ls-files --eol
    ```


### <span class="section-num">3.1</span> Параметр `autocrlf` {#параметр-autocrlf}

-   Настройка `core.autocrlf` предназначена для того, чтобы в главном репозитории все переводы строк текстовых файлах были одинаковы.
-   Настройка `core.autocrlf` с параметрами `true` и `input` делает все переводы строк текстовых файлов в главном репозитории одинаковыми.
    -   `core.autocrlf true`: конвертация `CRLF->LF` при коммите и обратно `LF->CRLF` при выгрузке кода из репозитория на файловую систему (обычно используется в Windows).
    -   `core.autocrlf input`: конвертация `CRLF->LF` только при коммитах (используются в MacOS/Linux).
-   Варианты конвертации

    <div class="table-caption">
      <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
      Варианты конвертации для разных значений параметра core.autocrlf
    </div>

    | core.autocrlf | false           | input           | true            |
    |---------------|-----------------|-----------------|-----------------|
    | git commit    | LF -&gt; LF     | LF -&gt; LF     | LF -&gt; CRLF   |
    |               | CR -&gt; CR     | CR -&gt; CR     | CR -&gt; CR     |
    |               | CRLF -&gt; CRLF | CRLF -&gt; LF   | CRLF -&gt; CRLF |
    | git checkout  | LF -&gt; LF     | LF -&gt; LF     | LF -&gt; CRLF   |
    |               | CR -&gt; CR     | CR -&gt; CR     | CR -&gt; CR     |
    |               | CRLF -&gt; CRLF | CRLF -&gt; CRLF | CRLF -&gt; CRLF |
-   Установка параметра:
    -   Для Windows
        ```shell
        git config --global core.autocrlf true
        ```
    -   Для Linux
        ```shell
        git config --global core.autocrlf input
        ```


### <span class="section-num">3.2</span> Параметр `safecrlf` {#параметр-safecrlf}

-   Настройка `core.safecrlf`  предназначена для проверки, является ли окончаний строк обратимым для текущей настройки `core.autocrlf`.
    -   `core.safecrlf true`: запрещается необратимое преобразование `lf<->crlf`. Полезно, когда существуют бинарные файлы, похожие на текстовые файлы.
    -   `core.safecrlf warn`: печать предупреждения, но коммиты с необратимым переходом принимаются.
-   Установка параметра:
    ```shell
    git config --global core.safecrlf warn
    ```


## <span class="section-num">4</span> Перечисление веток {#перечисление-веток}

-   Настроим, чтобы перечисление веток git по умолчанию не упорядочивалось по алфавиту.

    -   `branch.sort` : сортирует список не по алфавиту, а по свежести дат коммитов;
    -   `column.ui` : выстраивает имена веток в формате столбцов так, чтобы на экране было видно больше такой информации.

    <!--listend-->

    ```shell
    git config --global column.ui auto
    git config --global branch.sort -committerdate
    ```


## <span class="section-num">5</span> Перечисление тегов {#перечисление-тегов}

-   При перечислении тегов командой `git tag` сортировка провидится в алфавитном порядке.
-   Но метки обычно имеют вид набора цифр (номер версии).
-   Настроим сортировку по номеру версии:
    ```shell
    git config --global tag.sort version:refname
    ```


## <span class="section-num">6</span> Отображение git diff {#отображение-git-diff}

-   Для команды `git diff`.
-   По умолчанию _git_ использует для вычисления разности коммитов алгоритм Майерса.
-   В базовой комплектации _git_ встроено 4 алгоритма вычисления разности: myers, minimal, patience, histogram (инкрементная усовершенствованная версия patience).
-   Установим по умолчанию алгоритм histogram:
    ```shell
    git config --global diff.algorithm histogram
    ```
-   При включённой опции `colorMoved` перемещение кода будет отображаться разными цветами, в зависимости от того, были какие-то строки добавлены или удалены.
    ```shell
    git config --global diff.colorMoved plain
    ```
-   Опция `diff.renames` позволяет выявить, был ли файл переименован
    ```shell
    git config --global diff.renames true
    ```
-   Опция `diff.mnemonicPrefix` заменяет префиксы (обычно `a/` и `b/`) на информацию о том, откуда пришло различие: `i/` (индекс), `w/` (рабочий каталог), или `c/` (коммит).
    ```shell
    git config --global diff.mnemonicPrefix true
    ```


## <span class="section-num">7</span> Настройка git push {#настройка-git-push}

-   Опция `push.default simple` установлена по умолчанию, начиная с _git_ 2.0.
-   Умолчание `simple` осуществляет отправку в текущую ветку и в одноимённую ветку на удалённой машине.
    ```shell
    git config --global push.default simple
    ```
-   Если удалённая ветка не существует, а отслеживание веток не настроено, то вы получите ошибку.
-   Опция `push.autoSetupRemote` служит для автоматического задания удалённой ветки:
    ```shell
    git config --global push.autoSetupRemote true
    ```
-   Настройка `push.followTags` запушит все теги, имеющиеся у вас на локальной машине, но отсутствующие на сервере.
-   Если вы создаёте теги на локальной машине, то активируйте эту настройку:
    ```shell
    git config --global push.followTags true
    ```


## <span class="section-num">8</span> Улучшенная выборка {#улучшенная-выборка}

-   Не стоит держать на локальной машине историю копий веток и тегов, которые когда-то были на сервере, а теперь там отсутствуют:
    ```shell
    git config --global fetch.prune true
    git config --global fetch.pruneTags true
    git config --global fetch.all true
    ```


## <span class="section-num">9</span> Предложения автозамены {#предложения-автозамены}

-   После ввода команды, которой не существует, следует запрос, что пользователь имел в виду.
-   Это поведение можно изменять с помощью параметра `help.autocorrect`:
    -   `0` (по умолчанию): показать предложенную команду.
    -   положительное число: выполнить предложенную команду через указанное количество децисекунд (0,1 секунды);
    -   `immediate`: выполнить предложенную команду немедленно;
    -   `prompt`: показать предложение и запросить подтверждение на выполнение команды;
    -   `never`: не выполнять и не показывать предложенную команду.
-   Вариант `prompt` представляется вполне разумным:
    ```shell
    git config --global help.autocorrect prompt
    ```


## <span class="section-num">10</span> Коммиты с указанием разности {#коммиты-с-указанием-разности}

-   По умолчанию `git commit` выдаёт только список изменившихся файлов.
-   Если установить `commit.verbose` в значение `true`, то будет представлен весь вывод `diff`:

<!--listend-->

```shell
git config --global commit.verbose true
```


## <span class="section-num">11</span> Повторное использование ранее записанных разрешений конфликтов {#повторное-использование-ранее-записанных-разрешений-конфликтов}

-   Настройка работает только при применении `rebase`.
-   Пригодится, когда регулярно возникают конфликты.
-   Опция `enabled` гарантирует, что система будет записывать состояния «до» и «после» конфликтов при перебазировании.
-   После этого `autoupdate` будет автоматически раз за разом применять проверенные способы разрешения конфликтов.
    ```shell
    git config --global rerere.enabled true
    git config --global rerere.autoupdate true
    ```


## <span class="section-num">12</span> Глобальный файл ignore {#глобальный-файл-ignore}

-   Вы можете создать локальный файл `.gitignore`.
-   Настройка `core.excludesfile` позволяет задать собственный глобальный файл для игнорирования:

<!--listend-->

```shell
touch ~/.config/git/ignore
git config --global core.excludesfile ~/.config/git/ignore
```

-   Примеры файлов игнорирования можно взять в <https://github.com/github/gitignore>.


## <span class="section-num">13</span> Аккуратное перебазирование {#аккуратное-перебазирование}

-   Опция организует в виде ветки стопку ссылок и гарантирует, что при перебазировании ветки эти ссылки также будут правильно перемещены:
    ```shell
    git config --global rebase.autoSquash true
    git config --global rebase.autoStash true
    git config --global rebase.updateRefs true
    ```


## <span class="section-num">14</span> Улучшенная обработка конфликтов при слиянии {#улучшенная-обработка-конфликтов-при-слиянии}

-   Для обработки конфликтов будем использовать алгоритм `zdiff3`:
    ```shell
    git config --global merge.conflictstyle zdiff3
    ```


## <span class="section-num">15</span> Настройки git pull {#настройки-git-pull}

-   Можно установить `rebase` по умолчаниию:
    ```shell
    git config --global pull.rebase true
    ```


## <span class="section-num">16</span> ИСпользование fsmonitor {#использование-fsmonitor}

-   Можно запускаться процесс для мониторинга файловой системы (по одному на каждый репозиторий), который будет отслеживать изменения в файлах и обновлять кэш.
-   На больших репозиториях можно ускорить операции (например, `git status`):
    ```shell
    git config --global core.fsmonitor true
    git config --global core.untrackedCache true
    ```
