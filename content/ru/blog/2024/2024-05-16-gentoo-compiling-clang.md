---
title: "Gentoo. Компиляция системы clang"
author: ["Dmitry S. Kulyabov"]
date: 2024-05-16T15:18:00+03:00
lastmod: 2026-02-10T11:37:00+03:00
tags: ["gentoo", "sysadmin", "linux"]
categories: ["computer-science"]
draft: false
slug: "gentoo-compiling-clang"
---

Переход на Clang для компиляции системы.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Обязательно должен быть запасной вариант с _GCC_.
-   На данный момент система не сможет скомпилировать все, что использует _Clang_.


## <span class="section-num">2</span> Установка {#установка}

-   Установите `llvm-libunwind`:
    ```shell
    emerge --deselect libunwind
    FEATURES="-protect-owned" emerge -vO llvm-libunwind
    ```
-   Установите _Clang_:
    ```shell
    emerge sys-devel/clang-runtime sys-devel/clang sys-libs/compiler-rt sys-libs/compiler-rt-sanitizers sys-devel/lld-toolchain-symlinks sys-devel/lld
    ```
-   Установите библиотеку для C++:
    ```shell
    emerge sys-libs/libcxxabi sys-libs/libcxx
    ```
-   Вместо `lld` можно использовать линкер `mold`:
    ```shell
    emerge mold
    ```


## <span class="section-num">3</span> Обновление системы {#обновление-системы}

-   Перекомпилим пакеты с библиотекой `libunwind`:
    ```shell
    revdep-rebuild --library libunwind -- --keep-going
    ```
-   Удалите библиотеку `libunwind`:
    ```shell
    emerge -cv libunwind
    ```
-   Необходимо перекомпилить программы, слинкованные со стандартной библиотекой `libstdc++`.
-   Проверьте, какие программы надо перекомпилить:
    ```shell
    revdep-rebuild --library libstdc++ -p
    ```
-   Перекомпилим эти пакеты:
    ```shell
    revdep-rebuild --library libstdc++ -- --keep-going
    ```


## <span class="section-num">4</span> Конфигурация {#конфигурация}


### <span class="section-num">4.1</span> Основная системная конфигурация {#основная-системная-конфигурация}


#### <span class="section-num">4.1.1</span> Общие настройки {#общие-настройки}

-   Файл `/etc/portage/make.conf`:
    ```conf-unix
    # this sources the PORTDIR_OVERLAY variable defined by layman. however, the variable expanded by layman was empty
    # source /var/db/repos/gentoo/local/layman/make.conf
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      /etc/portage/make.conf
    </div>
-   Подключение настроек конкретного хоста:
    ```conf-unix
    source /etc/portage/make.profile/make.conf
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 2:</span>
      /etc/portage/make.conf
    </div>


#### <span class="section-num">4.1.2</span> Настройка portage {#настройка-portage}

-   Выбор формата бинарных пакетов:
    ```conf-unix
    ## binpkg
    BINPKG_FORMAT="gpkg"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 3:</span>
      /etc/portage/make.conf
    </div>
-   Выбор формата сжатия бинарных пакетов:
    ```conf-unix
    BINPKG_COMPRESS="zstd"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 4:</span>
      /etc/portage/make.conf
    </div>
-   Формат каталога пакетов:
    ```conf-unix
    FEATURES=binpkg-multi-instance
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 5:</span>
      /etc/portage/make.conf
    </div>
-   Управление приоритетом:
    ```conf-unix
    ## https://wiki.gentoo.org/wiki/Portage_niceness
    ## Extremely low priority (per above)
    PORTAGE_SCHEDULING_POLICY="idle"
    ## Lowest priority
    PORTAGE_NICENESS="19"
    PORTAGE_IONICE_COMMAND="ionice -c 3 -p \${PID}"

    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 6:</span>
      /etc/portage/make.conf
    </div>


#### <span class="section-num">4.1.3</span> Настройка clang {#настройка-clang}

