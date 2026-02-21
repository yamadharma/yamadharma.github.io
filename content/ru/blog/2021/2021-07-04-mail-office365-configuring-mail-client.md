---
title: "Почта. Office365. Настройка почтового клиента"
author: ["Dmitry S. Kulyabov"]
date: 2021-07-04T17:47:00+03:00
lastmod: 2023-09-14T16:45:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "mail-office365-configuring-mail-client"
---

Настройка клиента для работы с почтой _Office365_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.office.com/>
-   Используются стандартные названия для папок IMAP.
-   Папки IMAP имеют локализованные названия. В web-интерфейсе они помечаются специальными иконками.


## <span class="section-num">2</span> Настройка клиента {#настройка-клиента}

-   Информация по настройке: <https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-8361e398-8af4-4e97-b147-6c6c4ac95353>
-   SMTP по умолчанию отключен, его нужно включать в свойствах почтового ящика, опция "SMTP с проверкой подлинности":
    -   <https://docs.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission>


### <span class="section-num">2.1</span> SMTP {#smtp}

-   login --- почтовый адрес `name@example.com` на Office365 (где `name` --- это имя почтового ящика, а `example.com` --- имя домена);
-   password --- пароль от почтового ящика домена на Office365;
-   адрес почтового сервера --- `smtp.office365.com`;
-   защита соединения --- STARTTLS;
-   порт --- 587.


### <span class="section-num">2.2</span> IMAP {#imap}

-   login --- почтовый адрес `name@example.com` на Office365 (где `name` --- это имя почтового ящика, а `example.com` --- имя домена);
-   password --- пароль от вашего почтового ящика домена на Office365;
-   адрес почтового сервера --- `outlook.office365.com`;
-   защита соединения --- SSL;
-   порт --- 993.


### <span class="section-num">2.3</span> POP3 {#pop3}

-   login --- почтовый адрес `name@example.com` на Office365 (где `name` --- это имя почтового ящика, а `example.com` --- имя домена);
-   password --- пароль от вашего почтового ящика домена на Office365;
-   адрес почтового сервера --- `outlook.office365.com`;
-   защита соединения --- SSL;
-   порт --- 995.
