---
title: Montrer qu'une suite décroissante et minorée de nombres entiers relatifs est stationnaire.
authors:
  - Julien Dubousquet
date: 11/22/2025
pid: 1763851326
tags:
  - Suite
---

---

Soit $u \in \mathbb{Z}^\mathbb{N}$ une suite décroissante et minorée fixée quelconque.  

Considérons 
$$
A = \{ u_n \mid n \in \mathbb{N} \},
$$
c'est-à-dire l'ensemble des valeurs prises par la suite $u$.  

$A$ est :  
- une partie de $\mathbb{Z}$ car $u$ est à valeurs dans $\mathbb{Z}$  
- non vide car $u_0 \in A$  
- minoré car $u$ est minorée  

Donc $A$ admet un plus petit élément. Donc il existe $n_0 \in \mathbb{N}$ tel que 
$$
u_{n_0} = \min A.
$$
Fixons un tel $n_0$.  

Soit $n \in \mathbb{N}$ tel que $n \ge n_0$. Alors
$$
\begin{cases}
u_n \in A \implies u_n \ge \min A = u_{n_0} \\
u \text{ est décroissante et } n \ge n_0 \implies u_n \le u_{n_0}
\end{cases}
\implies u_n = u_{n_0}.
$$

Ainsi, $u$ est stationnaire.

