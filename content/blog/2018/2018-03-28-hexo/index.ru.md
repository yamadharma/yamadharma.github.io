---
categories:
  - sysadmin
date: '2018-03-28T13:10:47+00:00'
lang: ru
slug: hexo
tags:
  - blogging
title: Переход блога на hexo
projects: ["misc-utils"]
---


Блог на [Jekyll](https://jekyllrb.com/) вести не получилось. Попробовал перейти на [Hexo](https://hexo.io). Он
попроще, но зато всё, что нужно, работает сразу.

<!--more-->

## Установка Hexo

* Установил Hexo (глобально):
  ```
  npm install -g hexo-cli
  ```

* Инициализировал каталог блога:
  ```
  hexo init .
  npm install
  ```

* Установил плагин для выкладывания на git (это делается в каталоге блога):
  ```
  npm install hexo-deployer-git --save
  ```

* Установил плагин для генерации RSS (такая опция есть в теме):
  ```
  npm install hexo-generator-feed --save
  ```

* Задал конфигурацию `_config.yml`:

```yaml
# Site
title: В борьбе обретёшь ты право своё
subtitle: Делай, что должен, и будь, что будет
description:
keywords:
author: Дмитрий Кулябов
language: ru
timezone:

# URL
# If your site is put in a subdirectory, set url as 'http://yoursite.com/child' and root as '/child/'
url: https://yamadharma.bitbucket.io/
root: /
permalink: :lang/:year/:month/:day/:title/
permalink_defaults:
  lang: ru

# Directory
source_dir: source
public_dir: public
tag_dir: tags
archive_dir: archives
category_dir: categories
code_dir: downloads/code
i18n_dir: :lang
skip_render:

# Writing
new_post_name: :lang/:year-:month-:day-:title.md # File name of new posts
default_layout: post
titlecase: false # Transform title into titlecase
external_link: true # Open external links in new tab
filename_case: 0
render_drafts: false
post_asset_folder: false
relative_link: false
future: true
highlight:
  enable: true
  line_number: true
  auto_detect: false
  tab_replace:

# Home page setting
# path: Root path for your blogs index page. (default = '')
# per_page: Posts displayed per page. (0 = disable pagination)
# order_by: Posts order. (Order by date descending by default)
index_generator:
  path: ''
  per_page: 10
  order_by: -date

# Category & Tag
default_category: uncategorized
category_map:
tag_map:

# Date / Time format
# Hexo uses Moment.js to parse and display date
# You can customize the date format as defined in
# http://momentjs.com/docs/#/displaying/format/
date_format: YYYY-MM-DD
time_format: HH:mm:ss

# Pagination
# Set per_page to 0 to disable pagination
per_page: 10
pagination_dir: page

# Extensions
# Plugins: https://hexo.io/plugins/
# Themes: https://hexo.io/themes/
theme: landscape

# Deployment
# Docs: https://hexo.io/docs/deployment.html
deploy:
  type: git
  repo: git@bitbucket.org:yamadharma/yamadharma.bitbucket.org.git
  branch: master

# Feed
# https://github.com/hexojs/hexo-generator-feed
feed:
  type: atom
  path: atom.xml
  limit: 20
  hub:
  content:
  content_limit: 600
  content_limit_delim: ' '
```

Таким образом, без настройки, получена работающая конфигурация.

## Порядок работы следующий

* Создаём новый файл для поста:
  ```
  hexo new <title>
  ```
* Радактируем пост.
* Генерим страницы:
  ```
  hexo generate
  ```
  или
  ```
  hexo g
  ```
* Выкладываем страницы на сайт:
  ```
  hexo deploy
  ```
  или
  ```
  hexo d
  ```
* Очищаем каталог:
  ```
  hexo clean
  ```

