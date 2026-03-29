---
title: "Markdown. Утилита markitdown"
author: ["Dmitry S. Kulyabov"]
date: 2026-03-27T09:02:00+03:00
lastmod: 2026-03-27T09:10:00+03:00
draft: false
slug: "markdown-markitdown"
---

Markdown. Утилита markitdown.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/microsoft/markitdown>
-   Библиотека с открытым исходным кодом, разработанная компанией Microsoft.
-   Предназначена для преобразования различных типов файлов (в основном офисных) в формат Markdown.

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Поддерживаемые форматы
</div>

| Категория      | Расширения / типы                              |
|----------------|------------------------------------------------|
| Документы      | PDF, PowerPoint (`.pptx`), Word (`.docx`)      |
| Таблицы        | Excel (`.xlsx`, `.xls`), CSV, JSON, XML        |
| Веб-страницы   | HTML, EPUB                                     |
| Изображения    | JPEG, PNG, GIF и др. --- через OCR (Tesseract) |
| Аудио          | MP3, WAV и др. --- через распознавание речи    |
| Архивы         | ZIP (рекурсивно обрабатывает содержимое)       |
| Видео (ссылки) | YouTube --- извлекает субтитры                 |


## <span class="section-num">2</span> Установка {#установка}

-   Чтобы получить все возможности (OCR, распознавание речи, работа с Excel и т.д.), рекомендуется устанавливать с опцией `[all]`:

<!--listend-->

```shell
uv tool install 'markitdown[all]'
```


## <span class="section-num">3</span> Использование (командная строка) {#использование--командная-строка}

```shell
# Конвертировать PDF и вывести результат в консоль
markitdown отчет.pdf

# Сохранить результат в файл
markitdown презентация.pptx -o текст.md

# Обработать ZIP-архив (все файлы внутри)
markitdown архив.zip -o итог.md
```


## <span class="section-num">4</span> Использование (python) {#использование--python}

```python
from markitdown import MarkItDown

# Создаём объект конвертера
converter = MarkItDown()

# Конвертируем файл
result = converter.convert("таблица.xlsx")

# Печатаем полученный Markdown
print(result.text_content)

# Если нужно работать с содержимым
with open("результат.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)
```
