---
title: "Параметры systemd-run"
author: ["Dmitry S. Kulyabov"]
date: 2026-05-24T16:39:00+03:00
lastmod: 2026-05-24T17:12:00+03:00
tags: ["sysadmin", "linux"]
categories: ["computer-science"]
draft: false
slug: "systemd-run-parameters"
---

Параметры systemd-run.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   `systemd-run` динамически создает временные (transient) юниты в systemd.
-   Это могут быть сервисы или области (scope).
-   Transient units --- это способ получить преимущества systemd (cgroups, логирование, изоляция) для разовых и интерактивных задач без постоянных unit-файлов.
-   Два режима:
    -   `--service` (значение по умолчанию) --- создается transient-сервис с `ExecStart` равным вашей команде.
    -   `--scope` --- не сервис, а контейнер для уже запущенного процесса с вашим TTY.
        -   Для интерактивных команд: вы видите stdout/stderr сразу в консоли, а cgroup-лимиты работают как на полноценный сервис.


## <span class="section-num">2</span> Процессор {#процессор}

-   Свойство `CPUQuota` задает потолок CPU в процентах от одного ядра:
    -   `CPUQuota=50%` --- половина одного CPU в сумме по всем ядрам.
    -   `CPUQuota=100%` --- ровно одно полноценное ядро.
    -   `CPUQuota=250%` --- два с половиной ядра суммарно (на 4 vCPU это около 62.5% общего CPU).

-   Это интегральный потолок «сколько CPU-времени суммарно» потребляет группа процессов в cgroup.
-   100% --- это одно полноценное ядро. Если у вас 8 vCPU и вы хотите «не более половины всей мощности», ставьте 400%, а не 50%.
-   Это не пиннинг на конкретные ядра и не приоритет.
-   Если вам нужно распределить долю CPU относительно других сервисов, используйте `CPUWeight` (от 1 до 10000).
-   Если требуется закрепить выполнение на определенных ядрах, используйте `CPUAffinity` или `AllowedCPUs`.

-   Итого:
    -   `CPUQuota=` --- жесткий лимит (сколько CPU максимум).
    -   `CPUWeight=` --- относительная важность при конкуренции.
    -   `AllowedCPUs=` --- перечисление разрешенных CPU (например, `0-1,3`).
    -   `CPUAffinity=` --- битовая маска/список для пиннинга процессов юнита.


## <span class="section-num">3</span> Память {#память}

-   `MemoryMax=` --- жесткий потолок RSS+cache для cgroup.
    -   Превышение ведет к OOMKill внутри cgroup.
    -   Значение `0` означает «без лимита».
-   `MemoryHigh=` --- мягкий потолок: ядро будет ограничивать задачи при превышении, но не обязательно завершать.
-   `MemorySwapMax=` --- лимит на swap для cgroup.
    -   Значение `0` --- запрет свопа для юнита; `infinity` --- без лимита.
-   Поведение при OOM можно уточнить через `OOMPolicy=` (например, `continue`, `stop`, `kill`) и параметры взаимодействия с `systemd-oomd`.
-   Если процесс завершился с OOM, важно понять «чей OOM»: ядра внутри cgroup (жесткий лимит `MemoryMax`) или системный/oomd из-за глобального давления:
    -   При срабатывании `MemoryMax` журнал содержит записи о «killed process in cgroup»; exit code обычно 9 или 137 (SIGKILL).
    -   Если сработал `systemd-oomd`, в журнале появятся строчки от него с PSI-контекстом.
-   Для критичных задач добавляйте мягкий `MemoryHigh` рядом с `MemoryMax`.
    -   Это позволит ядру заранее ограничивать задачи и снизить риск мгновенного убийства.


## <span class="section-num">4</span> Режимы запуска {#режимы-запуска}

-   Используйте `--scope`, если:
    -   нужна интерактивность (вы видите вывод в своей TTY, можно вводить пароли и т.п.);
    -   вы запускаете разовую команду с лимитами и хотите вернуться к шеллу после завершения;
    -   достаточно простых ограничений ресурсов и журналирования.

-   Используйте `--service`, если:
    -   нужен «one-shot» сервис с `Type=oneshot`, контролем зависимостей, политиками перезапуска;
    -   вы хотите именованный юнит для мониторинга/логов (`--unit=`), и чтобы он оставался в истории (`--collect` или без него);
    -   планируете подключить таймеры (`systemd-run --on-active=`, `--on-unit-active=`).


## <span class="section-num">5</span> Логи {#логи}

-   Все, что запущено через `systemd-run`, автоматически уходит в journald.
-   Нагрузка по cgroups видна в `systemd-cgtop`.
-   Для именованных юнитов проверяйте:
    ```shell
    journalctl -u backup-db -e
    ```

-   `systemd-cgtop` --- покажет потребление CPU и памяти по cgroups; удобно для проверки эффектов `CPUQuota`, `MemoryMax`.
-   `journalctl -u <unit>` --- логи конкретного transient unit.
-   Проверяйте результат через код выхода: `systemd-run --wait` вернет код процесса в оболочку.
-   Для долгих задач полезно добавить `RuntimeMaxSec=`, чтобы не забыть «висящий» процесс.


