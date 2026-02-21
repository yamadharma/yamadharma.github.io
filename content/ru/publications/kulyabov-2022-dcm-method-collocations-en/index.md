---
title: Multistage pseudo-spectral method (method of collocations) for the approximate solution of an ordinary differential equation of the first order
authors:
- Konstantin Petrovich Lovetskiy
- Dmitry Sergeevich Kulyabov
- Ali Weddeye Hissein
date: '2022-05-01'
publishDate: '2026-01-23T13:43:24.537268Z'
publication_types:
- article-journal
publication: '*Discrete and Continuous Models and Applied Computational Science*'
abstract: The classical pseudospectral collocation method based on the expansion of the solution in a basis of Chebyshev polynomials is considered. A new approach to constructing systems of linear algebraic equations for solving ordinary differential equations with variable coefficients and with initial (and/or boundary) conditions makes possible a significant simplification of the structure of matrices, reducing it to a diagonal form. The solution of the system is reduced to multiplying the matrix of values of the Chebyshev polynomials on the selected collocation grid by the vector of values of the function describing the given derivative at the collocation points. The subsequent multiplication of the obtained vector by the two-diagonal spectral matrix, ‘inverse’ with respect to the Chebyshev differentiation matrix, yields all the expansion coefficients of the sought solution except for the first one. This first coefficient is determined at the second stage based on a given initial (and/or boundary) condition. The novelty of the approach is to first select a class (set) of functions that satisfy the differential equation, using a stable and computationally simple method of interpolation (collocation) of the derivative of the future solution. Then the coefficients (except for the first one) of the expansion of the future solution are determined in terms of the calculated expansion coefficients of the derivative using the integration matrix. Finally, from this set of solutions only those that correspond to the given initial conditions are selected.
tags:
- category:numerical
- index:rinc
- index:vak
- mine
- index:scopus
hugoblox:
  ids:
    doi: 10.22363/2658-4670-2022-30-2-127-138

---
