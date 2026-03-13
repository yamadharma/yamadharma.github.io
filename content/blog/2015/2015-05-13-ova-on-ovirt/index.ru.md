---
categories:
  - sysadmin
date: 2015-05-13T08:48:57+00:00
lang: ru
slug: ova-on-ovirt
tags:
  - net
title: Установка виртуальной машины NOC на oVirt
projects: ["misc-utils"]
---


Чтобы не мучиться с установкой [NOC](https://kb.nocproject.org) решил установить с образа, [предлагаемого на сайте](https://kb.nocproject.org/display/SITE/Downloads). К сажалению, образ предлагается в формате `ova`, а у меня стоит oVirt (`ovirt-engine`). Он этот формат не понимает. Однако у меня есть ещё хост с `kvm` (`kvm-host`).

<!--more-->

* Распаковываю `noc-x86_64-Debian-8.ova`:
{% codeblock lang:bash %}
tar -xf noc-x86_64-Debian-8.ova
{% endcodeblock %}

* Конвертирую в формат `qcow2`:
{% codeblock lang:bash %}
qemu-img convert -O qcow2 noc-x86_64-Debian-8-disk1.vmdk noc-x86_64-Debian-8-disk1.qcow2
{% endcodeblock %}

* Создаю виртуальную машину на kvm. По большому счёту это нужно лишь для создания xml-файла описания виртуальной машины.

* Машина сначала не загрузилась потому, что в `/etc/fstab` на `/boot` был жёстко прописан `/dev/sda1`. Поменял на `/dev/vda1`.

* Пароли следующие:
{% codeblock lang:bash %}
Username: user
Password: thenocproject
Root password: thenocproject
{% endcodeblock %}

* На web-интерфейс логин и пароль:
{% codeblock lang:bash %}
User: admin
Password: admin
{% endcodeblock %}

* Образы на `kvm-host` находятся в каталоге `/var/lib/libvirt/images`, а соответствующие конфигурационные файлы в `/etc/libvirt/qemu`. Копируем нужный конфиг в `/var/lib/libvirt/images` и называем `noc-x86_64-Debian-8-disk1.xml`. Поскольку будем работать по сети, заменяем в нём путь к образу с `/var/lib/...` на  `/net/kvm-host/var/lib/...`.

* Заходим на хост `ovirt-engine`, монтируем `kvm-host` по autofs:
{% codeblock lang:bash %}
cd /net/kvm-host/var/lib/libvirt/images
{% endcodeblock %}

* Импортируем образ в oVirt:

{% codeblock lang:bash %}
virt-v2v -b vlan5  -i libvirtxml -o rhev -os ovirt-node-01:/ovirt/export noc-x86_64-Debian-8-disk1.xml
{% endcodeblock %}

Здесь `ovirt-node-01` — узел, на котором запускаются виртуальные машины, `vlan5` — интерфейс, к которому она будет подключена.