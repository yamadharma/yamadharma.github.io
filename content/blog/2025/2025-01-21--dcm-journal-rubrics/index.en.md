---
title: "DCM. Journal rubrics"
author: ["Dmitry S. Kulyabov"]
date: 2025-01-21T15:19:00+03:00
lastmod: 2025-01-21T19:39:00+03:00
tags: ["science-admin", "rudn"]
categories: ["job", "science"]
draft: false
slug: "dcm-journal-rubrics"
---

DCM Journal rubrics

<!--more-->

{{< toc >}}


## <span class="section-num">1</span> Rubrics of the journal {#rubrics-of-the-journal}

-   The editorial board has decided to return the explicitly allocated rubrics in the journal.
-   The journal contains subject and organizational rubrics.
-   The subject rubrics are:
    -   Informatics (computer science);
    -   mathematical modeling;
    -   physics.
-   Organizational rubrics:
    -   editorials;
    -   letters to the editor.


## <span class="section-num">2</span> Subject rubrics {#subject-rubrics}

-   The journal publishes articles on computer science, mathematical modeling, and physics.
-   All these scientific fields are closely related, and the connecting core is mathematical modeling.


### <span class="section-num">2.1</span> Computer Science {#computer-science}

-   Computer science research articles cover a wide range of topics related to modern information processing technologies and techniques:
    -   networks and database management systems;
    -   artificial intelligence and machine learning;
    -   software engineering;
    -   cybersecurity;
    -   software methods development;
    -   theory of computing;
    -   information technology.


### <span class="section-num">2.2</span> Physics {#physics}

-   Physics research articles cover a wide range of topics, each aiming to advance understanding of different aspects of nature (Nature-1) and to develop new technologies (Nature-2):
    -   particle physics;
    -   cosmology and astrophysics;
    -   nuclear physics;
    -   condensed state physics;
    -   nonlinear physics;
    -   laser physics and optics;
    -   quantum mechanics;
    -   field theory;
    -   computational physics.


### <span class="section-num">2.3</span> Mathematical Modeling {#mathematical-modeling}

-   Mathematical modeling emerged at the intersection of several fields of science:
    -   applied theoretical physics;
    -   mathematical physics;
    -   computational physics.
-   The structure of the field of mathematical modeling is given as the triad Model--Algorithm--Program [<a href="#citeproc_bib_item_1">1</a>; <a href="#citeproc_bib_item_2">2</a>].
-   Modeling as a discipline encompasses different types of modeling approaches [<a href="#citeproc_bib_item_3">3</a>].
-   From our point of view, these approaches can be schematically described in a unified way.
-   The research framework consists of operational and theoretical parts.
-   The operational parts are represented by the procedures of system preparation and measurement. It is also possible to describe the operational parts as input and output data.
-   The theoretical part consists of two layers: model layer and implementation layer.
    -   The modeling layer is the main layer and defines the actual model under study.
    -   The realization layer describes the specific structure of the system evolution. Depending on the type of realization, different types of models can be obtained:
        -   realization---mathematical expressions: analytical mathematical models;
        -   implementation---analog system: physical model;
        -   realization---algorithm: simulation models;
        -   implementation---behavior approximation: surrogate model.
-   Each type of model has its own area of applicability, advantages and disadvantages.
-   The use of the full range of models allows the deepest and most comprehensive study of the system being modeled.


#### <span class="section-num">2.3.1</span> Analytical modeling {#analytical-modeling}

-   The most rigorous study is based, usually, on an analytical mathematical model. In this case, the model layer is realized through mathematical expressions describing the evolution of the system.


#### <span class="section-num">2.3.2</span> Physical modeling {#physical-modeling}

-   The obtained mathematical model should be compared with experimental data, verify it. For this purpose, a model analogous to a physical or technical system can be created.
-   A physical model can also be a virtual model. For example, you can build a model of a data network using images of operating systems of routers and switches.


#### <span class="section-num">2.3.3</span> Simulation Modeling {#simulation-modeling}

-   With the development of computer technology, it became possible to specify a model realization not in the form of a mathematical description, but in the form of some algorithm.
-   This type of models was called _simulation models_, and the approach itself was called _simulation modeling_.
-   A simulation model plays a dual role.
    -   A simulation model, debugged and tested on experimental data and a physical model, can itself serve the purpose of verification of a mathematical model.
    -   On the other hand, the simulation model allows to investigate the behavior of the simulated system under different variants of input data more effectively than the mathematical model.


#### <span class="section-num">2.3.4</span> Statistical modeling {#statistical-modeling}

-   This type of modeling includes models that are implemented through _machine learning_ methods.
-   It can be divided into several approaches (e.g., surrogate modeling; data-driven modeling).

