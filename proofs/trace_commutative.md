---
title: La trace d'un produit de deux matrices carrées est indépendante de l'ordre de multiplication
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743272906
tags:
  - algèbre linéaire
  - matrices
---

- Si $A$ et $B$ sont deux matrices carrées de taille $n$ à coefficients dans le corps $\K$, alors

  $$
      \tr(AB) = \tr(BA)
  $$

- Soient $\B$ et $\B'$ deux bases d’un $\K$-espace vectoriel $E$ de dimension finie et $u \in \L_{\K}(E)$.

  Notons $u=\mat(u,\B)$ et $U'=\mat(u,\B')$.
  Alors

  $$
      \tr(U') = \tr(U)
  $$

---

- Calculons

  $$
        \begin{align*}
            \tr(AB) &= \sum_{i=1}^{n}[A \times B]_{i,i} \\
    &= \sum_{i=1}^{n}\sum_{k=1}^{n}A_{i,k} \times B_{k,i} \\
    &= \sum_{k=1}^{n}\sum_{i=1}^{n}A_{i,k} \times  B_{k,i} \\
    &=\sum_{k=1}^{n}\sum_{i=1}^{n}B_{k,i}\times A_{i,k} \\
    &= \sum_{k=1}^{n}[B \times A]_{k,k} \\
    &= \tr(BA)
        \end{align*}
  $$

- Posons $P = \P(\B \rightarrow \B')$. La formule du changement de base donne $U'=P^{-1}UP$ si bien que

  $$
      \begin{align*}
          \tr(U) &= \tr(P^{-1}UP)\\
  &= \tr(P^{-1} \times UP)\\
  &= \tr(UP \times P^{-1}) \\
  &= \tr(U \underbrace{PP^{-1}}_{=I_{n}}) \\
  &= \tr(U)
      \end{align*}
  $$
