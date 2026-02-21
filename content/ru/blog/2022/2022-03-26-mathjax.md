---
title: "MathJax"
author: ["Dmitry S. Kulyabov"]
date: 2022-03-26T16:56:00+03:00
lastmod: 2023-08-27T18:25:00+03:00
tags: ["tex"]
categories: ["science"]
draft: false
slug: "mathjax"
---

_MathJax_ есть библиотека JavaScript, отображающая математические обозначения в веб-броузерах с использованием разметки MathML, LaTeX (см. [Система TeX]({{< relref "2021-04-23-tex" >}})) и ASCIIMathML (см. [AsciiMath]({{< relref "2021-10-25-asciimath" >}})).

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   Сайт: <https://www.mathjax.org/>
-   Документация: <http://docs.mathjax.org/>


## <span class="section-num">2</span> Подключение библиотеки {#подключение-библиотеки}

-   MathJax позволяет использовать как копию библиотеки на собственном сервере, так и версию библиотеки из CDN.
-   Примерный формат подключения библиотеки:
    ```html
    <script type="text/javascript" id="MathJax-script" async
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"
    </script>
    ```


## <span class="section-num">3</span> Разметка LaTeX {#разметка-latex}


### <span class="section-num">3.1</span> Набор {#набор}

-   Для отображения формулы в отдельном блоке заключите её в разделители `$$` … `$$` или `\[` … `\]`:
    ```latex
    \[ \sum_{i=0}^{n} i^{2} = \frac{(n^2 + n)(2n + 1)}{6}. \]
    ```

\\[ \sum\_{i=0}^{n} i^{2} = \frac{(n^2 + n)(2n + 1)}{6}. \\]

-   Для отображения формулы внутри строки заключите её в разделители `\(` … `\)`. Например, \\( \sum\_{i=0}^{n} i^{2} = \frac{(n^2 + n)(2n + 1)}{6}. \\)
-   Разделители `$` … `$` по умолчанию не поддерживаются, так как одиночные знаки доллара могут появляться в тексте и вызывать ошибочное преобразование текста в формулу.
-   Для отображения букв греческого алфавита используются
    -   строчные: `\alpha`, `\beta`, …, `\omega` : \\(\alpha\\), \\(\beta\\), …, \\(\omega\\);
    -   прописные: `\Gamma`, `\Delta`, …, `\Omega` : \\(\Gamma\\), \\(\Delta\\), …, \\(\Omega\\).
-   Для верхних и нижних индексов используются `^` и `_`. Например, `x_i^2` : \\(x\_i^2\\).
-   Группировка.
    -   Верхний и нижний индексы, а также другие операции применяются только к следующей _группе_.
    -   _Группой_ является либо один символ, либо любая формула, заключённая в фигурные скобки `{` … `}`.
    -   Например, `10^10` соответствует \\(10^10\\), а `10^{10}` соответствует \\(10^{10}\\).
-   Скобки.
    -   Одиночные символы `()[]` создают круглые и квадратные скобки \\((2+3)[4+4]\\).
    -   Для отображения фигурных скобок используются `\{` и `\}` : \\(\\{\\) и \\(\\}\\).
    -   Эти скобки не масштабируются вместе с формулой: `(\frac{\sqrt x}{y^3})` : \\((\frac{\sqrt x}{y^3})\\).
    -   Для автомасштабирования используются `\left(` и `\right)`: `\left(\frac{\sqrt x}{y^3}\right)` : \\(\left(\frac{\sqrt x}{y^3}\right)\\).
        -   `\left` и `\right` применяются к следующим типам скобок:
            -   `\left(` `\right)` : \\(\left( x \right)\\);
            -   `\left[` `\right]` : \\(\left[ x \right]\\);
            -   `\left\{` `\right\}` : \\(\left\\{ x \right\\}\\);
            -   `\left|` `\right|` : \\(\left| x \right|\\);
            -   `\langle` `\rangle` : \\(\langle x \rangle\\);
            -   `\lceil`  `\rceil` : \\(\lceil x \rceil\\);
            -   `\lfloor`  `\rfloor` : \\(\lfloor x \rfloor\\)
            -   Невидимые скобки (обозначаются `.`): `\left. \frac{1}{2} \right\}` :
                \\(\left. \frac{1}{2} \right\\}\\).
