---
categories:
  - sysadmin
date: '2018-04-21T15:37:34+00:00'
lang: ru
slug: from-lj-to-hexo
tags:
  - blogging
title: Миграция с livejournal на hexo
projects: ["misc-utils"]
---


Миграция с [livejornal](https://yamadharma.livejournal.com/) составила некоторые проблемы.

<!--more-->

Хочу заметить, что комментарии я не переносил.

Наиболее подходящим показался мне [livejournal-export](https://github.com/arty-name/livejournal-export). Он переводит сразу в _markdown_. Однако, при этом не импортируются теги. 
Для идентификации использует параметры сессии броузера.

Вторым вариантом я рассмотрел [ljdump](https://github.com/ghewgill/ljdump). Он скачивает журнал в _html_. Для идентификации использует логин и пароль.

Потом пришлось преобразовать в _markdown_. Для этого написал скрипт _xml2md_.

```python
##!/usr/bin/python3
## -*- coding: utf-8 -*-

import os
import sys
from lxml import etree
import html2text
from datetime import datetime
from transliterate import translit, get_available_language_codes

outdir = 'markdown'
os.makedirs(outdir, exist_ok=True)

infile = sys.argv[1]
print(infile)

tree = etree.parse(infile)
post = tree.getroot()

postTitle = ''
postTags = ''

for elem in post.getchildren():
    if not elem.text:
        text = "None"
    else:
        text = elem.text
    ## print(elem.tag + " => " + text)
    ## book_dict[elem.tag] = text
    if elem.tag == 'subject':
        postTitle = text
    if elem.tag == 'eventtime':
        postDate = text
    if elem.tag == 'event':
        postContent = text
    if elem.tag == 'props':
        for propsElem in elem.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = propsElem.text
            ## print(propsElem.tag + " => " + text)
            if propsElem.tag == 'taglist':
                postTags = text
            



postHeader = 'layout: post\n'+'title: '+postTitle+'\n'+'date: '+str(postDate)
postHeader = postHeader+'\ncategories: blog\nlang: ru'
postHeader = postHeader+'\ntags: ['+postTags+']'
postHeader = postHeader+'\n'+'---'

h = html2text.HTML2Text()
h.ignore_links = False
h.body_width = 0
h.unicode_snob = True
postContent = h.handle(postContent)

fullPost = postHeader+'\n\n\n'+postContent

date = datetime.strptime(postDate, '%Y-%m-%d %H:%M:%S')
outFile = '{0.year}-{0.month:02d}-{0.day:02d}'.format(date)
if postTitle != '':
    translitTitle = translit(postTitle, 'ru', reversed=True)
    translitTitle = translitTitle.replace(" ","_")
    translitTitle = translitTitle.replace(":","")
    translitTitle = translitTitle.replace("'","")
    translitTitle = translitTitle.replace("«","")
    translitTitle = translitTitle.replace("»","")
    translitTitle = translitTitle.replace(";","")
else:
    translitTitle = '{0.hour:02d}-{0.minute:02d}-{0.second:02d}'.format(date)
outFile = outFile+'-'+translitTitle

f = open(outdir+'/'+str(outFile)+'.md', 'w')
f.write(fullPost)
f.close()
```

Преобразование можно выполнить с помощью команды:
```bash
./xml2md <file>
```
При этом создаётся каталог _markdown_ и в него помещается результат конвертации.

