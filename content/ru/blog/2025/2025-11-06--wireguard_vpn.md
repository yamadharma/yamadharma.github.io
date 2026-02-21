---
title: "WireGuard VPN"
author: ["Dmitry S. Kulyabov"]
date: 2025-11-06T08:53:00+03:00
lastmod: 2025-11-19T19:32:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "wireguard-vpn"
---

WireGuard VPN.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   WireGuard есть коммуникационный протокол и бесплатное программное обеспечение с открытым исходным кодом, которое реализует зашифрованные виртуальные частные сети (VPN).


### <span class="section-num">1.1</span> Основные особенности WireGuard {#основные-особенности-wireguard}

-   Минималистичный дизайн.
-   Высокая производительность.
-   Простота конфигурации.
-   Криптографические примитивы:
    -   Curve25519 --- для обмена ключами;
    -   ChaCha20 --- для шифрования данных;
    -   Poly1305 --- для проверки целостности сообщений;
    -   BLAKE2s --- для высокоскоростного хэширования;
    -   HKDF --- для безопасной генерации ключей.
-   Кроссплатформенность.
-   Несколько топологий. Поддерживает топологии «точка-точка», «звезда» (сервер/клиент) и Mesh (сеть).


### <span class="section-num">1.2</span> Применение WireGuard {#применение-wireguard}

-   Защита трафика в корпоративных сетях.
-   Создание безопасного доступа к облачным и локальным ресурсам.
-   Шифрование данных в публичных Wi-Fi сетях.
-   Настройка протокола на домашних роутерах для защиты всей сети.


### <span class="section-num">1.3</span> Ограничения WireGuard {#ограничения-wireguard}

-   Привязка к статическим IP:
    -   каждый клиент должен быть настроен с фиксированным IP, что может быть неудобно в динамических сетях.
-   Ограниченная анонимность
    -   протокол не скрывает метаданные, такие как IP-адреса.
-   Отсутствие встроенной обфускации
    -   WireGuard не скрывает трафик от анализа.


## <span class="section-num">2</span> Пояснение настроек {#пояснение-настроек}


### <span class="section-num">2.1</span> Сервер и клиент {#сервер-и-клиент}

-   После установления соединения серверная и клиентская части WireGuard имеют абсолютно одинаковую функциональность.
-   Обычно ожидается, что серверная часть всегда запущена и имеет публичный IP-адрес, но это всего лишь для удобства.


### <span class="section-num">2.2</span> AllowedIPs {#allowedips}

-   Директива `AllowedIPs`  в WireGuard --- это параметр конфигурации, который определяет, какие IP-адреса могут проходить через туннель WireGuard.
-   Она указывает, какой трафик будет разрешён для передачи через VPN-соединение, и играет ключевую роль в настройке маршрутизации и безопасности.


#### <span class="section-num">2.2.1</span> Основные функции AllowedIPs {#основные-функции-allowedips}

-   Определение разрешённого трафика.
    -   С помощью AllowedIPs указывается, какие IP-адреса (или диапазоны адресов) могут быть получены или отправлены через конкретный интерфейс WireGuard.
    -   Это позволяет контролировать, какой трафик будет проходить через туннель.

-   Настройка маршрутизации.
    -   Система будет направлять трафик для указанных IP-адресов через интерфейс WireGuard.

-   Обеспечение безопасности.
    -   Ограничение трафика помогает предотвратить несанкционированный доступ и утечки данных.


#### <span class="section-num">2.2.2</span> Как работает AllowedIPs {#как-работает-allowedips}

-   В конфигурационном файле WireGuard для каждого пира (peer) можно указать список IP-адресов или подсетей, которые будут разрешены для этого пира.

-   Формат указания адресов: стандартный для IP-сетей, включая CIDR-нотацию (например, 192.168.1.0/24 для подсети).

-   Можно указывать как отдельные IP-адреса, так и диапазоны.


#### <span class="section-num">2.2.3</span> Примеры использования AllowedIPs {#примеры-использования-allowedips}

-   `AllowedIPs = 0.0.0.0/0` : весь трафик будет направляться через туннель WireGuard (полная маршрутизация через VPN).

-   `AllowedIPs = 192.168.1.0/24` : через туннель будут проходить только адреса из указанной подсети.

-   `AllowedIPs = 10.0.0.5/32` : разрешение трафика только для конкретного IP-адреса 10.0.0.5.

-   Если в `AllowedIPs` указаны узкие диапазоны или конкретные адреса, то трафик для остальных адресов будет идти через обычный сетевой интерфейс, а не через VPN.

-   Настройка `AllowedIPs` влияет на то, как система будет маршрутизировать трафик, поэтому важно правильно указать адреса, чтобы обеспечить нужную функциональность и безопасность.

-   При настройке `AllowedIPs` необходимо учитывать как локальные сети, так и публичные IP-адреса, если требуется доступ к определённым ресурсам в интернете через VPN.
-


