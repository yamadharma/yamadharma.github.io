---
title: "Emacs. Пакет treemacs"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-20T09:09:00+03:00
lastmod: 2025-07-14T19:37:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-treemacs"
---

Emacs. Пакет treemacs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиториий: <https://github.com/Alexander-Miller/treemacs>
-   Предоставляет интерфейс для работы с файловой системой и проектами.
-   Позволяет организовать файлы и папки в виде дерева, что упрощает навигацию и управление проектами.


## <span class="section-num">2</span> Комбинации клавиатурные {#комбинации-клавиатурные}


### <span class="section-num">2.1</span> Настраиваемые {#настраиваемые}


### <span class="section-num">2.2</span> Project (префикс `C-c C-p`) {#project--префикс-c-c-c-p}

| Сочетание               | Функция                                | Описание                                               |
|-------------------------|----------------------------------------|--------------------------------------------------------|
| `C-c C-p a`             | treemacs-add-project-to-workspace      | Select a new project to add to the treemacs workspace. |
| `C-c C-p p`             | treemacs-projectile                    | Select a projectile project to add to the workspace.   |
| `C-c C-p d`             | treemacs-remove-project-from-workspace | Remove project at point from the workspace.            |
| `C-c C-p r`             | treemacs-rename-project                | Rename project at point.                               |
| `C-c C-p c c`           | treemacs-collapse-project              | Collapse project at point.                             |
| `C-c C-p c o` / `S-TAB` | treemacs-collapse-all-projects         | Collapse all projects.                                 |
| `C-c C-p c o`           | treemacs-collapse-all-projects         | Collapse all projects except the project at point.     |


### <span class="section-num">2.3</span> Workspaces Keybinds (префикс `C-c C-w`) {#workspaces-keybinds--префикс-c-c-c-w}

| Сочетание   | Функция                         | Описание                               |
|-------------|---------------------------------|----------------------------------------|
| `C-c C-w r` | treemacs-rename-workspace       | Rename a workspace.                    |
| `C-c C-w a` | treemacs-create-workspace       | Create a new workspace.                |
| `C-c C-w d` | treemacs-remove-workspace       | Delete a workspace.                    |
| `C-c C-w s` | treemacs-switch-workspace       | Switch the current workspace.          |
| `C-c C-w e` | treemacs-edit-workspaces        | Edit workspace layout via org-mode.    |
| `C-c C-w n` | treemacs-next-workspace         | Switch to the next workspace.          |
| `C-c C-w f` | treemacs-set-fallback-workspace | Select the default fallback workspace. |


### <span class="section-num">2.4</span> Node Visit Keybinds (префикс `o`) {#node-visit-keybinds--префикс-o}

| Сочетание    | Функция                                          | Описание                                                                                                       |
|--------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `ov`         | treemacs-visit-node-vertical-split               | Open current file or tag by vertically splitting `next-window` .                                               |
| `oh`         | treemacs-visit-node-horizontal-split             | Open current file or tag by horizontally splitting `next-window` .                                             |
| `oo` / `RET` | treemacs-visit-node-no-split                     | Open current file or tag, performing no split and using `next-window`  directly.                               |
| `oc`         | treemacs-visit-node-close-treemacs               | Open current file or tag, performing no split and using `next-window`  directly, and close treemacs.           |
| `oaa`        | treemacs-visit-node-ace                          | Open current file or tag, using ace-window to decide which window to open the file in.                         |
| `oah`        | treemacs-visit-node-ace-horizontal-split         | Open current file or tag by horizontally splitting a window selected by ace-window.                            |
| `oav`        | treemacs-visit-node-ace-vertical-split           | Open current file or tag by vertically splitting a window selected by ace-window.                              |
| `or`         | treemacs-visit-node-in-most-recently-used-window | Open current file or tag in the most recently used window.                                                     |
| `ox`         | treemacs-visit-node-in-external-application      | Open current file according to its mime type in an external application. Linux, Windows and Mac are supported. |


### <span class="section-num">2.5</span> Toggle Keybinds (префикс `t`) {#toggle-keybinds--префикс-t}

| Сочетание | Функция                             | Описание                                                                               |
|-----------|-------------------------------------|----------------------------------------------------------------------------------------|
| `th`      | treemacs-toggle-show-dotfiles       | Toggle the hiding and displaying of dotfiles.                                          |
| `ti`      | treemacs-hide-gitignored-files-mode | Toggle the hiding and displaying of gitignored files.                                  |
| `tw`      | treemacs-toggle-fixed-width         | Toggle whether the treemacs window should have a fixed width. See also treemacs-width. |
| `tf`      | treemacs-follow-mode                | Toggle `treemacs-follow-mode` .                                                        |
| `ta`      | treemacs-filewatch-mode             | Toggle `treemacs-filewatch-mode` .                                                     |
| `tv`      | treemacs-fringe-indicator-mode      | Toggle `treemacs-fringe-indicator-mode` .                                              |
| `td`      | treemacs-git-commit-diff-mode       | Toggle `treemacs-git-commit-diff-mode` .                                               |


### <span class="section-num">2.6</span> Copy Keybinds (префикс `y`) {#copy-keybinds--префикс-y}

