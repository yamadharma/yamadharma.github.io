---
title: "Репозитории для научных исследований. Zenodo"
author: ["Dmitry S. Kulyabov"]
date: 2025-08-27T17:41:00+03:00
lastmod: 2025-08-27T17:58:00+03:00
draft: false
slug: "research-repositories-zenodo"
---

Репозитории для научных исследований. Zenodo.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   <https://zenodo.org/>
-   Репозиторий научных данных.
-   Предназначен для хранения «всех результатов исследований любого направления науки».
-   Управляется ЦЕРН.
-   Любому файлу, загруженному на сервера Zenodo присваивается DOI.
-   Позволяет загружать файлы до 50 ГБ.
-   Есть интеграция с github.


## <span class="section-num">2</span> Подключение репозитория github к zenodo {#подключение-репозитория-github-к-zenodo}


### <span class="section-num">2.1</span> Общая информация {#общая-информация}

-   DOI присваивается каждому релизу, а не всему репозиторию.
-   Новые версии получают новые DOI.
-   Для общего DOI всех версий используйте концептуальный DOI из раздела _Cite all versions_ в Zenodo.


### <span class="section-num">2.2</span> Свяжите GitHub с Zenodo {#свяжите-github-с-zenodo}

-   Перейдите на _Zenodo_ и авторизуйтесь через кнопку _Log in with GitHub_.
-   В разделе _Account Settings_ → _GitHub_ найдите нужный репозиторий.
-   Активируйте интеграцию, переключив тумблер в положение _On_.


### <span class="section-num">2.3</span> Создайте релиз на GitHub {#создайте-релиз-на-github}

-   Можно создать релиз или из командной строки или через web-интерфейс.
-   В вашем репозитории перейдите в Releases → Draft a new release.
-   Укажите:
    -   Tag version: версия в формате `v1.0.0` (семантическое версионирование) (см. [Семантическое версионирование]({{< relref "2020-12-11-semantic-versioning" >}})).
    -   Release title: название релиза.
    -   Description: описание изменений.
-   Нажмите Publish release.


### <span class="section-num">2.4</span> Получите DOI через Zenodo {#получите-doi-через-zenodo}

-   Zenodo автоматически создаст DOI для этого релиза.
-   Проверьте его:
    -   Зайдите в Zenodo Uploads (<https://zenodo.org/deposit>).
    -   Найдите запись с названием вашего релиза.
    -   Скопируйте DOI (например, `10.5281/zenodo.1234567`).


### <span class="section-num">2.5</span> Настройка метаданных (опционально) {#настройка-метаданных--опционально}

-   Добавьте файл `.zenodo.json` в корень репозитория, чтобы кастомизировать метаданные:

<!--listend-->

```js
{
  "title": "Название проекта",
  "creators": [{"name": "Иванов, Иван", "affiliation": "Университет"}],
  "description": "Описание проекта",
  "keywords": ["ключевое слово 1", "ключевое слово 2"],
  "license": "MIT"
}
```


### <span class="section-num">2.6</span> Добавьте бейдж DOI в README {#добавьте-бейдж-doi-в-readme}

-   Вставьте в `README.md`:

<!--listend-->

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.<doi>.svg)](https://doi.org/10.5281/zenodo.<doi>)
```

-   Пример:

<!--listend-->

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16963592.svg)](https://doi.org/10.5281/zenodo.16963592)
```
