---
title: "Package manager for Windows. Chocolatey"
author: ["Dmitry S. Kulyabov"]
date: 2021-01-18T11:23:00+03:00
lastmod: 2025-08-27T18:08:00+03:00
tags: ["windows", "sysadmin", "education"]
categories: ["computer-science"]
draft: false
slug: "package-manager-windows-chocolatey"
---

The most popular package manager for Windows is _Chocolatey_.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Resources {#resources}

-   Homepage: <https://chocolatey.org/>
-   Repository: <https://github.com/chocolatey/choco>


## <span class="section-num">2</span> Installing Chocolatey {#installing-chocolatey}

-   The installation procedure is described on the page <https://chocolatey.org/install>.
-   Installation is performed in PowerShell.
-   PowerShell must be run with administrator rights.
-   The easiest way to launch it is with the key combination `Win+X`.
-   The installation command is located on the page <https://chocolatey.org/install>.

{{< youtube _1O4vKHhm3I >}}


## <span class="section-num">3</span> Additional settings {#additional-settings}

-   To install without asking for confirmation, you can configure the following:

<!--listend-->

```shell
choco feature enable -n=allowGlobalConfirmation
```

-   You can re-enable the confirmation request with the command:

<!--listend-->

```shell
choco feature disable -n=allowGlobalConfirmation
```


## <span class="section-num">4</span> Packages {#packages}

-   The list of packages is on the page <https://chocolatey.org/packages>.
-   List of packages:

<!--listend-->

```shell
choco list
```


## <span class="section-num">5</span> Working with software {#working-with-software}


### <span class="section-num">5.1</span> Service functions {#service-functions}

-   Information on command line switches:

<!--listend-->

```shell
choco --help
```

-   List of packages in the repository:

<!--listend-->

```shell
choco list
```

-   List of installed packages:

<!--listend-->

```shell
choco list --local-only
```


### <span class="section-num">5.2</span> Installing a package {#installing-a-package}

-   To install a package, run the command:

<!--listend-->

```shell
choco install package_name
```

-   To install without asking for confirmation, add the `y` switch:

<!--listend-->

```shell
choco install package_name -y
```


### <span class="section-num">5.3</span> Removing a package {#removing-a-package}

-   To remove a package, run the command:

<!--listend-->

```shell
choco uninstall package_name
```


### <span class="section-num">5.4</span> Updating packages {#updating-packages}

-   To update a package, run the command:

<!--listend-->

```shell
choco upgrade package_name
```

-   To update all installed packages, run the command:

<!--listend-->

```shell
choco upgrade all -y
```


### <span class="section-num">5.5</span> Updating packages automatically {#updating-packages-automatically}

-   To update packages automatically, use the `choco-upgrade-all-at` package:

<!--listend-->

```shell
choco install choco-upgrade-all-at
```

-   You can update using the command:

<!--listend-->

```shell
choco-upgrade-all
```

-   To set the update time, you need to install with certain parameters:
-   if you do not specify any parameters, `choco-upgrade-all-at` will run by default every day at 2 am and stop at 4 am;
-   run `choco upgrade all -y` daily (by default) at 23:00 and abort at 1:00 (by default `ABORTTIME` is +2 hours):

<!--listend-->

```shell
choco install choco-upgrade-all-at --params "'/TIME:23:00'"
```

-   run `choco upgrade all -y` daily at 4:00 and abort at 8:00:

<!--listend-->

```shell
choco install choco-upgrade-all-at --params "'/DAILY:yes /TIME:04:00 /ABORTTIME:08:00'"
```

-   run `choco upgrade all -y` every Sunday at 1:00 and abort at 3:00:

<!--listend-->

```shell
choco install choco-upgrade-all-at --params "'/WEEKLY:yes /DAY:SUN /TIME:01:00'"
```

-   You can edit the parameters by running the command:

<!--listend-->

```shell
choco-upgrade-all -EditConfig
```
