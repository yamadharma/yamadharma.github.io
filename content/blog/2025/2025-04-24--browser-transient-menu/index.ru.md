---
title: "Броузер. Реализация transient menu"
author: ["Dmitry S. Kulyabov"]
date: 2025-04-24T16:54:00+03:00
lastmod: 2025-04-24T17:31:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "browser-transient-menu"
---

Броузер. Реализация transient menu (см. [Интерфейс. Transient menu]({{< relref "2025-04-24--transient-menu-interface" >}})).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> ShortcutKey2URL {#shortcutkey2url}

-   Клавиатурное сочетание для вызова меню по умолчанию: `Ctrl+.`
-   Проверьте, что оно не конфликтует с другими расширениями.
-   Можно изменить в настройках.


### <span class="section-num">1.1</span> Firefox {#firefox}

-   Репозиторий: <https://github.com/onozaty/firefox-shortcutkey2url>
-   Add-on: <https://addons.mozilla.org/en-US/firefox/addon/shortcutkey2url/>


### <span class="section-num">1.2</span> Chrome {#chrome}

-   Репозиторий: <https://github.com/onozaty/chrome-shortcutkey2url>
-   Add-on: <https://chrome.google.com/webstore/detail/shortcutkey2url-for-chrom/hfohmffbfcobmhfgpkbcjjaijmfplcdg>
