---
title: Description explicite du sous-espace vectoriel engendré par une partie.
authors:
  - Félix Rondeau
date: 24/02/2025
pid: 1740414408
tags:
  - algèbre linéaire
---

Le sous-espace vectoriel engendré dane $E$ par la famille $(a_{i})_{i\in I}$ est

$$
    \Vect_{E}\{a_{i} \mid i\in I\} = \left\{\sum_{i\in I}\lambda_{i}a_{i} \;\middle |\; (\lambda_{i})_{i\in I}\in\K^{(I)}\right\}
$$

On note cet ensemble $W$ pour la démonstration.

---

- _Inclusion directe_:

  - _$W$ est un sous-espace vectoriel de $E$._

    - $W \subset E$ et $E$ est un $\K$-espace vectoriel.
    - $W \neq \emptyset$ car $0_E \in W$ (pour $(\lambda_i)_{i \in I} \leftarrow (O_\K)_{i \in I}$).
    - Soient $(x,y) \in W^2$ et $\lambda \in \K$ fixé quelconque. Il existe $(\lambda_i)$ et $(\mu_i)$, deux familles presque nulles de $\K$, telles que

      $$
      x = \sum_{i \in I} \lambda_i \, a_i \quad \text{et} \quad y = \sum_{i \in I} \mu_i \, a_i
      $$

      Ainsi,

      $$
      \lambda x + y = \sum_{i \in I} \underbrace{(\lambda \times \lambda_i + \mu_i)}_{\in \K} \cdot a_i \in W
      $$

  - $W$ contient $\{a_i \mid i \in I\}$ : Soit $i_0 \in I$ fixé quelconque. Pour $(\lambda_i) \leftarrow (\delta_{i_0, i})$ (autorisé car $\mathrm{supp}\;(\delta_{i_0, i}) = \{i_0\}$ est fini),

    $$
    a_{i_0} = \sum_{i \in I} \delta_{i_0, i} \, a_i \in W
    $$

  Ainsi, $W$ appartient à l’ensemble des sous-espaces vectoriels de $E$ contenant $\{a_{i} \mid i\in I\}$ donc $\Vect \{a_{i} \mid i\in I\} \subset W$ comme plus petit élément de cet ensemble.

- _Inclusion réciproque_: Soit $x \in W$ fixé quelconque. Il existe une famille $(\lambda_i)$ presque nulle de scalaires telle que
  $$
  x = \sum_{i \in I} \lambda_i \, a_i \in \Vect\{a_i \mid i \in I\}
  $$
  car $x$ est une combinaison linéaire de vecteurs de $\{a_i \mid i \in I\}$, donc de vecteurs de $\Vect\{a_i \mid i \in I\}$, et ainsi $\Vect\{a_i \mid i \in I\}$ est un sous-espace vectoriel de $E$.

Ainsi, nous avons l’égalité recherchée.
