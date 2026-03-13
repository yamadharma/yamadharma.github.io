---
title: "Почта. Синхронизация. mbsync"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-22T15:10:00+03:00
lastmod: 2024-10-19T16:15:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "mail-synchronization-mbsync"
---

Настройка синхронизации IMAP с помощью _mbsync_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Описание {#описание}

-   Домашняя страница: <https://isync.sourceforge.io/>.
-   Репозиторий: <https://sourceforge.net/p/isync/isync/ci/master/tree/>
-   `isync` / `mbsync` --- программа для синхронизации IMAP и локальных почтовых файлов.
-   `isync` --- старое название (для совместимости).


## <span class="section-num">2</span> Установка {#установка}

-   Gentoo
    ```shell
    emerge isync
    ```


## <span class="section-num">3</span> Настройка {#настройка}


### <span class="section-num">3.1</span> Общие положения {#общие-положения}

-   Все учётные записи приводятся к единой структуре.
-   Папки IMAP унифицируются следующим образом: Inbox, Archive, Sent, Trash, Drafts, Spam.
-   В принципе, никто не мешает использовать названия папок самого IMAP-сервера.


### <span class="section-num">3.2</span> Конфигурация учётных записей {#конфигурация-учётных-записей}

-   Учётные записи делаем по полному наименованию почты. Я это делаю потому, что у меня есть почтовые ящики с одинаковыми именами в разных почтовых доменах.
-   Создать необходимые каталоги:
    ```conf-unix
    mkdir -p ~/Maildir/account@domain
    ```
-   Можно создать каталоги все скопом из конфигурационного файла `~/.config/isyncrc`:
    ```shell
    #!/bin/sh

    MAILDIR=~/Maildir

    ## Make mailbox directories
    grep -e "^IMAPAccount" ~/.config/isyncrc | cut -d" " -f2 | xargs -I {} -n 1 mkdir -p "${MAILDIR}/{}"
    mbsync -a
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      Файл ~/bin/mbsync-mkdir
    </div>
-   Делаем конфигурационный файл для _mbsync_. Файл называется `~/.config/isyncrc`.
-   Чтобы не хранить пароли в конфигурационном файле (оператор `Pass`) будем использовать хранение пароля, совместимое с _emacs_ (с использованием оператора `PassCmd`):
    -   в файле `~/.authinfo.gpg` (см. [Emacs. Почта. Парольная аутентификация]({{< relref "2021-01-22-mail-password-authentication" >}})):
        -   структура команды:
            ```conf-unix
            PassCmd "gpg -q --for-your-eyes-only --no-tty -d ~/.authinfo.gpg | awk '/machine account@example.com/ {print $6}'"
            ```
    -   в менеджере паролей _pass_ (см. [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})):

        -   структура команды:

        <!--listend-->

        ```conf-unix
        PassCmd "pass email/example.com/account@example.com"
        ```

-   Начиная с версии _mbsync-1.4.1_ операторы `Master` и `Slave` заменены на `Far` и `Near`.


### <span class="section-num">3.3</span> Общие параметры {#общие-параметры}

-   Установка параметра `CopyArrivalDate`:
    ```conf-unix
    # By default (CopyArrivalDate no), if you copy an old email from inbox to
    # Archive (e.g.) it will get the date of the copy assigned, instead of just
    # keeping its original date of arrival! Also see:
    # https://rakhim.org/fastmail-setup-with-emacs-mu4e-and-mbsync-on-macos/
    # https://wiki.archlinux.org/index.php/Isync#Emails_on_remote_server_have_the_wrong_date
    CopyArrivalDate yes
    ```


### <span class="section-num">3.4</span> Примеры конфигурации для разных провайдеров {#примеры-конфигурации-для-разных-провайдеров}

-   Может потребоваться для разных провайдеров увеличить тайм-аут соединения (по умолчанию равно `20`):
    ```conf-unix
    # Increase timeout
    Timeout 120
    ```
-   Вместо `pass` можно использовать `gopass`. При последовательном запуске нескольких `pass` утилита может не находить ключ _pgp_.
-   Папки IMAP можно получить либо через web-интерфейс, либо в командной строке (см. [Запросы по протоколу imap из командной строки]({{< relref "2024-04-13-imap-queries-command-line" >}}))


#### <span class="section-num">3.4.1</span> Gmail {#gmail}

-   <https://www.google.com/intl/ru/gmail/about/>
-   [Почта. Google. Настройка почтового клиента]({{< relref "2021-07-06-mail-google-configuring-mail-client" >}})
-   Из-за структуры тегов Gmail необходимо явно задавать названия почтовых ящиков в директивах `Far` и `Near`.
-   Синхронизацию папки `Отправленные` можно отключить. Google сохраняет всю электронную почту в папке `Все сообщения`. В результате можно получить локальные дубликаты.
-   Рекомендуется на сайте Gmail настроить в пункте `Настройки > Пересылка и POP/IMAP > Доступ по протоколу IMAP` (`Settings` &gt; `Forwarding and POP/IMAP` &gt; `IMAP Access`):
    -   отметить `Автоматическое стирание включено (немедленно обновлять данные на сервере; по умолчанию)` `Auto-Expunge on - Immediately update the server. (default)`;
    -   ~~отметить `Автоматическое стирание выключено (ожидать, пока клиент не обновит данные на сервере)` (`Turn Auto Expunge Off`)~~;
    -   отметить `Архивировать сообщение (по умолчанию)` (`Archive message (default)`).
    -   ~~отметить `Отправить письмо в корзину` (`Send email to trash`)~~.
-   При использовании двуфакторной аутентификации (2FA) необходимо использовать _пароль приложения_ (см. [Почта. Подключение к Google]({{< relref "2020-12-25-mail-google-connect" >}})).
    ```conf-unix
    # IMAPAccount (gmail)

    IMAPAccount account@gmail.com
    Host imap.gmail.com
    User account@gmail.com
    # Pass ***************
    ## To store the password in an encrypted file use PassCmd instead of Pass
    # PassCmd "gpg -q --for-your-eyes-only --no-tty -d ~/.authinfo.gpg | awk '/machine account@gmail.com/ {print $6}'"
    # PassCmd "pass email/google.com/account@gmail.com@apppassword"
    PassCmd "pass email/google.com/account@gmail.com"
    Port 993
    TLSType IMAPS
    AuthMechs LOGIN
    TLSVersions +1.2 +1.3
    # Increase timeout
    Timeout 120

    IMAPStore account@gmail.com-remote
    Account account@gmail.com

    MaildirStore account@gmail.com-local
    Path ~/Maildir/account@gmail.com/
    Inbox ~/Maildir/account@gmail.com/Inbox
    SubFolders Verbatim

    IMAPStore account@gmail.com-remote
    Account account@gmail.com

    Channel account@gmail.com-inbox
    Far :account@gmail.com-remote:"INBOX"
    Near :account@gmail.com-local:"INBOX"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@gmail.com-trash
    # Far :account@gmail.com-remote:"[Gmail]/Trash"
    Far :account@gmail.com-remote:"[Gmail]/&BBoEPgRABDcEOAQ9BDA-"
    Near :account@gmail.com-local:"Trash"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@gmail.com-spam
    # Far :account@gmail.com-remote:"[Gmail]/Spam"
    Far :account@gmail.com-remote:"[Gmail]/&BCEEPwQwBDw-"
    Near :account@gmail.com-local:"Spam"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@gmail.com-all
    # Far :account@gmail.com-remote:"[Gmail]/All Mail"
    Far :account@gmail.com-remote:"[Gmail]/&BBIEQQRP- &BD8EPgRHBEIEMA-"
    Near :account@gmail.com-local:"Archive"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@gmail.com-drafts
    # Far :account@gmail.com-remote:"[Gmail]/Drafts"
    Far :account@gmail.com-remote:"[Gmail]/&BCcENQRABD0EPgQyBDgEOgQ4-"
    Near :account@gmail.com-local:"Drafts"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@gmail.com-sent
    # Far :account@gmail.com-remote:"[Gmail]/Sent Mail"
    Far :account@gmail.com-remote:"[Gmail]/&BB4EQgQ,BEAEMAQyBDsENQQ9BD0ESwQ1-"
    Near :account@gmail.com-local:"Sent"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Group account@gmail.com
    Channel account@gmail.com-inbox
    Channel account@gmail.com-trash
    Channel account@gmail.com-all
    Channel account@gmail.com-spam
    Channel account@gmail.com-drafts
    Channel account@gmail.com-sent
    ```


#### <span class="section-num">3.4.2</span> Apple {#apple}

-   <https://www.icloud.com/mail>
    ```conf-unix
    # IMAPAccount (Apple)

    IMAPAccount account@icloud.com
    Host imap.mail.me.com
    PORT 993
    User account@icloud.com
    PassCmd "gpg -q --for-your-eyes-only --no-tty -d ~/.authinfo.gpg | awk '/machine account@icloud.com/ {print $6}'"
    AuthMechs LOGIN
    TLSType IMAPS
    TLSVersions +1.2 +1.3
    # Increase timeout
    Timeout 120

    MaildirStore account@icloud.com-local
    Path ~/Maildir/account@icloud.com/
    Inbox ~/Maildir/account@icloud.com/Inbox
    SubFolders Verbatim

    IMAPStore account@icloud.com-remote
    Account account@icloud.com

    Channel account@icloud.com-all
    Far :account@icloud.com-remote:
    Near :account@icloud.com-local:
    # Included mailboxes
    Patterns "INBOX" "Archive" "Trash" "Spam" "Drafts"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@icloud.com-sent
    Far :account@icloud.com-remote:"Sent Messages"
    Near :account@icloud.com-local:"Sent"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Group account@icloud.com
    Channel account@icloud.com-sent
    Channel account@icloud.com-all
    ```


#### <span class="section-num">3.4.3</span> GMX {#gmx}

-   <https://www.gmx.com/>
-   <https://www.gmx.net/>
    ```conf-unix
    # IMAPAccount (GMX)

    IMAPAccount account@gmx.com
    Host imap.gmx.com
    User account@gmx.com
    PassCmd "gpg -q --for-your-eyes-only --no-tty -d ~/.authinfo.gpg | awk '/machine account@gmx.com/ {print $6}'"
    AuthMechs LOGIN
    TLSType IMAPS
    TLSVersions +1.2 +1.3
    # Increase timeout
    Timeout 120

    MaildirStore account@gmx.com-local
    Path ~/Maildir/account@gmx.com/
    Inbox ~/Maildir/account@gmx.com/Inbox
    SubFolders Verbatim

    IMAPStore account@gmx.com-remote
    Account account@gmx.com

    Channel account@gmx.com
    Far :account@gmx.com-remote:
    Near :account@gmx.com-local:
    Patterns "INBOX" "Archive" "Trash" "Spam" "Drafts" "Sent"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *
    ```


#### <span class="section-num">3.4.4</span> Proton {#proton}

-   <https://protonmail.com/>
-   Заблокирован в России.
-   Для работы необходимо установить локальное приложение <https://protonmail.com/bridge/>.
    ```conf-unix
    # IMAPAccount (Proton)

    IMAPAccount account@protonmail.com
    Host 127.0.0.1
    PORT 1111
    User account@protonmail.com
    PassCmd "gpg -q --for-your-eyes-only --no-tty -d ~/.authinfo.gpg | awk '/machine account@protonmail.com/ {print $6}'"
    AuthMechs LOGIN
    TLSType STARTTLS
    TLSVersions +1.2 +1.3
    # Increase timeout
    Timeout 120

    MaildirStore account@protonmail.com-local
    Path ~/Maildir/account@protonmail.com/
    Inbox ~/Maildir/account@protonmail.com/Inbox
    SubFolders Verbatim

    IMAPStore account@protonmail.com-remote
    Account account@protonmail.com

    Channel account@protonmail.com
    Far :account@protonmail.com-remote:
    Near :account@protonmail.com-local:
    Patterns "INBOX" "Archive" "Trash" "Spam" "Drafts" "Sent"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *
    ```


#### <span class="section-num">3.4.5</span> Yandex {#yandex}

-   <https://yandex.ru/>
-   [Почта. Yandex. Настройка почтового клиента]({{< relref "2021-07-04-mail-yandex-configuring-mail-client" >}})
-   Пароли приложений
    -   При подключении паролей приложений обычные пароли использовать не получится. Придётся сгенерить пароль приложения (см. [Почта. Yandex. Пароли приложений]({{< relref "2021-11-01-mail-yandex-application-passwords" >}})).
    -   Для паролей `pass`:
        -   Пароль для приложения почты можно назвать `account@yandex.ru@apppassword@mail`.
        -   Пароль для smtp следует именовать как `account@yandex.ru@smtp.yandex.ru` (это тот же пароль для почтового приложения).
-   Конфигурация:
    ```conf-unix
    ## IMAPAccount (Yandex)

    IMAPAccount account@yandex.ru
    Host imap.yandex.ru
    User account@yandex.ru
    # Pass ***************
    ## To store the password in an encrypted file use PassCmd instead of Pass
    # PassCmd "gpg -q --for-your-eyes-only --no-tty -d ~/.authinfo.gpg | awk '/machine account@yandex.ru/ {print $6}'"
    # PassCmd "pass email/yandex.ru/account@yandex.ru@apppassword@mail"
    PassCmd "pass email/yandex.ru/account@yandex.ru"
    AuthMechs LOGIN
    TLSType IMAPS
    TLSVersions +1.2 +1.3
    # Increase timeout
    Timeout 120

    MaildirStore account@yandex.ru-local
    Path ~/Maildir/account@yandex.ru/
    Inbox ~/Maildir/account@yandex.ru/Inbox
    SubFolders Verbatim

    IMAPStore account@yandex.ru-remote
    Account account@yandex.ru

    Channel account@yandex.ru
    Far :account@yandex.ru-remote:
    Near :account@yandex.ru-local:
    Patterns "INBOX" "Archive" "Trash" "Spam" "Drafts" "Sent"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *
    ```


#### <span class="section-num">3.4.6</span> Mail.ru {#mail-dot-ru}

-   [Почта. Mail.ru. Настройка почтового клиента]({{< relref "2021-07-04-mail-mail-ru-configuring-mail-client" >}})
-   Пароли приложений
    -   При подключении паролей приложений обычные пароли использовать не получится. Придётся сгенерить пароль приложения (см. [Пароли mail.ru]({{< relref "2022-10-27-mail-ru-passwords" >}})).
    -   Для паролей `pass`:
        -   Пароль для приложения почты можно назвать `account@mail.ru@apppassword@mail`.
        -   Пароль для smtp следует именовать как `account@mail.ru@smtp.mail.ru` (это тот же пароль для почтового приложения).
-   Конфигурация:
    ```conf-unix
    ## IMAPAccount (Mail.ru)

    IMAPAccount account@mail.ru
    Host imap.mail.ru
    User account@mail.ru
    # Pass ***************
    ## To store the password in an encrypted file use PassCmd instead of Pass
    # PassCmd "gpg -q --for-your-eyes-only --no-tty -d ~/.authinfo.gpg | awk '/machine account@mail.ru@apppassword@mail/ {print $6}'"
    PassCmd "pass email/mail.ru/account@mail.ru@apppassword@mail"
    AuthMechs LOGIN
    TLSType IMAPS
    TLSVersions +1.2 +1.3
    # Increase timeout
    Timeout 120

    MaildirStore account@mail.ru-local
    Path ~/Maildir/account@mail.ru/
    Inbox ~/Maildir/account@mail.ru/Inbox
    SubFolders Verbatim

    IMAPStore account@mail.ru-remote
    Account account@mail.ru

    Channel account@mail.ru-inbox
    Far :account@mail.ru-remote:"INBOX"
    Near :account@mail.ru-local:"INBOX"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@mail.ru-trash
    Far :account@mail.ru-remote:"Корзина"
    Near :account@mail.ru-local:"Trash"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@mail.ru-spam
    Far :account@mail.ru-remote:"Спам"
    Near :account@mail.ru-local:"Spam"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@mail.ru-drafts
    Far :account@mail.ru-remote:"Черновики"
    Near :account@mail.ru-local:"Drafts"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@mail.ru-archive
    Far :account@mail.ru-remote:"Архив"
    Near :account@mail.ru-local:"Archive"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@mail.ru-sent
    Far :account@mail.ru-remote:"Отправленные"
    Near :account@mail.ru-local:"Sent"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Group account@mail.ru
    Channel account@mail.ru-inbox
    Channel account@mail.ru-trash
    Channel account@mail.ru-spam
    Channel account@mail.ru-drafts
    Channel account@mail.ru-archive
    Channel account@mail.ru-sent
    ```


#### <span class="section-num">3.4.7</span> Office365 {#office365}

-   [Почта. Office365. Настройка почтового клиента]({{< relref "2021-07-04-mail-office365-configuring-mail-client" >}})
-   Названия IMAP-ящиков даётся в модифицированной кодировке UTF-7 (см. [Почта. Кодировка папок IMAP]({{< relref "2021-07-04-mail-imap-folder-encoding" >}})).

<!--list-separator-->

1.  Аутентификация _LOGIN_

    -   Конфигурация _mbsync_:
        ```conf-unix
        ## IMAPAccount (outlook.office365.com)

        IMAPAccount account@example.com
        Host smtp.office365.com
        User account@example.com
        # Pass ***************
        ## To store the password in an encrypted file use PassCmd instead of Pass
        # PassCmd "gpg -q --for-your-eyes-only --no-tty -d ~/.authinfo.gpg | awk '/machine account@example.com/ {print $6}'"
        PassCmd "pass email/example.com/account@example.com"
        AuthMechs LOGIN
        TLSType IMAPS
        TLSVersions +1.2 +1.3
        # Increase timeout
        Timeout 120
        PipelineDepth 50

        MaildirStore account@example.com-local
        Path ~/Maildir/account@example.com/
        Inbox ~/Maildir/account@example.com/Inbox
        SubFolders Verbatim

        IMAPStore account@example.com-remote
        Account account@example.com

        Channel account@example.com-inbox
        Far :account@example.com-remote:"INBOX"
        Near :account@example.com-local:"INBOX"
        CopyArrivalDate yes
        Create Both
        Expunge Both
        SyncState *

        Channel account@example.com-trash
        Far :account@example.com-remote:"&BCMENAQwBDsENQQ9BD0ESwQ1-"
        Near :account@example.com-local:"Trash"
        CopyArrivalDate yes
        Create Both
        Expunge Both
        SyncState *

        Channel account@example.com-spam
        Far :account@example.com-remote:"&BB0ENQQ2BDUEOwQwBEIENQQ7BEwEPQQwBE8- &BD8EPgRHBEIEMA-"
        Near :account@example.com-local:"Spam"
        CopyArrivalDate yes
        Create Both
        Expunge Both
        SyncState *

        Channel account@example.com-drafts
        Far :account@example.com-remote:"&BCcENQRABD0EPgQyBDgEOgQ4-"
        Near :account@example.com-local:"Drafts"
        CopyArrivalDate yes
        Create Both
        Expunge Both
        SyncState *

        Channel account@example.com-archive
        Far :account@example.com-remote:"Archive1"
        Near :account@example.com-local:"Archive"
        CopyArrivalDate yes
        Create Both
        Expunge Both
        SyncState *

        Channel account@example.com-sent
        Far :account@example.com-remote:"&BB4EQgQ,BEAEMAQyBDsENQQ9BD0ESwQ1-"
        Near :account@example.com-local:"Sent"
        CopyArrivalDate yes
        Create Both
        Expunge Both
        SyncState *

        Group account@example.com
        Channel account@example.com-inbox
        Channel account@example.com-trash
        Channel account@example.com-spam
        Channel account@example.com-drafts
        Channel account@example.com-archive
        Channel account@example.com-sent
        ```
    -   Конфигурация SMTP для Emacs:
        ```emacs-lisp
        (setq send-mail-function    'smtpmail-send-it
              smtpmail-smtp-server  "example.com"
              smtpmail-stream-type  'starttls
              smtpmail-smtp-service 587)
        ```

        -   Для smtp следует именовать пароль _pass_ как `account@example.com@smtp.office365.com` (см. [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})).

<!--list-separator-->

2.  Аутентификация _Oauth2_ с _DavMail_

    -   Аутентификацию _oauth2_ можно настроить с помощью _DavMail_ (см. [DavMail]({{< relref "2022-04-10-davmail" >}})).
    -   Сначала настройте _DavMail_ аутентификацией `O365Interactive` или `O365Manual`, а потом переключите в режим `O365Modern`.
    -   В конфигурации меняется блок аутентификации:
        ```conf-unix
        IMAPAccount account@example.com
        Host 127.0.0.1
        Port 1143
        User account@example.com
        # Pass ***************
        ## To store the password in an encrypted file use PassCmd instead of Pass
        # PassCmd "gpg -q --for-your-eyes-only --no-tty -d ~/.authinfo.gpg | awk '/machine account@example.com/ {print $6}'"
        PassCmd "pass email/example.com/account@example.com"
        AuthMechs LOGIN
        TLSType None
        ## Increase timeout
        Timeout 120
        PipelineDepth 50
        ```
    -   Конфигурация SMTP для Emacs:
        ```emacs-lisp
        (setq send-mail-function    'smtpmail-send-it
              smtpmail-smtp-server  "localhost"
              smtpmail-stream-type  'plain
              smtpmail-smtp-service 1025)
        ```

        -   Для smtp следует именовать пароль _pass_ как `account@example.com@localhost` (см. [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})).


#### <span class="section-num">3.4.8</span> Yahoo.com {#yahoo-dot-com}

-   [Почта. Yahoo.com. Настройка почтового клиента]({{< relref "2022-04-26-mail-yahoo-com-configuring-mail-client" >}})
-   Конфигурация:
    ```conf-unix
    ## IMAPAccount (Yahoo.com)

    IMAPAccount account@yahoo.com
    Host imap.mail.yahoo.com
    User account@yahoo.com
    # PassCmd "gpg -q --for-your-eyes-only --no-tty -d ~/.authinfo.gpg | awk '/machine account@yahoo.com/ {print $6}'"
    PassCmd "gopass email/yahoo.com/account@yahoo.com@apppassword"
    AuthMechs LOGIN
    TLSType IMAPS
    TLSVersions +1.2 +1.3
    # Increase timeout
    Timeout 120
    PipelineDepth 50

    MaildirStore account@yahoo.com-local
    Path ~/Maildir/account@yahoo.com/
    Inbox ~/Maildir/account@yahoo.com/Inbox
    SubFolders Verbatim

    IMAPStore account@yahoo.com-remote
    Account account@yahoo.com

    Channel account@yahoo.com-inbox
    Far :account@yahoo.com-remote:"INBOX"
    Near :account@yahoo.com-local:"INBOX"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@yahoo.com-trash
    Far :account@yahoo.com-remote:"Trash"
    Near :account@yahoo.com-local:"Trash"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@yahoo.com-spam
    Far :account@yahoo.com-remote:"Bulk"
    Near :account@yahoo.com-local:"Spam"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@yahoo.com-drafts
    Far :account@yahoo.com-remote:"Draft"
    Near :account@yahoo.com-local:"Drafts"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@yahoo.com-archive
    Far :account@yahoo.com-remote:"Archive"
    Near :account@yahoo.com-local:"Archive"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Channel account@yahoo.com-sent
    Far :account@yahoo.com-remote:"Sent"
    Near :account@yahoo.com-local:"Sent"
    CopyArrivalDate yes
    Create Both
    Expunge Both
    SyncState *

    Group account@yahoo.com
    Channel account@yahoo.com-inbox
    Channel account@yahoo.com-trash
    Channel account@yahoo.com-spam
    Channel account@yahoo.com-drafts
    Channel account@yahoo.com-archive
    Channel account@yahoo.com-sent
    ```


## <span class="section-num">4</span> Синхронизация {#синхронизация}


### <span class="section-num">4.1</span> Настройка синхронизации {#настройка-синхронизации}

-   Будем настраивать синхронизацию нескольких учётных записей.
-   Для хранения паролей будем использовать аутентификацию, совместимую с emacs (например, файл формата `.authinfo`) (см. [Emacs. Почта. Парольная аутентификация]({{< relref "2021-01-22-mail-password-authentication" >}})).


### <span class="section-num">4.2</span> Запуск из командной строки {#запуск-из-командной-строки}

-   Синхронизация конкретной учётной записи:
    ```shell
    mbsync <chanel>
    ```

-   Синхронизация всех учётных записей:
    ```shell
    mbsync --all
    ```


### <span class="section-num">4.3</span> Запуск по таймеру {#запуск-по-таймеру}

-   Для синхронизации с помощью `systemd` надо добавить сервис и таймер.
-   После создания этих файлов добавьте `mbsync.timer` в `systemctl`:
    ```shell
    systemctl --user --now enable mbsync.timer
    ```

-   `~/.config/systemd/user/mbsync.service`.
    ```conf-unix
    # ~/.config/systemd/user/mbsync.service

    [Unit]
    Description=Mailbox synchronization service

    [Service]
    Type=oneshot
    ExecStart=/usr/bin/mbsync -a
    ```

-   `~/.config/systemd/user/mbsync.service`. Здесь мы после синхронизации запускаем индексирование для `mu`.
    ```conf-unix
    # ~/.config/systemd/user/mbsync.service

    [Unit]
    Description=Mailbox synchronization service

    [Service]
    Type=oneshot
    ExecStart=-/usr/bin/mbsync -a
    ExecStartPost=-/usr/bin/mu index
    ```

    -   Знак `-` перед командой позволяет игнорировать код возврата.
-   `~/.config/systemd/user/mbsync.timer`. Настраиваем запуск `mbsync` через 2 минуты после загрузки, а затем запускаем каждые 5 минут.
    ```conf-unix
    # ~/.config/systemd/user/mbsync.timer

    [Unit]
    Description=Mailbox synchronization timer

    [Timer]
    OnBootSec=2m
    OnUnitActiveSec=5m
    Unit=mbsync.service

    [Install]
    WantedBy=timers.target
    ```


## <span class="section-num">5</span> Поддержка почтовых файлов {#поддержка-почтовых-файлов}


### <span class="section-num">5.1</span> Удаление дубликатов {#удаление-дубликатов}

-   При копировании могут возникать дубликаты сообщений.
-   Их можно удалить (см. [Почта. Удаление дубликатов сообщений из локальных почтовых ящиков]({{< relref "2021-09-09-removing-duplicate-messages" >}})).


## <span class="section-num">6</span> Перенос почтовых файлов на другую машину {#перенос-почтовых-файлов-на-другую-машину}

-   Имя почтового файла содержит имя хоста. Поэтому просто так синхронизировать почтовую базу между хостами не получится.
-   Синхронизация может понадобиться для случая, когда у Вас большие почтовые ящики, а сервер квотирует почтовый трафик.
-   Предлагается скопировать текущую базу на другой хост (в качестве первоначальной постовой базы), а потом переименовать файлы почты.
    -   Необходимо скопировать данные с `host1` на `host2`.
    -   Проведём проверку переименования:
        ```shell
        cd ~/Maildir/
        find . -iname "*host1*" | sed 'p;s:host1:host2:' | xargs -n2 -p mv
        ```
    -   Проведём переименование, убрав ключ `p` у `xargs`:
        ```shell
        cd ~/Maildir/
        find . -iname "*host1*" | sed 'p;s:host1:host2:' | xargs -n2 mv
        ```


## <span class="section-num">7</span> Технические моменты {#технические-моменты}


### <span class="section-num">7.1</span> Имена почтовых файлов {#имена-почтовых-файлов}

-   Информация по почтовым файлам хранится либо в каталоге `~/.mbsync` в файлах вида:
    ```shell
    <remote account>:<remote!folder>:<local account>:<local!folder>
    ```
-   Либо информация хранится в почтовых папках в файлах `.mbsyncstate` (параметр `SyncState *`).
-   В файле `.uidvalidity` хранится последняя отметка времени и идентификатор.
-   Файлы сообщений именуются по шаблону:
    ```shell
    <timestamp>.<PID>_<counter>.<hostname>,U=<increment>:2,<flags>
    ```
