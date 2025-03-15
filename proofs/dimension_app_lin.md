---
title: Dimension de l’ensemble des application linéaires entre deux ensembles finis
authors:
  - Félix Rondeau
date: 15/03/2025
pid: 1742060866
tags:
  - algèbre linéaire
---

Si $E$ et $F$ sont deux $\K$-espaces vectoriels de dimension finie, alors $\L_{\K}(E,F)$ est de dimension finie et

$$
    \dim_{\K}\L_{\K}(E,F) = \dim_{\K}E \times \dim_{\K}F
$$

---

- si $E=\{0_{E}\}$, $\L_{\K}(E,F)=\{0_{\L_{\K}(E,F)}\}$ qui est bien de dimension finie égale à $0=\underbrace{\dim_{\K}E}_{=0} \times \dim_{\K}F$.
- si $F=\{0_{F}\}$, on a de même $\L_{\K}(E,F)=\{0_{\L_{\K}(E,F)}\}$.
- sinon, $E\neq\{0_{E}\}$ et $F \neq \{0_{F}\}$, ce qui permet en posant $n=\dim_\K E\in\N^{*}$ et $p=\dim_{\K}F\in\N^{*}$ de choisir $(e_{1},\dots, e_{n})$ une base de $E$ et $(f_{1},\dots, f_{p})$ une base de $F$. Considérons l’application

  $$
      \psi : \begin{array}{rcl}
          \L_{\K}(E,F) & \longrightarrow & F^{n} \\
          g & \longmapsto & (g(e_{1}), \dots, g(e_{n}))
      \end{array}
  $$

  - _C’est une application linéaire :_ soient $(g,h,\lambda)\in\L_{\K}(E,F)^{2} \times \K$.

  $$
      \begin{align*}
          \psi(\lambda g+h) &= \left((\lambda g+h)(e_{1}), \dots, (\lambda g+h)(e_{n})\right) \\
                            &= (\lambda g(e_{1}) + h(e_{1}),\dots , \lambda g(e_{1})+h(e_{1})) \\
                            &= \lambda(g(e_{1}),\dots, g(e_{n})) + (h(e_{1}),\dots,h(e_{n})) \\
                            &= \lambda \psi(g) + \psi(h)
      \end{align*}
  $$

  - _C’est une bijection :_ pour tout n-uplet $(y_{1},\dots,y_{n})\in F^{n}$, il existe une unique application linéaire $g$ de $E$ dans $F$ telle que $\forall i\in\iset{1,n}, g(e_{i})=y_{i}$ car $(e_{1},\dots, e_{n})$ est une base de $E$.

Ainsi, $\psi$ est un isomorphisme de $\L_{\K}(E,F)$ sur $F^{n}$ qui est de dimension finie donc $\L_{\K}(E,F)$ est de dimension finie et

$$
    \dim_{\K}\L_{\K}(E,F) = \dim_{\K}F^{n} = n\dim_{\K}F = \dim_{\K}F \times \dim_{\K}E
$$
