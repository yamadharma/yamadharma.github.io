---
title: "Python. Переход с pipx на uv"
author: ["Dmitry S. Kulyabov"]
date: 2026-03-21T14:21:00+03:00
lastmod: 2026-03-21T14:43:00+03:00
tags: ["programming", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "python-moving-pipx-uv"
---

Python. Переход с pipx на uv.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   `pipx` предназначен для установки и запуска Python-приложений в изолированных средах.
-   Трудно поддерживается.
    -   <https://bugs.gentoo.org/971387>
-   Предлагается заменить на `uv` и его компонент `uvx`.
-   `uv` --- менеджер пакетов и проектов Python, написанный на Rust.
-   Быстрее `pip` и `pipx`, умеет управлять версиями Python, виртуальными окружениями и проектами.
-   `uvx` --- встроенная команда `uv`, которая работает как аналог `pipx run` (запускает инструмент во временном виртуальном окружении без долгосрочной установки).
-   `uvx` является синонимом `uv tool run`.
-   Репозиторий: <https://github.com/astral-sh/uv>
-   Документация:
    -   <https://docs.astral.sh/uv/>
    -   <https://docs.astral.sh/uv/concepts/tools/>


## <span class="section-num">2</span> Установка uv {#установка-uv}

-   С помощью официального установщика:
    ```shell
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

-   Windows (PowerShell):
    ```powershell
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

-   Через pip:
    ```shell
    pip install uv
    ```

-   Менеджеры пакетов:
    ```shell
    brew install uv
    winget install astral-sh.uv
    choco install uv
    ```


## <span class="section-num">3</span> Соответствие команд {#соответствие-команд}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Основные команды <code>pipx</code> и их аналоги в <code>uv</code>
</div>

| Действие                                  | pipx                         | uv / uvx                                                    |
|-------------------------------------------|------------------------------|-------------------------------------------------------------|
| Установка инструмента                     | `pipx install PACKAGE`       | `uv tool install PACKAGE`                                   |
| Запуск инструмента без установки          | `pipx run PACKAGE [args...]` | `uvx PACKAGE [args...]` или `uv tool run PACKAGE [args...]` |
| Список установленных инструментов         | `pipx list`                  | `uv tool list`                                              |
| Обновление инструмента                    | `pipx upgrade PACKAGE`       | `uv tool upgrade PACKAGE`                                   |
| Обновление всех инструментов              | `pipx upgrade-all`           | `uv tool upgrade --all`                                     |
| Удаление инструмента                      | `pipx uninstall PACKAGE`     | `uv tool uninstall PACKAGE`                                 |
| Установка с дополнительными зависимостями | `pipx inject PACKAGE DEP`    | `uv tool install PACKAGE --with DEP`                        |
| Просмотр информации об окружении          | `pipx list --json`           | `uv tool list --show-paths` или `uv tool list --json`       |


### <span class="section-num">3.1</span> Примеры {#примеры}

-   Установка `black`:

<!--listend-->

```shell
# pipx
pipx install black

# uv
uv tool install black
```

-   Запуск `ruff` без установки:

<!--listend-->

```shell
# pipx
pipx run ruff check .

# uv
uvx ruff check .
```

-   Обновление всех инструментов:

<!--listend-->

```shell
# pipx
pipx upgrade-all

# uv
uv tool upgrade --all
```

-   Удаление `black`:

<!--listend-->

```sh
# pipx
pipx uninstall black

# uv
uv tool uninstall black
```

-   Установка `jupyter` и `notebook`:

<!--listend-->

```shell
# pipx
pipx install jupyter
pipx inject jupyter notebook

# uv (одной командой)
uv tool install jupyter --with notebook
```


## <span class="section-num">4</span> Перенос существующих инструментов из pipx в uv {#перенос-существующих-инструментов-из-pipx-в-uv}

-   `uv` и `pipx` используют разные места для хранения виртуальных окружений:
    -   `pipx` хранит окружения в `~/.local/pipx/venvs` (Linux/macOS) или `%USERPROFILE%\.local\pipx\venvs` (Windows).
    -   `uv` хранит окружения в `~/.local/share/uv/tools` (Linux/macOS) или `%LOCALAPPDATA%\uv\tools` (Windows).

-   Инструменты, установленные через `pipx`, не видны для `uv`, и наоборот.


### <span class="section-num">4.1</span> Переустановка через uv {#переустановка-через-uv}

-   Просто переустановите все необходимые инструменты с помощью `uv tool install`.


### <span class="section-num">4.2</span> Перенос с сохранением версий {#перенос-с-сохранением-версий}

-   Можно получить список установленных пакетов и их версий из `pipx` и затем установить их через `uv`:

<!--listend-->

```shell
# Получить список пакетов и версий (Linux/macOS)
pipx list --json | jq -r '.venvs[] | "\(.metadata.main_package.package)@\(.metadata.main_package.package_version)"'

# Затем установить каждый
uv tool install black==24.4.2
```


## <span class="section-num">5</span> Дополнительные возможности uv {#дополнительные-возможности-uv}

-   Управление версиями Python:
    ```shell
    uv python install 3.12
    uv python list
    ```

-   Создание и управление виртуальными окружениями:
    ```shell
    uv venv
    uv pip install requests
    ```

-   Работа с проектами (аналог `poetry` / `pipenv`):
    ```shell
    uv init my-project
    cd my-project
    uv add requests
    uv run python script.py
    ```

-   Глобальные инструменты с явным указанием версии Python:
    ```shell
    uv tool install black --python 3.10
    ```

-   Установка инструментов из git, локальных путей, URL:
    ```shell
    uv tool install --from git+https://github.com/psf/black black
    ```

-   Конфигурация через `~/.config/uv/uv.toml`.
    -   Можно задать пути к инструментам, настройки кэширования и т.д.