-   Опции для ядерных модулей:
    ```conf-unix
    ## This is added to make options by linux-mod.eclass
    BUILD_FIXES="LLVM=1 LLVM_IAS=1"
    CLANG_NO_DEFAULT_CONFIG=1

    COMMON_FLAGS="-O2 -march=native"
    CFLAGS="${COMMON_FLAGS}"
    CXXFLAGS="${COMMON_FLAGS}"

    # CFLAGS="${CFLAGS} -flto=thin"
    CXXFLAGS="${CFLAGS} ${CXXFLAGS}"
    #CFLAGS="${CFLAGS} -mllvm -extra-vectorizer-passes -mllvm -enable-cond-stores-vec -mllvm -slp-vectorize-hor-store -mllvm -enable-loopinterchange -mllvm -enable-loop-distribute -mllvm -enable-unroll-and-jam -mllvm -enable-loop-flatten -mllvm -interleave-small-loop-scalar-reduction -mllvm -unroll-runtime-multi-exit -mllvm -aggressive-ext-opt -fno-math-errno -fno-trapping-math -falign-functions=32 -funroll-loops -fno-semantic-interposition -fcf-protection=none -mharden-sls=none -fomit-frame-pointer -mprefer-vector-width=256 -flto"


    CC="clang"
    CPP="clang-cpp" # necessary for xorg-server and possibly other packages
    CXX="clang++"
    AR="llvm-ar"
    NM="llvm-nm"
    RANLIB="llvm-ranlib"
    OBJCOPY="llvm-objcopy"
    LD="mold"

    ## No need to set this, clang-common can handle this based on chosen USE flags
    # LDFLAGS="${LDFLAGS} -fuse-ld=lld"
    # LDFLAGS="${LDFLAGS} -fuse-ld=mold"
    # LDFLAGS="${LDFLAGS} -Wl,-O2 -Wl,--as-needed -Wl,--undefined-version"
    # LDFLAGS="${LDFLAGS} -rtlib=compiler-rt -unwindlib=libunwind"
    # LDFLAGS="${LDFLAGS} -flto"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 7:</span>
      /etc/portage/make.conf
    </div>


### <span class="section-num">4.2</span> Конфигурация окружения для каждого пакета {#конфигурация-окружения-для-каждого-пакета}

-   Можно задать компилятор для каждого пакета в отдельности в файле `/etc/portage/package.env`:
    ```conf-unix
    =app-emulation/virtualbox-7.0*			compiler-gcc    # ld.lld error
    =app-emulation/virtualbox-7.1*			compiler-gcc    # ld.lld error
    =app-emulation/virtualbox-7.2*			compiler-gcc    # ld.lld error
    =app-emulation/virtualbox-kvm-7.0*		compiler-gcc    # ld.lld error
    =app-emulation/virtualbox-kvm-7.1*		compiler-gcc    # ld.lld error
    =app-emulation/virtualbox-kvm-7.2*		compiler-gcc    # ld.lld error
    =dev-util/gengetopt-2.23*			compiler-gcc	#
    =sci-libs/coinor-osi-0.108.6			compiler-gcc		# bug: #919825
    =sci-mathematics/octave-8*			compiler-gcc
    app-accessibility/brltty			compiler-clang-mold
    app-arch/arj					compiler-gcc
    app-arch/lha					compiler-gcc
    app-cdr/cdrtools				compiler-gcc
    app-editors/emacs				compiler-gcc	# gcc-jit
    app-editors/wily				compiler-gcc
    app-editors/wily				compiler-gcc
    app-emulation/dosemu				compiler-gcc
    app-i18n/scim					compiler-gcc
    app-misc/ddcutil				compiler-gcc
    app-office/dia					compiler-gcc
    app-text/fbreader				compiler-gcc
    app-text/paper-clip				compiler-gcc
    app-text/tesseract				compiler-clang-mold
    app-text/texlive-core				compiler-gcc
    app-text/zathura-pdf-mupdf			compiler-clang-mold
    dev-db/cdb					compiler-gcc
    dev-db/libiodbc					compiler-clang-mold
    dev-db/mariadb					compiler-gcc
    dev-db/sqlite					compiler-gcc
    dev-debug/ddd					compiler-gcc
    dev-debug/gdb					compiler-gcc	# gcc itself
    dev-debug/systemtap				compiler-gcc
    dev-games/openscenegraph			compiler-gcc
    dev-haskell/network				compiler-clang
    dev-haskell/old-time				compiler-clang
    dev-haskell/resolv				compiler-gcc
    dev-java/commons-daemon				compiler-gcc
    dev-java/openjdk:11				compiler-gcc
    dev-java/openjdk:17				compiler-clang-mold
    dev-java/openjdk:21				compiler-clang-mold
    dev-java/openjdk:8				compiler-gcc
    dev-java/snappy					compiler-gcc
    dev-lang/gprolog				compiler-clang-mold
    dev-lang/harbour				compiler-gcc
    dev-lang/rust					compiler-gcc
    dev-lang/zig					compiler-gcc
    dev-libs/cereal					compiler-clang-mold-18
    dev-libs/efl					compiler-clang-mold-18
    dev-libs/ffcall					compiler-gcc
    dev-libs/intel-vc-intrinsics			compiler-gcc
    dev-libs/libayatana-appindicator		compiler-clang-mold
    dev-libs/libbpf					compiler-clang-mold
    dev-libs/libcdio				compiler-gcc
    dev-libs/libdnet				compiler-gcc
    dev-libs/libgamin				compiler-clang-mold
    dev-libs/libgudev				compiler-gcc
    dev-libs/liblouis				compiler-gcc
    dev-libs/liboil					compiler-gcc
    dev-libs/libphonenumber				compiler-clang-mold
    dev-libs/libpqxx				compiler-clang-mold-18
    dev-libs/log4cpp				compiler-gcc
    dev-libs/olm					compiler-gcc
    dev-libs/opencl-clang				compiler-clang-mold
    dev-libs/opencl-clang:15			compiler-gcc
    dev-libs/totem-pl-parser			compiler-clang-mold
    dev-libs/xmlrpc-c				compiler-gcc
    dev-lisp/ecl					compiler-gcc
    dev-perl/OpenGL					compiler-clang-mold
    dev-perl/OpenGL-GLUT				compiler-clang-mold
    dev-perl/PDL					compiler-clang-mold
    dev-perl/PGPLOT					compiler-clang-mold
    dev-python/cysignals				compiler-gcc
    dev-python/pygame				compiler-gcc
    dev-python/scipy				compiler-clang-mold
    dev-python/zstandard				compiler-gcc
    dev-qt/qtwebengine:5				compiler-clang-mold-18
    dev-qt/qtwebengine:6				compiler-clang-mold-18
    dev-tex/tectonic				compiler-gcc
    dev-util/android-tools				compiler-gcc
    dev-util/kdevelop				compiler-clang-mold-18
    dev-util/mingw64-toolchain			compiler-gcc	# gcc itself
    dev-util/yacc					compiler-gcc
    dev-vcs/cvs					compiler-gcc
    dev-vcs/darcs					compiler-clang
    gui-libs/gtk:4					compiler-clang
    kde-apps/step					compiler-clang-mold-18
    llvm-core/lldb					compiler-clang
    mail-client/thunderbird				compiler-gcc
    media-gfx/autopano-sift-C			compiler-gcc
    media-gfx/blender:4.0				compiler-gcc
    media-gfx/exact-image				compiler-gcc
    media-gfx/graphicsmagick			compiler-clang-mold
    media-gfx/inkscape				compiler-clang-mold
    media-gfx/openvdb				compiler-clang-mold-18
    media-gfx/povray				compiler-gcc
    media-gfx/sane-backends				compiler-gcc
    media-libs/avidemux-core			compiler-gcc
    media-libs/avidemux-plugins			compiler-gcc
    media-libs/exempi				compiler-gcc
    media-libs/intel-mediasdk			compiler-gcc
    media-libs/libdc1394				compiler-gcc
    media-libs/libdv				compiler-gcc
    media-libs/libfpx				compiler-gcc
    media-libs/libgphoto2				compiler-clang-mold
    media-libs/libopenraw				compiler-gcc
    media-libs/libquvi				compiler-gcc
    media-libs/libsidplay				compiler-gcc
    media-libs/openglide				compiler-gcc
    media-libs/tg_owt				compiler-gcc
    media-libs/urt					compiler-gcc
    media-sound/audacity				compiler-clang-mold
    media-sound/sox					compiler-clang-mold
    media-video/avidemux				compiler-gcc
    media-video/ffmpeg				compiler-clang-mold
    media-video/gpac				compiler-gcc
    media-video/mpv					compiler-clang-mold
    net-analyzer/rrdtool				compiler-clang-mold
    net-dns/bind-tools				compiler-clang-mold
    net-firewall/ipset				compiler-clang-mold
    net-fs/autofs					compiler-gcc
    net-fs/openafs					compiler-gcc
    net-fs/samba					compiler-clang-mold
    net-libs/gtk-vnc				compiler-clang-mold
    net-libs/libnftnl				compiler-clang-mold
    net-libs/serf					compiler-clang-mold
    net-libs/webkit-gtk				compiler-clang-mold-18
    net-misc/netkit-telnetd				compiler-gcc
    net-misc/omniORB				compiler-gcc
    net-misc/openssh-contrib			compiler-gcc
    net-misc/remmina				compiler-gcc
    net-nds/openldap				compiler-clang-mold
    net-print/gutenprint				compiler-gcc
    net-proxy/dante					compiler-gcc
    net-vpn/networkmanager-vpnc			compiler-gcc
    sci-libs/djbfft					compiler-gcc
    sci-libs/pdal					compiler-clang-mold-18
    sci-libs/vtk					compiler-clang-mold-18
    sci-mathematics/giac				compiler-gcc
    sci-mathematics/pari				compiler-gcc		# needs fix makefiles
    sci-mathematics/singular			compiler-gcc
    sci-physics/openmodelica			compiler-gcc
    sci-visualization/gnuplot			compiler-gcc
    sci-visualization/paraview			compiler-clang-mold-18
    sys-apps/flashrom				compiler-gcc
    sys-apps/fwupd-efi				compiler-gcc
    sys-apps/keyutils				compiler-clang-mold
    sys-apps/memtest86+				compiler-gcc
    sys-apps/systemd				compiler-gcc
    sys-auth/sssd					compiler-clang-mold
    sys-boot/gnu-efi				compiler-gcc
    sys-cluster/glusterfs				compiler-clang-mold
    sys-devel/bin86					compiler-gcc    # error: ISO C99
    sys-devel/binutils				compiler-gcc	# gcc itself	# configure: error: AR
    sys-devel/gcc					compiler-gcc	# gcc itself
    sys-fs/duperemove				compiler-gcc
    sys-libs/binutils-libs				compiler-gcc	# gcc itself
    sys-libs/ldb					compiler-clang-mold
    sys-libs/talloc					compiler-gcc
    sys-libs/tdb					compiler-clang-mold
    sys-libs/tevent					compiler-gcc
    www-client/chromium				compiler-clang
    x11-libs/agg					compiler-gcc
    x11-libs/fox					compiler-gcc
    x11-misc/redshift				compiler-gcc
    x11-misc/virtualgl				compiler-clang-mold
    dev-lang/python					compiler-gcc
    sys-boot/grub					compiler-gcc
    sci-libs/netcdf-cxx				compiler-gcc
    dev-lisp/clisp					compiler-gcc
    sys-libs/freeipmi				compiler-gcc
    dev-lang/ghc					compiler-gcc
    ```


### <span class="section-num">4.3</span> Конфигурация специальных окружений {#конфигурация-специальных-окружений}

-   Нужно задать конфигурации для разных компиляторов.


#### <span class="section-num">4.3.1</span> gcc {#gcc}

-   Конфигурация для компилятора _gcc_ в файле `/etc/portage/env/compiler-gcc`:
    ```conf-unix
    COMMON_FLAGS="-O2 -march=native"
    CFLAGS="${COMMON_FLAGS}"
    CXXFLAGS="${COMMON_FLAGS}"
    LDFLAGS="-Wl,--as-needed"

    CC="gcc"
    CXX="g++"
    CPP="gcc -E"
    AR="ar"
    NM="nm"
    RANLIB="ranlib"
    OBJCOPY="objcopy"
    STRIP="strip"
    LD="ld"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 8:</span>
      /etc/portage/env/compiler-gcc
    </div>


