---
title: "Update your Bitbucket Cloud SSH Host Keys"
author: ["Dmitry S. Kulyabov"]
date: 2023-06-14T17:45:00+03:00
lastmod: 2023-06-14T17:54:00+03:00
tags: ["sysadmin"]
categories: ["computer-science"]
draft: false
slug: "update-bitbucket-ssh-host-keys"
---

Update your Bitbucket Cloud SSH Host Keys.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Information {#information}

-   Encrypted copies of Bitbucket’s SSH host keys were included in a data breach of a third-party credential management vendor.
-   Bitbucket issued two new SSH host keys and will be replacing the current host keys on June 20, 2023.


## <span class="section-num">2</span> Identify if your client is impacted {#identify-if-your-client-is-impacted}

-   To verify which host key your SSH client is using, you can run the following command:
    ```shell
    $ ssh git@bitbucket.org host_key_info
    You are using host key with fingerprint:
    ssh-ed25519 SHA256:ybgmFkzwOSotHTHLJgHO0QN8L0xErw6vd0VhFA9m3SM

    See https://bitbucket.org/blog/ssh-host-key-changes for more details.
    ```
-   Do you see either the new ECDSA or Ed25519 host key fingerprint in the output?
-   Your SSH client has switched to the new host keys automatically and no further action is required for this client.


## <span class="section-num">3</span> Otherwise, configure your client to trust the new host keys {#otherwise-configure-your-client-to-trust-the-new-host-keys}

-   If neither new fingerprints appear in the output of your OpenSSH client, you can configure the new trusted host keys in the known_hosts file with these commands:
    ```shell
    ssh-keygen -R bitbucket.org && curl https://bitbucket.org/site/ssh >> ~/.ssh/known_hosts
    ```
