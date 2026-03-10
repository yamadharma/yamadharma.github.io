---
categories:
  - sysadmin
date: 2015-10-27T13:48:49+03:00
lang: ru
slug: samba-migrate
tags:
  - samba
title: Миграция с Samba3 на Samba4
projects: ["misc-utils"]
---


## Установка пакетов

В качестве системы для сервера используем Centos7. Там пока не
поддерживается функционал Samba4 AD (конфликт mit-krb и heimdal). Поэтому поставим самбу с
EnterpriseSAMBA.com <https://portal.enterprisesamba.com/>.

<!--more-->

```bash
cd /etc/yum.repos.d
wget https://sernet-samba-public:Noo1oxe4zo@download.sernet.de/packages/samba/4.2/rhel/7/sernet-samba-4.2.repo
```

В файле `/etc/yum.repos.d/sernet-samba-4.2.repo` заменим
`USERNAME:ACCESSKEY` на свои данные либо на публичную учётную запись
`sernet-samba-public:Noo1oxe4zo`.

Установим нужные пакеты:

```bash
yum -y install sernet-samba sernet-samba-ad
yum -y install bind
```



## Поиск дубликатов SID

Найдём дубликаты SID с помощью следующего скрипта (запусткается на
машине, где расположен ldap).

```python
#!/usr/bin/python
# A quick and dirty python script that checks for duplicat SID's using slapcat.
import os
 
data = os.popen("slapcat | grep sambaSID", 'r')
line = []
 
def anydup(thelist):
        dups = list(set([x for x in thelist if thelist.count(x) > 1]))
        for i in dups:
                print "Duplicate id: ", i
 
for each_line in data:
        line.append(each_line.strip())
 
anydup(line)
```

