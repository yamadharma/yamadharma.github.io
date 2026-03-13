---
title: "Firefox. Расширения"
author: ["Dmitry S. Kulyabov"]
date: 2006-12-24T18:10:00+03:00
lastmod: 2024-10-10T16:28:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "firefox-extention"
---

Расширения Firefox, которые я использую.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Актуальный список {#актуальный-список}


### <span class="section-num">1.1</span> Блокировщики {#блокировщики}


#### <span class="section-num">1.1.1</span> Ghostery {#ghostery}

-   Сайт: <http://www.ghostery.com/>
-   Firefox: <https://addons.mozilla.org/ru/firefox/addon/ghostery/>.
-   Блокировка рекламы.
-   Защита конфиденциальности.


#### <span class="section-num">1.1.2</span> AdGuard Addblocker {#adguard-addblocker}

-   Сайт: <https://adguard.info>.
-   Репозиторий: <https://github.com/AdguardTeam/AdguardBrowserExtension>
-   Firefox: <https://addons.mozilla.org/ru/firefox/addon/adguard-adblocker/>
-   Лицензия:  GPL-3.0.
-   Блокирует рекламу, включая:
    -   видеорекламу (в том числе на YouTube);
    -   Rich media (анимированную рекламу);
    -   нежелательные всплывающие окна;
    -   баннеры и текстовые объявления.


### <span class="section-num">1.2</span> Закладки {#закладки}


#### <span class="section-num">1.2.1</span> Bukubrow {#bukubrow}

-   [Менеджер закладок buku]({{< relref "2024-06-22-buku-bookmark-manager" >}})
-   Репозиторий: <https://github.com/samhh/bukubrow-webext>
-   Firefox: <https://addons.mozilla.org/en-US/firefox/addon/bukubrow/>
-   Chrome/Chromium: <https://chrome.google.com/webstore/detail/bukubrow/ghniladkapjacfajiooekgkfopkjblpn>
-   Переведён в неподдерживаемое состояние <span class="timestamp-wrapper"><span class="timestamp">[2024-09-07 Сб]</span></span>.
-   Предполагается замена на использование лаунчера (см. [Лаунчеры]({{< relref "2024-08-11-launcher" >}})).


### <span class="section-num">1.3</span> Навигация {#навигация}


#### <span class="section-num">1.3.1</span> Vimium C {#vimium-c}

-   [Vim. Клавиатура. Броузеры]({{< relref "2023-08-19-vim-keyboard-browsers" >}})
-   Навигация в стиле Vim.
-   Репозиторий: <https://github.com/gdh1995/vimium-c>
-   Firefox: <https://addons.mozilla.org/ru/firefox/addon/vimium-c/>


### <span class="section-num">1.4</span> Пароли {#пароли}


#### <span class="section-num">1.4.1</span> Browserpass {#browserpass}

-   [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})
-   Работа с паролями через парольный менеджер _pass_.
-   Репозиторий: <https://github.com/browserpass/browserpass-extension>
-   Firefox: <https://github.com/browserpass/browserpass-extension>


#### <span class="section-num">1.4.2</span> Gopass Bridge {#gopass-bridge}

-   [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})
-   Работа с паролями через парольный менеджер _gopass_.
-   Репозиторий: <https://github.com/gopasspw/gopassbridge>
-   Firefox: <https://addons.mozilla.org/en-US/firefox/addon/gopass-bridge/>


### <span class="section-num">1.5</span> Переводчики {#переводчики}


#### <span class="section-num">1.5.1</span> TWP - Translate Web Pages {#twp-translate-web-pages}

-   Перевод страницы с помощью Google или Яндекс.
-   Репозиторий: <https://github.com/FilipePS/Traduzir-paginas-web>
-   Firefox: <https://addons.mozilla.org/ru/firefox/addon/traduzir-paginas-web/>


#### <span class="section-num">1.5.2</span> voice-over-translation {#voice-over-translation}

