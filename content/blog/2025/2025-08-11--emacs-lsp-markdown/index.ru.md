---
title: "Emacs. LSP для Markdown"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-11T13:59:00+03:00
lastmod: 2025-08-11T15:53:00+03:00
tags: ["markdown", "emacs"]
categories: ["computer-science"]
draft: false
slug: "emacs-lsp-markdown"
---

Emacs. LSP для Markdown.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Серверы {#серверы}


### <span class="section-num">1.1</span> Marksman {#marksman}

-   Репозиторий: <https://github.com/artempyanykh/marksman>
-   LSP-сервер для Markdown.
-   Поддержка перекрёстных ссылок, автоформатирования и проверки синтаксиса.


### <span class="section-num">1.2</span> Unified Language Server {#unified-language-server}

-   Сайт: <https://unifiedjs.com/>
-   Репозиторий: <https://github.com/unifiedjs/unified-language-server>
-   Универсальный сервер для текстовых форматов, включая Markdown.


### <span class="section-num">1.3</span> Remark Language Server {#remark-language-server}

-   Репозиторий: <https://github.com/remarkjs/remark-language-server>
-   LSP-сервер для работы с Markdown.
-   Рекомендован для замены Unified Language Server.
-   Основан на инструменте remark.
-   Предоставляет линтинг, форматирование и базовую навигацию для Markdown-файлов.
-   Поддержка плагинов remark (например, для фронтматтера, GitHub-таблиц).
-   Интеграция с экосистемой Unified (используется в Prettier, Gatsby).
-   Не требует сложной настройки для базового использования.
-   Ограниченные возможности LSP. Нет продвинутого автодополнения или рефакторинга.
-   Для расширенных функций нужны плагины.
-   Меньше возможностей, чем у Marksman (например, нет перекрёстных ссылок между файлами).
