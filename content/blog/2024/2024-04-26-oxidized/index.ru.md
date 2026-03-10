---
title: "Система управления конфигурациями Oxidized"
author: ["Dmitry S. Kulyabov"]
date: 2024-04-26T17:44:00+03:00
lastmod: 2025-11-20T14:08:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "oxidized"
---

Система управления конфигурациями Oxidized.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Создавался как альтернатива RANCID.
-   Репозиторий: <https://github.com/ytti/oxidized>


## <span class="section-num">2</span> Установка {#установка}


### <span class="section-num">2.1</span> Необходимое программное обеспечение {#необходимое-программное-обеспечение}

-   Установите язык ruby:
    ```shell
    dnf -y install ruby
    ```
-   Установите необходимые средства разработки:
    ```shell
    dnf -y group install "Development Tools"
    dnf -y install make cmake which sqlite-devel ruby gcc ruby-devel libicu-devel gcc-c++
    dnf -y install openssl-devel
    ```
-   Установите git для хранения файлов:
    ```shell
    dnf -y install git
    ```


### <span class="section-num">2.2</span> Установка Oxidized {#установка-oxidized}

-   Добавьте пользователя `oxidized`:
    ```shell
    useradd -c "oxidized system account" -m -d /home/oxidized -s /bin/bash oxidized
    ```
-   Устанавливаем Oxidized:
    ```shell
    gem install oxidized
    gem install oxidized-script oxidized-web
    ```


### <span class="section-num">2.3</span> Обновление Oxidized {#обновление-oxidized}

-   Логинимся под пользователем oxidized:
    ```shell
    su - oxidized
    ```
-   Обновляем Oxidized:
    ```shell
    gem update oxidized
    gem update oxidized-script oxidized-web
    ```


## <span class="section-num">3</span> Конфигурация {#конфигурация}


### <span class="section-num">3.1</span> Конфигурация Oxidized {#конфигурация-oxidized}

-   Документация: <https://github.com/ytti/oxidized/blob/master/docs/Configuration.md>
-   Запустите oxidized однократно для создания структуры каталогов и шаблона конфигурационного файла:
    ```shell
    su - oxidized
    oxidized
    ```
-   Отредактируйте шаблон файла конфигурации `~oxidized/.config/oxidized/config`.
-   Oxidized использует формат YAML для конфигурационных файлов, поэтому все отступы должны быть выполнены пробелами, допускается два или четыре пробела на отступ.
-   Основные элементы файла конфигурации:
    -   Задание имени пользователя и пароля по умолчанию для соединения с устройствами:
        ```yaml
        username: oxidized
        password: Password
        ```
    -   Указание типа устройства по умолчанию (например, Cisco):
        ```yaml
        model: ios
        ```

        -   Список устройств можно посмотреть в <https://github.com/ytti/oxidized/tree/master/lib/oxidized/model>.
        -   Список операционных систем: <https://github.com/ytti/oxidized/blob/master/docs/Supported-OS-Types.md>.
    -   Зададим интервал создания копий данных в секундах (рекомендуется делать копии раз в сутки, что соответствует 86400 секундам):
        ```yaml
        interval: 86400
        ```
    -   Для устройств со слабыми характеристиками и медленными каналами связи рекомендуется увеличить таймаут (здесь таймаут 60 секунд, три повторные попытки):
        ```yaml
        timeout: 60
        retries: 3
        ```
    -   Если вы не хотите, чтобы ваши резервные копии содержали чувствительные данные, такие как ключи и пароли, добавьте следующую опцию:
        ```yaml
        remove_secret: true
        ```
    -   Раздел `input` отвечает за связь с устройствами (по умолчанию используются протоколы `ssh` и `telnet`, протокол `telnet` не безопасен, рекомендуется использовать только `ssh`):
        ```yaml
        input:
                default: ssh
                debug: false
                ssh:
                  secure: false
                ftp:
                  passive: true
                utf8_encoded: true
        ```
    -   Раздел `output` определяет способ хранения собранной информации (будем использовать _git_ для этой цели):
        ```yaml
        output:
                default: git
                git:
                  user: oxidized
                  email: oxidized@MYDOMAIN.ru
                  repo: "/home/oxidized/.config/oxidized/devices.git"
        ```
    -   Раздел `source` задаёт базу данных устройств (используем CSV-файл с двоеточием в качестве разделителя):
        ```yaml
        source:
                default: csv
                csv:
                  file: "/home/oxidized/.config/oxidized/router.db"
                  delimiter: !ruby/regexp /:/
                  map:
                    name: 0
                    model: 1
                    ip: 2
                    port: 3
                    username: 4
                    password: 5
                  gpg: false
        ```

        -   Опция `file` задаёт путь к файлу с базой устройств.
        -   Подсекция `map` определяет порядок параметров подключения к устройству в строке CSV-файла.
