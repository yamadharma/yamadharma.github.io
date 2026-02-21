---
title: "Emacs. Просмотр каталогов"
author: ["Dmitry S. Kulyabov"]
date: 2021-10-03T20:25:00+03:00
lastmod: 2025-01-20T09:08:00+03:00
tags: ["seedling", "emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-directory-browsing"
---

Просмотр каталогов и проектов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Распространённой особенностью многих IDE и текстовых редакторов является просмотрщик файловой системы или проекта, который обычно отображается слева от редактора.
-   Emacs предоставляет различные варианты реализации этой возможности.


## <span class="section-num">2</span> Резюме {#резюме}

-   Я использую:
    -   _dired_:  для просмотра файловой системы;
    -   _treemacs_: для разработки программного обеспечения.


## <span class="section-num">3</span> Пакеты, реализующие просмотр и навигацию по файловой системе {#пакеты-реализующие-просмотр-и-навигацию-по-файловой-системе}


### <span class="section-num">3.1</span> Dired {#dired}

-   _Dired_ поставляется с Emacs и позволяет перемещаться по файловой системе в буфере.
-   По умолчанию Dired показывает подробную информацию о каждом файле в выбранном каталоге.
-   По умолчанию Dired открывает каждый каталог в собственном буфере.
-   Запускается с помощью `C-x d` или `M-x dired`.


#### <span class="section-num">3.1.1</span> Dired Sidebar {#dired-sidebar}

-   Dired Sidebar --- минорный режим, в котором используется режим _dired_ для имитации просмотрщика в виде дерева.
-   В каталогах не отображается треугольная иконка, что визуально затрудняет навигацию.
-   Репозиторий: <https://github.com/jojojames/dired-sidebar>


### <span class="section-num">3.2</span> Speed Bar {#speed-bar}

-   _Speed Bar_ поставляется с Emacs.
-   Запускается с помощью `M-x speedbar`.
-   Открывается в новом фрейме.
-   Предлагает различные возможности навигации с учётом контекста.
-   Показывает файлы, буферы, заголовки организационного режима, информационные файлы, электронные письма в соответствии с содержимым, отображаемым в другом фрейме.


#### <span class="section-num">3.2.1</span> SrSpeedbar {#srspeedbar}

-   _SrSpeedbar_ --- это режим, в котором _Speedbar_ отображается в текущем фрейме.


### <span class="section-num">3.3</span> Neotree {#neotree}

-   [Emacs. Neotree]({{< relref "2022-03-23-emacs-neotree" >}})
-   _Neotree_ основан на идее NerdTree для Vim.
-   Репозиторий: <https://github.com/jaypei/emacs-neotree>


### <span class="section-num">3.4</span> Treemacs {#treemacs}

-   _Treemacs_ не для работы с файловой системой, а для работы с проектами.
-   Репозиторий: <https://github.com/Alexander-Miller/treemacs>
