---
title: "MinGW. Приложения Unix под Windows"
author: ["Dmitry S. Kulyabov"]
date: 2023-09-22T13:22:00+03:00
lastmod: 2023-09-28T16:19:00+03:00
tags: ["sysadmin", "windows"]
categories: ["computer-science"]
draft: false
slug: "mingw-unix-applications-windows"
---

MinGW. Приложения Unix под Windows.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://osdn.net/projects/mingw/>.
-   MinGW (англ. Minimalist GNU for Windows), ранее mingw32.
-   Набор инструментов разработки программного обеспечения для создания приложений под Windows.
-   Включает в себя компилятор, родной программный порт GNU Compiler Collection (GCC) под Windows вместе с набором свободно распространяемых библиотек импорта и заголовочных файлов для Windows API.
-   В MinGW включены расширения для библиотеки времени выполнения Microsoft Visual C++ для поддержки функциональности C99.
-   Поддерживает стандарт C++11.


## <span class="section-num">2</span> Отличия от Cygwin {#отличия-от-cygwin}

-   Цель Cygwin --- предоставить полный слой POSIX (подобный тому, который находится в Linux и других Unix-системах) над Windows, жертвуя производительностью там, где это необходимо для совместимости.
-   Цель MinGW --- предоставление нативной функциональности и производительности посредством прямых вызовов Windows API.
-   В отличие от Cygwin, MinGW не нуждается в DLL-слое совместимости и, таким образом, программы не обязаны распространяться с исходным кодом.
-   Вследствие того, что MinGW использует вызовы Win32 API, он не может предоставить полного POSIX API.
-   Нельзя скомпилировать некоторые приложения Unix, которые могут быть скомпилированы с Cygwin (приложения, требующие `fork()`, `mmap()` или `ioctl()`).


## <span class="section-num">3</span> Компоненты MinGW {#компоненты-mingw}

-   GNU toolchain (gcc, binutils).
-   Компонент MSYS (Minimal SYStem) предоставляет win32-порты окружения легковесной Unix-подобной оболочки, включающей rxvt и набор инструментов POSIX.
