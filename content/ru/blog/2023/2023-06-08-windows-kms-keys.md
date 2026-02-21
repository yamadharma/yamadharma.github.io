---
title: "Windows. Ключи KMS"
author: ["Dmitry S. Kulyabov"]
date: 2023-06-08T15:36:00+03:00
lastmod: 2024-01-28T20:08:00+03:00
tags: ["sysadmin", "windows"]
categories: ["computer-science"]
draft: false
slug: "windows-kms-keys"
---

Активация клиента службы управления ключами (KMS) и ключи продуктов.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Установка ключа продукта {#установка-ключа-продукта}

-   Если вы переключаете компьютер из режима использования узла KMS, ключа MAK или розничной версии Windows в режим клиента KMS, установите соответствующий ключ продукта (GVLK):
    ```shell
    slmgr /ipk <product key>
    ```
-   Указать адрес KMS сервера (если при установке KMS сервер не опубликован в DNS):
    ```shell
    slmgr /skms kms-server.winitpro.ru:1688
    ```
-   Активировать ОС:
    ```shell
    slmgr /ato
    ```
-   Активировать Office:
    ```shell
    slmgr /ato <ключ GLVK>
    ```


## <span class="section-num">2</span> Универсальные ключи многократной установки (GVLK) {#универсальные-ключи-многократной-установки--gvlk}

-   Страница: <https://learn.microsoft.com/ru-ru/windows-server/get-started/kms-client-activation-keys>

-   LTSC означает Long-Term Servicing Channel.
-   LTSB означает Long-Term Servicing Branch.


### <span class="section-num">2.1</span> Windows 11 и Windows 10 (версии Semi-Annual Channel) {#windows-11-и-windows-10--версии-semi-annual-channel}

| Версия операционной системы                  | Ключ продукта клиента KMS     |
|----------------------------------------------|-------------------------------|
| Windows Pro                                  | W269N-WFGWX-YVC9B-4J6C9-T83GX |
| Windows Pro N                                | MH37W-N47XK-V7XM9-C7227-GCQG9 |
| Windows Pro для рабочих станций              | NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J |
| Windows Pro для рабочих станций N            | 9FNHH-K3HBT-3W4TD-6383H-6XYWF |
| Windows Pro для образовательных учреждений   | 6TP4R-GNPTD-KYYHQ-7B7DP-J447Y |
| Windows Pro для образовательных учреждений N | YVWGF-BXNMC-HTQYQ-CPQ99-66QFC |
| Windows для образовательных учреждений       | NW6C2-QMPVW-D7KKK-3GKT6-VCFB2 |
| Windows для образовательных учреждений N     | 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ |
| Windows Корпоративная                        | NPPR9-FWDCX-D2C8J-H872K-2YT43 |
| Windows Корпоративная N                      | DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 |
| Windows Корпоративная G                      | YYVX9-NTFWV-6MDM3-9PT4T-4M68B |
| Windows Корпоративная G N                    | 44RPN-FTY23-9VTTB-MP9BX-T84FV |


### <span class="section-num">2.2</span> Microsoft Office 2021/2019/2016 {#microsoft-office-2021-2019-2016}

-   Список официальных публичных GVLK ключей: <https://technet.microsoft.com/en-us/library/dn385360(v=office.16).aspx>
-   Все корпоративные версии Office 2021/2019/2016 устанавливаются с публичными Generic Volume License Key (GVLK) ключами (эти ключи являются открытыми и доступны абсолютно всем на страницах портала Microsoft TechNet).
-   Они автоматически активируются при наличии в сети KMS сервера.
-   Как правило, вводить GVLK ключ в Office не требуется.

| Продукт                            | GVLK ключ для KMS активации   |
|------------------------------------|-------------------------------|
| Office LTSC Professional Plus 2021 | FXYTK-NJJ8C-GB6DW-3DYQT-6F7TH |
| Office LTSC Standard 2021          | KDX7X-BNVR8-TXXGX-4Q7Y8-78VT3 |
| Project Professional 2021          | FTNWT-C6WBT-8HMGF-K9PRX-QV9H8 |
| Project Standard 2021              | J2JDC-NJCYY-9RGQ4-YXWMH-T3D4T |
| Visio LTSC Professional 2021       | KNH8D-FGHT4-T8RK3-CTDYJ-K2HT4 |
| Visio LTSC Standard 2021           | MJVNY-BYWPY-CWV6J-2RKRT-4M8QG |
| Access LTSC 2021                   | WM8YG-YNGDD-4JHDC-PG3F4-FC4T4 |
| Excel LTSC 2021                    | NWG3X-87C9K-TC7YY-BC2G7-G6RVC |
| Outlook LTSC 2021                  | C9FM6-3N72F-HFJXB-TM3V9-T86R9 |
| PowerPoint LTSC 2021               | TY7XF-NFRBR-KJ44C-G83KF-GX27K |
| Publisher LTSC 2021                | 2MW9D-N4BXM-9VBPG-Q7W6M-KFBGQ |
| Skype for Business LTSC 2021       | HWCXN-K3WBT-WJBKY-R8BD9-XK29P |
| Word LTSC 2021                     | TN8H9-M34D3-Y64V9-TR72V-X79KV |
| Office Professional Plus 2019      | NMMKJ-6RK4F-KMJVX-8D9MJ-6MWKP |
| Office Standard 2019               | 6NWWJ-YQWMR-QKGCB-6TMB3-9D9HK |
| Project Professional 2019          | B4NPR-3FKK7-T2MBV-FRQ4W-PKD2B |
| Project Standard 2019              | C4F7P-NCP8C-6CQPT-MQHV9-JXD2M |
| Visio Professional 2019            | 9BGNQ-K37YR-RQHF2-38RQ3-7VCBB |
| Visio Standard 2019                | 7TQNQ-K3YQQ-3PFH7-CCPPM-X4VQ2 |
| Access 2019                        | 9N9PT-27V4Y-VJ2PD-YXFMF-YTFQT |
| Excel 2019                         | TMJWT-YYNMB-3BKTF-644FC-RVXBD |
| Outlook 2019                       | 7HD7K-N4PVK-BHBCQ-YWQRW-XW4VK |
| PowerPoint 2019                    | RRNCX-C64HY-W2MM7-MCH9G-TJHMQ |
| Publisher 2019                     | G2KWX-3NW6P-PY93R-JXK2T-C9Y9V |
| Skype for Business 2019            | NCJ33-JHBBY-HTK98-MYCV8-HMKHJ |
| Word 2019                          | PBX3G-NWMT6-Q7XBW-PYJGG-WXD33 |
| Office Professional Plus 2016      | XQNVK-8JYDB-WJ9W3-YJ8YR-WFG99 |
| Office Standard 2016               | JNRGM-WHDWX-FJJG3-K47QV-DRTFM |
| Project Professional 2016          | YG9NW-3K39V-2T3HJ-93F3Q-G83KT |
| Project Standard 2016              | GNFHQ-F6YQM-KQDGJ-327XX-KQBVC |
| Visio Professional 2016            | PD3PC-RHNGV-FXJ29-8JK7D-RJRJK |
| Visio Standard 2016                | 7WHWN-4T7MP-G96JF-G33KR-W8GF4 |
| Access 2016                        | GNH9Y-D2J4T-FJHGG-QRVH7-QPFDW |
| Excel 2016                         | 9C2PK-NWTVB-JMPW8-BFT28-7FTBF |
| OneNote 2016                       | DR92N-9HTF2-97XKM-XW2WJ-XW3J6 |
| Outlook 2016                       | R69KK-NTPKF-7M3Q4-QYBHW-6MT9B |
| PowerPoint 2016                    | J7MQP-HNJ4Y-WJ7YM-PFYGF-BY6C6 |
| Publisher 2016                     | F47MM-N3XJP-TQXJ9-BP99D-8K837 |
| Skype for Business 2016            | 869NQ-FJ69K-466HW-QYCP2-DDBV6 |
| Word 2016                          | WXY84-JN2Q9-RBCCQ-3Q3J3-3PFJ6 |
