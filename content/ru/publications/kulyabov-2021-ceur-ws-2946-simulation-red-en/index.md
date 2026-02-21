---
title: Computer simulation of the stochastic RED algorithm
authors:
- Anna Maria Yurievna Apreutesey
- Anna Vladislavovna Korolkova
- Dmitry Sergeevich Kulyabov
date: '2021-04-01'
publishDate: '2026-01-23T13:43:24.248689Z'
publication_types:
- paper-conference
publication: '*Workshop on information technology and scientific computing in the framework of the XI International Conference Information and Telecommunication Technologies and Mathematical Modeling of High-Tech Systems (ITTMM-2021)*'
abstract: The purpose of this work is to study the capabilities of the Julia language for numerical modeling of stochastic systems. As a stochastic system we consider the model of interaction between the process of data transmission via the Transmission Control Protocol (TCP) and the process of regulating the flow state using the Random Early Detection (RED) algorithm. The mathematical model of this interaction is a system of stochastic differential equations, where there are both continuous and discrete elements of the model. When simulating such systems, it is important to consider the properties of continuous parameters, such as queue length of a router and the TCP window size, as well as discrete transitions between TCP states and the probabilistic packet drop function. Such hybrid systems can be quite easily implemented in specialized dynamic systems modeling languages, for example in Modelica. However, this software package does not have built-in universal tools for modeling stochastic systems, where it is important to consider the random nature of the behavior. The aim of this work is to find optimal tools for modeling such stochastic systems using the Julia language which in used for scientific calculations. For modeling the RED algorithm, the DifferentialEquations.jl library is used. This tool of the Julia language allows solving various kinds of differential equations, including stochastic differential equations and delay differential equations. As a result of the simulation graphs were obtained that demonstrate the dynamics of changes of the TCP window size and the queue length, depending on the initial model parameters and queue threshold values, the correct selection of which ensures the stable operation of the system.
tags:
- mine
- project:aqm
- grant:rfbr:19-01-00645
- grant:rudn:5-100
- index:scopus
hugoblox:
  links:
  - type: pdf
    url: http://ceur-ws.org/Vol-2946/paper-04.pdf

---
