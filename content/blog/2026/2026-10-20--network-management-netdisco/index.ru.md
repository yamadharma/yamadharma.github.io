---
title: "Управление сетью. Netdisco"
author: ["Dmitry S. Kulyabov"]
date: 2026-10-20T21:05:00+03:00
lastmod: 2026-10-21T21:12:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "network-management-netdisco"
---

Управление сетью. Netdisco.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://netdisco.org/>
-   Репозиторий: <https://github.com/netdisco/netdisco>
-   Wiki: <https://github.com/netdisco/netdisco/wiki>
-   Docker: <https://hub.docker.com/r/netdisco/netdisco>
-   Netdisco --- это веб-инструмент с открытым исходным кодом для управления сетью.
-   В первую очередь предназначен для автоматического обнаружения устройств, документирования и инвентаризации, особенно на Layer 2 (L2).
-   Собирает данные через SNMP (а также CDP/LLDP) в базу PostgreSQL.
-   Позволяя точно определить, какое устройство находится на каком порту коммутатора.
-   Распространяется по лицензии BSD.


### <span class="section-num">1.1</span> Преимущества Netdisco {#преимущества-netdisco}

-   Отличное обнаружение L2 и видимость портов.
    -   Netdisco точно определяет местоположение конечного устройства по MAC- или IP-адресу и показывает конкретный коммутатор и порт.
    -   Также хорошо подходит для аудита использования портов.
-   Автоматическое построение топологии.
    -   Автоматически строит физическую карту соединений между коммутаторами.
-   Умеет выявлять несоответствия дуплекса (duplex mismatches) и обнаруживать несанкционированные беспроводные точки доступа.
-   Можно вести инвентаризацию оборудования по модели, вендору и версии ПО, а также сохранять историю IP-адресов и местоположений устройств.


### <span class="section-num">1.2</span> Недостатки Netdisco {#недостатки-netdisco}

-   Сложная установка и настройка.
-   Крутая кривая обучения.
-   Ограниченная поддержка не-SNMP устройств.
-   Не предназначен для мониторинга в реальном времени.
-   Ограниченный охват (только L1/L2).


### <span class="section-num">1.3</span> Сравнение с LibreNMS {#сравнение-с-librenms}

-   [Система мониторинга LibreNMS]({{< relref "2023-03-20-librenms-monitoring-system" >}})

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Сравнение Netdisco и Librenms
</div>

| Аспект      | Netdisco                                         | **LibreNMS**                       |
|-------------|--------------------------------------------------|------------------------------------|
| Роль        | Инвентаризация и топология Layer 2 (L2)          | Мониторинг сети                    |
| Фокус       | Соединения и физическое местоположение устройств | Сбор метрик и оповещения           |
| Обнаружение | SNMP, CDP, LLDP, ARP                             | SNMP, CDP, LLDP, OSPF, BGP, агенты |


## <span class="section-num">2</span> Установка Netdisco через docker {#установка-netdisco-через-docker}

Вот пошаговая инструкция, основанная на официальной документации с Docker Hub.


### <span class="section-num">2.1</span> Подготовка директорий и прав доступа {#подготовка-директорий-и-прав-доступа}

-   Создать рабочие каталоги:
    ```shell
    mkdir -p /opt/netdisco
    cd /opt/netdisco
    mkdir -p netdisco/{logs,config,nd-site-local}
    ```

-   Netdisco в контейнере работает от имени пользователя с UID `901`, поэтому ему нужны соответствующие права на запись в директории, которые вы будете монтировать.

<!--listend-->

```shell
sudo groupadd netdisco -g 901
sudo useradd -r -u 901 -g netdisco -s /sbin/nologin netdisco
sudo chown -R netdisco:netdisco /opt/netdisco
```


### <span class="section-num">2.2</span> Загрузка и запуск через Docker Compose {#загрузка-и-запуск-через-docker-compose}

-   Netdisco распространяется с готовым файлом `compose.yaml`, который описывает все необходимые сервисы (базу данных PostgreSQL, бэкенд-демон и веб-интерфейс).

-   Скачайте официальный compose-файл:
    ```shell
    cd /opt/
    curl -Ls -o compose.yaml https://raw.githubusercontent.com/netdisco/netdisco-docker/master/docker-compose.yml
    ```

-   Запустите контейнеры:
    ```sh
    cd /opt/
    docker compose up --detach
    ```

-   Ключ `--detach` (или `-d`) запустит все сервисы в фоновом режиме.
-   После выполнения этой команды Docker скачает необходимые образы (`netdisco/netdisco`, `postgres` и др.) и запустит их.


### <span class="section-num">2.3</span> Брандмауэр {#брандмауэр}

-   Откройте порт 5000 в `firewalld`:
    ```shell
    sudo firewall-cmd --permanent --add-port=5000/tcp
    sudo firewall-cmd --reload
    ```


### <span class="section-num">2.4</span> Первичная настройка {#первичная-настройка}

-   Доступ к веб-интерфейсу
    -   Netdisco будет доступен по адресу `http://<IP-адрес-вашего-сервера>:5000`.
    -   Порт `5000` используется по умолчанию.
