---
title: "Sway. Скриншоты"
author: ["Dmitry S. Kulyabov"]
date: 2023-11-05T15:33:00+03:00
lastmod: 2024-02-29T20:26:00+03:00
tags: ["wayland"]
categories: ["computer-science"]
draft: false
slug: "sway-screenshots"
---

Создание снимков экрана в Sway и Wayland.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> grim {#grim}

-   В X11 аналогом является `scrot`.
-   Для Wayland используется связка `grim` (получение снимка экрана) + [slurp](https://github.com/emersion/slurp) (выделение области экрана)
-   Grim:
    -   Репозиторий: <https://git.sr.ht/~emersion/grim/refs>
-   Slurp:
    -   Репозиторий: <https://github.com/emersion/slurp>


### <span class="section-num">1.1</span> Установка {#установка}

-   Gentoo:

<!--listend-->

```shell
emerge -uv gui-apps/slurp gui-apps/grim
```


### <span class="section-num">1.2</span> Настройка {#настройка}

-   Настроим получение снимков экрана:

<!--listend-->

```conf-unix
# ~/.config/sway/config.d/80-screenshots.conf
### Screenshot

## Screenshot active display
bindsym Print exec grim -t png "$(xdg-user-dir PICTURES)"/$(date +%Y-%m-%d_%H-%M-%S).png

## Screenshot selected region
bindsym Control+Print exec grim -t png -g "$(slurp)" "$(xdg-user-dir PICTURES)"/$(date +%Y-%m-%d_%H-%M-%S).png

## Screenshot active display and copy to buffer
bindsym Alt+Print exec grim -t png - | wl-copy

## Screenshot selected region and copy to buffer
bindsym Alt+Control+Print exec grim -t png -g "$(slurp)" - | wl-copy
```

-   При нажатии `PrtScr` делается снимок всего экрана и изображение сохраняется в каталог `$(xdg-user-dir PICTURES)` (`~/Pictures`).
-   При нажатии `Control + PrtScr` предлагается выбрать область экрана, снимок которой следует сделать. Изображение сохраняется в каталог `$(xdg-user-dir PICTURES)` (`~/Pictures`).
-   При нажатии `Alt + PrtScr` делается снимок всего экрана и изображение копируется в системный буфер.
-   При нажатии `Alt+ Control + PrtScr` предлагается выбрать область экрана, снимок которой следует сделать. Изображение копируется в системный буфер.


## <span class="section-num">2</span> Swappy {#swappy}

-   Инструмент для создания и редактирования снимков экрана в Wayland.
-   Вдохновлён Snappy для macOS (<http://snappy-app.com/>).
-   Репозиторий: <https://github.com/jtheoof/swappy>


### <span class="section-num">2.1</span> Установка {#установка}

-   Gentoo:

<!--listend-->

```shell
emerge gui-apps/swappy
```


### <span class="section-num">2.2</span> Настройка {#настройка}

-   Настроим получение снимков экрана:

<!--listend-->

```conf-unix
# ~/.config/sway/config.d/80-screenshots.conf
### Screenshot

## Screenshot selected region and send to editor tool
bindsym $mod+Print exec grim -t png -g "$(slurp)" - | swappy -f -
```

-   При нажатии `Mod + PrtScr` делается снимок области экрана и изображение открывается в редакторе скриншотов.


## <span class="section-num">3</span> Satty {#satty}

-   Инструмент для аннотаций скриншотов, вдохновленный Swappy и Flameshot .
-   Репозиторий: <https://github.com/gabm/Satty>
-   Улучшения по сравнению с существующими инструментами аннотирования скриншотов:
    -   простой и понятный набор инструментов;
    -   полноэкранный режим аннотаций и обрезка кадров после съемки;
    -   работа с композиторами на базе wlroots (Sway, Hyprland, River).


### <span class="section-num">3.1</span> Установка {#установка}

-   Gentoo:
    -   присутствует в оверлее `guru` (см. [Gentoo. Дополнительные репозитории]({{< relref "2023-10-01-gentoo-additional-repositories" >}})):

<!--listend-->

```shell
eselect repository enable guru
emerge --sync guru
emerge satty
```


### <span class="section-num">3.2</span> Настройка {#настройка}

-   Настроим получение снимков экрана:

<!--listend-->

```conf-unix
# ~/.config/sway/config.d/80-screenshots.conf
### Screenshot

## Screenshot selected region and send to editor tool
bindsym $mod+Print exec grim -g "$(slurp -o -r -c '#ff0000ff')" - | satty --filename - --fullscreen --output-filename "$(xdg-user-dir PICTURES)"/$(date +%Y-%m-%d_%H-%M-%S).png
```

-   При нажатии `Mod + PrtScr` делается снимок области экрана и изображение открывается в редакторе скриншотов.
