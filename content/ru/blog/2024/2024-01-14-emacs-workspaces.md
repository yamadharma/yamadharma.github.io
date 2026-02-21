---
title: "Emacs. Рабочее пространство"
author: ["Dmitry S. Kulyabov"]
date: 2024-01-14T15:44:00+03:00
lastmod: 2024-01-15T10:15:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-workspaces"
---

Управление рабочими пространствами (workspaces) в Emacs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Пакеты {#пакеты}


### <span class="section-num">1.1</span> Perspective for Emacs {#perspective-for-emacs}

-   Репозиторий: <https://github.com/nex3/perspective-el>
-   Создаёт несколько именованных рабочих пространств (_перспектив_) в Emacs, аналогично нескольким рабочим столам в тайловых оконных менеджерах (см. [Тайловые оконные менеджеры]({{< relref "2023-06-19-tiling-window-manager" >}})).
-   Каждая _перспектива_ имеет свой собственный список буферов и собственный макет окон.
-   В _перспективе_ по умолчанию доступны только её буферы.
-   Каждый фрейм Emacs имеет отдельный список перспектив.
-   Поддерживается сохранение состояния в файл.


### <span class="section-num">1.2</span> persp-mode {#persp-mode}

-   Репозиторий: <https://github.com/Bad-ptr/persp-mode.el>
-   Форк _Perspective_.
-   Реализует другой подход к сохранению состояния и другие параметры конфигурации.
-   При форке были оставлены те же названия функций, что и в _Perspective_. Поэтому их невозможно установить одновременно.


### <span class="section-num">1.3</span> Workgroups 2 {#workgroups-2}

-   Репозиторий: <https://github.com/pashinin/workgroups2>
-   По функциям пакет аналогичен _Perspective_.


### <span class="section-num">1.4</span> eyebrowse {#eyebrowse}

-   Репозиторий: <https://github.com/wasamasa/eyebrowse>
-   Поддерживает структуру окон, но не списки буферов.


### <span class="section-num">1.5</span> wconf {#wconf}

-   Репозиторий: <https://github.com/ilohmar/wconf>
-   Поддерживает структуру окон, но не списки буферов.


### <span class="section-num">1.6</span> ElScreen {#elscreen}

-   Репозиторий: <https://github.com/knu/elscreen>
-   Поддерживает структуру окон, но не списки буферов.
-   Скорее всего не поддерживается.


### <span class="section-num">1.7</span> Burly {#burly}

-   Репозиторий: <https://github.com/alphapapa/burly.el>
-   Только сохранение конфигураций окон и фреймов с использованием закладок (bookmarks) Emacs.


### <span class="section-num">1.8</span> Bufler.el {#bufler-dot-el}

-   Репозиторий: <https://github.com/alphapapa/bufler.el>
-   Группирует буферы на основе правил группировки.
-   Рабочие области создаются динамически.
-   Состояние не сохраняется.
-   Для сохранения состояния используется _Burly_.


### <span class="section-num">1.9</span> Tabspaces {#tabspaces}

-   Репозиторий: <https://github.com/mclear-tools/tabspaces>
-   Использует `tab-bar.el` и `project.el` для создания изолированных от буфера рабочих пространств (_пространств вкладок_).


### <span class="section-num">1.10</span> IBuffer {#ibuffer}

-   Информация: <https://www.emacswiki.org/emacs/IbufferMode>
-   В составе Emacs начиная с версии 22.
-   Замена встроенной команды `list-buffer`.
-   Позволяет программно группировать буферы.
