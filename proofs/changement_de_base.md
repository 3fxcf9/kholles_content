---
title: Formule du changement de base
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743272905
tags:
  - algèbre linéaire
  - matrices
---

Soient $E$ et $F$ deux $\K$-espaces vectoriels de dimensions respectives $n$ et $p$ finies.
Soient $\B_{E}$, $\B_{E}'$ deux bases de $E$ et $\B_{F}$, $\B_{F}'$ deux bases de $F$.
Soit $u$ une application linéaire de $E$ dans $F$.

Notons

- $U = \mat(u,\B_{E}, \B_{F})$, $U'=\mat(u,\B_{E}', \B_{F}')$
- $P = \P(\B_{E}\rightarrow \B_{E}')$, $Q = \P(\B_{F} \rightarrow \B_{F}')$

Alors

$$
    U' = Q^{-1}UP
$$

En particulier, si $u$ est un endomorphisme, alors en notant $P = \mat(\B_{E} \rightarrow \B_{E}')$,

$$
    \mat(u, \B_{E}') = P^{-1}\mat(u,\B_{E})P
$$

(application de la formule précédente pour $\B_{F}\leftarrow \B_{E}$ et $\B_{F}'\leftarrow \B_{E}'$).

---

$$
    \begin{align*}
        Q^{-1}UP &= \mat(\Id_{F},\B_{F}',\B_{F})^{-1} \times \mat(u,\B_{E},\B_{F}) \times \mat(\Id_{E}, \B_{E}', \B_{E}) \\
                &= \mat(\Id_{F}, \B_{F}, \B_{F}')\times \mat(u,\B_{E},\B_{F}) \times \mat(\Id_{E}, \B_{E}', \B_{E}) \\
                &= \mat(\Id_{F}\circ u, \B_{E}, \B_{F}') \times \mat(\Id_{E}, \B_{E}',\B_{E}) \\
                &= \mat(u, \B_{E}, \B_{F}') \times \mat(\Id_{E}, \B_{E}',\B_{E}) \\
                &= \mat(u\circ\Id_{F}, \B_{E}', \B_{F}') \\
                &= \mat(u, \B_{E}', \B_{F}') \\
                &= U'
    \end{align*}
$$
