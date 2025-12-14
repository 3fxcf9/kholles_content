---
title: Preuve des expressions de $a \land b$ et $a \lor b$ à partir des décompositions en facteurs premiers de a et b.
authors:
  - Julien Dubousquet
date: 12/14/2025
pid: 1765738836
tags:
  - PPCM
  - PGCD
---

Soient $(a,b) \in {\Z^*}^2$

$$
a \land b = \prod_{p \in \mathcal{P}}p^{min(\nu_p(a),\nu_p(b))}
$$

$$
a \lor b = \prod_{p \in \mathcal{P}}p^{max(\nu_p(a),\nu_p(b))}
$$

---

Posons $d = a \land b$

Soit $p \in \mathcal{P}$

$$
d = a \land b \implies 
\begin{cases} 
d \mid a \\ 
d \mid b 
\end{cases} 
\implies 
\begin{cases}
\nu_p(d) \leq \nu_p(a) \\ 
\nu_p(d) \leq \nu_p(b) 
\end{cases}
\implies \nu_p(d) \leq min(\nu_p(a),\nu_p(b)).
$$

Posons

$$
d' = \prod_{p \in \mathcal{P}}p^{min(\nu_p(a),\nu_p(b))}
$$

Nous avons prouvé que 

$$
\forall p \in \mathcal{P},\ \nu_p(d) \leq \nu_p(d')
$$

donc $d \mid d'$.

Par ailleurs, 

$$
\forall p \in \mathcal{P}, \ \nu_p(d') = min(\nu_p(a),\nu_p(b)) \leq \begin{cases}
\nu_p(a) \\ \nu_p(b)
\end{cases}
$$

donc $ d' \mid a$ et $d' \mid b$

donc $d' \mid a \wedge b$

donc $d' \mid d$

Ainsi, $|d|=|d'|$

Or $d>0$ et $d>'0$, donc $d=d'$.

$$
(a \land b)(a \lor b) = |ab|
$$

d'où 
$$
(a \lor b) \times \prod_{p \in \mathcal{P}}p^{min(\nu_p(a),\nu_p(b))} = |ab| = \prod_{p \in \mathcal{P}}p^{\nu_p(a) + \nu_p(b)}
$$

On a donc:

$$
a \lor b = \prod_{p \in \mathcal{P}}p^{\nu_p(a) + \nu_p(b)-min(\nu_p(a),\nu_p(b))} = \prod_{p \in \mathcal{P}}p^{max(\nu_p(a),\nu_p(b))}
$$

car $\forall (x,y) \in \R^2, \ min(x,y) + max(x,y) = x + y.$

*Remarque*:

Petite arnaque : il faudrait transformer les produits indexés par les nombres premiers, donc par un ensemble infini, en produits indexés par des ensembles finis pour les manipuler rigoureusement.