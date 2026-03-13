---
title: "Сопоставление команд Cisco и Huawei"
author: ["Dmitry S. Kulyabov"]
date: 2023-04-04T15:26:00+03:00
lastmod: 2024-09-10T19:56:00+03:00
tags: ["cisco", "sysadmin", "network"]
categories: ["computer-science"]
draft: false
slug: "cisco-huawei-commands"
---

Команды Cisco и Huawei.

<!--more-->

{{< toc >}}

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 1:</span>
  Exec mode
</div>

| Cisco exec mode                    | Huawei user view               |
|------------------------------------|--------------------------------|
| clear                              | reset                          |
| clear access-list counters         | reset acl counter all          |
| clear counters                     | reset counters interface       |
| clear interface                    | reset counters interface       |
| configure terminal                 | system-view                    |
| copy running-config startup-config | save                           |
| debug / no debug                   | debugging / undo debugging     |
| disable                            | super 0                        |
| enable                             | super                          |
| erase                              | delete                         |
| exit                               | quit                           |
| more nvram:startup-config          | display saved-configuration    |
| no                                 | undo                           |
| reload                             | reboot                         |
| show                               | display                        |
| show clock                         | display clock                  |
| show flash                         | dir flash:                     |
| show history-command               | display history-command        |
| show interfaces                    | display interface              |
| show ip bgp                        | display bgp routing-table      |
| show ip interface                  | display ip interface           |
| show ip route                      | display ip routing-table       |
| show logging                       | display logbuffer              |
| show running-config                | display current-configuration  |
| show snmp                          | display snmp-agent statistics  |
| show startup-config                | display saved-configuration    |
| show tech-support                  | display diagnostic-information |
| show users                         | display users                  |
| show version                       | display version                |
| terminal length 0                  | screen-length 0 temporary      |
| traceroute                         | tracert                        |
| write erase                        | reset saved-configuration      |
| write memory                       | save                           |
| write terminal                     | display current-configuration  |

<div class="table-caption">
  <span class="table-number">&#1058;&#1072;&#1073;&#1083;&#1080;&#1094;&#1072; 2:</span>
  Configuration mode
</div>

| Cisco configuration mode | Huawei system view       |
|--------------------------|--------------------------|
| end                      | return                   |
| snmp-server              | snmp-agent               |
| hostname                 | sysname                  |
| router bgp               | bgp                      |
| router ospf              | ospf                     |
| router rip               | rip                      |
| shutdown / no shutdown   | shutdown / undo shutdown |
