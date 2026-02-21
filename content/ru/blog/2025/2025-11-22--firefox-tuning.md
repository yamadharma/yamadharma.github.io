---
title: "Firefox. Настройка"
author: ["Dmitry S. Kulyabov"]
date: 2025-11-22T19:09:00+03:00
lastmod: 2025-11-22T21:13:00+03:00
tags: ["network", "sysadmin"]
categories: ["computer-science"]
draft: false
slug: "firefox-tuning"
---

Firefox. Настройка.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Настройки пользователя {#настройки-пользователя}

-   Можно напрямую изменять настройки в `about:config`, но они будут сохранены только в текущем профиле и не синхронизируются между устройствами.
-   Создайте файл `user.js`  в папке профиля Firefox.
-   Расположение папки можно найти на странице `about:profiles`.
-   Найдите текущий используемый профиль, откройте корневой каталог и там создайте файл `user.js`.
-   Там же, где находится файл `prefs.js`. Можно использовать его как пример для создания `user.js`.
-   Вариант конфигурации:

<!--listend-->

```js
user_pref("browser.urlbar.decodeURLsOnCopy", true);
user_pref("browser.tabs.closeWindowWithLastTab", true);
user_pref("browser.tabs.allowTabDetach", false);
user_pref("browser.tabs.insertAfterCurrent", true);
```


## <span class="section-num">2</span> Примеры настроек {#примеры-настроек}


### <span class="section-num">2.1</span> Отключение URL-encoding {#отключение-url-encoding}

-   При копировании ссылок русские буквы преобразуются в кодированное значение.
-   Для отключения измените `browser.urlbar.decodeURLsOnCopy` на `true`.
-   При этом пробел остаётся пробелом, и скопированная ссылка у вас может не работать.


### <span class="section-num">2.2</span> Не закрывать браузер с последней закрытой вкладкой {#не-закрывать-браузер-с-последней-закрытой-вкладкой}

-   Можно отключить закрытие окна при закрытии последней вкладки.
-   Замените `browser.tabs.closeWindowWithLastTab` на `false`.


### <span class="section-num">2.3</span> Открепление вкладок {#открепление-вкладок}

-   Иногда вкладки при их перемещении открепляются и открываются в новом окне.
-   Чтобы этого не происходило, нужно отключить `browser.tabs.allowTabDetach`.


### <span class="section-num">2.4</span> Открытие новой вкладки рядом с текущей {#открытие-новой-вкладки-рядом-с-текущей}

-   По умолчанию новая вкладка открывается в конце.
-   Чтобы она открывалась рядом с текущей, установите `browser.tabs.insertAfterCurrent` в `true`.


## <span class="section-num">3</span> Навигация {#навигация}

-   [Emacs. Клавиатура. Броузеры]({{< relref "2023-08-19-emacs-keyboard-browsers" >}})
-   [Vim. Клавиатура. Броузеры]({{< relref "2023-08-19-vim-keyboard-browsers" >}})
-   [Броузер. Расширение Vimium-c]({{< relref "2025-04-06--browser-plugin-vimiumc" >}})


## <span class="section-num">4</span> Дополнения {#дополнения}

-   [Firefox. Расширения]({{< relref "2006-12-24-firefox-extention" >}})
