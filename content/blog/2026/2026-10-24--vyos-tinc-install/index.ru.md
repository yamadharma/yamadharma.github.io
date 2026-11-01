---
title: "VyOS. Установка tinc"
author: ["Dmitry S. Kulyabov"]
date: 2026-10-24T19:50:00+03:00
lastmod: 2026-10-25T13:54:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "vyos-tinc-install"
---

VyOS. Установка tinc.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Дополнительное ПО в VyOS {#дополнительное-по-в-vyos}

-   При обновлении через `vyos upgrade`, `add system image` фактически устанавливается новый образ системы.
-   Поэтому пакеты, установленные через `apt`, и файлы в `/usr`, `/usr/local` не переживают обновление.
-   Постоянно сохраняется пользовательский каталог `/config`.
-   Будем ставить в следующую иерархию:
    ```text
    /config/opt/tinc/
    ├── sbin/
    │ ├── tinc
    │ └── tincd
    ├── etc/
    │ └── tinc/
    │ └── /
    ├── systemd/
    │ └── tinc@.service
    └── var/
    ```
-   Пути:
    ```shell
    /config/opt/tinc/
    /config/opt/tinc/sbin/tincd
    /config/opt/tinc/etc/tinc/tinc.conf
    /config/opt/tinc/etc/tinc/hosts/
    /config/opt/tinc/systemd/tinc@.service
    ```


## <span class="section-num">2</span> Скачать пакет {#скачать-пакет}

-   Создадим каталог:

<!--listend-->

```shell
sudo mkdir -p /config/opt/tinc
```

-   Скачаем пакет:
    ```shell
    mkdir /tmp/tinc
    cd /tmp/tinc
    wget https://mirror.yandex.ru/debian/pool/main/t/tinc/tinc_1.1~pre18-1+b1_amd64.deb
    wget https://mirror.yandex.ru/debian/pool/main/m/miniupnpc/libminiupnpc17_2.2.4-1+b1_amd64.deb
    ```
-   Распакуем пакет:
    ```shell
    dpkg --extract tinc_1.1~pre18-1+b1_amd64.deb .
    dpkg --extract libminiupnpc17_2.2.4-1+b1_amd64.deb .
    ```
-   Скопируем файлы:
    ```shell
    sudo cp -R {etc,lib,usr} /config/opt/tinc
    sudo mkdir -p /config/opt/tinc/etc/tinc
    ```


## <span class="section-num">3</span> Создать systemd unit {#создать-systemd-unit}

-   Создадим шаблонный unit `tinc@.service`, чтобы можно было запускать несколько сетей:

<!--listend-->

```sh
sudo mkdir -p /config/opt/tinc/systemd

sudo tee /config/opt/tinc/systemd/tinc@.service >/dev/null <<'EOF'
[Unit]
Description=tinc VPN network %i
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
Environment=PATH=/usr/sbin:/usr/bin:/sbin:/bin
Environment="LD_LIBRARY_PATH=/config/opt/tinc/usr/lib/x86_64-linux-gnu"
ExecStartPre=-/sbin/modprobe tun
ExecStart=/config/opt/tinc/usr/sbin/tincd -n %i -c /config/opt/tinc/etc/tinc/%i -D
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5
SyslogIdentifier=tinc-%i

[Install]
WantedBy=multi-user.target
EOF
```


## <span class="section-num">4</span> Скрипт восстановления {#скрипт-восстановления}

-   Этот скрипт будет копировать unit в `/run/systemd/system` и запускать все найденные сети tinc.

<!--listend-->

```shell
sudo tee /config/scripts/tinc-restore.sh >/dev/null <<'EOF'
#!/bin/sh

TINC=/config/opt/tinc
UNIT_SRC=$TINC/systemd/tinc@.service
UNIT_DST=/run/systemd/system/tinc@.service

[ -x "$TINC/usr/sbin/tincd" ] || exit 0
[ -f "$UNIT_SRC" ] || exit 0

install -d /run/systemd/system
install -m 0644 "$UNIT_SRC" "$UNIT_DST"

systemctl daemon-reload

for d in "$TINC/etc/tinc"/*/; do
    [ -f "${d}tinc.conf" ] || continue
    net=$(basename "$d")
    systemctl --no-block start "tinc@$net" || true
done
EOF

sudo chmod 755 /config/scripts/tinc-restore.sh
```


## <span class="section-num">5</span> Подключить скрипт к загрузке VyOS {#подключить-скрипт-к-загрузке-vyos}

-   В VyOS есть пользовательский скрипт:

<!--listend-->

```shell
/config/scripts/vyos-postconfig-bootup.script
```

-   Он сохраняется в `/config` и переживает обновления.
-   Нужно сделать так, чтобы он вызывал `tinc-restore.sh`.
-   Добавьте в него строку:

<!--listend-->

```shell
/config/scripts/tinc-restore.sh
```


## <span class="section-num">6</span> Сконфигурите сеть {#сконфигурите-сеть}

-   [VPN. Настройка tinc]({{< relref "2026-10-25--vpn-tinc-configure" >}})
-   Для вызова `tinc` используйте (замените $VPNNAME на имя сети):
    ```shell
    /config/opt/tinc/usr/sbin/tinc -c /config/opt/tinc/etc/tinc/$VPNNAME
    ```
-   Для вызова `tincd` используйте:
    ```shell
    LD_LIBRARY_PATH=/config/opt/tinc/usr/lib/x86_64-linux-gnu /config/opt/tinc/usr/sbin/tincd -c /config/opt/tinc/etc/tinc/$VPNNAME -n $VPNNAME -D
    ```


## <span class="section-num">7</span> Проверить запуск вручную {#проверить-запуск-вручную}

-   Запустите скрипт вручную:

<!--listend-->

```shell
sudo /config/scripts/tinc-restore.sh
```

Если у вас есть сеть, например `vpn1`, проверьте:

```shell
systemctl status tinc@vpn1
journalctl -u tinc@vpn1 -n 50 --no-pager
```


## <span class="section-num">8</span> После обновления системы {#после-обновления-системы}

-   После `vyos upgrade` или установки нового образа:
    -   `/config` останется;
    -   `/config/opt/tinc/sbin/tincd` останется;
    -   `/config/scripts/tinc-restore.sh` останется;
    -   при загрузке VyOS выполнит `vyos-postconfig-bootup.script`;
    -   тот восстановит systemd unit и запустит ваши сети.
