---
title: "Pdf. Просмотр. Zathura"
author: ["Dmitry S. Kulyabov"]
date: 2023-09-20T13:12:00+03:00
lastmod: 2025-03-11T09:30:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "pdf-viewer-zathura"
---

Zathura --- программа просмотра pdf-файлов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://pwmt.org/projects/zathura/>
-   Репозиторий: <https://github.com/pwmt/zathura.git>


### <span class="section-num">1.1</span> Особенности {#особенности}

-   Keyboard Driven, сочетания клавиш очень похожи на Vim.
-   Минималистичный дизайн.
-   Автоматически перезагружать файл при обнаружении изменений.
    -   В отличие, например, от Evince Zathura отслеживает имя файла, а не _inode_.
    -   Поэтому, при переименовании файла Zathura его теряет.


### <span class="section-num">1.2</span> Режимы {#режимы}

-   Просмотр документов (основной режим)
-   Оглавлениу (`tab`)
-   Презентация (`F5`)
-   Полноэкранный режим (`F11`)


### <span class="section-num">1.3</span> Поддерживаемые форматы документов {#поддерживаемые-форматы-документов}

-   Поддерживает различные форматы с помощью плагинов:

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Поддерживаемые форматы документов
</div>

| Формат             | Плагин              | Библиотека для рендеринга |
|--------------------|---------------------|---------------------------|
| PDF                | zathura-pdf-poppler | poppler                   |
| PDF                | zathura-pdf-mupdf   | mupdf                     |
| DjVu               | zathura-djvu        | djvulibre                 |
| PostScript         | zathura-ps          | libspectre                |
| Comic Book Archive | zathura-cb          | libarchive                |
| epub               | zathura-pdf-mupdf   | mupdf                     |

-   Не поддерживается работа с pdf-формами.
-   Не поддерживается работа с аннотированием pdf.


## <span class="section-num">2</span> Комбинации клавиш {#комбинации-клавиш}


### <span class="section-num">2.1</span> Стандартные комбинации {#стандартные-комбинации}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 2:</span>
  Комбинация клавиш Zathura в основном режиме
</div>

| Комбинации клавиш      | Значение комбинаций                                 |
|------------------------|-----------------------------------------------------|
| `J`, `K`               | перейти на следующую, предыдущую страницу           |
| `h`, `k`, `j`, `l`     | прокрутка влево, вверх, вниз, вправо                |
| `←`, `↑`, `↓`, →       | прокрутка влево, вверх, вниз, вправо                |
| `Ctrl+t`, `Ctrl+y`,    | прокрутка влево, вправо на полстраницы              |
| `Ctrl+u`, `Ctrl+d`     | прокрутка вверх, вниз на полстраницы                |
| `Ctrl+f`, `Ctrl+b`     | прокрутка вверх, вниз на страницу                   |
| `gg`, `G`, `nG`, `ngg` | в начало, в конец, на n-ую страницу документа       |
| `a`, `s`               | вместить страницу по высоте, по ширине              |
| `d`                    | просмотр разворота                                  |
| `/`, `?`               | поиск по тексту                                     |
| `Shift+/`              | обратный поиск по тексту                            |
| `n`, `N`               | перейти к следующему, предыдущему результату поиска |
| `o`, `O`               | открыть документ                                    |
| `f`                    | перейти по ссылке                                   |
| `F`                    | показать адрес ссылки                               |
| `r`, `nr`              | поворот по часовой стрелке, поворот `n` раз         |
| `Ctrl+r`               | инвертировать цвета (в ЧБ)                          |
| `R`                    | перезагрузить документ                              |
| `+`, `-`, =            | увеличить, уменьшить, оригинальный размер           |
| `q`                    | выход                                               |

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 3:</span>
  Комбинация клавиш Zathura в режиме оглавления
</div>

| Комбинации клавиш | Значение комбинаций             |
|-------------------|---------------------------------|
| `l`               | Развернуть пункт                |
| `L`               | Развернуть все                  |
| `h`               | Свернуть                        |
| `H`               | Свернуть все                    |
| `k`, `j`          | Перемещение на пункт выше, ниже |
| `Space`, `Enter`  | Выбрать и открыть пункт         |

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 4:</span>
  Переключение режимов
