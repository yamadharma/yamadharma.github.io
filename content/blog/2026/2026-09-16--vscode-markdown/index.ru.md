---
title: "VSCode. Расширения для markdown"
author: ["Dmitry S. Kulyabov"]
date: 2026-09-16T20:51:00+03:00
lastmod: 2026-09-17T21:39:00+03:00
tags: ["programming", "markdown"]
categories: ["computer-science"]
draft: false
slug: "vscode-markdown"
---

VSCode. Расширения для markdown.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Расширения доступны в панели расширений VS Code (горячая клавиша `Ctrl+Shift+X`).
-   Для установки запустите функцию быстрого открытия VS Code (`Ctrl+P`), вставьте команду установки и нажмите `Enter`.
-   Для установки из консоли:
    ```shell
    code --install-extension <publisher.extension-name>
    ```


## <span class="section-num">2</span> Markdown All in One {#markdown-all-in-one}

-   Расширение: yzhang.markdown-all-in-one
    -   Из vscode
        ```shell
        ext install yzhang.markdown-all-in-one
        ```
    -   Из консоли
        ```shell
        code --install-extension yzhang.markdown-all-in-one
        ```
-   Основа для работы с Markdown.
-   Расширение добавляет горячие клавиши для форматирования (`Ctrl+B` для жирного, `Ctrl+I` для курсива).
-   Автоматически генерирует и обновляет оглавление при вводе `[TOC]`.
-   Помогает с форматированием таблиц и списков.


## <span class="section-num">3</span> Markdown Preview Enhanced {#markdown-preview-enhanced}

-   Расширение: shd101wyy.markdown-preview-enhanced
    -   Из vscode:
        ```shell
        ext install shd101wyy.markdown-preview-enhanced
        ```
    -   Из консоли:
        ```shell
        code --install-extension shd101wyy.markdown-preview-enhanced
        ```
-   Продвинутый предпросмотр.
-   Поддерживает рендеринг диаграмм Mermaid и PlantUML, математических формул LaTeX.
-   С его помощью можно экспортировать документы в PDF, HTML, PNG и JPEG.


### <span class="section-num">3.1</span> Клавиатурные сочетания {#клавиатурные-сочетания}

| Клавиши               | Функциональность                                         |
|-----------------------|----------------------------------------------------------|
| `Ctrl-k v`            | Открыть предварительный просмотр сбоку                   |
| `Ctrl-Shift-v`        | Открыть предварительный просмотр                         |
| `Ctrl-k Shift-l`      | Откройте заблокированный предварительный просмотр сбоку. |
| `Ctrl-k Ctrl-Shift-l` | Переключить блокировку предварительного просмотра        |
| `Ctrl-Shift-s`        | Синхронизация                                            |
| `Shift-Enter`         | Выполнить фрагмент кода                                  |
| `Ctrl-Shift-Enter`    | Выполните все фрагменты кода                             |
| `Ctrl-shift-=`        | Предварительный просмотр с увеличением                   |
| `Ctrl-Shift-_`        | Предварительный просмотр с уменьшением                   |
| `Ctrl-0`              | Сброс масштабирования                                    |
| `Esc`                 | Переключить оглавление боковой панели                    |


## <span class="section-num">4</span> markdownlint {#markdownlint}

-   Расширение: DavidAnson.vscode-markdownlint
    -   Из vscode:
        ```shell
        ext install DavidAnson.vscode-markdownlint
        ```
    -   Из консоли:
        ```shell
        code --install-extension davidanson.vscode-markdownlint
        ```
-   Линтер.


### <span class="section-num">4.1</span> Использовать {#использовать}

-   При редактировании файла любые строки, нарушающие правила, вызовут предупреждение в редакторе.
-   Предупреждения обозначаются волнистой зеленой линией.
-   Могут быть просмотрены нажатием клавиши `Ctrl+Shift+M` для открытия диалогового окна «Ошибки и предупреждения».
-   Наведите указатель мыши на зеленую строку, чтобы увидеть предупреждение, или нажмите `F8` и `Shift+F8` для переключения между всеми предупреждениями.


## <span class="section-num">5</span> Paste Image {#paste-image}

-   Расширение: mushan.vscode-paste-image
    -   Из vscode:
        ```shell
        ext install mushan.vscode-paste-image
        ```
    -   Из консоли:
        ```shell
        code --install-extension mushan.vscode-paste-image
        ```
-   Упрощает вставку изображений.


### <span class="section-num">5.1</span> Использование {#использование}

-   Сделать снимок экрана в буфер обмена.
-   Откройте палитру команд: `Ctrl+Shift+P` (`Cmd+Shift+P` на Mac).
-   Введите команду «Вставить изображение» или воспользуйтесь стандартной комбинацией клавиш `Ctrl+Alt+V` (`Cmd+Alt+V` на Mac).
-   Изображение будет сохранено в папке, содержащей текущий файл редактирования.
-   Относительный путь будет вставлен в текущий редактируемый файл.


## <span class="section-num">6</span> Quarto {#quarto}

-   Расширенеи: quarto.quarto
    -   Из vscode:
        ```shell
        ext install quarto.quarto
        ```
    -   Из консоли:
        ```shell
        code --install-extension quarto.quarto
        ```
-   Официальное расширение для работы с системой Quarto.


### <span class="section-num">6.1</span> Использование {#использование}

-   Чтобы преобразовать `.qmd` в финальный документ (HTML, PDF, DOCX), нажмите `Ctrl+Shift+K` (`Cmd+Shift+K` на Mac) или воспользуйтесь кнопкой `Render` в правом верхнем углу редактора.


## <span class="section-num">7</span> PandocCiter {#pandocciter}

-   Расширение: notZaki.pandoc-citer
    -   Из vscode:
        ```shell
        ext install notZaki.pandocciter
        ```
    -   Из консоли:
        ```shell
        code --install-extension notzaki.pandocciter
        ```

-   Обеспечивает автодополнение цитат и перекрёстных ссылок для документов Markdown.


### <span class="section-num">7.1</span> Использование {#использование}

-   В начале вашего Markdown-файла добавьте YAML-заголовок, указав путь к файлу библиографии:
    ```yaml
    ---
    bibliography: references.bib
    ---
    ```
-   При вводе `@` в тексте документа появится окно автодополнения с ключами из вашего `.bib` файла.
-   Выберите нужный источник, и в тексте появится ссылка вида `[@citekey]`.
