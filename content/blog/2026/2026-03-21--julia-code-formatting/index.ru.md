---
title: "Julia. Форматирование кода"
author: ["Dmitry S. Kulyabov"]
date: 2026-03-21T14:57:00+03:00
lastmod: 2026-03-21T16:40:00+03:00
tags: ["julia", "programming"]
categories: ["computer-science"]
draft: false
slug: "julia-code-formatting"
---

Julia. Форматирование кода.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Пакет JuliaFormatter.jl {#пакет-juliaformatter-dot-jl}


### <span class="section-num">1.1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/domluna/JuliaFormatter.jl>


### <span class="section-num">1.2</span> Установка {#установка}

-   Установите пакет через REPL:

<!--listend-->

```julia
using Pkg
Pkg.add("JuliaFormatter")
```

-   Или в командной строке:

<!--listend-->

```shell
julia -e 'using Pkg; Pkg.add("JuliaFormatter")'
```


### <span class="section-num">1.3</span> Использование из REPL {#использование-из-repl}

-   Вызовите `format` на файле или каталоге:
    ```julia
    using JuliaFormatter
    format("myfile.jl")                # форматирует один файл
    format("src/")                     # форматирует все .jl файлы в папке
    format(".")                        # рекурсивно форматирует всё в текущей директории
    ```

-   По умолчанию используется стиль BlueStyle --- стандартный для Julia.
-   Можно явно указать другой стиль (например, `YASStyle`, `DefaultStyle`):
    ```julia
    format("src/", style=YASStyle())
    ```


### <span class="section-num">1.4</span> Использование из командной строки {#использование-из-командной-строки}

-   После установки пакета выполните:
    ```shell
    julia -e 'using JuliaFormatter; format(".")'
    ```


### <span class="section-num">1.5</span> Отдельный инструмент командной строки {#отдельный-инструмент-командной-строки}

-   Начиная с версии 2.2.0, JuliaFormatter предоставляет исполняемый файл для работы из командной строки `jlfmt`.

-   Установка:
    ```julia
    pkg> app add JuliaFormatter
    ```

-   Применение:
    ```shell
    # Format a file and write to stdout
    jlfmt src/file.jl

    # Format a file in place
    jlfmt --inplace src/file.jl

    # Check if all files in a directory are already formatted with verbose mode
    jlfmt --check -v src/

    # Format all files in a directory with multiple threads
    jlfmt --threads=6 -- --inplace -v src/

    # Show diff without modifying files
    jlfmt --diff src/file.jl
    ```


### <span class="section-num">1.6</span> Рекомендации по стилю {#рекомендации-по-стилю}

-   BlueStyle --- де-факто стандарт, используется в большинстве пакетов Julia. Он соответствует официальному руководству по стилю.
-   Для проектов можно зафиксировать стиль, добавив в корень файл `.JuliaFormatter.toml`:
    ```toml
    style = "blue"
    margin = 92
    indent = 4
    ```

-   Этот файл будет применяться при вызове `format(".")` без дополнительных параметров.


### <span class="section-num">1.7</span> Форматирование без изменения файла (проверка) {#форматирование-без-изменения-файла--проверка}

-   Если нужно только проверить, требуется ли форматирование, используйте:
    ```julia
    format("src/", overwrite=false)   # покажет изменения, но не применит их
    ```


## <span class="section-num">2</span> Пакет Runic.jl {#пакет-runic-dot-jl}


### <span class="section-num">2.1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/fredrikekre/Runic.jl>


## <span class="section-num">3</span> Сравнение Runic.jl и JuliaFormatter.jl {#сравнение-runic-dot-jl-и-juliaformatter-dot-jl}


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   JuliaFormatter.jl предлагает максимальную гибкость: вы можете настроить практически всё --- от количества пробелов до того, как форматировать kwargs и цепочки вызовов.
    -   Это удобно для проектов, где команда уже имеет устоявшиеся предпочтения.
-   Runic.jl следует философии `gofmt`: полное отсутствие конфигурации.
    -   Это устраняет дискуссии о форматировании в код-ревью.


### <span class="section-num">3.2</span> Таблица {#таблица}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Сравнение Runic.jl и JuliaFormatter.jl
</div>

| Характеристика        | JuliaFormatter.jl                                      | Runic.jl                                                         |
|-----------------------|--------------------------------------------------------|------------------------------------------------------------------|
| Философия             | Гибкий, настраиваемый под ваш стиль                    | Не имеет конфигурации                                            |
| Подход                | Ваше мнение --- ваш выбор                              | Стиль gofmt: никто не любит, но все его используют               |
| Конфигурация          | `.JuliaFormatter.toml` с множеством опций              | Отсутствует --- только вкл/выкл через комментарии                |
| Встроенные стили      | BlueStyle, YASStyle, SciMLStyle, DefaultStyle          | Только один фиксированный стиль                                  |
| Форматирование блоков | Настраиваемое                                          | Всегда начинаются и заканчиваются с новой строки                 |
| Отступы               | Настраиваемые (по умолчанию 4)                         | Фиксированные 4 пробела                                          |
| Ограничение строки    | margin (по умолчанию 92)                               | Нет --- "используйте Enter или рефакторите код"                  |
| Специфичные правила   | alignAssignment, alwaysForIn, pipeToFunctionCall и др. | Обработка "жесткой" и "мягкой" индентации для цепочек операторов |
| Интеграция VS Code    | Встроенная в расширение Julia                          | Через стороннее расширение Custom Local Formatters               |
| Интеграция Neovim     | Через conform.nvim                                     | Через conform.nvim (с ручной настройкой)                         |
| CLI                   | format(), format_file(), format_text(), jlfmt          | runic с флагами --check, --diff, --inplace                       |
| Git интеграция        | Можно настроить                                        | git-runic для форматирования только измененных строк             |
| Производительность    | Стандартная                                            | Может быть скомпилирован в бинарник (runicc) для скорости        |
| Требования к Julia    | Julia 1.0+                                             | Рекомендуется Julia 1.12+ для флага -m                           |
| Статус                | Стабильный, широко используется                        | Новый (с 2024), активно развивается                              |


### <span class="section-num">3.3</span> Форматирование {#форматирование}

-   JuliaFormatter.jl позволяет настраивать множество аспектов:
    -   Предел длины строки через `margin`
    -   Выравнивание присваиваний (`alignAssignment`)
    -   Автозамену `for i = 1:10` на `for i in 1:10` (`alwaysForIn`)
    -   Преобразование `x |> f` в `f(x)` (`pipeToFunctionCall`)

-   Runic.jl придерживается строгих правил:
    -   4 пробела отступа --- всегда
    -   Блоки всегда начинаются и заканчиваются с новой строки
    -   Нет ограничения длины строки --- разработчик сам решает, где переносить
    -   Умная обработка цепочек операторов с "мягкой" индентацией
    -   Пробелы вокруг всех инфиксных операторов, включая kwargs


### <span class="section-num">3.4</span> Отключение форматирования {#отключение-форматирования}

-   Оба инструмента позволяют временно отключать форматирование с помощью комментариев:

<!--listend-->

```julia
#! format: off          # JuliaFormatter.jl
# runic: off            # Runic.jl

# здесь код не форматируется

#! format: on           # JuliaFormatter.jl
# runic: on             # Runic.jl
```

-   Runic также позволяет отключить форматирование до конца файла одной командой `# runic: off` на верхнем уровне .
