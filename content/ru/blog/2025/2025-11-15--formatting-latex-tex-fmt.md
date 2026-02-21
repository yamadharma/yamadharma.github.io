---
title: "Форматирование. LaTeX. tex-fmt"
author: ["Dmitry S. Kulyabov"]
date: 2025-11-15T14:05:00+03:00
lastmod: 2025-11-15T17:50:00+03:00
tags: ["programming", "latex"]
categories: ["computer-science"]
draft: false
slug: "formatting-latex-tex-fmt"
---

Форматирование. LaTeX. tex-fmt.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/WGUNDERWOOD/tex-fmt>
-   CTAN: <https://ctan.org/pkg/latex-formatter>
-   Написан на Rust.
-   Онлайт форматер: <https://wgunderwood.github.io/tex-fmt/>


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   Репозиторий karma ([Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
    ```shell
    emerge dev-tex/tex-fmt
    ```


## <span class="section-num">3</span> Отключение форматирования {#отключение-форматирования}

-   Завершение исходной строки на `% tex-fmt: skip` отключает форматирование для этой строки.
-   Чтобы отключить форматирование для блока, используйте `% tex-fmt: off` и `% tex-fmt: on`.

<!--listend-->

```tex
\documentclass{article}

\begin{document}

    This line is skipped % tex-fmt: skip

% tex-fmt: off
  These lines are also
    not formatted or wrapped
% tex-fmt: on

\end{document}
```

Среды Verbatim, включая `verbatim`, `Verbatim`, `lstlisting` и `minted`


## <span class="section-num">4</span> Файл конфигурации {#файл-конфигурации}

-   Явно указанный файл конфигурации:
    -   если вы укажете путь к файлу конфигурации с помощью `tex-fmt --config <PATH>`, будет использоваться этот файл.
-   Текущий рабочий каталог:
    -   файл с именем `tex-fmt.toml` в каталоге, где выполняется `tex-fmt`.
-   Корневой каталог Git-репозитория:
    -   файл с именем `tex-fmt.toml` в корневом каталоге текущего Git-репозитория.
-   Каталог конфигурации пользователя:
    -   Файл с именем `tex-fmt.toml` в подкаталоге `tex-fmt/` каталога конфигурации пользователя:
        -   Linux: `~/.config/tex-fmt/tex-fmt.toml`
        -   macOS: `/Users/<user>/Library/Application Support/tex-fmt/tex-fmt.toml`
        -   Windows: `C:\Users\<user>\AppData\Roaming\tex-fmt\tex-fmt.toml`
-   Можно игнорировать все файлы конфигурации, используя флаг `--noconfig`.


## <span class="section-num">5</span> Параметры командной строки {#параметры-командной-строки}

-   В командной строке можно передать следующие аргументы.

| Вариант                | Псевдоним | По умолчанию | Описание                                                       |
|------------------------|-----------|--------------|----------------------------------------------------------------|
| `--check`              | `-c`      |              | Проверьте форматирование, не изменяйте файлы.                  |
| `--print`              | `-p`      |              | Выводить на стандартный вывод, не изменять файлы               |
| `--fail-on-change`     | `-f`      |              | Ошибка, если файлы были изменены                               |
| `--recursive`          | `-r`      |              | Рекурсивный поиск файлов для форматирования                    |
| `--nowrap`             | `-n`      |              | Не переносите длинные строки                                   |
| `--wraplen <N>`        | `-l`      | `80`         | Длина строки для переноса                                      |
| `--tabsize <N>`        | `-t`      | `2`          | Количество символов, используемых в качестве размера табуляции |
| `--usetabs`            |           |              | Используйте табуляции вместо пробелов для отступов.            |
| `--stdin`              | `-s`      |              | Обрабатывать stdin как один файл, выводить на stdout           |
| `--config <PATH>`      |           |              | Путь к файлу конфигурации                                      |
| `--noconfig`           |           |              | Не читайте ни один файл конфигурации                           |
| `--verbose`            | `-v`      |              | Показывать информационные сообщения                            |
| `--quiet`              | `-q`      |              | Скрыть предупреждающие сообщения                               |
| `--trace`              |           |              | Показать сообщения трассировки                                 |
| `--completion <SHELL>` |           |              | Сгенерировать скрипт завершения оболочки                       |
| `--man`                |           |              | Создать страницу руководства                                   |
| `--args`               |           |              | Просмотреть аргументы, переданные в tex-fmt                    |
| `--help`               | `-h`      |              | Распечатать справку                                            |
| `--version`            | `-V`      |              | Версия для печати                                              |


## <span class="section-num">6</span> Параметры файла конфигурации {#параметры-файла-конфигурации}

-   Файл конфигурации: `tex-fmt.toml`.
-   Первый пример в каждой строке есть значение по умолчанию.

| Вариант          | Тип      | Примеры                | Описание                                                                |
|------------------|----------|------------------------|-------------------------------------------------------------------------|
| `check`          | bool     | `false`                | Проверьте форматирование, не изменяйте файлы.                           |
| `print`          | bool     | `false`                | Выводить на стандартный вывод, не изменять файлы                        |
| `fail-on-change` | bool     | `false`                | Ошибка, если файлы были изменены                                        |
| `wrap`           | bool     | `true`                 | Переносить длинные строки                                               |
| `wraplen`        | int      | `80`, `100`            | Длина строки для переноса                                               |
| `wrapmin`        | int      | `70`, `90`             | Минимальная целевая длина для переноса строк                            |
| `tabsize`        | int      | `2`, `4`               | Количество символов, используемых в качестве размера табуляции          |
| `tabchar`        | str      | `"space"`, `"tab"`     | Символ, используемый для отступа                                        |
| `stdin`          | bool     | `false`                | Обрабатывать stdin как один файл, выводить на stdout                    |
| `lists`          | arr[str] | `[]`, `["myitemize"]`  | Дополнительный список сред, которые нужно отформатировать как `itemize` |
| `verbatims`      | arr[str] | `[]`, `["myverbatim"]` | Дополнительные дословные среды                                          |
| `no-indent-envs` | arr[str] | `[]`, `["mydocument"]` | Среды без отступов                                                      |
| `wrap-chars`     | arr[str] | `[]`, `["。"]`         | Символы, после которых возможен перенос строк                           |
| `verbosity`      | str.     | `"warn"`, `"error"`    | Уровень детализации для терминального журнала                           |


## <span class="section-num">7</span> Пример файла конфигурации {#пример-файла-конфигурации}

-   Возможный файл конфигурации `tex-fmt.toml`:
    ```toml
    # tex-fmt.toml
    check = false
    print = false
    wrap = true
    wraplen = 80
    tabsize = 2
    tabchar = "space"
    stdin = false
    verbosity = "warn"
    lists = []
    no-indent-envs = []
    ```
