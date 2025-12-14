---
title: Montrer que si A et B sont deux parties non vides majorées de $\mathbb{R}$, alors sup(A+B) = supA + supB.
authors:
  - Julien Dubousquet
date: 22/11/2025
pid: 1763851544
tags:
  - Borne sup
---

---

Soient $A$ et $B$ deux parties non vides et majorées de $\mathbb{R}$. On note $A+B$ l'ensemble

$$
A+B=\{\,a+b \mid (a,b)\in A\times B\,\}.
$$

C'est aussi une partie non vide de $\mathbb{R}$.

Soit $x\in A+B$ fixé. Par définition de $A+B$, il existe $(a,b)\in A\times B$ tel que $x=a+b$. Comme $a\le \sup A$ et $b\le \sup B$, on obtient

$$
x=a+b \le \sup A + \sup B,
$$

donc $\sup A + \sup B$ est un majorant de $A+B$. Ainsi, puisque $A+B$ est non vide et majorée, il admet une borne supérieure, la plus petite des majorants, et en particulier

$$
\sup(A+B) \le \sup A + \sup B.
$$

Réciproquement, $\sup(A+B)$ est un majorant de $A+B$, donc pour tout $(a,b)\in A\times B$ on a

$$
a+b \le \sup(A+B) \quad\Longrightarrow\quad a \le \sup(A+B)-b.
$$

En fixant $b\in B$ et en relâchant $a$, on obtient

$$
\forall a\in A,\quad a \le \sup(A+B)-b,
$$

donc $\sup(A+B)-b$ est un majorant de $A$. Par conséquent $\sup A \le \sup(A+B)-b$, ce qui donne

$$
b \le \sup(A+B)-\sup A.
$$

En relâchant le choix de $b$ (pour tout $b\in B$), on obtient que $\sup(A+B)-\sup A$ est un majorant de $B$, d'où

$$
\sup B \le \sup(A+B)-\sup A,
$$

soit

$$
\sup A + \sup B \le \sup(A+B).
$$

En combinant les deux inégalités précédentes, on conclut :

$$
\sup(A+B) = \sup A + \sup B.
$$
