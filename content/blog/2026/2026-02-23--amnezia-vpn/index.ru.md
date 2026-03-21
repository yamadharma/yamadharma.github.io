---
title: "VPN. Реализация Amnezia VPN"
author: ["Dmitry S. Kulyabov"]
date: 2026-02-23T18:33:00+03:00
lastmod: 2026-03-19T12:03:00+03:00
draft: false
slug: "amnezia-vpn"
---

VPN. Реализация Amnezia VPN.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/amnezia-vpn/amnezia-client>
-   Amnezia VPN есть VPN-клиент с открытым исходным кодом.
-   Позволяет подключаться к готовым VPN-сервисам.
-   Позволяет собственный приватный VPN-сервер (Self-hosted VPN).


### <span class="section-num">1.1</span> Особенности {#особенности}

-   Self-hosted VPN
    -   Не только клиентская часть, но и серверная часть.

-   Мультипротокольность
    -   Поддерживается широкий спектр VPN-протоколов.
    -   Используются протоколы с маскировкой трафика.
    -   Классические протоколы: OpenVPN, WireGuard, IKEv2.
    -   Протоколы с маскировкой (обфускацией): Shadowsocks, OpenVPN поверх Cloak, XRay (с протоколом REALITY), собственный протокол AmneziaWG.

-   Открытый исходный код


### <span class="section-num">1.2</span> Как работает маскировка трафика (обфускация) {#как-работает-маскировка-трафика--обфускация}

-   AmneziaWG (Улучшенный WireGuard)
    -   форк популярного протокола WireGuard;
    -   изменяются статические параметры пакетов;
    -   добавляются мусорные пакеты в начале сессии.
-   OpenVPN over Cloak
    -   комбинация OpenVPN и плагина Cloak;
    -   Cloak маскирует VPN-трафик под обычный веб-трафик;
    -   если подключение проверяется (активное зондирование), Cloak перенаправляет проверяющего на фейковый сайт, скрывая сам факт работы VPN.
-   XRay (с протоколом REALITY)
    -   маскирует VPN-трафик под обычный веб-трафик.


### <span class="section-num">1.3</span> Варианты использования {#варианты-использования}

-   Клиент AmneziaVPN --- бесплатное приложение:
    -   создание своего сервера;
    -   подключение по готовым конфигурациям.

-   Сервисы от Amnezia ---опциональные платные и бесплатные предложения для тех, кто не хочет самостоятельно арендовать и настраивать сервер:
    -   Amnezia Free: бесплатный VPN для доступа к социально значимым ресурсам;
    -   Amnezia Premium: платная подписка;
    -   торрент-трафик ограничен на всех локациях, кроме Швейцарии.


### <span class="section-num">1.4</span> Протоколы Amnezia {#протоколы-amnezia}

| Протокол        | Тип           | Уровень маскировки | Производительность | Сложность обнаружения DPI |
|-----------------|---------------|--------------------|--------------------|---------------------------|
| WireGuard       | Классический  | Низкая             | Очень высокая      | Легко обнаруживается      |
| OpenVPN         | Классический  | Низкая             | Средняя            | Легко обнаруживается      |
| AmneziaWG       | С маскировкой | Очень высокая      | Очень высокая      | Крайне сложно             |
| OpenVPN + Cloak | С маскировкой | Высокая            | Средняя            | Сложно                    |
| XRay (REALITY)  | С маскировкой | Очень высокая      | Высокая            | Крайне сложно             |
| Shadowsocks     | С маскировкой | Средняя            | Высокая            | Может быть обнаружен      |


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Linux {#linux}


#### <span class="section-num">2.1.1</span> Установщик {#установщик}

-   Скачайте установщик. Скачайте файл `AmneziaVPN_Linux_Installer.tar`.
-   Распакуйте архив. В терминале перейдите в папку со скачанным файлом и выполните:
    ```shell
    tar -xvf AmneziaVPN_Linux_Installer.tar
    ```

-   Установите необходимые зависимости.
    -   Для Ubuntu/Debian:
        ```shell
        sudo apt update
        sudo apt install libxcb-xinerama0 libxcb-cursor0
        ```

-   Запустите установку.
    ```shell
    chmod +x AmneziaVPN_Linux_Installer.bin
    ./AmneziaVPN_Linux_Installer.bin
    ```


#### <span class="section-num">2.1.2</span> Gentoo (serg-sg) {#gentoo--serg-sg}

-   Для установки бинарной версии клиента можно использовать оверлей serg-sg.

-   Добавьте оверлей serg-sg:
    ```shell
    eselect repository add serg-sg git https://git.calculate-linux.org/serg-sg/gentoo-ebuild.git
    ```

-   Если репозиторий не включился автоматически, включите его:
    ```shell
    eselect repository enable serg-sg
    ```

-   Затем синхронизируйте:
    ```sh
    emerge --sync serg-sg
    # или
    emaint sync --repo serg-sg
    ```

-   Размаскируйте пакет.
    -   Добавьте в файл `/etc/portage/package.accept_keywords/custom` строку:
        ```sh
        echo "net-vpn/amnezia-client-bin::serg-sg ~amd64" >> /etc/portage/package.accept_keywords/custom
        ```

-   Установите клиент.
    ```sh
    emerge --ask net-vpn/amnezia-client-bin
    ```


#### <span class="section-num">2.1.3</span> Gentoo {#gentoo}

-   Установка из репозитория karma (см. [Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
    ```shell
    emerge amnezia-client-bin
    ```


#### <span class="section-num">2.1.4</span> Manjaro {#manjaro}

-   Из AUR:
    ```shell
    pamac install amneziavpn-bin
    ```


#### <span class="section-num">2.1.5</span> Настройка после установки {#настройка-после-установки}

<!--list-separator-->

1.  Модуль tun

    -   Необходимо наличие в ядре модуля `tun`.
    -   Пакет устанавливает конфигурационный файл для загрузки этого модуля.

<!--list-separator-->

2.  cgroup

    -   Желательно подключить net_cls cgroup.
    -   Необходимо смонтировать `/sys/fs/cgroup/net_cls/` как файловую систему cgroup v1:
        ```shell
        sudo mkdir -p /sys/fs/cgroup/net_cls
        sudo mount -t cgroup -o net_cls net_cls /sys/fs/cgroup/net_cls
        ```
    -   Постоянная конфигурация в файле `/etc/fstab`:
        ```conf-unix
        net_cls /sys/fs/cgroup/net_cls cgroup net_cls 0 0
        ```

<!--list-separator-->

3.  Сервис

    -   Подключение сервиса:
        ```shell
        systemctl enable --now AmneziaVPN.service
        ```

<!--list-separator-->

4.  Запуск

    -   Запуск:
        ```shell
        AmneziaVPN
        ```
