---
title: "Gentoo. emerge. Ограничение ресурсов"
author: ["Dmitry S. Kulyabov"]
date: 2026-05-24T16:25:00+03:00
lastmod: 2026-05-24T19:28:00+03:00
draft: false
slug: "gentoo-emerge-resource-limitation"
---

Gentoo. emerge. Ограничение ресурсов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Стоит задача ограничения использования ресурсов системы при компиляции пакетов.


## <span class="section-num">2</span> Cgroup {#cgroup}

-   Используем либо возможности systemd, либо настраиваем сами.


### <span class="section-num">2.1</span> systemd {#systemd}

-   Используем `systemd-run` (см. [Параметры systemd-run]({{< relref "2026-05-24--systemd-run-parameters" >}})).
-   `systemd` сам позаботится о создании нужной cgroup и применении всех заданных в файле лимитов.
-   Создайте файл, например, `/etc/systemd/system/emerge.slice`:
    ```shell
    sudo touch /etc/systemd/system/emerge.slice
    ```
-   Заполните его:

<!--listend-->

```ini
[Slice]
MemoryMax=4G
CPUQuota=50%
CPUWeight=idle
IOWeight=50
```

-   Запустите команду от имени этого slice:

<!--listend-->

```shell
sudo systemd-run --slice=emerge.slice --scope emerge <package>
```


### <span class="section-num">2.2</span> Ручная настройка {#ручная-настройка}


#### <span class="section-num">2.2.1</span> Проверка cgroups {#проверка-cgroups}

-   Убедимся, что система использует cgroups второй версии (v2).
-   Проверим, что файловая система `cgroup2` смонтирована:

<!--listend-->

```shell
mount -l | grep cgroup2
```

-   Ожидаемый вывод:

<!--listend-->

```text
cgroup2 on /sys/fs/cgroup type cgroup2 (rw,nosuid,nodev,noexec,relatime,nsdelegate)
```


#### <span class="section-num">2.2.2</span> Настройка для portage {#настройка-для-portage}

<!--list-separator-->

1.  Создаем cgroup

    -   Создадим отдельную директорию для группы, которой будем управлять:

    <!--listend-->

    ```shell
    sudo mkdir -p /sys/fs/cgroup/emerge
    ```

    -   Проверим, какие ресурсы доступны для управления:

    <!--listend-->

    ```shell
    cat /sys/fs/cgroup/cgroup.controllers
    ```

<!--list-separator-->

2.  Настройка лимитов

    -   Зададим конкретные ограничения для этой группы.

    -   Ограничение памяти (Memory).
        -   Установим лимит на использование оперативной памяти в 4 гигабайта и включим групповой OOM-киллер (который при нехватке памяти завершит всю группу процессов, а не по одному):
            ```shell
            echo "4G" | sudo tee /sys/fs/cgroup/emerge/memory.max
            echo 1 | sudo tee /sys/fs/cgroup/emerge/memory.oom.group
            ```

    -   Ограничение CPU.
        -   Ограничение процессора задается через веса. Например, вес `100` означает, что группа `emerge` будет получать примерно в два раза меньше процессорного времени, чем группа с весом `200` (стандартный вес по умолчанию --- 100).
            ```shell
            echo "50" | sudo tee /sys/fs/cgroup/emerge/cpu.weight
            ```

    -   Ограничение дискового I/O.
        -   Ограничение операций ввода-вывода настраивается чуть сложнее. Сначала нужно узнать номера ваших дисков (`major:minor`):
            ```shell
            lsblk -o NAME,MAJ:MIN
            ```

        -   Предположим, мы хотим ограничить пропускную способность для диска с номерами `8:0` (обычно это `/dev/sda`) до 10 мегабайт в секунду.
        -   Мы записываем лимит в формате `Номер_устройства:номер_узла Тип_операции=Лимит`.
        -   Число `$((10 * 1024 * 1024))` --- это 10 МиБ/с:
            ```shell
            echo "8:0 wbps=$((10 * 1024 * 1024))" | sudo tee /sys/fs/cgroup/emerge/io.max
            echo "8:0 rbps=$((10 * 1024 * 1024))" | sudo tee /sys/fs/cgroup/emerge/io.max
            ```

