---
title: Théorème des suites adjacentes.
authors:
  - Julien Dubousquet
date: 07/12/2025
pid: 1765121385
tags:
  - Limites de suites
---

**Énoncé.**
Soient $u$ et $v$ deux suites réelles adjacentes. Alors $u$ et $v$ convergent et ont la même limite.

---

Soient $u$ et $v$ deux suites adjacentes. Quitte à échanger leurs rôles, supposons que $u$ est croissante et que $v$ est décroissante.

On a alors :
$$
\forall n \in \N,\quad
(u_n \le v_n \le v_0) \ \wedge\ (u_0 \le u_n \le v_n),
$$
car la monotonie implique ces inégalités.

D'après le théorème de convergence monotone :

* $u$ est croissante et majorée, donc elle converge ;
* $v$ est décroissante et minorée, donc elle converge.

Par définition des suites adjacentes, on a :
$$
0 = \lim_{n\to+\infty}(u_n - v_n)
= \lim_{n\to+\infty} u_n ;-; \lim_{n\to+\infty} v_n.
$$

Ainsi,
$$
\lim u = \lim v.
$$
