---
title: "Системное администрирование"
author: ["Dmitry S. Kulyabov"]
date: 2021-04-10T18:18:00+03:00
lastmod: 2026-02-15T20:33:00+03:00
tags: ["MOC", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "system-administration"
---

По мере сил занимаюсь настройкой компьютеров. В основном на Linux.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> DevOps {#devops}

-   [Непрерывная интеграция. GitHub Actions]({{< relref "../notes/public/20230716190400-непрерывная_интеграция_github_actions.md" >}})
-   [Система автоматизации Ansible]({{< relref "../notes/public/20251210T201500--система_автоматизации_ansible.md" >}})


## <span class="section-num">2</span> Базы данных {#базы-данных}

-   [PostgreSQL]({{< relref "../notes/public/20251211T112000--postgresql.md" >}})


## <span class="section-num">3</span> Безопасность {#безопасность}


### <span class="section-num">3.1</span> Пароли {#пароли}

-   [Менеджеры паролей]({{< relref "../notes/public/20210429115600-менеджеры_паролеи.md" >}})
-   [Have I Been Pwned (HIBP)]({{< relref "../notes/public/20210503152100-have_i_been_pwned_hibp.md" >}})
-   [Одноразовые пароли]({{< relref "../notes/public/20230824200900-одноразовые_пароли.md" >}})


### <span class="section-num">3.2</span> PKI {#pki}

-   [Конвертация сертификатов PKCS12 в PEM]({{< relref "../notes/public/20241213205800-конвертация_сертификатов_pkcs12_в_pem.md" >}})


### <span class="section-num">3.3</span> Разное {#разное}

-   [Тип ключа ssh]({{< relref "../notes/public/20220203144800-тип_ключа_ssh.md" >}})
-   [Сертификаты ACME]({{< relref "../notes/public/20220430144900-сертификаты_let_s_encrypt.md" >}})
-   [Механизм HSTS]({{< relref "../notes/public/20220503200500-механизм_hsts.md" >}})
-   [fail2ban. Основные настройки]({{< relref "../notes/public/20231030110100-fail2ban_основные_настроики.md" >}})


### <span class="section-num">3.4</span> Резервное копирование {#резервное-копирование}

-   [Ротирование бэкапов]({{< relref "../notes/public/20250311T162900--ротирование_бэкапов.md" >}})
-   [Proxmox Backup Server]({{< relref "../notes/public/20250304T140200--proxmox_backup_server.md" >}})
-   [Резервное копирование. Restic]({{< relref "../notes/public/20250817T205600--резервное_копирование_restic.md" >}})


## <span class="section-num">4</span> Гаджеты {#гаджеты}

-   [Гаджеты]({{< relref "../notes/public/20240822143100-гаджеты.md" >}})


## <span class="section-num">5</span> Графическое окружение {#графическое-окружение}


### <span class="section-num">5.1</span> Общее {#общее}

-   [Буфер обмена]({{< relref "../notes/public/20250311T090300--буфер_обмена.md" >}})
-   [Интерфейс. Transient menu]({{< relref "../notes/public/20250424T155000--интерфеис_transient_menu.md" >}})
-   [Броузер. Реализация transient menu]({{< relref "../notes/public/20250424T165400--броузер_реализация_transient_menu.md" >}})


### <span class="section-num">5.2</span> Linux {#linux}

-   [Мультимедиа сервер PipeWire]({{< relref "../notes/public/20210428162800-мультимедиа_сервер_pipewire.md" >}})
-   [XDG. Каталоги]({{< relref "../notes/public/20241019182100-xdg_каталоги.md" >}})
-   [XDG. Пользовательские каталоги]({{< relref "../notes/public/20210916201500-xdg_пользовательские_каталоги.md" >}})
-   [XDG. Приложения MIME]({{< relref "../notes/public/20230402133900-xdg_mime_applications.md" >}})
-   [Ввод с помощью Compose]({{< relref "../notes/public/20211226133300-ввод_с_помощью_compose.md" >}})
-   [Тайловые оконные менеджеры]({{< relref "../notes/public/20230619093700-таиловые_оконные_менеджеры.md" >}})
-   [Консоль linux. Kmscon]({{< relref "../notes/public/20240625120800-консоль_linux_kmscon.md" >}})
-   [Лаунчеры]({{< relref "../notes/public/20240811120000-лаунчеры.md" >}})
-   [Дисплейный менеджер gdm]({{< relref "../notes/public/20250821T115000--дисплеиныи_менеджер_gdm.md" >}})


### <span class="section-num">5.3</span> Wayland {#wayland}

-   [Wayland]({{< relref "../notes/public/20230814114900-wayland.md" >}})
-   [Linux. Приложения. Индикатор прогресса wob]({{< relref "../notes/public/20240306210000-linux_приложения_индикатор_прогресса_wob.md" >}})
-   [Переход на Sway]({{< relref "../notes/public/20210410175400-переход_на_sway.md" >}})


### <span class="section-num">5.4</span> X11 {#x11}

-   [Window manager i3]({{< relref "../notes/public/20210514113200-window_manager_i3.md" >}})


### <span class="section-num">5.5</span> Темы оформления {#темы-оформления}

-   [Linux. Темы оформления]({{< relref "../notes/public/20240507153900-linux_темы_оформления.md" >}})


## <span class="section-num">6</span> Инфраструктура в РУДН {#инфраструктура-в-рудн}

-   [Переход на домен pfur.ru]({{< relref "../notes/public/20230420181800-переход_на_домен_pfur_ru.md" >}})
-   [Спецификации компьютеров]({{< relref "../notes/public/20230611215000-спецификации_компьютеров.md" >}})
-   [Серверы на Донской]({{< relref "../notes/public/20220915201900-виртуальные_машины_на_донскои.md" >}})
-   [Сеть на Донской]({{< relref "../notes/public/20230813194000-сеть_на_донскои.md" >}})


## <span class="section-num">7</span> Конфигурации {#конфигурации}

-   [Моя конфигурация программного обеспечения]({{< relref "../notes/public/20240306214200-моя_конфигурация_программного_обеспечения.md" >}})


## <span class="section-num">8</span> Оборудование {#оборудование}


### <span class="section-num">8.1</span> Подбор компьютера {#подбор-компьютера}

-   [Критерии выбора ноутбука]({{< relref "../notes/public/20220430200600-критерии_выбора_ноутбука.md" >}})
-   [Критерии выбора персонального компьютера]({{< relref "../notes/public/20220721201700-критерии_выбора_персонального_компьютера.md" >}})
-   [Набор вещей для системного администратора]({{< relref "../notes/public/20220911165100-набор_вещеи_для_системного_администратора.md" >}})
-   [Клавиатуры]({{< relref "../notes/public/20231011164900-клавиатуры.md" >}})


### <span class="section-num">8.2</span> Процессоры {#процессоры}

-   [Варианты микроархитектуры x86]({{< relref "../notes/public/20240920201600-варианты_микроархитектуры_x86.md" >}})


## <span class="section-num">9</span> Операционные системы {#операционные-системы}


### <span class="section-num">9.1</span> Windows {#windows}

-   [Администрирование Windows]({{< relref "../notes/public/20210501162800-администрирование_windows.md" >}})
-   [MSYS2. Приложения Unix под Windows]({{< relref "../notes/public/20230923155500-msys2_приложения_unix_под_windows.md" >}})


### <span class="section-num">9.2</span> Linux {#linux}

-   [Администрирование Linux]({{< relref "../notes/public/20230607183500-администрирование_linux.md" >}})
-   [Linux. Подсистема Live Update Orchestrator]({{< relref "../notes/public/20260215T202900--linux_подсистема_live_update_orchestrator.md" >}})


### <span class="section-num">9.3</span> Установка операционных систем {#установка-операционных-систем}

-   [Загрузочная флешка]({{< relref "../notes/public/20210410184600-загрузочная_флешка.md" >}})
-   [Перенос Linux на btrfs]({{< relref "../notes/public/20210521203800-установка_linux_на_btrfs.md" >}})
-   [Установка загрузчика grub]({{< relref "../notes/public/20210919135800-установка_загрузчика_grub.md" >}})
-   [Использование vagrant]({{< relref "../notes/public/20211112121100-использование_vagrant.md" >}})
-   [Система установки SALI]({{< relref "../notes/public/20240827174200-система_установки_sali.md" >}})
-   [Система установки SALII]({{< relref "../notes/public/20240827192500-система_установки_salii.md" >}})


### <span class="section-num">9.4</span> Серверные системы {#серверные-системы}

-   [Замена Centos]({{< relref "../notes/public/20210525152200-замена_centos.md" >}})
-   [CentOS 8. Изменение адресов репозиториев]({{< relref "../notes/public/20220210143900-centos_8_изменение_адресов_репозиториев.md" >}})
-   [Rocky Linux. Установка сервера]({{< relref "../notes/public/20220812135700-rocky_linux_9_установка_сервера.md" >}})
-   [Автообновление систем на базе деривативов RedHat]({{< relref "../notes/public/20220925094200-автообновление_систем_на_базе_деривативов_redhat.md" >}})
-   [Обновление деривативов RedHat]({{< relref "../notes/public/20240912124800-обновление_деривативов_redhat.md" >}})


### <span class="section-num">9.5</span> Управление программным обеспечением {#управление-программным-обеспечением}

-   [Обновление пакетов python]({{< relref "../notes/public/20220121163300-обновление_пакетов_python.md" >}})


### <span class="section-num">9.6</span> Терминальный доступ {#терминальный-доступ}

-   [Virtual Desktop Infrastructure]({{< relref "../notes/public/20220723192900-virtual_desktop_infrastructure.md" >}})


### <span class="section-num">9.7</span> Утилиты настройки среды {#утилиты-настройки-среды}

-   [Утилита module]({{< relref "../notes/public/20220724161400-утилита_module.md" >}})


### <span class="section-num">9.8</span> Загрузчики {#загрузчики}

-   [Загрузчик rEFInd]({{< relref "../notes/public/20240129114100-загрузчик_refind.md" >}})


## <span class="section-num">10</span> Организация обучения {#организация-обучения}

-   [Дисплейные классы]({{< relref "../notes/public/20210926194000-дисплеиные_классы.md" >}})
-   [Системы управления обучением]({{< relref "../notes/public/20240914165200-системы_управления_обучением.md" >}})


## <span class="section-num">11</span> Пользовательские программы {#пользовательские-программы}


### <span class="section-num">11.1</span> Виртуализация {#виртуализация}

-   [Система виртуализации VirtualBox]({{< relref "../notes/public/20210917113500-система_виртуализации_virtualbox.md" >}})
-   [Система виртуализации VMware]({{< relref "../notes/public/20240516113300-система_виртуализации_vmware.md" >}})
-   [Виртуализация. Libvirt]({{< relref "../notes/public/20241126133900-виртуализация_libvirt.md" >}})
    -   [Виртуализация. Virt-manager]({{< relref "../notes/public/20241126140800-виртуализация_virt_manager.md" >}})
    -   [Виртуализация. Virtiofs]({{< relref "../notes/public/20241126145000-виртуализация_virtiofs.md" >}})
-   [Контейнеры. podman]({{< relref "../notes/public/20241204201300-контеинеры_podman.md" >}})


### <span class="section-num">11.2</span> Вычисления {#вычисления}

-   [Принципы работы на суперкомпьютере]({{< relref "../notes/public/20220722105100-принципы_работы_на_суперкомпьютере.md" >}})
-   [Регламент доступа к суперкомпьютеру РУДН]({{< relref "../notes/public/20220907143700-регламент_доступа_к_суперкомпьютеру_рудн.md" >}})


### <span class="section-num">11.3</span> Квантовая химия {#квантовая-химия}

-   [Квантовая химия. Gamess]({{< relref "../notes/public/20221017165800-квантовая_химия_gamess.md" >}})


### <span class="section-num">11.4</span> Наборы программ {#наборы-программ}

-   [Программы на Android]({{< relref "../notes/public/20230626190600-программы_на_android.md" >}})


### <span class="section-num">11.5</span> Обработка видео {#обработка-видео}

-   [Видео. KDEnlive]({{< relref "../notes/public/20210723191000-видео_kdenlive.md" >}})
-   [Обработка видео. Командная строка]({{< relref "../notes/public/20211021172600-обработка_видео_командная_строка.md" >}})
-   [Закачка с youtube]({{< relref "../notes/public/20220309173800-закачка_с_youtube.md" >}})
-   [OBS Studio]({{< relref "../notes/public/20250220T113800--obs_studio.md" >}})
-   [OBS Studio. Стриминг]({{< relref "../notes/public/20250216T171600--obs_studio_стриминг.md" >}})


### <span class="section-num">11.6</span> Офисные программы {#офисные-программы}

-   [Настройка LibreOffice]({{< relref "../notes/public/20220127140000-настроика_libreoffice.md" >}})
-   [Альтернативы Microsoft Office]({{< relref "../notes/public/20230319171300-альтернативы_microsoft_office.md" >}})


### <span class="section-num">11.7</span> Просмотрщики {#просмотрщики}

-   [Pdf. Просмотр. Zathura]({{< relref "../notes/public/20230920131200-pdf_просмотр_zathura.md" >}})


### <span class="section-num">11.8</span> Работа с дисками {#работа-с-дисками}

-   [Использование sfdisk]({{< relref "../notes/public/20220308194500-использование_sfdisk.md" >}})


### <span class="section-num">11.9</span> Работа с терминалом {#работа-с-терминалом}

-   [Терминальный мультиплексор tmux]({{< relref "../notes/public/20240219101100-терминальныи_мультиплексор_tmux.md" >}})
-   [Эмулятор терминала kitty]({{< relref "../notes/public/20240316170700-эмулятор_терминала_kitty.md" >}})
-   [Командные оболочки Unix]({{< relref "../notes/public/20250101T160600--командные_оболочки_unix.md" >}})


### <span class="section-num">11.10</span> Работа с файлами {#работа-с-файлами}

-   [Файловый менеджер Midnight Commander]({{< relref "../notes/public/20230826174000-фаиловыи_менеджер_midnight_commander.md" >}})


### <span class="section-num">11.11</span> Редакторы {#редакторы}

-   [Emacs]({{< relref "../notes/public/20201224162300-emacs.md" >}})
-   [Редактор VSCode]({{< relref "../notes/public/20251231T221400--vscode.md" >}})
-   [Редактор vim]({{< relref "../notes/public/20230704202200-редактор_vim.md" >}})
-   [Семейство редакторов vi]({{< relref "../notes/public/20250128T192200--семеиство_редакторов_vi.md" >}})


### <span class="section-num">11.12</span> Видео {#видео}


#### <span class="section-num">11.12.1</span> Просмотр {#просмотр}

-   [Проигрывание видеофайлов]({{< relref "../notes/public/20241212162600-проигрывание_видеофаилов.md" >}})


#### <span class="section-num">11.12.2</span> Видео-серверы {#видео-серверы}

-   [Plex Media Server]({{< relref "../notes/public/20250127T120200--plex_media_server.md" >}})


### <span class="section-num">11.13</span> Сетевые клиенты {#сетевые-клиенты}

-   [Почтовый клиент aerc]({{< relref "../notes/public/20240717185500-почтовыи_клиент_aerc.md" >}})
-   [Linux. Использование мессенджеров]({{< relref "../notes/public/20250626T123600--linux_использование_мессенджеров.md" >}})


#### <span class="section-num">11.13.1</span> Броузеры {#броузеры}

-   [Флаги запуска google chrome]({{< relref "../notes/public/20230228153100-флаги_запуска_google_chrome.md" >}})
-   [Броузер Nyxt]({{< relref "../notes/public/20231005204300-броузер_nyxt.md" >}})
-   [Броузер Qutebrowser]({{< relref "../notes/public/20241201184100-броузер_qutebrowser.md" >}})
-   [Firefox. Расширения]({{< relref "../notes/public/20240823202500-firefox_расширения.md" >}})
-   [Firefox. Настройка]({{< relref "../notes/public/20251122T190900--firefox_настроика.md" >}})
-   [Vim. Клавиатура. Броузеры]({{< relref "../notes/public/20230819184700-vim_клавиатура_броузеры.md" >}})
-   [Emacs. Клавиатура. Броузеры]({{< relref "../notes/public/20230819191500-emscs_клавиатура_броузеры.md" >}})


### <span class="section-num">11.14</span> Синхронизация файлов {#синхронизация-файлов}

-   [rclone]({{< relref "../notes/public/20221027142900-rclone.md" >}})
-   [Синхронизация файлов с помощью syncthing]({{< relref "../notes/public/20210801155800-синхронизация_фаилов_с_помощью_syncthing.md" >}})
-   [Скачать фотографии с google photo]({{< relref "../notes/public/20240601164200-скачать_фотографии_с_google_photo.md" >}})


### <span class="section-num">11.15</span> Телеконференции {#телеконференции}

-   [Аналоги программ для видеоконференций]({{< relref "../notes/public/20230323183200-аналоги_программ_для_видеоконференции.md" >}})


### <span class="section-num">11.16</span> Утилиты {#утилиты}

-   [Pdf. Поиск подстроки]({{< relref "../notes/public/20230627092800-pdf_поиск_подстроки.md" >}})
-   [Локальные поисковики]({{< relref "../notes/public/20230627105700-локальные_поисковики.md" >}})
-   [Linux. Архивирование]({{< relref "../notes/public/20240322134200-linux_архивирование.md" >}})
-   [Менеджер закладок buku]({{< relref "../notes/public/20240622204300-менеджер_закладок_buku.md" >}})


### <span class="section-num">11.17</span> Файлы конфигурации {#файлы-конфигурации}

-   [Управление файлами конфигурации. Домашний каталог. Chezmoi]({{< relref "../notes/public/20221028194900-управление_фаилами_конфигурации_chezmoi.md" >}})
-   [Управление файлами конфигурации. Домашний каталог. Репозиторий]({{< relref "../notes/public/20230730142400-управление_фаилами_конфигурации_домашнии_каталог_репозитории.md" >}})


## <span class="section-num">12</span> Профессиональные требования {#профессиональные-требования}

-   [Профессия Системный администратор]({{< relref "../notes/public/20210702120200-профессия_системныи_администратор.md" >}})
-   [Тест Лимончелли]({{< relref "../notes/public/20240127202600-тест_лимончелли.md" >}})


## <span class="section-num">13</span> Разработка {#разработка}

-   [Обновление хостовых ключей ssh Bitbucket Cloud]({{< relref "../notes/public/20230614174500-обновление_хостовых_ключеи_ssh_bitbucket_cloud.md" >}})
-   [Система контроля версий git]({{< relref "../notes/public/20201207154700-система_контроля_версии_git.md" >}})
-   [Система контроля версий Jujutsu]({{< relref "../notes/public/20251013T100900--система_контроля_версии_jujutsu.md" >}})


## <span class="section-num">14</span> Серверы приложений {#серверы-приложений}


### <span class="section-num">14.1</span> RSS {#rss}

-   [rss. Сервер FreshRSS]({{< relref "../notes/public/20250602T143700--rss_сервер_freshrss.md" >}})
-   [Подключение ресурсов через RSS]({{< relref "../notes/public/20220117171400-подключение_ресурсов_через_rss.md" >}})
-   [Emacs. Чтение rss. Elfeed]({{< relref "../notes/public/20250602T154400--emacs_чтение_rss_elfeed.md" >}})


### <span class="section-num">14.2</span> Drupal {#drupal}

-   [Перенос Drupal на другую машину]({{< relref "../notes/public/20220913194500-перенос_drupal_на_другую_машину.md" >}})


### <span class="section-num">14.3</span> OJS {#ojs}

-   [Open Journal Systems]({{< relref "../notes/public/20221022155000-open_journal_systems.md" >}})


### <span class="section-num">14.4</span> Ldap {#ldap}

-   [Перенос Openldap на другую машину]({{< relref "../notes/public/20230901201200-перенос_openldap_на_другую_машину.md" >}})
-   [Настройка Openldap]({{< relref "../notes/public/20230902195300-настроика_openldap.md" >}})


### <span class="section-num">14.5</span> Kerberos {#kerberos}

-   [Перенос kerberos на другую машину]({{< relref "../notes/public/20230903181300-перенос_kerberos_на_другую_машину.md" >}})


### <span class="section-num">14.6</span> Git {#git}

-   [Хостинг git. gitea]({{< relref "../notes/public/20231029185400-хостинг_git_gitea.md" >}})


### <span class="section-num">14.7</span> Хранилища {#хранилища}

-   [Файловое хранилище Seafile]({{< relref "../notes/public/20250408T122100--фаиловое_хранилище_seafile.md" >}})


## <span class="section-num">15</span> Разное {#разное}

-   [Сайт The Movie Database]({{< relref "../notes/public/20241114185600-саит_the_movie_database.md" >}})


## <span class="section-num">16</span> Сети {#сети}


### <span class="section-num">16.1</span> Оборудование {#оборудование}

-   [Администрирование Cisco]({{< relref "../notes/public/20210616123800-администрирование_cisco.md" >}})
-   [Администрирование Huawei]({{< relref "../notes/public/20240906153400-администрирование_huawei.md" >}})
-   [Mesh-системы]({{< relref "../notes/public/20241007162700-mesh_системы.md" >}})


### <span class="section-num">16.2</span> VLAN {#vlan}

-   [Linux. Настройка vlan]({{< relref "../notes/public/20240513103400-linux_настроика_vlan.md" >}})


### <span class="section-num">16.3</span> VPN {#vpn}

-   [VPN. L2TP+IPsec. Подключение клиента]({{< relref "../notes/public/20230205133500-vpn_l2tp_ipsec_подключение_клиента.md" >}})
-   [Подключение к Cisco VPN]({{< relref "../notes/public/20230819133400-подключение_к_cisco_vpn.md" >}})
-   [Настройка vpn-клиента Континент АП]({{< relref "../notes/public/20250205T183200--настроика_vpn_клиента_континент_ап.md" >}})
-   [WireGuard VPN]({{< relref "../notes/public/20251106T085300--wireguard_vpn.md" >}})
-   [Пиринговые VPN]({{< relref "../notes/public/20260115T161600--пиринговые_vpn.md" >}})


### <span class="section-num">16.4</span> Железо {#железо}

-   [Формат Small Form-factor Pluggable (SFP)]({{< relref "../notes/public/20230319163800-small_form_factor_pluggable_sfp.md" >}})


### <span class="section-num">16.5</span> Коммутаторы {#коммутаторы}

-   [DHCP snooping]({{< relref "../notes/public/20230905094900-dhcp_snooping.md" >}})


### <span class="section-num">16.6</span> Управление и мониторинг {#управление-и-мониторинг}

-   [Система мониторинга Observium]({{< relref "../notes/public/20230302154600-система_мониторинга_observium.md" >}})
-   [Система мониторинга LibreNMS]({{< relref "../notes/public/20230320150700-система_мониторинга_librenms.md" >}})
-   [Мониторинг пропускной способности и скорости сети]({{< relref "../notes/public/20230616113400-мониторинг_пропускнои_способности_и_скорости_сети.md" >}})
-   [Система управления сетью NetBox]({{< relref "../notes/public/20240619175200-система_управления_сетью_netbox.md" >}})


### <span class="section-num">16.7</span> Протоколы {#протоколы}

-   [Протокол IPv6]({{< relref "../notes/public/20230626193600-протокол_ipv6.md" >}})


#### <span class="section-num">16.7.1</span> Bittorrent {#bittorrent}

-   [bittorrent. Трекер opentracker]({{< relref "../notes/public/20240131211500-bittorrent_трекер_opentracker.md" >}})


### <span class="section-num">16.8</span> Сетевые сервисы {#сетевые-сервисы}


#### <span class="section-num">16.8.1</span> DNS {#dns}

-   [Domain Name System (DNS)]({{< relref "../notes/public/20230916194700-domain_name_system_dns.md" >}})


#### <span class="section-num">16.8.2</span> DHCP {#dhcp}

-   [Сервер DHCP Kea]({{< relref "../notes/public/20240618110700-сервер_dhcp_kea.md" >}})
-   [Сервер ISC DHCP]({{< relref "../notes/public/20240619152600-сервер_isc_dhcp.md" >}})
-   [DHCP snooping]({{< relref "../notes/public/20230905094900-dhcp_snooping.md" >}})
-   [Адресация IPv4 и IPv6. Настройка DHCP для IPv4]({{< relref "../notes/public/20220815202100-адресация_ipv4_и_ipv6_настроика_dhcp_для_ipv4.md" >}})
-   [Адресация IPv4 и IPv6. Настройка DHCPv6 для IPv6]({{< relref "../notes/public/20220817194800-адресация_ipv4_и_ipv6_настроика_dhcpv6_для_ipv6.md" >}})


#### <span class="section-num">16.8.3</span> Почта {#почта}

-   [Запросы по протоколу imap из командной строки]({{< relref "../notes/public/20240413172700-запросы_по_протоколу_imap_из_комманднои_строки.md" >}})


#### <span class="section-num">16.8.4</span> HTTP {#http}

-   [Web-сервер Nginx]({{< relref "../notes/public/20241205133600-web_сервер_nginx.md" >}})
-   [Обратный прокси-сервер Nginx Proxy Manager]({{< relref "../notes/public/20250412T131600--обратныи_прокси_сервер_nginx_proxy_manager.md" >}})


## <span class="section-num">17</span> Управление и мониторинг {#управление-и-мониторинг}

-   [Web консоль Cockpit]({{< relref "../notes/public/20220118172300-web_консоль_cockpit.md" >}})
-   [Система мониторинга LibreNMS]({{< relref "../notes/public/20230320150700-система_мониторинга_librenms.md" >}})
-   [Система мониторинга Observium]({{< relref "../notes/public/20230302154600-система_мониторинга_observium.md" >}})
-   [IPMI. Supermicro]({{< relref "../notes/public/20251027T184200--ipmi_supermicro.md" >}})


## <span class="section-num">18</span> Файловые системы {#файловые-системы}


### <span class="section-num">18.1</span> Локальные файловые системы {#локальные-файловые-системы}

-   [Файловая система btrfs]({{< relref "../notes/public/20210827113300-фаиловая_система_btrfs.md" >}})
-   [Дедупликация данных]({{< relref "../notes/public/20220526133100-дедупликация_данных.md" >}})
-   [Файловая система xfs]({{< relref "../notes/public/20230826195000-фаиловая_система_xfs.md" >}})


### <span class="section-num">18.2</span> Сетевые и распределённые файловые системы {#сетевые-и-распределённые-файловые-системы}

-   [Файловая система afs]({{< relref "../notes/public/20230828100400-фаиловая_система_afs.md" >}})
-   [Использование Яндекс-диска]({{< relref "../notes/public/20240625153200-использование_яндекс_диска.md" >}})
-   [Файловая система ipfs]({{< relref "../notes/public/20240830202700-фаиловая_система_ipfs.md" >}})
-   [Настройка NFS]({{< relref "../notes/public/20250817T201600--настроика_nfs.md" >}})


### <span class="section-num">18.3</span> Файловые системы объединения (union) {#файловые-системы-объединения--union}

-   [Файловая система mergerfs]({{< relref "../notes/public/20240128190400-фаиловая_система_mergerfs.md" >}})


## <span class="section-num">19</span> Форматы файлов {#форматы-файлов}


### <span class="section-num">19.1</span> csv {#csv}

-   [Формат CSV. csvkit]({{< relref "../notes/public/20230706182900-формат_csv_csvkit.md" >}})


### <span class="section-num">19.2</span> Офисные форматы файлов {#офисные-форматы-файлов}

-   [Конвертация документов. unoserver]({{< relref "../notes/public/20251122T180300--конвертация_документов_unoserver.md" >}})


### <span class="section-num">19.3</span> Epub {#epub}

-   [Epub. Утилиты]({{< relref "../notes/public/20260109T213700--epub_утилиты.md" >}})


## <span class="section-num">20</span> Шрифты {#шрифты}

-   [Шрифты в Linux]({{< relref "../notes/public/20211027113600-шрифты_в_linux.md" >}})


## <span class="section-num">21</span> Языки программирования {#языки-программирования}

-   [Язык программирования HCL]({{< relref "../notes/public/20221105180300-язык_программирования_hcl.md" >}})


## <span class="section-num">22</span> Ресурсы {#ресурсы}

-   Awesome Sysadmin: <https://github.com/awesome-foss/awesome-sysadmin>


## <span class="section-num">23</span> Серверы приложений {#серверы-приложений}

-   [Система управления событиями Indico]({{< relref "../notes/public/20240924111300-система_управления_событиями_indico.md" >}})
-   [Система управления обучением Moodle]({{< relref "../notes/public/20240915161000-система_управления_обучением_moodle.md" >}})


## <span class="section-num">24</span> Репозитории программного обеспечения {#репозитории-программного-обеспечения}

-   [Репозиторий программного обеспечения Entware]({{< relref "../notes/public/20241220T181800--репозитории_программного_обеспечения_entware.md" >}})
