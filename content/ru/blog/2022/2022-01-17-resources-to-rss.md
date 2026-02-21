---
title: "Подключение ресурсов через RSS"
author: ["Dmitry S. Kulyabov"]
date: 2022-01-17T17:14:00+03:00
lastmod: 2025-06-08T19:19:00+03:00
tags: ["sysadmin"]
categories: ["computer-science", "self-management"]
draft: false
slug: "resources-to-rss"
---

-   Мне удобно читать обновления web-ресурсов через RSS.
-   К сожалению сейчас стало много ресурсов, не поддерживающих подключение через этот формат.
-   Но можно осуществить просмотр ресурсов через RSS, используя разные шлюзы.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   RSS --- семейство XML-форматов, предназначенных для описания разных интернет ресурсов.
-   В разных версиях аббревиатура RSS имела разные расшифровки:
    -   Rich Site Summary (RSS 0.9x) --- обогащённая сводка сайта;
    -   RDF Site Summary (RSS 0.9 и 1.0) --- сводка сайта с применением инфраструктуры описания ресурсов;
    -   Really Simple Syndication (RSS 2.x) --- очень простое распространение.
-   Существуют специализированные приложения (RSS-агрегаторы), собирающие и обрабатывающие информацию RSS-каналов.


## <span class="section-num">2</span> Определение адреса ленты rss {#определение-адреса-ленты-rss}


### <span class="section-num">2.1</span> Как найти rss {#как-найти-rss}

-   Наиболее распространённые ссылки на rss:
    -   `/feed/`
    -   `/rss/`
    -   `/blog/feed/`
    -   `/blog/rss/`
    -   `/rss.xml`
    -   `/blog/rss.xml`


### <span class="section-num">2.2</span> Сайты-помощники {#сайты-помощники}

-   <https://rssfinder.app/>
-   <https://getrssfeed.com/>
-   <https://lighthouseapp.io/tools/feed-finder>


## <span class="section-num">3</span> Универсальный шлюз _rsshub.app_ {#универсальный-шлюз-rsshub-dot-app}

-   Адрес: <https://rsshub.app/>
-   Репозиторий: <https://github.com/DIYgod/RSSHub>
-   Документация: <https://docs.rsshub.app/>
-   Имеет большое количество шлюзов для обработки разных ресурсов.


## <span class="section-num">4</span> Ресурсы {#ресурсы}

-   Ресурсы, которыми я пользуюсь.


### <span class="section-num">4.1</span> Vkontakte {#vkontakte}

-   Шлюз _vkrss.ru_
    -   Адрес: <https://vkrss.ru/>
    -   Если у вас группа `https://vk.com/groupname`, то имя rss-канала будет `https://vkrss.ru/groupname`.


### <span class="section-num">4.2</span> Telegram {#telegram}

-   Шлюз _rsshub.app_
    -   Если нужно подключить канал _<https://t.me/channelname>_, то имя rss-канала будет _<https://rsshub.app/telegram/channel/channelname>_.
