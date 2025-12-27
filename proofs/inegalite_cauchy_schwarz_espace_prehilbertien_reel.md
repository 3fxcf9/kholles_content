---
title: Inégalité de Cauchy-Schwarz dans un espace préhilbertien réel
authors:
  - Félix Rondeau
date: 24/05/2025
pid: 1748102589
tags:
  - espaces préhilbertiens
---

Si $(E,\scalar{\cdot}{\cdot})$ est un espace préhilbertien réel, alors pour tous $(x,y) \in E$,

$$
    \abs{\scalar{x}{y}} \leq \norm{x} \times \norm{y}
$$

avec égalité si et seulement si $x$ et $y$ sont liés.

---

#### Preuve de l’égalité

Posons

$$
    f: \applic{\R}{\R}{t}{\scalar{x+ty}{x+ty}}
$$

Alors, pour tout $t \in \R$,

$$
\begin{align*}
    f(t) = \scalar{x}{x} + t\scalar{y}{x} + t\scalar{x}{y} + t^{2}\scalar{y}{y} \\
\end{align*}
$$

donc $f$ est une fonction polynomiale de degré inférieur ou égal à 2.

- si $\norm y \neq 0$, $f$ est un trinôme du second degré de signe constant, donc de discriminant négatif, soit

  $$
      \left(\cancel{2}\scalar{x}{y}\right)^{2} - \cancel{4}\norm{x}^{2}\cdot \norm{y}^{2}\leq 0
  $$

  donc, par croissance de la fonction racine carrée,

  $$
      \abs{\scalar{x}{y}} \leq \norm x \cdot \norm y
  $$

- sinon, $\norm{y} = 0$ donc par propriété du produit scalaire, $y=0$. Ainsi,

  $$
      \abs{\scalar x y} = \abs{\scalar x 0} = 0
  $$

  d’où l’inégalité.

#### Caractérisation du cas d’égalité

- Supposons que $x$ et $y$ réalisent un cas d’égalité.

  - si $y = 0$, alors la famille $(x,y)$ est liée.

    d’où l’égalité.

  - sinon, en reprenant les notations de la preuve de l’inégalité, $f$ est un trinôme du second degré de discrimant nul, i.e.

    $$
        4 \left\{\scalar x y\right\}^{2}  - 4\norm{x}^{2} \cdot \norm{y}^{2} = 0
    $$

  donc $f$ admet une racine réelle (double) $t_{0}$, donc $\norm{x+t_{0}y} = 0$, donc $\scalar{x+t_{0}y}{x+t_{0}y} = 0$, soit $1x + t_{0}y = 0$, d’où la liaison de la famille $(x,y)$.

- Supposons la famille $(x,y)$ liée.

  - si $y = 0$, les deux membres sont nuls donc il y a bien égalité.
  - sinon, $y\neq 0$ donc il existe $\lambda \in \R$ tel que $x = \lambda y$. Alors d’une part

    $$
        \abs{\scalar x y} = \abs{\scalar{\lambda y} y} = \abs{\lambda} \abs{\scalar y y} = \abs{\lambda}\norm{y}^{2}
    $$

    et d’autre part

    $$
        \norm x \cdot \norm y = \sqrt{\scalar{\lambda y}{\lambda y}}\cdot \norm y = \sqrt{\lambda^{2} \norm{y}^{2}} = \abs{\lambda}\cdot \norm{y}^{2}
    $$
