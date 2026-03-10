---
title: "Броузер Nyxt"
author: ["Dmitry S. Kulyabov"]
date: 2023-10-05T20:43:00+03:00
lastmod: 2023-12-21T16:27:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "nyxt-browser"
---

Броузер Nyxt.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://nyxt.atlas.engineer/>
-   Репозиторий: <https://github.com/atlas-engineer/nyxt>


## <span class="section-num">2</span> Раскладка клавиатуры {#раскладка-клавиатуры}


### <span class="section-num">2.1</span> Emacs {#emacs}

<a id="table--override-map"></a>

| Command                     | Documentation              |
|-----------------------------|----------------------------|
| execute-command ( C-space ) | Execute a command by name. |

<a id="table--help-mode-default-map"></a>

| Command                     | Documentation                                                        |
|-----------------------------|----------------------------------------------------------------------|
| describe-bindings ( ? )     | Show a list of all available keybindings in the current buffer.      |
| jump-to-heading ( m )       | Jump to a particular heading, of type h1, h2, h3, h4, h5, or h6.     |
| next-heading ( n )          | Scroll to the next heading of the BUFFER.                            |
| previous-heading ( p )      | Scroll to the previous heading of the BUFFER.                        |
| delete-current-buffer ( q ) | Delete the current buffer, and make the next buffer the current one. |
| search-buffer ( s )         | Search incrementally on the current buffer.                          |
| headings-panel ( t )        | Display a list of heading for jumping.                               |

<a id="table--bookmarks-mode-emacs-map"></a>

| Command                           | Documentation                                                    |
|-----------------------------------|------------------------------------------------------------------|
| list-bookmarks ( unbound )        | List all bookmarks in a new buffer.                              |
| bookmark-hint ( C-m g )           | Prompt for element hints and bookmark them.                      |
| bookmark-current-url ( C-x r M )  | Bookmark the URL of the current BUFFER.                          |
| set-url-from-bookmark ( C-x r j ) | Set the URL for the current buffer from a bookmark.              |
| delete-bookmark ( C-x r k )       | Delete bookmark(s) matching the chosen URLS-OR-BOOKMARK-ENTRIES. |
| bookmark-url ( C-x r l )          | Prompt for a URL to bookmark.                                    |
| bookmark-buffer-url ( C-x r m )   | Bookmark the page(s) currently opened in the existing buffers.   |

<a id="table--history-mode-emacs-map"></a>

| Command                              | Documentation                                                          |
|--------------------------------------|------------------------------------------------------------------------|
| history-backwards ( C-b )            | Go to parent URL of BUFFER in history.                                 |
| history-forwards-maybe-query ( C-f ) | If current node has multiple children, query which one to navigate to. |
| history-backwards ( C-b )            | Go to parent URL of BUFFER in history.                                 |
| history-forwards ( M-] )             | Go forward one step/URL in BUFFER's history.                           |
| history-backwards-query ( M-b )      | Query parent URL to navigate back to.                                  |
| history-forwards-query ( M-f )       | Query forward-URL to navigate to.                                      |
| history-all-query ( C-M-b )          | Query URL to go to, from the whole history.                            |
| history-forwards-all-query ( C-M-f ) | Query URL to forward to, from all child branches.                      |
| history-all-query ( C-M-b )          | Query URL to go to, from the whole history.                            |
| history-all-query ( C-M-b )          | Query URL to go to, from the whole history.                            |
| history-backwards ( C-b )            | Go to parent URL of BUFFER in history.                                 |
| history-forwards ( M-] )             | Go forward one step/URL in BUFFER's history.                           |
| history-backwards ( C-b )            | Go to parent URL of BUFFER in history.                                 |
| history-forwards ( M-] )             | Go forward one step/URL in BUFFER's history.                           |
| history-all-query ( C-M-b )          | Query URL to go to, from the whole history.                            |
| history-backwards-query ( M-b )      | Query parent URL to navigate back to.                                  |
| history-forwards-all-query ( C-M-f ) | Query URL to forward to, from all child branches.                      |
| history-backwards ( C-b )            | Go to parent URL of BUFFER in history.                                 |
| history-forwards ( M-] )             | Go forward one step/URL in BUFFER's history.                           |
| history-forwards-query ( M-f )       | Query forward-URL to navigate to.                                      |

