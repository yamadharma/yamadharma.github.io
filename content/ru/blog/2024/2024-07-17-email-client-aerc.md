---
title: "Почтовый клиент aerc"
author: ["Dmitry S. Kulyabov"]
date: 2024-07-17T18:55:00+03:00
lastmod: 2024-08-08T20:30:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "email-client-aerc"
---

Консольный почтовый клиент aerc.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://aerc-mail.org/>
-   Репозиторий:
    -   <https://git.sr.ht/~rjarry/aerc>
    -   <https://github.com/rjarry/aerc>
-   Сочетания клавиш в стиле Vim.
-   Поддержка нескольких учетных записей: IMAP, Maildir, Notmuch, Mbox и JMAP.
-   Протоколы передачи: IMAP, JMAP, SMTP, sendmail.
-   Асинхронная поддержка IMAP и JMAP.
-   Подписание, шифрование и проверка PGP с помощью GNUpg.


## <span class="section-num">2</span> Установка {#установка}

-   Gentoo:
    ```shell
    emerge mail-client/aerc
    ```


## <span class="section-num">3</span> Основные команды {#основные-команды}

-   Перемещение между электронными письмами: `j`, `k`, `Page up`, `Page down`, стрелки, `gg`, `G`.
-   Перемещение между папками: `Shift+j`, `Shift+k`.
-   Просмотр электронной почты: `Enter`.
-   Вернуться к списку адресов электронной почты: `q`.
-   Удалить электронную почту: `:delete`.
-   Написать электронное письмо: `C`.
-   Отправить письмо: `:q`.
-   Ответ: `Rr`.
-   Ответить всем: `rr`.


## <span class="section-num">4</span> Полезное {#полезное}


### <span class="section-num">4.1</span> Формате HTML {#формате-html}

-   В электронных письмах в формате HTML будут отображаться теги HTML.
-   Для рендеринга используется броузер w3.
-   Добавьте строку в `$XDG_CONFIG_HOME/aerc/aerc.conf`:
    ```conf-unix
    text/html=/usr/bin/w3m -T text/html -o display_link_number=1
    ```


### <span class="section-num">4.2</span> Адресная книга VCARD {#адресная-книга-vcard}

-   Используйте `khard`.
-   Настройте в `$XDG_CONFIG_HOME/aerc/aerc.conf`:
    ```conf-unix
    [compose]
    address-book-cmd=khard email --parsable --remove-first-line %s
    ```