</div>

| Комбинации клавиш | Значение комбинаций                       |
|-------------------|-------------------------------------------|
| `F11`             | Полноэкранный режим                       |
| `:`               | Режим ввода команд                        |
| `F5`              | Режим презентации                         |
| `Tab`             | Переключение в режим оглавления и обратно |
| `Esc`             | Обычный режим                             |

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 5:</span>
  Команды (вводимые после :)
</div>

| Команда           | Описание                                      |
|-------------------|-----------------------------------------------|
| `bmark`           | Сохранить закладку                            |
| `bdelete`         | Удалить закладку                              |
| `blist`           | Список закладок                               |
| `close`           | Закрыть документ                              |
| `exec`            | Выполнить внешнюю команду                     |
| `info`            | Показать информацию о документе               |
| `help`            | Показать справочную страницу                  |
| `open`, `o`       | Открыть документ                              |
| `offset`          | Настройка смещения страницы                   |
| `print`           | Печать документа                              |
| `write`, `write!` | Сохранить документ, принудительная перезапись |
| `export`          | Экспорт приложений (Export attachments)       |


### <span class="section-num">2.2</span> Модификаторы комбинаций {#модификаторы-комбинаций}

-   Везде, где это имеет смысл, перед командой можно ставить число для повторения команды соответствующее число раз, например:
-   `10 J` : перейти на 10 страниц вперёд;
-   `3 r` : повернуть 3 раза по часовой стрелке (что эквивалентно одному разу против часовой).


### <span class="section-num">2.3</span> Emacs-подобная конфигурация {#emacs-подобная-конфигурация}