<a id="table--hint-mode-emacs-map"></a>

| Command                                         | Documentation                                                                 |
|-------------------------------------------------|-------------------------------------------------------------------------------|
| follow-hint-new-buffer-focus ( M-g g )          | Like \`follow-hint-new-buffer', but with focus.                               |
| follow-hint-nosave-buffer ( C-M-g g )           | Like \`follow-hint', but open the selected hints in new \`nosave-buffer's (no |
| copy-hint-url ( C-x C-w )                       | Prompt for element hints and save its corresponding URLs to clipboard.        |
| follow-hint ( M-g M-g )                         | Prompt for element hints and open them in the current buffer.                 |
| follow-hint-new-buffer ( C-u M-g M-g )          | Like \`follow-hint', but open the selected hints in new buffers (no focus).   |
| follow-hint-nosave-buffer-focus ( C-M-g C-M-g ) | Like \`follow-hint-nosave-buffer', but with focus.                            |
| follow-hint-new-buffer ( C-u M-g M-g )          | Like \`follow-hint', but open the selected hints in new buffers (no focus).   |

<a id="table--document-mode-emacs-map"></a>

| Command                                   | Documentation                                                                    |
|-------------------------------------------|----------------------------------------------------------------------------------|
| jump-to-heading ( m )                     | Jump to a particular heading, of type h1, h2, h3, h4, h5, or h6.                 |
| undo ( C-/ )                              | Undo the last editing action.                                                    |
| redo ( C-? )                              | Redo the last editing action.                                                    |
| reload-with-modes ( C-R )                 | Reload the BUFFER with the queried modes.                                        |
| nothing ( C-g )                           | A command that does nothing.                                                     |
| scroll-down ( C-n )                       | Scroll down the current page.                                                    |
| scroll-up ( C-p )                         | Scroll up the current page.                                                      |
| scroll-page-down ( C-v )                  | Scroll down by one page height.                                                  |
| cut ( C-w )                               | Cut the selected text in BUFFER.                                                 |
| paste ( C-y )                             | Paste from clipboard into active element.                                        |
| headings-panel ( t )                      | Display a list of heading for jumping.                                           |
| scroll-to-top ( M-&lt; )                  | Scroll to the top of the current page.                                           |
| scroll-to-bottom ( M-&gt; )               | Scroll to the bottom of the current page.                                        |
| focus-first-input-field ( M-i )           | Move the focus to the first inputtable element of BUFFER.                        |
| scroll-page-up ( M-v )                    | Scroll up by one page height.                                                    |
| copy ( M-w )                              | Copy selected text to clipboard.                                                 |
| paste-from-clipboard-ring ( M-y )         | Show \`\*browser\*' clipboard ring and paste selected entry.                     |
| previous-heading ( p )                    | Scroll to the previous heading of the BUFFER.                                    |
| next-heading ( n )                        | Scroll to the next heading of the BUFFER.                                        |
| jump-to-heading-buffers ( C-M-. )         | Jump to a particular heading, of type h1, h2, h3, h4, h5, or h6 across a set     |
| passthrough-mode ( C-M-Z )                | Toggle \`passthrough-mode'.                                                      |
| open-inspector ( C-M-c )                  | Open the inspector, a graphical tool to inspect and change the buffer's content. |
| open-inspector ( C-M-c )                  | Open the inspector, a graphical tool to inspect and change the buffer's content. |
| select-all ( C-x h )                      | Select all the text in the text field.                                           |
| zoom-page ( C-x C-+ )                     | Zoom in the current page BUFFER.                                                 |
| reset-page-zoom ( C-x C-0 )               | Reset the BUFFER zoom to the \`zoom-ratio-default' or RATIO.                     |
| zoom-page ( C-x C-+ )                     | Zoom in the current page BUFFER.                                                 |
| edit-with-external-editor ( C-u C-x C-f ) | Edit the current input field using \`external-editor-program'.                   |
| unzoom-page ( C-x C-hyphen )              | Zoom out the current page in BUFFER.                                             |

<a id="table--search-buffer-mode-emacs-map"></a>

| Command                       | Documentation                               |
|-------------------------------|---------------------------------------------|
| remove-search-marks ( C-s k ) | Remove all search marks.                    |
| search-buffer ( s )           | Search incrementally on the current buffer. |

<a id="table--autofill-mode-default-map"></a>

| Command          | Documentation                                   |
|------------------|-------------------------------------------------|
| autofill ( C-i ) | Fill in a field with a value from a saved list. |

<a id="table--spell-check-mode-emacs-map"></a>

| Command                  | Documentation       |
|--------------------------|---------------------|
| spell-check-word ( M-$ ) | Spell check a word. |

<a id="table--base-mode-emacs-map"></a>

| Command                                 | Documentation                                                              |
|-----------------------------------------|----------------------------------------------------------------------------|
| delete-panel-buffer ( f4 )              | Prompt for panel buffer(s) to be deleted.                                  |
| reopen-buffer ( C-T )                   | Reopen queried deleted buffer(s).                                          |
| list-downloads ( C-d )                  | Display a buffer listing all downloads.                                    |
| set-url ( C-l )                         | Set the URL for the current buffer, completing with history.               |
| reload-current-buffer ( C-r )           | Reload current buffer.                                                     |
| make-buffer-focus ( C-t )               | Switch to a new buffer.                                                    |
| repeat-key ( M-1 )                      | Repeat the command bound to the user-pressed keybinding TIMES times.       |
| set-url-new-buffer ( M-l )              | Prompt for a URL and set it in a new focused buffer.                       |
| toggle-prompt-buffer-focus ( C-x o )    | Toggle the focus between the current buffer and the current prompt buffer. |
| reload-buffers ( M-r )                  | Prompt for BUFFERS to be reloaded.                                         |
| execute-command ( C-space )             | Execute a command by name.                                                 |
| toggle-fullscreen ( f11 )               | Fullscreen WINDOW, or the current window, when omitted.                    |
| describe-class ( C-h C )                | Inspect a class and show it in a help buffer.                              |
| describe-any ( C-h a )                  | Inspect anything and show it in a help buffer.                             |
| describe-bindings ( ? )                 | Show a list of all available keybindings in the current buffer.            |
| describe-command ( C-h c )              | Inspect a command and show it in a help buffer.                            |
| describe-function ( C-h f )             | Inspect a function and show it in a help buffer.                           |
| describe-key ( C-h k )                  | Display binding of user-inputted keys.                                     |
| describe-package ( C-h p )              | Inspect a package and show it in a help buffer.                            |
| manual ( C-h r )                        | Display Nyxt manual.                                                       |
| describe-slot ( C-h s )                 | Inspect a slot and show it in a help buffer.                               |
| tutorial ( C-h t )                      | Display Nyxt tutorial.                                                     |
| describe-variable ( C-h v )             | Inspect a variable and show it in a help buffer.                           |
| delete-all-panel-buffers ( s-f4 )       | Delete all the open panel buffers in WINDOW.                               |
| copy-url ( C-M-l )                      | Save current URL to clipboard.                                             |
| copy-title ( C-M-t )                    | Save current page title to clipboard.                                      |
| execute-extended-command ( C-M-x )      | Prompt for arguments to pass to a given COMMAND.                           |
| describe-class ( C-h C )                | Inspect a class and show it in a help buffer.                              |
| describe-any ( C-h a )                  | Inspect anything and show it in a help buffer.                             |
| describe-bindings ( ? )                 | Show a list of all available keybindings in the current buffer.            |
| describe-command ( C-h c )              | Inspect a command and show it in a help buffer.                            |
| describe-function ( C-h f )             | Inspect a function and show it in a help buffer.                           |
| describe-key ( C-h k )                  | Display binding of user-inputted keys.                                     |
| describe-package ( C-h p )              | Inspect a package and show it in a help buffer.                            |
| manual ( C-h r )                        | Display Nyxt manual.                                                       |
| describe-slot ( C-h s )                 | Inspect a slot and show it in a help buffer.                               |
| tutorial ( C-h t )                      | Display Nyxt tutorial.                                                     |
| describe-variable ( C-h v )             | Inspect a variable and show it in a help buffer.                           |
| list-downloads ( C-d )                  | Display a buffer listing all downloads.                                    |
| list-downloads ( C-d )                  | Display a buffer listing all downloads.                                    |
| switch-buffer-next ( C-x C-right )      | Switch to the next buffer in the buffer tree.                              |
| switch-buffer ( C-x b )                 | Switch buffer using fuzzy completion.                                      |
| delete-buffer ( C-x k )                 | Query the buffer(s) to delete.                                             |
| toggle-prompt-buffer-focus ( C-x o )    | Toggle the focus between the current buffer and the current prompt buffer. |
| switch-buffer-previous ( C-x C-left )   | Switch to the previous buffer in the buffer tree.                          |
| execute-command ( C-space )             | Execute a command by name.                                                 |
| delete-current-window ( C-x 5 0 )       | Delete WINDOW, or the current window, when omitted.                        |
| delete-window ( C-x 5 1 )               | Delete the queried window(s).                                              |
| make-window ( C-x 5 2 )                 | Create a new window.                                                       |
| list-buffers ( C-x C-b )                | Show all buffers and their interrelations.                                 |
| quit ( C-x C-c )                        | Quit Nyxt.                                                                 |
| open-file ( C-x C-f )                   | Open a file from the filesystem.                                           |
| delete-current-buffer ( q )             | Delete the current buffer, and make the next buffer the current one. If no |
| resume-prompt ( M-space )               | Query an older prompt and resume it.                                       |
| switch-buffer-previous ( C-x C-left )   | Switch to the previous buffer in the buffer tree.                          |
| execute-extended-command ( C-M-x )      | Prompt for arguments to pass to a given COMMAND.                           |
| execute-predicted-command ( C-s-space ) | Execute the predicted next command.                                        |
| switch-buffer-next ( C-x C-right )      | Switch to the next buffer in the buffer tree.                              |
| switch-buffer-previous ( C-x C-left )   | Switch to the previous buffer in the buffer tree.                          |
| switch-buffer-next ( C-x C-right )      | Switch to the next buffer in the buffer tree.                              |


### <span class="section-num">2.2</span> Vim {#vim}

<a id="table--override-map"></a>

| Command                     | Documentation              |
|-----------------------------|----------------------------|
| execute-command ( C-space ) | Execute a command by name. |

<a id="table--help-mode-default-map"></a>

| Command                     | Documentation                                                              |
|-----------------------------|----------------------------------------------------------------------------|
| describe-bindings ( ? )     | Show a list of all available keybindings in the current buffer.            |
| jump-to-heading ( m )       | Jump to a particular heading, of type h1, h2, h3, h4, h5, or h6.           |
| next-heading ( n )          | Scroll to the next heading of the BUFFER.                                  |
| previous-heading ( p )      | Scroll to the previous heading of the BUFFER.                              |
| delete-current-buffer ( q ) | Delete the current buffer, and make the next buffer the current one. If no |
| search-buffer ( s )         | Search incrementally on the current buffer.                                |
| headings-panel ( t )        | Display a list of heading for jumping.                                     |

<a id="table--bookmarks-mode-vi-normal-map"></a>

| Command                       | Documentation                                                    |
|-------------------------------|------------------------------------------------------------------|
| list-bookmarks ( m l )        | List all bookmarks in a new buffer.                              |
| bookmark-current-url ( m M )  | Bookmark the URL of the current BUFFER.                          |
| delete-bookmark ( m d )       | Delete bookmark(s) matching the chosen URLS-OR-BOOKMARK-ENTRIES. |
| bookmark-hint ( m f )         | Prompt for element hints and bookmark them.                      |
| list-bookmarks ( m l )        | List all bookmarks in a new buffer.                              |
| bookmark-buffer-url ( m m )   | Bookmark the page(s) currently opened in the existing buffers.   |
| set-url-from-bookmark ( m o ) | Set the URL for the current buffer from a bookmark.              |
| bookmark-url ( m u )          | Prompt for a URL to bookmark.                                    |
| bookmark-hint ( m f )         | Prompt for element hints and bookmark them.                      |

<a id="table--history-mode-vi-normal-map"></a>

| Command                            | Documentation                                                          |
|------------------------------------|------------------------------------------------------------------------|
| history-backwards ( H )            | Go to parent URL of BUFFER in history.                                 |
| history-forwards-maybe-query ( L ) | If current node has multiple children, query which one to navigate to. |
| history-all-query ( M-H )          | Query URL to go to, from the whole history.                            |
| history-forwards-all-query ( M-L ) | Query URL to forward to, from all child branches.                      |
| history-backwards ( H )            | Go to parent URL of BUFFER in history.                                 |
| history-forwards ( M-] )           | Go forward one step/URL in BUFFER's history.                           |
| history-backwards-query ( M-h )    | Query parent URL to navigate back to.                                  |
| history-forwards-query ( M-l )     | Query forward-URL to navigate to.                                      |
| history-all-query ( M-H )          | Query URL to go to, from the whole history.                            |
| history-all-query ( M-H )          | Query URL to go to, from the whole history.                            |
| history-backwards ( H )            | Go to parent URL of BUFFER in history.                                 |
| history-forwards ( M-] )           | Go forward one step/URL in BUFFER's history.                           |
| history-backwards ( H )            | Go to parent URL of BUFFER in history.                                 |
| history-forwards ( M-] )           | Go forward one step/URL in BUFFER's history.                           |
| history-all-query ( M-H )          | Query URL to go to, from the whole history.                            |
| history-backwards-query ( M-h )    | Query parent URL to navigate back to.                                  |
| history-forwards-all-query ( M-L ) | Query URL to forward to, from all child branches.                      |
| history-backwards ( H )            | Go to parent URL of BUFFER in history.                                 |
| history-forwards ( M-] )           | Go forward one step/URL in BUFFER's history.                           |
| history-forwards-query ( M-l )     | Query forward-URL to navigate to.                                      |

<a id="table--hint-mode-vi-normal-map"></a>

| Command                                 | Documentation                                                                 |
|-----------------------------------------|-------------------------------------------------------------------------------|
| follow-hint-new-buffer-focus ( F )      | Like \`follow-hint-new-buffer', but with focus.                               |
| follow-hint ( f )                       | Prompt for element hints and open them in the current buffer.                 |
| follow-hint-new-buffer ( ; f )          | Like \`follow-hint', but open the selected hints in new buffers (no focus).   |
| follow-hint-nosave-buffer-focus ( g F ) | Like \`follow-hint-nosave-buffer', but with focus.                            |
| follow-hint-nosave-buffer ( g f )       | Like \`follow-hint', but open the selected hints in new \`nosave-buffer's (no |

<a id="table--document-mode-vi-normal-map"></a>

| Command                         | Documentation                                                                    |
|---------------------------------|----------------------------------------------------------------------------------|
| zoom-page ( + )                 | Zoom in the current page BUFFER.                                                 |
| reset-page-zoom ( 0 )           | Reset the BUFFER zoom to the \`zoom-ratio-default' or RATIO.                     |
| scroll-to-bottom ( G )          | Scroll to the bottom of the current page.                                        |
| paste-from-clipboard-ring ( P ) | Show \`\*browser\*' clipboard ring and paste selected entry.                     |
| scroll-left ( h )               | Scroll left the current page.                                                    |
| scroll-down ( j )               | Scroll down the current page.                                                    |
| scroll-up ( k )                 | Scroll up the current page.                                                      |
| scroll-right ( l )              | Scroll right the current page.                                                   |
| paste ( unbound )               | Paste from clipboard into active element.                                        |
| undo ( u )                      | Undo the last editing action.                                                    |
| previous-heading ( p )          | Scroll to the previous heading of the BUFFER.                                    |
| next-heading ( n )              | Scroll to the next heading of the BUFFER.                                        |
| reload-with-modes ( C-R )       | Reload the BUFFER with the queried modes.                                        |
| scroll-page-up ( C-b )          | Scroll up by one page height.                                                    |
| scroll-page-down ( C-f )        | Scroll down by one page height.                                                  |
| print-buffer ( C-p )            | Print the current buffer.                                                        |
| redo ( C-r )                    | Redo the last editing action.                                                    |
| headings-panel ( t )            | Display a list of heading for jumping.                                           |
| focus-first-input-field ( M-i ) | Move the focus to the first inputtable element of BUFFER.                        |
| previous-heading ( p )          | Scroll to the previous heading of the BUFFER.                                    |
| next-heading ( n )              | Scroll to the next heading of the BUFFER.                                        |
| cut ( d d )                     | Cut the selected text in BUFFER.                                                 |
| jump-to-heading-buffers ( g H ) | Jump to a particular heading, of type h1, h2, h3, h4, h5, or h6 across a set     |
| scroll-to-top ( g g )           | Scroll to the top of the current page.                                           |
| jump-to-heading ( m )           | Jump to a particular heading, of type h1, h2, h3, h4, h5, or h6.                 |
| copy ( y y )                    | Copy selected text to clipboard.                                                 |
| zoom-page ( + )                 | Zoom in the current page BUFFER.                                                 |
| unzoom-page ( hyphen )          | Zoom out the current page in BUFFER.                                             |
| reset-page-zoom ( 0 )           | Reset the BUFFER zoom to the \`zoom-ratio-default' or RATIO.                     |
| passthrough-mode ( C-M-Z )      | Toggle \`passthrough-mode'.                                                      |
| open-inspector ( C-M-c )        | Open the inspector, a graphical tool to inspect and change the buffer's content. |
| open-inspector ( C-M-c )        | Open the inspector, a graphical tool to inspect and change the buffer's content. |
| scroll-page-down ( C-f )        | Scroll down by one page height.                                                  |
| unzoom-page ( hyphen )          | Zoom out the current page in BUFFER.                                             |
| scroll-page-up ( C-b )          | Scroll up by one page height.                                                    |
| scroll-page-up ( C-b )          | Scroll up by one page height.                                                    |
| scroll-page-down ( C-f )        | Scroll down by one page height.                                                  |

<a id="table--search-buffer-mode-vi-normal-map"></a>

| Command                         | Documentation                               |
|---------------------------------|---------------------------------------------|
| search-buffer ( s )             | Search incrementally on the current buffer. |
| remove-search-marks ( unbound ) | Remove all search marks.                    |

<a id="table--autofill-mode-default-map"></a>

| Command          | Documentation                                   |
|------------------|-------------------------------------------------|
| autofill ( C-i ) | Fill in a field with a value from a saved list. |

<a id="table--spell-check-mode-vi-normal-map"></a>

| Command                  | Documentation       |
|--------------------------|---------------------|
| spell-check-word ( z = ) | Spell check a word. |

<a id="table--vi-normal-mode-vi-normal-map"></a>

| Command              | Documentation             |
|----------------------|---------------------------|
| vi-insert-mode ( i ) | Toggle \`vi-insert-mode'. |
| visual-mode ( v )    | Toggle \`visual-mode'.    |

<a id="table--base-mode-vi-normal-map"></a>

| Command                                 | Documentation                                                              |
|-----------------------------------------|----------------------------------------------------------------------------|
| repeat-key ( 1 )                        | Repeat the command bound to the user-pressed keybinding TIMES times.       |
| execute-command ( C-space )             | Execute a command by name.                                                 |
| make-buffer-focus ( B )                 | Switch to a new buffer.                                                    |
| delete-current-buffer ( q )             | Delete the current buffer, and make the next buffer the current one.       |
| set-url-new-buffer ( O )                | Prompt for a URL and set it in a new focused buffer.                       |
| reload-current-buffer ( R )             | Reload current buffer.                                                     |
| make-window ( C-w C-w )                 | Create a new window.                                                       |
| switch-buffer-previous ( [ )            | Switch to the previous buffer in the buffer tree.                          |
| switch-buffer-next ( ] )                | Switch to the next buffer in the buffer tree.                              |
| delete-buffer ( unbound )               | Query the buffer(s) to delete.                                             |
| set-url ( o )                           | Set the URL for the current buffer, completing with history.               |
| reload-buffers ( r )                    | Prompt for BUFFERS to be reloaded.                                         |
| reopen-buffer ( C-T )                   | Reopen queried deleted buffer(s).                                          |
| delete-panel-buffer ( f4 )              | Prompt for panel buffer(s) to be deleted.                                  |
| reopen-buffer ( C-T )                   | Reopen queried deleted buffer(s).                                          |
| set-url ( o )                           | Set the URL for the current buffer, completing with history.               |
| reload-current-buffer ( R )             | Reload current buffer.                                                     |
| make-buffer-focus ( B )                 | Switch to a new buffer.                                                    |
| set-url-new-buffer ( O )                | Prompt for a URL and set it in a new focused buffer.                       |
| toggle-prompt-buffer-focus ( M-o )      | Toggle the focus between the current buffer and the current prompt buffer. |
| reload-buffers ( r )                    | Prompt for BUFFERS to be reloaded.                                         |
| quit ( Z Z )                            | Quit Nyxt.                                                                 |
| toggle-fullscreen ( f11 )               | Fullscreen WINDOW, or the current window, when omitted.                    |
| switch-buffer ( g b )                   | Switch buffer using fuzzy completion.                                      |
| set-url-new-nosave-buffer ( g o )       | Prompt for a URL and set it in a new focused nosave buffer.                |
| copy-title ( y t )                      | Save current page title to clipboard.                                      |
| copy-url ( y u )                        | Save current URL to clipboard.                                             |
| describe-class ( f1 C )                 | Inspect a class and show it in a help buffer.                              |
| describe-any ( f1 a )                   | Inspect anything and show it in a help buffer.                             |
| describe-bindings ( ? )                 | Show a list of all available keybindings in the current buffer.            |
| describe-command ( f1 c )               | Inspect a command and show it in a help buffer.                            |
| describe-function ( f1 f )              | Inspect a function and show it in a help buffer.                           |
| describe-key ( f1 k )                   | Display binding of user-inputted keys.                                     |
| describe-package ( f1 p )               | Inspect a package and show it in a help buffer.                            |
| manual ( f1 r )                         | Display Nyxt manual.                                                       |
| describe-slot ( f1 s )                  | Inspect a slot and show it in a help buffer.                               |
| tutorial ( f1 t )                       | Display Nyxt tutorial.                                                     |
| describe-variable ( f1 v )              | Inspect a variable and show it in a help buffer.                           |
| delete-all-panel-buffers ( s-f4 )       | Delete all the open panel buffers in WINDOW.                               |
| set-url-new-nosave-buffer ( g o )       | Prompt for a URL and set it in a new focused nosave buffer.                |
| list-downloads ( C-s-Y )                | Display a buffer listing all downloads.                                    |
| list-downloads ( C-s-Y )                | Display a buffer listing all downloads.                                    |
| switch-buffer-next ( ] )                | Switch to the next buffer in the buffer tree.                              |
| delete-current-window ( C-w q )         | Delete WINDOW, or the current window, when omitted.                        |
| switch-buffer-previous ( [ )            | Switch to the previous buffer in the buffer tree.                          |
| execute-command ( C-space )             | Execute a command by name.                                                 |
| delete-window ( C-w C-q )               | Delete the queried window(s).                                              |
| make-window ( C-w C-w )                 | Create a new window.                                                       |
| resume-prompt ( M-space )               | Query an older prompt and resume it.                                       |
| execute-extended-command ( C-M-space )  | Prompt for arguments to pass to a given COMMAND.                           |
| execute-predicted-command ( C-s-space ) | Execute the predicted next command.                                        |


## <span class="section-num">3</span> Расширения {#расширения}


### <span class="section-num">3.1</span> nx-freestance-handler {#nx-freestance-handler}

-   Репозиторий: <https://github.com/kssytsrk/nx-freestance-handler>
-   Перенаправление с основных веб-сайтов на их зеркала, поддерживающие конфиденциальность.
-   Перенаправление:
    -   с Youtube на Invidious,
    -   с Reddit на Teddit,
    -   с Instagram на Bibliogram;
    -   с Twitter на Nitter.


### <span class="section-num">3.2</span> nx-search-engines {#nx-search-engines}

-   Репозиторий: <https://github.com/aartaka/nx-search-engines>
-   Упрощение использования разных поисковых систем.


### <span class="section-num">3.3</span> nx-ace {#nx-ace}

-   Репозиторий: <https://github.com/atlas-engineer/nx-ace>
-   Использование редактора Ace в Nyxt.
-   Редактор Ace: <https://ace.c9.io/>


### <span class="section-num">3.4</span> nx-kaomoji {#nx-kaomoji}

-   Репозитоирий: <https://github.com/aartaka/nx-kaomoji.git>
-   Позволяет вставлять Kaomoji в любое поле ввода с помощью специальной команды.
-   Kaomoji --- японские смайлики (например, <http://kaomoji.ru/>)


### <span class="section-num">3.5</span> nx-fruit {#nx-fruit}

-   Репозиторий: <https://github.com/atlas-engineer/nx-fruit>
-   Показывает фрукт дня.


### <span class="section-num">3.6</span> nx-router {#nx-router}

-   Репозиторий: <https://github.com/migalmoreno/nx-router>
-   Упрощение обработки ресурсов (перенаправлений, блокировщиков, обработчиков ресурсов), используя декларативное описание.


### <span class="section-num">3.7</span> nx-tailor {#nx-tailor}

-   Репозиторий: <https://github.com/migalmoreno/nx-tailor>
-   Переключение тем на основе правил.


### <span class="section-num">3.8</span> nx-zotero {#nx-zotero}

-   Репозиторий: <https://github.com/rolling-robot/nx-zotero>
-   Подключение к Zotero.


### <span class="section-num">3.9</span> nx-dark-reader {#nx-dark-reader}

-   Репозиторий: <https://github.com/aartaka/nx-dark-reader>
-   Интеграция с Dark Reader.
-   Dark Reader (<https://darkreader.org/>) позволяет включить тёмную тему на любом сайте.


## <span class="section-num">4</span> Материалы {#материалы}


### <span class="section-num">4.1</span> Конфигурации {#конфигурации}

-   <https://github.com/aartaka/nyxt-config>
-   <https://github.com/Gavinok/dotnyxt>
-   <https://github.com/ericdrgn/drgn.nyxt>


### <span class="section-num">4.2</span> Дискуссии {#дискуссии}

-   <https://discourse.atlas.engineer/>
