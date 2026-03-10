---
categories:
  - sysadmin
date: '2006-09-17T20:55:00+00:00'
lang: ru
slug: monit-i-gentoo-rc-scripts
tags:
  - init-scripts
  - gentoo
title: Monit и gentoo rc-scripts
---



При использовании monit для перезапуска rc-скриптов в gentoo использовал killall и опцию zap.  
Нашёл это-же решение, но оформленное красивее.  

<!--more-->
  
Это файл /etc/monit.d/bin/kickservice  
  

``` bash
##!/bin/sh  
## kickservice by Eric Radman  
## Script used by monit to kill off and restart daemons  
## /etc/monit.d/bin/kickservice  
   
function stop ()  
{  
     /etc/init.d/$1 pause  
     /etc/init.d/$1 zap  
     if [ "$2" == "kill" ]  
         then  
         /bin/killall $3  
     fi  
}  
   
function start ()  
{  
     /etc/init.d/$1 zap  
     /etc/init.d/$1 start  
}  
   
case "$1" in  
  start)  
     start $2 $3 $4  
     ;;  
  stop)  
     stop $2 $3 $4  
     ;;  
  *)  
     echo "Usage: kickservice [start|stop] [service] kill [daemon]"  
     ;;  
 esac  
```

  
Проблема возникла из-за того, что при установке baselayout-1.12.x перестал нормально работать pppd (при подключении через pptp к VPN-серверу провайдера). Очень часто соединение не устанавливается (вина, думаю, провайдерского сервера). По идее после этого он должен перезапускаться, а он просто ничего не делал. Решил снять проблему с помощью monit.   
Убрал net.ppp0 из загрузки, и заставил monit мониторить ppp0.  
  
Вот скрипт /etc/monit.d/ppp0  
  

``` bash
check process pppd with pidfile /var/run/ppp0.pid  
   start program = "/etc/monit.d/bin/kickservice start net.ppp0"  
   stop program = "/etc/monit.d/bin/kickservice stop net.ppp0 kill pppd"  
   if 5 restarts within 5 cycles then timeout
``` 

P. S. Хотел запостить скрипты, но не знаю как :(  
  
