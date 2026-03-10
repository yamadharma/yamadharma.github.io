---
title: "Почта. vk.com. Настройка почтового клиента"
author: ["Dmitry S. Kulyabov"]
date: 2023-09-03T17:14:00+03:00
lastmod: 2023-09-10T20:37:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "mail-vk-com-configuring-mail-client"
---

Настройка почтового клиента для почты _vk.com_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://vk.mail.ru/>
-   Сделан на основе сервиса почты _mail.ru_ (см. [Почта. Mail.ru. Настройка почтового клиента]({{< relref "2021-07-04-mail-mail-ru-configuring-mail-client" >}})).
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


### <span class="section-num">2.1</span> Общие параметры {#общие-параметры}

-   login: адрес электронной почты в формате `имя_пользователя@vk.com`, где `имя_пользователя` --- учётная запись ВКонтакте.
-   password: пароль от учётной записи ВКонтакте.


### <span class="section-num">2.2</span> SMTP {#smtp}

-   адрес почтового сервера: `smtp.vk.com`;
-   защита соединения: SSL;
-   порт: 465.


### <span class="section-num">2.3</span> IMAP {#imap}

-   адрес почтового сервера: `imap.vk.com`;
-   защита соединения: SSL;
-   порт: 993.


### <span class="section-num">2.4</span> POP3 {#pop3}

-   адрес почтового сервера --- `imap.vk.com`;
-   защита соединения: SSL;
-   порт: 995.
