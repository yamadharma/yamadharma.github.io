---
title: "Почта. Yahoo.com. Настройка почтового клиента"
author: ["Dmitry S. Kulyabov"]
date: 2022-04-26T17:01:00+03:00
lastmod: 2023-09-14T16:41:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "mail-yahoo-com-configuring-mail-client"
---

Настройка клиента для работы с почтой _Yahoo.com_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://mail.yahoo.com/>
-   Используются локализованные названия для папок IMAP.
-   Папки почты по умолчанию (отображение в web-интерфейсе):
    -   `INBOX`;
    -   `Архив`;
    -   `Корзина`;
    -   `Спам`;
    -   `Черновики`;
    -   `Отправленные`.
-   Папки почты по умолчанию (IMAP названия):
    -   `INBOX`;
    -   `Archive`;
    -   `Trash`;
    -   `Bulk Mail`;
    -   `Draft`;
    -   `Sent`.
-   Необходимо использовать пароль приложения: <https://help.yahoo.com/kb/generate-manage-third-party-passwords-sln15241.html>
    -   Войдите на страницу безопасности учетной записи Yahoo <https://login.yahoo.com/account/security?.lang=en-US&.intl=us&.src=yhelp>.
    -   Нажмите «Создать пароль приложения» или «Создать и управлять паролями приложений».
    -   Введите название вашего приложения в текстовое поле.
    -   Щёлкните _Создать пароль_.
    -   Следуйте инструкциям под паролем приложения.
    -   Щёлкните _Готово_.


## <span class="section-num">2</span> Настройка клиента {#настройка-клиента}

-   Справочная страница:
    -   <https://help.yahoo.com/kb/SLN4075.html>
    -   <https://help.yahoo.com/kb/pop-access-settings-instructions-yahoo-mail-sln4724.html>


### <span class="section-num">2.1</span> SMTP {#smtp}

-   login --- почтовый адрес `name@domain.ru` на `yahoo.com` (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   password --- пароль приложения для вашего почтового ящика домена на `yahoo.com`;
-   адрес почтового сервера --- `smtp.mail.yahoo.com`;
-   защита соединения --- SSL;
    -   порт --- 465;
-   защита соединения --- STARTTLS;
    -   порт --- 587.


### <span class="section-num">2.2</span> IMAP {#imap}

-   login --- почтовый адрес `name@domain.ru` на `yahoo.com` (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   password --- пароль приложения для вашего почтового ящика домена на `yahoo.com`;
-   адрес почтового сервера --- `imap.mail.yahoo.com`;
-   защита соединения --- SSL;
-   порт --- 993.


### <span class="section-num">2.3</span> POP3 {#pop3}

-   login --- почтовый адрес `name@domain.ru` на `yahoo.com` (где `name` --- это имя почтового ящика, а `domain.ru` --- имя домена);
-   password --- пароль приложения для вашего почтового ящика домена на `yahoo.com`;
-   адрес почтового сервера --- `pop.mail.yahoo.com`;
-   защита соединения --- SSL;
-   порт --- 995.


## <span class="section-num">3</span> Парольные файлы для _pass_ (см. [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})) {#парольные-файлы-для-pass--см-dot-менеджер-паролей-pass-20210428185000-менеджер-паролеи-pass-dot-md}

-   Для входа через web-интерфейс: `yahoo.com/account@yahoo.com.gpg`.
-   Пароль приложения: `yahoo.com/account@yahoo.com@apppassword.gpg`.
-   Пароль приложения для SMTP: `yahoo.com/account@yahoo.com@smtp.mail.yahoo.com.gpg`.
