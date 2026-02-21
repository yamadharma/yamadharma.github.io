---
title: "Saratov Fall Meeting Conference 2023"
author: ["Dmitry S. Kulyabov"]
date: 2023-08-25T13:38:00+03:00
lastmod: 2023-08-25T20:24:00+03:00
categories: ["science"]
draft: false
slug: "conference-saratov-fall-meeting-2023"
---

Saratov Fall Meeting Conference 2023.

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> General information {#general-information}

-   Site: <https://sfmconference.org/sfm/sfm23/>
-   25-29 september, 2023, Saratov, Russia


## <span class="section-num">2</span> Claimed speeches {#claimed-speeches}


### <span class="section-num">2.1</span> Methodological derivation of the eikonal equation {#methodological-derivation-of-the-eikonal-equation}

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


### <span class="section-num">2.2</span> Ray tracing visualization based on ray optics {#ray-tracing-visualization-based-on-ray-optics}

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


### <span class="section-num">2.3</span> Application of machine learning methods to electrodynamics problems {#application-of-machine-learning-methods-to-electrodynamics-problems}

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
