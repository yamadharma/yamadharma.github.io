---
title: "Chromium. Расширения"
author: ["Dmitry S. Kulyabov"]
date: 2026-05-27T09:11:00+03:00
lastmod: 2026-07-12T19:01:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "chromium-extensions"
---

Chromium. Расширения, которые я использую.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Актуальный список {#актуальный-список}


### <span class="section-num">1.1</span> Блокировщики {#блокировщики}


#### <span class="section-num">1.1.1</span> Ghostery {#ghostery}

-   Сайт: <http://www.ghostery.com/>
-   Firefox: <https://addons.mozilla.org/ru/firefox/addon/ghostery/>.
-   Chrome: <https://chromewebstore.google.com/detail/ghostery-adblocker-for-pr/mlomiejdfkolichcflejclcbmpeaniij>.
-   Блокировка рекламы.
-   Защита конфиденциальности.


#### <span class="section-num">1.1.2</span> AdGuard Addblocker {#adguard-addblocker}

-   Сайт: <https://adguard.info>.
-   Репозиторий: <https://github.com/AdguardTeam/AdguardBrowserExtension>
-   Firefox: <https://addons.mozilla.org/ru/firefox/addon/adguard-adblocker/>
-   Chrome: <https://chromewebstore.google.com/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg>
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
-   Chrome: <https://chrome.google.com/webstore/detail/vimium-c-all-by-keyboard/hfjbmagddngcpeloejdejnfgbamkjaeg>


### <span class="section-num">1.4</span> Пароли {#пароли}


#### <span class="section-num">1.4.1</span> Browserpass {#browserpass}

-   [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})
-   Работа с паролями через парольный менеджер _pass_.
-   Репозиторий: <https://github.com/browserpass/browserpass-extension>
-   Firefox: <https://github.com/browserpass/browserpass-extension>
-   Chrome: <https://chromewebstore.google.com/detail/browserpass/naepdomgkenhinolocfifgehidddafch>


#### <span class="section-num">1.4.2</span> Gopass Bridge {#gopass-bridge}

-   [Менеджер паролей pass]({{< relref "2021-04-28-password-manager-pass" >}})
-   Работа с паролями через парольный менеджер _gopass_.
-   Репозиторий: <https://github.com/gopasspw/gopassbridge>
-   Firefox: <https://addons.mozilla.org/en-US/firefox/addon/gopass-bridge/>
-   Chrome: <https://chromewebstore.google.com/detail/gopass-bridge/kkhfnlkhiapbiehimabddjbimfaijdhk>


### <span class="section-num">1.5</span> Чтение {#чтение}


#### <span class="section-num">1.5.1</span> Wallabager {#wallabager}

-   [Отложенное чтение. Wallabag]({{< relref "2024-12-05-read-it-later-wallabag" >}})
-   Репозиторий: <https://github.com/wallabag/wallabagger>
-   Firefox: <https://addons.mozilla.org/en-US/firefox/addon/wallabagger/>
-   Chrome: <https://chromewebstore.google.com/detail/wallabagger/gbmgphmejlcoihgedabhgjdkcahacjlj>


### <span class="section-num">1.6</span> Преобразование {#преобразование}


#### <span class="section-num">1.6.1</span> Copy as Org-Mode {#copy-as-org-mode}

-   Преобразует в формат org.
-   Репозиторий: <https://github.com/yibie/Copy-as-org-mode-chrome>

<!--list-separator-->

1.  Как использовать

    -   Запускается из контекстного меню, вызываемого щелчком правой кнопки мыши.

    <div class="table-caption">
      <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
      Выполняемые операции
    </div>

    | Пункт меню                                                  | Действие                                                               | Выход                                                       |
    |-------------------------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------|
    | Копировать выделенный фрагмент в режиме Org-Mode            | Выделите текст на странице, щелкните правой кнопкой мыши → скопировать | Текст, отформатированный в режиме Org-mode, в буфере обмена |
    | Сохранить страницу как Org-Mode                             | Щелкните правой кнопкой мыши в любом месте страницы.                   | `.org` файл загружен                                        |
    | Сохранить страницу как Org-Mode (с изображениями)           | Щелкните правой кнопкой мыши в любом месте страницы.                   | `.org` файл + все изображения сохранены в папку             |
    | Скопировать ссылку в режиме Org-Mode                        | Щелкните правой кнопкой мыши по гиперссылке                            | `[[url][text]]` в буфере обмена                             |
    | Скопируйте URL страницы в качестве ссылки в режиме Org-Mode | Щелкните правой кнопкой мыши по фону страницы.                         | `[[url][title]]` в буфере обмена                            |

    -   Для функции «Копировать выделенный фрагмент» также доступна комбинация клавиш `Ctrl+Alt+O`.

<!--list-separator-->

2.  Настройки

    -   Откройте страницу настроек расширения (щелкните правой кнопкой мыши значок расширения → Параметры).
        -   Язык для транскрипции и извлечения.
            -   Код языка BCP 47 (например `zh-Hans`, , `en`, `fr`), используемый YouTube для выбора дорожек субтитров и Defuddle для установки `Accept-Language` заголовков для экстракторов. Если пусто, то определяется автоматически.
        -   Размер отступа списка, стиль маркированного списка, стиль кода.
            -   Настройка синтаксиса вывода Org-mode.
        -   Формат ссылки.
            -   Шаблон для ссылок на исходные страницы (`%title%`, `%url%`, `%date%`).
        -   Стиль уведомления.
            -   Всплывающее уведомление на странице или системное уведомление.
        -   Префикс пути к изображению.
            -   Как пути к изображениям записываются в файле Org (например, `./images/`).

<!--list-separator-->

3.  Сохранение страницы с изображениями

    -   Опция «Сохранить страницу как Org-Mode (с изображениями)» загружает все изображения страницы в папку рядом с файлом Org:
        -   Щелкните правой кнопкой мыши → Сохранить страницу как Org-Mode (с изображениями).
        -   Откроется новая вкладка → нажмите «Выбрать папку и сохранить».
        -   Выберите любую папку (например, `~/Documents/Notes`).
        -   Предоставьте браузеру разрешение на редактирование файла, когда он запросит его.

<!--list-separator-->

4.  Установка

    -   Скачать можно `copy-as-org-mode-v<version>.zip` на [странице релизов](https://github.com/yibie/Copy-as-org-mode-chrome/releases).
    -   Распакуйте архив.
    -   Откройте Chrome → перейдите по ссылке `chrome://extensions` .
    -   Включите режим разработчика  (переключатель в правом верхнем углу).
    -   Нажмите «Загрузить распакованное» → выберите папку.

    -   Или клонируйте репозиторий и выполните сборку:
        ```shell
        git clone https://github.com/yibie/Copy-as-org-mode-chrome
        cd Copy-as-org-mode-chrome
        npm install
        npm run build
        ```

    -   Затем загрузите каталог `dist/` как распакованное расширение.
