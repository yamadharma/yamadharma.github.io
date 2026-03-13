---
categories:
  - sysadmin
date: 2015-04-20T13:17:32+00:00
lang: ru
slug: octopus-multilingual
subtitle: Поддержка многоязычности в Jekyll на основе Octopress Multilingual
tags:
  - jekyll
title: Поддержка многоязычности
projects: ["misc-utils"]
---


Добавим в конфигурационный файл (`_config.yml`):

```yaml
gems:
  - octopress-multilingual
  - octopress-linkblog
```

Также зададим язык по-умолчанию:

```yaml
lang: ru
```

<!--more-->

## Язык для постов ##

Добавим язык  в заголовок шаблонов:

```yaml
lang: ru
```

## Конфигурация для разных языков ##

В каталоге `_data` создадим конфигурационные файлы вида
`lang_[language_code].yml`:

```yaml
_data
  lang_en.yml
  lang_ru.yml
```

Примерное их содержание:

```yaml
# lang_en.yml
title: English title

# lang_ru.yml
title: Русское название сайта
```
