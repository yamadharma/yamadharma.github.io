---
title: "Работа без учётной записи в Cisco Packet Tracer"
author: ["Dmitry S. Kulyabov"]
date: 2022-05-07T15:39:00+03:00
lastmod: 2023-10-06T20:10:00+03:00
tags: ["cisco", "network", "education"]
categories: ["computer-science"]
draft: false
slug: "cisco-packet-tracer-accountless"
---

В начале марта 2022 года Cisco заблокировало учётные записи пользователей из России и доступ с ip-адресов России.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Начиная с версии PacketTracer7 для работы требуется наличие учётной записи в Network Academy: <https://www.netacad.com/> или <https://skillsforall.com/>.
-   В начале марта 2022 года Cisco заблокировало учётные записи пользователей из России и доступ с ip-адресов России.


## <span class="section-num">2</span> Установка патча на Packet Tracer {#установка-патча-на-packet-tracer}

-   Можно установить патч, отключающий проверку учётной записи при запуске PacketTracer.
-   Один из вариантов находится по адресу <https://rutracker.org/forum/viewtopic.php?t=6103761>.
-   Патч копируется в каталог с программой и запускается от имени администратора.
-   Перед этим следует отключить (временно) антивирус.


### <span class="section-num">2.1</span> Видео: Установка патча на Packet Tracer (Windows) {#видео-установка-патча-на-packet-tracer--windows}

{{< youtube JVmEkkMFI_g >}}


## <span class="section-num">3</span> Запуск Packet Tracer без сети {#запуск-packet-tracer-без-сети}

-   При запуске Packet Tracer на компьютере без доступа к сети учётная запись не проверяется.


### <span class="section-num">3.1</span> Linux {#linux}


#### <span class="section-num">3.1.1</span> Программа _firejail_ {#программа-firejail}

<!--list-separator-->

1.  Общая информация

    -   Ограничивает среду выполнения ненадёжных приложений с помощью _пространств имён Linux_ и _seccomp-bpf_.
    -   Сайт: <https://firejail.wordpress.com/>

<!--list-separator-->

2.  Установка

    -   Gentoo
        -   Стандартная версия
            ```shell
            emerge sys-apps/firejail
            ```
        -   Версия с долговременной поддержкой
            ```shell
            emerge sys-apps/firejail-lts
            ```

<!--list-separator-->

3.  Запуск Packet Tracer

    -   Запускаем с отключённой сетью:
        ```shell
        firejail --net=none --noprofile packettracer
        ```


#### <span class="section-num">3.1.2</span> Запуск Packet Tracer без сети на Linux {#запуск-packet-tracer-без-сети-на-linux}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube d20632ba64ccef923c3295da9fe19a7d >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube OvfE3MsH-Jo >}}

{{< /rtab >}}
{{< /tabs >}}


### <span class="section-num">3.2</span> Windows {#windows}


#### <span class="section-num">3.2.1</span> Блокировка доступа в интернет {#блокировка-доступа-в-интернет}

-   Откройте _Панель управления_.
-   Откройте пункт _Брандмауэр Защитника Windows_ или просто _Брандмауэр Windows_.
-   В открывшемся окне нажмите _Дополнительные параметры_.
-   Откроется окно брандмауэра в режиме повышенной безопасности.
-   Выберите _Правило для исходящего подключения_, а потом --- _Создать правило_.
-   Выберите _Для программы_ и нажмите _Далее_.
-   Укажите путь к исполняемому файлу программы, которой нужно запретить доступ в Интернет.
-   В следующем окне оставьте отмеченным пункт /Блокировать подключение.
-   В следующем окне отметьте, для каких сетей выполнять блокировку. Если для любых --- оставьте отмеченными все пункты.
-   Укажите понятное для вас имя правила и нажмите _Готово_.


#### <span class="section-num">3.2.2</span> Запуск Packet Tracer без сети на Windows {#запуск-packet-tracer-без-сети-на-windows}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 220a90487801dbf81e5016f6c1d213be >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube DMkFAMDjLIo >}}

{{< /rtab >}}
{{< /tabs >}}
