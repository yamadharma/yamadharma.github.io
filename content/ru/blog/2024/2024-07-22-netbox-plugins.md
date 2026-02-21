---
title: "NetBox. Плагины"
author: ["Dmitry S. Kulyabov"]
date: 2024-07-22T17:45:00+03:00
lastmod: 2025-03-26T13:58:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "netbox-plugins"
---

Плагины NetBox.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Основные плагины: <https://netboxlabs.com/netbox-plugins/>
-   Плагины NetBox являются приложениями Django.
-   Плагины могут добавлять свои собственные модели и представления, но не могут вмешиваться в работу существующих компонентов.
-   Архитектура плагинов NetBox позволяет следующее:
    -   добавлять новые модели данных;
    -   добавлять новые URL-адреса и представления.
        -   могут регистрировать URL-адреса  `/plugins` для предоставления пользователям возможности просмотра;
    -   добавлять контент в существующие шаблоны моделей;
    -   добавлять пункты в меню навигации;
    -   добавлять собственное промежуточное программное обеспечение;
    -   объявлять параметры конфигурации;
        -   параметры конфигурации определяются пользователем в разделе `PLUGINS_CONFIG` в `configuration.py`.


## <span class="section-num">2</span> Установка плагинов {#установка-плагинов}


### <span class="section-num">2.1</span> Установите пакет Python {#установите-пакет-python}

-   Загрузите и установите пакет Python плагина, следуя инструкциям по установке.
-   Плагины, публикуемые через PyPI, обычно устанавливаются с помощью утилиты `pip` командной строки.
-   Обязательно установите плагин в виртуальной среде NetBox.
    ```shell
    source /opt/netbox/venv/bin/activate
    (venv) $ pip install <package>
    ```
-   Альтернативно, можно установить плагин вручную:
    ```shell
    python setup.py install
    ```


### <span class="section-num">2.2</span> Включите плагин {#включите-плагин}

-   В `configuration.py` добавьте имя плагина в список `PLUGINS`:
    ```yaml
    PLUGINS = [
        # ...
        'plugin_name',
    ]
    ```


### <span class="section-num">2.3</span> Настройте плагин {#настройте-плагин}

-   Если плагин требует какой-либо настройки, задайте её в `/opt/netbox/netbox/netbox/configuration.py` в параметре `PLUGINS_CONFIG`:
    ```yaml
    PLUGINS_CONFIG = {
        'plugin_name': {
            'foo': 'bar',
            'buzz': 'bazz'
        }
    }
    ```


### <span class="section-num">2.4</span> Запустите миграцию базы данных {#запустите-миграцию-базы-данных}

-   Если плагин вводит новые модели базы данных, выполните миграцию схемы:
    ```shell
    (venv) $ cd /opt/netbox/netbox/
    (venv) $ python3 manage.py migrate
    ```


### <span class="section-num">2.5</span> Статические файлы {#статические-файлы}

-   Плагины могут упаковывать статические ресурсы, такие как изображения или скрипты, для непосредственного обслуживания HTTP-интерфейсом.
-   Убедитесь, что они скопированы в статический корневой каталог с именем `collectstatic`:
    ```shell
    (venv) $ cd /opt/netbox/netbox/
    (venv) $ python3 manage.py collectstatic
    ```


### <span class="section-num">2.6</span> Перезапустите службу WSGI {#перезапустите-службу-wsgi}

-   Перезапустите службу WSGI:
    ```shell
    systemctl restart netbox netbox-rq
    ```


## <span class="section-num">3</span> Удаление плагинов {#удаление-плагинов}


### <span class="section-num">3.1</span> Отключите плагин {#отключите-плагин}

-   Отключите плагин, удалив его из списка `PLUGINS` список в `configuration.py` .


### <span class="section-num">3.2</span> Удалите конфигурацию {#удалите-конфигурацию}

-   Удалите запись о плагине в словаре `PLUGINS_CONFIG` в `configuration.py` .


### <span class="section-num">3.3</span> Переиндексируйте записи поиска {#переиндексируйте-записи-поиска}

-   Запустите команду `reindex` для переиндексации глобальной поисковой системы.
-   Это удалит все устаревшие записи, относящиеся к объектам, предоставляемым плагином:
    ```shell
    cd /opt/netbox/netbox/
    source /opt/netbox/venv/bin/activate
    (venv) $ python3 manage.py reindex
    ```


### <span class="section-num">3.4</span> Удалите пакет Python {#удалите-пакет-python}

-   Используйте `pip`, чтобы удалить установленный плагин:
    ```shell
    source /opt/netbox/venv/bin/activate
    (venv) $ pip uninstall <package>
    ```


### <span class="section-num">3.5</span> Перезапустите службу WSGI {#перезапустите-службу-wsgi}

-   Перезапустите службу WSGI:
    ```shell
    systemctl restart netbox
    ```


### <span class="section-num">3.6</span> Удалите таблицы базы данных {#удалите-таблицы-базы-данных}

-   Этот шаг необходим только для плагинов, которые создали одну или несколько таблиц базы данных.
-   Войдите в оболочку базы данных PostgreSQL (`manage.py dbshell`), чтобы определить, создал ли плагин какие-либо таблицы SQL.
-   Можно запустить командe `\dt` без шаблона для вывода списка всех  таблиц.
    ```shell
    netbox=> \dt pluginname_*
    ```
-   Удалите каждую из перечисленных таблиц:
    ```shell
    netbox=> DROP TABLE pluginname_foo;
    netbox=> DROP TABLE pluginname_bar;
    ```


### <span class="section-num">3.7</span> Удалите записи миграции Django {#удалите-записи-миграции-django}

-   После удаления таблиц, созданных плагином, миграции, создавшие эти таблицы, также необходимо удалить из истории миграции Django.
-   Это необходимо для того, чтобы иметь возможность переустановить плагин позже.
-   Если бы история миграции осталась на месте, Django пропустил бы все миграции, которые были выполнены в ходе предыдущей установки, что привело бы к сбою плагина после переустановки.
    ```shell
    netbox=> SELECT * FROM django_migrations WHERE app='pluginname';
    netbox=> DELETE FROM django_migrations WHERE app='pluginname';
    ```
