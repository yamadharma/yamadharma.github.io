---
categories:
  - sysadmin
date: '2018-05-17T08:43:05+00:00'
lang: ru
slug: webfm-uninstall
tags:
  - drupal
title: Деинсталляция WebFM из Drupal
projects: ["misc-utils"]
---


## Circumstantia ##

### Дано ###

Сайт на [Drupal](https://www.drupal.org) 5.

### Требуется ###

Превести сайт на Drupal 8.

### Предварительный план действий ###

Drupal 5 -> Drupal 6 -> Drupal 8.

### Проблема ###

В системе установлен пакет [webfm](https://www.drupal.org/project/webfm), который не поддерживается после Drupal 6. Webfm ведёт свою базу файлов, и в тексте сайта ставит указание не на файл, на а запись в своей базе данных.

<!--more-->

## Solutio ##

При поиски решения проблемы были найдены следующие сайты:
* <http://puna.upf.edu/node/97>
* <https://gist.github.com/heidar/3707913>

Основываясь на них, набросал скипт `webfm-fix`.
``` python
#!/usr/bin/python2
import MySQLdb

# For REALY work set update = True
update = False

# connect to the databases

db = MySQLdb.connect(
	host="localhost",        # your host, usually localhost
	user="username",         # your username
	passwd="userpassword",   # your password
	db="database",           # name of the data base
	use_unicode=True, charset='utf8')

cur = db.cursor()

# get all the file ids and paths from the old webfm table

filename_query = "SELECT fid, fpath FROM webfm_file"
cur.execute(filename_query)

fid_max = 0

filenames = {}
for row in cur.fetchall():
    filenames[row[0]] = row[1]
    if fid_max < row[0]:
	fid_max = row[0]

# find all webfm links and replace them with the actual file path

query = "SELECT nid, body, teaser FROM node_revisions WHERE body like '%webfm_send%' OR teaser like '%webfm_send%'"
cur.execute(query)

for row in cur.fetchall():
    entity_id = row[0]
    body = row[1]
    teaser = row[2]
    for i in range(fid_max, 0, -1):
	webfm1 = u'ru/webfm_send/' + str(i)
        webfm2 = u'webfm_send/' + str(i)
        webfm_list = [webfm1, webfm2]
        for webfm in webfm_list:
	    if i in filenames:
		sql_body = "UPDATE node_revisions SET body = REPLACE(body,'%s','%s') WHERE nid = %d" % (webfm,filenames[i],entity_id)
                sql_teaser = "UPDATE node_revisions SET teaser = REPLACE(teaser,'%s','%s') WHERE nid = %d" % (webfm,filenames[i],entity_id)
                if update:
	            try:
	                # Execute the SQL command
	        	cur.execute(sql_body)
                        cur.execute(sql_teaser)
	                # Commit your changes in the database
	        	db.commit()
	            except:
	                # Rollback in case there is any error
                        db.rollback()
db.close()
```

При написании скрипта использовал следующую информацию:
[Where does Drupal store the content of a node's body?](https://drupal.stackexchange.com/questions/6787/where-does-drupal-store-the-content-of-a-nodes-body)

In Drupal 6, content of the node's body is saved in `node_revisions` table under `body` field.
``` bash
node_revisions.body
```

In Drupal 7, content of the node's body is saved in `field_data_body` table under `body_value` field. In case content revisions are there then it also saves the data in `field_revision_body` table under `body_value` field.
``` bash
field_data_body.body_value
field_revision_body.body_value
```

In Drupal 8, content of the node's body is saved in `node__body` table under `body_value` field. In case content revisions are there then it also saves the data in `node_revision__body` table under `body_value` field.
``` bash
node__body.body_value
node_revision__body.body_value
```