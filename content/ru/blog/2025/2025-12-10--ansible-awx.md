---
title: "Ansible. Графический интерфейс AWX"
author: ["Dmitry S. Kulyabov"]
date: 2025-12-10T20:24:00+03:00
lastmod: 2025-12-10T20:27:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "ansible-awx"
---

Ansible. Графический интерфейс AWX.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/ansible/awx>
-   Лицензия: Apache License
-   Открытая версия Ansible Tower с аналогичным функционалом, но с открытым исходным кодом.
-   Управление инвентарём через GUI, включая динамические источники (AWS, GCP).
-   Планирование и выполнение заданий с поддержкой шаблонов и переменных.
-   Контроль доступа через LDAP, SAML, OAuth.
-   Логирование и мониторинг с интеграцией в ELK-стек и Grafana.
-   CI/CD и интеграция с SCM (GitHub, GitLab).

-   Сценарии использования:
    -   Open-source проекты и малые команды.
    -   Тестирование перед переходом на Ansible Tower.
