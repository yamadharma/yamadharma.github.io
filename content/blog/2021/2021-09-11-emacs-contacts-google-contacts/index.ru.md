---
title: "Emacs. Контакты. Google-contacts"
author: ["Dmitry S. Kulyabov"]
date: 2021-09-11T13:33:00+03:00
lastmod: 2023-10-06T17:05:00+03:00
tags: ["emacs", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "emacs-contacts-google-contacts"
---

-   Пакет _google-contacts_.
-   На данный момент не работает из-за изменений API Google (замена Contacts API на People API).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/jd/google-contacts.el>


## <span class="section-num">2</span> Настройка {#настройка}


### <span class="section-num">2.1</span> Первый запуск {#первый-запуск}

-   Запустите google-contacts:
    ```elisp
    M-x google-contacts
    ```
-   Будет запрошена учётная запись на google и будет предложено залогиниться.
-   Запрос откроется в _eww_ --- броузере emacs. Через меню откройте этот URL во внешнем броузере.
-   При первом использовании необходимо вставить токен `oauth2` в минибуфер emacs.
-   Затем необходимо ввести кодовую фразу для шифрования токена `oauth2`.
-   Это происходит потому, что _google-contacts_ использует `oauth2.el`, который хранит информацию аутентификации в зашифрованном файле GPG с использованием `plstore.el`.
-   Если вы не хотите вводить пароль при каждом поиске контактов в Google, вам необходимо установить для `plstore-cache-passphrase-for-simric-encryption` значение `t`:
    ```elisp
    (setq plstore-cache-passphrase-for-symmetric-encryption t)
    ```
