---
title: "Windows. Автоустановка. Простой файл ответов"
author: ["Dmitry S. Kulyabov"]
date: 2023-06-08T16:47:00+03:00
lastmod: 2024-10-08T15:39:00+03:00
tags: ["sysadmin", "windows"]
categories: ["computer-science"]
draft: false
slug: "windows-unattended-simple-autounattend"
---

Простой файл ответов для автоустановки Windows.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Файл ответов {#файл-ответов}

-   За счет файла значительно сокращается количество экранов программы установки, из которых остаются только:
    -   выбор издания
    -   управление дисками
    -   подключение к Wi-Fi
    -   пароль учетной записи (можно задать)
-   Файл предназначен для 64-разрядной Windows. Сохраните его с именем `autounattend.xml` в корень установочной флэшки.
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <!-- https://www.outsidethebox.ms/19924/ -->
    <unattend xmlns="urn:schemas-microsoft-com:unattend">
            <settings pass="windowsPE">
                <component name="Microsoft-Windows-International-Core-WinPE" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                    <InputLocale>en-US; ru-RU</InputLocale>
                    <SystemLocale>ru-RU</SystemLocale>
                    <UILanguage>ru-RU</UILanguage>
                    <UserLocale>ru-RU</UserLocale>
                </component>
                <component name="Microsoft-Windows-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                    <UserData>
                        <!-- KMS keys https://docs.microsoft.com/windows-server/get-started/kmsclientkeys -->
                        <ProductKey>
                            <Key>NW6C2-QMPVW-D7KKK-3GKT6-VCFB2</Key>
                        </ProductKey>
                        <AcceptEula>true</AcceptEula>
                    </UserData>
                </component>
            </settings>
            <settings pass="oobeSystem">
                <component name="Microsoft-Windows-International-Core" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                    <InputLocale>en-US; ru-RU</InputLocale>
                    <SystemLocale>ru-RU</SystemLocale>
                    <UILanguage>ru-RU</UILanguage>
                    <UserLocale>ru-RU</UserLocale>
                </component>
                <component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                    <OOBE>
                        <HideOnlineAccountScreens>true</HideOnlineAccountScreens>
                        <ProtectYourPC>3</ProtectYourPC>
                    </OOBE>
                    <UserAccounts>
                        <LocalAccounts>
                            <LocalAccount wcm:action="add">
                                <Group>Administrators</Group>
                                <Name>Admin</Name>
                                <!--<Password>
                                    <Value>goofy reward replica danger</Value>
                                    <PlainText>true</PlainText>
                                </Password> -->
                            </LocalAccount>
                        </LocalAccounts>
                    </UserAccounts>
                   <AutoLogon>
                     <Password>
                       <Value>123456</Value>
                       <PlainText>true</PlainText>
                     </Password>
                     <Username>Admin</Username>
                     <LogonCount>1</LogonCount>
                     <Enabled>true</Enabled>
                   </AutoLogon>
                </component>
            </settings>
    </unattend>
    ```
-   Файл рассчитан на русскую версию ОС.
-   Издание выбирается на основе ключа продукта в файле ответов.
-   Используется ключ KMS для установки (но не обязательно активации).
-   Создаётся локальная учетная запись:
    -   экран создания учетной записи Microsoft (MSA) пропускается.
    -   Локальной учетной записи не задаются три контрольных вопроса.
-   Пароль закомментирован, поэтому программа установки предложит сменить его – задайте любой или продолжайте с пустым, нажав стрелку рядом с подтверждением пароля.


## <span class="section-num">2</span> Ресурсы {#ресурсы}

-   Заметки по файлу автоустановки: <https://github.com/memstechtips/UnattendedWinstall>
