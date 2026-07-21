---
title: "Заголовки безопасности HTTP"
author: ["Dmitry S. Kulyabov"]
date: 2026-07-20T18:02:00+03:00
lastmod: 2026-07-20T21:06:00+03:00
tags: ["security", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "http-security-headers"
---

Заголовки безопасности HTTP.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Типы проблем безопасности {#типы-проблем-безопасности}

-   Отсутствие или неправильная настройка HTTP-заголовков безопасности создаёт конкретные векторы атак.

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Таблица рисков
</div>

| Заголовок                 | Последствие отсутствия               | Последствие неправильного наличия                     |
|---------------------------|--------------------------------------|-------------------------------------------------------|
| `X-Frame-Options`         | Кликджекинг                          | Блокировка легитимных фреймов или слабая защита       |
| `X-Content-Type-Options`  | XSS через загрузку файлов            | Обычно безопасен                                      |
| `X-XSS-Protection`        | Снижение защиты для старых броузеров | Может вызвать блокировку страниц                      |
| `HSTS`                    | SSL-стриппинг                        | Недостаточное время жизни, проблемы с откатом         |
| `CSP`                     | XSS-атаки всех видов                 | Сломанный сайт или бесполезная политика               |
| `Referrer-Policy`         | Утечка приватных данных в URL        | Сломанная аналитика или передача слишком много данных |
| `Server` / `X-Powered-By` | Безопасно                            | Раскрытие информации о версиях                        |


### <span class="section-num">1.1</span> `X-Frame-Options` {#x-frame-options}


#### <span class="section-num">1.1.1</span> Отсутствие {#отсутствие}

-   Сайт становится уязвимым к кликджекингу (clickjacking).
-   Злоумышленник встраивает вашу страницу в `<iframe>` на своём сайте и накладывает поверх неё прозрачные элементы.
-   Пользователь думает, что кликает по кнопке на сайте злоумышленника, а на самом деле взаимодействует с вашим сайтом (например, переводит деньги, меняет пароль).
-   Без этого заголовка броузер не запрещает встраивание в фреймы.


#### <span class="section-num">1.1.2</span> Наличие {#наличие}

-   `X-Frame-Options: ALLOW-FROM https://bad-site.com` --- устаревший и плохо поддерживаемый параметр.
-   Если установлено `DENY` --- можно случайно заблокировать легитимные встраивания (например, виджеты на партнёрских сайтах).
-   Если `SAMEORIGIN` --- не защищает от атак через поддомены (если они скомпрометированы).


### <span class="section-num">1.2</span> `X-Content-Type-Options` {#x-content-type-options}


#### <span class="section-num">1.2.1</span> Отсутствие {#отсутствие}

-   Броузер может выполнять MIME-сниффинг (автоопределение типа содержимого).
-   Если злоумышленник загрузит на ваш сервер файл с расширением `.jpg`, но с содержимым HTML/JavaScript, броузер может распознать его как скрипт и выполнить в контексте вашего домена.
-   Это приводит к XSS-атакам через загрузку файлов (например, в аватарках).


#### <span class="section-num">1.2.2</span> Наличие {#наличие}

-   Проблем нет, если установлено `nosniff`.
-   Это строгое требование доверять заголовку `Content-Type`, что полностью предотвращает сниффинг.


### <span class="section-num">1.3</span> `X-XSS-Protection` {#x-xss-protection}


#### <span class="section-num">1.3.1</span> Отсутствие {#отсутствие}

-   В старых броузерах (Internet Explorer, Safari, Chrome до версии 78) была встроенная защита от отражённого XSS.
-   Если её отключить или не установить заголовок, броузер может не включить эту защиту.
-   Однако в современных броузерах этот заголовок устарел и игнорируется, поэтому основной риск --- для устаревших клиентов.


#### <span class="section-num">1.3.2</span> Наличие {#наличие}

-   `X-XSS-Protection: 0` --- отключает защиту, что плохо.
-   `X-XSS-Protection: 1; mode=block` --- включает защиту с блокировкой страницы.


#### <span class="section-num">1.3.3</span> Проблема {#проблема}

-   Сам механизм защиты может создавать уязвимости (например, DOM-based XSS с использованием `mode=block`), поэтому современные рекомендации советуют удалить этот заголовок и полагаться на CSP.
-   Но в корпоративных средах со старыми броузерами его временно оставляют.


### <span class="section-num">1.4</span> `Strict-Transport-Security` (HSTS) {#strict-transport-security--hsts}


#### <span class="section-num">1.4.1</span> Отсутствие {#отсутствие}

-   Пользователь может быть атакован через SSL-стриппинг (злоумышленник перехватывает первый HTTP-запрос и перенаправляет на поддельный сайт без HTTPS).
-   Даже если у вас включён HTTPS, первый запрос может быть по HTTP, и атакующий может вмешаться до переадресации.
-   Без HSTS броузер не запоминает, что к вашему сайту нужно ходить только по HTTPS.


#### <span class="section-num">1.4.2</span> Наличие {#наличие}

-   Слишком короткий `max-age` (например, 5 минут) не даёт достаточной защиты.
-   Если не включён `includeSubDomains`, то поддомены остаются незащищёнными.
-   Ошибка в настройке может привести к тому, что броузер будет отказываться подключаться к сайту по HTTP, что сломает доступ для пользователей, если у них нет HTTPS.
-   Если вы установите `preload` и отправите домен в список HSTS preload, вы не сможете легко отказаться от HTTPS в будущем.


### <span class="section-num">1.5</span> `Content-Security-Policy` (CSP) {#content-security-policy--csp}


#### <span class="section-num">1.5.1</span> Общая информация {#общая-информация}

-   CSP --- это белый список для броузера.
-   Разрешает работать с ресурсами только из списка.
-   Для защиты от XSS-атак (межсайтовый скриптинг).
-   Даже если хакер внедрит свой скрипт на вашу страницу, броузер не выполнит его, потому что его нет в белом списке.


#### <span class="section-num">1.5.2</span> Отсутствие {#отсутствие}

-   Отсутствие CSP позволяет выполнять любой инлайн-скрипт и загружать ресурсы с любых источников.
-   Это делает сайт максимально уязвимым для XSS-атак любого типа (отражённых, хранимых, DOM-based).
-   Злоумышленник, внедривший скрипт, сможет украсть куки, сессии, данные форм и т.д.


#### <span class="section-num">1.5.3</span> Наличие {#наличие}

-   Слишком слабая политика (например, `default-src *` или `script-src 'unsafe-inline'`) почти не даёт защиты (эквивалентно отсутствию).
-   Если установить слишком строгую политику, то сайт перестаёт работать: не грузятся скрипты, стили, картинки, шрифты с CDN, блокируются виджеты, API. Это приводит к нарушению функционирования сайта, но не к уязвимости.
-   Неправильные директивы для `frame-ancestors` могут разрешить кликджекинг (если не используется `X-Frame-Options`).
-   Отсутствие `report-uri` или `report-to` мешает отслеживать нарушения и корректировать политику.


### <span class="section-num">1.6</span> `Referrer-Policy` {#referrer-policy}


#### <span class="section-num">1.6.1</span> Отсутствие {#отсутствие}

-   Броузер по умолчанию передаёт полный URL предыдущей страницы в заголовке `Referer`.
-   Это может раскрывать чувствительные данные в строке запроса (например, `?token`, `?sessionid`) при переходе на сторонние сайты.
-   Утечка таких данных может привести к компрометации сессий.


#### <span class="section-num">1.6.2</span> Наличие {#наличие}

-   Неправильная политика, например `no-referrer`, может сломать аналитику или логику, зависящую от источника перехода.
-   `unsafe-url` передаёт полный URL даже внутри сайта.
-   Рекомендуется `strict-origin-when-cross-origin` (передаёт только домен для кросс-доменов и полный для своих), это безопасно.


### <span class="section-num">1.7</span> `Server` и `X-Powered-By` {#server-и-x-powered-by}


#### <span class="section-num">1.7.1</span> Наличие {#наличие}

-   Раскрытие информации.
-   Заголовок `Server: Apache/2.4.54 (Ubuntu)` сообщает злоумышленнику точную версию веб-сервера и ОС.
-   Заголовок `X-Powered-By: PHP/8.1.2` раскрывает версию интерпретатора.
-   Это помогает атакующему подобрать известные эксплойты именно для версии сайта.


#### <span class="section-num">1.7.2</span> Отсутствие {#отсутствие}

-   Усложняет исследование сайта.
-   Однако их отсутствие не создаёт прямой уязвимости, но скрытие уменьшает поверхность атаки.


### <span class="section-num">1.8</span> Приоритеты безопасности {#приоритеты-безопасности}

-   Критично (высокий приоритет):
    -   Добавить `Strict-Transport-Security` (HSTS) на всех HTTPS-портах.
    -   Добавить `X-Content-Type-Options: nosniff` (защита от MIME-атак).
    -   Убрать `Server` и `X-Powered-By` (скрытие информации).

-   Важно (средний приоритет):
    -   Добавить `X-Frame-Options` (защита от кликджекинга).
    -   Добавить `Content-Security-Policy` (защита от XSS, но требует тонкой настройки, чтобы не сломать сайт).

-   Рекомендуется (низкий приоритет):
    -   `X-XSS-Protection` (устаревает в современных броузерах, но полезен как запасной вариант).
    -   `Referrer-Policy` (контроль конфиденциальности).


### <span class="section-num">1.9</span> Риски массового применения (через общий конфиг) {#риски-массового-применения--через-общий-конфиг}

-   Если применять одни и те же заголовки ко всем виртуальным хостам, возможны следующие проблемы:
    -   CSP для одного сайта может оказаться слишком строгим для другого (например, на одном используются внешние скрипты, а на другом --- нет).
    -   HSTS на поддоменах (`includeSubDomains`) может заставить все поддомены работать только по HTTPS, что может быть проблематично, если некоторые из них используют HTTP для внутренних целей.
    -   Referrer-Policy может повлиять на работу аналитических систем.


## <span class="section-num">2</span> Устранение недостатков {#устранение-недостатков}

-   Все проблемы решаются настройкой веб-сервера (Nginx, Apache, IIS).


### <span class="section-num">2.1</span> Добавить недостающие заголовки безопасности {#добавить-недостающие-заголовки-безопасности}

-   В зависимости от вашего веб-сервера, добавьте следующие директивы:

-   Для Nginx (в блоке `server`):
    ```nginx
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self';" always;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always; # ТОЛЬКО ДЛЯ HTTPS
    ```

-   Для Apache (в `.htaccess` или конфиге):
    ```apache
    Header always set X-XSS-Protection "1; mode=block"
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self';"
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" env=HTTPS
    ```


### <span class="section-num">2.2</span> Убрать информативные заголовки (`Server`, `X-Powered-By`) {#убрать-информативные-заголовки--server-x-powered-by}

-   Эти заголовки раскрывают версию ПО, что помогает злоумышленникам.

-   Nginx: В `nginx.conf` в секции `http` добавьте `server_tokens off;`.
-   Apache: Включите `ServerSignature Off` и `ServerTokens Prod`.
-   Убрать `X-Powered-By`:
    -   PHP: `expose_php = Off` в `php.ini`.
    -   Python/Flask: Используйте `app.config['PROPAGATE_EXCEPTIONS'] = True` или удалите заголовок в middleware.
    -   Java: Настройте `server.servlet.session.cookie` или используйте фильтр для удаления заголовка.


### <span class="section-num">2.3</span> Настройка CSP (Content-Security-Policy) {#настройка-csp--content-security-policy}


#### <span class="section-num">2.3.1</span> Пример работы {#пример-работы}

-   Пусть заголовок содержит: `default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; ...`

-   Это означает:
    -   `default-src 'self'` : все ресурсы по умолчанию грузить только со своего домена.
    -   `'unsafe-inline'` : разрешить выполнять скрипты и стили, написанные прямо в HTML.

-   Шаблон блокирует работу, если на сайте есть:
    -   Яндекс.Метрика или Google Analytics (скрипты грузятся с их серверов).
    -   Видео с YouTube или Vimeo (iframe).
    -   Шрифты Google Fonts (загружаются с `fonts.googleapis.com`).
    -   Картинки с внешних CDN.
    -   Виджеты или API (подключение к сторонним сервисам).

-   Например, броузер увидит попытку загрузить скрипт с `https://mc.yandex.ru` и заблокирует его, потому что в политике разрешен только `'self'` (свой хост).


#### <span class="section-num">2.3.2</span> Настройка под сайт {#настройка-под-сайт}

-   Необходимо предварительно исследовать работу сайта.

<!--list-separator-->

1.  Режим отчетов (Report-Only)

    -   В Apache используется `Header set Content-Security-Policy-Report-Only`.
    -   В этом режиме броузер не блокирует ресурсы, а пишет в отлабочную консоль ошибки.

    <!--listend-->

    ```apache
    # Включаем безопасный режим наблюдения, чтобы ничего не сломать
    Header always set Content-Security-Policy-Report-Only "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self';"
    ```

<!--list-separator-->

2.  Консоль разработчика

    -   Откройте сайт.
    -   Нажмите F12 в броузере (Chrome/Firefox), перейдите на вкладку Console (Консоль).

    Вы увидите красные ошибки типа:

    > Refused to load the script '<https://mc.yandex.ru/metrika/tag.js>' because it violates the following Content Security Policy directive: "script-src 'self' 'unsafe-inline'".

<!--list-separator-->

3.  Правка шаблона

    -   Глядя на ошибки, добавляйте недостающие домены в нужные директивы.
        -   Шаблон:
            `script-src 'self' 'unsafe-inline';`

        -   Видим ошибку с Яндекс.Метрикой:
            -   Добавляем `https://mc.yandex.ru` `https://yandex.ru`:
                `script-src 'self' 'unsafe-inline' https://mc.yandex.ru https://yandex.ru;`

        -   Видим ошибку с Google Fonts (стили и шрифты):
            -   Добавляем в `style-src` и `font-src`:
                `style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;`
                `font-src 'self' https://fonts.gstatic.com;`

        -   Видим ошибку с загрузкой картинок с внешнего CDN:
            -   Добавляем в `img-src`:
                `img-src 'self' data: https://cdn.myhost.ru;`

<!--list-separator-->

4.  Включайте политику

    -   Когда в режиме `Report-Only` консоль чиста, меняете название заголовка с `Content-Security-Policy-Report-Only` на `Content-Security-Policy` (убираете `-Report-Only`).
    -   Теперь защита работает.


### <span class="section-num">2.4</span> Конфигурационный файл {#конфигурационный-файл}


#### <span class="section-num">2.4.1</span> Apache {#apache}

<!--list-separator-->

1.  Общий конфигурационный файл

    -   Стандартные каталоги Apache для хранения общих конфигураций:

    | Дистрибутив        | Путь для общих конфигураций                            |
    |--------------------|--------------------------------------------------------|
    | Debian/Ubuntu      | `/etc/apache2/conf-available/`, `/etc/apache2/conf.d/` |
    | RHEL/CentOS/Fedora | `/etc/httpd/conf.d/`                                   |

<!--list-separator-->

2.  Способ 1: Создать файл в conf.d / conf-available

    -   Создайте файл с заголовками безопасности
        -   Debian/Ubuntu:
            ```shell
            sudo touch /etc/apache2/conf-available/security-headers.conf
            ```

        -   RHEL/CentOS:
            ```shell
            sudo touch /etc/httpd/conf.d/security-headers.conf
            ```

    -   Добавьте нужные заголовки:
        ```apache
        # security-headers.conf — общие заголовки безопасности для всех виртуальных хостов

        # Защита от кликджекинга
        Header always set X-Frame-Options "SAMEORIGIN"

        # Защита от MIME-атак
        Header always set X-Content-Type-Options "nosniff"

        # Защита от XSS (для старых браузеров)
        Header always set X-XSS-Protection "1; mode=block"

        # Контроль Referer
        Header always set Referrer-Policy "strict-origin-when-cross-origin"

        # HSTS — ТОЛЬКО ДЛЯ HTTPS (проверьте, что у вас включён HTTPS)
        Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"

        # CSP (настройте под свой сайт)
        Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self';"

        # Скрываем версию сервера (глобально, в httpd.conf/apache2.conf)
        ServerTokens Prod
        ServerSignature Off
        ```

    -   Подключите файл
        -   Debian/Ubuntu
            ```shell
            sudo a2enconf security-headers
            sudo systemctl reload apache2
            ```

            -   Или вручную добавьте в `/etc/apache2/apache2.conf`:
                ```apache
                IncludeOptional /etc/apache2/conf-available/security-headers.conf
                ```

        -   RHEL/CentOS
            -   Файлы в `conf.d/` подключаются автоматически.
            -   Перезагрузите Apache:
                ```shell
                sudo systemctl reload httpd
                ```

<!--list-separator-->

3.  Способ 2: Использовать .htaccess

    -   Если включена обработка `.htaccess`, можно разместить общие заголовки в корневом `.htaccess` сайта.
    -   `.htaccess` снижает производительность, так как Apache проверяет его при каждом запросе.
    -   Для продакшена лучше использовать основной конфиг.

    -   Файл: `/var/www/html/.htaccess` или `/путь_к_сайту/.htaccess`
        ```apache
        # .htaccess с общими заголовками безопасности
        Header always set X-Frame-Options "SAMEORIGIN"
        Header always set X-Content-Type-Options "nosniff"
        Header always set X-XSS-Protection "1; mode=block"
        Header always set Referrer-Policy "strict-origin-when-cross-origin"
        Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
        ```

<!--list-separator-->

4.  Способ 3: Подключить общий файл в каждом виртуальном хосте

    -   Если нужно, чтобы разные виртуальные хосты использовали разные общие файлы:
        ```apache
        <VirtualHost *:443>
            ServerName site1.example.com
            DocumentRoot /var/www/site1

            # Подключаем общий файл с заголовками
            Include /etc/apache2/conf-available/security-headers.conf

            # Дополнительные настройки для этого хоста
            SSLEngine on
            SSLCertificateFile /path/to/cert.pem
        </VirtualHost>
        ```

<!--list-separator-->

5.  Проверка конфигурации

    -   Проверьте синтаксис конфигурации:
        ```shell
        sudo apachectl configtest
        # или
        sudo httpd -t
        ```

    -   Проверьте заголовки в ответе сервера:
        ```shell
        curl -I http://ваш-сервер:порт
        curl -I https://ваш-сервер:443 -k
        ```

        -   В выводе должны появиться все добавленные заголовки.

    -   Проверьте, что конфигурация загружена:
        ```shell
        # Debian/Ubuntu
        sudo apache2ctl -t -D DUMP_CONFIG | grep -i "security-headers"

        # RHEL/CentOS
        sudo httpd -t -D DUMP_CONFIG | grep -i "security-headers"
        ```


## <span class="section-num">3</span> Проверка {#проверка}


### <span class="section-num">3.1</span> Ручная проверка через командную строку {#ручная-проверка-через-командную-строку}

-   Используйте `curl` для каждого IP и порта, чтобы увидеть заголовки ответа:
    ```shell
    # Для HTTP
    curl -I http://hostname:80

    # Для HTTPS
    curl -I https://hostname:443 -k
    ```

-   Ожидаемый результат:
    ```text
    HTTP/1.1 200 OK
    Server: nginx                         # <--- Если оставили, то скрыли версию
    X-XSS-Protection: 1; mode=block
    X-Content-Type-Options: nosniff
    X-Frame-Options: SAMEORIGIN
    Referrer-Policy: strict-origin-when-cross-origin
    Content-Security-Policy: default-src 'self'; ...
    Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
    ```


### <span class="section-num">3.2</span> Использование онлайн-инструментов {#использование-онлайн-инструментов}


#### <span class="section-num">3.2.1</span> SecurityHeaders.com {#securityheaders-dot-com}

-   Сайт блокирует доступ из России.
-   Перейдите на сайт SecurityHeaders.com.
-   Введите URL вашего сервера.
-   Он выдаст оценку (A+, A, B и т.д.) и покажет, какие заголовки все еще отсутствуют.


### <span class="section-num">3.3</span> Расширения для броузера {#расширения-для-броузера}


#### <span class="section-num">3.3.1</span> Web Security Headers Checker {#web-security-headers-checker}

-   Расширение для Chrome, которое сканирует заголовки и выдает оценку от A+ до F прямо на панели инструментов.
-   Chrome: <https://chromewebstore.google.com/detail/security-headers/oahaipcejmlamohcchffgpcnfbidaklj>


### <span class="section-num">3.4</span> Скрипт автоматической проверки {#скрипт-автоматической-проверки}

-   bash-скрипт для проверки всех IP и портов:
    ```shell
    #!/bin/bash
    hosts=("host:80" "host:443" "host:3128")
    for host in "${hosts[@]}"; do
        echo "Checking $host"
        curl -s -I "http://$host" | grep -E "X-XSS-Protection|X-Content-Type-Options|X-Frame-Options|Referrer-Policy|Content-Security-Policy|Strict-Transport-Security|Server|X-Powered-By"
        echo "---"
    done
    ```