#### <span class="section-num">4.3.2</span> clang без LTO {#clang-без-lto}

-   Конфигурация для компилятора _clang_ без _LTO_ в файле `/etc/portage/env/compiler-clang-no-lto`:
    ```conf-unix
    CC="clang"
    CPP="clang-cpp"
    CXX="clang++"
    AR="llvm-ar"
    NM="llvm-nm"
    RANLIB="llvm-ranlib"
    OBJCOPY="llvm-objcopy"
    LD="lld"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 9:</span>
      /etc/portage/env/compiler-clang-no-lto
    </div>


#### <span class="section-num">4.3.3</span> clang {#clang}

-   Конфигурация для компилятора /clang/в файле `/etc/portage/env/compiler-clang`:
    ```conf-unix
    CC="clang"
    CPP="clang-cpp"
    CXX="clang++"
    AR="llvm-ar"
    NM="llvm-nm"
    RANLIB="llvm-ranlib"
    OBJCOPY="llvm-objcopy"
    LD="lld"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 10:</span>
      /etc/portage/env/compiler-clang
    </div>


#### <span class="section-num">4.3.4</span> clang + mold {#clang-plus-mold}

```conf-unix
# Normal settings here
COMMON_FLAGS="-O2 -march=native"
CFLAGS="${COMMON_FLAGS}"
CXXFLAGS="${COMMON_FLAGS}"
CLANG_NO_DEFAULT_CONFIG=1

CC="clang"
CPP="clang-cpp" # necessary for xorg-server and possibly other packages
CXX="clang++"
AR="llvm-ar"
NM="llvm-nm"
RANLIB="llvm-ranlib"
OBJCOPY="llvm-objcopy"
LD="mold"

LDFLAGS="${LDFLAGS} -fuse-ld=mold"
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 11:</span>
  /etc/portage/env/compiler-clang-mold
</div>


#### <span class="section-num">4.3.5</span> clang-18 + mold {#clang-18-plus-mold}

```conf-unix
# Normal settings here
COMMON_FLAGS="-O2 -march=native"
CFLAGS="${COMMON_FLAGS}"
CXXFLAGS="${COMMON_FLAGS}"
CLANG_NO_DEFAULT_CONFIG=1

