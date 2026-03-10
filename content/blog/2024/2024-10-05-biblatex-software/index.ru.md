---
title: "BibLaTeX. Ссылка на программный продукт"
author: ["Dmitry S. Kulyabov"]
date: 2024-10-05T18:49:00+03:00
lastmod: 2024-10-06T12:44:00+03:00
tags: ["bib", "tex"]
categories: ["computer-science"]
draft: false
slug: "biblatex-software"
---

BibLaTeX. Ссылка на программный продукт.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   В BibLaTeX есть стандартное поле `software`.
-   Однако в стандартных стилях оно не реализовано (вернее, просто является заглушкой).


## <span class="section-num">2</span> Пакет biblatex-software {#пакет-biblatex-software}

-   CTAN: <https://ctan.org/pkg/biblatex-software>
-   Репозиторий: <https://gitlab.inria.fr/gt-sw-citation/bibtex-sw-entry>
-   Добавляет поддержку четырёх типов записей программного обеспечения к любому другому стилю BibLaTeX.
-   Состоит из следующих компонентов:
    -   стиль ссылок (`software.bbx`);
    -   расширение модели данных (`software.dbx`);
    -   файлы локализации строк (`<lang>-software.lbx`).


### <span class="section-num">2.1</span> Типы записей {#типы-записей}

-   Четыре типа записей:
    -   `@software`;
    -   `@softwareversion`;
    -   `@softwaremodule`;
    -   `@codefragment`.


#### <span class="section-num">2.1.1</span> @software {#software}

-   Применение : программное обеспечение.
-   Обязательные поля : `author` / `editor`, `title`, `url`, `year`.
-   Дополнительные поля : `abstract`, `date`, `doi`, `eprint`, `eprintclass`, `eprinttype`, `file`, `hal_id`, `hal_version`, `institution`, `license`, `month`, `note`, `organization`, `publisher`, `related`, `relatedtype`, `relatedstring`, `repository`, `swhid`, `urldate`, `version`.


#### <span class="section-num">2.1.2</span> @softwareversion {#softwareversion}

-   Применение : конкретная версия программного обеспечения.
-   Наследует значения отсутствующих полей из записи, упомянутой в поле `crossref`.
-   Обязательные поля : `author` / `editor`, `title`, `url`, `version`, `year`.
-   Дополнительные поля : `abstract`, `crossref`, `date`, `doi`, `eprint`, `eprintclass`, `eprinttype`, `file`, `hal_id`, `hal_version`, `institution`, `introducedin`, `license`, `month`, `note`, `organization`, `publisher`, `related`, `relatedtype`, `relatedstring`, `repository`, `swhid`, `subtitle`, `urldate`.


#### <span class="section-num">2.1.3</span> @softwaremodule {#softwaremodule}

-   Применение : конкретный модуль более крупного программного проекта.
-   Наследует значения отсутствующих полей из записи, упомянутой в поле `crossref`.
-   Обязательные поля : `author`, `subtitle`, `url`, `year`.
-   Дополнительные поля : `abstract`, `crossref`, `date`, `doi`, `eprint`, `eprintclass`, `eprinttype`, `editor`, `file`, `hal_id`, `hal_version`, `institution`, `introducedin`, `license`, `month`, `note`, `organization`, `publisher`, `related`, `relatedtype`, `relatedstring`, `repository`, `swhid`, `title`, `urldate`, `version`.


#### <span class="section-num">2.1.4</span> @codefragment {#codefragment}

-   Применение : фрагмент кода (например, конкретный алгоритм в программе или библиотеке).
-   Наследует значения отсутствующих полей из записи, упомянутой в поле `crossref`.
-   Обязательные поля : `url`.
-   Дополнительные поля : `author`, `abstract`, `crossref`, `date`, `doi`, `eprint`, `eprintclass`, `eprinttype`, `file`, `hal_id`, `hal_version`, `institution`, `introducedin`, `license`, `month`, `note`, `organization`, `publisher`, `related`, `relatedtype`, `relatedstring`, `repository`, `swhid`, `subtitle`, `title`, `urldate`, `version`, `year`.


### <span class="section-num">2.2</span> Дополнительные поля {#дополнительные-поля}