-   <https://web.archive.org/web/20220815064614/https://gist.github.com/ne9z/8778d614b90b85dfe8f6b698ad758f36>
-   Конфигурационный файл:
    ```conf-unix
    # Being an Emacs user, it is natural for me to use emacs-like and info-like keybindings for zathura.
    #
    # Zathura configuration documentation is available at
    # https://git.pwmt.org/pwmt/zathura/-/blob/e5d2ca487147e79d0bb7acbf5174cd9dcc92a86c/doc/man/zathurarc.5.rst
    # A full list of available functions and default keybindings is available at
    # https://git.pwmt.org/pwmt/zathura/-/blob/e5d2ca487147e79d0bb7acbf5174cd9dcc92a86c/zathura/config.c#L301
    #
    # If you want to integrate Zathura with Emacs AUCTeX mode, see
    # [emacs wiki](https://www.emacswiki.org/emacs/AUCTeX).
    #
    # Put the following inside `$XDG_CONFIG_HOME/zathura/zathurarc

    ## niceties
    # when selecting text with mouse,
    # copy to clipboard
    set selection-clipboard clipboard

    # keep several lines of text when
    # scrolling a screenful
    set scroll-full-overlap 0.2

    # see documentation for details
    set scroll-page-aware true
    set window-title-basename true
    set adjust-open width
    set statusbar-home-tilde true
    set vertical-center true
    set synctex true
    # large bold font easier on the eyes in index mode
    # status bar can be disabled with A-s
    set font "FreeSans bold 16"
    set zoom-step 3

    map [normal] <C-b> scroll left
    map [normal] <C-n> scroll down
    map [normal] <C-p> scroll up
    map [normal] <C-f> scroll right
    map [normal] <C-g> abort
    map [insert] <C-g> abort
    map [normal] <C-[> abort
    map [normal] <A-\<> goto top
    map [normal] <A-\>> goto bottom
    map [normal] a adjust_window best-fit
    map [normal] s adjust_window width
    map [normal] F display_link
    map [normal] <C-c> copy_link
    map [normal] f follow
    map [normal] m mark_add
    map [normal] \' mark_evaluate
    map [normal] \, navigate next
    map [normal] \. navigate previous
    map [normal] <A-Right> navigate next
    map [normal] <A-Left> navigate previous
    map [normal] <PageDown> scroll full-down
    map [normal] <PageUp> scroll full-up
    map [normal] <C-P> print
    map [normal] c recolor
    map [normal] R reload
    map [normal] v rotate rotate_cw
    map [normal] V rotate rotate_ccw
    map [normal] <Left> scroll left
    map [normal] <Up> scroll up
    map [normal] <Down> scroll down
    map [normal] <Right> scroll right
    map [normal] <A-a> scroll half-left
    map [normal] <C-V> scroll half-down
    map [normal] <A-V> scroll half-up
    map [normal] <A-e> scroll half-right
    map [normal] <C-a> scroll full-left
    map [normal] <C-v> scroll full-down
    map [normal] <Return> scroll full-down
    map [normal] <A-v> scroll full-up
    map [normal] <C-e> scroll full-right
    map [normal] <Space> scroll full-down
    map [normal] <C-h> scroll full-up
    map [normal] <BackSpace> scroll full-up
    map [normal] <S-Space> scroll full-up
    map [normal] l jumplist backward
    map [normal] r jumplist forward
    map [normal] <A-r> bisect forward
    map [normal] <A-l> bisect backward
    # still need to use '/' to trigger search
    map [normal] <C-s> search forward
    map [normal] <C-r> search backward
    map [normal] p snap_to_page
    map [normal] <C-i> toggle_index
    map [normal] i toggle_index
    map [normal] <Tab> toggle_index
    map [normal] <A-s> toggle_statusbar
    map [normal] <A-i> focus_inputbar
    map [normal] d toggle_page_mode
    map [normal] q quit
    map [normal] + zoom in
    map [normal] - zoom out
    map [normal] = zoom in
    map [normal] <A-P> toggle_presentation
    map [normal] <A-F> toggle_fullscreen
    map [normal] j toggle_fullscreen
    map [fullscreen] j toggle_fullscreen
    map [fullscreen] q toggle_fullscreen
    map [fullscreen] <C-b> scroll left
    map [fullscreen] <C-n> scroll down
    map [fullscreen] <C-p> scroll up
    map [fullscreen] <C-f> scroll right
    map [fullscreen] <C-g> abort
    map [fullscreen] <C-[> abort
    map [fullscreen] <A-\<> goto top
    map [fullscreen] <A-\>> goto bottom
    map [fullscreen] a adjust_window best-fit
    map [fullscreen] s adjust_window width
    map [fullscreen] F display_link
    map [fullscreen] <C-c> copy_link
    map [fullscreen] f follow
    map [fullscreen] m mark_add
    map [fullscreen] \' mark_evaluate
    map [fullscreen] \, navigate next
    map [fullscreen] \. navigate previous
    map [fullscreen] <A-Right> navigate next
    map [fullscreen] <A-Left> navigate previous
    map [fullscreen] <PageDown> scroll full-down
    map [fullscreen] <PageUp> scroll full-up
    map [fullscreen] <C-P> print
    map [fullscreen] c recolor
    map [fullscreen] R reload
    map [fullscreen] v rotate rotate_cw
    map [fullscreen] V rotate rotate_ccw
    map [fullscreen] <Left> scroll left
    map [fullscreen] <Up> scroll up
    map [fullscreen] <Down> scroll down
    map [fullscreen] <Right> scroll right
    map [fullscreen] <A-a> scroll half-left
    map [fullscreen] <C-V> scroll half-down
    map [fullscreen] <A-V> scroll half-up
    map [fullscreen] <A-e> scroll half-right
    map [fullscreen] <C-a> scroll full-left
    map [fullscreen] <C-v> scroll full-down
    map [fullscreen] <Return> scroll full-down
    map [fullscreen] <A-v> scroll full-up
    map [fullscreen] <C-e> scroll full-right
    map [fullscreen] <Space> scroll full-down
    map [fullscreen] <C-h> scroll full-up
    map [fullscreen] <BackSpace> scroll full-up
    map [fullscreen] <S-Space> scroll full-up
    map [fullscreen] l jumplist backward
    map [fullscreen] r jumplist forward
    map [fullscreen] <A-r> bisect forward
    map [fullscreen] <A-l> bisect backward
    map [fullscreen] <C-s> search forward
    map [fullscreen] <C-r> search backward
    map [fullscreen] p snap_to_page
    map [fullscreen] i toggle_index
    map [fullscreen] <C-i> toggle_index
    map [fullscreen] <Tab> toggle_index
    map [fullscreen] <A-s> toggle_statusbar
    map [fullscreen] <A-i> focus_inputbar
    map [fullscreen] d toggle_page_mode
    map [fullscreen] + zoom in
    map [fullscreen] - zoom out
    map [fullscreen] = zoom in
    # status bar will obscure last item in index mode
    map [index] <A-s> toggle_statusbar
    map [index] q toggle_index
    map [index] i toggle_index
    map [index] <C-p> navigate_index up
    map [index] <C-h> navigate_index up
    map [index] <BackSpace> navigate_index up
    map [index] <C-n> navigate_index down
    map [index] <A-v> navigate_index up
    map [index] <C-v> navigate_index down
    map [index] \< navigate_index top
    map [index] \> navigate_index bottom
    map [index] <A-\<> navigate_index top
    map [index] <A-\>> navigate_index bottom
    map [index] <C-b> navigate_index collapse
    map [index] <C-f> navigate_index expand
    map [index] <C-i> navigate_index expand-all
    map [index] <A-i> navigate_index collapse-all
    map [index] <Up> navigate_index up
    map [index] <Down> navigate_index down
    map [index] <Left> navigate_index collapse
    map [index] <Right> navigate_index expand
    map [index] <C-m> navigate_index select
    map [index] <Space> navigate_index select
    map [index] <Return> navigate_index select
    map [index] <C-j> navigate_index select
    map [index] <Esc> toggle_index
    map [index] <C-[> toggle_index
    map [index] <C-g> toggle_index
    map [index] <C-c> toggle_index
    map [presentation] i toggle_index
    map [presentation] r navigate next
    map [presentation] <Down> navigate next
    map [presentation] <Right> navigate next
    map [presentation] <PageDown> navigate next
    map [presentation] <Space> navigate next
    map [presentation] l navigate previous
    map [presentation] <Left> navigate previous
    map [presentation] <Up> navigate previous
    map [presentation] <PageUp> navigate previous
    map [presentation] <S-Space> navigate previous
    map [presentation] <BackSpace> navigate previous
    map [presentation] <F5> toggle_presentation
    map [presentation] q toggle_presentation
    map [presentation] <C-h> navigate previous
    map [presentation] <M-v> navigate previous
    map [presentation] <C-v> navigate next
    map [presentation] <A-\<> goto top
    map [presentation] <A-\>> goto bottom
    ```


## <span class="section-num">3</span> Настройки {#настройки}


### <span class="section-num">3.1</span> Установка как приложения по умолчанию {#установка-как-приложения-по-умолчанию}

-   Приложение по умолчанию устанавливается с помощью _xdg-utils_ (см. [XDG. Приложения MIME]({{< relref "2023-04-02-xdg-mime-applications" >}})):
    ```shell
    xdg-mime default org.pwmt.zathura.desktop application/pdf
    xdg-mime default org.pwmt.zathura.desktop image/vnd.djvu+multipage
    xdg-mime default org.pwmt.zathura.desktop application/postscript
    xdg-mime default org.pwmt.zathura.desktop image/x-eps
    ```


### <span class="section-num">3.2</span> Конфигурационный файл {#конфигурационный-файл}

-   Конфигурационный файл: `~/.config/zathura/zathurarc`.


## <span class="section-num">4</span> Конфигурация {#конфигурация}

-   Конфигурационный файл: `~/.config/zathura/zathurarc`.
    ```conf-unix
    # -*- mode: conf-unix -*-
    ## Zathura configuration file
    ## See man `man zathurarc'
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      ~/.config/zathura/zathurarc
    </div>


### <span class="section-num">4.1</span> Настройка графического интерфейса {#настройка-графического-интерфейса}

-   Показывает или скрывает элементы графического интерфейса:
    -   `c` : командная строка;
    -   `s` : панель состояния;
    -   `v` : вертикальная полоса прокрутки;
    -   `h` : горизонтальная полоса прокрутки.
        ```conf-unix
        set guioptions shv
        ```


### <span class="section-num">4.2</span> Общие настройки {#общие-настройки}

```conf-unix
## Open document in fit-width mode by default
set adjust-open "best-fit"

## One page per row by default
set pages-per-row 1

## Stop at page boundries
set scroll-page-aware "true"
set smooth-scroll "true"
set scroll-full-overlap 0.01
set scroll-step 100

## Zoom settings
set zoom-min 10
set zoom-step 3

# keep several lines of text when
# scrolling a screenful
set scroll-full-overlap 0.2

# see documentation for details
set scroll-page-aware true
set window-title-basename true
set adjust-open width
set statusbar-home-tilde true
set vertical-center true
set synctex true
# large bold font easier on the eyes in index mode
# status bar can be disabled with A-s
set font "Iosevka 12"

set render-loading "false"
set scroll-step 50
unmap f
map f toggle_fullscreen
map [fullscreen] f toggle_fullscreen
```


### <span class="section-num">4.3</span> Буфер обмена {#буфер-обмена}

-   Устанавливаем режим, при котором выделение мышью копируется в буфер обмена, а не в _x11 primary selection_ (см. [Буфер обмена]({{< relref "2025-03-11--clipboard" >}})).
    ```conf-unix
    ## Enable copy to clipboard when selecting text with mouse
    set selection-clipboard clipboard
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 2:</span>
      ~/.config/zathura/zathurarc
    </div>


### <span class="section-num">4.4</span> Разное {#разное}

-   Инкрементальный поиск:
    ```conf-unix
    ## Enable incremental search
    set incremental-search true
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 3:</span>
      ~/.config/zathura/zathurarc
    </div>

<!--listend-->

```conf-unix
## Disable sandbox
set sandbox none

## Zoom
map <C-i> zoom in
map <C-o> zoom out
```


### <span class="section-num">4.5</span> Комбинации клавиш {#комбинации-клавиш}


#### <span class="section-num">4.5.1</span> Нормальный режим {#нормальный-режим}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 6:</span>
  Комбинация клавиш Zathura в основном режиме
</div>

| Комбинации vi          | Комбинации emacs | Значение комбинаций                                 |
|------------------------|------------------|-----------------------------------------------------|
| `J`, `K`               |                  | перейти на следующую, предыдущую страницу           |
| `h`, `k`, `j`, `l`     |                  | прокрутка влево, вверх, вниз, вправо                |
| `←`, `↑`, `↓`, →       |                  | прокрутка влево, вверх, вниз, вправо                |
| `Ctrl+t`, `Ctrl+y`,    |                  | прокрутка влево, вправо на полстраницы              |
| `Ctrl+u`, `Ctrl+d`     |                  | прокрутка вверх, вниз на полстраницы                |
| `Ctrl+f`, `Ctrl+b`     |                  | прокрутка вверх, вниз на страницу                   |
| `gg`, `G`, `nG`, `ngg` | `A-<`, `A->`     | в начало, в конец, на n-ую страницу документа       |
| `a`, `s`               |                  | вместить страницу по высоте, по ширине              |
| `d`                    |                  | просмотр разворота                                  |
| `/`, `?`               |                  | поиск по тексту                                     |
| `Shift+/`              |                  | обратный поиск по тексту                            |
| `n`, `N`               |                  | перейти к следующему, предыдущему результату поиска |
| `o`, `O`               |                  | открыть документ                                    |
| `f`                    |                  | перейти по ссылке                                   |
| `F`                    |                  | показать адрес ссылки                               |
| `r`, `nr`              |                  | поворот по часовой стрелке, поворот `n` раз         |
| `Ctrl+r`               |                  | инвертировать цвета (в ЧБ)                          |
| `R`                    |                  | перезагрузить документ                              |
| `+`, `-`, =            |                  | увеличить, уменьшить, оригинальный размер           |
| `q`                    | `q`              | выход                                               |
|                        | `C-P`            | печать                                              |

<!--list-separator-->

1.  Стандартные комбинации

<!--list-separator-->

2.  Комбинации emacs

    ```conf-unix
    ## Emacs-like keybindings
    map [normal] <C-b> scroll left
    map [normal] <C-n> scroll down
    map [normal] <C-p> scroll up
    map [normal] <C-f> scroll right
    map [normal] <C-g> abort
    map [insert] <C-g> abort
    map [normal] <C-[> abort
    map [normal] <A-\<> goto top
    map [normal] <A-\>> goto bottom
    map [normal] a adjust_window best-fit
    map [normal] s adjust_window width
    map [normal] F display_link
    map [normal] <C-c> copy_link
    map [normal] f follow
    map [normal] m mark_add
    map [normal] \' mark_evaluate
    map [normal] \, navigate next
    map [normal] \. navigate previous
    map [normal] <A-Right> navigate next
    map [normal] <A-Left> navigate previous
    map [normal] <PageDown> scroll full-down
    map [normal] <PageUp> scroll full-up
    map [normal] <C-P> print
    map [normal] c recolor
    map [normal] R reload
    map [normal] v rotate rotate_cw
    map [normal] V rotate rotate_ccw
    map [normal] <Left> scroll left
    map [normal] <Up> scroll up
    map [normal] <Down> scroll down
    map [normal] <Right> scroll right
    map [normal] <A-a> scroll half-left
    map [normal] <C-V> scroll half-down
    map [normal] <A-V> scroll half-up
    map [normal] <A-e> scroll half-right
    map [normal] <C-a> scroll full-left
    map [normal] <C-v> scroll full-down
    map [normal] <Return> scroll full-down
    map [normal] <A-v> scroll full-up
    map [normal] <C-e> scroll full-right
    map [normal] <Space> scroll full-down
    map [normal] <C-h> scroll full-up
    map [normal] <BackSpace> scroll full-up
    map [normal] <S-Space> scroll full-up
    map [normal] l jumplist backward
    map [normal] r jumplist forward
    map [normal] <A-r> bisect forward
    map [normal] <A-l> bisect backward
    # still need to use '/' to trigger search
    map [normal] <C-s> search forward
    map [normal] <C-r> search backward
    map [normal] p snap_to_page
    map [normal] <C-i> toggle_index
    map [normal] i toggle_index
    map [normal] <Tab> toggle_index
    map [normal] <A-s> toggle_statusbar
    map [normal] <A-i> focus_inputbar
    map [normal] d toggle_page_mode
    map [normal] q quit
    map [normal] + zoom in
    map [normal] - zoom out
    map [normal] = zoom in
    map [normal] <A-P> toggle_presentation
    map [normal] <A-F> toggle_fullscreen
    map [normal] j toggle_fullscreen
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 4:</span>
      ~/.config/zathura/zathurarc
    </div>


#### <span class="section-num">4.5.2</span> Полноэкранный режим {#полноэкранный-режим}

```conf-unix
map [fullscreen] j toggle_fullscreen
map [fullscreen] q toggle_fullscreen
map [fullscreen] <C-b> scroll left
map [fullscreen] <C-n> scroll down
map [fullscreen] <C-p> scroll up
map [fullscreen] <C-f> scroll right
map [fullscreen] <C-g> abort
map [fullscreen] <C-[> abort
map [fullscreen] <A-\<> goto top
map [fullscreen] <A-\>> goto bottom
map [fullscreen] a adjust_window best-fit
map [fullscreen] s adjust_window width
map [fullscreen] F display_link
map [fullscreen] <C-c> copy_link
map [fullscreen] f follow
map [fullscreen] m mark_add
map [fullscreen] \' mark_evaluate
map [fullscreen] \, navigate next
map [fullscreen] \. navigate previous
map [fullscreen] <A-Right> navigate next
map [fullscreen] <A-Left> navigate previous
map [fullscreen] <PageDown> scroll full-down
map [fullscreen] <PageUp> scroll full-up
map [fullscreen] <C-P> print
map [fullscreen] c recolor
map [fullscreen] R reload
map [fullscreen] v rotate rotate_cw
map [fullscreen] V rotate rotate_ccw
map [fullscreen] <Left> scroll left
map [fullscreen] <Up> scroll up
map [fullscreen] <Down> scroll down
map [fullscreen] <Right> scroll right
map [fullscreen] <A-a> scroll half-left
map [fullscreen] <C-V> scroll half-down
map [fullscreen] <A-V> scroll half-up
map [fullscreen] <A-e> scroll half-right
map [fullscreen] <C-a> scroll full-left
map [fullscreen] <C-v> scroll full-down
map [fullscreen] <Return> scroll full-down
map [fullscreen] <A-v> scroll full-up
map [fullscreen] <C-e> scroll full-right
map [fullscreen] <Space> scroll full-down
map [fullscreen] <C-h> scroll full-up
map [fullscreen] <BackSpace> scroll full-up
map [fullscreen] <S-Space> scroll full-up
map [fullscreen] l jumplist backward
map [fullscreen] r jumplist forward
map [fullscreen] <A-r> bisect forward
map [fullscreen] <A-l> bisect backward
map [fullscreen] <C-s> search forward
map [fullscreen] <C-r> search backward
map [fullscreen] p snap_to_page
map [fullscreen] i toggle_index
map [fullscreen] <C-i> toggle_index
map [fullscreen] <Tab> toggle_index
map [fullscreen] <A-s> toggle_statusbar
map [fullscreen] <A-i> focus_inputbar
map [fullscreen] d toggle_page_mode
map [fullscreen] + zoom in
map [fullscreen] - zoom out
map [fullscreen] = zoom in
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 5:</span>
  ~/.config/zathura/zathurarc
</div>


#### <span class="section-num">4.5.3</span> Режим работы с оглавлением {#режим-работы-с-оглавлением}

```conf-unix
# status bar will obscure last item in index mode
map [index] <A-s> toggle_statusbar
map [index] q toggle_index
map [index] i toggle_index
map [index] <C-p> navigate_index up
map [index] <C-h> navigate_index up
map [index] <BackSpace> navigate_index up
map [index] <C-n> navigate_index down
map [index] <A-v> navigate_index up
map [index] <C-v> navigate_index down
map [index] \< navigate_index top
map [index] \> navigate_index bottom
map [index] <A-\<> navigate_index top
map [index] <A-\>> navigate_index bottom
map [index] <C-b> navigate_index collapse
map [index] <C-f> navigate_index expand
map [index] <C-i> navigate_index expand-all
map [index] <A-i> navigate_index collapse-all
map [index] <Up> navigate_index up
map [index] <Down> navigate_index down
map [index] <Left> navigate_index collapse
map [index] <Right> navigate_index expand
map [index] <C-m> navigate_index select
map [index] <Space> navigate_index select
map [index] <Return> navigate_index select
map [index] <C-j> navigate_index select
map [index] <Esc> toggle_index
map [index] <C-[> toggle_index
map [index] <C-g> toggle_index
map [index] <C-c> toggle_index
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 6:</span>
  ~/.config/zathura/zathurarc
</div>


#### <span class="section-num">4.5.4</span> Режим презентации {#режим-презентации}

```conf-unix
map [presentation] i toggle_index
map [presentation] r navigate next
map [presentation] <Down> navigate next
map [presentation] <Right> navigate next
map [presentation] <PageDown> navigate next
map [presentation] <Space> navigate next
map [presentation] l navigate previous
map [presentation] <Left> navigate previous
map [presentation] <Up> navigate previous
map [presentation] <PageUp> navigate previous
map [presentation] <S-Space> navigate previous
map [presentation] <BackSpace> navigate previous
map [presentation] <F5> toggle_presentation
map [presentation] q toggle_presentation
map [presentation] <C-h> navigate previous
map [presentation] <M-v> navigate previous
map [presentation] <C-v> navigate next
map [presentation] <A-\<> goto top
map [presentation] <A-\>> goto bottom
```
<div class="src-block-caption">
  <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 7:</span>
  ~/.config/zathura/zathurarc
</div>