CC="clang-18"
CPP="clang-cpp-18"
CXX="clang++-18"
AR="llvm-ar"
NM="llvm-nm"
RANLIB="llvm-ranlib"
OBJCOPY="llvm-objcopy"
LD="mold"
LDFLAGS="${LDFLAGS} -fuse-ld=mold"
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 12:</span>
  /etc/portage/env/compiler-clang-mold-18
</div>


#### <span class="section-num">4.3.6</span> clang-19 + mold {#clang-19-plus-mold}

```conf-unix
# Normal settings here
COMMON_FLAGS="-O2 -march=native"
CFLAGS="${COMMON_FLAGS}"
CXXFLAGS="${COMMON_FLAGS}"
CLANG_NO_DEFAULT_CONFIG=1

CC="clang-19"
CPP="clang-cpp-19"
CXX="clang++-19"
AR="llvm-ar"
NM="llvm-nm"
RANLIB="llvm-ranlib"
OBJCOPY="llvm-objcopy"
LD="mold"
LDFLAGS="${LDFLAGS} -fuse-ld=mold"
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 13:</span>
  /etc/portage/env/compiler-clang-mold-19
</div>


#### <span class="section-num">4.3.7</span> clang + binutils {#clang-plus-binutils}

-   Конфигурация для компилятора /clang/в файле `/etc/portage/env/compiler-clang-binutils`:
    ```conf-unix
    CC="clang"
    CPP="clang-cpp"
    CXX="clang++"
    AR="ar"
    NM="nm"
    RANLIB="ranlib"
    OBJCOPY="objcopy"
    STRIP="strip"
    LD="ld"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 14:</span>
      /etc/portage/env/compiler-clang-binutils
    </div>