<!--list-separator-->

1.  Surrogate modeling

    -   Other names: approximation models, response surface models, metamodels, black box models.
    -   In this approach, the modeling layer is known and even has an implementation (most often in the form of an analytical model).
    -   For many real-world problems, modeling can take quite a long time.  Extremely difficult (rather routine) problems such as solution optimization, solution space exploration, sensitivity analysis and “what if” analysis become impossible because they require thousands or millions of simulation evaluations.
    -   To simplify the study, models are built that mimic the behavior of the original model as closely as possible while being computationally cheap. Surrogate models are built using a data-driven approach. The exact inner workings of the simulation code are not assumed to be known (or even understood), only the input-output (cooking-measuring) behavior is important. The model is built by simulating the response to a limited number (sometimes quite large) of selected data points. The scientific goal of surrogate modeling is to create a surrogate that is as accurate as possible, using as few modeling estimates as possible.

<!--list-separator-->

2.  Data-driven modeling

    -   Used when there is no model per se and the nature of the true function is unknown a priori, so it is unclear which surrogate model will be most accurate. Furthermore, it is not clear how to obtain the most reliable estimates of the accuracy of this surrogate. In this case, the model layer is replaced by the researcher's guesses.


## <span class="section-num">3</span> Organizational rubrics {#organizational-rubrics}

-   The following organizational rubrics are suggested for the journal:
    -   editorial rubric;
    -   letters to the editor.
-   In our view, editorials fulfill several tasks. In these articles, the editorial board:
    -   gives advice and recommendations on the proper design and structuring of scientific articles (in particular, for natural science articles, the structure of the IMRAD (Introduction, Methods, Results and Discussion) article [<a href="#citeproc_bib_item_4">4</a>; <a href="#citeproc_bib_item_5">5</a>] is supposed to be used, which facilitates the perception and understanding of the research);
    -   communicates the requirements of the journal; indicates the specific requirements of journals for article layout, both semantic and syntactic.
    -   gives direction to improve the quality of articles, emphasizes the elements of research; the editorial board tries to strengthen the scientific value of the papers;
    -   provides semantic navigation through the current issue.
-   Editorial articles inform the authors about the current goal-setting of the journal.
-   The column _Letters to the Editor_ is intended for publication of short messages containing comments, explanations or alternative points of view concerning both previously published articles and different thoughts that the editorial board does not consider it necessary to place in the corresponding subject rubrics.
-   The main purposes of such letters are:
    -   comments and clarifications on certain aspects of a previously published article, if some points remained unclear or insufficiently disclosed;
    -   alternative or additional opinions on the issues discussed in the published articles;
    -   constructive criticism of the data or conclusions presented in the article;
    -   expansion of scientific discourse.


## <span class="section-num">4</span> Bibliography {#bibliography}

## Литература

<div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>1.	Samarskii, A.A. Principles of Mathematical Modelling: Ideas, Methods, Examples. Principles of Mathematical Modelling / A.A. Samarskii, A.P. Mikhailov. – CRC Press, 2001. – 360 pp.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>2.	Chetverushkin, B.N. Triad of Samarskii. The 100th anniversary of academician A.A. Samarskii / B.N. Chetverushkin, A.P. Mikhailov // Herald of the Russian Academy of Sciences. – 2019. – Vol. 89. – № 2. – Pp. 187–193. DOI: <a href="https://doi.org/10.31857/s0869-5873892187-193">10.31857/s0869-5873892187-193</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_3"></a>3.	Korolkova, A.V. <a href="https://doi.org/10.1007/978-3-030-66471-8_40">Practical Application of the Multi-model Approach in the Study of Complex Systems</a> / A.V. Korolkova, D.S. Kulyabov, M. Hnatič // Distributed Computer and Communication Networks. DCCN 2020 : Lecture Notes в Computer Science / V.M. Vishnevskiy et al. eds. . – Cham : Springer Nature Switzerland AG, 2020. – Vol. 12563. – Pp. 526–537.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_4"></a>4.	Wu, J. Improving the writing of research papers: IMRAD and beyond / J. Wu // Landscape Ecology. – 2011. – Vol. 26. – Improving the writing of research papers. – № 10. – Pp. 1345–1349. DOI: <a href="https://doi.org/10.1007/s10980-011-9674-3">10.1007/s10980-011-9674-3</a>.</div>
  <div class="csl-entry"><a id="citeproc_bib_item_5"></a>5.	Brain, L. Structure of the scientific paper / L. Brain // British Medical Journal. – 1965. – Vol. 2. – № 5466. – Pp. 868–869. DOI: <a href="https://doi.org/10.1136/bmj.2.5466.868">10.1136/bmj.2.5466.868</a>.</div>
</div>
