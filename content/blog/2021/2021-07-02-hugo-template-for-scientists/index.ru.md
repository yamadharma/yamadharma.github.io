---
title: "Hugo. Шаблон для научных работников"
author: ["Dmitry S. Kulyabov"]
date: 2021-07-02T15:02:00+03:00
lastmod: 2026-01-21T21:57:00+03:00
tags: ["hugo", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "hugo-template-for-scientists"
---

-   Тема _Hugo Academic CV Theme_.
-   Бывшая тема _Wowchemy_.
-   Бывшая тема _Academic_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Информация {#информация}

-   Сайт: <https://hugoblox.com/>
-   Репозиторий темы: <https://github.com/HugoBlox/theme-academic-cv>
-   Репозитории вариантов тем: <https://github.com/HugoBlox>
-   Репозиторий модулей тем: <https://github.com/HugoBlox/kit>


### <span class="section-num">1.1</span> На основе bootstrap {#на-основе-bootstrap}

-   До 2023 года включительно.
-   Документация по сайту на bootstrap: <https://bootstrap.hugoblox.com/>


### <span class="section-num">1.2</span> На основе tailwind {#на-основе-tailwind}

-   С 2024 года.
-   Документация: <https://docs.hugoblox.com/>


## <span class="section-num">2</span> Обновление шаблонов Wowchemy {#обновление-шаблонов-wowchemy}

-   [Hugo. HugoBlox. Обновление шаблонов]({{< relref "2026-01-21--hugo-hugoblox-update-template" >}})


## <span class="section-num">3</span> Устранение проблем {#устранение-проблем}


### <span class="section-num">3.1</span> Ошибка: нарушение безопасности {#ошибка-нарушение-безопасности}

-   После обновления до 0.91 возникла следующая ошибка при генерации сайта:
    ```shell
    hugo v0.91.0+extended linux/amd64 BuildDate=2021-12-22T12:45:46+03:00 VendorInfo=Gentoo
    ERROR render of "page" failed: execute of template failed: template: project/single.html:5:3: executing "project/single.html" at <partial "site_head" .>: error calling partial: "/home/dharma/work/blog/git/resources/hugo_cache/modules/filecache/modules/pkg/mod/github.com/wowchemy/wowchemy-hugo-modules/wowchemy/v5@v5.0.0-20211221220555-87f69f8c265e/layouts/partials/site_head.html:207:13": execute of template failed: template: partials/site_head.html:207:13: executing "partials/site_head.html" at <getenv "WC_POST_CSS">: error calling getenv: access denied: "WC_POST_CSS" is not whitelisted in policy "security.funcs.getenv"; the current security configuration is:

    [security]
      enableInlineShortcodes = false
      [security.exec]
        allow = ['^dart-sass-embedded$', '^go$', '^npx$', '^postcss$']
        osEnv = ['(?i)^(PATH|PATHEXT|APPDATA|TMP|TEMP|TERM)$']

      [security.funcs]
        getenv = ['^HUGO_']

      [security.http]
        methods = ['(?i)GET|POST']
        urls = ['.*']
    ```
-   Необходимо добавить строчки в белый список для переменной среды `WC_POST_CSS`.
-   Для `config/_default/config.toml` (в формате TOML):
    ```toml
    [security.funcs]
    getenv = [ "^HUGO_", "^WC_",]
    ```
-   Для `config/_default/config.yaml` (в формате YAML):
    ```yaml
    security:
      funcs:
        getenv:
    ​      - ^HUGO_
    ​      - ^WC_
    ```


## <span class="section-num">4</span> Элементы шаблонов Wowchemy {#элементы-шаблонов-wowchemy}


## <span class="section-num">5</span> Типы контента Wowchemy {#типы-контента-wowchemy}

-   [Hugo. Wowchemy. Book]({{< relref "2022-11-22-hugo-wowchemy-book" >}})


## <span class="section-num">6</span> Полезности {#полезности}

-   [Hugo. Шаблон для научных работников. Полезные скрипты]({{< relref "2025-01-08--hugo-template-for-scientists-scripts" >}})
-   [Hugo. Шаблон для научных работников. Библиография]({{< relref "2025-01-08--hugo-template-for-scientists-bibliography" >}})
