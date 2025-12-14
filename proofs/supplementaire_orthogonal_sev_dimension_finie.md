---
title: Supplémentaire orthogonal d’un sous-espace vectoriel de dimension finie
authors:
  - Félix Rondeau
date: 25/05/2025
pid: 1748172203
tags:
  - espaces préhilbertiens
  - orthogonalité
---

Si $F$ est un sous-espace vectoriel de dimension finie d’un espace préhilbertien réel $(E,\scalar{\cdot }{\cdot })$, alors $F\perp$ est son supplémentaire orthogonal.

On en déduit l’expression explicite du projeté orthogonal sur le sous-espace vectoriel $F$ (dont une BON est $(e_{1}, \ldots, e_{r})$) d’un espace euclidien.

---

Fixons $(e_{1}, \ldots, e_{r})$ une BON de $F$ ce qui est possible car $F$, muni du produit scalaire induit par le produit scalaire de $E$ est un espace euclidien.

- **Analyse.** Soit $x \in  E$. Supposons qu’il existe $(x_{\parallel}, x_{\perp}) \in F \times F\ortho$ tels que $x = x_{\parallel} + x_{\perp}$. Décomposons $x_{\parallel}$ dans la BON fixée :

  $$
      \exists (\lambda_{1}, \ldots, \lambda_{r}) \in \R^{r}: x_{\parallel} = \sum_{i=1}^{r}\lambda_{i}e_{i}
  $$

  Pour tout $j \in \icc{1,r}$,

  $$
  \begin{align*}
    \scalar x {e_{j}} &= \scalar{x_{\parallel}+x_{\perp}}{e_{j}}\\
  &= \scalar{\sum_{i=1}^{r}\lambda_{i}e_{i}}{e_{j}} + \underbrace{\scalar{x_{\perp}}{e_{j}}}_{=0}\\
  &= \sum_{i=1}^{r}\lambda_{i}\scalar{e_{i}}{e_{j}} = \lambda_{j}
  \end{align*}
  $$

  donc $x_{\parallel} = \sum_{i=1}^{r}\scalar{x}{e_{i}}e_{i}$ est unique, donc

  $$
      x_{\perp} = x - x_{\parallel} = x - \sum_{i=1}^{r}\scalar{x}{e_{i}}e_{i}
  $$

  est unique.

- **Synthèse.** Soit $x \in E$. Posons

  $$
      x_{\parallel} = \sum_{i=1}^{r}\scalar{x}{e_{i}}e_{i} \quad\text{et}\quad x_{\perp} = x-\sum_{i=1}^{r}\scalar{x}{e_{i}}e_{i}
  $$

  On a

  - $x_{\parallel} \in F$ comme combinaison linéaire de vecteurs de $F$,
  - $x_{\perp} + x_{\parallel} = x$
  - Pour tout $j \in \icc{1,r}$,

  $$
      \begin{align*}
          \scalar{x_{\perp}}{e_{j}} &= \scalar{x-\sum_{i=1}^{r}\scalar{x}{e_{i}}e_{i}}{e_{j}} \\
  &= \scalar{x}{e_{j}} - \sum_{i=1}^{r}\scalar{x}{e_{i}}\underbrace{\scalar{e_{i}}{e_{j}}}_{=\delta_{i,j}} = 0
      \end{align*}
  $$

  donc

  $$
      x_{\perp} \in \{e_{1}, \ldots, e_{r}\}\ortho = \left(\Vect\left\{e_{1}, \ldots, e_{r}\right\}\right)\ortho = F\ortho
  $$

Ainsi, $F$ et $F\ortho$ sont orthogonaux.

