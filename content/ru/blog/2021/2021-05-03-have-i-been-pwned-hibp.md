---
title: "Have I Been Pwned (HIBP)"
author: ["Dmitry S. Kulyabov"]
date: 2021-05-03T15:21:00+03:00
lastmod: 2023-07-12T18:08:00+03:00
tags: ["security", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "have-i-been-pwned-hibp"
---

Сервис _Have I Been Pwned?_ содержит данные по скомпрометированным интернет-ресурсам и позволяет проверить, скомпрометирована ли Ваша личная информация.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт <https://haveibeenpwned.com/>
-   Код <https://github.com/HaveIBeenPwned/>
-   Написан на C#.
-   Лицензия BSD.
-   2021-05-28 открыты исходные сервиса:
    -   <https://www.troyhunt.com/pwned-passwords-open-source-in-the-dot-net-foundation-and-working-with-the-fbi/>


## <span class="section-num">2</span> Порядок работы {#порядок-работы}

-   Переходим на сайт <https://haveibeenpwned.com/>.
-   Вводим адрес электронной почты и нажимаем кнопку _pwned_.
-   Если адрес скомпрометирован, то появится сообщение _Oh no - pwned!_.
    -   Будет показана информация о сайтах, допустивших утечку.
-   В противном случае появится сообщение _Good news - no pwnage found!_.
-   На сайте также имеется страница _Взломанные пароли_ _(Pwned Passwords)_.


## <span class="section-num">3</span> Клиентские утилиты {#клиентские-утилиты}


### <span class="section-num">3.1</span> passchek {#passchek}

-   <https://github.com/edyatl/passchek>


### <span class="section-num">3.2</span> pwnedpasswords.sh {#pwnedpasswords-dot-sh}

-   <https://github.com/jamesridgway/pwnedpasswords.sh>
