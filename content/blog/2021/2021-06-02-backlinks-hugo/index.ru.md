---
title: "Обратные ссылки в Hugo"
author: ["Dmitry S. Kulyabov"]
date: 2021-06-02T17:19:00+03:00
lastmod: 2023-09-28T16:30:00+03:00
tags: ["hugo", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "backlinks-hugo"
---

Можно создавать обратные ссылки и в самом Hugo.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Источники обратных ссылок {#источники-обратных-ссылок}

-   У меня обратные ссылки получаются из заметок в Org-roam, которые я стараюсь вести по методике Zettelkasten (см. [Метод Zettelkasten]({{< relref "2021-02-18-zettelkasten-method" >}})).


## <span class="section-num">2</span> Создание обратных ссылок из emacs {#создание-обратных-ссылок-из-emacs}

-   Обратные ссылки можно создавать напрямую при экспорте из _emacs_.
-   Для экспорта обратных ссылок я использовал следующий скрипт на _elisp_:
    ```emacs-lisp
    ;;; -*- mode: emacs-lisp; lexical-binding: t; coding: utf-8-unix; -*-
    ;;; Export Backlinks

    (defun ecf/org-roam--backlinks-list (file)
      (with-temp-buffer
        (if-let* ((backlinks (org-roam--get-backlinks file))
                  (grouped-backlinks (--group-by (nth 0 it) backlinks)))
            (progn
              (dolist (group grouped-backlinks)
                (let ((file-from (car group))
                      (bls (cdr group)))
                  (insert (format "- [[file:%s][%s]]\n"
                                  file-from
                                  (org-roam-db--get-title file-from)))
                  (dolist (backlink bls)
                    (pcase-let ((`(,file-from _ ,props) backlink))
                      (s-trim (s-replace "\n" " " (prin1-to-string (plist-get props :content))))
                      (insert "\n\n")))))))
        (buffer-string)))

    (defun ecf/org-export-preprocessor (backend)
      (let (
            (links (ecf/org-roam--backlinks-list (buffer-file-name))))
        (unless (string= links "")
          (save-excursion
            (goto-char (point-max))
            (insert (concat "\n* Backlinks\n") links)))))

    ;;; Export backlinks only for ox-hugo
    (defun ecf/org-export-preprocessor-hugo (backend)
      (when (org-export-derived-backend-p backend 'hugo)
        (ecf/org-export-preprocessor 'hugo)))

    (add-hook 'org-export-before-processing-hook 'ecf/org-export-preprocessor-hugo)
    ```
-   Недостатки:
    -   Использовался вызов внутреннего API org-roam. При этом он постоянно менялся.
    -   Расположение обратных ссылок жёстко кодируется.
    -   Обратные ссылки получались статичными: при изменении связей необходимо повторно экспортировать все связанные ноды.


## <span class="section-num">3</span> Создание обратных ссылок с помощью генератора Hugo {#создание-обратных-ссылок-с-помощью-генератора-hugo}

-   Но, возможно, оптимальнее создавать их с помощью самого Hugo.


### <span class="section-num">3.1</span> Общая информация {#общая-информация}

-   Примеры создания обратных ссылок в Hugo:
    -   <https://gabrielleearnshaw.medium.com/implementing-backlinks-in-a-hugo-website-e548d3d8f0e0>
    -   <https://seds.nl/notes/export_org_roam_backlinks_with_gohugo/>
-   Есть тема для Hugo, основным свойством которой является поддержка обратных ссылок:
    -   <https://github.com/kausalflow/connectome>
-   Для создания обратных ссылок необходимо поправить шаблон.
-   Саму генерацию обратных ссылок будем выполнять с помощью механизма _частичных шаблонов_:
    -   <https://gohugo.io/templates/partials/>.
-   Шаблон страницы будем делать на основе шаблона _single page_:
    -   <https://gohugo.io/templates/single-page-templates>.


### <span class="section-num">3.2</span> Каталоги для новой структуры {#каталоги-для-новой-структуры}

-   Добавим каталог `layouts` в корень нашего сайта для создания собственных шаблонов:
    ```shell
    layouts
    ├── _default
    │   └── single.html
    └── partials
        └── backlinks.html
    ```


### <span class="section-num">3.3</span> Шаблон генерации обратных ссылок {#шаблон-генерации-обратных-ссылок}

-   Зададим частичный шаблон `layouts/partials/backlinks.html`, создающий список обратных ссылок и отображающий его:
    ```html
    {{ $re := $.File.BaseFileName }}
    {{ $backlinks := slice }}
    {{ range .Site.AllPages }}
       {{ if and (findRE $re .RawContent) (not (eq $re .File.BaseFileName)) }}
          {{ $backlinks = $backlinks | append . }}
       {{ end }}
    {{ end }}

    <hr>
    {{ if gt (len $backlinks) 0 }}
      <div class="bl-section">
        <h4>Links to this note</h4>
        <div class="backlinks">
          <ul>
           {{ range $backlinks }}
              <li><a href="{{ .RelPermalink }}">{{ .Title }}</a></li>
           {{ end }}
         </ul>
        </div>
      </div>
    {{ else  }}
      <div class="bl-section">
        <h4>No notes link to this note</h4>
      </div>
    {{ end }}
    ```


### <span class="section-num">3.4</span> Шаблон страницы {#шаблон-страницы}

-   Шаблон страницы лучше делать на основе используемой темы.
-   Я использую шаблон _Academic_ (`https://github.com/wowchemy/starter-hugo-academic`), основанную на модуле _wowchemy_ (`https://github.com/wowchemy/wowchemy-hugo-modules.git`).
    -   Скачиваю модуль:
        ```shell
        git clone https://github.com/wowchemy/wowchemy-hugo-modules.git
        ```
    -   Копирую файл `wowchemy-hugo-modules/wowchemy/layouts/_default/single.html` в локальный каталог. Он имеет следующий вид (зависит от темы):
        ```html
        {{- define "main" -}}

        <article class="article">

          {{ partial "page_header" . }}

          <div class="article-container">

            <div class="article-style">
              {{ .Content }}
            </div>

            {{ partial "page_footer" . }}

          </div>
        </article>

        {{- end -}}
        ```
    -   Добавляю использование частичного шаблона обратных ссылок:
        ```diff
        --- orig/single.html	2021-06-02 18:12:17.337530907 +0300
        +++ single.html	2021-06-02 16:15:08.178764024 +0300
        @@ -8,6 +8,7 @@

             <div class="article-style">
               {{ .Content }}
        ​+      {{ partial "backlinks" . }}
             </div>

             {{ partial "page_footer" . }}
        ```
    -   Получаю следующий файл `layouts/_default/single.html`:
        ```html
        {{- define "main" -}}

        <article class="article">

          {{ partial "page_header" . }}

          <div class="article-container">

            <div class="article-style">
              {{ .Content }}
              {{ partial "backlinks" . }}
            </div>

            {{ partial "page_footer" . }}

          </div>
        </article>

        {{- end -}}
        ```


## <span class="section-num">4</span> Исправление обратных ссылок {#исправление-обратных-ссылок}

-   При экспорте _ox-hugo_ экспортирует ссылки как указатели на имя файла.
-   Имя файла в каталоге _org-roam_ может отличаться от имени, которое имеет файл в каталоге для сайта.
-   Имя для сайта задаётся полем `#+EXPORT_FILE_NAME:`.
-   Предлагается после экспорта заменять ссылки на файлы на внутренние ссылки Hugo типа `{{</* relref имя_файла */>}}` (см. [Синтаксис Markdown для генератора сайтов Hugo]({{< relref "2020-11-26-hugo-markdown" >}})).
-   Имя файла предполагается брать из поля `#+EXPORT_FILE_NAME:`.
-   Для этого был написан скрипт:
    ```python
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    # org-roam-links

    import sys
    import re
    import os

    orgroamdir = "~/work/org/notes/"

    def find_md_links(md):
        """Returns dict of links in markdown:
        'regular': [foo](some.url)
        'footnotes': [foo][3]

        [3]: some.url
        """
        # https://stackoverflow.com/a/30738268/2755116

        INLINE_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        FOOTNOTE_LINK_TEXT_RE = re.compile(r'\[([^\]]+)\]\[(\d+)\]')
        FOOTNOTE_LINK_URL_RE = re.compile(r'\[(\d+)\]:\s+(\S+)')

        links = list(INLINE_LINK_RE.findall(md))
        footnote_links = dict(FOOTNOTE_LINK_TEXT_RE.findall(md))
        footnote_urls = dict(FOOTNOTE_LINK_URL_RE.findall(md))

        footnotes_linking = []

        for key in footnote_links.keys():
            footnotes_linking.append((footnote_links[key], footnote_urls[footnote_links[key]]))

        return {'regular': links, 'footnotes': footnotes_linking}


    def replace_md_links(md, f):
        """Replace links url to f(url)"""

        links = find_md_links(md)
        newmd = md

        for r in links['regular']:
            newmd = newmd.replace(r[1], f(r[1]))

        for r in links['footnotes']:
            newmd = newmd.replace(r[1], f(r[1]))

        return newmd

    if __name__ == "__main__":
        filename = sys.argv[1]
        print(filename)
        fin = open(filename, "rt")
        filetext = fin.read()

        export_file_name_re = re.compile(r'#\+EXPORT_FILE_NAME:\s+\S+', re.IGNORECASE)
        relref_re = re.compile(r"{{</* relref \"(.+)\" */>}}")


        links = find_md_links(filetext)
        for mdlink in links['regular']:
            fulllink = mdlink[1]
            isrelref = relref_re.match(fulllink)
            if isrelref:
                linkpath = isrelref.group(1)
            else:
                # drop extention
                linkpath = os.path.splitext(fulllink)[0]
            # add extention
            md2org = linkpath + '.org'
            orgfile = os.path.expanduser(orgroamdir + md2org)
            if os.path.exists(orgfile):
                orgfiletext =  open(orgfile).read()
                export_file_name_text = export_file_name_re.findall(orgfiletext)
                export_file_name_link = export_file_name_text[0].split()
                hugolink = "{{</* relref \"" + export_file_name_link[1] + "\" */>}}"
                if isrelref:
                    filetext = filetext.replace("{{</* relref \"" + linkpath + "\" */>}}",hugolink)
                else:
                    filetext = filetext.replace(linkpath + '.md',hugolink)

        fin.close()
        fin = open(filename, "wt")
        fin.write(filetext)
        fin.close()
    ```
-   Запуск скрипта осуществляется через `Makefile`:
    ```makefile
    all:

    fixlinks:
            find . -name "*.md" -newer .fixlinks -exec ./org-roam-links '{}' \;
            touch .fixlinks

    clean:
            find . -name "*~" -delete
    ```
-   Запуск осуществляется следующим образом:
    ```shell
    make fixlinks clean
    ```
-   Скрипты помещаются в каталог `content/`.
