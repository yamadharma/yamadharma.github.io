---
title: "Gentoo. Пакет eclean-kernel"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-13T20:38:00+03:00
lastmod: 2025-07-13T21:00:00+03:00
tags: ["gentoo", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "gentoo-eclean-kernel"
---

Gentoo. Пакет eclean-kernel.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Служит для удаления старых ядер.
-   Репозиторий: <https://github.com/projg2/eclean-kernel/>
-   PyPi: <https://pypi.org/project/eclean-kernel/>
-   Описание использования:
    -   <https://wiki.gentoo.org/wiki/Kernel/Removal>
    -   <https://wiki.gentoo.org/wiki/Kernel/Removal/ru>


## <span class="section-num">2</span> Установка {#установка}

-   Установите пакет через `emerge`:
    ```shell
    emerge app-admin/eclean-kernel
    ```


## <span class="section-num">3</span> Основные параметры {#основные-параметры}

-   `-l` (`--list-kernels`) : выводит список установленных ядер:
    ```shell
    eclean-kernel -l
    ```

-   `-a` (`--all`) : удаляет все ядра, кроме текущего:
    ```shell
    eclean-kernel -a
    ```

-   `-n X` (`--num X`) --- сохраняет последние `X` ядер, удаляя остальные:
    ```shell
    eclean-kernel -n 3  # Сохраняет 3 последних ядра
    ```


## <span class="section-num">4</span> Дополнительные параметры {#дополнительные-параметры}

-   `-d` (`--destructive`) : принудительное удаление ядер, даже если они используются загрузчиком.
-   `-b BOOTLOADER` (`--bootloader BOOTLOADER`) --- указывает тип загрузчика (`grub2`, `lilo`, `grub`, `yaboot`).
-   `-L LAYOUT` (`--layout LAYOUT`) : задаёт схему расположения файлов (`auto`, `std`, `blspec`).
-   `-x EXCLUDE` (`--exclude EXCLUDE`) : исключает части ядра из удаления (например, `vmlinuz, initramfs`).


## <span class="section-num">5</span> Примеры использования {#примеры-использования}

-   Сохранение 3 последних ядер:
    ```shell
    eclean-kernel -n 3 -l  # Вывод списка перед очисткой
    eclean-kernel -n 3     # Выполнение очистки
    ```

-   Удаление всех ядер, кроме текущего:
    ```shell
    eclean-kernel -a
    ```

-   Проверка действий перед выполнением:
    ```shell
    eclean-kernel -p -n 2  # Имитация удаления
    ```


## <span class="section-num">6</span> Рекомендации {#рекомендации}

-   Всегда сохраняйте минимум 2 предыдущих ядра для возможности отката в случае проблем.
-   Проверяйте конфигурацию загрузчика после очистки, чтобы избежать ошибок при загрузке.
-   Используйте `emerge --depclean` для удаления исходных кодов ядер, если они больше не нужны.


## <span class="section-num">7</span> Ручное удаление ядра {#ручное-удаление-ядра}

-   Если eclean-kernel не удаляет все файлы, можно очистить каталоги вручную:

<!--listend-->

```shell
rm -r /usr/src/linux-X.Y.Z       # Исходные коды
rm -r /lib/modules/X.Y.Z        # Модули ядра
rm /boot/vmlinuz-X.Y.Z          # Бинарные файлы в /boot
```


## <span class="section-num">8</span> Ошибки и решения {#ошибки-и-решения}

-   Если утилита не находит ядра, проверьте переменную `BOOT_ORDER` в `/etc/portage/make.conf`.
-   При ошибках с загрузчиком обновите его конфигурацию вручную (например, `grub-mkconfig -o /boot/grub/grub.cfg`).
