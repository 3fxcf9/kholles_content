---
title: Régularité d’une fonction définie par une intégrale
authors:
  - Félix Rondeau
date: 09/05/2025
pid: 1746817056
tags:
  - intégration
---

Soient $f \in \Cont^{0}(I,\C)$ et $(\alpha, \beta) \in \Diff^{1}(J,I)^{2}$.Alors la fonction

$$
    h: \applic{J}{\C}{x}{\displaystyle\int_{\alpha(x)}^{\beta(x)}f(u)\dd u}
$$

est dérivable sur $J$ et sa dérivée est

$$
    \forall x \in J, h'(x) = \beta'(x)f(\beta(x)) - \alpha'(x)f(\alpha(x))
$$

---

- Pour tout $x \in J$, $\alpha(x) \in I$ et $\beta(x) \in I$, donc $f$ étant continue sur $I$, elle est continue sur l’intervalle d’extrémités $\alpha(x)$ et $\beta(x)$ si bien que $h(x)$ est définie.

- $f$ est continue sur $I$ donc $f$ admet une primitive notée $F$ définie sur $I$. Par conséquent,

  $$
      \begin{align*}
          \forall x \in J, h(x) &= \int_{\alpha(x)}^{\beta(x)}f(u)\dd u \\
  &= \bigl[F(u)\bigr]_{\alpha(x)}^{\beta(x)} \\
  &= (F\circ \beta)(x) - (F\circ \alpha)(x)
      \end{align*}
  $$

  d’où l’expression de sa dérivée.

