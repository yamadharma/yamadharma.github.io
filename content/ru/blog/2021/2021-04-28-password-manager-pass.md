---
title: "Менеджер паролей pass"
author: ["Dmitry S. Kulyabov"]
date: 2021-04-28T18:50:00+03:00
lastmod: 2025-08-19T16:38:00+03:00
tags: ["security", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "password-manager-pass"
---

-   Менеджер паролей `pass` --- программа, сделанная в рамках идеологии Unix.
-   Также носит название стандартного менеджера паролей для Unix (_The standard Unix password manager_).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Основные свойства {#основные-свойства}

-   Данные хранятся в файловой системе в виде каталогов и файлов.
-   Файлы шифруются с помощью GPG-ключа.


## <span class="section-num">2</span> Структура базы паролей {#структура-базы-паролей}

-   Структура базы может быть произвольной, если Вы собираетесь использовать её напрямую, без промежуточного программного обеспечения. Тогда семантику структуры базы данных Вы держите в своей голове.
-   Если же необходимо использовать дополнительное программное обеспечение, необходимо семантику заложить в структуру базы паролей.


### <span class="section-num">2.1</span> Семантическая структура базы паролей {#семантическая-структура-базы-паролей}

-   Рассмотрим пользователя `user` в домене `example.com`, порт `22`.
-   Отсутствие имени пользователя или порта в имени файла означает, что любое имя пользователя и порт будут совпадать:
    ```shell
    example.com.pgp
    ```
-   Соответствующее имя пользователя может быть именем файла внутри каталога, имя которого совпадает с хостом. Это полезно, если в базе есть пароли для нескольких пользователей на одном хосте:
    ```shell
    example.com/user.pgp
    ```
-   Имя пользователя также может быть записано в виде префикса, отделенного от хоста знаком `@`:
    ```shell
    user@example.com.pgp
    ```
-   Соответствующий порт может быть указан после хоста, отделённый двоеточием (`:`):
    ```shell
    example.com:22.pgp
    example.com:22/user.pgp
    user@example.com:22.pgp
    ```
-   Эти все записи могут быть расположены в произвольных каталогах, задающих Вашу собственную иерархию.


## <span class="section-num">3</span> Реализации {#реализации}


### <span class="section-num">3.1</span> Утилиты командной строки {#утилиты-командной-строки}

-   На данный момент существует 2 основных реализации:
    -   `pass`;
    -   `gopass`.
-   Они имеют высокуую совместимость по опциям и хранилищам.
-   Дальше в тексте будет использоваться программа `pass`, но всё то же самое можно сделать с помощью программы `gopass`.


#### <span class="section-num">3.1.1</span> pass {#pass}

-   Классическая реализация в виде shell-скриптов
-   Сайт: <https://www.passwordstore.org/>


#### <span class="section-num">3.1.2</span> gopass {#gopass}

-   Реализация `pass` на go с дополнительными интегрированными функциями
-   Сайт: <https://www.gopass.pw/>.
-   [Менеджер паролей gopass]({{< relref "2025-08-19--gopass-password-manager" >}})


### <span class="section-num">3.2</span> Графические интерфейсы {#графические-интерфейсы}


#### <span class="section-num">3.2.1</span> qtpass {#qtpass}

-   `qtpass` --- может работать как графический интерфейс к `pass`, так и как самостоятельная программа. В настройках можно переключаться между использованием `pass` и `gnupg`.


#### <span class="section-num">3.2.2</span> gopass-ui {#gopass-ui}

-   `gopass-ui` --- интерфейс к `gopass`.


#### <span class="section-num">3.2.3</span> webpass {#webpass}

-   Репозиторий: <https://github.com/emersion/webpass>
-   Веб-интерфейс к pass.
-   Написано на golang.


### <span class="section-num">3.3</span> Приложения для Android {#приложения-для-android}


#### <span class="section-num">3.3.1</span> Password Store {#password-store}

<!--list-separator-->

1.  android-password-store/Android-Password-Store

    -   URL: <https://play.google.com/store/apps/details?id=dev.msfjarvis.aps>
    -   Репозиторий с кодом: <https://github.com/android-password-store/Android-Password-Store>
    -   Документация: <https://android-password-store.github.io/docs/>
    -   Для синхронизации с git необходимо импортировать ssh-ключи.
    -   Поддерживает разблокировку по биометрическим данным.
    -   Версия 1.x для работы требует наличия _OpenKeychain: Easy PGP_.
    -   Репозиторий переведён в режим только для чтения <span class="timestamp-wrapper"><span class="timestamp">[2025-10-15 Ср]</span></span>
        -   <https://github.com/android-password-store/Android-Password-Store/discussions/3260>

<!--list-separator-->

2.  buckley-w-david/Android-Password-Store

    -   Репозиторий с кодом: <https://github.com/buckley-w-david/Android-Password-Store>
    -   Форк от основного репозитория.
    -   Выглядит живым.

<!--list-separator-->

3.  История

    <!--list-separator-->

    1.  <span class="timestamp-wrapper"><span class="timestamp">[2024-10-15 Вт]</span></span>

        -   Репозиторий <https://github.com/android-password-store/Android-Password-Store> переведён в режим read-only.
        -   Сообщение: <https://github.com/android-password-store/Android-Password-Store/discussions/3260>
        -   Текущий ментейнер сообщил, что далее не может работать над проектом и готов отдать его другому сопровождающему.


#### <span class="section-num">3.3.2</span> OpenKeychain: Easy PGP {#openkeychain-easy-pgp}

-   URL: <https://play.google.com/store/apps/details?id=org.sufficientlysecure.keychain>
-   Операции с ключами pgp.
-   Необходимо будет импортировать pgp-ключи.
-   Не поддерживает разблокировку по биометрическим данным. Необходимо набирать пароль ключа.


### <span class="section-num">3.4</span> Пакеты для Emacs {#пакеты-для-emacs}


#### <span class="section-num">3.4.1</span> pass {#pass}

-   Основной режим для управления хранилищем и редактирования записей.
-   [Emacs. Пакет pass]({{< relref "2023-12-02-emacs-pass" >}})
-   Репозиторий: <https://github.com/NicolasPetton/pass>
-   Позволяет редактировать базу данных паролей.
-   Запуск:
    ```elisp
    M-x pass
    ```


#### <span class="section-num">3.4.2</span> helm-pass {#helm-pass}

-   Интерфейс _helm_ для _pass_.
-   Репозиторий: <https://github.com/emacs-helm/helm-pass>
-   Запуск:
    ```elisp
    M-x helm-pass
    ```
-   Выдаёт в минибуфере список записей из базы паролей. При нажатии `Enter` копирует пароль в буфер.


#### <span class="section-num">3.4.3</span> ivy-pass {#ivy-pass}

-   Интерфейс _ivy_ для _pass_.
-   Репозиторий: <https://github.com/ecraven/ivy-pass>


### <span class="section-num">3.5</span> Форки {#форки}


#### <span class="section-num">3.5.1</span> passage {#passage}

-   Репозиторий: <https://github.com/FiloSottile/passage>
-   Используется `age` (<https://age-encryption.org>) как бэкенд.


## <span class="section-num">4</span> Установка {#установка}

-   Linux
    -   Gentoo
        -   `pass`
            ```shell
            emerge app-admin/pass
            ```
        -   `gopass`
            ```shell
            emerge app-admin/gopass
            ```
        -   `qtpass`
            ```shell
            emerge app-admin/qtpass
            ```
        -   Gopass UI
            -   Находится в оверлее awesome (<https://gitlab.awesome-it.de/overlays/awesome/>).
            -   Установка:
                ```shell
                emerge app-admin/gopass-ui
                ```
    -   Fedora
        -   `pass`
            ```shell
            dnf install pass pass-otp
            ```

            -   `gopass`
                ```shell
                dnf install gopass
                ```

-   Macintosh
    ```shell
    brew install pass
    ```
-   Windows
    -   `pass`
        ```shell
        choco install pass4win
        ```
    -   `gopass`
        ```shell
        choco install gopass
        ```


## <span class="section-num">5</span> Настройка {#настройка}


### <span class="section-num">5.1</span> Ключи GPG {#ключи-gpg}

-   Просмотр списка ключей:
    ```shell
    gpg --list-secret-keys
    ```
-   Если ключа нет, нужно создать новый:
    ```shell
    gpg --full-generate-key
    ```


### <span class="section-num">5.2</span> Инициализация хранилища {#инициализация-хранилища}


#### <span class="section-num">5.2.1</span> pass {#pass}

-   Инициализируем хранилище:
    ```shell
    pass init <gpg-id or email>
    ```


#### <span class="section-num">5.2.2</span> gopass {#gopass}

-   Для `gopass` можно просто ввести:
    ```shell
    gopass init
    ```

    -   Программа запросит ключ и почту для git.
    -   Будет инициализирована сразу структура git в каталоге `~/.password-store`.


#### <span class="section-num">5.2.3</span> qtpass {#qtpass}

-   Также можно инициализировать с помощью графического инструмента `qtpass`:
    ```shell
    qtpass
    ```


### <span class="section-num">5.3</span> Синхронизация с git {#синхронизация-с-git}


#### <span class="section-num">5.3.1</span> gopass {#gopass}

-   При инициализации `gopass` инициализирует также структуру git.
-   При необходимости это можно сделать отдельно:
    ```shell
    gopass git init
    ```
-   Также можно задать адрес репозитория на хостинге (репозиторий необходимо предварительно создать):
    ```shell
    gopass git remote add origin git@github.com:<git_username>/<git_repo>.git
    ```
-   Для синхронизации выполняется следующая команда:
    ```shell
    gopass sync
    ```


#### <span class="section-num">5.3.2</span> Прямые изменения {#прямые-изменения}

-   Следует заметить, что отслеживаются только изменения, сделанные через сам `gopass` (или `pass`).
-   Если изменения сделаны непосредственно на файловой системе, необходимо вручную закоммитить и выложить изменения:
    ```shell
    cd ~/.password-store/
    git add .
    git commit -am 'edit manually'
    git push
    ```
-   Проверить статус синхронизации модно командой
    ```shell
    gopass git status
    ```


### <span class="section-num">5.4</span> Тонкие настройки {#тонкие-настройки}

-   По умолчанию каталог с паролями называется `~/.password-store`. Но его можно задать также с помощью переменной окружения `PASSWORD_STORE_DIR`.


### <span class="section-num">5.5</span> Устранение сбоев {#устранение-сбоев}


#### <span class="section-num">5.5.1</span> Невозможно расшифровать пароль {#невозможно-расшифровать-пароль}

-   Команда `gopass show secret` выдаёт `Error: Failed to decrypt`.
-   Можно установить в `~/.bashrc` или `~/.profile`:
    ```shell
    export GPG_TTY=$(tty)
    ```

    -   <https://github.com/gopasspw/gopass/issues/208>
    -   <https://github.com/gopasspw/gopass/issues/209>


## <span class="section-num">6</span> Работа с паролями {#работа-с-паролями}


### <span class="section-num">6.1</span> Создание нового пароля {#создание-нового-пароля}


### <span class="section-num">6.2</span> Ручная правка базы паролей {#ручная-правка-базы-паролей}

-   Базу паролей можно редактировать и без использования специальных утилит.
-   Можно использовать для исправления структуры каталогов и имён файлов.
-   Синхронизацию с _git_ придётся выполнять вручную.
-   Не следует использовать символьные ссылки. Они не переносимы между разными операционными системами и могут нарушиться при синхронизации (например, с Android).
-   После ручного редактирования рекомендуется проверить структуру базы паролей:
    ```shell
    gopass fsck
    ```


## <span class="section-num">7</span> Миграция баз паролей из других программ {#миграция-баз-паролей-из-других-программ}


### <span class="section-num">7.1</span> Скрипты для миграции {#скрипты-для-миграции}


#### <span class="section-num">7.1.1</span> pass-import {#pass-import}

-   <https://github.com/roddhjav/pass-import>
-   Расширение для `pass`.
-   Можно использовать для разных менеджеров паролей:

    | Целевой менеджер паролей | Формат |
    |--------------------------|--------|
    | csv                      | csv    |
    | gopass                   | gopass |
    | keepass                  | kdbx   |
    | keepassx2                | kdbx   |
    | keepassxc                | kdbx   |
    | pass                     | pass   |

<!--list-separator-->

1.  Установка

    -   Gentoo
        -   Находится в оверлее `wjn-overlay` (<https://data.gpo.zugaina.org/wjn-overlay/>).
        -   Установка:
            ```shell
            emerge app-admin/pass-import
            ```

<!--list-separator-->

2.  Использование

    -   Для `pass`:
        -   Автоопределение формата источника:
            ```shell
            pass import path/to/passwords
            ```
        -   Если автоопределение не сработало:
            ```shell
            pass import <password_manager> path/to/passwords
            ```
        -   Если конвертация не для `pass`:
            ```shell
            pimport <new_pm> <former_pm> path/to/passwords --out path/to/destination/pm
            ```


#### <span class="section-num">7.1.2</span> Отдельные скрипты {#отдельные-скрипты}

-   На странице <https://www.passwordstore.org/> приведён список отдельных скриптов для миграции из разных служб.
-   Используйте в целях эксперимента.


### <span class="section-num">7.2</span> Конкретные рецепты {#конкретные-рецепты}


#### <span class="section-num">7.2.1</span> LastPass {#lastpass}

-   В меню выберите _Account options &gt; Advanced &gt; Export &gt; LastPass CVS File_.
-   Сохраняем результат в файл `lastpass_export.csv`.
-   Конвертация с помощью `pass-import`:
    ```shell
    pass import lastpass lastpass_export.csv
    ```
-   Альтернативный вариант. Не используйте его. Результат не соответствует структуре именования `pass`.
    -   Скачайте скрипт:
        ```shell
        wget https://git.zx2c4.com/password-store/plain/contrib/importers/lastpass2pass.rb
        ```
    -   Сделайте скрипт исполняемым:
        ```shell
        chmod +x lastpass2pass.rb
        ```
    -   Импортируйте пароли:
        ```shell
        ./lastpass2pass.rb lastpass_export.csv
        ```


### <span class="section-num">7.3</span> Экспорт паролей {#экспорт-паролей}


#### <span class="section-num">7.3.1</span> pass2csv {#pass2csv}

-   Репозиторий: <https://github.com/reinefjord/pass2csv>
-   Сайт: <https://pypi.org/project/pass2csv/>
-   Экспортирует хранилище паролей pass в _csv_.
-   Поддерживает задание шаблонов экспорта.


## <span class="section-num">8</span> Дополнительные возможности {#дополнительные-возможности}


### <span class="section-num">8.1</span> Проверка утечки пароля {#проверка-утечки-пароля}

-   Проверка утечки пароля производится с помощью сервиса <https://haveibeenpwned.com/> (см. [Have I Been Pwned (HIBP)]({{< relref "2021-05-03-have-i-been-pwned-hibp" >}})).


#### <span class="section-num">8.1.1</span> pass {#pass}

-   Проверка производится с помощью плагина `pass-audit`.
-   Код: <https://github.com/roddhjav/pass-audit>.
-   Установка:
    -   Gentoo:
        Находится в репозитории <https://github.com/yamadharma/gentoo-portage-local>.
        ```shell
        emerge app-admin/pass-audit
        ```
-   Использование:
    -   Проверка по парольному каталогу или по парольной записи:
        ```shell
        pass audit [каталог или одна запись]
        ```
    -   Без параметра проверяет всю базу паролей.


#### <span class="section-num">8.1.2</span> gopass {#gopass}

<!--list-separator-->

1.  Простая проверка качества пароля

    -   Простая проверка качества пароля по парольному каталогу или по парольной записи:
        ```shell
        gopass audit [каталог или одна запись]
        ```
    -   Без параметра проверяет всю базу паролей.

<!--list-separator-->

2.  Проверка утечки пароля

    -   Начиная с версии gopass-1.12.0 команда создания интерфейса взаимодействия с HIPB выделена в отдельную утилиту.
    -   Проверка производится с помощью плагина `gopass-hibp`.
    -   Код: <https://github.com/gopasspw/gopass-hibp>.
    -   Установка:
        -   Gentoo:
            ```shell
            emerge app-admin/gopass-hibp
            ```
    -   Использование:
        -   Использование HIBPv2 API
            ```shell
            gopass-hibp api
            ```
        -   Сравнение хешей паролей с дампом HIBP:
            -   Скачиваем дамп SHA-1 хешей паролей с <https://haveibeenpwned.com/Passwords> и распаковываем его.
            -   Проверяем пароли:
                ```shell
                gopass-hibp dump pwned-passwords-1.0.txt
                ```
                Этот вариант помедленнее.
    -   Проверяет сразу все записи в базе паролей. Один пароль проверить нельзя.


### <span class="section-num">8.2</span> Одноразовые пароли {#одноразовые-пароли}

-   [Менеджер паролей pass. Одноразовые пароли]({{< relref "2023-08-24-password-manager-pass-one-time-passwords" >}})


## <span class="section-num">9</span> Интеграция с другими программами {#интеграция-с-другими-программами}

-   [Менеджер паролей pass. Интеграция с другими программами]({{< relref "2021-11-20-password-manager-pass-integration" >}})
