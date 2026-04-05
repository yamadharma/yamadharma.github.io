---
title: "Файловая система ipfs"
author: ["Dmitry S. Kulyabov"]
date: 2024-08-30T20:27:00+03:00
lastmod: 2026-03-26T13:35:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "ipfs-file-system"
---

Файловая система ipfs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   IPFS состоит из следующих уровней:
-   уровень имён: пользователи могут выбирать глобальные имена (привязка к DNS при помощи записей TXT);
-   уровень файлов: файловая система с изменяемыми файлами и снимками;
-   уровень объектов: неизменяемые объекты (могут или храниться в распределённой хеш-таблице (если маленькие), или скачиваться как в торрентах);
-   уровень обмена данными: протокол BitSwap;
-   уровень маршрутизации: как узлам добираться друг до друга;
-   сетевой уровень: по каким протоколам узлам связываться между собой;
-   уровень подлинности узлов (identity): чтобы нельзя было дублировать слишком много узлов (узлы с заданным номером), нарушая целостность сети.
-   Сайт: <https://ipfs.tech/>
-   Репозиторий описания: <https://github.com/ipfs/ipfs>


## <span class="section-num">2</span> Реализации {#реализации}

-   [IPFS. Реализация kubo]({{< relref "2026-03-26--ipfs-implementation-kubo" >}})


## <span class="section-num">3</span> Ресурсы {#ресурсы}

-   Awesome IPFS <https://github.com/ipfs/awesome-ipfs>


## <span class="section-num">4</span> Плагины {#плагины}


### <span class="section-num">4.1</span> IPFS Companion {#ipfs-companion}

-   Репозиторий: <https://github.com/ipfs/ipfs-companion>
-   Firefox: <https://addons.mozilla.org/ru/firefox/addon/ipfs-companion>
-   Chrome: <https://chromewebstore.google.com/detail/ipfs-companion/nibjojkomfdiaoajekhjakgkdhaomnch>
-   Поддержка адресации `ipfs://`.
-   Перенаправление адресов веб-сайтов и путей к файлам на локальный шлюз.
