---
title: "Nmstate. Декларативное управление сетевыми настройками"
author: ["Dmitry S. Kulyabov"]
date: 2026-09-12T19:32:00+03:00
lastmod: 2026-09-13T20:05:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "nmstate-declarative-network-configuration"
---

## <span class="section-num">1</span> Nmstate. Декларативное управление сетевыми настройками {#index.ru}

Nmstate. Декларативное управление сетевыми настройками.

<!--more-->

{{< toc >}}


### <span class="section-num">1.1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/nmstate/nmstate>
-   Библиотека и утилита командной строки для декларативного управления сетевыми настройками хоста.
-   Описание в текстовом файле (YAML или JSON).
-   Реализует декларативный подход.
-   В качестве основного бэкенда используется NetworkManager.


### <span class="section-num">1.2</span> Nmstate и NetworkManager {#nmstate-и-networkmanager}


#### <span class="section-num">1.2.1</span> Императивный подход (`nmcli`) {#императивный-подход--nmcli}

-   Что нужно сделать:
    ```shell
    nmcli connection add type vlan con-name vlan10 ifname ens18.10 dev ens18 id 10 ipv4.addresses 10.10.10.2/24 ipv4.method manual
    ```

-   Не идемпотентно (если вы запустите эту команду дважды, она выдаст ошибку).


#### <span class="section-num">1.2.2</span> Декларативный подход (`nmstate`) {#декларативный-подход--nmstate}

-   Какой результат нужно получить:
    ```yaml
    interfaces:
    ​  - name: ens18.10
        type: vlan
        state: up
        vlan:
          base-iface: ens18
          id: 10
        ipv4:
          enabled: true
          address:
    ​        - ip: 10.10.10.2
              prefix-length: 24
    ```

-   Идемпотентность (Если профиль уже существует --- ничего не произойдет. Если его нет --- он будет создан).


### <span class="section-num">1.3</span> Установка {#установка}

```shell
sudo dnf -y install nmstate
```


### <span class="section-num">1.4</span> Миграция на nmstate {#миграция-на-nmstate}

-   Процесс миграции сводится к экспорту текущих настроек в YAML и переходу на управление через файлы.
-   В RHEL 9/10 классические скрипты `/etc/sysconfig/network-scripts` не поддерживаются.
-   Настройки хранятся в файлах NetworkManager (`/etc/NetworkManager/system-connections/`).


#### <span class="section-num">1.4.1</span> Экспорт текущей конфигурации {#экспорт-текущей-конфигурации}

-   Выполните команду:

<!--listend-->

```shell
nmstatectl show > current-network.yaml
```
