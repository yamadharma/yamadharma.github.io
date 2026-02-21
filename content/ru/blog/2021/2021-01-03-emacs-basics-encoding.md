---
title: "Emacs. Основы. Кодировка"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-03T12:22:00+03:00
lastmod: 2023-10-05T20:06:00+03:00
tags: ["emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-basics-encoding"
---

Настройка кодировки в Emacs.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Настройка кодировки по-умолчанию {#настройка-кодировки-по-умолчанию}

Обычно по-умолчанию устанавливают UTF-8:

```elisp
(prefer-coding-system 'utf-8)
(set-default-coding-systems 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-keyboard-coding-system 'utf-8)
(set-selection-coding-system 'utf-8)
(set-file-name-coding-system 'utf-8)
(set-clipboard-coding-system 'utf-8)
(set-buffer-file-coding-system 'utf-8)

(setq default-process-coding-system '(utf-8 . utf-8))

;;; Backwards compatibility as default-buffer-file-coding-system is deprecated in 23.2.
(if (boundp 'buffer-file-coding-system)
    (setq-default buffer-file-coding-system 'utf-8)
  (setq default-buffer-file-coding-system 'utf-8))

;;; Treat clipboard input as UTF-8 string first; compound text next, etc.
(setq x-select-request-type '(UTF8_STRING COMPOUND_TEXT TEXT STRING))
```


## <span class="section-num">2</span> Кодировка для файла {#кодировка-для-файла}

Для каждого конкретного файла можно установить кодировку в локальных переменных, например, в первой строке файла (как комментарий):

```elisp
-*- coding: utf-8 -*-
```


## <span class="section-num">3</span> Установка кодировки при операциях с файлами {#установка-кодировки-при-операциях-с-файлами}


### <span class="section-num">3.1</span> Открыть файл с заданной кодировкой {#открыть-файл-с-заданной-кодировкой}

Откройте файл в обычном режиме, затем нажмите `M+x revert-buffer-with-coding-system`, затем введите кодировку. Нажмите `Tab` для просмотра вариантов.


### <span class="section-num">3.2</span> Установить кодировку для сохранения файла {#установить-кодировку-для-сохранения-файла}

Нажмите `M+x set-buffer-file-coding-system`, затем введите желаемую кодировку. Нажмите =Tab=для просмотра вариантов.


## <span class="section-num">4</span> Информация по кодировке {#информация-по-кодировке}


### <span class="section-num">4.1</span> Кодировка текущего файла {#кодировка-текущего-файла}

Проверьте значение переменной `buffer-file-coding-system`. Можно сделать это с помощью `M+x description-variable` (комбинация клавиш `Ctrl+h v`).


### <span class="section-num">4.2</span> Какая кодировка используется для открытия и сохранения файлов {#какая-кодировка-используется-для-открытия-и-сохранения-файлов}

Наберите `M+x describe-coding-system`.


### <span class="section-num">4.3</span> Какие кодировки поддерживает emacs {#какие-кодировки-поддерживает-emacs}

Наберите `M+x list-coding-systems`.
