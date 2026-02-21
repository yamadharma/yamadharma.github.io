---
title: "LaTeX. Пакет unicode-math"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-11T20:26:00+03:00
lastmod: 2025-07-11T21:17:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex-unicode-math"
---

LaTeX. Пакет unicode-math.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Пакет unicode-math предназначен для работы с Unicode-символами в математических формулах.
-   Позволяет использовать широкий спектр математических символов напрямую в исходном коде документа и поддерживает OpenType-шрифты.
-   CTAN: <https://ctan.org/pkg/unicode-math>
-   Репозиторий: <https://github.com/latex3/unicode-math>
-   Пакет требует компиляторов XeLaTeX или LuaLaTeX.


## <span class="section-num">2</span> Основные возможности {#основные-возможности}

-   Поддержка Unicode-символов
    -   Позволяет вводить математические символы (например, ∂, ∀, ∫) напрямую, без использования команд LaTeX. Например, вместо `\alpha` можно писать `α`.

-   Совместимость со шрифтами
    -   Поддерживает шрифты с OpenType-математикой, такие как:
        -   Latin Modern Math
        -   STIX Two Math
        -   XITS Math
        -   Asana Math
        -   Fira Math

-   Расширенные возможности форматирования
    -   Автоматическое определение стилей (курсив, жирный, sans-serif)
    -   Поддержка многострочных формул и сложных конструкций
    -   Совместимость с пакетами `amsmath` и `mathtools`


## <span class="section-num">3</span> Подключение пакета {#подключение-пакета}

-   Для использования добавьте в преамбулу:

<!--listend-->

```tex
\usepackage{unicode-math}
\setmathfont{Latin Modern Math} % Пример шрифта
```


## <span class="section-num">4</span> Особенности и рекомендации {#особенности-и-рекомендации}

-   Работа с кириллицей и греческими буквами
    -   В математических формулах используйте команды `\text{}` для текстовых символов:
        ```tex
        $\text{Привет} \quad \text{αβγ}$
        ```

-   Команды для математического шрифта
    -   Пакет вводит новые команды для разных стилей:
        -   `\symup` --- upright (прямой)
        -   `\symit` --- italic (курсив)
        -   `\symbf` --- bold (жирный)
        -   `\symsf` --- sans-serif (гротеск)

-   Настройка стилей и версий математики
    -   Можно создавать альтернативные версии математических шрифтов:


## <span class="section-num">5</span> Список поддерживаемых шрифтов {#список-поддерживаемых-шрифтов}

| Шрифт             | Тип           | Особенности                     |
|-------------------|---------------|---------------------------------|
| Latin Modern Math | Бесплатный    | Стандарт для LaTeX              |
| STIX Two Math     | Бесплатный    | Широкая поддержка символов      |
| XITS Math         | Бесплатный    | Совместимость с Times New Roman |
| Cambria Math      | Проприетарный | Встроенный в Windows            |
| Minion Math       | Проприетарный | Высокий уровень детализации     |


## <span class="section-num">6</span> Дополнительные рекомендации {#дополнительные-рекомендации}

-   Порядок загрузки пакетов
    -   `hyperref` рекомендуется подключить последним, чтобы избежать конфликтов:
        ```tex
        \usepackage{unicode-math}
        \usepackage{hyperref}
        ```

-   Работа с разными стилями шрифтов
    -   Для заголовков с нестандартными шрифтами (например, sans-serif) используйте:
        ```tex
        \setmathfont[version=sans]{Fira Math}
        \mathversion{sans}  % Активация sans-serif версии
        ```
    -   <https://tex.stackexchange.com/questions/546828/math-mode-in-titles-doesnt-match-font>

-   Избегание `\mathbf` для греческих букв
    -   Команда `\mathbf` может некорректно работать с греческими символами.
    -   Используйте `\symbf` из `unicode-math`:
        ```tex
        \symbf{\alpha}  % Жирный греческий символ
        ```

---


## <span class="section-num">7</span> Совместимость с другими пакетами {#совместимость-с-другими-пакетами}


### <span class="section-num">7.1</span> Совместимость unicode-math и hyperref {#совместимость-unicode-math-и-hyperref}

-   Все символы `unicode-math` работают корректно внутри гиперссылок.
-   Можно использовать команды `unicode-math` (`\symup`, `\symit`, `\symbf`) внутри ссылок.


#### <span class="section-num">7.1.1</span> Основные проблемы {#основные-проблемы}

<!--list-separator-->

1.  Предупреждения о недопустимых токенах

    -   При компиляции документа с математическими символами в заголовках появляются предупреждения:
        ```tex
        Package hyperref Warning: Token not allowed in a PDF string (PDFDocEncoding):
        (hyperref)                removing \tau_2 on input line ...
        ```
    -   PDFDocEncoding не поддерживает большинство математических символов Unicode.
    -   `hyperref` автоматически преобразует заголовки в закладки, что вызывает конфликты при наличии сложных символов.

    -   Решение: Используйте команду `\texorpdfstring` для указания альтернативного текста для закладок pdf:
        ```tex
        \section{\texorpdfstring{$\tau_2$}{tau2}}
        \section{\texorpdfstring{$\varepsilon$}{$\symit{\epsilon}$}}
        ```

    -   Это позволяет сохранить математический символ в тексте документа, но использовать текстовое представление в закладках.

<!--list-separator-->

2.  Конфликты шрифтов и стилей

    -   В заголовках секций математические символы могут отображаться некорректно (например, не жирным шрифтом).
    -   Решение:
        -   Для сложных случаев используйте `pdfencoding=auto` и `psdextra` в опциях `hyperref`:
            ```tex
            \usepackage[pdfencoding=auto, psdextra]{hyperref}
            \usepackage{textgreek}
            \pdfstringdefDisableCommands{\def\varepsilon{\textepsilon}}
            ```

            -   Вариант `pdfencoding=auto` или `unicode` включает закладки в Unicode с большим количеством символов.
            -   Вариант `psdextra` определяет множество математических символов.
            -   `\pdfstringdefDisableCommands` может использоваться для определения строки замены закладки для команд.
        -   Настройте альтернативные версии шрифтов для заголовков:
            ```tex
            \setmathfont[version=bold]{Latin Modern Math}
            \mathversion{bold}  % Активация жирного стиля
            ```
    -   <https://tex.stackexchange.com/questions/251491/math-symbol-in-section-heading>
