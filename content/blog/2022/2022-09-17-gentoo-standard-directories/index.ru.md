---
title: "Стандартные каталоги Gentoo"
author: ["Dmitry S. Kulyabov"]
date: 2022-09-17T13:31:00+03:00
lastmod: 2023-10-05T20:21:00+03:00
tags: ["linux", "gentoo"]
categories: ["computer-science"]
draft: false
slug: "gentoo-standard-directories"
---

Стандартные каталоги Gentoo.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Конфигурация portage {#конфигурация-portage}


### <span class="section-num">1.1</span> Основные файлы настройки {#основные-файлы-настройки}

-   Portage поставляется с настройками по умолчанию, которые хранятся в `/usr/share/portage/config/make.globals`.
-   Все настройки Portage обрабатываются с помощью переменных.
-   У portage есть конфигурационные файлы по умолчанию, которые является частью системного профиля.
-   Системный профиль задаётся с помощью символьной ссылки `/etc/portage/make.profile`.
-   Для замены конфигурационных переменных следует использовать файл `/etc/portage/make.conf`.
-   Пример конфигурационного файла: `/usr/share/portage/config/make.conf.example`.


### <span class="section-num">1.2</span> Информация из определённого профиля {#информация-из-определённого-профиля}

-   Каталог `/etc/portage/make.profile` является символьной ссылкой на один из профилей.
-   По умолчанию это `/var/db/repos/gentoo/profiles/`.
-   Профиль, на который указывает символьная ссылка, и есть системный профиль.
-   Профиль содержит информацию о конкретной архитектуре и настройках программного обеспечения.


### <span class="section-num">1.3</span> Пользовательская конфигурация {#пользовательская-конфигурация}

-   Для пользовательских настроек следует использовать файлы в `/etc/portage/`.
-   Пользователи могут создать в `/etc/portage/` следующие файлы:
    -   `package.mask`: список пакетов, которые Portage никогда не будет устанавливать;
    -   `package.unmask`: список пакетов, которые Portage будет устанавливать, даже если они заблокированы на системном уровне;
    -   `package.accept_keywords`: список пакетов, которые Portage будет устанавливать, даже если они не подходят для используемой системы или архитектуры;
    -   `package.use` список пакетов, для которых необходимо использовать специфичные USE-флаги, а не брать системные USE-флаги.
-   Они могут быть не файлами, а каталогами (содержимое разбито по отдельным файлам).


## <span class="section-num">2</span> Каталоги системы portage {#каталоги-системы-portage}


### <span class="section-num">2.1</span> Изменение расположения каталогов {#изменение-расположения-каталогов}

-   На основании обсуждения [#662982](https://bugs.gentoo.org/662982) были внесены изменения в расположение каталогов portage.

    <div class="table-caption">
      <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
      Смена расположения каталогов системы portage
    </div>

    | Назначение           | Старый путь              | Новый путь             |
    |----------------------|--------------------------|------------------------|
    | Дерево portage       | `/usr/portage`           | `/var/db/repos/gentoo` |
    | Исходный код пакетов | `/usr/portage/distfiles` | `/var/cache/distfiles` |
    | Бинарные пакеты      | `/usr/portage/packages`  | `/var/cache/binpkgs`   |


#### <span class="section-num">2.1.1</span> Миграция каталогов {#миграция-каталогов}

-   Удалите (или закомментируйте) любые записи `PORTDIR`, `DISTDIR`, `PKGDIR` в `/etc/portage/make.conf`.
-   Значения переменных окружения можно посмотреть командой:
    ```shell
    emerge --info -v
    emerge --info -v | grep PORTDIR
    emerge --info -v | grep DISTDIR
    emerge --info -v | grep PKGDIR
    ```
-   Если `/var/db/repos/` не существует, создайте его.
-   Переместите `/usr/portage/distfiles` в `/var/cache/distfiles`.
-   Переместите `/usr/portage/packages` в `/var/cache/binpkgs`.
-   Переместите `/usr/portage` в `/var/db/repos/gentoo`.
-   Измените переменную `location` в файле `/etc/portage/repos.conf/gentoo.conf` (или аналогичном) на `/var/db/repos/gentoo`.
-   Переустановите `portage`:
    ```shell
    DISTDIR=/var/cache/distfiles PKGDIR=/var/cache/binpkgs emerge --oneshot portage
    ```
-   Если вы запускаете локальное зеркало rsync, отредактируйте запись пути в `/etc/rsyncd.conf` так, чтобы она указывала на `/var/db/repos/gentoo`.
-   Если вы делитесь своими дистрибутивами, не забудьте обновить любую символическую ссылку или файл конфигурации, которые вам нужны для этого.


### <span class="section-num">2.2</span> Репозитории ebuild-файлов {#репозитории-ebuild-файлов}

-   Репозитории ebuild-файлов по умолчанию находится в /var/db/repos/&lt;reponame&gt;.


### <span class="section-num">2.3</span> Gentoo репозиторий ebuild-файлов {#gentoo-репозиторий-ebuild-файлов}

-   Gentoo репозиторий ebuild-файлов по умолчанию находится в `/var/db/repos/gentoo`.
-   Месторасположение определяется файлом `repos.conf`, пример которого можно найти в `/usr/share/portage/config/repos.conf`.
-   Чтобы изменить значения по умолчанию, скопируйте этот файл в `/etc/portage/repos.conf/gentoo.conf` и измените `location`.
-   Не забудьте сменить символьную ссылку на `/etc/portage/make.profile`, если хотите хранить (меняя переменную) Gentoo репозиторий ebuild-файлов в другом месте.
-   После изменения настройки location в `/etc/portage/repos.conf/gentoo.conf` рекомендуется изменить следующие переменные `/etc/portage/make.conf`, так как они не заметят изменений в `location`: `PKGDIR`, `DISTDIR`, `RPMDIR`.


### <span class="section-num">2.4</span> Двоичные пакеты {#двоичные-пакеты}

-   Бинарные пакеты находятся в каталоге `/var/cache/binpkgs`.
-   Этот каталог определяется переменной `PKGDIR`.


### <span class="section-num">2.5</span> Исходный код {#исходный-код}

-   По умолчанию исходный код для приложений хранится в каталоге `/var/cache/distfiles`.
-   Этот каталог определяется переменной `DISTDIR`.


### <span class="section-num">2.6</span> База состояния Portage {#база-состояния-portage}

-   База состояния системы (какие пакеты установлены, какие файлы какому пакету принадлежат и т.д.) находится в каталоге `/var/db/pkg`.


### <span class="section-num">2.7</span> Кеш Portage {#кеш-portage}

-   Кэш portage хранится в `/var/cache/edb`.
-   Можно отчистить это каталог, если на данный момент не запущено никаких приложений Portage.


### <span class="section-num">2.8</span> Временные файлы Portage {#временные-файлы-portage}

-   Временные файлы Portage по умолчанию хранятся в `/var/tmp/`.
-   Этот каталог определяется с помощью переменной `PORTAGE_TMPDIR`.


### <span class="section-num">2.9</span> Каталог компиляции {#каталог-компиляции}

-   Portage создаёт специальные каталоги в `/var/tmp/portage/` для всех компилируемых пакетов.
-   Этот каталог определяется переменной `PORTAGE_TMPDIR`.