## <span class="section-num">6</span> Срезы {#срезы}

-   Срезы удобны тем, что их лимиты наследуются всеми дочерними юнитами.
-   Если несколько периодических задач, имеет смысл складывать их в общий slice и задать лимиты на уровне среза, а отдельным запускам --- дополнительные, более строгие:
    ```shell
    systemd-run --scope -p Slice=batch.slice -p CPUQuota=200% -p MemoryMax=3G bash -lc 'rclone sync /data s3:bucket/data'
    ```


## <span class="section-num">7</span> Пользовательские юниты {#пользовательские-юниты}

-   `systemd-run --user` запускает transient units в пользовательском менеджере systemd:
    ```shell
    systemd-run --user --scope -p CPUQuota=150% -p MemoryMax=2G bash -lc 'npm ci && npm run build'
    ```


## <span class="section-num">8</span> Таймеры {#таймеры}

-   `systemd-run` умеет использовать transient timers.
-   Это удобно для одноразового отложенного запуска с лимитами, без редактирования файлов:
    ```shell
    systemd-run --unit=cleanup-once --on-active=10min -p Type=oneshot -p CPUQuota=50% -p MemoryMax=512M bash -lc 'find /tmp -type f -mtime +1 -delete'
    ```

-   Через 10 минут запустится разовая уборка с ограничениями по CPU и памяти.


## <span class="section-num">9</span> Чек-лист перед запуском {#чек-лист-перед-запуском}

-   Определите потолок CPU: `CPUQuota` для жесткой или `CPUWeight` для справедливой конкуренции.
-   Задайте память: `MemoryMax` и, при необходимости, `MemoryHigh`; подумайте о `MemorySwapMax`.
-   Выберите режим: `--scope` для интерактива, `--service` для one-shot с мониторингом состояния.
-   Дайте понятное имя юниту через `--unit=`.
-   При необходимости ограничьте процессоры: `AllowedCPUs` или `CPUAffinity`.
-   Сгруппируйте схожие задачи в `batch.slice` и задайте общий бюджет.


## <span class="section-num">10</span> Примеры команд {#примеры-команд}


### <span class="section-num">10.1</span> Интерактивный запуск {#интерактивный-запуск}

-   Ограничить задачу одним CPU и 1 Гбайтом памяти.
-   После завершения вернемся в shell, а лог попадет в journald под именем transient-unit.
    ```shell
    systemd-run --scope -p CPUQuota=100% -p MemoryMax=1G bash -lc 'tar -cf /backups/site.tar /var/www/site'
    ```


### <span class="section-num">10.2</span> Запуск с именем и ожиданием завершения {#запуск-с-именем-и-ожиданием-завершения}

-   `--wait` вернет код завершения процесса.
-   `--quiet` приглушает вспомогательный вывод.
-   Имя юнита `backup-db.service` упростит поиск логов в `journalctl -u backup-db`.
    ```shell
    systemd-run --unit=backup-db --wait --quiet -p Type=oneshot -p CPUQuota=80% -p MemoryMax=2G bash -lc 'pg_dump -F c appdb > /srv/backup/appdb.dump'
    ```


### <span class="section-num">10.3</span> Пиннинг к ядрам {#пиннинг-к-ядрам}

-   Использовать только CPU 2 и 3.
-   `CPUWeight` подскажет планировщику относительную «важность» этой группы по сравнению с другими cgroups.
    ```shell
    systemd-run --scope -p AllowedCPUs=2-3 -p CPUWeight=200 bash -lc 'make -j4 build'
    ```


### <span class="section-num">10.4</span> Бэкап БД ночью {#бэкап-бд-ночью}

-   `MemoryHigh` позволит ядру притормаживать pg_dump при всплесках page cache.
-   `MemoryMax` спасет остальную систему от безлимитного роста потребления памяти.
    ```shell
    systemd-run --unit=nightly-pg-backup --wait -p Type=oneshot -p CPUQuota=60% -p MemoryHigh=1.5G -p MemoryMax=2G bash -lc 'pg_dump -F c app > /srv/backup/app-$(date +%F).dump'
    ```


### <span class="section-num">10.5</span> Ограничение build-пайплайна {#ограничение-build-пайплайна}

-   Сборка не съест весь CPU сервера:
    ```shell
    systemd-run --scope -p CPUQuota=150% -p MemoryMax=2G bash -lc 'corepack pnpm i && corepack pnpm build'
    ```


### <span class="section-num">10.6</span> Перепаковка медиа с пиннингом {#перепаковка-медиа-с-пиннингом}

-   Пиннинг на 1-2 CPU сохраняет отзывчивость системы:
    ```shell
    systemd-run --scope -p AllowedCPUs=1-2 -p MemoryMax=1G bash -lc 'ffmpeg -i in.mp4 -c:v libx264 -preset veryfast -c:a aac out.mp4'
    ```
