---
title: "pass. Хранение ключей ssh"
author: ["Dmitry S. Kulyabov"]
date: 2026-07-27T17:20:00+03:00
lastmod: 2026-07-27T21:29:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "pass-storing-ssh-keys"
---

pass. Хранение ключей ssh.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Хранение SSH-ключей с разной привязкой (к хостам, сервисам, проектам) в pass, gopass.


## <span class="section-num">2</span> Иерархия хранения {#иерархия-хранения}

-   Используем следующие пространства:
    -   `ssh/machines/<hostname>/` : ключи, созданные на конкретном хосте.
        -   Эти ключи обычно используются для аутентификации этой машины на других серверах или сервисах.
    -   `ssh/hosts/` : ключи, привязанные к конкретным хостам.
    -   `ssh/services/` : ключи, относящиеся к конкретным сервисам (git, GitHub, GitLab), которые могут использоваться на разных хостах.
    -   `ssh/default` : ключ по умолчанию (если используется).

-   Пример структуры:

<!--listend-->

```text
ssh/
├── machines/
│   ├── laptop/
│   │   ├── id_ed25519
│   │   └── id_ed25519.pub
│   ├── server-01/
│   │   ├── id_rsa
│   │   └── id_rsa.pub
│   └── desktop/
│       ├── id_ecdsa
│       └── id_ecdsa.pub
├── hosts/
│   ├── prod-web-01/
│   │   ├── id_rsa
│   │   └── id_rsa.pub
│   └── bastion/
│       ├── id_ed25519
│       └── id_ed25519.pub
└── services/
    ├── github/
    │   ├── id_rsa
    │   └── id_rsa.pub
    ├── gitlab/
    │   ├── id_ecdsa
    │   └── id_ecdsa.pub
    └── aws/
        ├── id_rsa
        └── id_rsa.pub
```


## <span class="section-num">3</span> Добавление ключей {#добавление-ключей}

-   Для каждого ключа можно выполнить добавление через редактор:
    ```shell
    # Создать запись для приватного ключа
    gopass insert ssh/machines/laptop/id_rsa
    # Вставить содержимое файла ~/.ssh/id_rsa (включая BEGIN/END)

    # Создать запись для публичного ключа
    gopass insert ssh/machines/laptop/id_rsa.pub
    # Вставить содержимое соответствующего .pub
    ```

-   Можно выполнить копированием из файла напрямую:
    ```shell
    gopass insert -f ssh/machines/laptop/id_ed25519 < ~/.ssh/id_ed25519
    gopass insert -f ssh/machines/laptop/id_ed25519.pub < ~/.ssh/id_ed25519.pub
    ```

    -   Флаг `-f` заставит перезаписать запись, если она уже существует.

-   Аналогично для сервисов:
    ```shell
    gopass insert -f ssh/services/github/id_ed25519 < ~/.ssh/id_ed25519_github
    gopass insert -f ssh/services/github/id_ed25519.pub < ~/.ssh/id_ed25519_github.pub
    ```


## <span class="section-num">4</span> Извлечение ключей {#извлечение-ключей}


### <span class="section-num">4.1</span> Сохранение в файл {#сохранение-в-файл}

-   Можно восстановить SSH-ключи из gopass в каталог `~/.ssh`.
-   Посмотрите список сохранённых ключей:
    ```shell
    gopass list ssh/
    ```

-   Для каждого приватного ключа:
    ```shell
    gopass show ssh/machines/laptop/id_rsa > ~/.ssh/id_rsa
    chmod 600 ~/.ssh/id_rsa
    ```

-   Для каждого публичного ключа:
    ```shell
    gopass show ssh/machines/laptop/id_rsa.pub > ~/.ssh/id_rsa.pub
    chmod 644 ~/.ssh/id_rsa.pub
    ```

<!--listend-->

-   Восстановить сервисные ключи:
    ```shell
    # Восстановить ключ для GitHub
    gopass show ssh/services/github/id_ed25519 > ~/.ssh/id_ed25519_github
    chmod 600 ~/.ssh/id_ed25519_github
    gopass show ssh/services/github/id_ed25519.pub > ~/.ssh/id_ed25519_github.pub
    chmod 644 ~/.ssh/id_ed25519_github.pub
    ```

-   Чтобы восстановить все ключи сразу, можно использовать скрипт:

<!--listend-->