-   Суммы и интегралы `\sum` и `\int`.
    -   нижний индекс соответствует нижнему  пределу, а верхний индекс --- верхнему пределу.
    -   Например, `\sum_{i=0}^{\infty} i^{2}` : \\(\sum\_{i=0}^{\infty} i^{2}\\).
    -   Аналогично
        -   `\prod` : \\(\prod\\);
        -   `\int` : \\(\int\\);
        -   `\iint` : \\(\iint\\).
        -   `\bigcup` : \\(\bigcup\\);
        -   `\bigcap` : \\(\bigcap\\).
-   Дроби. Используется `\frac{a+1}{b+1}` : \\(\frac{a+1}{b+1}\\).
-   Шрифты.
    -   команда `\mathbb` или `\Bbb` для полужирного шрифта _для бедных_: `\mathbb{CHNQRZ}` : \\(\mathbb{CHNQRZ}\\);
    -   команда `\mathbf` для полужирного шрифта: `\mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz}` : \\(\mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}\\) \\(\mathbf{abcdefghijklmnopqrstuvwxyz}\\);
    -   команда `\mathtt` для шрифта _печатной машинки_: `\mathtt{ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz}` : \\(\mathtt{ABCDEFGHIJKLMNOPQRSTUVWXYZ}\\) \\(\mathtt{abcdefghijklmnopqrstuvwxyz}\\);
    -   команда `\mathrm` для обычного прямого шрифта: `\mathrm{ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz}` : \\(\mathrm{ABCDEFGHIJKLMNOPQRSTUVWXYZ}\\) \\(\mathrm{abcdefghijklmnopqrstuvwxyz}\\);
    -   команда `\mathsf` для шрифта без засечек: `\mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz}` : \\(\mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}\\) \\(\mathsf{abcdefghijklmnopqrstuvwxyz}\\);
    -   команда `\mathcal` для _каллиграфического_ написания: `\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz}` : \\(\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ}\\) \\(\mathcal{abcdefghijklmnopqrstuvwxyz}\\);
    -   команда `\mathscr` для шрифта, написанного от руки: `\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz}` : \\(\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ}\\) \\(\mathscr{abcdefghijklmnopqrstuvwxyz}\\);
    -   команда `\mathfrak` для фрактуры: `\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz}` : \\(\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZ}\\) \\(\mathfrak{abcdefghijklmnopqrstuvwxyz}\\).
-   Знак корня.
    -   команда `\sqrt` подстраивается к размеру аргумента:
        -   `\sqrt{x^3}` : \\(\sqrt{x^3}\\);
        -   `\sqrt[3]{\frac xy}` : \\(\sqrt[3]{\frac xy}\\).
-   Функции.
    -   `\sin` : \\(\sin x\\);
    -   `\max` : \\(\max (x,y)\\);
    -   `\ln` : \\(\ln x\\);
    -   `\lim` : `\lim_{x\to 0} f(x)` : \\(\lim\_{x\to 0} f(x)\\).
-   Специальные символы.
    -   `\lt \gt \le \ge \neq` : \\(\lt \gt \le \ge \neq\\);
    -   чтобы зачеркнуть символ, можно использовать `\not` : `\not\lt` : \\(\not\lt\\);
    -   `\times \div \pm \mp` : \\(\times \div \pm \mp\\);
    -   `\cdot` соответствует точке в центре : \\(x ⋅ y\\);
    -   `\cup \cap \setminus \subset \subseteq \subsetneq \supset \in \notin \emptyset \varnothing` : \\(\cup \cap \setminus \subset \subseteq \subsetneq \supset \in \notin \emptyset \varnothing\\);
    -   `\binom{n+1}{2k}` : \\(\binom{n+1}{2k}\\);
    -   `\to \rightarrow \leftarrow \Rightarrow \Leftarrow \mapsto` : \\(\to \rightarrow \leftarrow \Rightarrow \Leftarrow \mapsto\\);
    -   `\land \lor \lnot \forall \exists \top \bot \vdash \vDash` : \\(\land \lor \lnot \forall \exists \top \bot \vdash \vDash\\);
    -   `\star \ast \oplus \circ \bullet` : \\(\star \ast \oplus \circ \bullet\\);
    -   `\approx \sim \simeq \cong \equiv \prec` : \\(\approx \sim \simeq \cong \equiv \prec\\);
    -   `\infty \aleph_0` : \\(\infty \aleph\_0\\);
    -   `\nabla \partial` : \\(\nabla \partial\\);
    -   `\ldots` соответствует многоточию внизу : \\(a\_1, a\_2, \ldots a\_n\\);
    -   `\cdots` соответствует многоточию в центре \\(a\_1 + a\_2 + \cdots + a\_n\\);
    -   `\pmod` --- сравнение по модулю : `a \equiv b \pmod n` : \\(a \equiv b \pmod n\\);
    -   дополнительные написания греческих букв:
        -   `\epsilon \varepsilon` : \\(\epsilon \varepsilon\\);
        -   `\phi \varphi` : \\(\phi \varphi\\).
