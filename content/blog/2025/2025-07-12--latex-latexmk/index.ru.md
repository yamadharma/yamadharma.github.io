---
title: "LaTeX. Утилита latexmk"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-12T20:52:00+03:00
lastmod: 2025-07-12T21:41:00+03:00
tags: ["latex"]
categories: ["computer-science"]
draft: false
slug: "latex-latexmk"
---

LaTeX. Утилита latexmk.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.cantab.net/users/johncollins/latexmk/index.html>
-   CTAN: <https://www.ctan.org/tex-archive/support/latexmk>


## <span class="section-num">2</span> Основные возможности {#основные-возможности}

-   Автоматическое определение зависимостей
    -   Анализирует файлы `.fls`, `.log` и `.aux` для выявления зависимостей между исходными файлами, что позволяет эффективно управлять повторными запусками компиляторов.

-   Поддержка различных форматов вывода
    -   Генерирует документы в форматах PDF, DVI, PS, включая возможность прямого создания PDF через `pdflatex` или последовательность `latex → dvips → ps2pdf`.

-   Непрерывный предпросмотр
    -   Опция `-pvc` (preview continuously) автоматически обновляет предварительный просмотр при изменении исходных файлов.

-   Управление библиографиями
    -   Автоматически выбирает между `BibTeX` и `biber` в зависимости от настроек документа.

-   Очистка временных файлов
    -   Команды `-c` и `-C` удаляют вспомогательные файлы (`.aux`, `.log`, `.bbl` и др.), сохраняя при этом итоговые документы.
-   Автоматизация повторных запусков
    -   Определяет необходимое количество компиляций для разрешения перекрёстных ссылок, библиографических записей и других зависимостей.
-   Поддержка нестандартных задач
    -   Позволяет добавлять пользовательские зависимости через конфигурационные файлы (например, для генерации глоссариев или конвертации EPS в PDF).
-   Интеграция с инструментами
    -   Работает с `makeglossaries`, `makeindex` и другими программами, автоматизируя сложные рабочие процессы.


## <span class="section-num">3</span> Примеры использования {#примеры-использования}

```shell
# Базовая компиляция в PDF
latexmk -pdf document.tex

# Принудительное завершение при ошибках
latexmk -f document.tex

# Непрерывный предпросмотр с обновлением PDF
latexmk -pvc -pdf document.tex

# Очистка всех временных файлов
latexmk -C
```


## <span class="section-num">4</span> Примеры запуска latexmk {#примеры-запуска-latexmk}

-   Простой запуск:

<!--listend-->

```shell
latexmk
```

-   Это запускает LaTeX для всех `.tex` файлов в текущем каталоге с использованием вывода формат, указанных в файле конфигурации.

-   Получить `.pdf` файл:

<!--listend-->

```shell
latexmk -pdf
```

-   Получить `ps`, а затем `pdf`:

<!--listend-->

```shell
latexmk -pdfps
```

-   Скомпилировать только один конкретный `.tex`-файл в текущем каталоге:

<!--listend-->

```shell
latexmk myfile.tex
```

-   Если вы хотите предварительно просмотреть полученные выходные файлы:

<!--listend-->

```shell
latexmk -pv
```


## <span class="section-num">5</span> Очистка {#очистка}

-   После запуска LaTeX текущий каталог загрязнён временными файлами; нужно удалить их:

<!--listend-->

```shell
latexmk -c
```

-   Это не удаляет последний `.pdf`, `.ps`, `.dvi` файлы. Чтобы их удалить:

<!--listend-->

```shell
latexmk -C
```


## <span class="section-num">6</span> Глобальный файл конфигурации {#глобальный-файл-конфигурации}

-   В Linux можно поместить свои конфигурации в `$HOME/.latexmkrc`, который может содержать что-то вроде этого:

<!--listend-->

```perl
$dvi_previewer = 'start xdvi -watchfile 1.5';
$ps_previewer  = 'start gv --watch';
$pdf_previewer = 'start evince';
```


## <span class="section-num">7</span> Локальный файл конфигурации {#локальный-файл-конфигурации}

-   Можно поместить файл конфигурации в текущий каталог.
-   Настройки влияют только на файлы в текущем каталоге.
-   Файл конфигурации должен называться `latexmkrc` или `.latexmkrc`.

-   Чтобы указать, какой формат файла вы хотите вывести: pdf или ps:

<!--listend-->

```perl
$pdf_mode = 1;        # tex -> pdf
$pdf_mode = 2;        # tex -> ps -> pdf
$postscript_mode = 1; # tex -> ps
```

-   Если работа разделена на несколько файлов, необходимо указать основной файл:

<!--listend-->

```perl
@default_files = ('main.tex');
```

-   Можно обработать несколько файлов:

<!--listend-->

```perl
@default_files = ('file-one.tex', 'file-two.tex');
```

-   Если не указать `@default_files`, будут использованы все `.tex`-файлы в текущем каталоге.

-   Cоздать номенклатуру (пакет `nomencl`) с помощью глоссария:

<!--listend-->

```perl
@cus_dep_list = (@cus_dep_list, "glo gls 0 makenomenclature");
sub makenomenclature {
    system("makeindex $_[0].glo -s nomencl.ist -o $_[0].gls"); }
@generated_exts = (@generated_exts, 'glo');
```

-   Преобразовать рисунки в формате `eps` в формат `pdf`:

<!--listend-->

```perl
@cus_dep_list = (@cus_dep_list, "eps pdf 0 eps2pdf");
sub eps2pdf {
    system("epstopdf $_[0].eps"); }
```

-   Включить опцию оболочки `\write18`:

<!--listend-->

```perl
$latex = 'latex -interaction=nonstopmode -shell-escape';
$pdflatex = 'pdflatex -interaction=nonstopmode -shell-escape';
```

-   Явно указать расширения временных файлов:

<!--listend-->

```perl
$clean_ext = "bbl nav out snm";
```
