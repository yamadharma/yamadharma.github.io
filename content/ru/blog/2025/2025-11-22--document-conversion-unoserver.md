---
title: "Конвертация документов. unoserver"
author: ["Dmitry S. Kulyabov"]
date: 2025-11-22T18:03:00+03:00
lastmod: 2025-11-22T18:52:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "document-conversion-unoserver"
---

Конвертация документов. unoserver.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий: <https://github.com/unoconv/unoserver>
-   Используется для конвертации документов с использованием LibreOffice или OpenOffice.
-   Позволяет преобразовывать различные форматы документов в другие форматы.
-   Разработан как переписанная версия и потенциальная замена unoconv.
-   Не блокирует использование LibreOffice как обычного приложения.
-   Можно одновременно работать с документами и использовать сервер для конвертации.
-   Включает команды:
    -   `unoserver` (запускает слушатель),
    -   `unoconverter` (для конвертации документов);
    -   `unocompare` (для сравнения документов и конвертации результата);
    -   `unoping`.


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Gentoo {#gentoo}

-   Репозиторий karma ([Gentoo. Репозиторий karma]({{< relref "2024-05-25-gentoo-karma-repository" >}})):
    ```shell
    emerge app-office/unoserver
    ```


## <span class="section-num">3</span> Использование {#использование}

-   Сервер должен быть предварительно запущен.


### <span class="section-num">3.1</span> unoserver {#unoserver}

```shell
unoserver [-h] [-v] [--interface INTERFACE] [--uno-interface UNO_INTERFACE] [--port PORT] [--uno-port UNO_PORT] [--daemon] [--executable EXECUTABLE] [--user-installation USER_INSTALLATION] [-p/--libreoffice-pid-file LIBREOFFICE_PID_FILE] [--conversion-timeout CONVERSION_TIMEOUT] [--stop-after STOP_AFTER] [--verbose] [--quiet] [-f/--logfile logfile]
```

-   `-v`, `--version` : отобразить версию и выйти.
-   `--interface` : интерфейс, используемый сервером XMLRPC, по умолчанию 127.0.0.1.
-   `--port` : порт, используемый сервером XMLRPC, по умолчанию 2003.
-   `--uno-interface` : интерфейс, используемый сервером LibreOffice, по умолчанию 127.0.0.1.
-   `--uno-port` : порт, используемый сервером LibreOffice, по умолчанию 2002.
-   `--daemon` : демонизировать сервер.
-   `--executable` : путь к исполняемому файлу LibreOffice.
-   `--user-installation` : путь к профилю пользователя LibreOffice, по умолчанию --- динамически создаваемый временный каталог.
-   `--p`, `--libreoffice-pid-file` : если установлено, unoserver запишет PID процесса Libreoffice в этот файл. При запуске в режиме демона файл не будет удалён при завершении работы `unoserver`.
-   `--conversion-timeout` : завершить работу Libreoffice и выйти, если преобразование не завершится за указанное время (в секундах).
-   `--stop-after` : завершить работу Libreoffice и выйти после указанного количества запросов.
-   `--verbose` : добавить отладочную информацию в качестве вывода.
-   `--quiet` : выводить только ошибки и предупреждения.
-   `-f`, `--logfile` : Записывать журналы в файл (по умолчанию в stderr).


### <span class="section-num">3.2</span> unoconvert {#unoconvert}

```shell
unoconvert [-h] [-v] [--convert-to CONVERT_TO] [--input-filter INPUT_FILTER] [--output-filter OUTPUT_FILTER] [--filter-option FILTER_OPTIONS] [--update-index] [--dont-update-index] [--host HOST] [--port PORT] [--host-location {auto,remote,local}] [--protocol {http, https}] [-f/--logfile logfile] infile outfile
```

-   `infile` : путь к файлу, который необходимо преобразовать (используйте `-` для `stdin`).
-   `outfile` : путь к преобразованному файлу (используйте `-` для `stdout`).
-   `--convert-to` : тип/расширение выходного файла (например, `pdf`). Требуется при использовании stdout.
-   `--input-filter` : фильтр ввода LibreOffice, который будет использоваться (например, `writer8`), если автоопределение не удалось.
-   `--output-filter` : фильтр экспорта, используемый при конвертации. Если не указан, выбирается автоматически.
-   `--filter-option` : передайте параметр для фильтра экспорта в формате `имя=значение` или список позиционных параметров, разделённый запятыми.
    -   Используйте `true` / `false` для логических значений.
    -   Можно повторить для нескольких параметров.
-   `--password` : пароль.
-   `--host` : хост, используемый сервером, по умолчанию 127.0.0.1.
-   `--port` : порт, используемый сервером, по умолчанию 2003.
-   `--protocol` : какой протокол использовать для подключения к серверу (по умолчанию `http`).
-   `--host-location` : расположение хоста определяет обработку файлов.
    -   Если клиент запущен на той же машине, что и сервер, можно выбрать локальное расположение, и файлы будут отправляться в виде путей.
    -   Если же это разные машины, то расположение будет удалённым, и файлы будут отправляться в виде двоичных данных.
    -   Значение по умолчанию `auto`, и файл будет отправляться в виде пути, если хост --- 127.0.0.1 или `localhost`, и в виде двоичных данных для остальных хостов.
-   `-v`, `--version` : отобразить версию и выйти.
-   `-f`, `--logfile` : записывать журналы в файл (по умолчанию в `stderr`).
-   `--verbose` : увеличить объем выводимой информации в журналы.
-   `--quiet` : уменьшить вывод информации в журналы.

-   Пример настройки ширины/высоты PNG:

<!--listend-->

```shell
unoconvert infile.odt outfile.png --filter-options PixelWidth=640 --filter-options PixelHeight=480
```

-   Пример настройки параметров вывода CSV:

<!--listend-->

```shell
unoconvert infile.xlsx outfile.csv --filter-options "59,34,76,1"
```

-   Пример экспорта HTML со встроенными изображениями:

<!--listend-->

```shell
unoconvert infile.odt outfile.html --filter-options EmbedImages
```


### <span class="section-num">3.3</span> unocompare {#unocompare}

```shell
unocompare [-h] [-v] [--file-type FILE_TYPE] [--host HOST] [--port PORT] [--protocol {http, https}] [--host-location {auto,remote,local}] [-f/--logfile logfile] oldfile newfile outfile
```

-   Опции подобны опциям `unoconvert`.


### <span class="section-num">3.4</span> unoping {#unoping}

```shell
unoping [-h] [-v] [--host HOST] [--port PORT] [--protocol {http,https}] [--verbose | --quiet] [-f logfile]
```

-   Опции подобны опциям `unoconvert`.
