---
title: "Linux. Пакетные менеджеры"
author: ["Dmitry S. Kulyabov"]
date: 2025-10-14T20:15:00+03:00
lastmod: 2025-10-14T20:35:00+03:00
tags: ["linux", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "linux-package-managers"
---

Linux. Пакетные менеджеры.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Пакетные менеджеры по дистрибутивам Linux {#пакетные-менеджеры-по-дистрибутивам-linux}


### <span class="section-num">1.1</span> Debian и его производные (например, Ubuntu) {#debian-и-его-производные--например-ubuntu}


#### <span class="section-num">1.1.1</span> apt (Advanced Package Tool) {#apt--advanced-package-tool}

-   Основной пакетный менеджер для работы с пакетами DEB.
-   Позволяет управлять программами через командную строку, работает с репозиториями, автоматически разрешает зависимости.
-   Код для работы:
    -   `apt update` --- обновление списка пакетов;
    -   `apt install <имя_пакета>` --- установка пакета;
    -   `apt remove <имя_пакета>` --- удаление пакета.
-   Сайт: <https://www.debian.org>.


#### <span class="section-num">1.1.2</span> pacstall {#pacstall}

-   Репозиторий: <https://github.com/pacstall/pacstall>
-   Сайт: <https://pacstall.dev/>
-   Сделан по концепции AUR.
-   Установка программ без необходимости искать информацию в репозиториях.
-   Поддерживает создание собственных пакетов из двоичных файлов, репозиториев git, appimages, пакетов `.deb`.


### <span class="section-num">1.2</span> Red Hat, Fedora, CentOS {#red-hat-fedora-centos}


#### <span class="section-num">1.2.1</span> YUM (Yellowdog Updater, Modified) {#yum--yellowdog-updater-modified}

-   Использовался для управления пакетами RPM в этих дистрибутивах.
-   Предоставляет удобный интерфейс для установки, обновления и удаления пакетов.
-   Код для работы:
    -   `yum install <имя_пакета>` --- установка пакета;
    -   `yum update` --- обновление пакетов;
    -   `yum remove <имя_пакета>` --- удаление пакета.
-   Сайт: <https://fedoraproject.org>.
-   Устаревший. Заменён на dnf.


#### <span class="section-num">1.2.2</span> DNF (Dandified YUM) {#dnf--dandified-yum}

-   Преемник YUM.
-   Предлагает улучшенную производительность и более удобный интерфейс.
-   Поддерживает работу с модулями и группами пакетов.
-   Код для работы:
    -   `dnf install <имя_пакета>` --- установка пакета;
    -   `dnf update` --- обновление пакетов.
-   Сайт: <https://dnf.readthedocs.io>.


### <span class="section-num">1.3</span> Arch Linux и его производные (например, Manjaro) {#arch-linux-и-его-производные--например-manjaro}


#### <span class="section-num">1.3.1</span> Pacman {#pacman}

-   Основной пакетный менеджер.
-   Работает с пакетами в формате TAR.XZ.
-   Отличается простотой и эффективностью, имеет интегрированную систему проверки целостности пакетов.
-   Код для работы:
    -   `pacman -S <имя_пакета>` --- установка пакета;
    -   `pacman -Ru <имя_пакета>` --- обновление пакета.
-   Сайт: <https://archlinux.org>.


#### <span class="section-num">1.3.2</span> AUR (Arch User Repository) {#aur--arch-user-repository}

-   Репозиторий для пользовательских пакетов в Arch Linux и его производных.
-   Содержит пакеты, которые не включены в официальные репозитории.
-   Для работы с AUR часто используются вспомогательные инструменты, например, `yay` или `trizen`.
-   Код для работы: `yay -S <имя_пакета>` для установки через `yay`.
-   Сайт: <https://aur.archlinux.org>.


#### <span class="section-num">1.3.3</span> Pamac {#pamac}

-   Графический пакетный менеджер для дистрибутивов на базе Arch (например, Manjaro).
-   Упрощает установку и управление пакетами, поддерживает работу с официальными репозиториями, AUR и другими источниками пакетов.


### <span class="section-num">1.4</span> openSUSE {#opensuse}


#### <span class="section-num">1.4.1</span> Zypper {#zypper}

-   Основной пакетный менеджер для управления программным обеспечением.
-   Код для работы:
    -   `zypper install <имя_пакета>` --- установка пакета;
    -   `zypper update` --- обновление пакетов;
    -   `zypper remove <имя_пакета>` --- удаление пакета.
-   Сайт: <https://opensuse.org>.


### <span class="section-num">1.5</span> Gentoo {#gentoo}


#### <span class="section-num">1.5.1</span> Portage {#portage}

-   Основной пакетный менеджер, позволяющий компилировать пакеты из исходного кода с использованием системы ebuild.
-   Код для работы: `emerge <имя_пакета>` --- установка и управление пакетами.
-   Сайт: <https://gentoo.org>.


## <span class="section-num">2</span> Менеджеры пакетов-контейнеров {#менеджеры-пакетов-контейнеров}


### <span class="section-num">2.1</span> Snap {#snap}

-   Кросс-дистрибутивный пакетный менеджер.
-   Разработан Canonical.
-   Позволяет устанавливать приложения в контейнерах, что обеспечивает изоляцию и портативность.
-   Код для работы: `snap install <имя_пакета>`.
-   Сайт: <https://snapcraft.io>.


### <span class="section-num">2.2</span> Flatpak {#flatpak}

-   Кросс-дистрибутивный менеджер.
-   Обеспечивает изолированную среду для приложений.
-   Поддерживает установку приложений из централизованных репозиториев.
-   Код для работы: `flatpak install <имя_пакета>`.
-   Сайт: <https://flatpak.org>.
