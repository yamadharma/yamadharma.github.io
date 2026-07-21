---
title: "Технология passkey. Реализация passless"
author: ["Dmitry S. Kulyabov"]
date: 2026-07-04T21:20:00+03:00
lastmod: 2026-07-05T21:36:00+03:00
tags: ["linux", "sysadmin", "security"]
categories: ["computer-science"]
draft: false
slug: "passkey-passless"
---

Технология passkey. Реализация passless.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/pando85/passless>
-   Хранение:
    -   менеджер паролей pass (см. [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}}));
    -   TPM 2.0;
    -   локальный файл.


### <span class="section-num">1.1</span> Функционал {#функционал}

-   Эмулирует виртуальное FIDO2‑устройство (например, YubiKey) через интерфейс `/dev/uhid`.
-   Предоставляет клиентскую утилиту для управления учётными данными (создание, удаление, список).


### <span class="section-num">1.2</span> Режимы {#режимы}

-   Фоновый сервис -- виртуальный токен, доступный броузерам и приложениям через WebAuthn.
-   Командная строка -- управление ключами и PIN-кодом.


## <span class="section-num">2</span> Другие платформы {#другие-платформы}

-   Для Android есть вариант Android Password Store.
-   С поддержкой passless.
-   Репозиторий: <https://github.com/pando85/Android-Password-Store>


## <span class="section-num">3</span> Установка {#установка}


### <span class="section-num">3.1</span> Gentoo {#gentoo}