<!--list-separator-->

3.  Интегрируем с portage

    -   Нужно, чтобы все процессы, запускаемые командой `emerge`, попадали в нашу новую группу.

    <!--list-separator-->

    1.  Утилита `cgexec`

        -   Установите пакет `dev-libs/libcgroup` и затем запускайте `emerge` с помощью `cgexec`:
            ```shell
            cgexec -g cpu,memory,io:emerge emerge <package>
            ```

        -   Здесь явно указаны ресурсы `cpu`, `memory`, `io` и группа `emerge`.

    <!--list-separator-->

    2.  Скрипт

        -   Если `cgexec` по каким-то причинам недоступен, подойдет shell-скрипт.
        -   Создайте файл `~/bin/emerge-cg` со следующим содержимым:
            ```shell
            #!/bin/bash
            # Путь к cgroup
            CGROUP_PATH="/sys/fs/cgroup/emerge"

            # Проверяем, существует ли группа
            if [ ! -d "$CGROUP_PATH" ]; then
                echo "Ошибка: Cgroup $CGROUP_PATH не найдена. Создайте ее: sudo mkdir -p $CGROUP_PATH"
                exit 1
            fi

            # Добавляем текущий PID и все будущие дочерние процессы в группу emerge
            echo $$ | sudo tee "$CGROUP_PATH/cgroup.procs" > /dev/null

            # Запускаем оригинальную команду emerge со всеми переданными аргументами
            exec emerge "$@"
            ```

        -   Сделайте скрипт исполняемым: `chmod +x ~/bin/emerge-cg`.
        -   Теперь команда `emerge-cg <package>` запустит сборку с лимитами.


## <span class="section-num">3</span> Параметры portage {#параметры-portage}


### <span class="section-num">3.1</span> Ограничение использования CPU {#ограничение-использования-cpu}

-   Ограничение числа потоков (`MAKEOPTS`)
    -   Переменная напрямую влияет на загрузку процессора и потребление памяти.
    -   Рекомендуется указывать значение на 1-2 меньше числа логических ядер, чтобы система оставалась отзывчивой.
        ```shell
        # /etc/portage/make.conf
        MAKEOPTS="-j4" # для 4-поточного CPU
        ```

-   Понижение приоритета планировщика (`PORTAGE_SCHEDULING_POLICY`).
    -   Политика `idle` дает компиляции наименьший приоритет, используя ресурсы ЦП только в моменты полного простоя, и является более эффективным методом, чем `PORTAGE_NICENESS`.
        ```sh
        # /etc/portage/make.conf
        PORTAGE_SCHEDULING_POLICY="idle"
        ```


### <span class="section-num">3.2</span> Контроль использования памяти {#контроль-использования-памяти}

-   Индивидуальная настройка для «прожорливых» пакетов.
    -   Для управления пакетами, потребляющими много памяти при компиляции (например, `qtwebengine`, `firefox`), можно создать файл `/etc/portage/package.env` с ограничением потоков только для них:
        ```sh
        # /etc/portage/package.env
        dev-qt/qtwebengine lowmemory.conf
        www-client/firefox lowmemory.conf
        ```

-   В файле `/etc/portage/env/lowmemory.conf` прописать:
    ```shell
    MAKEOPTS="-j1"
    ```


### <span class="section-num">3.3</span> Снижение нагрузки на диск {#снижение-нагрузки-на-диск}

-   Понижение приоритета ввода-вывода.
-   Эта настройка дает процессам компиляции (`emerge`) наименьший приоритет доступа к диску, что помогает сохранить отзывчивость системы.
    ```shell
    # /etc/portage/make.conf
    PORTAGE_IONICE_COMMAND="ionice -c 3 -p \${PID}"
    ```
