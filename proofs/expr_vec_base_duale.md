---
title: Expression d’un vecteur et d’une application linéaire dans une base duale
authors:
  - Félix Rondeau
date: 22/03/2025
pid: 1742662330
tags:
  - algèbre linéaire
---

Soit $(e_{1}, \ldots, e_{n})$ une base d’un $\K$-espace vectoriel $E$ de dimension $n \in \N^{*}$. Alors tout vecteur $x$ de $E$ s’écrit

$$
    x = \sum_{i=1}^{n}e_{i}^{*}(x)\cdot e_{i}
$$

et toute forme linéaire de $E$ s’écrit

$$
    \varphi = \sum_{i=1}^{n}\varphi(e_{i})\cdot e_{i}^{*}
$$

---

- Soit $x \in E$ fixé quelconque. $(e_{1}, \ldots, e_{n})$ est une base de $E$ donc il existe $\lambda_{1}, \ldots, \lambda_{n}$ des scalaires tels que

  $$
      x=\sum_{i=1}^{n}\lambda_{i}\cdot e_{i}
  $$

  Soit $i_{0} \in \iset{1,n}$ fixé quelconque.

  $$
  \begin{align*}
      e_{i_{0}}^{*}(x) &= e_{i_{0}}^{*}\left(\sum_{i=1}^{n}\lambda_{i}\cdot e_{i}\right) \\
  &= \sum_{i=1}^{n}\lambda_{i}\cdot e_{i_{0}}^{*}(e_{i}) \\
  &= \lambda
  \end{align*}
  $$

- Soit $\varphi \in E^{*}$ fixée quelconque. $(e_{1}^{*}, \ldots, e_{n}^{*})$ est une base de $E$ donc il existe $\mu_{1}, \ldots, \mu_{n}$ des scalaires tels que

  $$
      \varphi = \sum_{i=1}^{n} \mu_{i}\cdot e_{i}^{*}
  $$

  Soit $i_{0} \in \iset{1,n}$ fixé quelconque. Évaluons $\varphi$ en $e_{i_{0}}$ :

  $$
      \begin{align*}
          \varphi(e_{i_{0}}) &= \left(\sum_{i=1}^{n}\mu_{i}\cdot e_{i}^*\right)(e_{i_{0}}) \\
                             &= \sum_{i=1}^{n}\mu_{i}\cdot \underbrace{e_{i}^*(e_{i_{0}})}_{\delta_{i_{0}, i}} = \mu_{i_{0}}
      \end{align*}
  $$

  Ainsi, $\varphi = \displaystyle\sum_{i=1}^{n}\varphi(e_{i})\cdot e_{i}^{*}$.
