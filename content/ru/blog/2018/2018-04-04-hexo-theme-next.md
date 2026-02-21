---
categories:
  - sysadmin
date: '2018-04-04T13:24:22+00:00'
lang: ru
slug: hexo-theme-next
tags:
  - blogging
title: Установка темы NexT для hexo
projects: ["misc-utils"]
---


Пробую поменять тему оформления блога на [NexT](https://github.com/iissnan/hexo-theme-next).

<!--more-->

Также можно посмотреть документацию:
  * <https://github.com/theme-next/hexo-theme-next/blob/master/docs/ru/README.md>
  * <https://github.com/iissnan/hexo-theme-next/blob/master/README.md> 

## Скачиваем тему

Переходим в каталог блога и скачиваем.
``` bash
git clone https://github.com/theme-next/hexo-theme-next themes/next
```


## Конфигурационный файл

``` bash
mkdir -p source/_data
cd source/_data
touch next.yml
```

Убедимся, что в файле `themes/next/_config.yml` установлено:
``` yaml
override: false
```

В корневом файле `_config.yml` устанавливаем:
``` yaml
theme: next
```
и
``` yaml
source_dir: source
```

В файл `source/_data/next.yml` переносим из `themes/next/_config.yml`
параметры, которые меняем.

## Страницы категорий и тегов

Создадим страницы `tags` и `categories`
``` bash
hexo new page "tags"
hexo new page "categories"
```

Отредактирем файлы `source/tags/index.md`
``` markdown
---
title: tags
date: "2018-04-04T14:41:32+00:00"
type: "tags"
---
```
и `source/categories/index.md`
``` markdown
---
title: categories
date: "2018-04-04T14:41:37+00:00"
type: "categories"
---
```

Добавим описание меню в файл `source/_data/next.yml`:
``` yaml
menu:
  home: / || home
  tags: /tags/ || tags
  categories: /categories/ || th
  archives: /archives/ || archive
```

## Личная фотография

Сделаем каталог для изображений:
``` bash
mkdir -p source/images
```

Поместим туда файл (например, `avatar.jpg`) и запишем в конфиг
`source/_data/next.yml`:
``` yaml
avatar: /images/avatar.jpg
```
Я сделал ширину 126px.

### Комментарии

Комментарии настроил через Disqus. 
Для этого сконфигурил на [Disqus](http://www.disqus.com) сайт с коротким именем _yamadharma-blog_.
Добавил в файл `source/_data/next.yml`:
``` yaml
disqus:
  enable: true
  shortname: yamadharma-blog
  count: true
  lazyload: false
```