-   Пакет вводит новые поля, специфичные для пакета:
    -   `hal_id` : цифровой идентификатор для запись программного обеспечения, включая его описание и метаданные в HAL;
    -   `hal_version` : версия записи программного обеспечения HAL;
    -   `license` : лицензия на право собственности в формате SPDX;
    -   `introducedin` : если это программный модуль или фрагмент, версия содержащего проекта, в которой он был впервые представлен;
    -   `repository` : URL-адрес репозитория кода (например, на GitHub, GitLab);
    -   `swhid` : идентификатор цифрового объекта (<https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html>):
        -   `swh-id` : внутренний идентификатор элемента;
        -   `swh:cnt` : для содержимого;
        -   `swh:dir` : для каталога;
        -   `swh:rev` : для ревизия;
        -   `swh:rel` : для выпуска.


### <span class="section-num">2.3</span> Использование {#использование}

-   Добавить модель данных к `biblatex`:
    ```latex
    \usepackage[datamodel=software]{biblatex}
    ```
-   Подключить стиль:
    ```latex
    \usepackage{software-biblatex}
    ```
-   Установите опции пакета:
    ```latex
    \ExecuteBibliographyOptions{
      halid=true,
      swhid=true,
      shortswhid=false,
      swlabels=true,
      vcs=true,
      license=true}
    ```
-   Опции пакета:
    -   `swlabels=true|false` : программное обеспечение --- это особый результат исследования, отличный от публикаций, поэтому записи о программном обеспечении в библиографии по умолчанию помечаются специальной меткой;
    -   `license=true|false` : информация о лицензии (по умолчанию `true`);
    -   `halid=true|false` : включением идентификатора в репозитории HAL (по умолчанию `true`);
    -   `swhid=true|false` : включением идентификатора в архиве Software Heritage (SWHID) (по умолчанию `true`);
    -   `shortswhid=true|false` : способ отображения SWHID; если `true`, в печатную версию будет включена только основная часть SWHID, а в гиперссылке будет сохранен полный SWHID со всей контекстной информацией (по умолчанию `false`);
    -   `vcs=true|false` : URL-адрес платформы размещения кода, на которой разрабатывается программное обеспечение, описанное в записи (по умолчанию `true`).


### <span class="section-num">2.4</span> Примеры {#примеры}


#### <span class="section-num">2.4.1</span> software, softwareversion {#software-softwareversion}

-   Пример описания выпуска программного обеспечения с использованием одной записи `@softwareversion`:
    ```bibtex
    @softwareversion {delebecque:hal-02090402-condensed,
      title = {Scilab},
      author = {Delebecque, Fran{\c c}ois and Gomez, Claude and Goursat, Maurice and Nikoukhah, Ramine and Steer, Serge and Chancelier, Jean-Philippe},
      url = {https://www.scilab.org/},
      date = {1994-01},
      file = {https://hal.inria.fr/hal-02090402/file/scilab-1.1.tar.gz},
      institution = {Inria},
      license = {Scilab license},
      hal_id = {hal-02090402},
      hal_version = {v1},
      swhid = {swh:1:dir:1ba0b67b5d0c8f10961d878d91ae9d6e499d746a;origin=https://hal.archives-ouvertes.fr/hal-02090402},
      version = {1.1},
      note = {First Scilab version. It was distributed by anonymous ftp.},
      repository= {https://github.com/scilab/scilab},
      abstract = {Software for Numerical Computation freely distributed.}
    }
    ```

-   Эту же информацию можно также представить с помощью пары `@software` и `@softwareversion`; общая информация в `@software`, изменения в `@softwareversion`:
    ```bibtex
    @software {delebecque:hal-02090402,
      title = {Scilab},
      author = {Delebecque, Fran{\c c}ois and Gomez, Claude and Goursat, Maurice and Nikoukhah, Ramine and Steer, Serge and Chancelier, Jean-Philippe},
      date = {1994},
      institution = {Inria},
      license = {Scilab license},
      hal_id = {hal-02090402},
      hal_version = {v1},
      url = {https://www.scilab.org/},
      abstract = {Software for Numerical Computation freely distributed.},
      repository= {https://github.com/scilab/scilab},
    }

    @softwareversion {delebecque:hal-02090402v1,
      version = {1.1},
      date = {1994-01},
      file = {https://hal.inria.fr/hal-02090402/file/scilab-1.1.tar.gz},
      swhid = {swh:1:dir:1ba0b67b5d0c8f10961d878d91ae9d6e499d746a;origin=https://hal.archives-ouvertes.fr/hal-02090402},
      note = {First Scilab version. It was distributed by anonymous ftp.},
      crossref = {delebecque:hal-02090402}
    }
    ```


