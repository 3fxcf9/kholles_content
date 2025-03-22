---
title: Lien entre la compositions d’application linéaires et la multiplication matricielle
authors:
  - Félix Rondeau
date: 22/03/2025
pid: 1742662334
tags:
  - algèbre linéaire
  - matrices
---

Soient $E, F$ et $G$ trois $\K$-espaces vectoriels de dimensions finies respectives $(p,q,r) \in {\N^{*}}^{3}$.
Soient $\B_{E}, \B_{F}$ et $\B_{G}$ trois bases respectives des espaces vectoriels $E,F$ et $G$.
Soient $u \in \L_{\K}(E,F)$ et $v \in \L_{\K}(F,G)$. Alors

$$
    \mat(v\circ u,\B_{E}, \B_{G}) = \mat(v,\B_{F}, \B_{G})\mat(u,\B_{E}, \B_{F})
$$

---

Soit $X \in \M_{p,1}(\K)$ fixé quelconque. Soit $x$ tel que $X=\mat(x,\B_{E})$.
Posons $Y=\mat(u(x), \B_{F})$, $Y=\mat((v\circ u)(x), \B_{G})$, $U=\mat(u, \B_{E}, \B_{F})$, $V=\mat(v, \B_{F}, \B_{G})$ et $W=\mat(v\circ u, \B_{E}, \B_{G})$.

Alors

$$
    Y=UX \quad\text{et}\quad Z=WX
$$

et par ailleurs

$$
    \begin{align*}
        Z &= \mat((v\circ u)(x), \B_{G}) \\
        &= \mat(v(u(x)), \B_{G}) \\
&= \mat(v,\B_{F},\B_{G})\times \mat(u(x),\B_{F}) \\
&= VY \\
&= VUX
    \end{align*}
$$

par conséquent,

$$
    WX = VUX
$$

Ce résultat étant valable pour tout $X \in \M_{p,1}(\K)$, appliqué pour chacun des matrices de la base canonique, il permet de conclure que

$$
    W=VU
$$
