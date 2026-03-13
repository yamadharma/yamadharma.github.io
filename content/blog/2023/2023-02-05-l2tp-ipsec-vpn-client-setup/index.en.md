---
title: "L2TP over IPsec VPN client setup"
author: ["Dmitry S. Kulyabov"]
date: 2023-02-05T13:35:00+03:00
lastmod: 2023-02-17T20:23:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "l2tp-ipsec-vpn-client-setup"
---

L2TP/IPsec VPN client setup

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Linux {#linux}


### <span class="section-num">1.1</span> Gentoo {#gentoo}


#### <span class="section-num">1.1.1</span> NetworkManager {#networkmanager}

-   Open the NetworkManager UI, then:
    -   Go to Network &gt; VPN. Click _+_.
    -   Select _Layer 2 Tunneling Protocol (L2TP)_.
    -   You can choose a name for the VPN.
    -   Enter Your VPN Server IP for the Gateway.
    -   Enter Your VPN Username for the User name.
    -   Right-click the _?_ in the Password field, select Store the password only for this user.
        -   You might want to use _Store password for all users_.
    -   Enter Your VPN Password for the Password.
    -   Leave the NT Domain field blank.
    -   Click the _IPsec Settings..._ button.
    -   Check the Enable IPsec tunnel to L2TP host checkbox.
    -   Leave the Gateway ID field blank.
    -   Enter Your VPN IPsec PSK for the Pre-shared key.
    -   Then click _Add_ to save the VPN connection information.


#### <span class="section-num">1.1.2</span> Strongswan interactions {#strongswan-interactions}

-   By default, strongswan is built with capabilities support and the ability to run as an unprivileged user.
-   However, capabilities are not configured in NetworkManager.
-   As a result, the connection is not established.
-   You can solve the problem as follows:
    -   either install strongswan without capabilities support and the ability to run as an unprivileged user:
        ```shell
        USE="-caps -non-root" emerge strongswan
        ```
    -   either build NetworkManager with capabilities support (see <https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/merge_requests/1053>).