-   Изначально веб-интерфейс открыт без аутентификации и с полными правами администратора.
-   Следует включить аутентификацию:
    -   Войдите в веб-интерфейс.
    -   Перейдите в меню `Admin -> User Management`.
        -   Создайте пользователя.
    -   В файле `netdisco/config/deployment.yml` установите параметр `no_auth: false`.
    -   Перегрузите контейнеры:
        ```shell
        docker compose restart
        ```


### <span class="section-num">2.5</span> Настройка {#настройка}


#### <span class="section-num">2.5.1</span> Привязка к хостовому адресу {#привязка-к-хостовому-адресу}

-   В стандартной конфигурации Docker (bridge network) контейнер `netdisco-backend` имеет собственный внутренний IP-адрес.
-   Когда он отправляет SNMP-запрос на ваш коммутатор, этот запрос проходит через механизм NAT (MASQUERADE).
-   Netdisco не имеет встроенной опции для принудительного выбора исходного IP-адреса для SNMP-запросов.
-   Чтобы Netdisco гарантированно использовал IP-адрес сервера для всех SNMP-запросов, самый простой путь --- перевести контейнеры Netdisco в сетевой режим `host`.
-   В этом режиме контейнер не получает изолированную сеть, а использует сетевой стек хоста напрямую.
-   Все SNMP-пакеты будут уходить с IP-адреса хоста и с тех же интерфейсов.
-   В файле `compose.yaml`:
    ```yaml
    services:
      netdisco-backend:
        # ...
        network_mode: "host"
    ```


#### <span class="section-num">2.5.2</span> SNMP community {#snmp-community}

-   Основной файл конфигурации находится по пути `netdisco/config/deployment.yml` внутри папки `/opt/netdisco`.
-   В этом файле вы можете определить списки community strings для чтения и записи.
-   Netdisco будет пробовать их по очереди, пока не найдёт рабочую, а затем закэширует её в базе данных.
-   Пример конфигурации:

<!--listend-->

```yaml
device_auth:
  - tag: 'default_v2_readonly'
    community: 'public'
    read: true
    write: false
```

-   `device_auth:`  : список правил аутентификации для опроса устройств.
-   `- tag: 'default_v2_readonly'` : метка для правила, используется только для идентификации в конфигурации и логах.
-   `community: 'public'` : SNMP-сообщество, которое Netdisco будет использовать для доступа к устройствам.
-   `read: true` : разрешает использовать это правило для операций чтения (сбор данных).
-   `write: false` : запрещает использование для операций записи (изменение настроек).


#### <span class="section-num">2.5.3</span> Сети для обнаружения {#сети-для-обнаружения}

-   Используется механизм Access Control Lists (ACL), который позволяет гибко включать (`discover_only`) или исключать (`discover_no`) целые подсети или отдельные IP-адреса из процесса обнаружения.
-   Настроить это можно в файле `deployment.yml`.

<!--list-separator-->

1.  `discover_only` (Белый список)

    -   Этот параметр указывает Netdisco, что обнаруживать нужно только устройства из перечисленных сетей.
    -   Все остальные IP-адреса будут проигнорированы.

    -   Пример в `deployment.yml`:
        ```yaml
        # Обнаруживать устройства только в этих подсетях
        discover_only:
        ​  - 192.168.1.0/24
        ​  - 10.0.0.0/24
        ​  - '2001:db8::/32' # Пример для IPv6
        ```

<!--list-separator-->

2.  `discover_no` (Чёрный список)

    -   Этот параметр используется для исключения определённых сетей или адресов из процесса обнаружения.
    -   Это удобно, если вы хотите сканировать большую сеть, но пропустить, например, сеть с принтерами или гостевой Wi-Fi.

    -   Пример в `deployment.yml`:

    <!--listend-->

    ```yaml
    # Исключить эти подсети из обнаружения
    discover_no:
      - 192.168.0.0/16
      - 172.16.0.0/12
    ```

    -   Эти два параметра можно комбинировать.
    -   Если сеть указана и в `discover_only`, и в `discover_no`, она не будет сканироваться.


#### <span class="section-num">2.5.4</span> Регулярное сканирование {#регулярное-сканирование}

-   Регулярное сканирование настраивается через встроенный планировщик.
-   Netdisco выполняет базовое ежедневное обновление без какой-либо дополнительной настройки.
-   Автоматически запускается задача `discoverall` (обнаружение всех известных устройств) один раз в сутки, чтобы поддерживать систему в актуальном состоянии.
-   Можно переопределить настройки по умолчанию в файле `deployment.yml`.
-   Планировщик управляется секцией `schedule`.
-   Для каждой задачи указывается своё правило `when` в формате cron (5 полей: минуты, часы, день месяца, месяц, день недели).
    ```yaml
    schedule:
      discoverall:
        when: '5 2 * * *'   # Запускать discoverall каждый день в 02:05
      arpwalk:
        when: '20 * * * *'  # Запускать сбор ARP-таблиц каждый час в :20
      macwalk:
        when: '50 * * * *'  # Запускать сбор MAC-таблиц каждый час в :50
    ```