-   Весь файл конфигурации:
    ```yaml
    ---
    username: oxidized
    password: Password
    model: ios
    resolve_dns: true
    interval: 86400
    use_syslog: false
    debug: false
    threads: 30
    timeout: 140
    retries: 3
    prompt: !ruby/regexp /^([\w.@-]+[#>]\s?)$/
    rest: 127.0.0.1:8888
    next_adds_job: false
    remove_secret: true
    vars: {}
    groups: {}
    models: {}
    pid: "/home/oxidized/.config/oxidized/pid"
    log: "/home/oxidized/.config/oxidized/log"
    crash:
      directory: "/home/oxidized/.config/oxidized/crashes"
      hostnames: false
    stats:
      history_size: 10
    input:
      default: ssh
      debug: false
      ssh:
            secure: false
      ftp:
            passive: true
      utf8_encoded: true
    output:
      default: git
      git:
            user: oxidized
            email: oxidized@MYDOMAIN.ru
            repo: "/home/oxidized/.config/oxidized/devices.git"
    source:
      default: csv
      csv:
            file: "/home/oxidized/.config/oxidized/router.db"
            delimiter: !ruby/regexp /:/
            map:
              name: 0
              model: 1
              ip: 2
              port: 3
              username: 4
              password: 5
            gpg: false
    model_map:
      juniper: junos
      cisco: ios
    ```


### <span class="section-num">3.2</span> Хранение в git {#хранение-в-git}


#### <span class="section-num">3.2.1</span> Конфигурация сохранения в git {#конфигурация-сохранения-в-git}

-   Здесь используется интерфейс `libgit2` (не работают хуки).

<!--list-separator-->

1.  Репозиторий без групп

    -   Конфигурация имеет вид:
        ```yaml
        output:
          default: git
          git:
                user: Oxidized
                email: o@example.com
                repo: "/home/oxidized/.config/oxidized/devices.git"
        ```

<!--list-separator-->

2.  Репозитории с группами

    -   Конфигурация имеет вид:
        ```yaml
        output:
          default: git
          git:
                user: Oxidized
                email: o@example.com
                repo: "/home/oxidized/.config/oxidized/git-repos/default.git"
        ```
    -   Oxidized создаст репозиторий для каждой группы в том же каталоге, что и репозиторий `default.git`.
    -   Если вы хотите использовать группы и один репозиторий, вы можете принудительно сделать это с помощью конфигурации `single_repo`:
        ```yaml
        output:
          default: git
          git:
                single_repo: true
                repo: "/home/oxidized/.config/oxidized/devices.git"
        ```


#### <span class="section-num">3.2.2</span> Просмотр файлов устройств {#просмотр-файлов-устройств}

-   Перейдите в правильный репозиторий git для необходимого устройства и получите список устройств:
    ```shell
    git ls-files -s
    ```
-   Посмотрите содержимое файла:
    ```shell
    git cat-file -p <object id>
    ```


#### <span class="section-num">3.2.3</span> Удалить отключённое устройство {#удалить-отключённое-устройство}

-   Очистить сохранённую конфигурацию устройства:
    ```shell
    git rm --cached <object id>
    ```


### <span class="section-num">3.3</span> Файл описания оборудования {#файл-описания-оборудования}

-   Создадим файл: `/home/oxidized/.config/oxidized/router.db`:
    ```conf-unix
    sw01:ios:10.10.10.1
    sw02:ios:10.10.10.10:22:test:PASSWORD
    ```
-   Структура полей: наименование, тип оборудования, IP-адрес, порт, логин, пароль.
-   Если значения отсутствуют, то используются значения по умолчания.


### <span class="section-num">3.4</span> Службы запуска {#службы-запуска}

-   Запустим oxidized:
    ```shell
    systemctl enable --now oxidized.service
    ```


## <span class="section-num">4</span> Подключение к LibreNMS {#подключение-к-librenms}

-   Подключим oxidized к LibreNMS (см. [Система мониторинга LibreNMS]({{< relref "2023-03-20-librenms-monitoring-system" >}}))


### <span class="section-num">4.1</span> Общая информация {#общая-информация}

