---
title: Preuve de la caractérisation de la densité avec des $\varepsilon$.
authors:
  - Julien Dubousquet
date: 11/22/2025
pid: 1763852335
tags:
  - Réels
---

---

Soient $(A,B)\in\mathcal{P}(\mathbb{R})^2$ fixés.

**Définition.**  
$A$ est dense dans $B$ si
- $A\subset B$, et
- $\forall (u,v)\in\mathbb{R}^2,\quad B\cap {]}u;v{[}\neq\varnothing \implies A\cap {]}u;v{[}\neq\varnothing$.

**Caractérisation par les $\varepsilon$.** On montre l'équivalence
$$
A\text{ est dense dans }B
\iff
\begin{cases}
A\subset B,\\[2pt]
\forall b\in B,\ \forall\varepsilon\in\mathbb{R}_+^*,\ \exists a\in A:\ |b-a|<\varepsilon.
\end{cases}
$$

---

### Sens direct.  
Supposons $A$ dense dans $B$.

- Par définition $A\subset B$.

- Soit $b\in B$ et $\varepsilon>0$. Posons $u=b-\varepsilon$ et $v=b+\varepsilon$.  
  Alors $B\cap {]}b-\varepsilon,b+\varepsilon{[}\neq\varnothing$ (car $b$ appartient à cette intersection), donc par densité $A\cap {]}b-\varepsilon,b+\varepsilon{[}\neq\varnothing$.  
  On peut donc choisir $a\in A$ tel que $a\in {]}b-\varepsilon,b+\varepsilon{[}$, ce qui équivaut à $|b-a|<\varepsilon$.

---

### Sens réciproque.  
Supposons
$$
A\subset B
\quad\text{et}\quad
\forall b\in B,\ \forall\varepsilon>0,\ \exists a\in A:\ |b-a|<\varepsilon.
$$

Montrons que $A$ est dense dans $B$. Soient $u<v$ tels que $B\cap {]}u,v{[}\neq\varnothing$.  
Choisissons $b\in B\cap {]}u,v{[}$. Posons $\varepsilon=\min\{v-b,\; b-u\}>0$. Par hypothèse il existe $a\in A$ avec $|b-a|<\varepsilon$, donc
$$
b-\varepsilon < a < b+\varepsilon.
$$
Comme $\varepsilon\le v-b$ et $\varepsilon\le b-u$ on obtient
$$
a < b+\varepsilon \le b+(v-b)=v
\quad\text{et}\quad
a > b-\varepsilon \ge b-(b-u)=u,
$$
donc $a\in {]}u,v{[}$. Ainsi $A\cap {]}u,v{[}\neq\varnothing$.

---

Conclusion : les deux formulations sont équivalentes.
