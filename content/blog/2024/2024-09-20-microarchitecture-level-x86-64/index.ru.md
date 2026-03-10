---
title: "Варианты микроархитектуры x86"
author: ["Dmitry S. Kulyabov"]
date: 2024-09-20T20:16:00+03:00
lastmod: 2024-09-20T20:32:00+03:00
tags: ["hard"]
categories: ["computer-science"]
draft: false
slug: "microarchitecture-level-x86-64"
---

Варианты микроархитектуры x86-64.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Варианты микроархитектуры {#варианты-микроархитектуры}

-   Пропишем именование уровней и соответствующие расширения макроархитектуры.
-   x86-64-v1 : CMOV, CX8, FPU, FXSR, MMX, OSFXSR, SCE, SSE, SSE2;
-   x86-64-v2 : CMPXCHG16B, LAHF-SAHF, POPCNT, SSE3, SSE4_1, SSE4_2, SSSE3;
-   x86-64-v3 : AVX, AVX2, BMI1, BMI2, F16C, FMA, LZCNT, MOVBE, OSXSAVE;
-   x86-64-v4 : AVX512F, AVX512BW, AVX512CD, AVX512DQ, AVX512VL.


## <span class="section-num">2</span> Программное определение варианта микроархитектуры {#программное-определение-варианта-микроархитектуры}


### <span class="section-num">2.1</span> Флаг процессора {#флаг-процессора}

-   Флаги процессора можно определить через `/proc`-файловую систему:
    ```shell
    cat /proc/cpuinfo | grep "^flags.*" | uniq
    ```


### <span class="section-num">2.2</span> glibc {#glibc}

-   Можно запустить линкер:
    ```shell
    /lib64/ld-linux-x86-64.so.2 --help | grep supported
    ```


### <span class="section-num">2.3</span> x86-64-level {#x86-64-level}

-   Репозиторий: <https://github.com/HenrikBengtsson/x86-64-level>
-   По сути своей является скриптом, проверяющим наличие определённых флагов у процессора.
