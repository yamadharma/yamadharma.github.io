---
title: "Замена Centos"
author: ["Dmitry S. Kulyabov"]
date: 2021-05-25T15:22:00+03:00
lastmod: 2023-11-05T15:50:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "replacing-centos"
---

После серии покупок (Centos -&gt; RedHat -&gt; IBM) дистрибутив _Centos_, представляющий из себя свободную реализацию _RedHat_, приказал долго жить.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Предыстория {#предыстория}

-   Red Hat купила Centos.
-   IBM купила RedHat.
-   Компания RedHat декларировала завершение разработки и поддержки _CentOS_ в конце 2021 года и переход на поддержку непрерывного релиза _CentOS Stream_.
    -   <https://blog.centos.org/2020/12/future-is-centos-stream/>.
    -   ~~<https://centos.rip/> (издевательский сайт)~~.


## <span class="section-num">2</span> Прекращение публикации исходных текстов RedHat {#прекращение-публикации-исходных-текстов-redhat}

-
-   <https://www.redhat.com/en/blog/furthering-evolution-centos-stream>
-   Компания Red Hat объявила об изменении подхода к публикации исходных текстов пакетов дистрибутива Red Hat Enterprise Linux и прекращении публикации кода пакетов в Git-репозитории <https://git.centos.org/>.
-   Единственным публично доступным источником исходных текстов пакетов RHEL теперь будет репозиторий CentOS Stream.
-   Для клиентов и партнёров Red Hat будет оставлена возможность загрузки кода пакетов, соответствующих релизам RHEL, через клиентский портал компании, доступ к которому требует наличия учётной записи.
-   В <https://git.centos.org/> публиковались исходные тексты пакетов уже выпущенных релизов, а в репозитории CentOS Stream развивается код пакетов для ещё не выпущенных релизов.
-   Из этого репозиторий альтернативные реализации брали исходные коды пакетов для сборки.
-   AlmaLinux и Rocky Linux опубликовали заявления c планом дальнейших действий.
-   AlmaLinux
    -   <https://almalinux.org/blog/impact-of-rhel-changes/>
    -   Отслеживание изменений из репозитория CentOS Stream, использование репозитория Oracle Linux.
    -   -   <https://almalinux.org/blog/future-of-almalinux/>
        -   Проект AlmaLinux объявил об изменении стратегии развития
        -   Дистрибутив больше не будет полностью клонировать Red Hat Enterprise Linux и станет допускать наличие незначительных расхождений в поведении.
        -   Сохранит бинарную совместимость на уровне ABI.
-   Rocky Linux
    -   <https://rockylinux.org/news/2023-06-22-press-release/>
    -   Создании дополнительного репозитория <https://git.rockylinux.org/staging/src-rhel/rpms>, отслеживании рассинхронизированных обновлений.


### <span class="section-num">2.1</span> OpenELA {#openela}

-   <span class="timestamp-wrapper"><span class="timestamp">[2023-11-02 Чт]</span></span>Ассоциация OpenELA (Open Enterprise Linux Association)создала репозиторий OpenELA для замены репозитория `git.centos.org`.
-   Репозиторий: <https://github.com/openela-main>
-   Сообщение о создании репозитория: <https://openela.org/news/2023.11.02-governance_and_code_availability/>


## <span class="section-num">3</span> Альтернативы Centos {#альтернативы-centos}


### <span class="section-num">3.1</span> Условные альтернативы {#условные-альтернативы}

-   Данные дистрибутивы можно считать либо условными, либо временными альтернативами.


#### <span class="section-num">3.1.1</span> RHEL {#rhel}

<!--list-separator-->

1.  Описание дистрибутива

    -   <https://www.redhat.com/>
    -   Собственно, это и есть первичный дистрибутив, который копируют.
    -   Отличается надёжностью, используется для корпоративных систем.
    -   Большой значение имеют дополнительные продукты: Satellite, Openstack, RHEV, Pacemaker, Gluster, Ceph, Openshift.
    -   <span class="timestamp-wrapper"><span class="timestamp">[2022-03-08 Вт]</span></span>Компания Red Hat прекратила работу с организациями из России и Белоруссии (<https://www.redhat.com/en/blog/red-hats-response-war-ukraine>).

<!--list-separator-->

2.  Распространение

    -   В качестве компенсации за прекращение распространения CentOS предлагает программу для разработчиков ([Red Hat Developer](https://developers.redhat.com/products/rhel/download)).
    -   В рамках этой программы можно установить 16 хостов.

<!--list-separator-->

3.  Миграция с Centos8

    -   Репозиторий скриптов: <https://github.com/oamg/convert2rhel/>
    -   Документация: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/converting_from_an_rpm-based_linux_distribution_to_rhel/index>
    -   Обновить дистрибутив:
        ```shell
        sudo dnf update -y
        sudo reboot
        ```
    -   Установить репозиторий:
        -   Загрузите GPG-ключ Red Hat:
            ```shell
            curl -o /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release https://www.redhat.com/security/data/fd431d51.txt
            ```
        -   Загрузите SSL-сертификат:
            ```shell
            curl --create-dirs -o /etc/rhsm/ca/redhat-uep.pem https://ftp.redhat.com/redhat/convert2rhel/redhat-uep.pem
            ```
        -   Установите файл репозитория `Convert2RHEL`:
            ```shell
            curl -o /etc/yum.repos.d/convert2rhel.repo https://ftp.redhat.com/redhat/convert2rhel/version_number/convert2rhel.repo
            ```

    -   Установите скрипт:
        ```shell
        yum -y install convert2rhel
        ```
    -   Провести миграцию:
        -   С идентификатором организации и ключом активации:
            ```shell
            convert2rhel --org organization_ID --activationkey activation_key
            ```
        -   С именем пользователя, паролем и идентификатором пула:
            ```shell
            convert2rhel --username username --password password --pool pool_ID
            ```


#### <span class="section-num">3.1.2</span> CentOS Stream {#centos-stream}

<!--list-separator-->

1.  Описание дистрибутива

    -   <https://www.centos.org/>
    -   Это rolling release.
    -   Теряется основное преимущество --- стабильность.

<!--list-separator-->

2.  Миграция на CentOS Stream

    -   Подключаем репозиторий CentOS Stream:
        ```shell
        dnf install centos-release-stream
        ```
    -   Указываем новый репозиторий в качестве репозитория по умолчанию:
        ```shell
        dnf swap centos-{linux,stream}-repos
        ```
    -   Синхронизируем установленные пакеты:
        ```shell
        dnf distro-sync
        ```


#### <span class="section-num">3.1.3</span> Oracle Linux {#oracle-linux}

<!--list-separator-->

1.  Описание дистрибутива

    -   <https://www.oracle.com/linux/>
    -   Особенность ---  собственное ядро _Unbreakable Enterprise Kernel_.
    -   Нет доверия Ораклу. Они и дистрибутив сделали открытым в пику RedHat, чтобы пользователей перетянуть. В любой момент могут доступ прикрыть.

<!--list-separator-->

2.  Миграция с Centos8

    -   Репозиторий скриптов: <https://github.com/oracle/centos2ol>
    -   Обновить дистрибутив:
        ```shell
        sudo dnf update -y
        sudo reboot
        ```
    -   Скачать скрипт:
        ```shell
        git clone https://github.com/oracle/centos2ol.git
        ```
    -   Провести миграцию:
        ```shell
        sudo bash centos2ol.sh
        ```


#### <span class="section-num">3.1.4</span> VzLinux {#vzlinux}

<!--list-separator-->

1.  Описание дистрибутива

    -   <https://vzlinux.org/>
    -   Разрабатывает компания Virtuozzo (бывшее подразделение компании Parallels).
    -   Специализация: разработка серверного ПО для виртуализации на основе открытых проектов.
    -   Для них это побочное занятие.

<!--list-separator-->

2.  Миграция с Centos8

    -   Репозиторий скриптов: <https://github.com/vzlinux/vzdeploy>
    -   Обновить дистрибутив:
        ```shell
        sudo dnf update -y
        sudo reboot
        ```
    -   Скачать скрипт:
        ```shell
        git clone https://github.com/vzlinux/vzdeploy.git
        ```
    -   Провести миграцию:
        ```shell
        sudo bash vzdeploy8
        ```


#### <span class="section-num">3.1.5</span> SUSE Liberty Linux {#suse-liberty-linux}

<!--list-separator-->

1.  Описание дистрибутива

    -   Сайт: <https://www.suse.com/products/suse-liberty-linux/>
    -   Пакеты пространства пользователя в SUSE Liberty Linux сформировано путём пересборки исходных SRPM-пакетов из RHEL 8.5.
    -   Пакет с ядром заменён на собственный вариант, основанный на ветке ядра Linux 5.3 и созданный путём пересборки пакета с ядром из дистрибутива SUSE Linux Enterprise 15 SP3.
    -   Дистрибутив формируется только для архитектуры x86-64.


### <span class="section-num">3.2</span> Полные альтернативы {#полные-альтернативы}


#### <span class="section-num">3.2.1</span> Rocky Linux {#rocky-linux}

<!--list-separator-->

1.  Описание дистрибутива

    -   <https://rockylinux.org/>
    -   Руководитель: Грегори Курцер (Gregory Kurtzer), основател CentOS.
    -   Для развития продуктов и поддержки сообщества разработчиков создана коммерческая компания Ctrl IQ.
    -   В финансировании проекта участвуют компании MontaVista, 45Drives, OpenDrives и Amazon Web Services.

<!--list-separator-->

2.  Миграция с Centos8

    -   Репозиторий скриптов: <https://github.com/rocky-linux/rocky-tools>
    -   Обновить дистрибутив:
        ```shell
        sudo dnf update -y
        sudo reboot
        ```
    -   Скачать скрипт:
        ```shell
        git clone https://github.com/rocky-linux/rocky-tools.git
        ```
    -   Провести миграцию:
        ```shell
        sudo bash migrate2rocky.sh -r
        ```


#### <span class="section-num">3.2.2</span> Almalinux {#almalinux}

<!--list-separator-->

1.  Описание дистрибутива

    -   <https://almalinux.org/>
    -   Основан компанией CloudLinux.
    -   Проект курирует отдельная некоммерческая организация AlmaLinux OS Foundation.
    -   Слишком быстро выходят сборки (сразу после выпуска RedHat).

<!--list-separator-->

2.  Зачем делается этот дистрибутив

    -   в CloudLinux осознали, что CentOS сам освобождает место под солнцем, а значит его можно попытаться занять;
    -   CloudLinux давно уже пересобирали RHEL/CentOS, есть опыт и своя сборочная инфраструктура;
    -   есть технология KernelCare --- обновления ядер без перезагрузки;
    -   стали срочно делать свою пересборку CentOS, доделывать сборочную инфраструктуру;
    -   купили железо для сборок под новые архитектуры (например, arm), под которые CloudLinux ранее не собирался;
    -   CloudLinux проверяет ABI своих пакетов на соответствие ABI пакетов из RHEL;
    -   хотят продвигать свои идеи в RHEL через CentOS Stream и апстримы.

<!--list-separator-->

3.  Миграция с Centos8

    -   Репозиторий скриптов: <https://github.com/AlmaLinux/almalinux-deploy>
    -   Обновить дистрибутив:
        ```shell
        sudo dnf update -y
        sudo reboot
        ```
    -   Скачать скрипт для обновления:
        ```shell
        curl -O https://raw.githubusercontent.com/AlmaLinux/almalinux-deploy/master/almalinux-deploy.sh
        ```
    -   Провести миграцию:
        ```shell
        sudo bash almalinux-deploy.sh
        ```


## <span class="section-num">4</span> Что выбрать {#что-выбрать}

-   Наблюдается паритет у Rocky Linux и Almalinux.
-   На данный момент склоняюсь более к Rocky Linux.