```shell
#!/bin/bash
# restore_all_ssh_keys.sh

SSH_DIR="$HOME/.ssh"
mkdir -p "$SSH_DIR"

# 1. Восстанавливаем ключ текущей машины
HOSTNAME=$(hostname -s)
MACHINE_PATH="ssh/machines/$HOSTNAME"
for key in $(gopass list "$MACHINE_PATH/" | grep -v '\.pub$'); do
    BASENAME=$(basename "$key")
    DEST="$SSH_DIR/$BASENAME"
    echo "Восстановление машины: $key -> $DEST"
    gopass show "$key" > "$DEST"
    chmod 600 "$DEST"
    # публичный
    pub="${key}.pub"
    if gopass show "$pub" &>/dev/null; then
        gopass show "$pub" > "$SSH_DIR/${BASENAME}.pub"
        chmod 644 "$SSH_DIR/${BASENAME}.pub"
    fi
done

# 2. Восстанавливаем все сервисные ключи
SERVICE_PATH="ssh/services"
for key in $(gopass list "$SERVICE_PATH/" | grep -v '\.pub$'); do
    BASENAME=$(basename "$key")
    # Добавляем суффикс сервиса, чтобы не конфликтовать с ключами машин
    SERVICE_NAME=$(echo "$key" | sed -E "s|^$SERVICE_PATH/([^/]+)/.*|\1|")
    DEST="$SSH_DIR/${BASENAME}_${SERVICE_NAME}"
    echo "Восстановление сервиса: $key -> $DEST"
    gopass show "$key" > "$DEST"
    chmod 600 "$DEST"
    # публичный
    pub="${key}.pub"
    if gopass show "$pub" &>/dev/null; then
        gopass show "$pub" > "$SSH_DIR/${BASENAME}_${SERVICE_NAME}.pub"
        chmod 644 "$SSH_DIR/${BASENAME}_${SERVICE_NAME}.pub"
    fi
done

echo "Готово. Ключи восстановлены в $SSH_DIR"
```


### <span class="section-num">4.2</span> Вручную -- для подключения по SSH {#вручную-для-подключения-по-ssh}

-   Если нужно подключиться к хосту, можно временно извлечь ключ в файл:
    ```shell
    gopass show ssh/hosts/prod-web-01/id_rsa > /tmp/prod_rsa
    chmod 600 /tmp/prod_rsa
    ssh -i /tmp/prod_rsa user@prod-web-01
    ```

-   Через `ssh-agent` (см. [Агент для ключей ssh-agent]({{< relref "2024-08-22-ssh-agent" >}})):
    ```shell
    # Добавить ключ в агент, не сохраняя на диск
    gopass show ssh/hosts/prod-web-01/id_rsa | ssh-add -
    # Затем обычный ssh без -i
    ssh user@prod-web-01
    ```


### <span class="section-num">4.3</span> Автоматический выбор ключа через `~/.ssh/config` {#автоматический-выбор-ключа-через-dot-ssh-config}

-   В конфиге SSH можно указать, какой ключ использовать для какого хоста или сервиса.
-   Чтобы не хранить ключи на диске, можно использовать скрипт-обёртку, который извлекает ключ из gopass и передаёт его SSH.
-   Вместо id_rsa можно использовать ключи с другими алгоритмами.

-   Скрипт `/usr/local/bin/ssh-with-gopass`:

<!--listend-->

```shell
#!/bin/bash
# Использование: ssh-with-gopass user@host
HOST=$1
# Извлекаем ключ для этого хоста из gopass (если есть)
KEY=$(gopass show ssh/hosts/$HOST/id_rsa 2>/dev/null)
if [ $? -eq 0 ]; then
    # Передаём ключ через временный файл или напрямую в ssh -i
    echo "$KEY" > /tmp/ssh_key_$$ && chmod 600 /tmp/ssh_key_$$
    ssh -i /tmp/ssh_key_$$ "$@"
    rm -f /tmp/ssh_key_$$
else
    # Если нет ключа для хоста, пробуем ключ по умолчанию
    ssh "$@"
fi
```

-   Можно добавить ключи в агент при старте сессии:
    ```shell
    # Добавить все ключи из gopass (или выборочно) в агент
    for key in $(gopass list ssh/hosts/ | grep -v '.pub$'); do
        gopass show "$key" | ssh-add -
    done
    for key in $(gopass list ssh/services/ | grep -v '.pub$'); do
        gopass show "$key" | ssh-add -
    done
    ```

    -   Эту команду можно поместить в `.bashrc` или `.profile`.
