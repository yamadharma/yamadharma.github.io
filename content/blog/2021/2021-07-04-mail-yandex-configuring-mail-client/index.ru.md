---
title: "Почта. Yandex. Настройка почтового клиента"
author: ["Dmitry S. Kulyabov"]
date: 2021-07-04T12:16:00+03:00
lastmod: 2024-04-23T15:57:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "mail-yandex-configuring-mail-client"
---

Настройка клиента для работы с почтой _Yandex_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://yandex.ru/>
-   Используются стандартные названия для папок IMAP.
-   Папки почты по умолчанию:
    -   `INBOX`;
    -   `Archive`;
    -   `Trash`;
    -   `Spam`;
    -   `Drafts`;
    -   `Sent`.
-   Нежелательные письма (_папка Spam_) удаляются через 10 дней.
-   Удалённые письма (_папка Trash_ ) удаляются через 31 день.


## <span class="section-num">2</span> Включение доступа к почтовому ящику {#включение-доступа-к-почтовому-ящику}

-   Проверить статус включения доступа к почтовым ящикам по протоколам IMAP и POP3 можно:
    -   по пунктам меню: `Все настройки > Почтовые программы`;
    -   по ссылке: <https://mail.yandex.ru/#setup/client>.
-   Авторизация для IMAP проводится через пароли приложений (см. [Почта. Yandex. Пароли приложений]({{< relref "2021-11-01-mail-yandex-application-passwords" >}})).
-   В Яндекс 360 для IMAP можно использовать и пароль входа.


## <span class="section-num">3</span> Настройка клиента {#настройка-клиента}


### <span class="section-num">3.1</span> SMTP {#smtp}

-   login --- почтовый адрес `name@domain.ru` на Яндексе (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   при имени ящика вида `name@yandex.ru`, логином является часть адреса до знака `@`;
-   password :
    -   пароль для почтового приложения (см. [Почта. Yandex. Пароли приложений]({{< relref "2021-11-01-mail-yandex-application-passwords" >}})).
-   адрес почтового сервера --- `smtp.yandex.ru`;
-   защита соединения --- SSL/TLS;
-   порт --- 465.


### <span class="section-num">3.2</span> IMAP {#imap}

-   login --- почтовый адрес `name@domain.ru` на Яндексе (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   при имени ящика вида `name@yandex.ru`, логином является часть адреса до знака `@`;
-   password :
    -   пароль от Яндекс ID (единый аккаунт на Яндексе) (OAuth2) или;
    -   пароль для почтового приложения (см. [Почта. Yandex. Пароли приложений]({{< relref "2021-11-01-mail-yandex-application-passwords" >}})).
-   адрес почтового сервера --- `imap.yandex.ru`;
-   защита соединения --- SSL/TLS;
-   порт --- 993.


### <span class="section-num">3.3</span> POP3 {#pop3}

-   login --- почтовый адрес `name@domain.ru` на Яндексе (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   при имени ящика вида `name@yandex.ru`, логином является часть адреса до знака `@`;
-   password :
    -   пароль от Яндекс ID (единый аккаунт на Яндексе) (OAuth2) или;
    -   пароль для почтового приложения (см. [Почта. Yandex. Пароли приложений]({{< relref "2021-11-01-mail-yandex-application-passwords" >}})).
-   адрес почтового сервера --- `pop.yandex.ru`;
-   защита соединения --- SSL;
-   порт --- 995.


## <span class="section-num">4</span> Синхронизация контактов {#синхронизация-контактов}

-   Используйте для адресной книги формат CardDAV.
-   login --- почтовый адрес `name@domain.ru` на Яндексе (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   при имени ящика вида `name@yandex.ru`, логином является `name@yandex.ru`;
-   password :
    -   пароль от Яндекс ID (единый аккаунт на Яндексе) (OAuth2) или;
    -   пароль для почтового приложения (см. [Почта. Yandex. Пароли приложений]({{< relref "2021-11-01-mail-yandex-application-passwords" >}})).
-   адрес сервера: `carddav.yandex.ru`.


## <span class="section-num">5</span> Синхронизация календаря {#синхронизация-календаря}

-   Используйте для адресной книги формат CalDAV.
-   login --- почтовый адрес `name@domain.ru` на Яндексе (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   при имени ящика вида `name@yandex.ru`, логином является `name@yandex.ru`;
-   password :
    -   пароль от Яндекс ID (единый аккаунт на Яндексе) (OAuth2) или;
    -   пароль для почтового приложения (см. [Почта. Yandex. Пароли приложений]({{< relref "2021-11-01-mail-yandex-application-passwords" >}})).
-   адрес сервера: `caldav.yandex.ru` (<https://caldav.yandex.ru>).
