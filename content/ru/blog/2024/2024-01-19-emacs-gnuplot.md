---
title: "Emacs. Пакеты. Gnuplot"
author: ["Dmitry S. Kulyabov"]
date: 2024-01-19T12:15:00+03:00
lastmod: 2024-01-19T17:38:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-gnuplot"
---

Поддержка gnuplot в Emacs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/emacs-gnuplot/gnuplot>
-   Позволяет запускать файлы gnuplot из редактора Emacs.
-   Основные свойства:
    -   Подсветка синтаксиса и отступы для сценариев gnuplot.
    -   Интерактивные сеансы gnuplot.
    -   Встроенное отображение графиков gnuplot.


## <span class="section-num">2</span> Настройка пакета {#настройка-пакета}

-   Подключите пакет:
    ```emacs-lisp
    (autoload 'gnuplot-mode "gnuplot" "Gnuplot major mode" t)
    (autoload 'gnuplot-make-buffer "gnuplot" "open a buffer in gnuplot-mode" t)
    (setq auto-mode-alist (append '(("\\.gp$" . gnuplot-mode)) auto-mode-alist))
    ```


## <span class="section-num">3</span> Использование {#использование}


### <span class="section-num">3.1</span> Ручной запуск {#ручной-запуск}

-   Ручной запуск режима gnuplot:
    -   `M-x gnuplot-mode`: запустить режим `gnuplot` в текущем буфере;
    -   `M-x gnuplot-make-buffer`: открыть новый буфер и запустить режим `gnuplot` в этом буфере.


### <span class="section-num">3.2</span> Клавиатурные сочетания {#клавиатурные-сочетания}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Клавиатурные сочетания режима gnuplot-mode
</div>

| Сочетание       | Описание                                                         |
|-----------------|------------------------------------------------------------------|
| C-c C-l         | отправить текущую строку в gnuplot                               |
| C-c C-v         | отправить текущую строку в gnuplot и перейти на следующую строку |
| C-c C-r         | отправить текущий регион в gnuplot                               |
| C-c C-b         | отправить весь буфер в gnuplot                                   |
| C-c C-f         | отправить файл в gnuplot                                         |
| C-c C-i         | вставить имя файла под курсором                                  |
| C-c C-n         | отменить параметр установки в текущей строке                     |
| C-c C-c         | закомментировать регион                                          |
| C-c C-o         | установить аргументы для команды под курсором                    |
| S-mouse-2       | установить аргументы для команды под курсором мыши               |
| C-c C-d         | просмотреть info-документацию                                    |
| C-c C-e         | `show-gnuplot-buffer`                                            |
| C-c C-k         | завершить процесс gnuplot                                        |
| C-c C-z         | настроить режим gnuplot                                          |
| M-tab или M-ret | дописать команду                                                 |
| ret             | новая строка и отступ                                            |
| tab             | отступ текущей строки                                            |

-   За исключением команд отправки строки в gnuplot, эти команды работают и в буфере командного интерпретатора gnuplot.

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 2:</span>
  Клавиатурные сочетания буфера командного интерпретатора gnuplot
</div>

| Сочетание | Описание                                           |
|-----------|----------------------------------------------------|
| M-C-p     | построчно отображать самый последний буфер скрипта |
| M-C-f     | сохраните текущий буфер скрипта и загрузите файл   |
| C-c C-e   | вернуться к последнему буферу скрипта              |
