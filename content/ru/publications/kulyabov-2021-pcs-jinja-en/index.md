---
title: Using a Template Engine as a Computer Algebra Tool
authors:
- Migran Nelsonovich Gevorkyan
- Anna Vladislavovna Korol'kova
- Dmitry Sergeevich Kulyabov
date: '2021-01-01'
publishDate: '2026-01-23T13:43:24.282169Z'
publication_types:
- article-journal
publication: '*Programming and Computer Software*'
abstract: In research problems that involve the use of numerical methods for solving systems of ordinary differential equations (ODEs), it is often required to select the most efficient method for a particular problem. To solve a Cauchy problem for a system of ODEs, Runge--Kutta methods (explicit or implicit ones, with or without step-size control, etc.) are employed. In that case, it is required to search through many implementations of the numerical method and select coefficients or other parameters of its numerical scheme. This paper proposes a library and scripts for automated generation of routine functions in the Julia programming language for a set of numerical schemes of Runge--Kutta methods. For symbolic manipulations, we use a template substitution tool. The proposed approach to automated generation of program code allows us to use a single template for editing, instead of modifying each individual function to be compared. On the one hand, this provides universality in the implementation of a numerical scheme and, on the other hand, makes it possible to minimize the number of errors in the process of modifying the compared implementations of the numerical method. We consider Runge--Kutta methods without step-size control, embedded methods with step-size control, and Rosenbrock methods with step-size control. The program codes for the numerical schemes, which are generated automatically using the proposed library, are tested by solving numerically several well-known problems.
tags:
- article
- grant:rfbr:19-01-00645
- grant:rudn:5-100
- index:rinc
- index:scopus
- index:wos
- index-rank:wos:jcr:q4
- project:cas
- mine
- index-rank:scopus:sjr:q3
hugoblox:
  ids:
    doi: 10.1134/S0361768821010047

---