-   Интеграция LibreNMS с Oxidized дает следующие преимущества:
    -   Просмотр конфигурации: «Текущая», «История» и «Различия» на вкладке «Конфигурации» каждого устройства.
    -   Автоматическое добавление устройств в Oxidized: включая фильтрацию и группировку для упрощения управления учетными данными.
    -   Поиск конфигурации.


### <span class="section-num">4.2</span> Порядок действий {#порядок-действий}

-   Установить Oxidized.
-   Подключить Oxidized к web-интерфейсу LibreNMS.
-   Чтобы устройства добавлялись автоматически, вам необходимо настроить извлечения их из LibreNMS.
-   LibreNMS автоматически сопоставит ОС с именем модели Oxidized, не нужно использовать параметр конфигурации `model_map` в Oxidized.


### <span class="section-num">4.3</span> SELinux {#selinux}

-   Необходимо разрешить `httpd` исходящие подключения к сети:
    ```shell
    setsebool -P httpd_can_network_connect 1
    ```


### <span class="section-num">4.4</span> Подключение Oxidized к web-интерфейсу LibreNMS {#подключение-oxidized-к-web-интерфейсу-librenms}

-   Активируйте подключение к Oxidized/
    -   Подключить можно в web-интерфейсе:
        ```text
        https://<ваш URL-адрес librenms>/settings/external/oxidized
        ```
    -   Подключить можно в командной строке:
        ```shell
        lnms config:set oxidized.enabled true
        lnms config:set oxidized.url http://127.0.0.1:8888
        ```
-   Подключите управление версиями конфигурации (работает с модулем вывода git).
    -   Подключить можно в web-интерфейсе:
        ```text
        https://<ваш URL-адрес librenms>/settings/external/oxidized
        ```
    -   Подключить можно в командной строке:
        ```shell
        lnms config:set oxidized.features.versioning true
        ```


### <span class="section-num">4.5</span> Информация о группах {#информация-о-группах}

-   Oxidized поддерживает различные способы использования учётных данных для входа на устройства.
-   Вы можете указать глобальное имя пользователя и пароль в Oxidized, имя пользователя и пароль на уровне группы или для каждого устройства.
-   При синхронизации с LibreNMS можно делать только конфигурации для групп.
-   LibreNMS поддерживает отправку групп в Oxidized, чтобы вы могли затем определить учётные данные группы в Oxidized. Чтобы включить эту поддержку, включите «Включить возврат групп в Oxidized».
    -   Подключить можно в web-интерфейсе:
        ```text
        https://<ваш URL-адрес librenms>/settings/external/oxidized
        ```
    -   Подключить можно в командной строке:
        ```shell
        lnms config:set oxidized.group_support true
        ```
-   Можно установить группу по умолчанию (все устройства попадут в эту группу):
    -   Подключить можно в web-интерфейсе:
        ```text
        https://<ваш URL-адрес librenms>/settings/external/oxidized
        ```
    -   Подключить можно в командной строке:
        ```shell
        lnms config:set oxidized.default_group default
        ```


#### <span class="section-num">4.5.1</span> Задание разделения на группы {#задание-разделения-на-группы}

-   Группы для Oxidized никак не связаны с группами LibreNMS.
-   Чтобы вернуть переопределение в Oxidized, вы можете сделать это, предоставив ключ переопределения, затем сопоставив поиск хоста (или хостов) и, наконец, определив само значение переопределения.
-   LibreNMS не проверяет достоверность этих атрибутов, а передает их в Oxidized в соответствии с определением.
-   Сопоставление хостов можно выполнить с помощью `hostname`, `sysname`, `os`, `location`, `sysDescr`, `hardware`, `purpose`, `notes`.
-   Порядок соответствия следующий:
    -   hostname
    -   sysName
    -   sysDescr
    -   hardware
    -   os
    -   location
    -   ip
    -   purpose
    -   notes
-   Пример:
    ```shell
    lnms config:set oxidized.maps.group.os.+ '{"match": "ios", "value": "cisco"}'
    lnms config:set oxidized.maps.group.os.+ '{"match": "vrp", "value": "huawei"}'
    lnms config:set oxidized.maps.group.os.+ '{"match": "asa", "value": "asa"}'
    lnms config:set oxidized.maps.group.os.+ '{"match": "bdcom", "value": "bdcom"}'
    ```


#### <span class="section-num">4.5.2</span> Конфигурация в Oxidized {#конфигурация-в-oxidized}

-   При необходимости вы можете указать учетные данные для групп, используя следующее в вашей конфигурации Oxidized:
    ```yaml
    groups:
      <groupname>:
            username: <user>
            password: <password>
    ```
