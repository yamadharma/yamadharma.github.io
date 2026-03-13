---
title: "Менеджер паролей gopass"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-19T14:45:00+03:00
lastmod: 2025-08-19T15:59:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "gopass-password-manager"
---

Менеджер паролей gopass.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Реализация `pass` на go с дополнительными интегрированными функциями
-   Сайт: <https://www.gopass.pw/>.
-   Репозиторий: <https://github.com/gopasspw/gopass>

-   Данные хранятся с использованием GPG (OpenPGP) или Age.
-   Синхронизация через Git: пароли хранятся в репозитории Git, что упрощает совместную работу.
-   Поддержка команд: несколько пользователей могут иметь доступ к общим хранилищам.
-   Генерация паролей: создание сложных паролей прямо из терминала.
-   Мультиплатформенность: работает на Linux, macOS, Windows.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Linux {#linux}

-   Debian/Ubuntu:

<!--listend-->

```shell
sudo apt install gopass
```


### <span class="section-num">2.2</span> macOS {#macos}

-   С помощью Homebrew:

<!--listend-->

```shell
brew install gopass
```


### <span class="section-num">2.3</span> Windows {#windows}

-   С помощью Chocolatey (см. [Пакетный менеджер для Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})):

<!--listend-->

```shell
choco install gopass
```


## <span class="section-num">3</span> Основные операции {#основные-операции}


### <span class="section-num">3.1</span> 1. Инициализация хранилища {#1-dot-инициализация-хранилища}

-   Создаём хранилище и настраивает GPG-ключ

<!--listend-->

```shell
gopass init
```


### <span class="section-num">3.2</span> 2. Добавление пароля: {#2-dot-добавление-пароля}

-   Запрашивает логин и пароль:

<!--listend-->

```shell
gopass insert social/media/twitter
```


### <span class="section-num">3.3</span> 3. Просмотр пароля {#3-dot-просмотр-пароля}

```shell
gopass show social/media/twitter
```


### <span class="section-num">3.4</span> 4. Генерация пароля {#4-dot-генерация-пароля}

-   Создаёт пароль из 20 символов:

<!--listend-->

```shell
gopass generate social/media/instagram 20
```


## <span class="section-num">4</span> Работа с форматом хранилища Git {#работа-с-форматом-хранилища-git}


### <span class="section-num">4.1</span> Клонирование общего хранилища {#клонирование-общего-хранилища}

```shell
gopass clone git@github.com:yourteam/passwords.git
```


## <span class="section-num">5</span> Командная работа {#командная-работа}


### <span class="section-num">5.1</span> Добавление пользователя {#добавление-пользователя}

-   Экспортируйте публичный GPG-ключ коллеги:
    ```shell
    gpg --export colleague@example.com > colleague.pub
    ```

-   Добавьте его в хранилище:
    ```shell
    gopass recipients add colleague@example.com
    ```

-   Синхронизируйте изменения:
    ```shell
    gopass sync
    ```


## <span class="section-num">6</span> Безопасность {#безопасность}

-   GPG-шифрование: каждый пароль зашифрован отдельно.
-   Аудит: история изменений через `gopass history`.
-   Проверка на утечки (ищет пароли в публичных базах утечек):
    ```shell
    gopass audit
    ```


## <span class="section-num">7</span> Полезные команды {#полезные-команды}

| Команда                            | Описание                        |
|------------------------------------|---------------------------------|
| `gopass list`                      | Показать структуру хранилища    |
| `gopass search twitter`            | Найти пароль по ключевому слову |
| `gopass edit social/media/twitter` | Изменить запись                 |
| `gopass mounts`                    | Показать подключённые хранилища |
| `gopass sync`                      | Синхронизировать все хранилища  |


## <span class="section-num">8</span> Интеграции {#интеграции}


### <span class="section-num">8.1</span> gopassbridge {#gopassbridge}

-   Броузеры: плагины для Firefox/Chrome ([gopassbridge](https://github.com/gopasspw/gopassbridge)).


### <span class="section-num">8.2</span> git-credential-gopass {#git-credential-gopass}

-   Интеграция менеджера паролей Gopass с Git.
-   Позволяет безопасно хранить и автоматически подставлять учётные данные (логины, пароли, токены) для работы с Git-репозиториями.
-   [gopass. Интеграция с git]({{< relref "2025-08-19--gopass-integration-git" >}})
