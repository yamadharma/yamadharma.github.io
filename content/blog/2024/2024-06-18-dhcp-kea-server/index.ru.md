---
title: "Сервер DHCP Kea"
author: ["Dmitry S. Kulyabov"]
date: 2024-06-18T11:07:00+03:00
lastmod: 2024-08-26T14:29:00+03:00
tags: ["linux", "sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "dhcp-kea-server"
---

Сервер DHCP Kea.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.isc.org/kea/>
-   Современный стандартный сервер DHCP.
-   Репозиторий:
    -   <https://gitlab.isc.org/isc-projects/kea>
    -   <https://github.com/isc-projects/kea>
-   Документация: <https://kea.readthedocs.io/en/latest/index.html>


### <span class="section-num">1.1</span> Особенности {#особенности}

-   Модульная конструкция компонентов
    -   Расширяется с помощью модулей-хуков.
    -   Дистрибутив Kea включает отдельные демоны для сервера DHCPv4, сервера DHCPv6 и модуля динамического DNS (DDNS).
-   Онлайн-реконфигурация с помощью REST API.
    -   Kea использует файл конфигурации JSON, который можно изменить удалённо без остановки и перезапуска сервера.
-   Панель управления через веб-интерфейс.
-   Поддерживает базы данных MySQL, PostgreSQL:
    -   упрощает интеграцию с другими системами;
    -   можно использовать один и тот же сервер резервирования хостов для нескольких DHCP-серверов;
    -   администрирование глобальных параметров из централизованной системы настройки.


## <span class="section-num">2</span> Установка {#установка}

-   [DHCP. Установка сервера DHCP Kea]({{< relref "2024-05-07-dhcp-server-installation" >}})


## <span class="section-num">3</span> Настройка {#настройка}

-   [Динамическое обновление DNS-сервера BIND при помощи Kea DHCP]({{< relref "2024-06-18-dynamically-updating-bind-dns-kea-dhcp" >}})


## <span class="section-num">4</span> Дополнения {#дополнения}

-   [NetBox. Плагин netbox-kea]({{< relref "2024-07-22-netbox-plugin-netbox-kea" >}})