-   Репозиторий karma (см. [Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
    ```shell
    emerge app-admin/passless
    ```


### <span class="section-num">3.2</span> Arch Linux {#arch-linux}

```shell
yay -S passless
```


## <span class="section-num">4</span> Настройка {#настройка}


### <span class="section-num">4.1</span> Конфигурационный файл {#конфигурационный-файл}

-   Конфигурационный файл по умолчанию: `/etc/passless/config.toml`.
-   Локальная конфигурация для конкретного пользователя: `~/.config/passless/config.toml`.

-   Пример файла конфигурации:
    ```toml
    # Настройки PIN-кода
    [pin]
    # enforcement = "optional" | "required" | "disabled"
    enforcement = "optional"   # "optional" – PIN запрашивается только если задан
    min_length = 4             # минимальная длина PIN
    max_retries = 8            # число попыток ввода до блокировки

    # Бэкенд хранения ключей
    # backend = "soft" | "tpm" | "pass"
    # "soft" – ключи хранятся в зашифрованном файле (пароль от PIN)
    # "tpm" – использует аппаратный TPM 2.0
    # "pass" - использовать pass
    backend = "pass"

    # Путь к хранилищу учётных данных (по умолчанию ~/.local/share/passless/credentials.db)
    # storage_path = "/home/user/.local/share/passless/credentials.db"

    # Настройки логирования
    # log_level = "info"   # info, debug, warn, error
    ```


### <span class="section-num">4.2</span> Модуль ядра {#модуль-ядра}

-   Убедитесь, что модуль ядра `uhid` загружен (если он не в ядре):
    ```shell
    lsmod | grep uhid
    ```

-   Если нет, то загрузите модуль:
    ```shell
    sudo modprobe uhid
    ```


### <span class="section-num">4.3</span> Права пользователя {#права-пользователя}

-   Пользователь должен быть в группе `fido` (для доступа к `/dev/uhid`).
-   Добавьте себя в группу:
    ```shell
    sudo usermod -aG fido $USER
    ```


### <span class="section-num">4.4</span> Настройка службы systemd {#настройка-службы-systemd}

-   Запустите пользовательскую службу:
    ```shell
    systemctl --user enable passless.service
    systemctl --user start passless.service
    ```

-   Проверьте статус:
    ```shell
    systemctl --user status passless.service
    ```

-   Если служба не запускается, посмотрите логи:
    ```shell
    journalctl --user -u passless.service -f
    ```

-   После запуска службы и задания PIN броузеры (Chrome, Firefox, Edge) автоматически увидят виртуальное устройство при попытке зарегистрироваться или войти через WebAuthn.


### <span class="section-num">4.5</span> Переключение между бэкендами {#переключение-между-бэкендами}

-   При смене бекэнда измените параметр `backend` в конфиге и выполните повторную инициализацию.
-   При смене бэкенда старые учётные данные не мигрируют автоматически.


### <span class="section-num">4.6</span> Настройка pin-кода {#настройка-pin-кода}

-   Перед первым использованием нужно задать pin.
-   Сделайте это через клиентскую утилиту:
    ```shell
    passless client pin set <PIN>
    ```

-   Необходимо ввести pin-код (не менее 4 символов по умолчанию).
-   После этого pin будет использоваться для подтверждения операций (если в конфиге `enforcement = "required"` или `"optional"`, но PIN задан).
-   Изменить pin-код:
    ```shell
    passless client pin change <OLD_PIN> <NEW_PIN>
    ```


### <span class="section-num">4.7</span> Проверка работоспособности {#проверка-работоспособности}


#### <span class="section-num">4.7.1</span> Проверить, видит ли система виртуальное устройство {#проверить-видит-ли-система-виртуальное-устройство}

```shell
passless client devices
```

-   Должен вывести список устройств.


#### <span class="section-num">4.7.2</span> Проверить, что устройство распознаётся как FIDO2 {#проверить-что-устройство-распознаётся-как-fido2}

-   Можно использовать броузер или утилиту `fido2-token` (из пакета `sys-auth/libfido2`):
    ```shell
    fido2-token -L
    ```

-   В выводе должно появиться устройство `Virtual FIDO2 Authenticator`.


### <span class="section-num">4.8</span> Управление учётными данными {#управление-учётными-данными}

-   Список всех ключей:
    ```shell
    passless client list
    ```

-   Удалить ключ по ID:
    ```shell
    passless client delete <credential-id>
    ```


### <span class="section-num">4.9</span> Работа с TPM {#работа-с-tpm}

-   Укажите в конфигурационном файле `backend = "tpm"`.
-   Все учётные данные будут защищены аппаратным TPM 2.0, а PIN будет использоваться только для разблокировки доступа к TPM-ключу.

-   Требования:
    -   Наличие TPM 2.0 и включение его в ядре.
    -   Пакет `app-crypt/tpm2-tss` (для Gentoo).

-   После смены бэкенда нужно пересоздать хранилище (оно несовместимо).
-   Сделайте бэкап старых ключей (если есть) и переинициализируйте:

<!--listend-->

```shell
passless
```


### <span class="section-num">4.10</span> Поддержка pass {#поддержка-pass}

-   passless может хранить FIDO2-учётные данные (passkey) непосредственно в хранилище `pass`.
-   Преимущества:
    -   Единое хранилище: пароли и passkey лежат в одном месте.
    -   Шифрование GPG: все данные надёжно зашифрованы вашим GPG-ключом.
    -   Синхронизация через Git: можно синхронизировать passkey между устройствами так же, как и обычные пароли.


#### <span class="section-num">4.10.1</span> Настройка бэкенда `pass` в passless {#настройка-бэкенда-pass-в-passless}

-   Сгенерируйте файл конфигурации:
    ```shell
    mkdir -p ~/.config/passless
    passless config print > ~/.config/passless/config.toml
    ```

-   Отредактируйте файл `~/.config/passless/config.toml` и укажите бэкенд `pass`:
    ```toml
    # --- Выбор бэкенда хранилища ---
    # backend = "soft"       # по умолчанию — локальный файл (не рекомендуется)
    backend = "pass"         # использовать pass (рекомендуется)

    # --- Настройки PIN-кода (остаются без изменений) ---
    [pin]
    enforcement = "optional"
    min_length = 4
    max_retries = 8
    ```

-   passless будет искать хранилище `pass` в стандартном месте (`~/.password-store`).
-   Если оно расположено в другом каталоге, укажите путь через переменную окружения `PASSWORD_STORE_DIR` или в файле конфигурации.
-   Если ваше хранилище `pass` находится не в `~/.password-store`, укажите путь в файле конфигурации:
    ```toml
    backend = "pass"

    [pass]
    path = "/путь/к/вашему/.password-store"
    ```


#### <span class="section-num">4.10.2</span> Инициализация хранилища passless {#инициализация-хранилища-passless}

-   После смены бэкенда на `pass` необходимо инициализировать хранилище.
-   Если у вас уже были созданы учётные данные с другим бэкендом (`soft`), они не будут перенесены автоматически.
-   Рекомендуется сделать бэкап или начать с чистого состояния.
-   Инициализация хранилища passless:
    ```shell
    passless
    ```


#### <span class="section-num">4.10.3</span> Проверка работы {#проверка-работы}

-   Посмотрите список учётных данных (пока пустой):
    ```shell
    passless client list
    ```


#### <span class="section-num">4.10.4</span> Синхронизация между устройствами {#синхронизация-между-устройствами}

-   Благодаря использованию `pass` и Git вы можете синхронизировать свои FIDO2-ключи между компьютерами.
-   Настройте синхронизацию хранилища `pass` через git.
-   На втором устройстве установите `passless`, настройте конфиг на бэкенд `pass` и выполните `passless init`.
-   passless автоматически подхватит все существующие учётные данные из синхронизированного хранилища.