-   Например:
    ```yaml
    groups:
      cisco:
            username: user1
            password: password1
      asa:
            username: user2
            password: password2
      huawei:
            username: user3
            password: password3
      bdcom:
            username: user5
            password: password5
            vars:
              enable: enpassword5
      default:
            username: user4
            password: password4
    ```


### <span class="section-num">4.6</span> Автоматическое добавление устройств в Oxidized {#автоматическое-добавление-устройств-в-oxidized}

-   Нужно настроить учётные данные по умолчанию для ваших устройств в конфигурации Oxidized:
    ```yaml
    source:
      default: http
      debug: false
      http:
            url: https://<ваш URL-адрес librenms>/api/v0/oxidized
            map:
              name: hostname
              model: os
              group: group
            headers:
              X-Auth-Token: '01582bf94c03104ecb7953dsadsadwed'
            vars_map:
              ssh_port: ssh_port
              telnet_port: telnet_port
    ```

    -   Токен можно создать в меню _Шестерёнка &gt; API &gt; API Settings_:
        ```text
        https://<ваш URL-адрес librenms>/api-access
        ```

    -   Проверить взаимодействие можно из командной строки:
        ```shell
        curl -H 'X-Auth-Token: YOUR_AUTH_TOKEN' https://<ваш URL-адрес librenms>/api/v0/oxidized
        ```
-   LibreNMS может перезагружать список узлов каждый раз, когда устройство добавляется в LibreNMS.
    -   Подключить можно в web-интерфейсе:
        ```text
        https://<ваш URL-адрес librenms>/settings/external/oxidized
        ```
    -   Подключить можно в командной строке:
        ```shell
        sudo -u librenms env "PATH=$PATH" lnms config:set oxidized.reload_nodes true
        ```


### <span class="section-num">4.7</span> Переименование устройства {#переименование-устройства}


#### <span class="section-num">4.7.1</span> Попытка переписать историю git {#попытка-переписать-историю-git}

