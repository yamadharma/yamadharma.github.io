---
categories:
  - sysadmin
date: 2015-05-15T05:56:13+00:00
lang: ru
slug: selinux-apps
tags:
  - selinux
  - centos
title: Настройка SELinux для некоторых приложений
projects: ["misc-utils"]
---


* `setsebool` запускаем как с ключём `-P` (для запоминания настроек), так и без него (чтобы работало в текущей сессии).

##  <a name='head_www-server'></a> WWW-сервер ##

```bash
setsebool -P httpd_unified 1
setsebool -P httpd_can_network_connect_db 1
setsebool -P httpd_can_network_connect 1
setsebool -P httpd_can_network_relay 1
setsebool -P httpd_can_sendmail 1
setsebool -P httpd_execmem 1
setsebool -P httpd_use_fusefs 1
```

## <a name='head_db'></a> Базы данных ##

<!--more-->

* Postgres

```bash
setsebool -P selinuxuser_postgresql_connect_enabled 1
```

* MySQL

```bash
setsebool -P selinuxuser_mysql_connect_enabled 1
```

## OJS ##

* Настраиваем [www-сервер](#head_www-server) и [базу данных](#head_db).

* Настраиваем доступ к файловой системе.

```bash
semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/html/ojs/cache(/.*)?"
semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/html/ojs/public(/.*)?"
semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/html/ojs/config.inc.php"
semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/html/ojs/plugins/generic(/.*)?"

semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/data(/.*)?"
```

## Drupal ##

* Настраиваем [www-сервер](#head_www-server) и [базу данных](#head_db).

* Настраиваем доступ к файловой системе.

```bash
semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/html/sites/drupal/(.*)/sites/(.*)/files(/.*)?"
semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/html/sites/drupal/(.*)/cache(/.*)?"
semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/html/sites/drupal/(.*)/sites/all(/.*)?"
```


## Moodle ##

* Настраиваем [www-сервер](#head_www-server) и [базу данных](#head_db).

* Настраиваем доступ к файловой системе.

```bash
semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/moodle/web-git/mod(/.*)?"
semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/moodle/web-git/local(/.*)?"
semanage fcontext --add -t httpd_sys_rw_content_t "/var/www/moodle/web-git/theme(/.*)?"
```

## LetsEncript ##

```bash
semanage fcontext -a -t cert_t '/etc/letsencrypt/(archive|live)(/.*)?'
```
