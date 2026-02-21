---
title: "Менеджер паролей pass. Одноразовые пароли"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-24T20:29:00+03:00
lastmod: 2024-12-01T14:41:00+03:00
tags: ["security", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "password-manager-pass-one-time-passwords"
---

Одноразовые пароли в менеджере паролей pass.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   [Одноразовые пароли]({{< relref "2023-08-24-one-time-passwords" >}})


## <span class="section-num">2</span> Формат файла {#формат-файла}

-   Токен можно хранить как в основном файле с паролем, так и в отдельном файле.
-   Хранение в том же файле: `git-passwordstore/website/yourLogin`.
    -   Формат может быть следующий:
        ```yaml
        yourPassword
        ---
        login: yourLogin
        url: https://website.com
        totp: YourOtpTokenBase32Encoded
        ```

        -   Формат `totp:` поддерживается не всеми программами работы с паролями.
    -   Можно хранить и в виде указателя на URL (этот формат является предпочтительным):
        ```yaml
        yourPassword
        ---
        login: yourLogin
        url: https://website.com
        otpauth://totp/Website:yourLogin?secret=YourOtpTokenBase32Encoded&issuer=Website
        ```
-   Хранение в отдельном файле `local-passwordstore/website/yourOtp`.
    -   Только в виде указателя на URL:
        ```yaml
        otpauth://totp/Website:yourLogin?secret=YourOtpTokenBase32Encoded&issuer=Website
        ```
-   Например, URL для github имеет вид:
    ```yaml
    otpauth://totp/GitHub:<username>?secret=<secret>&issuer=GitHub
    ```


## <span class="section-num">3</span> Аппаратный токен {#аппаратный-токен}

-   В идеале секретный ключ, способный расшифровать ваши секреты OTP, должен храниться на аппаратном токене, для расшифровки которого требуется какое-то взаимодействие с пользователем.
-   Это достигается путем настройки второго хранилища без использования тех же открытых ключей, что и для основного хранилища паролей.
-   Открытые ключи, используемые для вашего хранилища OTP, в идеале должны храниться только на аппаратных токенах.


## <span class="section-num">4</span> pass-otp {#pass-otp}

-   Репозиторий: <https://github.com/tadfisher/pass-otp>


## <span class="section-num">5</span> Добавить токен в запись {#добавить-токен-в-запись}

-   Ввести токен с терминала (скрывая ввод):
    ```shell
    pass otp insert totp-secret
    ```
-   Ввести токен с терминала (повторяя ввод):
    ```shell
    pass otp insert -e totp-secret
    ```
-   Направьте otpauth://URI в файл паролей:
    ```shell
    pass otp insert totp-secret < totp-secret.txt
    ```
-   Декодировать QR-изображения (используя `zbar`).
    -   Файл пароля будет заменён или создан:
        ```shell
        zbarimg -q --raw qrcode.png | pass otp insert totp-secret
        ```
    -   Добавление к существующему файлу паролей:
        ```shell
        zbarimg -q --raw google-qrcode.png | pass otp append google/example@gmail.com
        ```
-   Декодировать QR, получаемый из веб-камеры. Файл пароля будет заменён или создан:
    ```shell
    zbarcam -q --raw | pass otp insert totp-secret
    ```
-   Из буфера обмена (для Wayland):
    ```shell
    wl-paste | zbarimg -q --raw - | pass otp append google/example@gmail.com
    ```


## <span class="section-num">6</span> Использование токена {#использование-токена}

-   Сгенерировать код 2FA, используя токен:
    ```shell
    pass otp <totp-secret>
    ```
-   Отобразить QR-код для токена OTP:
    ```shell
    pass otp uri -q <totp-secret>
    ```
