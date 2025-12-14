---
title: Théorème de représentation de Riesz
authors:
  - Félix Rondeau
date: 05/24/2025
pid: 1748104231
tags:
  - espace euclidien
---

Si $(E,\scalar{\cdot}{\cdot})$ est un espace vectoriel euclidien, l’application

$$
    \chi : \applic{E}{E*}{x}{\applic{E}{\R}{y}{\scalar{x}{y}}}
$$

est un isomorphisme d’espaces vectoriels.

---

- $\chi$ est bien définie car pour tout $x \in E$, par linéairité du produit scalaire en sa seconde variable,

  $$
      \chi(x): \applic{R}{\R}{y}{\scalar x y}
  $$

  est une forme linéaire sur $E$.

- Soient $(x,x') \in E^{2}$ et $\lambda \in \R$. Pour tout $y \in E$,

  $$
      \begin{align*}
          \chi(x+\lambda x')(y) &= \scalar{x+\lambda x'}{y} \\
  &= \scalar x y + \lambda \times \scalar{x'}{y} \\
  &= \chi(x)(y) + \lambda \times \chi(x')(y) \\
  &= \left(\chi(x) + \lambda \chi(x')\right)(y)
      \end{align*}
  $$

  donc $\chi(x+\lambda x') = \chi(x) + \lambda \chi(x')$ ainsi $\chi$ est linéaire.

- Soit $x \in \Ker \chi$. Alors $\chi(x) = 0_{E*}$ donc

  $$
      \forall y \in T,\scalar x y = 0
  $$

  donc $x \in E\ortho = \{0_{E}\}$ d’où $x=0_{E}$. Ainsi, $\Ker  \chi \subset \{0_{E}\}$ et l’inclusion réciproque est immédiate, si bien que $\chi$ est injective.

- Nous savons que l’espace dual d’un espace de dimension finie est un espace de même dimension si bien que $\chi$ est une application linéaire injective entre deux espaces de même dimension finie, donc c’est un isomorphisme.
