---
title: $(a \land b)(a \lor b) = |ab|$
authors:
  - Julien Dubousquet
date: 12/14/2025
pid: 1765727106
tags:
  - PGCD
  - PPCM
---

**Montrer que $(a \land b)(a \lor b) = |ab|$**

---

Soient $(a,b)\in\Z^{2}$ fixés quelconques. Nous savons que

$$
\exists (a', b')\in\Z^{2} :
\begin{cases}
a = d a' \\
b = d b' \\
a' \land b' = 1
\end{cases}
\quad \text{où } d = a \land b.
$$

Observons alors que

$$
\begin{aligned}
(a \land b)(a \lor b)
&= (d a' \land d b')(d a' \lor d b') \\
&= d(\underbrace{a' \land b'}_{=1}) \times d(a' \lor b') \\
&= d^{2}(a' \lor b').
\end{aligned}
$$

Calculons $a' \lor b'$ :

- $a'b'$ est un multiple commun à $a'$ et $b'$, donc $a' \lor b' \mid a'b'$.
- $a' \lor b'$ est un multiple commun à $a'$ et $b'$, donc
  $$
  \left.
  \begin{array}{l}
  a' \land b' = 1 \\
  a' \mid a' \lor b' \\
  b' \mid a' \lor b'
  \end{array}
  \right\}
  \implies a'b' \mid a' \lor b'.
  $$

Ainsi, $a' \lor b'$ et $a'b'$ se divisent l’un l’autre, donc ils sont associés
(égaux ou opposés). Or $a' \lor b' \ge 0$, donc

$$
a' \lor b' = |a'b'|.
$$

Par conséquent,

$$
(a \land b)(a \lor b)
= d^{2}(a' \lor b')
= d^{2}|a'b'|
= |da' \times db'|
= |ab|.
$$
