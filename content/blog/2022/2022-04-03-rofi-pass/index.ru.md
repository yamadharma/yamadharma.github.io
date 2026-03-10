---
title: "rofi-pass"
author: ["Dmitry S. Kulyabov"]
date: 2022-04-03T19:11:00+03:00
lastmod: 2023-08-13T18:24:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "rofi-pass"
---

Скрипт bash для работы с менеджером паролей _pass_ (см. [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})), используя интерфейс _rofi_ (см. [Запуск приложений. Rofi]({{< relref "2021-11-19-launcher_rofi" >}})).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Интеграция _pass_ с _rofi_
-   Репозиторий: <https://github.com/carnager/rofi-pass>


## <span class="section-num">2</span> Установка {#установка}

-   Установка
    -   Gentoo
        ```shell
        emerge x11-misc/rofi-pass
        ```

        -   Находится в репозитории [winny](https://gpo.zugaina.org/Overlays/winny).
        -   Добавить репозиторий:
            ```shell
            layman -a winny
            ```


## <span class="section-num">3</span> Функциональность {#функциональность}

-   Открытие URL-адреса записей с помощью горячих клавиш.
-   Добавление новых записей в хранилище паролей.
-   Редактирование существующих записей.
-   Создание новых паролей для записей.
-   Перемещение/удаление существующих записей.
-   Поддержка нескольких хранилищ паролей.
-   Автозаполнение полей пользователя и/или пароля.
    -   Формат файлов паролей должен быть следующим:
        ```conf-unix
        foobarmysecurepassword
        user: MyUser
        url: http://my.url.foo
        ```
-   Автоматический ввод имени пользователя на основе пути файла пароля.
    -   Структура хранилища паролей должна быть следующей:
        ```shell
        foo/bar/site.com/username
        ```
    -   Нужно установить `default-autotype` в `path :tab pass`.
-   Автоматический ввод более одного поля с использованием записи `autotype`:
    ```conf-unix
    foobarmysecurepassword
    ---
    user: MyUser
    SomeField: foobar
    AnotherField: barfoo
    url: http://my.url.foo
    autotype: SomeField :tab user :tab AnotherField :tab pass
    ```

    -   Используются флаги: `:tab`, `:enter`, `:space`, `:otp`.
-   Генерация одноразовых паролей.
    -   Формат одноразовых паролей должен быть совместим с `pass-otp`:
        ```conf-unix
        [...]
        otpauth://[...]
        ```
    -   Можно задать метод генерации одноразовых паролей:
        ```conf-unix
        [...]
        otp_method: /opt/obscure-otp-generator/oog --some-option some args
        ```
    -   Поле `:delay` вызывает задержку (по умолчанию 2 секунды).
-   Все горячие клавиши настраиваются в конфигурационном файле.
-   Имена полей `user`, `url`, `autotype` можно настраивать.


## <span class="section-num">4</span> Конфигурация {#конфигурация}


### <span class="section-num">4.1</span> Поиск файла конфигурации {#поиск-файла-конфигурации}

-   Конфигурации считывается в следующем порядке:
    -   переменная среды `ROFI_PASS_CONFIG`;
    -   `$HOME/.config/rofi-pass/config`;
    -   `/etc/rofi-pass.conf`.
-   Загружается только первый найденный файл.
-   Если файл конфигурации не существует, используются значения по умолчанию.
-   Возможно установить переменную среды при запуске:
    ```shell
    ROFI_PASS_CONFIG="/path/to/config" rofi-pass
    ```


### <span class="section-num">4.2</span> Стандартные сочетания клавиш {#стандартные-сочетания-клавиш}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Сочетания клавиш для <i>rofi-pass</i>
</div>

| Команда     | Сочетание клавиш |
|-------------|------------------|
| autotype    | `Alt+1`          |
| type_user   | `Alt+2`          |
| type_pass   | `Alt+3`          |
| open_url    | `Alt+4`          |
| copy_name   | `Alt+u`          |
| copy_url    | `Alt+l`          |
| copy_pass   | `Alt+p`          |
| show        | `Alt+o`          |
| copy_entry  | `Alt+2`          |
| type_entry  | `Alt+1`          |
| copy_menu   | `Alt+c`          |
| action_menu | `Alt+a`          |
| type_menu   | `Alt+t`          |
| help        | `Alt+h`          |
| switch      | `Alt+x`          |
| insert_pass | `Alt+n`          |


## <span class="section-num">5</span> Интеграция с графическим окружением {#интеграция-с-графическим-окружением}


### <span class="section-num">5.1</span> i3wm {#i3wm}

-   Можно добавить в конфигурационный файл вызов _rofi-pass_:
    ```conf-unix
    bindsym $mod+p exec "rofi-pass"
    ```
