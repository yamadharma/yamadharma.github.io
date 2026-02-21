---
title: "Сети. Натурное моделирование"
author: ["Dmitry S. Kulyabov"]
date: 2025-07-20T18:19:00+03:00
lastmod: 2025-07-28T18:04:00+03:00
tags: ["network", "modeling"]
categories: ["computer-science"]
draft: false
slug: "networks-natural-modeling"
---

Сети. Натурное моделирование.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Средства натурного моделирования {#средства-натурного-моделирования}


### <span class="section-num">1.1</span> Принципы классификации {#принципы-классификации}

-   Введём следующую классификацию на основе функциональности.
    -   Мультисистемные средства моделирования.
    -   Моностековые средства моделирования.
    -   Специализированные средства моделирования.


### <span class="section-num">1.2</span> Мультисистемные средства моделирования {#мультисистемные-средства-моделирования}

-   Для реалистичного моделирования требуется использовать натурные модели разных вендоров.
-   Образы оборудования можно получить в виде образов операционной системы.
-   Для запуска таких образов требуется использование средств эмуляции процессора (QEMU, VirtualBox, vmWare).


#### <span class="section-num">1.2.1</span> GNS3 {#gns3}

-   Сайт: <https://www.gns3.com/>
-   Документация: <https://docs.gns3.com/>
-   Репозиторий:
    -   <https://github.com/GNS3/gns3-gui>
    -   <https://github.com/GNS3/gns3-server>
    -   <https://github.com/GNS3/gns3-web-ui>
    -   <https://github.com/GNS3/dynamips>
-   Лицензия: GPL-3.0
-   Графический интерфейс [<a href="#citeproc_bib_item_1">1</a>].
-   Интерфейс командной строки отсутствует.
-   Поддерживает работу с образами виртуальных машин для разных сетевых систем.
-   Интерфейс может быть как в виде отдельного приложения с графическим интерфейсом операционной системы (Qt), так и в виде встроенного web-интерфейса.
-   Использует интерфейс вложенных виртуальных машин.
-   Используется несколько типов виртуальных машин:
    -   Dynamips: для эмуляции Cisco IOS;
    -   QEMU: для запуска виртуальных машин (Cisco ASAv, Juniper vSRX);
    -   Docker: интеграция контейнеров.
-   Изначально основным эмулятором был эмулятор Dynamips.
-   GNS3 имеет крайне низкий уровень входа (в основном из-за графического интерфейса).
-   GNS3 вполне применим для научного моделирования сетей [<a href="#citeproc_bib_item_2">2</a>].
-   Однако проблема воспроизводимости исследований практически неразрешима.


#### <span class="section-num">1.2.2</span> Eve-ng {#eve-ng}

-   Сайт: <https://www.eve-ng.net/>
-   EVE-NG (Emulated Virtual Environment).
-   Лицензия: EULA (<https://www.eve-ng.net/index.php/documentation/eula/>).
-   Графический интерфейс.
-   Основан на проекте UNetLab (разработка прекращена в 2016 году).
-   Идеологически похож на GNS3.
-   Фактически сходный функционал.
-   Варианты:
    -   Community Edition, ограничения по размерам проекта;
    -   Professonal, предлагает расширенную функциональность;
    -   Corporate, возможность совместной работы.


#### <span class="section-num">1.2.3</span> PNetLab {#pnetlab}

-   Сайт: <https://pnetlab.com/pages/main>
-   Репозиторий: <https://github.com/pnetlab/pnetlab_main>
-   Документация: <https://www.pnetlab.com/pages/documentation>
-   Графический интерфейс.
-   Является форком Eve-ng.
-   Функциональность как у Eve-ng, но без необходимости оплаты.
-   Разработчики Eve-ng высказывали неудовольствие этим проектом (<https://www.eve-ng.net/forum/viewtopic.php?f=4&t=16925>).
-   Лицензия: не известно.
-   Проект выглядит заброшенным.


#### <span class="section-num">1.2.4</span> Containerlab {#containerlab}

-   Сайт: <https://containerlab.dev/>
-   Репозиторий: <https://github.com/srl-labs/containerlab>
-   Разработана Nokia.
-   Лицензия: BSD-3-Clause.
-   Виртуальные сетевые лаборатории строятся на базе контейнеров Docker.
-   Управление окружением происходит в специальном командном окружении.
-   Топология описывается в yaml-файле.
-   Решение поддерживает работу со множеством сетевых операционных систем, представленных в виде образов виртуальных машин.
-   Возможно объединять контейнеры и виртуальные машины в единую топологию.
-   Пакет vrnetlab (<https://github.com/vrnetlab/vrnetlab)> позволяет подключать виртуальную машину внутрь контейнера.
-   Можно создавать лаборатории, которые включают не только сетевые узлы, но и все, что между ними: стеки телеметрии, базы данных, узлы тестового оборудования, веб-серверы.


#### <span class="section-num">1.2.5</span> netlab {#netlab}

-   Сайт: <https://netlab.tools/>
-   Лицензия: MIT.
-   Фреймворк для автоматизации проектирования, развертывания и тестирования сетевых лабораторий с использованием концепции Infrastructure as Code (IaC).
-   Описание конфигураций через абстрактные функциональные модули, без привязки к вендору.
-   В качестве модельных провайдеров можно использовать Docker, Vagrant, KVM, Virtualbox, containerlab.


### <span class="section-num">1.3</span> Моностековые средства моделирования {#моностековые-средства-моделирования}

-   Данные системы реализуют какой-либо один сетевой стек.
-   Чаще всего на основе Linux.
-   Это позволяет оптимизировать средство моделирования намного сильнее, чем мультисистемные средства.


#### <span class="section-num">1.3.1</span> Mininet {#mininet}

-   Сайт: <https://mininet.org/>
-   Репозиторий: <https://github.com/mininet/mininet>
-   Лицензия: BSD-3-Clause.
-   Разработан в Стэнфордском университете.
-   Позволяет строить простые сети.
-   Можно реализовать технологии OpenFlow и SDN.
-   Настройки контроллеров на базе OpenFlow можно мигрировать на физическое оборудование.
-   Узлы сети в Mininet представляют собой процессы, запущенные в сетевом пространстве имён.
-   Такой подход позволяет изолировать хосты на одной машине друг от друга, но при этом каждый из них имеет собственный интерфейс.
-   Поддерживается Python API.
-   Данное средство первоначально было создано как специализированное средство моделирования. Основное предназначение --- моделирование Software-Defined Networks (SDN) [<a href="#citeproc_bib_item_3">3</a>–<a href="#citeproc_bib_item_5">5</a>].
-   Но постепенно произошёл дрейф в сторону универсальных пакетов моделирования.
-   Представляется, что это произошло из-за внедрения Mininet в обучение [<a href="#citeproc_bib_item_6">6</a>].
-   Кроме того, в рамках моделирования на Mininet исследователи стали уделять повышенное внимание воспроизводимости исследований [<a href="#citeproc_bib_item_7">7</a>–<a href="#citeproc_bib_item_9">9</a>].


#### <span class="section-num">1.3.2</span> Netkit {#netkit}

-   Сайт: <https://www.netkit.org/>
-   Разрабатывался для научных исследований и обучения [<a href="#citeproc_bib_item_10">10</a>; <a href="#citeproc_bib_item_11">11</a>].
-   Реализация строилась на подсистеме User-Mode Linux (UML).
-   с имеет исключительно историческое значение.
-   Заменён на Kathará.


#### <span class="section-num">1.3.3</span> Kathará {#kathará}

-   Сайт: <https://www.kathara.org/>
-   Репозиторий: <https://github.com/KatharaFramework/Kathara>
-   Лицензия: GPL-3.0.
-   Является развитием сетевого эмулятора Netkit [<a href="#citeproc_bib_item_12">12</a>].
-   Фактически можно воспринимать как Netkit, в котором User-Mode Linux заменён на Docker.
-   Kathará позволяет моделировать виртуальные сети на базе контейнеров Docker или кластеров Kubernetes [<a href="#citeproc_bib_item_13">13</a>; <a href="#citeproc_bib_item_14">14</a>].
-   Поддерживает технологии SDN, NFV (Network function virtualization), BGP, OSPF.
-   Есть графический интерфейс: Netkit-Lab-Generator (<https://github.com/KatharaFramework/Netkit-Lab-Generator>).
-   Особенностью данного проекта является его быстрое революционное развитие.
-   Постоянно появляются варианты данного эмулятора, направленные на решение новых задач.
-   В дальнейшем, чаще всего, эти новые ответвления вливаются в исходный проект.
-   Приведём примеры некоторых из них.

<!--list-separator-->

1.  Megalos и Sybil

    -   Проект Megalos направлен на моделирование больших гетерогенных сетей [<a href="#citeproc_bib_item_15">15</a>; <a href="#citeproc_bib_item_16">16</a>].
    -   Основное направление моделирования --- сетевая архитектура центров обработки данных.
    -   Используются сети VXLAN с маршрутизацией BGP.
    -   В подсистему Docker введён оркестратор Kubernetes, что позволяет моделировать большие сети.
    -   Распределение эмуляции по нескольким узлам позволяет Megalos эмулировать крупномасштабные сетевые инфраструктуры, где требуется значительное количество виртуальных локальных сетей.
    -   На основе Kathará и Megalos была создана программная платформа Sibyl [<a href="#citeproc_bib_item_17">17</a>].
    -   Sibyl реализует моделирование протоколов маршрутизации в сетях с толстыми деревьями.

<!--list-separator-->

2.  Вложенные контейнеры

    -   Задача состояла в построении цифрового двойника центра обработки данных.
    -   Для точной эмуляции иерархии, состоящей из физических серверов, виртуальных машин и контейнеров, поддержка вложенной виртуализации является фундаментальным требованием.
    -   Для решения этой задачи и была разработана возможность использования вложенных контейнеров [<a href="#citeproc_bib_item_18">18</a>].


#### <span class="section-num">1.3.4</span> IMUNES {#imunes}

-   IMUNES (Integrated Multi-protocol Network Emulator/Simulator).
-   Сайт: <https://imunes.net/>
-   Репозиторий: <https://github.com/imunes/imunes>
-   Лицензия: CC-BY 4.0.
-   Возможно использование как графического интерфейса, так и скриптового языка.
-   Реализует сетевой стек FreeBSD [<a href="#citeproc_bib_item_19">19</a>].
-   Host: Linux, FreeBSD.
-   Виртуализация [<a href="#citeproc_bib_item_20">20</a>]:
    -   FreeBSD: jails;
    -   Linux: Docker.
-   Развитие неравномерное.
-   Одно время создавалось впечатление, что проект заброшен.
-   Это типичный локальный проект для конкретных целей разработчиков.
-   Если что не нужно им, то это и не будет реализовано.


#### <span class="section-num">1.3.5</span> CORE {#core}

-   CORE (Common Open Research Emulator).
-   Сайт: <https://coreemu.github.io/core/>
-   Репозиторий: <https://github.com/coreemu/core>
-   Документация: <https://coreemu.github.io/core/index.html>
-   Лицензия: BSD-2-Clause.
-   Виртуализация: Linux namespaces.
-   Реализует сетевой стек FreeBSD [<a href="#citeproc_bib_item_21">21</a>].
-   Поддерживает Docker-контейнеры для развертывания сервисов (DNS, HTTP).
-   Связи реализуются через Linux-мосты, VLAN, VPN.
-   Динамическая маршрутизация: Quagga/FRR.
-   Графический интерфейс для построения топологии.


#### <span class="section-num">1.3.6</span> Cloonix {#cloonix}

-   Сайт: <https://clownix.net/>
-   Репозиторий: <https://github.com/clownix/cloonix>
-   Лицензия: AGPLv3.
-   Моделирование на базе виртуальных машин и контейнеров [<a href="#citeproc_bib_item_22">22</a>].
-   Для виртуальных машин: kvm.
-   Для контейнеров: podman.
-   Host: только Linux.
-   Есть графический интерфейс.
-   Линки между узлами основаны на Open vSwitch.
-   Теоретически средство может поддерживать разное сетевой оборудование (например, Cisco).
-   Однако реально используется только Linux.
-   Сценарии использования:
    -   тестирование маршрутизации (BGP, OSPF);
    -   эмуляция IoT-сетей и мобильных устройств;
    -   антирегрессионное тестирование сетевых приложений.


### <span class="section-num">1.4</span> Специализированные средства моделирования {#специализированные-средства-моделирования}

-   Данные средства моделирования направлены на решение узких задач.
-   Это вовсе не означает, что нельзя будет проводить комплексное моделирование.
-   Но это будет явно сложнее, чем на универсальных системах.


#### <span class="section-num">1.4.1</span> Toxiproxy {#toxiproxy}

-   Репозиторий: <https://github.com/Shopify/toxiproxy>
-   Лицензия: MIT.
-   Позволяет изучить отказоустойчивость решений в сетевой среде.
-   Можно имитировать аномалии и сбои: задержки при получении ответа от сервера, изменение пропускной способность.
-   Можно запускать приложения в среде, где все соединения проходят проверку в различных сетевых условиях.
-   Состоит из двух элементов: TCP-прокси и клиента, взаимодействующего с ним по HTTP.
-   Скрипты  создаются с помощью Ruby, Node.js, Python.
-   Клиент подключается к демону Toxiproxy по HTTP.


## <span class="section-num">2</span> Сравнение {#сравнение}

-   Соберём средства натурного моделирования сетей в таблицу, выделив те параметры, которые важны нам для проведения воспроизводимых исследований.
-   Тип лицензии будет соответствовать сложности использования программного обеспечения.
-   Поскольку все рассматриваемые системы используют контейнеры и виртуальные машины (либо что-то одно из этого), то будем считать, что все они поддерживают управление технологическими изменениями.
-   Наличие командного интерфейса и скриптового языка будет способствовать устранению человеческой ошибки.

<a id="table--tab:comparison"></a>
<div class="table-caption">
  <span class="table-number"><a href="#table--tab:comparison">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1</a>:</span>
  Средства натурного моделирования сетей
</div>

| Программа    | Интерфейс | Скриптовый язык              | Лицензия     |
|--------------|-----------|------------------------------|--------------|
| GNS3         | GUI, Web  | Нет                          | GPL-3.0      |
| Eve-ng       | Web       | Нет                          | EULA         |
| PNetLab      | Web       | Нет                          | Не известно  |
| Containerlab | CLI       | YAML, Ansible                | BSD-3-Clause |
| Mininet      | CLI       | Python                       | BSD-3-Clause |
| Kathará      | CLI, GUI  | Python, YAML, shell          | GPL-3.0      |
| IMUNES       | CLI, GUI  | Python, YAML, shell          | CC-BY 4.0    |
| CORE         | CLI, GUI  | Python                       | BSD-2-Clause |
| Toxiproxy    | CLI       | Ruby, Node.js, Python        | MIT          |
| Cloonix      | CLI, GUI  | Python, shell                | AGPLv3       |
| netlab       | CLI       | YAML, Ansible, Python, shell | MIT          |


## <span class="section-num">3</span> Обсуждение {#обсуждение}

-   В первую очередь следует удалить из рассмотрения инструментарий с несвободными лицензиями: Eve-ng и PNetLab.
-   GNS3 не поддерживает возможность автоматизации с помощью кода.
-   Отсутствие интерфейса командной строки не позволяет проводить воспроизводимые исследования.
-   Впрочем, GNS3 хорошо подходит для обучения работы с сетями и принципам проведения натурного моделирования.
-   Остальные рассмотренные нами средства моделирования вполне подходят для реализации воспроизводимых исследований.
-   Для моделирования гетерогенных сетей, состоящий из оборудования разных производителей, остаётся рекомендовать containerlab и netlab.
-   Если необходимо моделировать не столько протоколы сами по себе, а особенности их реализации в оборудовании разных производителей, альтернативы просто нет.
-   Впрочем, ничего не мешает использовать эти средства и просто для моделирования произвольных сетей.
-   Kathará поддерживает распределённое выполнение, поэтому незаменима для ресурсоёмкого моделирования.
-   Кроме того, в рамках данного средства явно рассматривалась методика создания цифровых двойников сетевых систем.
-   Mininet развивается крайне неторопливо.
-   Но эта среда кране проста в применении.
-   Кроме того, это средство моделирования входит в образовательную программу многих вузов.
-   А исследователь, при прочих равных условиях, предпочтёт использовать то средство моделирования, с которым он знаком.
-   Toxiproxy предназначен для исследования вопросов сетевой безопасности.
-   В отличии от других средств моделирования мы не исследовали его глубоко.
-   Впрочем, моделирование сетевой безопасности тоже входит в круг наших интересов.
-   Средства моделирования IMUNES, CORE, Cloonix выглядят вполне достойными.
-   Но, победитель получает всё.
-   Эти средства моделирования не предлагают, на данный момент, никаких особенных преимуществ относительно выделенных нами систем.

-   Резюмируем наши рекомендации.
    -   Для первичного обучения студентов --- GNS3.
    -   Для моделирования простых систем и обучения натурному моделированию --- Mininet.
    -   Для моделирования сложных систем, ресурсоёмкого моделирования --- Kathará, containerlab, netlab.
    -   Для моделирования гетерогенных сетей, максимального соответствия реальным системам --- containerlab, netlab.


## <span class="section-num">4</span> Библиография {#библиография}

## Литература

<div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>1.	Welsh, C. GNS3 Network Simulation Guide / C. Welsh. – Packt Publishing, 2013. – 154 сс.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>2.	Velieva, T.R. Designing Installations for Verification of the Model of Active Queue Management Discipline RED in the GNS3 / T.R. Velieva, A.V. Korolkova, D.S. Kulyabov. – [Электронный ресурс] // 6th International Congress on Ultra Modern Telecommunications and Control Systems and Workshops (ICUMT). – IEEE Computer Society, 2015. – Сс. 570–577. – Режим доступа: <a href="http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=7002164">http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=7002164</a> (дата обращения: 27.07.2025).</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>3.	Lantz, B. <a href="https://doi.org/10.1145/1868447.1868466">A Network in a Laptop: Rapid Prototyping for Software-Defined Networks</a> / B. Lantz, B. Heller, N. McKeown // Proceedings of the 9th ACM SIGCOMM Workshop on Hot Topics in Networks : Hotnets-IX. – New York, NY, USA : Association for Computing Machinery, 2010. – A Network in a Laptop. – Сс. 1–6.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>4.	Lantz, B. <a href="https://doi.org/10.1145/2785956.2790030">A Mininet-based Virtual Testbed for Distributed SDN Development</a> / B. Lantz, B. O’Connor // Proceedings of the 2015 ACM Conference on Special Interest Group on Data Communication : SIGCOMM ’15. – ACM, 2015. – Сс. 365–366.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_5"></a>5.	Oliveira, R.L.S. de. <a href="https://doi.org/10.1109/colcomcon.2014.6860404">Using Mininet for emulation and prototyping Software-Defined Networks</a> / R.L.S. de Oliveira, C.M. Schweitzer, A.A. Shinoda, L.R. Prete // 2014 IEEE Colombian Conference on Communications and Computing (COLCOM). – IEEE, 2014. – Сс. 1–6.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_6"></a>6.	Ryll, A. Measuring TCP Tail Loss Probe Performance / A. Ryll. – [Электронный ресурс] // Proceedings of the Seminars Future Internet (FI), Innovative Internet Technologies and Mobile Communications (IITM) and Autonomous Communication Networks (ACN), Summer Semester 2013 : Network Architectures и Services (NET) / G. Carle и др. ред. . – Munich, Germany : Chair for Network Architectures; Services, Department of Computer Science, Technische Universität München, 2013. – Тт. NET-2013-08-1. – Сс. 1–7. – Режим доступа: <a href="https://www.net.in.tum.de/fileadmin/TUM/NET/NET-2014-03-1/NET-2014-03-1_01.pdf">https://www.net.in.tum.de/fileadmin/TUM/NET/NET-2014-03-1/NET-2014-03-1_01.pdf</a> (дата обращения: 27.07.2025).</div>
  <div class="csl-entry"><a id="citeproc_bib_item_7"></a>7.	Handigol, N. <a href="https://doi.org/10.1145/2413176.2413206">Reproducible network experiments using container-based emulation</a> / N. Handigol, B. Heller, V. Jeyakumar и др. // Proceedings of the 8th international conference on Emerging networking experiments and technologies : CoNEXT ’12. – ACM, 2012. – Сс. 253–264.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_8"></a>8.	Heller, B. Reproducible network research with high-fidelity emulation : PhD thesis / B. Heller. – Department of Computer Science; Stanford University, 2013. – 124 сс. – Режим доступа: <a href="https://purl.stanford.edu/zk853sv3422">https://purl.stanford.edu/zk853sv3422</a> (дата обращения: 27.07.2025). – [Электронный ресурс].</div>
  <div class="csl-entry"><a id="citeproc_bib_item_9"></a>9.	Yan, L. Learning Networking by Reproducing Research Results / L. Yan, N. McKeown // ACM SIGCOMM Computer Communication Review. – 2017. – Т. 47. – № 2. – Сс. 19–26. DOI: <a href="https://doi.org/10.1145/3089262.3089266">10.1145/3089262.3089266</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_10"></a>10.	Pizzonia, M. Netkit: network emulation for education / M. Pizzonia, M. Rimondini // Software: Practice and Experience. – 2014. – Т. 46. – Netkit. – № 2. – Сс. 133–165. DOI: <a href="https://doi.org/10.1002/spe.2273">10.1002/spe.2273</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_11"></a>11.	Ariyanto, Y. Teaching network security in Linux using Netkit with implementation virtual laboratory / Y. Ariyanto, B. Harijanto, Y.W. Syaifudin // IOP Conference Series: Materials Science and Engineering. – 2018. – Т. 434. – С. 012273. DOI: <a href="https://doi.org/10.1088/1757-899x/434/1/012273">10.1088/1757-899x/434/1/012273</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_12"></a>12.	Scazzariello, M. <a href="https://doi.org/10.1109/noms47738.2020.9110351">Kathará: A Lightweight Network Emulation System</a> / M. Scazzariello, L. Ariemma, T. Caiazzi // NOMS 2020 - 2020 IEEE/IFIP Network Operations and Management Symposium. – IEEE, 2020. – Kathará. – Сс. 1–2.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_13"></a>13.	Alberro, L. Experimentation Environments for Data Center Routing Protocols: A Comprehensive Review / L. Alberro, A. Castro, E. Grampin // Future Internet. – 2022. – Т. 14. – Experimentation Environments for Data Center Routing Protocols. – № 1. – Сс. 29.1–22. DOI: <a href="https://doi.org/10.3390/fi14010029">10.3390/fi14010029</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_14"></a>14.	Bonofiglio, G. <a href="https://doi.org/10.1109/noms.2018.8406267">Kathará: A container-based framework for implementing network function virtualization and software defined networks</a> / G. Bonofiglio, V. Iovinella, G. Lospoto, G. Di Battista // NOMS 2018 - 2018 IEEE/IFIP Network Operations and Management Symposium. – IEEE, 2018. – Kathará. – Сс. 1–9.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_15"></a>15.	Scazzariello, M. <a href="https://doi.org/10.1109/noms47738.2020.9110288">Megalos: A Scalable Architecture for the Virtualization of Network Scenarios</a> / M. Scazzariello, L. Ariemma, G.D. Battista, M. Patrignani // NOMS 2020 - 2020 IEEE/IFIP Network Operations and Management Symposium. – IEEE, 2020. – Megalos. – Сс. 1–7.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_16"></a>16.	Scazzariello, M. Megalos: A Scalable Architecture for the Virtualization of Large Network Scenarios / M. Scazzariello, L. Ariemma, G. Di Battista, M. Patrignani // Future Internet. – 2021. – Т. 13. – Megalos. – № 9. – Сс. 227.1–17. DOI: <a href="https://doi.org/10.3390/fi13090227">10.3390/fi13090227</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_17"></a>17.	Caiazzi, T. <a href="https://doi.org/10.1109/noms54207.2022.9789876">Sibyl: a Framework for Evaluating the Implementation of Routing Protocols in Fat-Trees</a> / T. Caiazzi, M. Scazzariello, L. Alberro и др. // NOMS 2022-2022 IEEE/IFIP Network Operations and Management Symposium. – IEEE, 2022. – Sibyl. – Сс. 1–7.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_18"></a>18.	Caiazzi, T. <a href="https://doi.org/10.1109/noms56928.2023.10154391">Nesting Containers for Faithful Datacenters Emulations</a> / T. Caiazzi, M. Scazzariello, S. Quinzi и др. // NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium. – IEEE, 2023. – Сс. 1–5.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_19"></a>19.	Zec, M. Implementing a Clonable Network Stack in the FreeBSD Kernel / M. Zec // Proceedings of the FREENIX Track: 2003 USENIX Annual Technical Conference. – San Antonio, Texas, USA, 2003.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_20"></a>20.	Salopek, D. <a href="https://doi.org/10.1109/softcom.2014.7039061">A network testbed for commercial telecommunications product testing</a> / D. Salopek, V. Vasic, M. Zec и др. // 2014 22nd International Conference on Software, Telecommunications and Computer Networks (SoftCOM). – IEEE, 2014. – Сс. 372–377.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_21"></a>21.	Ahrenholz, J. <a href="https://doi.org/10.1109/milcom.2008.4753614">CORE: A real-time network emulator</a> / J. Ahrenholz, C. Danilov, T.R. Henderson, J.H. Kim // MILCOM 2008 - 2008 IEEE Military Communications Conference. – IEEE, 2008. – CORE. – Сс. 1–7.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_22"></a>22.	Linkletter, B. <a href="https://netdevconf.org/2.1/papers/Brian-Linkletter-Netdev-paper.pdf">Investigating Linux Network Behaviour Using Open-Source Network Emulators</a> / B. Linkletter // Proceedings of Netdev 2.1. – 2016. – Сс. 1–8.</div>
</div>