| Сочетание | Функция                              | Описание                                                          |
|-----------|--------------------------------------|-------------------------------------------------------------------|
| `ya`      | treemacs-copy-absolute-path-at-point | Copy the absolute path of the node at point.                      |
| `yr`      | treemacs-copy-relative-path-at-point | Copy the path of the node at point relative to the project root.  |
| `yp`      | treemacs-copy-project-path-at-point  | Copy the absolute path of the project root for the node at point. |
| `yn`      | treemacs-copy-filename-at-point      | Copy the filename for the node at point.                          |
| `yf`      | treemacs-copy-file                   | Copy the file at point.                                           |


### <span class="section-num">2.7</span> Общие сочетания {#общие-сочетания}

| Сочетание     | Функция                                     | Описание                                                                                               |
|---------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ?             | treemacs-common-helpful-hydra               | Summon a helpful hydra to show you treemacs’ most commonly used keybinds.                              |
| C-?           | treemacs-advanced-helpful-hydra             | Summon a helpful hydra to show you treemacs’ rarely used, advanced keybinds.                           |
| `n`           | treemacs-next-line                          | Go to the next line.                                                                                   |
| `p`           | treemacs-previous-line                      | Go to the previous line.                                                                               |
| M-J/N         | treemacs-next-line-other-window             | Go to the next line in `next-window` .                                                                 |
| M-K/P         | treemacs-previous-line-other-window         | Go to the previous line in `next-window` ..                                                            |
| &lt;PgUp&gt;  | treemacs-next-page-other-window             | Go to the next page in `next-window` .                                                                 |
| &lt;PgDn&gt;  | treemacs-previous-page-other-window         | Go to the previous page in `next-window` ..                                                            |
| M-j/M-n       | treemacs-next-neighbour                     | Go to the next same-level neighbour of the current node.                                               |
| `M-k` / `M-p` | treemacs-previous-neighbour                 | Go to the previous same-level neighbour of the current node.                                           |
| `u`           | treemacs-goto-parent-node                   | Go to parent of node at point, if possible.                                                            |
| `<M-Up>`      | treemacs-move-project-up                    | Switch positions of project at point and the one above it.                                             |
| `<M-Down>`    | treemacs-move-project-down                  | Switch positions of project at point and the one below it.                                             |
| `w`           | treemacs-set-width                          | Set a new value for the width of the treemacs window.                                                  |
| `<`           | treemacs-decrement-width                    | Decrease the width of the treemacs window.                                                             |
| `>`           | treemacs-increment-width                    | Increase the width of the treemacs window.                                                             |
| `RET`         | treemacs-RET-action                         | Run the action defined in `treemacs-RET-actions-config`  for the current node.                         |
| `TAB`         | treemacs-TAB-action                         | Run the action defined in `treemacs-TAB-actions-config`  for the current node.                         |
| g/r/gr        | treemacs-refresh                            | Refresh the project at point.                                                                          |
| `d`           | treemacs-delete-file                        | Delete node at point.                                                                                  |
| `R`           | treemacs-rename-file                        | Rename node at point.                                                                                  |
| cf            | treemacs-create-file                        | Создать файл.                                                                                          |
| cd            | treemacs-create-dir                         | Создать каталог.                                                                                       |
| q             | treemacs-quit                               | Hide the treemacs window.                                                                              |
| Q             | treemacs-kill-buffer                        | Delete the treemacs buffer.                                                                            |
| P             | treemacs-peek-mode                          | Peek at the files at point without fully opening them.                                                 |
| ya            | treemacs-copy-absolute-path-at-point        | Copy the absolute path of the node at point.                                                           |
| yr            | treemacs-copy-relative-path-at-point        | Copy the path of the node at point relative to the project root.                                       |
| yp            | treemacs-copy-project-path-at-point         | Copy the absolute path of the project root for the node at point.                                      |
| yf            | treemacs-copy-file                          | Copy the file at point.                                                                                |
| `m`           | treemacs-move-file                          | Move the file at point.                                                                                |
| `s`           | treemacs-resort                             | Set a new value for `treemacs-sorting` .                                                               |
| `b`           | treemacs-add-bookmark                       | Bookmark the currently selected files’s, dir’s or tag’s location.                                      |
| h/M-h         | treemacs-COLLAPSE-action                    | Run the action defined in `treemacs-COLLAPSE-actions-config`  for the current node.                    |
| l/M-l         | treemacs-RET-action                         | Run the action defined in `treemacs-RET-actions-config`  for the current node.                         |
| M-H           | treemacs-root-up                            | Move treemacs’ root one level upward. Only works with a single project in the workspace.               |
| M-L           | treemacs-root-down                          | Move treemacs’ root into the directory at point. Only works with a single project in the workspace.    |
| `H`           | treemacs-collapse-parent-node               | Collapse the parent of the node at point.                                                              |
| `!`           | treemacs-run-shell-command-for-current-node | Run an asynchronous shell command on the current node, replacing “$path” with its path.                |
| `M-!`         | treemacs-run-shell-command-in-project-root  | Run an asynchronous shell command in the root of the current project, replacing “$path” with its path. |
| C             | treemacs-cleanup-litter                     | Close all directories matching any of `treemacs-litter-directories` .                                  |
| `=`           | treemacs-fit-window-width                   | Adjust the width of the treemacs window to that of the longsest line.                                  |
| `W`           | treemacs-extra-wide-toggle                  | Toggle between normal and extra wide display for the treemacs window.                                  |