-   Акценты и диакритические знаки.
    -   команда `\hat` для одиночного символа : `\hat x` : \\(\hat x\\);
    -   команда `\widehat` для формулы : `\widehat xy` : \\(\widehat xy\\);
    -   команда `\bar` : `\bar x` : \\(\bar x\\);
    -   команда `\overline` : `\overline xyz` : \\(\overline xyz\\);
    -   команда `\vec` : `\vec x` : \\(\vec x\\);
    -   команда `\overrightarrow` : `\overrightarrow xy` : \\(\overrightarrow xy\\);
    -   команда `\overleftrightarrow` : `\overleftrightarrow xy` : \\(\overleftrightarrow xy\\);
    -   команды `\dot` и `\ddot` : `\frac{d x \dot{x}}{d x} = \dot{x}^2 + x \ddot{x}` : \\(\frac{d x \dot{x}}{d x} = \dot{x}^2 + x \ddot{x}\\).
-   Пробелы.
    -   пробел `\ = : : =x\ \ \ y` : \\(x\ \ \ y\\);
    -   тонкая шпация (узкий пробел) `\;` : `x\;y` : \\(x\\;y\\);
    -   квадрат (широкий пробел) `\quad` : `x \quad y` : \\(x \quad y\\);
    -   двойной квадрат `\qqquad` : `x \quad y` : \\(x \qquad y\\).


### <span class="section-num">3.2</span> Расширения LaTeX {#расширения-latex}


#### <span class="section-num">3.2.1</span> action {#action}


#### <span class="section-num">3.2.2</span> ams {#ams}


#### <span class="section-num">3.2.3</span> amscd {#amscd}


#### <span class="section-num">3.2.4</span> autoload {#autoload}


#### <span class="section-num">3.2.5</span> bbox {#bbox}


#### <span class="section-num">3.2.6</span> boldsymbol {#boldsymbol}


#### <span class="section-num">3.2.7</span> braket {#braket}


#### <span class="section-num">3.2.8</span> bussproofs {#bussproofs}


#### <span class="section-num">3.2.9</span> cancel {#cancel}


#### <span class="section-num">3.2.10</span> cases {#cases}


#### <span class="section-num">3.2.11</span> centernot {#centernot}


#### <span class="section-num">3.2.12</span> color {#color}


#### <span class="section-num">3.2.13</span> colortbl {#colortbl}


#### <span class="section-num">3.2.14</span> colorv2 {#colorv2}


#### <span class="section-num">3.2.15</span> configmacros {#configmacros}


#### <span class="section-num">3.2.16</span> empheq {#empheq}


#### <span class="section-num">3.2.17</span> enclose {#enclose}


#### <span class="section-num">3.2.18</span> extpfeil {#extpfeil}


#### <span class="section-num">3.2.19</span> gensymb {#gensymb}


#### <span class="section-num">3.2.20</span> html {#html}


#### <span class="section-num">3.2.21</span> mathtools {#mathtools}


#### <span class="section-num">3.2.22</span> mhchem {#mhchem}


#### <span class="section-num">3.2.23</span> newcommand {#newcommand}


#### <span class="section-num">3.2.24</span> noerrors {#noerrors}


#### <span class="section-num">3.2.25</span> noundefined {#noundefined}


#### <span class="section-num">3.2.26</span> physics {#physics}


#### <span class="section-num">3.2.27</span> require {#require}


#### <span class="section-num">3.2.28</span> setoptions {#setoptions}


#### <span class="section-num">3.2.29</span> tagformat {#tagformat}


#### <span class="section-num">3.2.30</span> textcomp {#textcomp}


#### <span class="section-num">3.2.31</span> textmacros {#textmacros}


#### <span class="section-num">3.2.32</span> unicode {#unicode}


#### <span class="section-num">3.2.33</span> upgreek {#upgreek}


#### <span class="section-num">3.2.34</span> verb {#verb}
