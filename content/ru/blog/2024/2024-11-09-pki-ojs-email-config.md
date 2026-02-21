---
title: "PKI OJS. Конфигурация e-mail"
author: ["Dmitry S. Kulyabov"]
date: 2024-11-09T19:30:00+03:00
lastmod: 2024-11-10T15:19:00+03:00
tags: ["sysadmin", "rudn"]
categories: ["job", "computer-science"]
draft: false
slug: "pki-ojs-email-config"
---

PKI OJS. Конфигурация e-mail.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Корпоративный почтовый адрес поддерживает Yandex.
-   Необходимо настроить пароль для приложения (см. [Почта. Yandex. Пароли приложений]({{< relref "2021-11-01-mail-yandex-application-passwords" >}})).
-   Также необходимо знать имена серверов почтовых сервисов (см. [Почта. Yandex. Настройка почтового клиента]({{< relref "2021-07-04-mail-yandex-configuring-mail-client" >}})).


## <span class="section-num">2</span> Создание пароля приложения {#создание-пароля-приложения}

-   Откройте страницу _Управление аккаунтом_ (<https://passport.yandex.ru/profile/>).
-   Войдите в раздел _Безопасность &gt; Доступ к вашим данным &gt; Пароли приложений_ (<https://id.yandex.ru/security/app-passwords>).
-   Включите переключатель _Использовать пароль приложений_.
-   Выберите пункт, соответствующий типу приложения.
-   Например, для работы с почтой выберите пункт _Почта_.
-   Придумайте название пароля, например укажите название приложения, для которого вы создаете пароль. С этим названием пароль будет отображаться в списке.
-   Нажмите кнопку _Далее_. Пароль приложения отобразится во всплывающем окне.
-   Созданный пароль можно увидеть только один раз. Если вы ввели его неправильно и закрыли окно, удалите текущий пароль и создайте новый.


### <span class="section-num">2.1</span> Видео {#видео}

{{< tabs tabTotal="4" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube dce7cc393ac83d782fafe466152e98a8 >}}

{{< /rtab >}}
{{< rtab tabName="Платформа" >}}

{{< plvideo 1SW2MCtcggzo >}}

{{< /rtab >}}
{{< rtab tabName="VKvideo" >}}

{{< vkvideo oid="606414976" id="456239647" hd="2" >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube P1hHHeyoqls >}}

{{< /rtab >}}
{{< /tabs >}}


## <span class="section-num">3</span> Настройка сайта OJS {#настройка-сайта-ojs}

-   Адрес сайта: <https://journals.rudn.ru/>.
-   Настройка почты делается на странице `https://journals.rudn.ru/<журнал>/manager/setup/1`
-   Для журнала _Discrete and Continuous Models and Applied Computational Science_ --- <https://journals.rudn.ru/miph/manager/setup/1>.
-   SMTP Yandex:
    -   адрес почтового сервера --- `smtp.yandex.ru`;
    -   защита соединения --- SSL/TLS;
    -   порт --- 465.


### <span class="section-num">3.1</span> Видео {#видео}

{{< tabs tabTotal="4" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 00fc8ad12e1098ffe54a6efb077d8d43 >}}

{{< /rtab >}}
{{< rtab tabName="Платформа" >}}

{{< plvideo yksiH_JHQRLf >}}

{{< /rtab >}}
{{< rtab tabName="VKvideo" >}}

{{< vkvideo oid="606414976" id="456239646" hd="2" >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube T0EOflU_xbk >}}

{{< /rtab >}}
{{< /tabs >}}
