---
title: "pass. Хранение ключей gpg"
author: ["Dmitry S. Kulyabov"]
date: 2026-07-27T21:27:00+03:00
lastmod: 2026-07-27T21:47:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "pass-storing-gpg-keys"
---

pass. Хранение ключей gpg

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Для хранения GPG-ключей в pass подход аналогичен SSH (см. [pass. Хранение ключей ssh]({{< relref "2026-07-27--pass-storing-ssh-keys" >}})).
-   Но есть специфика GPG.
-   GPG-ключи обычно привязаны к идентичностям (email, имя) и используются для шифрования, подписи и аутентификации.
-   Хранить их в gopass удобно как резервную копию или для переноса между машинами.
-   Можно хранить только приватные ключи (публичные легко восстановить из приватного), но лучше сохранять оба для удобства.


## <span class="section-num">2</span> Структура хранения {#структура-хранения}

-   Можно группировать ключи по владельцу/идентичности или назначению (например, рабочие и личные):

<!--listend-->

```text
gpg/
├── identities/
│   ├── work@company.com/
│   │   ├── private.asc
│   │   └── public.asc
│   └── personal@gmail.com/
│       ├── private.asc
│       └── public.asc
└── subkeys/
    ├── signing/
    │   ├── private.asc
    │   └── public.asc
    └── encryption/
        ├── private.asc
        └── public.asc
```


## <span class="section-num">3</span> Экспорт GPG-ключей {#экспорт-gpg-ключей}

-   Перед сохранением экспортируйте ключи в текстовый формат (armor), который можно вставить в gopass.


### <span class="section-num">3.1</span> Приватный ключ {#приватный-ключ}

```shell
gpg --export-secret-keys --armor <key-id или email> > ~/private_key.asc
```


### <span class="section-num">3.2</span> Публичный ключ {#публичный-ключ}

```shell
gpg --export --armor <key-id или email> > ~/public_key.asc
```

-   Субключи (если у вас раздельные ключи для подписи и шифрования) экспортируйте отдельно с опцией `--export-options export-minimal` или используйте идентификаторы субключей.


## <span class="section-num">4</span> Сохранение в gopass {#сохранение-в-gopass}

-   Для каждого ключа создайте запись (в редакторе):
    ```shell
    # Приватный ключ
    gopass insert gpg/identities/work@company.com/private.asc
    # Вставьте содержимое private_key.asc (включая -----BEGIN PGP PRIVATE KEY BLOCK----- ...)

    # Публичный ключ
    gopass insert gpg/identities/work@company.com/public.asc
    # Вставьте содержимое public_key.asc
    ```

-   Можно сохранить ключи из командной строки:
    ```shell
    gopass insert -f gpg/identities/work/private.asc < ~/private_key.asc
    gopass insert -f gpg/identities/work/public.asc < ~/public_key.asc
    ```


## <span class="section-num">5</span> Извлечение и импорт ключей {#извлечение-и-импорт-ключей}

-   Когда нужно восстановить ключ на новой машине или временно использовать.


### <span class="section-num">5.1</span> Восстановить в систему {#восстановить-в-систему}

-   Извлеките содержимое и передайте в `gpg --import`:
    ```shell
    gopass show gpg/identities/work@company.com/private.asc | gpg --import
    gopass show gpg/identities/work@company.com/public.asc | gpg --import
    ```


### <span class="section-num">5.2</span> Временное использование без импорта {#временное-использование-без-импорта}

-   GPG не поддерживает прямую работу с ключами из памяти, как ssh-agent.
-   Однако можно сохранить во временный файл и использовать с опцией `--keyring`:

<!--listend-->

```shell
TMP_KEY=$(mktemp)
gopass show gpg/identities/work/private.asc > "$TMP_KEY"
gpg --homedir /tmp/gpg_temp --import "$TMP_KEY"
gpg --homedir /tmp/gpg_temp --list-keys
# ... используйте с --homedir
```


## <span class="section-num">6</span> Управление несколькими GPG-ключами {#управление-несколькими-gpg-ключами}


### <span class="section-num">6.1</span> Выбор ключа по умолчанию {#выбор-ключа-по-умолчанию}

-   В `~/.gnupg/gpg.conf` можно указать `default-key <key-id>`.


### <span class="section-num">6.2</span> Использование разных ключей для разных задач {#использование-разных-ключей-для-разных-задач}

-   Например, один ключ для подписи коммитов в Git, другой для шифрования файлов.
-   Настройте `git config user.signingkey` и `gpg.conf` соответственно.


## <span class="section-num">7</span> Автоматизация импорта всех ключей при входе в систему {#автоматизация-импорта-всех-ключей-при-входе-в-систему}

-   Создайте скрипт `import-gpg-keys.sh`, который будет извлекать все приватные ключи из gopass и импортировать их:

<!--listend-->

```shell
#!/bin/bash
for key in $(gopass list gpg/identities/ | grep '/private.asc$'); do
    echo "Импорт $key"
    gopass show "$key" | gpg --import
done
```

-   Можно добавить его в `.bashrc` или `.profile`.

-   Если ключи в gopass зашифрованы вашим GPG-ключом, то при импорте они будут расшифрованы автоматически


## <span class="section-num">8</span> Пример {#пример}

-   Допустим, у вас есть рабочий ключ `work@company.com` и личный `personal@gmail.com`.

<!--listend-->

```shell
# Экспорт с текущей машины
gpg --export-secret-keys --armor work@company.com > work_private.asc
gpg --export --armor work@company.com > work_public.asc
gpg --export-secret-keys --armor personal@gmail.com > personal_private.asc
gpg --export --armor personal@gmail.com > personal_public.asc

# Сохранение в gopass
gopass insert gpg/identities/work/private.asc < work_private.asc
gopass insert gpg/identities/work/public.asc < work_public.asc
gopass insert gpg/identities/personal/private.asc < personal_private.asc
gopass insert gpg/identities/personal/public.asc < personal_public.asc

# Проверка
gopass show gpg/identities/work/public.asc | head -n 5

# На новой машине
gopass show gpg/identities/work/private.asc | gpg --import
gopass show gpg/identities/personal/private.asc | gpg --import
# Установить доверие
gpg --edit-key work@company.com trust quit
```


## <span class="section-num">9</span> Хранение только приватных ключей {#хранение-только-приватных-ключей}

-   Публичные ключи можно восстановить из приватных командой `gpg --export`, поэтому можно хранить только приватные, а публичные генерировать при необходимости.
