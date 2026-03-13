---
title: "Sway. Интеграция systemd"
author: ["Dmitry S. Kulyabov"]
date: 2023-12-08T19:03:00+03:00
lastmod: 2023-12-23T19:04:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "sway-systemd-integration"
---

Интеграция systemd в sway.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Информация {#информация}

-   Интеграция может подразумевать следующее:
    -   Взаимодействие sway с systemd.
    -   Запуск sway как сервиса systemd.


## <span class="section-num">2</span> Запуск sway как сервиса systemd {#запуск-sway-как-сервиса-systemd}

-   Репозиторий: <https://github.com/xdbob/sway-services>


## <span class="section-num">3</span> Взаимодействие sway с systemd {#взаимодействие-sway-с-systemd}

-   Репозиторий: <https://github.com/alebastr/sway-systemd>
-   Несколько направлений интеграции:
    -   Экспорт необходимых переменных в среду пользовательского сеанса systemd.
    -   Задание `sway-session.target` для запуска пользовательских служб.
    -   Обеспечения совместимости с `systemd-oomd`.


### <span class="section-num">3.1</span> Компоненты {#компоненты}


#### <span class="section-num">3.1.1</span> sway-session.target {#sway-session-dot-target}

-   Systemd запрещает запуск `graphical-session.target` напрямую и поощряет использование целевых модулей, специфичных для конкретной среды.
-   Пакет определяет `sway-session.target`.
-   `sway-session.target` должен запускаться, когда установлена среда пользовательского сеанса, и останавливаться перед выходом.
-   Специальный юнит `sway-session-shutdown.target` может быт использован для остановки `graphical-session.target` и `sway-session.target`.


#### <span class="section-num">3.1.2</span> Скрипт session.sh {#скрипт-session-dot-sh}

-   Скрипт `session.sh` отвечает за импорт переменных среды `systemd` и `dbus`.
-   Остаётся в фоновом режиме до тех пор, пока `sway` не завершит работу, не остановит сеанс и не сбросит переменные для пользовательского сеанса `systemd` (это можно отключить, передав --no-cleanup).
-   Сам скрипт не устанавливает никаких переменных, кроме `XDG_CURRENT_DESKTOP`, `XDG_SESSION_TYPE`.
-   Он просто передаёт значения, полученные от `sway`.
-   Список переменных и имя цели сеанса в настоящее время жестко запрограммированы и могут быть изменены путем редактирования сценария.


#### <span class="section-num">3.1.3</span> Настройка cgroups {#настройка-cgroups}

-   Сценарий `assign-cgroups.py` подписывается на новое событие `i3 ipc` окна и автоматически создаёт временную единицу области видимости для каждого приложения с графическим интерфейсом, запущенного в той же контрольной группе, что и `sway`.
-   Сценарий необходим для преодоления ограничения `systemd-oomd`: он отслеживает использование ресурсов только контрольными группами и уничтожает всю группу, когда одно приложение ведёт себя неправильно и превышает лимиты использования ресурсов.
-   Помещая отдельные приложения в изолированные контрольные группы, мы уменьшаем вероятность того, что `oomd killer` случайно завершит сеанс.
-   Для работы необходимы следующие пакеты python: `dbus-next`, `i3ipc`, `psutil`, `tenacity`, `python-xlib`.


#### <span class="section-num">3.1.4</span> Конфигурация раскладки клавиатуры {#конфигурация-раскладки-клавиатуры}

-   Сценарий изучает общесистемную входную конфигурацию из интерфейса systemd, преобразует ее в конфигурацию Sway и применяет ко всем устройствам с типом клавиатура.
-   Основной мотивацией для создания этого компонента была возможность применить общесистемные раскладки клавиатуры для `sway`.


#### <span class="section-num">3.1.5</span> Автозапуск XDG Desktop {#автозапуск-xdg-desktop}

-   `xdg-desktop-autostart.target` запускает модули, созданные из XDG-файлов рабочих стола в каталогах автозапуска.


### <span class="section-num">3.2</span> Установка вручную {#установка-вручную}


#### <span class="section-num">3.2.1</span> Подготовка {#подготовка}

-   Клонируйте репозиторий:
    ```shell
    cd /tmp
    git clone https://github.com/alebastr/sway-systemd.git
    cd sway-systemd
    ```


#### <span class="section-num">3.2.2</span> Юниты systemd {#юниты-systemd}

-   Скопируйте `units/*.target` в каталог пользовательского модуля `systemd` (`/usr/lib/systemd/user/`, `$XDG_CONFIG_HOME/systemd/user/`, `~/.config/systemd/user`):
    ```shell
    mkdir -p ~/.config/systemd/user/
    cp units/*.target ~/.config/systemd/user/
    ```
-   Запустите `systemctl --user daemon-reload`, чтобы systemd повторно просканировал служебные файлы.


#### <span class="section-num">3.2.3</span> Скрипт session.sh {#скрипт-session-dot-sh}

-   Добавьте конфигурационный файл `~/.config/sway/config.d/10-systemd-session.conf`:
    ```conf-unix
    exec ~/.config/sway/scripts/session.sh
    ```


#### <span class="section-num">3.2.4</span> Настройка Cgroups {#настройка-cgroups}

-   Установите необходимые пакеты python.
    -   Gentoo:
        ```shell
        emerge dev-python/dbus-next dev-python/i3ipc dev-python/psutil dev-python/tenacity dev-python/python-xlib
        ```
-   Добавьте конфигурационный файл `~/.config/sway/config.d/10-systemd-cgroups.conf`:
    ```conf-unix
    exec ~/.config/sway/scripts/assign-cgroups.py
    ```


#### <span class="section-num">3.2.5</span> Конфигурация раскладки клавиатуры {#конфигурация-раскладки-клавиатуры}

-   Добавьте конфигурационный файл `~/.config/sway/config.d/95-system-keyboard-config.conf`:
    ```conf-unix
    exec_always ~/.config/sway/scripts/locale1-xkb-config --oneshot
    ```


#### <span class="section-num">3.2.6</span> Автозапуск XDG Desktop {#автозапуск-xdg-desktop}

-   Добавьте конфигурационный файл `~/.config/sway/config.d/95-xdg-desktop-autostart.conf`:
    ```conf-unix
    exec ~/.config/sway/scripts/wait-sni-ready && systemctl --user start sway-xdg-autostart.target
    ```


#### <span class="section-num">3.2.7</span> Завершение {#завершение}

-   Перезапустите сеанс `sway`.
