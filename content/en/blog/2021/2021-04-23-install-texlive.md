---
title: "Installing TeXlive"
author: ["Dmitry S. Kulyabov"]
date: 2021-04-23T18:09:00+03:00
lastmod: 2025-08-27T18:04:00+03:00
tags: ["latex", "tex"]
categories: ["computer-science"]
draft: false
slug: "install-texlive"
---

Installing the distribution _TeXlive_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> General information {#general-information}

-   TeX Live --- the most complete LaTeX distribution supported by the TeX community.
-   Supports a large number of operating systems.
-   Developed since 1996.
-   Based on the teTeX distribution.
-   MacTeX --- a variant for MacOS.
-   Main page: <https://www.tug.org/texlive/>.
-   TeX Live --- is a distribution with continuous updates as part of the annual version of the distribution.


## <span class="section-num">2</span> Installation from distribution packages {#installation-from-distribution-packages}

-   Ubuntu:

<!--listend-->

```shell
apt install texlive-full
```


## <span class="section-num">3</span> Network installation on one computer {#network-installation-on-one-computer}


### <span class="section-num">3.1</span> Installation using distribution scripts {#installation-using-distribution-scripts}

-   Links on the site are to mirrors. The mirror is selected automatically.
-   Download the installer:
-   Unix: <https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz>

<!--listend-->

```shell
cd /tmp/
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
```

-   Windows: <https://mirror.ctan.org/systems/texlive/tlnet/install-tl-windows.exe>
-   For Windows: run the executable file and install.
-   For Linux
-   Unpack the downloaded file:

<!--listend-->

```shell
tar xzvf install-tl-unx.tar.gz
```

-   Go to the unpacked directory and run the installer:

<!--listend-->

```shell
cd install-tl-[0-9]*
sudo ./install-tl
```

-   It is recommended to create links to executable files in the `/usr/local/bin` directory. To do this, in the console version of the utility, select the `O` option, and then `L`. To return to the previous menu, use `R`.


### <span class="section-num">3.2</span> Installing with a package manager {#installing-with-a-package-manager}

-   Windows. Use the Chocolatey package manager (see [Package manager for Windows. Chocolatey]({{< relref "2021-01-18-package-manager-windows-chocolatey" >}})).

<!--listend-->

```shell
choco install texlive
```


## <span class="section-num">4</span> Network installation on multiple computers {#network-installation-on-multiple-computers}


### <span class="section-num">4.1</span> File server {#file-server}

-   A copy of the TeX Live archive is stored on the file server.
-   We store it in the directory `/com/lib/portage/extras/texlive` (of course, you can choose any).
-   We share this directory via NFS (for example).
-   Let's make a script for daily download:

<!--listend-->

```shell
#!/bin/bash
# /etc/cron.daily/texlive-rsync-tree

RSYNC_MIRROR=rsync://mirrors.mi.ras.ru/CTAN/

mkdir -p /com/lib/portage/extras/texlive
rsync -rltpD -v -HS --delete ${RSYNC_MIRROR}/systems/texlive/tlnet/ /com/lib/portage/extras/texlive
```


### <span class="section-num">4.2</span> Clients {#clients}


#### <span class="section-num">4.2.1</span> Installation {#installation}

-   First, install manually on clients. To do this, run on the client:

<!--listend-->

```shell
/com/lib/portage/extras/texlive/install-tl --repository=/com/lib/portage/extras/texlive
```


### <span class="section-num">4.3</span> Update {#update}

-   To update, use the script on the client:

<!--listend-->

```shell
#!/bin/bash

if [[ -d /com/lib/portage/extras/texlive ]]
then
tlmgr update --repository=/com/lib/portage/extras/texlive --self
tlmgr update --repository=/com/lib/portage/extras/texlive --all
else
tlmgr update --self
tlmgr update --all
fi
tlmgr path add
```
<div class="src-block-caption">
  <span class="src-block-number">Code Snippet 1:</span>
  /etc/cron.weekly/texlive-update
</div>


## <span class="section-num">5</span> Updating to the next version of TeXlive {#updating-to-the-next-version-of-texlive}

-   It is recommended to install the new version of TeXlive separately.
-   But you can do a manual update using an existing installation.
-   Let's assume that our architecture is `x86_64-linux`.
-   If you have installed symbolic links to system directories (via installer option or `tlmgr path add`), remove them:

<!--listend-->

```shell
tlmgr path remove
```

-   Move the entire TeXlive directory to match the new version, for example:

<!--listend-->

```shell
mv /usr/local/texlive/2024/ /usr/local/texlive/2025
```

-   Remove package backups:

<!--listend-->

```shell
rm /usr/local/texlive/2025/tlpkg/backups/*
```

-   Create links to executables:

<!--listend-->

```shell
/usr/local/texlive/2025/bin/x86_64-linux/tlmgr path add
```

-   Download the latest version of the script `update-tlmgr-latest.sh`:

<!--listend-->

```shell
wget https://mirror.ctan.org/systems/texlive/tlnet/update-tlmgr-latest.sh -O /tmp/update-tlmgr-latest.sh
```

-   Run the script:

<!--listend-->

```shell
sh /tmp/update-tlmgr-latest.sh -- upgrade
```

-   If you do not want to use the default repository for downloading new files, then replace it:

<!--listend-->

```shell
tlmgr option repository <reponame>
```

-   Update the TeXlive package manager:

<!--listend-->

```shell
tlmgr update --self
```

-   Update TeXlive packages:

<!--listend-->

```shell
tlmgr update --all
```

-   Set symbolic links to executables in system directories (`/usr/local/bin`):

<!--listend-->

```shell
tlmgr path add
```

-   You can recreate the cache _lualatex_ under the user:

<!--listend-->

```shell
mv ~/.texlive2024 ~/.texlive2025
luaotfload-tool -fu
```

-   If you don't do this, the cache will be recreated on the first run of `lualatex`.