-   Чтобы история конфигурационных файлов осталась вместе с устройством, необходимо переписать историю git.
-   Для переписывания истории используется скрипт <https://gist.github.com/emiller/6769886>:
    ```shell
    #!/bin/bash
    #
    # git-mv-with-history -- move/rename file or folder, with history.
    #
    # Moving a file in git doesn't track history, so the purpose of this
    # utility is best explained from the kernel wiki:
    #
    #   Git has a rename command git mv, but that is just for convenience.
    #   The effect is indistinguishable from removing the file and adding another
    #   with different name and the same content.
    #
    # https://git.wiki.kernel.org/index.php/GitFaq#Why_does_Git_not_.22track.22_renames.3F
    #
    # While the above sucks, git has the ability to let you rewrite history
    # of anything via `filter-branch`. This utility just wraps that functionality,
    # but also allows you to easily specify more than one rename/move at a
    # time (since the `filter-branch` can be slow on big repos).
    #
    # Usage:
    #
    #   git-rewrite-history [-d/--dry-run] [-v/--verbose] <srcname>=<destname> <...> <...>
    #
    # After the repsitory is re-written, eyeball it, commit and push up.
    #
    # Given this example repository structure:
    #
    #   src/makefile
    #   src/test.cpp
    #   src/test.h
    #   src/help.txt
    #   README.txt
    #
    # The command:
    #
    #   git-rewrite-history README.txt=README.md  \     <-- rename to markdpown
    #                       src/help.txt=docs/    \     <-- move help.txt into docs
    #                       src/makefile=src/Makefile   <-- capitalize makefile
    #
    #  Would restructure and retain history, resulting in the new structure:
    #
    #    docs/help.txt
    #    src/Makefile
    #    src/test.cpp
    #    src/test.h
    #    README.md
    #
    # @author emiller
    # @date   2013-09-29
    #

    function usage() {
      echo "usage: `basename $0` [-d/--dry-run] [-v/--verbose] <srcname>=<destname> <...> <...>"
      [ -z "$1" ] || echo $1

      exit 1
    }

    [ ! -d .git ] && usage "error: must be ran from within the root of the repository"

    dryrun=0
    filter=""
    verbose=""
    repo=$(basename `git rev-parse --show-toplevel`)

    while [[ $1 =~ ^\- ]]; do
      case $1 in
        -d|--dry-run)
          dryrun=1
          ;;

        -v|--verbose)
          verbose="-v"
          ;;

        *)
          usage "invalid argument: $1"
      esac

      shift
    done

    for arg in $@; do
      val=`echo $arg | grep -q '=' && echo 1 || echo 0`
      src=`echo $arg | sed 's/\(.*\)=\(.*\)/\1/'`
      dst=`echo $arg | sed 's/\(.*\)=\(.*\)/\2/'`
      dir=`echo $dst | grep -q '/$' && echo $dst || dirname $dst`

      [ "$val" -ne 1  ] && usage
      [ ! -e "$src"   ] && usage "error: $src does not exist"

      filter="$filter                            \n\
        if [ -e \"$src\" ]; then                 \n\
          echo                                   \n\
          if [ ! -e \"$dir\" ]; then             \n\
            mkdir -p ${verbose} \"$dir\" && echo \n\
          fi                                     \n\
          mv $verbose \"$src\" \"$dst\"          \n\
        fi                                       \n\
      "
    done

    [ -z "$filter" ] && usage

    if [[ $dryrun -eq 1 || ! -z $verbose ]]; then
      echo
      echo "tree-filter to execute against $repo:"
      echo -e "$filter"
    fi

    [ $dryrun -eq 0 ] && git filter-branch -f --tree-filter "`echo -e $filter`"
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 1:</span>
      /home/oxidized/bin/git-mv-with-history
    </div>

    -   Поместим его в файл `/home/oxidized/bin/git-mv-with-history`.
-   Полный скрипт взят со страницы: <https://github.com/ytti/oxidized/issues/1449>:
    ```shell
    #!/bin/bash
    ## https://github.com/ytti/oxidized/issues/1449
    #echo "Call rename-host host_old host_new huawei"

    OLD_NAME=$1
    NEW_NAME=$2
    HARD_TYPE=$3

    sudo systemctl stop oxidized

    sudo -u oxidized git config --global --add safe.directory "*"
    ## can't commit without setting email
    sudo -u oxidized git config --global user.email "oxidized@rudn.su"
    ## can't commit without setting name
    sudo -u oxidized git config --global user.name "Oxidized"

    rm -rf /tmp/devices.git.clone
    sudo -u oxidized mkdir -p /tmp/devices.git.clone && cd /tmp/devices.git.clone ;\
        git clone /home/oxidized/.config/oxidized/devices.git; \
        cd devices ; \
        /home/oxidized/bin/git-mv-with-history ${HARD_TYPE}/${OLD_NAME}=${HARD_TYPE}/${NEW_NAME} ; \
        git push --force
    rm -rf /tmp/devices.git.clone
    cd
    sudo -u librenms env "PATH=$PATH" lnms device:rename -vv ${OLD_NAME} ${NEW_NAME}
    sudo systemctl start oxidized
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 2:</span>
      ~/bin/rename-host
    </div>


#### <span class="section-num">4.7.2</span> Без сохранения истории git {#без-сохранения-истории-git}

-   Используем предыдущий файл.
    ```shell
    #!/bin/bash

    #echo "Call rename-host host_old host_new huawei"

    OLD_NAME=$1
    NEW_NAME=$2
    HARD_TYPE=$3

    sudo systemctl stop oxidized

    sudo -u oxidized git config --global --add safe.directory "*"
    ## can't commit without setting email
    sudo -u oxidized git config --global user.email "oxidized@rudn.su"
    ## can't commit without setting name
    sudo -u oxidized git config --global user.name "Oxidized"

    rm -rf /tmp/devices.git.clone
    sudo -u oxidized mkdir -p /tmp/devices.git.clone && cd /tmp/devices.git.clone ;\
        git clone /home/oxidized/.config/oxidized/devices.git; \
        cd devices ; \
        git mv ${HARD_TYPE}/${OLD_NAME} ${HARD_TYPE}/${NEW_NAME} ; \
        git commit -m "rename device ${HARD_TYPE}/${OLD_NAME} to ${HARD_TYPE}/${NEW_NAME}"
        git push

    ## Uses git filter-branch which rewrites history, so --force is needed
    #git push --force
    #cd ~
    rm -rf /tmp/devices.git.clone
    cd
    sudo -u librenms env "PATH=$PATH" lnms device:rename -vv ${OLD_NAME} ${NEW_NAME}
    sudo systemctl start oxidized
    ```
    <div class="src-block-caption">
      <span class="src-block-number">&#1056;&#1072;&#1089;&#1087;&#1077;&#1095;&#1072;&#1090;&#1082;&#1072; 3:</span>
      ~/bin/rename-host
    </div>
-   Запуск:
    ```shell
    rename-host <host_old> <host_new> <group_name>
    ```
