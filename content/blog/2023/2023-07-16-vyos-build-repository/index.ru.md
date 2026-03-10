---
title: "Сборка образа VyOS. Репозиторий"
author: ["Dmitry S. Kulyabov"]
date: 2023-07-16T19:13:00+03:00
lastmod: 2023-10-06T19:05:00+03:00
tags: ["sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "vyos-build-repository"
---

Репозиторий с поддержкой сборки образов VyOS.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Репозиторий предназначен для хранения образов VyOS, собранных для обучения.
-   Образы собираются по стандартной методике (см. [GNS3. Образ VyOS]({{< relref "2022-07-14-gns3-vyos" >}})).
-   Сборка организуется по технологии непрерывной интеграции (см. [Непрерывная интеграция. GitHub Actions]({{< relref "2023-07-16-continuous-integration-github-actions" >}})).


## <span class="section-num">2</span> Репозиторий {#репозиторий}

-   Репозиторий: <https://github.com/yamadharma/vyos-build>


## <span class="section-num">3</span> Скрипт для сборки {#скрипт-для-сборки}

-   Помещается в каталог `.github/workflows` репозиторий.
-   Назовём его `vyos-build-release.yml`
    ```yaml { linenos=true, linenostart=1, anchorlinenos=true, lineanchors=org-coderef--59b1f4 }
    name: VyOS Build (Release)

    on:
      push:
        tags:
    ​      - "*"

    jobs:
      build:

        runs-on: ubuntu-latest
        container:
          # For VyOS 1.2 (crux) use vyos/vyos-build:crux
          # For VyOS 1.3 (equuleus) use vyos/vyos-build:equuleus
          # For our VyOS rolling release you should use vyos/vyos-build which will always refer to the latest image.
          # Ref: https://docs.vyos.io/en/latest/contributing/build-vyos.html#build
          image: vyos/vyos-build:equuleus
          env:
            TZ: Etc/UTC
          options: --privileged


        steps:
    ​    - name: Set env
          run: |
            echo "RELEASE_VERSION=${GITHUB_REF:11}" >> $GITHUB_ENV

        - name: git clone vyos-build
          run: |
            set -eux

            git clone -b equuleus --single-branch https://github.com/vyos/vyos-build

        - name: configure
          working-directory: vyos-build
          run: |
            set -eux

            ./configure \
              --architecture amd64 \
              --build-by yamadharma@gmail.com \
              --build-type release \
              --version ${{ env.RELEASE_VERSION }}

        - name: make iso
          working-directory: vyos-build
          run: |
            set -eux

            make iso

        - name: make qemu
          working-directory: vyos-build
          run: |
            set -eux

            make qemu

        - name: ls
          run: |
            set -eux

            pwd
            ls -lah
            ls -lah vyos-build/build

        - uses: actions/create-release@master
          id: create_release
          env:
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          with:
            tag_name: ${{ github.ref }}
            release_name: VyOS ${{ github.ref }} for Education
            body: |
              VyOS ${{ env.RELEASE_VERSION }} for Education
            draft: true
            prerelease: true

        - uses: actions/upload-release-asset@master
          env:
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          with:
            #
            upload_url: ${{ steps.create_release.outputs.upload_url }}
            #
            asset_path: vyos-build/build/vyos-${{ env.RELEASE_VERSION }}-amd64.iso
            #
            asset_name: vyos-${{ env.RELEASE_VERSION }}-amd64.iso
            #
            asset_content_type: application/x-iso9660-image

        - uses: actions/upload-release-asset@master
          env:
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          with:
            #
            upload_url: ${{ steps.create_release.outputs.upload_url }}
            #
            asset_path: vyos-build/build/vyos-${{ env.RELEASE_VERSION }}-amd64.qcow2
            #
            asset_name: vyos-${{ env.RELEASE_VERSION }}-amd64.qcow2
            #
            asset_content_type: application/x-qemu-disk
    ```
-   Строка [6](#org-coderef--59b1f4-6): запускаем скрипт при создании любого тега.
-   Строка [26](#org-coderef--59b1f4-26): из полной ссылки на ветку тега выделяем номер версии.
    -   `refs/tags/v1.3.x` -&gt; `1.3.x`.


## <span class="section-num">4</span> Описание приложения для GNS3 {#описание-приложения-для-gns3}

-   Для установки образа VyOS в GNS3 (см. [Средство натурного моделирования сетей GNS3]({{< relref "2022-05-07-gns3-network-simulation-tool" >}})) необходимо создать файл приложения:
    ```js { linenos=true, linenostart=1 }
    {
        "appliance_id": "a5250e6e-be54-40d3-9082-0f0b601d3231",
        "name": "VyOS",
        "category": "router",
        "description": "VyOS is a community fork of Vyatta, a Linux-based network operating system that provides software-based network routing, firewall, and VPN functionality. Non-official build for Eduacation",
        "vendor_name": "Linux",
        "vendor_url": "https://vyos.net/",
        "documentation_url": "https://docs.vyos.io/",
        "product_name": "VyOS",
        "product_url": "https://vyos.net/",
        "registry_version": 4,
        "status": "stable",
        "maintainer": "Dmitry S. Kulyabov",
        "maintainer_email": "yamadharma@gmail.com",
        "usage": "Default username/password is vyos/vyos.\n\nThe -KVM versions are ready to use, no installation is required.\nThe other images will start the router from the CDROM on initial boot. Login and then type \"install image\" and follow the instructions.",
        "symbol": "vyos.svg",
        "port_name_format": "eth{0}",
        "qemu": {
            "adapter_type": "e1000",
            "adapters": 3,
            "ram": 512,
            "hda_disk_interface": "scsi",
            "arch": "x86_64",
            "console_type": "telnet",
            "boot_priority": "cd",
            "kvm": "allow"
        },
        "images": [
            {
                "filename": "vyos-1.3.3-amd64.iso",
                "version": "1.3.3-iso",
                "md5sum": "1ab25e1b63d9e3305bd5264721305794",
                "filesize": 382730240,
                "download_url": "https://github.com/yamadharma/vyos-build/releases/tag/v1.3.3",
                "direct_download_url": "https://github.com/yamadharma/vyos-build/releases/download/v1.3.3/vyos-1.3.3-amd64.iso"
            },
            {
                "filename": "vyos-1.3.3-amd64.qcow2",
                "version": "1.3.3-qemu",
                "md5sum": "9dffb9ab2af456c1eb993c0beef81b91",
                "filesize": 410058752,
                "download_url": "https://github.com/yamadharma/vyos-build/releases/tag/v1.3.3",
                "direct_download_url": "https://github.com/yamadharma/vyos-build/releases/download/v1.3.3/vyos-1.3.3-amd64.qcow2"
            },
            {
                "filename": "empty8G.qcow2",
                "version": "1.0",
                "md5sum": "f1d2c25b6990f99bd05b433ab603bdb4",
                "filesize": 197120,
                "download_url": "https://sourceforge.net/projects/gns-3/files/Empty%20Qemu%20disk/",
                "direct_download_url": "https://sourceforge.net/projects/gns-3/files/Empty%20Qemu%20disk/empty8G.qcow2/download"
            }
        ],
        "versions": [
            {
                "name": "1.3.3-iso",
                "images": {
                    "hda_disk_image": "empty8G.qcow2",
                    "cdrom_image": "vyos-1.3.3-amd64.iso"
                }
            },
            {
                "name": "1.3.3-qemu",
                "images": {
                    "hda_disk_image": "vyos-1.3.3-amd64.qcow2"
                }
            }
        ]
    }
    ```


## <span class="section-num">5</span> Использование в GNS3 {#использование-в-gns3}


### <span class="section-num">5.1</span> Установка образа VyOS quemu в GNS3 {#установка-образа-vyos-quemu-в-gns3}

-   Скачайте файл `vyos-edu.gns3a` из репозитория: <https://github.com/yamadharma/vyos-build/releases>.
-   Импортируйте `vyos-edu.gns3a` в GNS3 через пункт меню _File&gt;Import appliance_.
    -   Документация: <https://docs.gns3.com/docs/using-gns3/beginners/import-gns3-appliance>.
-   Установите необходимую версию VyOS.


### <span class="section-num">5.2</span> Видео: Установка образа VyOS quemu в GNS3 {#видео-установка-образа-vyos-quemu-в-gns3}

{{< tabs tabTotal="2" >}}
{{< rtab tabName="RuTube" >}}

{{< rutube 951fc2e6bf2157c298e019136b83992b >}}

{{< /rtab >}}
{{< rtab tabName="Youtube" >}}

{{< youtube 6bBXVc6bmrs >}}

{{< /rtab >}}
{{< /tabs >}}