### <span class="section-num">2.3</span> Настройка маршрутизации {#настройка-маршрутизации}

-   Чтобы добавить маршрутизацию в WireGuard, настройте `AllowedIPs` в конфигурации удаленного узла, что указывает ядру, как маршрутизировать трафик для этого узла.
-   Для более сложной маршрутизации может потребоваться вручную настроить статические маршруты.
-   `AllowedIPs` определяет, какие IP-адреса передаются через туннель WireGuard.
-   В системе Linux `wg-quick` автоматически преобразует `AllowedIP` в маршруты ядра при создании туннеля.
-   Для расширенной маршрутизации используйте `ip-rules`:
    -   Создайте новую таблицу маршрутизации с помощью команды `ip route add table 100`.
    -   Добавьте правило для использования этой таблицы для трафика, исходящего с IP-адреса интерфейса WireGuard: `ip rule add from 10.66.127.142/32 lookup 40`.
    -   Добавьте это правило в команду `PostUp` в конфигурации WireGuard, чтобы автоматизировать её.


## <span class="section-num">3</span> Сервер {#сервер}


### <span class="section-num">3.1</span> **Установка WireGuard** {#установка-wireguard}


#### <span class="section-num">3.1.1</span> Rocky Linux 9 {#rocky-linux-9}

-   Установим репозиторий EPEL:

<!--listend-->

```shell
sudo dnf install epel-release -y
```

-   Установим пакет `wireguard-tools`:

<!--listend-->

```shell
sudo dnf install wireguard-tools -y
```

-   Проверка установки:

<!--listend-->

```shell
wg --version
```


### <span class="section-num">3.2</span> Настройка WireGuard {#настройка-wireguard}

-   WireGuard использует криптографические ключи для аутентификации и шифрования трафика между узлами.


#### <span class="section-num">3.2.1</span> Генерация ключей сервера {#генерация-ключей-сервера}

-   Создадим директорию для хранения ключей и сгенерируем пару ключей:

<!--listend-->

```shell
sudo mkdir -p /etc/wireguard
sudo chmod 700 /etc/wireguard
sudo wg genkey | sudo tee /etc/wireguard/server_private.key
sudo wg pubkey < /etc/wireguard/server_private.key | sudo tee /etc/wireguard/server_public.key
sudo chmod 600 /etc/wireguard/server_private.key /etc/wireguard/server_public.key
```


#### <span class="section-num">3.2.2</span> Создание конфигурационного файла сервера {#создание-конфигурационного-файла-сервера}

-   Создадим файл конфигурации `wg0.conf`:

<!--listend-->

```shell
sudo touch /etc/wireguard/wg0.conf
```

-   Добавьте в него следующие строки, заменив на ваш приватный ключ:

<!--listend-->

```conf-unix
[Interface]
Address = 10.0.0.1/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <Server_Private_Key>
```

-   Приведенная выше конфигурация WireGuard создает новый интерфейс с частным IP-адресом. `10.0.0.1/24`:
    -   `Address = 10.0.0.1/24` : назначает частный IP-адрес `10.0.0.1` интерфейсу WireGuard с маской подсети `255.255.255.0` .
    -   `SaveConfig = true` : позволяет WireGuard автоматически сохранять конфигурацию при выключении сервера.
    -   `PrivateKey = <Server_Private_Key>` : устанавливает закрытый ключ сервера WireGuard.
    -   `ListenPort = 51820`: устанавливает порт сервера WireGuard `51820` для прослушивания входящих запросов на VPN-подключение.


#### <span class="section-num">3.2.3</span> Генерация конфигурации клиента {#генерация-конфигурации-клиента}

-   Замените `client` желаемой схемой именования клиентов.
-   Сгенерируем пару ключей для клиента:

<!--listend-->

```shell
sudo wg genkey | sudo tee /etc/wireguard/client_private.key
sudo wg pubkey < /etc/wireguard/client_private.key | sudo tee /etc/wireguard/client_public.key
```


#### <span class="section-num">3.2.4</span> Создание конфигурационного файла клиента {#создание-конфигурационного-файла-клиента}

-   Создайте файл `client.conf`:

<!--listend-->

```shell
sudo touch /etc/wireguard/client.conf
```

-   Добавьте следующие строки, заменив соответствующие значения вашими ключами и IP-адресом сервера:

<!--listend-->

