---
title: Inversibilité d’une matrice de passage
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743272904
tags:
  - algèbre linéaire
  - matrices
---

Toute matrice de changement de base $\P(\B\rightarrow \B')$ est inversible et son inverse est $\P(\B'\rightarrow\B)$.

---

- $\P(\B\rightarrow\B')$ vue comme la matrice $\mat(\Id_{H}, \B',\B)$ de l’automorphisme identité est inversible
- Calculons

  $$
  \begin{align*}
      \P(\B\rightarrow\B')\times \P(\B'\rightarrow\B) &= \mat(\Id_{H}, \B',\B) \times  \mat(\Id_{H},\B,\B') \\
  &= \mat(\Id_{H} \circ \Id_{H},\B,\B) \\
  &= I_{n}
  \end{align*}
  $$

  si bien que $\P(\B'\rightarrow\B)$ est l’inverse de $\P(\B\rightarrow\B')$.
