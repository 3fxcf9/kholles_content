---
title: Expressions du coefficient associé à un pôle simple dans une décomposition en éléments simples
authors:
  - Félix Rondeau
date: 16/04/2025
pid: 1744797235
tags:
  - fractions rationnelles
  - DES
---

Le coefficient du terme $\frac{a_{1,1}}{X-a}$ de la décomposition en éléments simples de la fraction irréductible $F=\frac{P_{0}}{Q_{0}}$ dont $a$ est un pôle simple est

$$
    a_{1,1} = \frac{P_{0}(a)}{H(a)} = \frac{P_{0}(a)}{Q_{0}'(a)}
$$

où

$$
    H = \frac{Q_{0}}{X-a}
$$

---

- Comme $a$ est un pôle simple de $F$, il existe $H \in \C[X]$ tel que

  $$
    H(a) \neq 0 \quad\text{et}\quad Q_{0} = (X-a)H
  $$

  D’après le théorème de décomposition en élément simple, $F$ se décompose dans $\C(X)$ sous la forme

  $$
      \frac{P_{0}}{Q_{0}} = \frac{P_{0}}{(X-a)H} = \frac{a_{1,1}}{X-a} + F_{0}
  $$

  avec $F_{0} \in \C(X)$ n’admettant pas $a$ comme pôle.

  En multipliant cette relation par $X-a$, on obtient l’égalité

  $$
      \frac{P_{0}}{H} = a_{1,1} + (X-a)F_{0}
  $$

  dans laquelle $a$ n’est pôle d’aucune fraction rationnelle.

  Il est ainsi possible d’en prendre l’image par le morphisme d’évaluation en $a$, pour obtenir

  $$
      \frac{P_{0}(a)}{H(a)} = a_{1,1} + 0
  $$

  d’où la première expression.

- Dérivons l’égalité $Q_{0} = (X-a)H$ pour obtenir

  $$
      Q_{0}' = H+(X-a)H'
  $$

  qui donne, évaluée en $a$ la seconde expression recherchée.
