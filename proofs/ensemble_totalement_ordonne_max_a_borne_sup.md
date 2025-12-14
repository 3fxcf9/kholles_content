---
title: Montrer que dans un ensemble totalement ordonné (E,≤), une partie A possède un plus grand élément si et seulement si la partie A admet une borne supérieure qui appartient à la partie A. De plus, dans ce cas, maxA=supA.
authors:
  - Julien Dubousquet
date: 11/22/2025
pid: 1763850375
tags:
  - Réels
---



---

### • Sens 1 : si $\sup A \in A$, alors $A$ possède un plus grand élément

Par définition, $\sup A \in M(A)$ signifie :

$$
\forall a\in A,\quad a \preccurlyeq \sup A.
$$

Donc $\sup A$ majore tous les éléments de $A$ et appartient à $A$.  
Ainsi, $A$ admet un pge et :

$$
\max A = \sup A.
$$

---

### • Sens 2 : si $A$ admet un plus grand élément, alors $\sup A$ existe et vaut $\max A$

Supposons que $A$ admet un plus grand élément, noté $\max A$. Alors :

$$
\forall a\in A,\quad a \preccurlyeq \max A
\qquad\text{et}\qquad
\max A \in A.
$$

Soit $M\in M(A)$ une borne supérieure quelconque de $A$ :

$$
\forall a\in A,\quad a\preccurlyeq M.
$$

En particulier, pour $a = \max A$ (autorisé car $\max A \in A$), on obtient :

$$
\max A \preccurlyeq M.
$$

Comme de plus $\max A\in M(A)$, cela montre que $\max A$ est la plus petite des bornes supérieures :

$$
\max A = \min M(A).
$$

Donc $A$ admet une borne supérieure et :

$$
\sup A = \max A.
$$
