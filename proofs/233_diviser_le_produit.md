---
title: Si tous les entiers $a_1, \dots ,a_n$ divisent b et sont deux à deux premiers entre eux, alors leur produit divise b.
authors:
  - Julien Dubousquet
date: 12/14/2025
pid: 1765726727
tags:
  - Divisibilité
---

**Si $a \land c = b \land c = 1$ alors $ab \land c = 1$  
et généralisation au cas de $n$ entiers premiers avec un même entier**

---

Soient $p \in \N^*$ et $(a,b_1,\dots,b_p)\in\Z^{p+1}$, $p+1$ entiers fixés quelconques,
premiers entre eux deux à deux.

Le théorème d’existence d’une relation de Bézout assure que

$$
\forall i \in \{1,\dots,p\},\ \exists (u_i,v_i)\in\Z^2 \text{ tels que } au_i + b_i v_i = 1.
$$

Donc

$$
\forall i \in \{1,\dots,p\},\ \exists (u_i,v_i)\in\Z^2 \text{ tels que } b_i v_i = 1 - a u_i.
$$

En effectuant le produit membre à membre de ces $p$ égalités, on obtient

$$
\prod_{i=1}^{p} (b_i v_i) = \prod_{i=1}^{p} (1 - a u_i).
$$

En développant le membre de droite, il existe $U \in \Z$ tel que

$$
\prod_{i=1}^{p} (b_i v_i) = 1 - aU.
$$

En posant

$$
V = \prod_{i=1}^{p} v_i,
$$

on obtient

$$
\left(\prod_{i=1}^{p} b_i\right) V = 1 - aU.
$$

Ainsi, il existe deux entiers relatifs $U$ et $V$ tels que

$$
aU + \left(\prod_{i=1}^{p} b_i\right) V = 1.
$$

Le théorème caractérisant la propriété *« deux entiers sont premiers entre eux »*
par l’existence d’une relation de Bézout permet donc de conclure que

$$
a \land \left(\prod_{i=1}^{p} b_i\right) = 1.
$$
