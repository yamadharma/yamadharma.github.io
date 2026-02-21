---
categories:
  - sysadmin
date: 2015-11-19T11:39:41+00:00
lang: ru
slug: drupal6-to-8
tags:
  - drupal
  - centos
title: Миграция с Drupal-6 на Drupal-8
projects: ["misc-utils"]
---


## Информация по миграции

* [Upgrading from Drupal 6 or 7 to Drupal 8](https://www.drupal.org/upgrade/migrate).

* [Executing a Drupal 6/7 to Drupal 8 upgrade](https://www.drupal.org/node/2257723).

* [The Drupal 6 to 8 Upgrade Challenge](https://drupalwatchdog.com/blog/2014/12/drupal-upgrade-1).

* [Known Issues with the Drupal 6/7 -> 8 Upgrade Path](https://www.drupal.org/node/2167633).

<!--more-->

## Обновление PHP

Для Drupal-8 нужен php-5.5. В Centos-7 идёт php-5.4. Обновим его до php-5.6. Вначале установним нужные репозитории
(см. <https://webtatic.com/packages/php56/>):

```bash
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
```

Сделаем подмену дистрибутивного php на php-5.6:

```bash
yum install yum-plugin-replace
yum replace php-common --replace-with=php56w-common
yum install php56w-opcache
```

## Установка Drush 8

Установим Composer:

```bash
yum -y install composer
```

Установим Drush (dev):

```bash
mkdir /usr/local/src/drush
cd /usr/local/src/drush
composer require drush/drush:dev-master
ln -s /usr/local/src/drush/vendor/drush/drush/drush /usr/local/bin/drush
```