## <span class="section-num">5</span> Компиляция ядра {#компиляция-ядра}

-   Ядро Linux можно скомпилировать с помощью _Clang_ и набора инструментов _LLVM_, определив переменную среды:
    ```shell
    LLVM=1
    ```
-   Чтобы настроить специальные параметры ядра _Clang_, такие как оптимизация времени компоновки или целостность потока управления, выполните следующую команду:
    ```shell
    LLVM=1 make menuconfig
    ```
-   Далее скомпилируйте ядро ​​как обычно:
    ```shell
    LLVM=1 make
    ```
-   Раньше необходимо было объявить `LLVM_IAS=1` для использования внутреннего ассемблера Clang для ядра.
-   Это больше не требуется, поскольку `LLVM=1` теперь включён по умолчанию.


## <span class="section-num">6</span> C++ ABI {#c-plus-plus-abi}

-   Для Clang по умолчанию устанавливается библиотека C++ `libcxx`.
-   При компиляции с помощью _gcc_ используется библиотека `libstdc++`.
-   Необходимо, как минимум, перекомпилить приложения, использующие библиотеку `libstdc++`:
    ```shell
    revdep-rebuild --library libstdc++ -- -v --keep-going
    ```


## <span class="section-num">7</span> Ресурсы {#ресурсы}

-   <https://wiki.gentoo.org/wiki/Clang>
-   <https://wiki.gentoo.org/wiki/Clang/Bootstrapping>