Далее дубликаты удаляются с помощью редактирования ldap (я использовал
<https://directory.apache.org/studio/>).

## Предварительная конфигурация

Добавил в файл `/etc/hosts` адрес хоста.

```
127.0.0.1               localhost.localdomain   localhost                                                                                                                                     
10.130.64.23            dc.dk.sci.pfu.edu.ru    dc
```

Также прописал его в прямой и обратной зонах DNS.

## Перенос конфигурационных файлов

```bash
pdc ~ # scp -r /var/lib/samba/private/ dc.dk.sci.pfu.edu.ru:/var/lib/samba/samba3tdb/
pdc ~ # scp /etc/samba/smb.conf dc.dk.sci.pfu.edu.ru:/var/lib/samba/samba3tdb/
```

В `/var/lib/samba/samba3tdb/smb.conf` следует заменить имя контроллера домена.
```
netbios name = dc
```

Поскольку при миграции используется информация из ldap, на хосте `dc`
задаю файл `/etc/openldap/ldap.conf`.

```
BASE    dc=dk,dc=sci,dc=pfu,dc=edu,dc=ru                                                                                                                                                      
URI     ldap://ldap.dk.sci.pfu.edu.ru                                                                                                                                                         
                                                                                                                                                                                              
TLS_REQCERT     allow
```

## Проведение миграции

```bash
samba-tool domain classicupgrade --dbdir=/var/lib/samba/samba3tdb/ --use-xattrs=yes --realm=dk.sci.pfu.edu.ru --dns-backend=BIND9_DLZ /var/lib/samba/samba3tdb/smb.conf
```

### Шаманство

В файле `/var/lib/samba/samba3tdb/smb.conf` заменил доменное имя
```
passdb backend = ldapsam:ldap://ldap.dk.sci.pfu.edu.ru
```
на ip-адрес
```
passdb backend = ldapsam:ldap://10.130.64.11
```
Без этого миграция падала с ошибкой `LDAP client internal error: NT_STATUS_BAD_NETWORK_NAME`.


### Настройка firewalld

```bash
firewall-cmd --add-service=ldap --permanent
firewall-cmd --add-service=kerberos --permanent
firewall-cmd --add-service=kpasswd --permanent
firewall-cmd --add-service=samba --permanent
firewall-cmd --add-service=samba-client --permanent
firewall-cmd --reload
```


### Настройка SELinux

```bash
setsebool -P samba_export_all_ro 1
setsebool -P samba_export_all_rw 1
setsebool -P samba_domain_controller 1
```

### Настройка Kerberos

Создадим файл конфигурации kerberos:
```bash
mv /etc/krb5.conf{,.default}
cp /var/lib/samba/private/krb5.conf /etc
```

### Настройка DNS

В файле `/etc/resolv.conf` задаём локальный DNS-сервер:
```
search dk.sci.pfu.edu.ru                                                                                                                                                                      
nameserver 127.0.0.1
```

В `/etc/named.conf` подключаем сконфигурённую конфигурацию:
```
include "/var/lib/samba/private/named.conf"; 
```

Также в раздел `options` добавляем:

```
options {
     [...]
     tkey-gssapi-keytab "/var/lib/samba/private/dns.keytab";
     [...]
};
```

А также следующее:

```
options {
     [...]
	 allow-query { localhost; 10.128.0.0/9; };
	 allow-update { 10.128.0.0/9; 127.0.0.0/8; };
     forwarders { 10.130.64.239; 8.8.8.8; 8.8.4.4; };
     allow-transfer {
		 # this config is for a single master DNS server
		 none;
	 };
     [...]
};
```

### Настройка firewalld

```bash
firewall-cmd --add-service=dns --permanent
firewall-cmd --reload
```

### Настройки прав доступа

Права доступа:

```bash
chown -R root:named /var/lib/samba/private/dns
chmod 770 /var/lib/samba/private/dns
chgrp named /var/lib/samba/private/dns.keytab
chmod g+r /var/lib/samba/private/dns.keytab
chgrp named /var/lib/samba/private
chgrp -R named /var/lib/samba/private/sam.ldb.d
chmod g+rw /var/lib/samba/private/sam.ldb.d/*
```

### Настройка SELinux

Изменим текущий контекст:

```bash
chcon -t named_conf_t /var/lib/samba/private/dns.keytab
chcon -t named_conf_t /var/lib/samba/private/named.conf
chcon -t named_conf_t /var/lib/samba/private/named.conf.update
chcon -R -t named_var_run_t /var/lib/samba/private/dns
chcon -t named_var_run_t /var/lib/samba/private/dns/${MYREALM}.zone
```

Изменим постоянный контекст:

```bash
semanage fcontext -a -t named_conf_t /var/lib/samba/private/dns.keytab
semanage fcontext -a -t named_conf_t /var/lib/samba/private/named.conf
semanage fcontext -a -t named_conf_t /var/lib/samba/private/named.conf.update
semanage fcontext -a -t named_var_run_t "/var/lib/samba/private/dns(/.*)?"
semanage fcontext -a -t named_var_run_t /var/lib/samba/private/dns/${MYREALM}.zone
semanage fcontext -a -t named_var_run_t /var/lib/samba/private/dns/${MYREALM}.zone.jnl
```

## Запуск демонов

Сконфигурим тип сервера samba в файле `/etc/default/sernet-samba`:
```
SAMBA_START_MODE="ad"
```

Запустим демоны:

```bash
systemctl start named.service
systemctl start sernet-samba-ad.service
```

Добавим их в автозагрузку:

```bash
systemctl enable named.service
systemctl enable sernet-samba-ad.service
```

## Проверка

Проверка DNS.

```bash
# host -t SRV _ldap._tcp.dk.sci.pfu.edu.ru.
_ldap._tcp.dk.sci.pfu.edu.ru has SRV record 0 100 389 dc.dk.sci.pfu.edu.ru.
# host -t SRV _kerberos._udp.dk.sci.pfu.edu.ru.
_kerberos._udp.dk.sci.pfu.edu.ru has SRV record 0 100 88 dc.dk.sci.pfu.edu.ru.
# host -t A dc.dk.sci.pfu.edu.ru.
dc.dk.sci.pfu.edu.ru has address 10.130.64.23
```

Замена пароля администратора:

```bash
samba-tool user setpassword Administrator
```
Проверка `smbclient`:

```bash
smbclient //localhost/netlogon -UAdministrator -c 'ls'
```

Аналогичный результат должно давать (`dc` --- имя сервера):

```bash
smbclient //dc/netlogon -k -c 'ls'
```

Проверка kerberos:

```bash
kinit administrator@DK.SCI.PFU.EDU.RU
klist
```

## Дополнительно

Убрать проверку сложности пароля:
```bash
samba-tool domain passwordsettings set --complexity=off
samba-tool domain passwordsettings set --history-length=0
samba-tool domain passwordsettings set --min-pwd-age=0
samba-tool domain passwordsettings set --max-pwd-age=0
```
