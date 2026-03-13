---
title: "Настройка рабочей среды"
author: ["Dmitry S. Kulyabov"]
date: 2023-07-30T15:25:00+03:00
lastmod: 2025-09-06T15:58:00+03:00
tags: ["education"]
categories: ["computer-science"]
draft: false
weight: 210
slug: "lab-work-environment-setup"
summary: "Настройка рабочей среды"
linktitle: "Настройка рабочей среды"
menu:
  "lab-work-environment-setup":
    parent: "os-intro-lab"
    weight: 210
    identifier: "lab-work-environment-setup"
---

Настройка рабочей среды.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Менеджер паролей pass {#менеджер-паролей-pass}

-   Менеджер паролей `pass` --- программа, сделанная в рамках идеологии Unix.
-   Также носит название стандартного менеджера паролей для Unix (_The standard Unix password manager_).


### <span class="section-num">1.1</span> Основные свойства {#основные-свойства}

-   Данные хранятся в файловой системе в виде каталогов и файлов.
-   Файлы шифруются с помощью GPG-ключа.


### <span class="section-num">1.2</span> Структура базы паролей {#структура-базы-паролей}

-   Структура базы может быть произвольной, если Вы собираетесь использовать её напрямую, без промежуточного программного обеспечения. Тогда семантику структуры базы данных Вы держите в своей голове.
-   Если же необходимо использовать дополнительное программное обеспечение, необходимо семантику заложить в структуру базы паролей.


#### <span class="section-num">1.2.1</span> Семантическая структура базы паролей {#семантическая-структура-базы-паролей}

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


### <span class="section-num">1.3</span> Реализации {#реализации}


#### <span class="section-num">1.3.1</span> Утилиты командной строки {#утилиты-командной-строки}

-   На данный момент существует 2 основных реализации:
    -   `pass` --- классическая реализация в виде shell-скриптов (<https://www.passwordstore.org/>);
    -   `gopass` --- реализация на go с дополнительными интегрированными функциями (<https://www.gopass.pw/>).
-   Дальше в тексте будет использоваться программа `pass`, но всё то же самое можно сделать с помощью программы `gopass`.


#### <span class="section-num">1.3.2</span> Графические интерфейсы {#графические-интерфейсы}

<!--list-separator-->

1.  qtpass

    -   `qtpass` --- может работать как графический интерфейс к `pass`, так и как самостоятельная программа. В настройках можно переключаться между использованием `pass` и `gnupg`.

<!--list-separator-->

2.  gopass-ui

    -   `gopass-ui` --- интерфейс к `gopass`.

<!--list-separator-->

3.  webpass

    -   Репозиторий: <https://github.com/emersion/webpass>
    -   Веб-интерфейс к pass.
    -   Написано на golang.


#### <span class="section-num">1.3.3</span> Приложения для Android {#приложения-для-android}

<!--list-separator-->

1.  Password Store

    -   URL: <https://play.google.com/store/apps/details?id=dev.msfjarvis.aps>
    -   Репозиторий с кодом: <https://github.com/android-password-store/Android-Password-Store>
    -   Документация: <https://android-password-store.github.io/docs/>
    -   Для синхронизации с git необходимо импортировать ssh-ключи.
    -   Поддерживает разблокировку по биометрическим данным.
    -   Для работы требует наличия _OpenKeychain: Easy PGP_.

<!--list-separator-->

2.  OpenKeychain: Easy PGP

    -   URL: <https://play.google.com/store/apps/details?id=org.sufficientlysecure.keychain>
    -   Операции с ключами pgp.
    -   Необходимо будет импортировать pgp-ключи.
    -   Не поддерживает разблокировку по биометрическим данным. Необходимо набирать пароль ключа.


#### <span class="section-num">1.3.4</span> Пакеты для Emacs {#пакеты-для-emacs}

<!--list-separator-->

1.  pass

    -   Основной режим для управления хранилищем и редактирования записей.
    -   [Emacs. Пакет pass]({{< relref "2023-12-02-emacs-pass" >}})
    -   Репозиторий: <https://github.com/NicolasPetton/pass>
    -   Позволяет редактировать базу данных паролей.
    -   Запуск:
        ```elisp
        M-x pass
        ```

<!--list-separator-->

2.  helm-pass

    -   Интерфейс _helm_ для _pass_.
    -   Репозиторий: <https://github.com/emacs-helm/helm-pass>
    -   Запуск:
        ```elisp
        M-x helm-pass
        ```
    -   Выдаёт в минибуфере список записей из базы паролей. При нажатии `Enter` копирует пароль в буфер.

<!--list-separator-->

3.  ivy-pass

    -   Интерфейс _ivy_ для _pass_.
    -   Репозиторий: <https://github.com/ecraven/ivy-pass>


## <span class="section-num">2</span> Управление файлами конфигурации {#управление-файлами-конфигурации}

-   Использование `chezmoi` для управления файлами конфигурации домашнего каталога пользователя.


### <span class="section-num">2.1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.chezmoi.io/>
-   Репозиторий: <https://github.com/twpayne/chezmoi>


### <span class="section-num">2.2</span> Конфигурация `chezmoi` {#конфигурация-chezmoi}


#### <span class="section-num">2.2.1</span> Рабочие файлы {#рабочие-файлы}

-   Состояние файлов конфигурации сохраняется в каталоге
    ```shell
    ~/.local/share/chezmoi
    ```
-   Он является клоном вашего репозитория `dotfiles`.
-   Файл конфигурации `~/.config/chezmoi/chezmoi.toml` (можно использовать также JSON или YAML) специфичен для локальной машины.
-   Файлы, содержимое которых одинаково на всех ваших машинах, дословно копируются из исходного каталога.
-   Файлы, которые варьируются от машины к машине, выполняются как шаблоны, обычно с использованием данных из файла конфигурации локальной машины для настройки конечного содержимого, специфичного для локальной машины.
-   При запуске
    ```shell
    chezmoi apply
    ```

вычисляется желаемое содержимое и разрешения для каждого файла, а затем вносит необходимые изменения, чтобы ваши файлы соответствовали этому состоянию.

-   По умолчанию chezmoi изменяет файлы только в рабочей копии.


#### <span class="section-num">2.2.2</span> Автоматически создавать файл конфигурации на новой машине {#автоматически-создавать-файл-конфигурации-на-новой-машине}

-   При выполнении `chezmoi init` также может автоматически создать файл конфигурации, если он еще не существует.
-   Если ваш репозиторий содержит файл с именем `.chezmoi.$FORMAT.tmpl`, где `$FORMAT` есть один из поддерживаемых форматов файла конфигурации (`json`, `toml`, или `yaml`), то `chezmoi init` выполнит этот шаблон для создания исходного файла конфигурации.
-   Например, пусть `~/.local/share/chezmoi/.chezmoi.toml.tmpl` выглядит так:
    ```toml
    {{- $email := promptStringOnce . "email" "Email address" -}}

    [data]
        email = {{ $email | quote }}
    ```

    -   При выполнении `chezmoi init` будет создан конфигурационный файл `~/.config/chezmoi/chezmoi.toml`.
    -   `promptStringOnce` --- это специальная функция, которая запрашивает у пользователя значение, если оно еще не установлено в разделе `data` конфигурационного файла.
-   Чтобы протестировать этот шаблон, используйте `chezmoi execute-template` с флагами `--init` и `--promptString`, например:
    ```shell
    chezmoi execute-template --init --promptString email=me@home.org < ~/.local/share/chezmoi/.chezmoi.toml.tmpl
    ```


#### <span class="section-num">2.2.3</span> Пересоздание файл конфигурации {#пересоздание-файл-конфигурации}

-   Если вы измените шаблон файла конфигурации, `chezmoi` предупредит вас, если ваш текущий файл конфигурации не был сгенерирован из этого шаблона.
-   Вы можете повторно сгенерировать файл конфигурации, запустив:
    ```shell
    chezmoi init
    ```


### <span class="section-num">2.3</span> Шаблоны {#шаблоны}


#### <span class="section-num">2.3.1</span> Общая информация {#общая-информация}

-   Шаблоны используются для изменения содержимого файла в зависимости от среды.
-   Используется синтаксис шаблонов Go.
-   Файл интерпретируется как шаблон, если выполняется одно из следующих условий:
    -   имя файла имеет суффикс `.tmpl`;
    -   файл находится в каталоге `.chezmoitemplates`.


#### <span class="section-num">2.3.2</span> Данные шаблона {#данные-шаблона}

-   Полный список переменных шаблона:
    ```shell
    chezmoi data
    ```
-   Источники переменных:
    -   файлы `.chezmoi`, например, `.chezmoi.os`;
    -   файлы конфигурации `.chezmoidata.$FORMAT`. Форматы (`json`, `jsonc`, `toml`, `yaml`) читаются в алфавитном порядке;
    -   раздел `data` конфигурационного файла.


#### <span class="section-num">2.3.3</span> Способы создания файла шаблона {#способы-создания-файла-шаблона}

-   При первом добавлении файла передайте аргумент `--template`:
    ```shell
    chezmoi add --template ~/.zshrc
    ```
-   Если файл уже контролируется _chezmoi_, но не является шаблоном, можно сделать его шаблоном:
    ```shell
    chezmoi chattr +template ~/.zshrc
    ```
-   Можно создать шаблон вручную в исходном каталоге, присвоив ему расширение `.tmpl`:
    ```shell
    chezmoi cd
    $EDITOR dot_zshrc.tmpl
    ```
-   Шаблоны в каталоге `.chezmoitemplates` должны создаваться вручную:
    ```shell
    chezmoi cd
    mkdir -p .chezmoitemplates
    cd .chezmoitemplates
    $EDITOR mytemplate
    ```


#### <span class="section-num">2.3.4</span> Редактирование файла шаблона {#редактирование-файла-шаблона}

-   Используйте `chezmoi edit`:
    ```shell
    chezmoi edit ~/.zshrc
    ```
-   Чтобы сделанные вами изменения сразу же применялись после выхода из редактора, используйте опцию `--apply`:
    ```shell
    chezmoi edit --apply ~/.zshrc
    ```


#### <span class="section-num">2.3.5</span> Тестирование шаблонов {#тестирование-шаблонов}

-   Тестирование с помощью команды `chezmoi execute-template`.
-   Тестирование небольших фрагментов шаблонов:
    ```shell
    chezmoi execute-template '{{ .chezmoi.hostname }}'
    ```
-   Тестирование целых файлов:
    ```shell
    chezmoi cd
    chezmoi execute-template < dot_zshrc.tmpl
    ```


#### <span class="section-num">2.3.6</span> Синтаксис шаблона {#синтаксис-шаблона}

-   Действия шаблона записываются внутри двойных фигурных скобок, `{{ }}`.
-   Действия могут быть переменными, конвейерами или операторами управления.
-   Текст вне действий копируется буквально.
-   Переменные записываются буквально:

<!--listend-->

```web
{{ .chezmoi.hostname }}
```

-   Условные выражения могут быть записаны с использованием `if`, `else if`, `else`, `end`:

<!--listend-->

```web
{{ if eq .chezmoi.os "darwin" }}
# darwin
{{ else if eq .chezmoi.os "linux" }}
# linux
{{ else }}
# other operating system
{{ end }}
```

<!--list-separator-->

1.  Удаление пробелов

    -   Для удаления проблем в шаблоне разместите знак минус и пробела рядом со скобками:
        ```web
        HOSTNAME={{- .chezmoi.hostname }}
        ```
    -   В результате получим:
        ```shell
        HOSTNAME=myhostname
        ```

<!--list-separator-->

2.  Отладка шаблона

    -   Используется подкоманда `execute-template`:
        ```shell
        chezmoi execute-template '{{ .chezmoi.os }}/{{ .chezmoi.arch }}'
        ```
    -   Интерпретируются любые данные, поступающие со стандартного ввода или в конце команды.
    -   Можно передать содержимое файла этой команде:
        ```shell
        cat foo.txt | chezmoi execute-template
        ```

<!--list-separator-->

3.  Логические операции

    -   Возможно выполнение логических операций.
    -   Если имя хоста машины равно `work-laptop`, текст между `if` и `end` будет включён в результат:
        ```web
        # common config
        export EDITOR=vi

        # machine-specific configuration
        {{- if eq .chezmoi.hostname "work-laptop" }}
        # this will only be included in ~/.bashrc on work-laptop
        {{- end }}
        ```

    <!--list-separator-->

    1.  Логические функции

        -   `eq`: возвращает `true`, если первый аргумент равен любому из остальных аргументов, может принимать несколько аргументов;
        -   `not`: возвращает логическое отрицание своего единственного аргумента;
        -   `and`: возвращает логическое И своих аргументов, может принимать несколько аргументов;
        -   `or`: возвращает логическое ИЛИ своих аргументов, может принимать несколько аргументов.

    <!--list-separator-->

    2.  Целочисленные функции

        -   `len`: возвращает целочисленную длину своего аргумента;
        -   `eq`: возвращает логическую истину `arg1 == arg2`;
        -   `ne`: возвращает логическое значение `arg1 != arg2`;
        -   `lt`: возвращает логическую истину `arg1 < arg2`;
        -   `le`: возвращает логическую истину `arg1 <= arg2`;
        -   `gt`: возвращает логическую истину `arg1 > arg2`;
        -   `ge`: возвращает логическую истину `arg1 >= arg2`.


#### <span class="section-num">2.3.7</span> Переменные шаблона {#переменные-шаблона}

-   Чтобы просмотреть переменные, доступные в вашей системе, выполните:
    ```shell
    chezmoi data
    ```
-   Чтобы получить доступ к переменной `chezmoi.kernel.osrelease` в шаблоне, используйте:
    ```web
    {{ .chezmoi.kernel.osrelease }}
    ```


## <span class="section-num">3</span> Выполнение лабораторной работы {#выполнение-лабораторной-работы}


### <span class="section-num">3.1</span> Менеджер паролей pass {#менеджер-паролей-pass}


#### <span class="section-num">3.1.1</span> Установка {#установка}

-   Fedora
    -   `pass`
        ```shell
        dnf install pass pass-otp
        ```

        -   `gopass`
            ```shell
            dnf install gopass
            ```


#### <span class="section-num">3.1.2</span> Настройка {#настройка}

<!--list-separator-->

1.  Ключи GPG

    -   Просмотр списка ключей:
        ```shell
        gpg --list-secret-keys
        ```
    -   Если ключа нет, нужно создать новый:
        ```shell
        gpg --full-generate-key
        ```

<!--list-separator-->

2.  Инициализация хранилища

    -   Инициализируем хранилище:
        ```shell
        pass init <gpg-id or email>
        ```

<!--list-separator-->

3.  Синхронизация с git

    -   Создадим структуру git:
        ```shell
        pass git init
        ```
    -   Также можно задать адрес репозитория на хостинге (репозиторий необходимо предварительно создать):
        ```shell
        pass git remote add origin git@github.com:<git_username>/<git_repo>.git
        ```
    -   Для синхронизации выполняется следующая команда:
        ```shell
        pass git pull
        pass git push
        ```

    <!--list-separator-->

    1.  Прямые изменения

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
            pass git status
            ```


#### <span class="section-num">3.1.3</span> Настройка интерфейса с броузером {#настройка-интерфейса-с-броузером}

-   Для взаимодействия с броузером используется интерфейс _native messaging_.
-   Поэтому кроме плагина к броузеру устанавливается программа, обеспечивающая интерфейс _native messaging_.

<!--list-separator-->

1.  Плагин [browserpass](https://github.com/browserpass/browserpass-extension)

    -   Репозиторий: <https://github.com/browserpass/browserpass-extension>
    -   Плагин для брoузера
        -   Плагин для Firefox: <https://addons.mozilla.org/en-US/firefox/addon/browserpass-ce/>.
        -   Плагин для Chrome/Chromium: <https://chrome.google.com/webstore/detail/browserpass-ce/naepdomgkenhinolocfifgehidddafch>.
    -   Интерфейс для взаимодействия с броузером (native messaging)
        -   Репозиторий: <https://github.com/browserpass/browserpass-native>
        -   Gentoo:
            ```shell
            emerge www-plugins/browserpass
            ```
        -   Fedora
            ```shell
            dnf copr enable maximbaz/browserpass
            dnf install browserpass
            ```


#### <span class="section-num">3.1.4</span> Сохранение пароля {#сохранение-пароля}

<!--list-separator-->

1.  Добавить новый пароль

    -   Выполните:
        ```shell
        pass insert [OPTIONAL DIR]/[FILENAME]
        ```

        -   `OPTIONAL DIR`: необязательное имя каталога, определяющее файловую структуру для вашего хранилища паролей;
        -   `FILENAME`: имя файла, который будет использоваться для хранения пароля.
    -   Отобразите пароль для указанного имени файла:
        ```shell
        pass [OPTIONAL DIR]/[FILENAME]
        ```
    -   Замените существующий пароль:
        ```shell
        pass generate --in-place FILENAME
        ```


### <span class="section-num">3.2</span> Управление файлами конфигурации {#управление-файлами-конфигурации}


#### <span class="section-num">3.2.1</span> Установка {#установка}

-   Fedora
    -   Установка из COPR:
        ```shell
        sudo dnf -y copr enable lihaohong/chezmoi
        sudo dnf -y install chezmoi
        ```


### <span class="section-num">3.3</span> Дополнительное программное обеспечение {#дополнительное-программное-обеспечение}

-   Установите дополнительное программное обеспечение:
    ```shell
    sudo dnf -y install \
             dunst \
             fontawesome-fonts \
             powerline-fonts \
             light \
             fuzzel \
             swaylock \
             kitty \
             waybar swaybg \
             wl-clipboard \
             mpv \
             grim \
             slurp
    ```
-   Установите шрифты:
    ```shell
    sudo dnf copr -y enable peterwu/iosevka
    sudo dnf search iosevka
    sudo dnf install iosevka-fonts iosevka-aile-fonts iosevka-curly-fonts iosevka-slab-fonts iosevka-etoile-fonts iosevka-term-fonts
    ```


#### <span class="section-num">3.3.1</span> Установка {#установка}

-   Установка бинарного файла. Скрипт определяет архитектуру процессора и операционную систему и скачивает необходимый файл:
    -   с помощью `wget`:
        ```shell
        sh -c "$(wget -qO- chezmoi.io/get)"
        ```


#### <span class="section-num">3.3.2</span> Создание собственного репозитория с помощью утилит {#создание-собственного-репозитория-с-помощью-утилит}

-   Будем использовать утилиты командной строки для работы с github (см. [github: утилиты командной строки]({{< relref "2021-08-04-github-command-line-utilities" >}})).
-   Создадим свой репозиторий для конфигурационных файлов на основе шаблона:
    ```shell
    gh repo create dotfiles --template="yamadharma/dotfiles-template" --private
    ```


#### <span class="section-num">3.3.3</span> Подключение репозитория к своей системе {#подключение-репозитория-к-своей-системе}

-   Инициализируйте `chezmoi` с вашим репозиторием `dotfiles`:
    ```shell
    chezmoi init git@github.com:<username>/dotfiles.git
    ```
-   Проверьте, какие изменения внесёт `chezmoi` в домашний каталог, запустив:
    ```shell
    chezmoi diff
    ```
-   Если вас устраивают изменения, внесённые `chezmoi`, запустите:
    ```shell
    chezmoi apply -v
    ```


#### <span class="section-num">3.3.4</span> Использование chezmoi на нескольких машинах {#использование-chezmoi-на-нескольких-машинах}

-   На второй машине инициализируйте `chezmoi` с вашим репозиторием `dotfiles`:
    ```shell
    chezmoi init https://github.com/<username>/dotfiles.git
    ```
-   Или через ssh:
    ```shell
    chezmoi init git@github.com:<username>/dotfiles.git
    ```
-   Проверьте, какие изменения внесёт `chezmoi` в домашний каталог, запустив:
    ```shell
    chezmoi diff
    ```
-   Если вас устраивают изменения, внесённые `chezmoi`, запустите:
    ```shell
    chezmoi apply -v
    ```
-   Если вас не устраивают изменения в файле, отредактируйте его с помощью:
    ```shell
    chezmoi edit file_name
    ```
-   Также можно вызвать инструмент слияния, чтобы объединить изменения между текущим содержимым файла, файлом в вашей рабочей копии и измененным содержимым файла:
    ```shell
    chezmoi merge file_name
    ```
-   При существующем каталоге `chezmoi` можно получить и применить последние изменения из вашего репозитория:
    ```shell
    chezmoi update -v
    ```


#### <span class="section-num">3.3.5</span> Настройка новой машины с помощью одной команды {#настройка-новой-машины-с-помощью-одной-команды}

-   Можно установить свои `dotfiles` на новый компьютер с помощью одной команды:
    ```shell
    chezmoi init --apply https://github.com/<username>/dotfiles.git
    ```
-   Через ssh:
    ```shell
    chezmoi init --apply git@github.com:<username>/dotfiles.git
    ```


#### <span class="section-num">3.3.6</span> Ежедневные операции c `chezmoi` {#ежедневные-операции-c-chezmoi}

<!--list-separator-->

1.  Извлеките последние изменения из репозитория и примените их

    -   Можно извлечь изменения из репозитория и применить их одной командой:
        ```shell
        chezmoi update
        ```
    -   Это запускается `git pull --autostash --rebase` в вашем исходном каталоге, а затем `chezmoi apply`.

<!--list-separator-->

2.  Извлеките последние изменения из своего репозитория и посмотрите, что изменится, фактически не применяя изменения

    -   Выполните:
        ```shell
        chezmoi git pull -- --autostash --rebase && chezmoi diff
        ```
    -   Это запускается `git pull --autostash --rebase` в вашем исходном каталоге, а `chezmoi diff` затем показывает разницу между целевым состоянием, вычисленным из вашего исходного каталога, и фактическим состоянием.
    -   Если вы довольны изменениями, вы можете применить их:
        ```shell
        chezmoi apply
        ```

<!--list-separator-->

3.  Автоматически фиксируйте и отправляйте изменения в репозиторий

    -   Можно автоматически фиксировать и отправлять изменения в исходный каталог в репозиторий.
    -   Эта функция отключена по умолчанию.
    -   Чтобы включить её, добавьте в файл конфигурации `~/.config/chezmoi/chezmoi.toml` следующее:
        ```shell
        [git]
            autoCommit = true
            autoPush = true
        ```
    -   Всякий раз, когда в исходный каталог вносятся изменения, `chezmoi` фиксирует изменения с помощью автоматически сгенерированного сообщения фиксации и отправляет их в ваш репозиторий.
    -   Будьте осторожны при использовании `autoPush`. Если ваш репозиторий `dotfiles` является общедоступным, и вы случайно добавили секрет в виде обычного текста, этот секрет будет отправлен в ваш общедоступный репозиторий.
