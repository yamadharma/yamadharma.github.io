---
categories:
  - sysadmin
date: '2018-03-27T15:56:18+00:00'
lang: ru
slug: from-blogspot-to-hexo
tags:
  - blogging
title: Миграция с blogspot на hexo
projects: ["misc-utils"]
---


## Hexo

Перешёл на [hexo](https://hexo.io). Дополнительно решил перенести свои заметки с [blogspot](http://yamadharma.blogspot.ru/).

<!--more-->

* Установил пакет для миграции:
  ```
  npm install hexo-migrator-blogger --save
  ```

* Подправил файл миграции
  (`node_modules/hexo-migrator-blogger/lib/migrate.js`), чтобы
  нормальные названия файлов были:
{% codeblock lang:patch %}
--- migrate.js.old      2016-09-24 10:02:27.000000000 +0300
+++ migrate.js  2018-03-27 15:23:52.475311505 +0300
@@ -11,17 +11,19 @@ module.exports = function(source, target
         var posts = JSON.parse(body).feed.entry;
         async.each(posts, function(item, cb) {
             var title = item.title['$t'];
-            var file = title.replace(/\s/g,'-').replace(/[^A-z 0-9 -]/g,'');
             var published = item.published['$t'];
+            var file = moment(published).format('YYYY-MM-DD') + '-' + title;
             var tags = '';
             if (item.category) {
                 tags = item.category.map(prop('term'));
             }
             var header = [
-                'title: |',
-                '\t' +  title,
+               'layout: post',
+                'title: ' + '\"' + title + '\"',
                 'date: ' + moment(published).format('YYYY-MM-DD HH:mm:ss'),
                 'tags: [' + tags + ']',
+               'categories: blog',
+               'lang: ru',
                 '---',
             ];
             var content = item.content['$t'];
{% endcodeblock %}

* Запустил миграцию:
  ```
  hexo migrate blogger "http://yamadharma.blogspot.ru/feeds/posts/default?alt=json&max-results=10000"
  ```

* Почистил получившиеся файлы:
{% codeblock lang:bash %}
#!/bin/bash
# name: clean

for i in *.md
do
    sed -i -e "s:</div>::g" \
	-e "s:<div.*>::g" \
	"$i"
done
{% endcodeblock %}

* Сделал транслит названий:
{% codeblock lang:bash %}
#!/bin/bash
# name: translit
# Перекодирует рекурсивно в текущем каталоге имена
# файлов и каталогов в транслит.
# Успенский В. А. К проблеме транслитерации русских текстов латинскими буквами
# <http://lingvoforum.net/index.php?topic=35758.0>

shopt -s nullglob
for NAME in *
do
    TRS=`echo $NAME | sed "y/абвгдезиклмнопрстуфц/abvgdeziklmnoprstufc/"`
    TRS=`echo $TRS | sed "y/АБВГДЕЗИКЛМНОПРСТУФЦ/ABVGDEZIKLMNOPRSTUFC/"`
    TRS=${TRS//х/kh} TRS=${TRS//Х/KH};
    TRS=${TRS//ч/ch} TRS=${TRS//Ч/CH};
    TRS=${TRS//ш/sh} TRS=${TRS//Ш/SH};
    TRS=${TRS//ё/yo} TRS=${TRS//Ё/YO};
    TRS=${TRS//ж/zh} TRS=${TRS//Ж/ZH};
    TRS=${TRS//щ/th} TRS=${TRS//Щ/TH};
    TRS=${TRS//э/eh} TRS=${TRS//Э/EH};
    TRS=${TRS//ю/yu} TRS=${TRS//Ю/YU};
    TRS=${TRS//я/ya} TRS=${TRS//Я/YA};
    TRS=${TRS//й/yj} TRS=${TRS//Й/yj};
    TRS=${TRS//ъ/jh} TRS=${TRS//Ъ/JH};
    TRS=${TRS//ь/j} TRS=${TRS//Ь/J};
    TRS=${TRS//ы/ih} TRS=${TRS//Ы/IH};

    TRS=${TRS// /_};
    
    if [[ -d "$NAME" ]]
    then
	mv -v "$NAME" "$TRS"
	cd "$TRS"
	"$0"
	cd ..
    else
	mv -v "$NAME" "$TRS"
    fi
done
{% endcodeblock %}