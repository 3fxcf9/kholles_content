---
title: Caractérisation des projecteurs vectoriels
authors:
  - Félix Rondeau
date: 24/02/2025
pid: 1741353634
tags:
  - algèbre linéaire
---

Soit $f$ un endomorphisme de $E$. $f$ est un projecteur vectoriel si et seulement si

$$
    f^{2}=f
$$

De plus, si $f$ est une projection vectorielle, alors $f$ est la projection vectorielle sur $\Imf f$ parallèlement à $\Ker f$.

---

- $(\implies )$ Soit $f$ un projecteur fixé quelconque. Alprs il existe deux espaces vectoriels $E_{1}$ et $E_{2}$ supplémentaires dans $E$ tels que

  $$
      f=p_{E_{1}, E_{2}} : \begin{array}{rcccl}
          E &=& E_{1}\oplus E_{2} & \longrightarrow & E \\
          x &=& x_{1} + x_{2} & \longmapsto & x_{1}
      \end{array}
  $$

  Soit $x\in E$ fixé quelconque.

  $$
      \exists !(x_{1}, x_{2})\in E_{1} \times E_{2} : \; x=x_{1}+x_{2}
  $$

  Alors

  $$
      f^{2}(x) = f(f(x_{1}+x_{2})) = f(x_{1}) = f(\underbrace{x_{1}}_{\in E_{1}} + \underbrace{0_{E}}_{\in E_{2}}) = x_{1} = f(x)
  $$

  donc $f^{2}=f$.

- $(\impliedby)$

  - *Étape 1* : montrons que $E=\Imf f\oplus \Ker f$.

    - _Analyse._ Soit $x\in E$ fixé quelconque. Supposons qu’il existe $(x_{I}, x_{K})\in \Imf f \times \Ker f$ tels que

      $$
          x=x_{I}+x_{K} \qquad (1)
      $$

      $x_{I}\in\Imf f$ donc $\exists x'_{I}\in E: \; f(x'_{I})=x_{I}$ d’où

      $$
          x=f(x'_{I})+x_{K} \qquad (2)
      $$

      Prenons l’image de $(2)$ par $f$ :

      $$
          f(x) = \underbrace{f^{2}(x'_{I})}_{=f(x'_{I})} + \underbrace{f(x_{K})}_{=0_{E}} = f(x'_{I})
      $$

      donc

      $$
          f(x) = x_{I}
      $$

      Ainsi, $x_{I} = f(x)$ donc en reportant dans $(1)$, on obtient

      $$
          x_{K} = x-f(x)
      $$

      Par conséquent, sous Réserve d’existence, l’écriture $(1)$ est unique.

    - _Synthèse._ Soit $x\in E$ fixé quelconque. Posons

      - $x_{1}=f(x)$
      - $x_{2}=x-f(x) = (\Id_{E}-f)(x)$

      et observons que

      1. $x_{1} + x_{2} = f(x) + x - f(x) = x$
      2. $x_{1} = f(x)$ donc $x_{1}\in \Imf f$
      3. $f(x_{2}) = f \big((\Id_{E}-f)(x)\big)=\big(f\circ (\Id_{E}-f)\big)(x)=(f^{2}-f)(x)=0_{E}$ donc $x_{2}\in\Ker f$

      Ainsi, tout vecteur de $E$ se décompose comme somme d’un vecteur de $\Imf f$ et d’un vecteur de $\Ker f$ donc $E=\Imf f \oplus \Ker f$.

  - *Étape 2* : identifions $f$.
    D’après la première étape, nous pouvons expliciter $f$ :

    $$
      f : \begin{array}{rcccl}
          E &=& \Imf f \oplus \Ker f & \longrightarrow & E \\
          x &=& f(x) + x-f(x) & \longmapsto & f(x)
      \end{array}
    $$
