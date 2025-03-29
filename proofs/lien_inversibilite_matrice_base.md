---
title: Lien entre base et inversibilité d’une matrice
authors:
  - Félix Rondeau
date: 29/03/2025
pid: 1743272903
tags:
  - algèbre linéaire
  - matrices
---

Une famille $(h_{1}, \ldots, h_{d})$ de vecteurs d’un espace vectoriel $H$ de dimension finie $d \in \N^{*}$ est une base si et seulement si la matrice de ces vecteurs dans une base quelconque est inversible.

---

- Supposons que la famille $(h_{1}, \ldots, h_{d})$ est une base de $H$. Fixons une base $\B$ de $H$ quelconque. Considérons l’application linéaire $u$ définie de $\K^{d}$ dans $H$ par

  $$
      \forall j \in \iset{1,d}, u(e_{j})=h_{j}
  $$

  où $e_{1}, \ldots, e_{d}$ sont les vecteurs de la base canonique de $\K^{d}$, notée $\B_{c}$.

  La matrice de $u$ relativement à la base $\B_{c}$ au départ et à la base $\B$ à l’arrivée est

  $$
      \begin{align*}
          \mat(u,\B_{c},\B) &= \mat((u(e_{1}), \ldots, u(e_{d})), \B) \\
  &= \mat((h_{1}, \ldots, h_{d}),\B)
      \end{align*}
  $$

  De plus, par définition de $u$, l’image de la base $\B_{c}$ est la base $(h_{1}, \ldots, h_{d})$ donc $u \in \GL_{\K}(\K^{d},H)$ si bien que $\mat(u,\B_{c},\B) \in \GL_{d}(\K)$ donc $\mat((h_{1}, \ldots, h_{d}), \B) \in \GL_{d}(\K)$

- Soit $\B=(b_{1}, \ldots, b_{d})$ une base de $H$ telle que $\mat((h_{1}, \ldots, h_{d}),\B) \in \GL_{d}(\K)$.

  Considérons l’application linéaire $u$ définie de $\K^{d}$ dans $H$ par

  $$
      \forall j \in \iset{1,d}, u(e_{j}) = h_{j}
  $$

  où $e_{1}, \ldots, e_{d}$ sont les vecteurs de la base canonique de $\K^{d}$, notée $\B_{c}$.

  La matrice de $u$ relativement à la base $\B_{c}$ au départ et à la base $\B$ à l’arrivée est

  $$
      \mat(u,\B_{c}, \B) = \mat((h_{1}, \ldots, h_{d}), \B)
  $$

  Par hypothèse, $\mat((h_{1}, \ldots, h_{d}), \B) \in \GL_{d}(\K)$ donc $u$ est un isomorphisme de $\K^{d}$ dans $H$ si bien que l’image de toute base de $\K^{d}$ est une base de $H$ donc $(h_{1}, \ldots, h_{d}) = (u(e_{1}), \ldots, u(e_{d}))=u(\B_{c})$ est une base de $H$.
