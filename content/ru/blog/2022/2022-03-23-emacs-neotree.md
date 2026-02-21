---
title: "Emacs. Neotree"
author: ["Dmitry S. Kulyabov"]
date: 2022-03-23T18:52:00+03:00
lastmod: 2023-10-06T17:19:00+03:00
tags: ["emacs", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "emacs-neotree"
---

Плагин к Emacs для отображения дерева каталогов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   _Neotree_ основан на идее NerdTree для Vim.
-   Отображает дерево каталогов в боковой панели.
-   Репозиторий: <https://github.com/jaypei/emacs-neotree>
-   Wiki: <https://www.emacswiki.org/emacs/NeoTree>


## <span class="section-num">2</span> Конфигурация {#конфигурация}


### <span class="section-num">2.1</span> Темы _NeoTree_ {#темы-neotree}

-   Можно изменить тему NeoTree, используя переменную `neo-theme`.
-   Значение по умолчанию `classic`.
-   Используйте `nerd`, если хотите, чтобы он больше всего походил на NERDTree в VIM.
-   Для настройки следует установить переменную `neo-theme`:
    ```emacs-lisp
    (setq neo-theme 'icons)
    ```

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Параметры темы NeoTree
</div>

| Параметр | Описание                                                  |
|----------|-----------------------------------------------------------|
| classic  | Использование иконок для отображения элементов            |
| ascii    | Использование символов `x`, `-` для отображения каталогов |
| arrow    | Использование стрелок Юникод                              |
| icons    | Использование пакета `all-the-icons`                      |
| nerd     | Использование режима отступов и стрелкок как в NERDTree   |


### <span class="section-num">2.2</span> Сочетания клавиш {#сочетания-клавиш}

-   Сочетания работают только в буфере _NeoTree_

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 2:</span>
  Сочетания клавиш NeoTree
</div>

| Клавиши                   | Значение                                                                                      |
|---------------------------|-----------------------------------------------------------------------------------------------|
| `n`                       | следующая строка                                                                              |
| `p`                       | предыдущая строка                                                                             |
| `SPC` или `RET` или `TAB` | Открыть текущий элемент, если это файл. Свернуть/развернуть текущий элемент, если это каталог |
| `U`                       | Перейти вверх по каталогу                                                                     |
| `g`                       | Обновить                                                                                      |
| `A`                       | Развернуть/свернуть окно NeoTree                                                              |
| `H`                       | Переключить отображение скрытых файлов                                                        |
| `O`                       | Рекурсивно открыть каталог                                                                    |
| `C-c` `C-n`               | Создайте файл или создайте каталог, если имя файла заканчивается на `/`                       |
| `C-c` `C-d`               | Удалить файл или каталог                                                                      |
| `C-c` `C-r`               | Переименуйте файл или каталог                                                                 |
| `C-c` `C-c`               | Измените корневой каталог                                                                     |
| `C-c` `C-p`               | Скопируйте файл или каталог                                                                   |


### <span class="section-num">2.3</span> Отслеживание каталога {#отслеживание-каталога}

-   Каждый раз при открытии окна _neotree_ фокус переходит на текущий файл:
    ```emacs-lisp
    (setq neo-smart-open t)
    ```


### <span class="section-num">2.4</span> Взаимодействие с _projectile_ {#взаимодействие-с-projectile}

-   Переключение на корень проекта при открытии:
    ```emacs-lisp
    (defun neotree-project-dir ()
      "Open NeoTree using the git root."
      (interactive)
      (let ((project-dir (projectile-project-root))
            (file-name (buffer-file-name)))
        (neotree-toggle)
        (if project-dir
            (if (neo-global--window-exists-p)
                (progn
                  (neotree-dir project-dir)
                  (neotree-find file-name)))
          (message "Could not find git project root."))))
    (global-set-key [f8] 'neotree-project-dir)
    ```
