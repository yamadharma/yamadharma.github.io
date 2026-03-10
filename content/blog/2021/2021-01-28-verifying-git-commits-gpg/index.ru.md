---
title: "Верификация коммитов git с помощью GPG"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-28T18:47:00+03:00
lastmod: 2026-01-28T18:41:00+03:00
tags: ["sysadmin", "programming"]
categories: ["computer-science"]
draft: false
slug: "verifying-git-commits-gpg"
---

Настроим верификацию коммитов git с помощью GPG.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Верификация коммитов с помощью _PGP_ {#верификация-коммитов-с-помощью-pgp}

-   Как настроить PGP-подпись коммитов с помощью `gpg`.


### <span class="section-num">1.1</span> Создание ключа {#создание-ключа}

-   Генерируем ключ
    ```shell
    gpg --full-generate-key
    ```

    -   Из предложенных опций выбираем:
        -   тип _RSA and RSA_;
        -   размер 4096;
        -   выберите срок действия; значение по умолчанию --- 0 (срок действия не истекает никогда).
    -   GPG запросит личную информацию, которая сохранится в ключе:
        -   Имя (не менее 5 символов).
        -   Адрес электронной почты.
            -   При вводе email убедитесь, что он соответствует адресу, используемому на GitHub.
        -   Комментарий. Можно ввести что угодно или нажать клавишу ввода, чтобы оставить это поле пустым.


### <span class="section-num">1.2</span> Экспорт ключа {#экспорт-ключа}

-   Выводим список ключей и копируем отпечаток приватного ключа:
    ```shell
    gpg --list-secret-keys --keyid-format LONG
    ```

    -   Отпечаток ключа --- это последовательность байтов, используемая для идентификации более длинного, по сравнению с самим отпечатком ключа.
    -   Формат строки:
        ```text
        sec   Алгоритм/Отпечаток_ключа Дата_создания [Флаги] [Годен_до]
              ID_ключа
        ```
-   Экспортируем ключ в формате ASCII по его отпечатку:
    ```shell
    gpg --armor --export <PGP Fingerprint>
    ```


### <span class="section-num">1.3</span> Добавление GPG ключа в GitHub {#добавление-gpg-ключа-в-github}

-   Копируем ключ и добавляем его в настройках профиля на GitHub (или GitLab).
-   Cкопируйте ваш сгенерированный PGP ключ в буфер обмена:
    -   X11:
        ```shell
        gpg --armor --export <PGP Fingerprint> | xclip -sel clip
        ```
    -   Wayland:
        ```shell
        gpg --armor --export <PGP Fingerprint> | wl-copy
        ```
-   Перейдите в настройки GitHub (<https://github.com/settings/keys>), нажмите на кнопку _New GPG key_ и вставьте полученный ключ в поле ввода.


### <span class="section-num">1.4</span> Подписывание коммитов git {#подписывание-коммитов-git}

-   Подпись коммитов при работе через терминал:
    ```shell
    git commit -a -S -m 'your commit message'
    ```
-   Флаг `-S` означает создание подписанного коммита. При этом может потребоваться ввод кодовой фразы, заданной при генерации GPG-ключа.


### <span class="section-num">1.5</span> Настройка автоматических подписей коммитов git {#настройка-автоматических-подписей-коммитов-git}

-   Используя введёный email, укажите Git применять его при подписи коммитов:
    ```shell
    git config --global user.signingkey <PGP Fingerprint>
    git config --global commit.gpgsign true
    git config --global gpg.program $(which gpg)
    ```


## <span class="section-num">2</span> Использование Keybase {#использование-keybase}

-   Для генерации и хранения GPG ключей можно использовать Keybase <https://keybase.io/>.
-   После того, как вы зарегистрируетесь в Keybase, зайдите в терминал и запустите следующие команды:
    ```shell
    keybase login
    ```


### <span class="section-num">2.1</span> Генерация GPG ключа {#генерация-gpg-ключа}

-   Создайте новый GPG ключ, используя ваше настоящее имя и email, сохраненный в GitHub:
    ```shell
    keybase pgp gen
    ```
-   Просмотр списка ключей:
    ```shell
    keybase pgp list
    ```


### <span class="section-num">2.2</span> Добавление GPG ключа в GitHub {#добавление-gpg-ключа-в-github}

-   Cкопируйте ваш сгенерированный PGP ключ:
    ```shell
    keybase pgp export | xclip -i
    ```
-   Перейдите в настройки GitHub (<https://github.com/settings/keys>), нажмите на кнопку _New GPG key_ и вставьте полученный ключ в поле ввода.


## <span class="section-num">3</span> Проверка коммитов в Git {#проверка-коммитов-в-git}

-   GitHub и GitLab будут показывать значок _Verified_ рядом с вашими новыми коммитами.


### <span class="section-num">3.1</span> Режим бдительности (vigilant mode) {#режим-бдительности--vigilant-mode}

-   На GitHub есть настройка [vigilant mode](https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification/displaying-verification-statuses-for-all-of-your-commits).
-   Все неподписанные коммиты будут явно помечены как _Unverified_.
-   Включается это в настройках в разделе _SSH and GPG keys_. Установите метку на _Flag unsigned commits as unverified_.
