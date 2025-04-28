---
title: Expression des coefficients associés à un pôle double dans une décomposition en éléments simples
authors:
  - Félix Rondeau
date: 04/16/2025
pid: 1744798590
tags:
  - fractions rationnelles
  - DES
---

Le coefficient du terme $\frac{a_{1,1}}{X-a}$ de la décomposition en éléments simples de la fraction irréductible $F=\frac{P_{0}}{Q_{0}}$ dont $a$ est un pôle double est

$$
    a_{1,1} = \left(\frac{P_{0}}{H}\right)' (a)
$$

et celui du terme $\frac{a_{1,2}}{(X-a)^{2}}$ est

$$
    a_{1,2} = \frac{P_{0}(a)}{H(a)}
$$

avec

$$
    H = \frac{Q_{0}}{X-a}
$$

---

- Comme $a$ est un pôle double de $F$ (racine de multiplicité 2 de $Q_{0}$), il existe $H \in \C[X]$ tel que

  $$
    H(a) \neq 0 \quad\text{et}\quad Q_{0} = (X-a)^{2}H
  $$

  D’après le théorème de décomposition en élément simple, $F$ se décompose dans $\C(X)$ sous la forme

  $$
      \frac{P_{0}}{Q_{0}} = \frac{P_{0}}{(X-a)} + \frac{a_{1,2}}{(X-a)^{2}} + F_{1}
  $$

  avec $F_{0} \in \C(X)$ n’admettant pas $a$ comme pôle.

  En multipliant cette relation par $(X-a)^{2}$, on obtient l’égalité

  $$
      \frac{P_{0}}{H} = a_{1,1}(X-a) + a_{1,2} + (X-a)^{2}F_{1} \qquad (*)
  $$

  dans laquelle $a$ n’est pôle d’aucune fraction rationnelle.

  Il est ainsi possible d’en prendre l’image par le morphisme d’évaluation en $a$, pour obtenir

  $$
      \frac{P_{0}(a)}{H(a)} = 0 + a_{1,1} + 0
  $$

  d’où l’expression de $a_{1,1}$.

- Dérivons l’égalité $(*)$ pour obtenir

  $$
      \left(\frac{P_{0}}{H}\right)' = a_{1,1} + 0 + 2(X-a)F_{1} + (X-a)^{2}F_{1}'
  $$

  qui donne, évaluée en $a$ (licite car $a$ n’étant pas pôle de $F$, il n’est pas pôle de sa dérivée) donne l’expression recherchée.
