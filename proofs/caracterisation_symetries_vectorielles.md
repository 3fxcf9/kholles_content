---
title: Caractérisation des symétries vectorielles
authors:
  - Félix Rondeau
date: 24/02/2025
pid: 1741353635
tags:
  - algèbre linéaire
---

Soit $f$ un endomorphisme de $E$. $f$ est une symétrie vectorielle si et seulement si

$$
    f^{2}=\Id_{E}
$$

De plus, si $f$ est une symétrie vectorielle, alors $f$ est la symétrie vectorielle par rapport à $\Ker(f-\Id_{E})$ et parallèlement à $\Ker(f+\Id_{E})$.

---

- $(\implies)$ Soit $f$ une symétrie vectorielle fixée quelconque. Alors il existe deux espaces vectoriels $E_{1}$ et $E_{2}$ supplémentaires dans $E$ tels que

  $$
        f=s_{E_{1}, E_{2}} : \begin{array}{rcccl}
            E &=& E_{1}\oplus E_{2} & \longrightarrow & E \\
            x &=& x_{1} + x_{2} & \longmapsto & x_{1}-x_{2}
        \end{array}
  $$

  Soit $x\in E$ fixé quelconque. $\exists !(x_{1}, x_{2})\in E_{1}\times E_{2}:\;x=x_{1}+x_{2}$.

  $$
      f^{2}(x)=f \big(f(x_{1}+x_{2})\big)=f(x_{1}-x_{2})=f(\underbrace{x_{1}}_{\in E_{1}} + \underbrace{-x_{2}}_{\in E_{2}})=x_{1}-(-x_{2})=x
  $$

  donc $f^{2}=\Id f$.

- $(\impliedby)$

  - *Étape 1* : montrons que $E=\Ker(f-\Id_{E})\oplus \Ker(f+\Id_{E})$.

    - _Analyse._ Soit $x\in E$ fixé quelconque. Supposons qu’il existe $(x_{+}, x_{-})\in\Ker(f-\Id_{E})\times \Ker(f+\Id_{E})$ tels que

    $$
        x=x_{+}+x_{-} \qquad (1)
    $$

    PRenons l’image de $(1)$ par $f$ :

    $$
        f(x)=f(x_{+})+f(x_{-}) = x_{+}-x_{-} \qquad (2)
    $$

    car pour tout $\alpha\in\K, z\in\Ker(f-\alpha \cdot \Id_{E}) \iff f(z)=\alpha \cdot z$. Ainsi, en effectuant des combinaisons linéaires :

    - $(1)+(2)$ donne $x+f(x)=2x_{+}$ donc $x_{+}=\dfrac{1}{2}(x+f(x))$
    - $(1)-(2)$ donne $x-f(x)=2x_{-}$ donc $x_{-}=\dfrac{1}{2}(x-(x))$
      Par conséquent, sous réserve d’existence, l’écriture $(1)$ est unique.

  - _Synthèse._ Soit $x\in E$ fixé quelconque. Posons

    $$
        x_{1}=\frac{1}{2}(x+f(\times)) = \frac{1}{2}(\Id_{E}+f)(x)
    $$

    et

    $$
      x_{2}=\frac{1}{2}(x-f(\times)) = \frac{1}{2}(\Id_{E}-f)(x)
    $$

    et observons que

    1. $x_{1}+x_{2} = \dfrac{1}{2}(x+fn(x)) + \dfrac{1}{2}(x-f(x)) = x$
    2. $(f-\Id_{E})(x_{1})=\left(\dfrac{1}{2}(\Id_{E}-f)\circ(\Id_{E}+f)\right)(x) = \left(\dfrac{1}{2}(\Id_{E}-f^{2})\right)(x) = 0_{E}$
    3. $(f+\Id_{E})(x_{2}) = \left(\dfrac{1}{2}(\Id_{E}+f)\circ (\Id_{E}-f)\right)(x) = \left(\dfrac{1}{2}(\Id_{E}-f^{2})\right)(x) = 0_{E}$

    Ainsi, tout vecteur de $E$ se décompose comme somme d’un vecteur de $\Ker(f-\Id_{E})$ et d’un vecteur de $\Ker(f+\Id_{E})$, donc $E=\Ker(f-\Id_{E})\oplus \Ker(f+\Id_{E})$.

- *Étape 2* : idientifions $f$. D’après la première étape, nous pouvons expliciter $f$ :

  $$
        f : \begin{array}{rcccl}
            E &=& \Ker(f-\Id_{E})\oplus \Ker(f+\Id_{E}) & \longrightarrow & E \\
            x &=& \dfrac{1}{2}(\Id_{E}+f)(x) + \dfrac{1}{2}(\Id_{E}-f)(x) & \longmapsto & f(x)=\dfrac{1}{2}(\Id_{E}+f)(x) - \dfrac{1}{2}(\Id_{E}-f)(x)
        \end{array}
  $$

  si bien que $f=s_{\Ker(f-\Id_{E}), \Ker(f+\Id_{E})}$.
