---
title: "LaTeX. Пакет pdfx"
author: ["Dmitry S. Kulyabov"]
date: 2021-07-30T11:25:00+03:00
lastmod: 2023-07-14T17:41:00+03:00
tags: ["tex"]
categories: ["computer-science"]
draft: false
slug: "latex-packages-pdfx"
---

Пакет для создание документов pdf, соответствующих стандартам PDF/A и PDF/X.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Проблемы {#проблемы}


### <span class="section-num">1.1</span> 2021-07 Совместимость с LaTeX2e, версия от 2021-06-01 {#2021-07-совместимость-с-latex2e-версия-от-2021-06-01}

-   После закрытия ошибки 605 (см. <https://github.com/latex3/latex2e/issues/605>) пакет _pdfx_ перестал работать.
-   В качестве временного решения предложено при компиляции откатиться на состояние до закрытия ошибки 605.
-   Предложенный код (см. <https://tex.stackexchange.com/questions/605854/error-using-pdfx-on-tex-live-2021>):
    ```latex
    \ProvidesPackage{fixpdfx}[2021-07-22 A package that fixes pdfx errors on TeX Live 2021 in a quick and dirty way]

    % temporarily reverts https://github.com/latex3/latex2e/commit/5fb2860f2fedc87b213730f06ec1d77bcab4814a
    % resp. https://github.com/latex3/latex2e/commit/dd2ec509ec98e9c359a41e35aea6aade86485ca2
    % as it breaks pdfx (see https://tex.stackexchange.com/questions/605854/error-using-pdfx-on-tex-live-2021)

    \@ifpackageloaded{pdfx}{
        \PackageError{fixpdfx}{pdfx is loaded}{This package must be loaded before pdfx}
    }{}

    \ExplSyntaxOn

    % this is the old implementation from base/ltpara.dtx, version 1.0g
    \cs_new_protected:Npn \__old_para_end: {
      % ltpara v1.0h as well as firstaid/latex2e-first-aid-for-external-files.dtx v1.0o inserted
      % \scan_stop: here, which breaks pdfx
      \mode_if_horizontal:TF {
        \mode_if_inner:F {
             \tex_unskip:D
             \hook_use:n{para/end}
             \@kernel@after@para@end
             \mode_if_horizontal:TF {
               \if_int_compare:w 0 < \tex_lastnodetype:D
                 \tex_kern:D \c_zero_dim
               \fi:
               \tex_par:D
               \hook_use:n{para/after}
               \@kernel@after@para@after
             }
             { \msg_error:nnnn { hooks }{ para-mode }{end}{horizontal} }
        }
      }
      \tex_par:D
    }

    \PackageWarning{fixpdfx}{Patching~\para_end:~implementation~to~fix~pdfx}
    \cs_set_eq:NN \par     \__old_para_end:
    % these two aren't actually required to fix pdfx, so we'll skip them...
    %\cs_set_eq:NN \@@par   \__old_para_end:
    %\cs_set_eq:NN \endgraf \__old_para_end:

    \AtBeginDocument{
        \@ifpackageloaded{pdfx}{}{
            \PackageError{fixpdfx}{pdfx~is~not~loaded}{You~did~not~load~pdfx~and~thus~do~not~need~this~package}
        }
        % pdfx v1.6.3 from 2019-02-27 is bad, so anything later is hopefully fixed...
        \@ifpackagelater{pdfx}{2019/02/28}{
            \PackageError{fixpdfx}{Please~check~whether~you~really~need~this~package.}{Your~pdfx~package~is~more~recent~than~2019-02-27~and~thus~might~not~require~this~package's~fix.}
        }{}

        \PackageWarning{fixpdf}{Restoring~old~\para_end:~implementation}

        % restore additional definitions
        \cs_set_eq:NN \par     \para_end:
        % see above: as we didn't replace them, no need to restore them.
        %\cs_set_eq:NN \@@par   \para_end:
        %\cs_set_eq:NN \endgraf \para_end:
    }

    \ExplSyntaxOff
    ```
