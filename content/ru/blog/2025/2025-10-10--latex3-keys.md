---
title: "LaTeX3. Работа с ключами"
author: ["Dmitry S. Kulyabov"]
date: 2025-10-10T21:30:00+03:00
lastmod: 2025-10-10T21:38:00+03:00
tags: ["programming", "latex3"]
categories: ["computer-science"]
draft: false
slug: "latex3-keys"
---

LaTeX3. Работа с ключами.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Интерфейс `\keys_define:nn` {#интерфейс-keys-define-nn}


### <span class="section-num">1.1</span> Общая информация {#общая-информация}

-   Интерфейс `\keys_define:nn` в LaTeX3 есть инструмент для определения и управления ключами.

-   Синтаксис:

<!--listend-->

```tex
\keys_define:nn { <group name> } { <key definitions> }
```

-   Параметры:
    -   `<group name>` --- имя группы ключей.
        -   Это пространство имён, которое помогает избежать конфликтов имён при использовании ключей в разных частях документа или в разных пакетах.
        -   Например, `mypackage/keys` указывает, что ключи принадлежат пакету `mypackage`.
    -   `<key definitions>` --- список определений ключей.
        -   Каждый ключ описывается своими свойствами и поведением.
        -   В этом списке можно задать:
            -   тип ключа (логический, строковый, целочисленный и др.);
            -   значение по умолчанию;
            -   обработчики, которые будут выполняться при задании ключа;
            -   проверки корректности значений, которые передаются ключу.


### <span class="section-num">1.2</span> Детальное описание работы {#детальное-описание-работы}


#### <span class="section-num">1.2.1</span> Определение типов ключей {#определение-типов-ключей}

-   Логический ключ (bool): принимает значения `true` или `false`.
    -   Пример: `mybool.bool_set:N = \l_mypackage_mybool_bool`.
-   Строковый ключ (tl): для хранения текстовых значений.
    -   Пример: `mystring.tl_set:N = \l_mypackage_mystring_tl`.
-   Целочисленный ключ (int): для хранения целых чисел.
    -   Пример: `myint.int_set:N = \l_mypackage_myint_int`.


#### <span class="section-num">1.2.2</span> Установка начальных значений {#установка-начальных-значений}

-   Для каждого ключа можно указать начальное значение с помощью `.initial:n`.
-   Например:
    ```tex
    mybool.initial:n = { false },
    mystring.initial:n = { Default String },
    myint.initial:n = { 42 }
    ```


#### <span class="section-num">1.2.3</span> Обработчики ключей {#обработчики-ключей}

-   Можно определить специальные команды, которые будут выполняться при установке ключа.
-   Это позволяет реализовывать сложное поведение в зависимости от заданных параметров.


#### <span class="section-num">1.2.4</span> Проверка корректности значений {#проверка-корректности-значений}

-   С помощью дополнительных опций можно проверять корректность значений, передаваемых ключу, что повышает надёжность использования ключей.


#### <span class="section-num">1.2.5</span> Пример полного определения ключей: {#пример-полного-определения-ключей}

```tex
\keys_define:nn { mypackage/keys } {
  mybool.bool_set:N = \l_mypackage_mybool_bool,
  mybool.initial:n = { false },
  mystring.tl_set:N = \l_mypackage_mystring_tl,
  mystring.initial:n = { Default String },
  myint.int_set:N = \l_mypackage_myint_int,
  myint.initial:n = { 42 },
  % Дополнительные ключи и их настройки
}
```


#### <span class="section-num">1.2.6</span> Использование определённых ключей в документе {#использование-определённых-ключей-в-документе}

-   После определения ключей их можно использовать с помощью команды `\keys_set:nn`:

<!--listend-->

```tex
\keys_set:nn { mypackage/keys } {
  mybool = true,
  mystring = { Custom String },
  myint = 100
}
```

-   Теперь переменные `\l_mypackage_mybool_bool`, `\l_mypackage_mystring_tl` и `\l_mypackage_myint_int` будут содержать заданные значения.
