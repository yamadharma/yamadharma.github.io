---
title: "Конференция Saratov Fall Meeting 2023"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-25T13:38:00+03:00
lastmod: 2023-09-09T18:40:00+03:00
tags: ["research"]
categories: ["science"]
draft: false
slug: "conference-saratov-fall-meeting-2023"
---

Конференция Saratov Fall Meeting 2023.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Общая информация {#общая-информация}

-   [Конференция Saratov Fall Meeting]({{< relref "2023-07-05-conference-saratov-fall-meeting" >}})
-   Сайт: <https://sfmconference.org/sfm/sfm23/>
-   25-29 september, 2023, Saratov, Russia


## <span class="section-num">2</span> Заявленные доклады {#заявленные-доклады}


### <span class="section-num">2.1</span> Методический вывод уравнения эйконала {#методический-вывод-уравнения-эйконала}

-   Королькова А. В., RUDN University, Russian Federation
-   Геворкян М. Н., RUDN University, Russian Federation
-   Фёдоров А. В., RUDN University, Russian Federation
-   Штепа К. А., RUDN University, Russian Federation
-   Кулябов Д. С., RUDN University, Russian Federation &amp; JINR, Russian Federation

Обычно при работе с уравнением эйконала ссылаются на его вывод в монографии Борна и Вольфа. Вывод этого уравнения выполнен достаточно небрежно. Для того, чтобы разобраться в этом выводе требуется определённое число имплицитных предположений. Для лучшего понимания приближения эйконала и для методических целей авторы решили повторить вывод уравнения эйконала, эксплицировав все возможные допущения.
Методически предлагается следующий алгоритм вывода уравнения эйконала. Из уравнения Максвелла выводится волновое уравнение. При этом явно вводятся все условия, при которых это возможно сделать.
Далее от волнового уравнения осуществляется переход к уравнению Гельмгольца. От уравнения Гельмгольца, при приложении определённых допущений, производится переход к уравнению эйконала.
После разбора всех допущений и шагов, реализуется собственно переход от уравнений Максвелла к уравнению эйконала.
При выводе уравнения эйконала используется несколько формализмов. В качестве первого формализма используется стандартный формализм векторного анализа. Уравнения Максвелла и уравнение эйконала записывается в виде трёхмерных векторов.
После этого и для уравнений Максвелла, и для уравнения эйконала используется ковариантный 4-мерный формализм.
Результатом работы является методически выдержанное описание уравнения эйконала.

---

-   Methodological derivation of the eikonal equation

-   Korolkova A. V., RUDN University, Russian Federation
-   Gevorkyan M. N., RUDN University, Russian Federation
-   Fedorov A. V., RUDN University, Russian Federation
-   Stepa C. A., RUDN University, Russian Federation
-   Kulyabov D. S., RUDN University, Russian Federation &amp; JINR, Russian Federation

-   Korolkova A. V.1 Gevorkyan M. N.1 Fedorov A. V.1 Stepa C. A.1 Kulyabov D. S.1,2
-   1 RUDN University, Russian Federation 2 JINR, Russian Federation

-   Speaker: Arseny V. Fedorov
-   RUDN University, Russian Federation
-   1042210107@rudn.ru

Usually, when working with the eikonal equation, reference is made to its derivation in the monograph by Born and Wolf. The derivation of this equation is rather careless. To make sense of this conclusion requires a certain number of implicit assumptions. For a better understanding of the eikonal approximation and for methodological purposes, the authors decided to repeat the derivation of the eikonal equation, explicating all possible assumptions.
Methodically, the following algorithm for deriving the eikonal equation is proposed. The wave equation is derived from Maxwell's equation. In this case, all conditions are explicitly introduced under which it is possible to do this.
Further, from the wave equation, the transition to the Helmholtz equation is carried out. From the Helmholtz equation, with the application of certain assumptions, a transition is made to the eikonal equation.
After analyzing all the assumptions and steps, the transition from the Maxwell equations to the eikonal equation is actually implemented.
When deriving the eikonal equation, several formalisms are used. The standard formalism of vector analysis is used as the first formalism. Maxwell's equations and the eikonal equation are written as three-dimensional vectors.
After that, both the Maxwell equations and the eikonal equation use the covariant 4-dimensional formalism.
The result of the work is a methodically consistent description of the eikonal equation.


### <span class="section-num">2.2</span> Визуализация трассировки лучей на основе лучевой оптики {#визуализация-трассировки-лучей-на-основе-лучевой-оптики}

-   Фёдоров А. В., RUDN University, Russian Federation
-   Геворкян М. Н., RUDN University, Russian Federation
-   Штепа К. А., RUDN University, Russian Federation
-   Королькова А. В., RUDN University, Russian Federation
-   Demidiva A. V., RUDN University, Russian Federation
-   Кулябов Д. С., RUDN University, Russian Federation &amp; JINR, Russian Federation

Рассмотрены вопросы лучевой и геометрической оптики, их взаимосвязь и применение при моделировании оптических систем. Для определения линий распространения световых волн используется уравнение эйконала, которое имеет широкое применение в различных областях физики. Работа описывает линзы Люнеберга и Максвелла, созданные на основе неоднородных сред, обладающие уникальными свойствами фокусировки световых лучей. Для моделирования оптических систем используется язык программирования Julia и библиотека PyVista для отрисовки 3D графиков. Описаны методы визуализации полученных данных в виде 3D графиков с помощью библиотеки PyVista.

---

-   Ray tracing visualization based on ray optics

-   Fedorov A. V., RUDN University, Russian Federation
-   Gevorkyan M. N., RUDN University, Russian Federation
-   Stepa C. A., RUDN University, Russian Federation
-   Korolkova A. V., RUDN University, Russian Federation
-   Demidova A. V., RUDN University, Russian Federation
-   Kulyabov D. S., RUDN University, Russian Federation &amp; JINR, Russian Federation

-   Fedorov A. V.1 Gevorkyan M. N.1 Stepa C. A.1 Demidova A. V.1 Korolkova A. V.1 Kulyabov D. S.1,2
-   1 RUDN University, Russian Federation 2 JINR, Russian Federation

-   Speaker: Arseny V. Fedorov
-   RUDN University, Russian Federation
-   1042210107@rudn.ru

The issues of ray and geometric optics, their relationship and application in the modeling of optical systems are considered. To determine the propagation lines of light waves, the eikonal equation is used, which is widely used in various fields of physics. The work describes Luneburg and Maxwell lenses, created on the basis of inhomogeneous media, which have unique properties of focusing light rays. To simulate optical systems, the Julia programming language and the PyVista library for drawing 3D graphs are used. Methods for visualizing the obtained data in the form of 3D graphs using the PyVista library are described.


### <span class="section-num">2.3</span> Применение методов машинного обучения к задачам электродинамики {#применение-методов-машинного-обучения-к-задачам-электродинамики}

-   Королькова А. В., RUDN University, Russian Federation
-   Штепа К. А., RUDN University, Russian Federation
-   Фёдоров А. В., RUDN University, Russian Federation
-   Демидова Е. А., RUDN University, Russian Federation
-   Кулябов Д. С., RUDN University, Russian Federation &amp; JINR, Russian Federation

В работе рассматриваются разные подходы при применении методов машинного обучения для задач электродинамики.
Подходы к решению дифференциальных уравнений на основе методов машинного обучения можно условно разделить на две категории: подходы, полностью основанные на данных, и подходы, основанные на физике.
В подходах, полностью управляемыми данными, алгоритмы обучаются напрямую на массивах данных, не зная законов связи между входными и выходными. Считается, что не существует физической предварительной информации, которая могла бы ограничить обучение моделей машинного обучения. Обычно создание достаточных выборок данных для обучения моделей машинного обучения занимает много времени. Эффективность подходов, полностью основанных на данных, зависит от качества обучающих данных, а способность к обобщению также ограничена.
Подходы, основанные на физике, включают априорные физические или математические модели, которые демонстрируют лучшую производительность и улучшенную способность к обобщению после достаточного обучения.
Традиционные численные методы решения дифференциальных уравнений вносят дополнительную семантику в методы машинного обучения.
Методы нейронных сетей можно рассматривать как семейство мощных методов численного решения уравнений электродинамики.
Нейронные сети, основанные на физике (PINN), являются одним важным подходом к моделированию электродинамики.

---

-   Application of machine learning methods to electrodynamics problems

-   Korolkova A. V., RUDN University, Russian Federation
-   Stepa C. A., RUDN University, Russian Federation
-   Fedorov A. V., RUDN University, Russian Federation
-   Demidova E. A., RUDN University, Russian Federation
-   Kulyabov D. S., RUDN University, Russian Federation &amp; JINR, Russian Federation

-   Korolkova A. V.1 Stepa C. A.1 Fedorov A. V.1 Demidova E. A.1 Kulyabov D. S.1,2
-   1 RUDN University, Russian Federation 2 JINR, Russian Federation

-   Speaker: Christina A. Stepa
-   RUDN University, Russian Federation
-   1042210111@rudn.ru

We consider different approaches to the application of machine learning methods for problems of electrodynamics.
Approaches to solving differential equations based on machine learning methods can be roughly divided into two categories: fully data-driven approaches and physics-based approaches.
In completely data-driven approaches, algorithms are trained directly on datasets, without knowing the laws of connection between inputs and outputs. It is believed that there is no physical prior information that could limit the training of machine learning models. It usually takes a long time to generate enough data samples to train machine learning models. The effectiveness of fully data-driven approaches depends on the quality of the training data, and the ability to generalize is also limited.
Physics-based approaches include a priori physical or mathematical models that show better performance and improved generalization after sufficient training.
Traditional numerical methods for solving differential equations bring additional semantics to machine learning methods.
Neural network methods can be considered as a family of powerful methods for the numerical solution of electrodynamics equations.
Physics based neural networks (PINNs) are one important approach to electrodynamics modeling.
