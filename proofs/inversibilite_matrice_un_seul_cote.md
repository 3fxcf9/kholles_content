---
title: Caractérisation de l’inversibilité des matrices carrées
authors:
  - Félix Rondeau
date: 22/03/2025
pid: 1742662333
tags:
  - algèbre linéaire
  - matrices
---

Si il existe un inverse à droite (resp. à gauche) pour une matrices carrée, alors elle est inversible et son inverse est cet inverse à droite (resp. à gauche).

---

Supposons qu’il existe $B \in \M_{n}(\K)$ telle que $AB=I_{n}$ ou $BA = I_{n}$. Notons $\hat{a}$ et $\hat{b}$ les endomorphismes de $\K^{n}$ canoniquement associés à $A$ et $B$. On a donc

$$
    \mat(\hat{a}, \B_{c,\K^{n}}) = A
$$

et

$$
    \mat(\hat{b}, \B_{c,\K^{n}}) = B
$$

- Si $AB=I_{n}$, on a

  $$
      \mat(\hat{a}, \B_{c,\K^{n}})\mat(\hat{b}, \B_{c,\K^{n}}) = I_{n}
  $$

  donc

  $$
      \mat(\hat{a}\circ\hat{b},\B_{c,\K^{n}}) = I_{n} = \mat(\Id_{\K^{n}}, \B_{c,\K^{n}})
  $$

  soit aussi

  $$
      \Phi_{\B_{c,\K^{n}}}(\hat{a}\circ\hat{b}) = \Phi_{\B_{c,\K^{n}}}(\Id_{\K^{n}})
  $$

  donc par injectivité de $\Phi$, $\hat{a}\circ\hat{b} = \Id_{\K^{n}}$. Cette relation nous assure que $\hat{a}$ est surjective et donc un automorphisme (accident de la dimension finie). Par conséquent, pour toute base $\B$ de $\K^{n}$, $\mat(\hat{a}, \B) \in \GLM_{n}(\K)$ si bien qu’en particulier pour $\B\leftarrow \B_{c,\K^{n}}$,

  $$
      A = \mat(\hat{a}, \B_{c,\K^{n}})\in \GLM_{n}(\K)
  $$

- Si $BA=I_{n}$, on montre de même la bijectivité de $\hat{b}\circ\hat{a}$ et donc celle de $\hat{a}$ grace à l’accident de la dimension finie. On conclut alors comme dans le premier cas.

Ainsi, dans les deux cas, nous avons montré que $A \in \GLM_{n}(\K)$, si bien qu’en multipliant par l’inverse de $A$ à droite ou à gauche selon le cas, on obtient $B=A^{-1}$.
