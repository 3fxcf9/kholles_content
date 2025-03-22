---
title: Caractérisation des hyperplans vectoriels en dimension finie
authors:
  - Félix Rondeau
date: 22/03/2025
pid: 1742662329
tags:
  - algèbre linéaire
---

Soient $E$ un $\K$-espace vectoriel de dimension finie $n \in \N^{*}$. Les propositions suivantes sont équivalentes :

- $H$ est un hyperplan de $E$
- $H$ est de dimension $n-1$
- $H$ admet une droite vectorielle comme supplémentaire

---

- $\bigl((i)\implies (ii)\bigr)$ Si $H$ est un hyperplan, il existe une forme linéaire $\varphi$ non nulle dont $H$ est le noyau. $\varphi$ étant de rang 1, le théorème du rang donne

  $$
      \dim_{\K} H = \dim_{\K} \Ker \varphi = -\rg \varphi + \dim_{\K} E = n-1
  $$

- $\bigl((ii)\implies (iii)\bigr)$ Soit $H$ un sous-espace vectoriel de $E$ de dimension $n-1$. D’après le théorème d’existence d’un supplémentaire en dimension finie, il existe un sous-espace vectoriel $D$ de $E$ tel que

  $$
      E = H\oplus D
  $$

  En prenant la dimension,

  $$
      n=\underbrace{\dim_{\K} H}_{=n-1} + \dim_{\K} D
  $$

  donc $\dim_{\K} D = 1$. Le théorème d’existence d’une base donne l’existence d’une base $\{a\}$ de $D$. Ainsi

  $$
      E = H\oplus \Vect\left\{a\right\}
  $$

- $\bigl((iii)\implies (i)\bigr)$ Notons $(h1,\ldots, h_{n-1})$ une base de $H$, et $(a)$ une base de $\Vect\left\{a\right\}$. Alors $(h1,\ldots , h_{n-1}, a)$ est une base de $E$. Considérons la forme linéaire $a^{*}$ de la base duale $(h_{1}^{*}, \ldots , h_{n-1}^{*}, a^{*})$ de $(h_{1}, \ldots , h_{n+1}, a)$. Alors

  - $a^{*} \in E^{*}$
  - $a^{*} \neq 0_{E^{*}}$ car $a^{*}(a) = 1$
  - Soit $x \in E$ fixé quelconque.

  $$
      \begin{align*}
          x \in \Ker a^{*} &\iff a^{*}(x) = 0_{\K} \\
          &\iff x=\sum_{i=1}^{n-1} h_{i}^{*} \cdot h_{i} + 0_{\K}\cdot a \\
          &\iff x \in H
      \end{align*}
  $$

  Ainsi $H=\Ker a^{*}$ ce qui conclut la preuve.