#### <span class="section-num">2.4.2</span> softwaremodule {#softwaremodule}

-   Если программный продукт содержит много модулей, то может потребоваться ссылаться конкретно на конкретный модуль, который отличает авторов, и, возможно, он будет включен в проект позднее:
    ```bibtex
    @software {cgal,
     title = {The Computational Geometry Algorithms Library},
     author = {The CGAL Project},
     editor = {CGAL Editorial Board},
     date = {1996},
     url = {https://cgal.org/}
    }

    @softwareversion{cgal:5-0-2,
     crossref = {cgal},
     version = {5.0.2},
     url = {https://docs.cgal.org/5.02},
     date = {2020},
     swhid = {swh:1:rel:636541bbf6c77863908eae744610a3d91fa58855;
              origin=https://github.com/CGAL/cgal/}
    }

    @softwaremodule{cgal:lp-gi-20a,
     crossref = {cgal:5-0-2},
     author = {Menelaos Karavelas},
     subtitle = {{2D} Voronoi Diagram Adaptor},
     license = {GPL},
     introducedin = {cgal:3-1},
     url = {https://doc.cgal.org/5.0.2/Manual/packages.html#PkgVoronoiDiagram2},
    }
    ```
-   Можно использовать только одну запись, чтобы получить эквивалентный результат:
    ```bibtex
    @softwaremodule{cgal:lp-gi-20a-condensed,
     title = {The Computational Geometry Algorithms Library},
     subtitle = {{2D} Voronoi Diagram Adaptor},
     author = {Menelaos Karavelas},
     editor = {CGAL Editorial Board},
     license = {GPL},
     version = {5.0.2},
     introducedin = {cgal:3-1},
     date = {2020},
     swhid = {swh:1:rel:636541bbf6c77863908eae744610a3d91fa58855;
              origin=https://github.com/CGAL/cgal/},
     url = {https://doc.cgal.org/5.0.2/Manual/packages.html#PkgVoronoiDiagram2},
    }
    ```


#### <span class="section-num">2.4.3</span> codefragment {#codefragment}

-   Если необходимо, чтобы определённый фрагмент кода появился в библиографии:
    ```bibtex
    @software {parmap,
      title = {The Parmap library},
      author = {Di Cosmo, Roberto and Marco Danelutto},
      date = {2012},
      institution = {{Inria} and {University of Paris} and {University of Pisa}},
      license = {LGPL-2.0},
      url = {https://rdicosmo.github.io/parmap/},
      repository= {https://github.com/rdicosmo/parmap},
    }

    @softwareversion {parmap-1.1.1,
      crossref = {parmap},
      date = {2020},
      version = {1.1.1},
      swhid = {swh:1:rel:373e2604d96de4ab1d505190b654c5c4045db773;
         origin=https://github.com/rdicosmo/parmap;
         visit=swh:1:snp:2a6c348c53eb77d458f24c9cbcecaf92e3c45615},
    }

    @codefragment {simplemapper,
      subtitle = {Core mapping routine},
      swhid = {swh:1:cnt:43a6b232768017b03da934ba22d9cc3f2726a6c5;
         origin=https://github.com/rdicosmo/parmap;
         visit=swh:1:snp:2a6c348c53eb77d458f24c9cbcecaf92e3c45615;
         anchor=swh:1:rel:373e2604d96de4ab1d505190b654c5c4045db773;
         path=/src/parmap.ml;
         lines=192-228},
      crossref = {parmap-1.1.1}
    }
    ```
-   Можно использовать только одну запись:
    ```bibtex
    @codefragment {simplemapper-condensed,
      title = {The Parmap library},
      author = {Di Cosmo, Roberto and Marco Danelutto},
      date = {2020},
      institution = {{Inria} and {University of Paris} and {University of Pisa}},
      license = {LGPL-2.0},
      url = {https://rdicosmo.github.io/parmap/},
      repository= {https://github.com/rdicosmo/parmap},
      version = {1.1.1},
      subtitle = {Core mapping routine},
      swhid = {swh:1:cnt:43a6b232768017b03da934ba22d9cc3f2726a6c5;
         origin=https://github.com/rdicosmo/parmap;
         visit=swh:1:snp:2a6c348c53eb77d458f24c9cbcecaf92e3c45615;
         anchor=swh:1:rel:373e2604d96de4ab1d505190b654c5c4045db773;
         path=/src/parmap.ml;
         lines=192-228}
    }
    ```