#### <span class="section-num">2.5.5</span> Использование https {#использование-https}

-   Официально рекомендованный способ --- разместить Netdisco за обратным прокси-сервером.
-   Пользователь открывает в браузере `https://netdisco.example.com`.
-   Обратный прокси (Nginx или Apache) принимает HTTPS-запрос, расшифровывает его с помощью SSL-сертификата и перенаправляет уже расшифрованный HTTP-трафик на Netdisco, который работает локально (обычно на порту 5000).
-   Netdisco отвечает прокси, а тот, в свою очередь, отправляет ответ пользователю обратно по HTTPS.

<!--list-separator-->

1.  Nginx

    ```nginx
    server {
        listen 80;
        server_name netdisco.example.com;
        # Перенаправляем весь HTTP-трафик на HTTPS
        return 301 https://$host$request_uri;
    }

    server {
        listen 443 ssl;
        server_name netdisco.example.com;

        # Укажите пути к вашим SSL-сертификатам
        ssl_certificate /etc/ssl/certs/netdisco.example.com.crt;
        ssl_certificate_key /etc/ssl/private/netdisco.example.com.key;

        location / {
            # Передаем запросы на локальный Netdisco
            proxy_pass http://127.0.0.1:5000;

            # Важно, чтобы Netdisco знал, что запрос пришел по HTTPS
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```

<!--list-separator-->

2.  Apache

    ```apache
    <VirtualHost *:80>
        ServerName netdisco.example.com
        # Перенаправляем весь HTTP-трафик на HTTPS
        Redirect permanent / https://netdisco.example.com/
    </VirtualHost>

    <VirtualHost *:443>
        ServerName netdisco.example.com

        SSLEngine on
        # Укажите пути к вашим SSL-сертификатам
        SSLCertificateFile /etc/httpd/ssl/netdisco.pem
        SSLCertificateKeyFile /etc/httpd/ssl/netdisco.key

        ProxyPreserveHost On
        ProxyPass / http://127.0.0.1:5000/ retry=0 timeout=60
        ProxyPassReverse / http://127.0.0.1:5000/
        ProxyRequests Off

        <Proxy *>
            Order allow,deny
            Allow from all
        </Proxy>
    </VirtualHost>
    ```

    -   Для работы этой конфигурации в Apache должны быть включены модули `headers`, `proxy` и `proxy_http`.

<!--list-separator-->

3.  Настройка Netdisco

    -   Netdisco нужно явно указать, что сессионные cookie должны быть защищёнными.
    -   В файле конфигурации Netdisco (`deployment.yml`) раскомментируйте или добавьте следующую строку:
        ```yaml
        session_secure: true
        ```


### <span class="section-num">2.6</span> Ручной опрос устройств {#ручной-опрос-устройств}

-   Можно использовать для отладки.
-   Запускать в каталоге, где находится `compose.yaml`.
-   Опрос устройства из командной строки в Netdisco выполняется с помощью утилиты `netdisco-do`.

-   Опрос устройства.
    ```shell
    docker compose exec netdisco-backend netdisco-do discover -d <IP-адрес-устройства>
    ```

-   Можно опросить несколько устройств сразу, указав несколько флагов `-d`:
    ```shell
    docker compose exec netdisco-backend netdisco-do discover -d 192.168.1.1 -d 192.168.1.2
    ```

-   Можно указать целую подсеть для немедленного обнаружения (эта команда поставит в очередь задание на обнаружение всех адресов в указанной подсети):
    ```shell
    docker compose exec netdisco-backend netdisco-do discover --enqueue -d 192.168.1.0/24
    ```

-   Для отладки используется флаг `-D` (можно несколько раз для большей детализации, например `-DDDD`):
    ```shell
    docker compose exec netdisco-backend netdisco-do discover -D -d 192.168.1.1
    ```

<!--listend-->

-   Запрос у устройства его `sysObjectID` (уникальный идентификатор вендора и модели):
    ```shell
    docker compose exec netdisco-backend netdisco-do show -d 192.168.1.1 -e id
    ```

-   Проверить соседние устройства (`show -e c_id`). Если Netdisco не видит связей между коммутаторами, проверьте, получает ли он информацию о соседях через CDP/LLDP:
    ```shell
    docker compose exec netdisco-backend netdisco-do show -d 192.168.1.1 -e c_id
    ```


### <span class="section-num">2.7</span> Обновление Netdisco {#обновление-netdisco}

-   Процесс обновления также выполняется через Docker Compose:
    ```shell
    # Остановить текущие контейнеры
    docker compose down

    # Загрузить свежий compose-файл
    curl -Ls --clobber -o compose.yaml https://raw.githubusercontent.com/netdisco/netdisco-docker/master/docker-compose.yml

    # Загрузить новые образы
    docker compose pull

    # Запустить обновленные контейнеры с профилем для обновления БД
    docker compose --profile with-pg-upgrade up --remove-orphans --force-recreate --detach
    ```

-   Флаг `--profile with-pg-upgrade` гарантирует, что схема базы данных PostgreSQL также будет корректно обновлена.