```conf-unix
[Interface]
PrivateKey = <Client_Private_Key>
Address = 10.0.0.2/24
DNS = 8.8.8.8

[Peer]
PublicKey = <Server_Public_Key>
Endpoint = <Server_Public_IP>:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

-   Создаётся клиент WireGuard с IP-адресом частного туннеля VPN `10.0.0.2/24`:
    -   `PrivateKey` : устанавливает закрытый ключ клиента WireGuard, используемый для шифрования и аутентификации в туннеле VPN.
    -   `Address` : устанавливает частный IP-адрес клиента WireGuard `10.0.0.2/24`.
    -   `DNS`: устанавливает публичный DNS-сервер Google `8.8.8.8` в качестве DNS-резолвера для разрешения доменных имен при подключении к VPN-туннелю.
    -   `PublicKey` : устанавливает открытый ключ целевого сервера WireGuard.
    -   `AllowedIPs` : определяет сетевые адреса клиентов сети, которым разрешено подключение через туннель VPN.
    -   `Endpoint`: устанавливает публичный IP-адрес сервера WireGuard и порт `51820` для использования при подключении к VPN-туннелю.
    -   `PersistentKeepalive` : поддерживает VPN-соединение активным, отправляя пакеты поддержки активности каждые `15` секунд.


#### <span class="section-num">3.2.5</span> Добавление клиента на сервер {#добавление-клиента-на-сервер}

-   Откройте конфигурационный файл сервера `/etc/wireguard/wg0.conf`.

-   Добавьте информацию о клиенте:

<!--listend-->

```conf-unix
[Peer]
PublicKey = <Client_Public_Key>
AllowedIPs = 10.0.0.2/32
```


#### <span class="section-num">3.2.6</span> Управление сервисом WireGuard {#управление-сервисом-wireguard}

-   Запустите интерфейс WireGuard:

<!--listend-->

```shell
sudo systemctl enable --now wg-quick@wg0
```

-   Убедитесь, что сервис работает корректно:

<!--listend-->

```shell
sudo systemctl status wg-quick@wg0
```


#### <span class="section-num">3.2.7</span> Настройка брандмауэра {#настройка-брандмауэра}

<!--list-separator-->

1.  Открытие порта

    -   Откройте порт 51820/UDP в FirewallD:

    <!--listend-->

    ```shell
    sudo firewall-cmd --add-service=wireguard --permanent
    sudo firewall-cmd --reload
    ```

    -   Разрешите пересылку пакетов для обеспечения работы VPN:

    <!--listend-->

    ```shell
    sudo echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.conf
    sudo sysctl -p
    ```


#### <span class="section-num">3.2.8</span> Маскарадинг {#маскарадинг}

-   Если необходимо подключить маскарадинг.
-   Добавьте правило маскарадинга для сети WireGuard:

<!--listend-->

```shell
sudo firewall-cmd --permanent --add-masquerade
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.0.0.0/24" masquerade'
sudo firewall-cmd --reload
```


## <span class="section-num">4</span> Клиент {#клиент}


### <span class="section-num">4.1</span> Установка {#установка}


#### <span class="section-num">4.1.1</span> Gentoo {#gentoo}

-   Установите:
    ```shell
    emerge net-vpn/wireguard-tools
    ```


#### <span class="section-num">4.1.2</span> Rocky Linux 9 {#rocky-linux-9}

-   Установим репозиторий EPEL:

<!--listend-->

```shell
sudo dnf install epel-release -y
```

-   Установим пакет `wireguard-tools`:

<!--listend-->

```shell
sudo dnf install wireguard-tools -y
```

-   Проверка установки:

<!--listend-->

```shell
wg --version
```


### <span class="section-num">4.2</span> Модуль ядра {#модуль-ядра}

-   Включите модуль в ядро:
    ```text
    Device Drivers  --->
      [*] Network device support  --->
          [*] Network core driver support
          <*>   WireGuard secure network tunnel
    ```
-   Кроме того, должны быть включены следующие параметры:
    ```conf-unix
    CONFIG_IP_MULTIPLE_TABLES=y
    ```
-   Это в конфигураторе:
    ```text
    -> Networking support (NET [=y])
       -> Networking options
          -> TCP/IP networking (INET [=y])
             -> IP: advanced router (IP_ADVANCED_ROUTER [=y])
                -> IP: policy routing (IP_MULTIPLE_TABLES [=y])
    ```
-   Для ipv6 нужно будет установить:
    ```conf-unix
    CONFIG_IPV6_MULTIPLE_TABLES=1
    ```


### <span class="section-num">4.3</span> Конфигурация {#конфигурация}

-   Скопируйте конфигурацию клиента с сервера, например с помощью `scp`:
    ```shell
    sudo scp root@wireguard-server-ip:/etc/wireguard/client.conf /etc/wireguard/wg0.conf
    sudo chmod 600 /etc/wireguard/wg0.conf
    ```
-   Активируйте сервис `systemd-resolved`:
    ```shell
    sudo systemctl enable --now systemd-resolved
    ```
-   Активируйте интерфейс:
    ```shell
    sudo wg-quick up wg0
    ```
-   Проверьте статус туннеля:
    ```shell
    sudo wg
    ```
-   Проверьте связь с сервером:
    ```shell
    ping -c 5 10.0.0.1
    ```


## <span class="section-num">5</span> Утилиты {#утилиты}


### <span class="section-num">5.1</span> wghttp {#wghttp}

-   Репозиторий: <https://github.com/zhsj/wghttp>
-   Использовать WireGuard в качестве прокси-сервера HTTP и SOCKS5.