-   Перевод видео на русский, английский, казахский.
-   Для перевода использует сервис [Yandex.Translate](https://translate.yandex.ru/).
-   Использует фреймворк _Tampermonkey_.
-   Репозиторий: <https://github.com/ilyhalight/voice-over-translation>
-   Сам скрипт: <https://raw.githubusercontent.com/ilyhalight/voice-over-translation/master/dist/vot.user.js>


### <span class="section-num">1.6</span> Фреймворки {#фреймворки}


#### <span class="section-num">1.6.1</span> Tampermonkey {#tampermonkey}

-   Позволяет запускать пользовательские скрипты на JavaScript.
-   Сайт: <https://www.tampermonkey.net/>
-   Firefox: <https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/>


## <span class="section-num">2</span> Архив {#архив}


### <span class="section-num">2.1</span> Usability {#usability}

-   [NoSquint](http://urandom.ca/nosquint/): запоминает увеличение страницы.


### <span class="section-num">2.2</span> Блокировщики {#блокировщики}

-   [Adblock Filterset.G Updater](http://www.pierceive.com/): обновление фильтров для Adblock Plus.
-   [Adblock Plus](http://adblockplus.org/): банерорезка.


### <span class="section-num">2.3</span> Загрузки {#загрузки}

-   [FlashGot](http://flashgot.net/): интерфейс к менеджерам загрузки.
-   [PDF Download](http://www.pdfdownload.org/): не загружает сразу PDF для просмотра, а предлагает некий набор действий.
-   [VideoDownloader](http://videodownloader.net/): загрузка разных медийных материалов со страницы.
-   [UnPlug](http://www.compunach.co.nr/unplug/): то же, что и предыдущее расширение. Поставил для пробы.
-   [CacheViewer](http://park2.wakwak.com/%7Ebenki/cacheviewer.html) (<https://addons.mozilla.org/firefox/2489>): работа с кэшем броузера. Есть возможность поиска.


### <span class="section-num">2.4</span> Закладки {#закладки}

-   [Foxmarks Bookmark Synchronizer](http://www.foxmarks.com/): синхронизирует закладки с сервером sync.foxcloud.com. Особенно удобно, когда работаешь в нескольких местах.
-   [Enhanced Bookmark Search](http://www.google.com/search?q=Firefox%20Enhanced%20Bookmark%20Search)


### <span class="section-num">2.5</span> Красивости {#красивости}

-   [CuteMenus - Crystal SVG](http://www.cutemenuproject.com/): красивости для оформления меню.
-   [Fission](https://addons.mozilla.org/en-US/firefox/addon/1951): Индикатор процесса загрузки страницы в панели адреса.


### <span class="section-num">2.6</span> Работа с изображениями {#работа-с-изображениями}

-   [Image Zoom](http://imagezoom.yellowgorilla.net/): удобное изменение масштаба изображения.
-   [ImgLikeOpera](http://imglikeopera.mozdev.org/): позволяет не загружать изображения (стоит, но я не пользуюсь).


### <span class="section-num">2.7</span> Разное {#разное}

-   [Deepest Sender](http://deepestsender.mozdev.org/): blog-клиент.
-   [FoxyTunes](http://www.foxytunes.com/): управление проигрыванием музыки.
-   [ScrapBook](http://amb.vis.ne.jp/mozilla/scrapbook/): позволяет сохранять страницы целиком и каталогизировать их.
-   [Password Exporter](http://passwordexporter.fligtar.com/)
-   [Enhanced History Manager](http://www.google.com/search?q=Firefox%20Enhanced%20History%20Manager)
-   [Fasterfox](http://fasterfox.mozdev.org/): должно ускорять работу броузера. Не знаю, работает или нет.
-   [InFormEnter](http://informenter.mozdev.org/): работа с формами.


### <span class="section-num">2.8</span> Улучшение интерфейса {#улучшение-интерфейса}

-   [All-in-One Sidebar](http://firefox.exxile.net/aios/): удобная боковая панель.
-   [MR Tech Local Install](http://www.mrtech.com/extensions/local_install/): улучшения для работы с расширениями.
-   [Tab Mix Plus](http://tmp.garyr.net/): работа с вкладками.


### <span class="section-num">2.9</span> Языковые инструменты {#языковые-инструменты}

-   [Russian hot keys bugfix](https://addons.mozilla.org/firefox/3529/): позволяет работать клавишным сочетаниям в русском регистре.
-   [Russian spell dictionary](https://addons.mozilla.org/firefox/3703/): собственно русский словарь для проверки орфографии.
-   [Dictionary Switcher](http://en.design-noir.de/mozilla/dictionary-switcher/): переключатель словарей.[[<http://en.design-noir.de/mozilla/dictionary-switcher-tb/>][]]
-   [Human URL](http://www.google.com/search?q=Firefox%20Human%20URL): вместо символов %XX пишутся нормальные буквы.
