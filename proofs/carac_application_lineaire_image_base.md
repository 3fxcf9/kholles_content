---
title: Existence et unicité d’une application linéaire envoyant une base donnée de l’espace de départ sur une famille de vecteurs imposée
authors:
  - Félix Rondeau
date: 07/03/2025
pid: 1741353628
tags:
  - algèbre linéaire
---

Soient $I$ un ensemble, $E$ et $F$ deux $\K$-espaces vectoriels.

Il existe une unique application linéaire de $E$ dans $F$ qui envoie les éléments de la base $(e_{i})i\in I$ sur les vecteurs de la famille $(y_{i})i\in I$. De plus, cette application est

$$
f:\begin{array}{rcl}
    E & \longrightarrow & F\\
    \displaystyle\sum_{i\in I}\lambda_{i}\cdot e_{i} & \longmapsto & \displaystyle\sum_{i\in I}\lambda_{i}\cdot y_{i}
\end{array}
$$

---

- _Analyse :_ Soit $f\in\L_{\K}(E,F)$ telle que $\forall i\in I, f(e_{i})=k_{i}$. Soit $x\in E$ fixé quelconque. $(e_{i})_{i\in I}$ est une base de $E$ donc il existe une famille $(\lambda_{i})_{i\in I}\in \K^{(I)}$ telle que

  $$
      x = \sum_{i\in I}\lambda_{i}e_{i} \quad\text{donc}\quad f(x)=\sum_{i\in I}\lambda_{i} f(e_{i})=\sum_{i\in I}\lambda_{i}y_{i}
  $$

  Ainsi $f$ est nécessairement

  $$
  f:\begin{array}{rcl}
    E & \longrightarrow & F\\
    \displaystyle\sum_{i\in I}\lambda_{i}\cdot e_{i} & \longmapsto & \displaystyle\sum_{i\in I}\lambda_{i}\cdot y_{i}
  \end{array}
  $$

  (qui est bien définie car les coefficients $(\lambda_{i})_{i\in I}$ sont uniques car $(e_{i})_{i\in I}$ est une base de $E$).

- _Synthèse :_ Posons l’application

  $$
    f:\begin{array}{rcl}
      E & \longrightarrow & F\\
      \displaystyle\sum_{i\in I}\lambda_{i}\cdot e_{i} & \longmapsto & \displaystyle\sum_{i\in I}\lambda_{i}\cdot y_{i}
    \end{array}
  $$

  qui est bien définie car $(x_{i})_{i\in I}$ est une base de $E$, donc la famille $(\lambda_{i})_{i\in I}$ est unique.

  Soient $(x, x', \lambda)\in E^{2}\times \K$ fixés quelconques. Il existe deux familles de scalaires $(x_{i})_{i\in I}$ et $(x'_{i})_{i\in I}$ presques nulles telles que

  $$
      x=\sum_{i\in I}x_{i} e_{i} \quad\text{et}\quad  x'=\sum_{i\in I}x'_{i} e_{i}
  $$

  Alors,

  $$
  \begin{align*}
      f(\lambda x+x') &= f \left(\sum_{i\in I}(\lambda_{i} + x'_{i})e_{i}\right) \\
                      &= \sum_{i\in I}(\lambda x_{i} + x'_{i})y_{i} \\
                      &= \sum_{i\in I}(\lambda x_{i})y_{i} + \sum_{i\in I}x'_{i}y_{i} \\
                      &= \lambda \sum_{i\in I}x_{i} y_{i} + \sum_{i\in I}x'_{i}y_{i} \\
                      &= \lambda f(x)+f(y)
  \end{align*}
  $$

  Soit $i_{0}\in I$ fixé quelconque.

  $$
      f(e_{i}) = f(\sum_{i\in I}\delta_{i_{0} i} e_{i}) = \sum_{i\in I}\delta_{i_{0} i}y_{i} = \delta_{i_{0} i_{0}}y_{i_{0}} = y_{i_{0}}
  $$
