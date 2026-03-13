---
title: "Почта. Mail.ru. Настройка почтового клиента"
author: ["Dmitry S. Kulyabov"]
date: 2021-07-04T15:30:00+03:00
lastmod: 2023-09-04T17:11:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "mail-mail-ru-configuring-mail-client"
---

Настройка клиента для работы с почтой _Mail.ru_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://mail.ru/>
-   Используются локализованные названия для папок IMAP.
-   Папки почты по умолчанию:
    -   `INBOX`;
    -   `Архив`;
    -   `Корзина`;
    -   `Спам`;
    -   `Черновики`;
    -   `Отправленные`.
-   Имена папок можно передавать в Unicode.


## <span class="section-num">2</span> Настройка клиента {#настройка-клиента}

-   Справочная страница: <https://help.mail.ru/mail/mailer/popsmtp>


### <span class="section-num">2.1</span> SMTP {#smtp}

-   login --- почтовый адрес `name@domain.ru` на Mail.ru (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   password --- пароль от почтового ящика домена на Mail.ru;
-   адрес почтового сервера --- `smtp.mail.ru`;
-   защита соединения --- SSL;
-   порт --- 465.


### <span class="section-num">2.2</span> IMAP {#imap}

-   login --- почтовый адрес `name@domain.ru` на Mail.ru (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   password --- пароль от вашего почтового ящика домена на Mail.ru;
-   адрес почтового сервера --- `imap.mail.ru`;
-   защита соединения --- SSL;
-   порт --- 993.


### <span class="section-num">2.3</span> POP3 {#pop3}

-   login --- почтовый адрес `name@domain.ru` на Mail.ru (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   password --- пароль от вашего почтового ящика домена на Mail.ru;
-   адрес почтового сервера --- `pop.mail.ru`;
-   защита соединения --- SSL;
-   порт --- 995.
